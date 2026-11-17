# Source and formulation review: bacillus_schlegelii_heterotrophic_medium (CultureMech:004664)

- Review: 20261021T220330Z-culturemech-004664-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T21:51:50Z
- Finished UTC: 2026-10-21T22:03:30Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 260 adds 3 mL of separately prepared SL-6. The maintained DSMZ owner restores that boundary and procedure, while generated/KOMODO records retain seven stock concentrations as direct medium concentrations. Nickel hexahydrate grounding and provider cobalt/nickel molarity need correction; historical medium 260 response authentication remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 383; batch 039 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-eight task batches contain 380 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 383 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004664 | data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml | generated | bacillus_schlegelii_heterotrophic_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004664 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004664 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/383/strict.tsv |
| validate-terms | passed | True | CultureMech:004664 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004664 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004664 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive260api | unavailable | False | CultureMech:004664 | Preserved optional current access limitation for mediadive260api; primary/stock evidence remains usable. |
| Exact source content access: mediadive260api_retry | unavailable | False | CultureMech:004664 | Preserved optional current access limitation for mediadive260api_retry; primary/stock evidence remains usable. |
| Exact source content access: mediadive27api | unavailable | False | CultureMech:004664 | Preserved optional current access limitation for mediadive27api; primary/stock evidence remains usable. |
| Exact source content access: mediadive27api_retry | unavailable | False | CultureMech:004664 | Preserved optional current access limitation for mediadive27api_retry; primary/stock evidence remains usable. |
| Exact source content access: komodo260detail | unavailable | False | CultureMech:004664 | Preserved optional current access limitation for komodo260detail; primary/stock evidence remains usable. |
| Historical medium 260 raw authentication | unavailable | True | CultureMech:004664 | Exact cited 96b77f81… response was not recovered by the bounded ignored-inclusive owned report/raw search. Nineteen decoded plan matches cannot authenticate that original response or its declared receiving normalization. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004664.

The four documented recipes completed; interpret the scope of each separately.

### Exact recipient and stock identities

identity: supported. Targets: CultureMech:004664.

CultureMech:004664 is the KOMODO/generated target and CultureMech:001359 the maintained DSMZ 260 source. Parent SOURCE_DUPLICATE links resolve, but their old identical-signature prose is stale after the DSMZ stock repair. SL-6 is solution 25; DSMZ 27 contributes only its named subsection.

### Layer-specific stock and preparation recovery

completeness: concern. Targets: CultureMech:004664.

DSMZ owner already has nine main solutes, main water, 3 mL SL-6 and its eight-member composition, plus full receiving preparation. Target/KOMODO are still flat and omit water/dose/procedure. Parent DSMZ 27 1 mL dose, Fe-citrate/B12/resazurin, pH 6.8, nitrogen and light are explicitly excluded. Quantity coverage of that dependency is only solutions[2].composition; its other amounts are not receiving-medium additions.

### Canonical keys versus supplied forms and provider identities

grounding: concern. Targets: CultureMech:004664.

All target primary and current secondary slots are populated (16/16 each), but linkage completeness does not establish chemical correctness. Nickel CHEBI:34887 has Cl2Ni, inconsistent with the printed hexahydrate. Exact current CHEBI-based secondary rows are inventoried separately from provider compound/solution IDs. The parent cobalt note about dichloride is historical wording; its current hexahydrate ID is correct.

### Undefined mixture and selected solid branch

scope: concern. Targets: CultureMech:004664.

Ferric ammonium citrate is explicitly an indefinite-composition mixture, so an unqualified DEFINED composition claim is unsupported; retain known quantitative ingredients and assess a partly defined classification rather than inventing a supplier formula. Optional agar supports the selected solid branch. Catalog aerobic false and medium title do not demonstrate an anaerobic requirement or organism growth.

### Current exact stock raw versus unavailable historical receiving raw

evidence: concern. Targets: CultureMech:004664.

Nineteen DSMZ-owner amount objects cite the unavailable October 7 medium 260 response 96b77f81…; decoded plan equality is derivative correspondence only. Eight standalone stock objects match current exact raw/hash eaab23d6… . Same-hash current primary PDFs authenticate those PDF representations, not the missing old API. Keep old access times and current reuse times distinct.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:004664.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:004664.

27 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Na2HPO4 x 2 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "Na2HPO4 x 2 H2O 4.50 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 4.5,
      "literal_unit": "g",
      "existing_nominal_g_L": 4.5,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "KH2PO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "KH2PO4 1.50 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 1.5,
      "literal_unit": "g",
      "existing_nominal_g_L": 1.5,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NH4Cl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "NH4Cl 1.00 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 1,
      "literal_unit": "g",
      "existing_nominal_g_L": 1,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "MnSO4 x H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "MnSO4 x H2O 0.01 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 0.01,
      "literal_unit": "g",
      "existing_nominal_g_L": 0.01,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "MgSO4 x 7 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "MgSO4 x 7 H2O 0.20 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 0.2,
      "literal_unit": "g",
      "existing_nominal_g_L": 0.2,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "CaCl2 x 2 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "CaCl2 x 2 H2O 0.01 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 0.01,
      "literal_unit": "g",
      "existing_nominal_g_L": 0.01,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Ferric ammonium citrate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "Ferric ammonium citrate 5.00 mg",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 5,
      "literal_unit": "mg",
      "existing_nominal_g_L": 0.005,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral after 5 mg = 0.005 g conversion. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Na-pyruvate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "Na-Pyruvate 1.50 g",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 1.5,
      "literal_unit": "g",
      "existing_nominal_g_L": 1.5,
      "stage": "main printed batch",
      "optional": false,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Optional agar",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main table / optional agar sentence",
        "exact_source_quote": "Agar if necessary 15.0 g.",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "literal_amount": 15,
      "literal_unit": "g",
      "existing_nominal_g_L": 15,
      "stage": "main printed batch",
      "optional": true,
      "measured_final_volume": null
    },
    "rationale": "Exact source batch mass matches the nominal numeral. Historical provider 1000 mL normalization is not independently authenticated; retain that distinction instead of asserting a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports the selected solid branch only."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "amount_mL": 1000,
      "stage": "main water input"
    },
    "rationale": "The maintained owner already stores correct 1 L batch water. Restore missing water in other layers without treating water plus 3 mL stock as a measured final volume."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "SL-6 receiving aliquot",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.003",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 table; see medium 27",
        "exact_source_quote": "Trace element solution SL-6 3.00 ml",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "amount_mL": 3,
      "amount_L": 0.003,
      "stage": "add SL-6 to main batch"
    },
    "rationale": "Current primary directly supports the existing DSMZ dose. The parent DSMZ 27 dose of 1 mL is excluded. No final-medium concentration is calculated."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL-6 ZnSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "0.10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\": \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.347752,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.1,
      "provider_stock_g_L": 0.1,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "SL-6 MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "MnCl2 x 4 H2O 0.03 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.151588,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.03,
      "provider_stock_g_L": 0.03,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-6 H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "0.30",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "H3BO3 0.30 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.3,\n                \"unit\": \"g\",\n                \"g_l\": 0.3,\n                \"mmol_l\": 4.85123,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.3,
      "provider_stock_g_L": 0.3,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-6 CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[3].concentration",
        "stored": {
          "value": "0.20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "CoCl2 x 6 H2O 0.20 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.2,
      "provider_stock_g_L": 0.2,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-6 CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "CuCl2 x 2 H2O 0.01 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0586569,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.01,
      "provider_stock_g_L": 0.01,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-6 NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[5].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 0.02 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\": \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.02,
      "provider_stock_g_L": 0.02,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-6 Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore stock scope; do not retain as a direct final-medium rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Correct existing stock scope; cited medium raw remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "rationale": "Attached exact solution 25 raw/hash matches this mass rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 subsection",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.03 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.123993,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "amount_g": 0.03,
      "provider_stock_g_L": 0.03,
      "provider_stock_volume_mL": 1000,
      "stage": "SL-6 stock only"
    },
    "rationale": "All seven stock masses agree across primary and current stock API. Correct generated/KOMODO scope while retaining repaired DSMZ nesting; quantitative evidence does not validate chemical form or provider mmol/L."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-6 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml",
        "field_path": "solutions[2].composition[7].concentration",
        "stored": {
          "value": "1000.00",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "Page 1 SL-6 final row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      },
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "water_input_mL": 1000,
      "provider_stock_volume_mL": 1000
    },
    "rationale": "DSMZ and standalone definitions correctly retain 1 L; parent 1000 ML_PER_L is stock-normalization notation. Record literal water input and API-declared volume separately, without inferring primary final-volume make-up."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Standalone placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.name",
        "exact_source_quote": "\"name\": \"Trace element solution SL-6\"",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      }
    ],
    "proposed_source_representation": {
      "placeholder_quantity": null
    },
    "rationale": "VARIABLE See source for composition and the incomplete-composition flag are stale alongside populated composition; they are not another ingredient or dose."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Main pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without agitation at 65°C.",
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.1,
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.1,
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.1,
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "Adjust pH to 7.1.",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "pH": 7.1
    },
    "rationale": "Source instruction is specific to DSMZ 260. Preserve the maintained owner’s existing text and add source-scoped preparation to stale layers. Incubation instruction is not a strain-specific growth assertion."
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Dispensing",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without agitation at 65°C.",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "Distribute in 30 - 50 ml amounts in",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "aliquot_range_mL": [
        30,
        50
      ],
      "vessel": "Erlenmeyer flask"
    },
    "rationale": "Source instruction is specific to DSMZ 260. Preserve the maintained owner’s existing text and add source-scoped preparation to stale layers. Incubation instruction is not a strain-specific growth assertion."
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Sterilization duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without agitation at 65°C.",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "sterilize for 15 minutes",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "duration_min": 15
    },
    "rationale": "Source instruction is specific to DSMZ 260. Preserve the maintained owner’s existing text and add source-scoped preparation to stale layers. Incubation instruction is not a strain-specific growth assertion."
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Sterilization temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without agitation at 65°C.",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "at 121C.",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121
    },
    "rationale": "Source instruction is specific to DSMZ 260. Preserve the maintained owner’s existing text and add source-scoped preparation to stale layers. Incubation instruction is not a strain-specific growth assertion."
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Incubation temperature and agitation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without agitation at 65°C.",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz260",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "65C.",
        "snapshot_sha256": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
        "parsed_text_sha256": "400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6",
        "accessed_at": "2026-10-21T20:56:16.187302Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 65,
      "agitation": "without agitation"
    },
    "rationale": "Source instruction is specific to DSMZ 260. Preserve the maintained owner’s existing text and add source-scoped preparation to stale layers. Incubation instruction is not a strain-specific growth assertion."
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Cobalt hexahydrate provider molarity",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[3].evidence[0].snippet",
        "stored": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "decision": "unsupported",
        "rationale": "Retain historical quote unchanged; do not endorse its mmol_l."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[3].evidence[0].snippet",
        "stored": "{\n                \"recipe_order\": 4,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\": 0\n            }",
        "decision": "unsupported",
        "rationale": "Exact raw authentication does not establish arithmetic correctness."
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      },
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "SL-6 supplied hydrate row",
        "exact_source_quote": "CoCl2 x 6 H2O 0.20 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      }
    ],
    "proposed_source_representation": {
      "provider_mmol_L": 1.54037,
      "hydrate_formula_mass_g_mol": 237.929,
      "calculated_stock_mmol_L": 0.8405868977720244,
      "calculation": "g/L * 1000 / supplied-hydrate formula mass",
      "receiving_molarity": null
    },
    "rationale": "Provider molarity corresponds approximately to anhydrous chloride, contrary to its hexahydrate name. Retain mass quantities; label this calculation and reject copying the provider molarity as verified. Nickel mass adds six water formula masses to the pinned anhydrous term; cobalt uses the pinned hexahydrate mass."
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Nickel hexahydrate provider molarity",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
        "field_path": "solutions[0].composition[5].evidence[0].snippet",
        "stored": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "decision": "unsupported",
        "rationale": "Retain historical quote unchanged; do not endorse its mmol_l."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[5].evidence[0].snippet",
        "stored": "{\n                \"recipe_order\": 6,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\": \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\": 0\n            }",
        "decision": "unsupported",
        "rationale": "Exact raw authentication does not establish arithmetic correctness."
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution25",
        "source_url": "https://mediadive.dsmz.de/rest/solution/25",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\": \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c",
        "accessed_at": "2026-10-21T11:55:47.053559Z"
      },
      {
        "source_key": "dsmz27",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
        "source_locator": "SL-6 supplied hydrate row",
        "exact_source_quote": "NiCl2 x 6 H2O 0.02 g",
        "snapshot_sha256": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
        "parsed_text_sha256": "b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af",
        "accessed_at": "2026-10-21T12:24:57.446428Z"
      }
    ],
    "proposed_source_representation": {
      "provider_mmol_L": 0.154322,
      "hydrate_formula_mass_g_mol": 237.689,
      "calculated_stock_mmol_L": 0.08414356575188588,
      "calculation": "g/L * 1000 / supplied-hydrate formula mass",
      "receiving_molarity": null
    },
    "rationale": "Provider molarity corresponds approximately to anhydrous chloride, contrary to its hexahydrate name. Retain mass quantities; label this calculation and reject copying the provider molarity as verified. Nickel mass adds six water formula masses to the pinned anhydrous term; cobalt uses the pinned hexahydrate mass."
  }
]

## Findings

### f1: Seven SL-6 rates remain at the wrong receiving scope

blocker / open / confirmed; issue key: culturemech.004664.stock-flattening.

Target/KOMODO store all seven stock g/L values as direct medium ingredients and omit the 3 mL aliquot and water. The maintained DSMZ owner has already repaired this topology.

### f2: SL-6 nickel hexahydrate uses an anhydrous identifier

major / open / confirmed; issue key: culturemech.004664.nickel-hydrate.

The source NiCl2 x 6 H2O is linked to CHEBI:34887 Cl2Ni in target, both owners, standalone stock and parent SL-6. Correct canonical labels do not resolve this supplied-form mismatch.

### f3: Historical receiving claims and provider molarity need explicit limits

major / open / confirmed; issue key: culturemech.004664.historical-and-derived-quantity.

Historical medium 260 raw is unavailable. Current stock raw is authentic but cobalt/nickel mmol_l values disagree with the named hydrated compounds. Original evidence must be preserved with an appended scoped assessment.

### f4: Unqualified defined classification conflicts with ferric ammonium citrate

major / open / confirmed; issue key: culturemech.004664.defined-composition.

The asserted ferric ammonium citrate term explicitly describes an indefinite-composition mixture; exact mass does not define its chemical stoichiometry.

### f5: Stock placeholder and historical metadata are stale

minor / open / confirmed; issue key: culturemech.004664.dependency-metadata.

Standalone SL-6 retains VARIABLE/incomplete-composition despite its populated composition. Target/KOMODO history includes malformed/naive times and duplicate-link prose no longer describes equal current formulas; parent cobalt note is stale relative to its correct current ID.

## Recommended Actions And Acceptance Checks

### a1

Preserve the repaired DSMZ owner; reconcile the KOMODO layer and missing source-scoped preparation before authorized regeneration. Retain stock mass rates without assuming final medium volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve an exact source-form identifier and corresponding current secondary mapping for the supplied hydrate, preserving amount and stock scope. Do not replace correctly grounded cobalt or calcium hydrates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Recover the cited receiving raw or retain partial historical authentication; attach exact primary/stock support and flag provider molarity without rewriting old snippets or transferring unsupported derived values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Review both classification fields using the exact indefinite mixture and selected agar branch; retain known constituents and avoid a guessed supplier formulation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reconcile dependency placeholder/flag and current relationship description; append honest time provenance without inventing missing timezones, preserving all historical events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch039/383/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/383/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml:1:id: CultureMech:004664<br>./data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml:1:id: CultureMech:004664<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch039/source-preflight-bound/383/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 34 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| standalone | data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml; Entire record read; only SL-6 composition transferred | context_only | Exact dependency identity and source-stage boundary; parent receiving dose and all unrelated parent recipe/conditions are excluded. |
| parent-stock | data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml; Entire record read; only SL-6 composition transferred | context_only | Exact dependency identity and source-stage boundary; parent receiving dose and all unrelated parent recipe/conditions are excluded. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf; Entire page: table and preparation | supports | Eight main masses, 3 mL SL-6, 1000 mL water and optional agar; explicit receiving procedure. |
| stock-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf; Trace element solution SL-6 subsection only | supports | Seven stock solutes and water; no DSMZ 27 main dose or culture conditions transfer. |
| stock-api | https://mediadive.dsmz.de/rest/solution/25; $.data.id/name/volume/recipe | supports | Current exact solution 25 raw authenticates its own attached stock claims and declares 1000 mL stock volume. This is distinct from the unavailable historical medium 260 response. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 260 row | supports | KOMODO/DSMZ accession identity only; aerobic false remains catalog metadata. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch039/383/grounding-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| history-inventory | /private/tmp/culturemech-review-work-batch039/383/history-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| chebi144421 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi62947 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62947; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi63675 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi91247 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact pinned current CHEBI preferred-key rows; metadata source commit/hash | context_only | {"CHEBI:144421": [{"label": "Fe(III) citrate", "match_type": "preferred_term", "identifier": "CHEBI:144421", "preferred_term": "Fe(III) citrate", "ontology_id": "CHEBI:144421", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31604": [{"label": "Ferric ammonium citrate", "match_type": "preferred_term", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62947": [{"label": "Ammonium acetate", "match_type": "preferred_term", "identifier": "CHEBI:62947", "preferred_term": "Ammonium acetate", "ontology_id": "CHEBI:62947", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label": "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91247": [{"label": "L-Cysteine HCl", "match_type": "preferred_term", "identifier": "CHEBI:91247", "preferred_term": "L-Cysteine HCl", "ontology_id": "CHEBI:91247", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| writer-0 | scripts/repair_reviewed_medium_stock_boundaries.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact stock-boundary repair validates source identity and preserves main versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe; no parent dose transfer is authorized. Current formulation-aware merger guards incompatible formulas; stale generated flattening is not attributed unconditionally to today’s implementation. |
| writer-1 | scripts/repair_dsmz_27_44_compositions.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact stock-boundary repair validates source identity and preserves main versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe; no parent dose transfer is authorized. Current formulation-aware merger guards incompatible formulas; stale generated flattening is not attributed unconditionally to today’s implementation. |
| writer-2 | scripts/import_mediadive_solutions.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact stock-boundary repair validates source identity and preserves main versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe; no parent dose transfer is authorized. Current formulation-aware merger guards incompatible formulas; stale generated flattening is not attributed unconditionally to today’s implementation. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Exact stock-boundary repair validates source identity and preserves main versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe; no parent dose transfer is authorized. Current formulation-aware merger guards incompatible formulas; stale generated flattening is not attributed unconditionally to today’s implementation. |
| history-metadata | data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml; data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.499891"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.499891"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml", "events": 7, "timestamp_issues": []}] |
| mediadive260api-attempt | https://mediadive.dsmz.de/rest/medium/260; Preserved exact public retrieval result | context_only | Preserved optional current access limitation for mediadive260api; primary/stock evidence remains usable. |
| mediadive260api_retry-attempt | https://mediadive.dsmz.de/rest/medium/260; Preserved exact public retrieval result | context_only | Preserved optional current access limitation for mediadive260api_retry; primary/stock evidence remains usable. |
| mediadive27api-attempt | https://mediadive.dsmz.de/rest/medium/27; Preserved exact public retrieval result | context_only | Preserved optional current access limitation for mediadive27api; primary/stock evidence remains usable. |
| mediadive27api_retry-attempt | https://mediadive.dsmz.de/rest/medium/27; Preserved exact public retrieval result | context_only | Preserved optional current access limitation for mediadive27api_retry; primary/stock evidence remains usable. |
| komodo260detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=260; Preserved exact public retrieval result | context_only | Preserved optional current access limitation for komodo260detail; primary/stock evidence remains usable. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch039/383/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Preserved optional current access limitation for mediadive260api; primary/stock evidence remains usable.
- Preserved optional current access limitation for mediadive260api_retry; primary/stock evidence remains usable.
- Preserved optional current access limitation for mediadive27api; primary/stock evidence remains usable.
- Preserved optional current access limitation for mediadive27api_retry; primary/stock evidence remains usable.
- Preserved optional current access limitation for komodo260detail; primary/stock evidence remains usable.
- Partial completion rests on required historical medium 260 correspondence, not optional current API/KOMODO failure alone. Primary water input is not a measured final volume; no downstream SL-6 concentration is asserted.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T220330Z-culturemech-004664-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_schlegelii_heterotrophic_medium (CultureMech:004664)'
started_at: '2026-10-21T21:51:50Z'
finished_at: '2026-10-21T22:03:30Z'
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
summary: DSMZ 260 adds 3 mL of separately prepared SL-6. The maintained DSMZ owner
  restores that boundary and procedure, while generated/KOMODO records retain seven
  stock concentrations as direct medium concentrations. Nickel hexahydrate grounding
  and provider cobalt/nickel molarity need correction; historical medium 260 response
  authentication remains unavailable.
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
  - path: data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    sha256: 6412adb9a681d57a960bb09d6540d6cf30a62cb7652b989b7cd9fc4895ce4c20
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    sha256: ffcc8b3a2189abf153c7a047fa71dc03f97645b309c953eaf5d87917c5ee823a
    role: context
  - path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    sha256: 15f3c43c7646827c4d90cbc9b4e0ea58bee6667aa87adb7203975ed895cd7a7c
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
    role: context
  - path: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
    sha256: 410329220111086b817fca840e50b4a41a2e3707d4bbe71df786efc17f6e6af0
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml.md
    sha256: 8e94a1a1ef0a866e6cd94a9fe70490c62c2a61c2a06f10ea55effba88a1e3712
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml.md
    sha256: e122ad99c2ce57ef25d4e206493dcc781981abe35fec3caad2492d2cdf8e1443
    role: context
  - path: reports/ingredient_concentration_curation/20261007-medium-stock-boundaries/260.md
    sha256: 42dff831be291420112413806a31ae9536f7632a747520f0ccb380b649804335
    role: context
  - path: reports/ingredient_concentration_curation/20261007-medium-stock-boundaries/plan.json
    sha256: d8acd7bce56a34eb8ea2377bc916db5d1cf40e363be5de5df4a0c436c9a2cb97
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  - path: scripts/repair_dsmz_27_44_compositions.py
    sha256: 1a0a33c0831f3b18c04f60e4c47bc48e152e28c991d7ba74c8b46dd5fea0f011
    role: context
  - path: scripts/repair_reviewed_medium_stock_boundaries.py
    sha256: fafff4038667c35c62bc6c146996d89f67c724fd3d40d3c9f4c0bc320bb599da
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  selection: Task review 383; batch 039 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-eight task batches
    contain 380 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 383 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004664
targets:
- target_id: CultureMech:004664
  path: data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  label: bacillus_schlegelii_heterotrophic_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/383/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/383/strict.tsv"
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004664
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
  - CultureMech:004664
- check_id: mediadive260api-source-access
  name: 'Exact source content access: mediadive260api'
  required: false
  status: unavailable
  summary: Preserved optional current access limitation for mediadive260api; primary/stock
    evidence remains usable.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - mediadive260api-attempt
- check_id: mediadive260api_retry-source-access
  name: 'Exact source content access: mediadive260api_retry'
  required: false
  status: unavailable
  summary: Preserved optional current access limitation for mediadive260api_retry;
    primary/stock evidence remains usable.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - mediadive260api_retry-attempt
- check_id: mediadive27api-source-access
  name: 'Exact source content access: mediadive27api'
  required: false
  status: unavailable
  summary: Preserved optional current access limitation for mediadive27api; primary/stock
    evidence remains usable.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - mediadive27api-attempt
- check_id: mediadive27api_retry-source-access
  name: 'Exact source content access: mediadive27api_retry'
  required: false
  status: unavailable
  summary: Preserved optional current access limitation for mediadive27api_retry;
    primary/stock evidence remains usable.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - mediadive27api_retry-attempt
- check_id: komodo260detail-source-access
  name: 'Exact source content access: komodo260detail'
  required: false
  status: unavailable
  summary: Preserved optional current access limitation for komodo260detail; primary/stock
    evidence remains usable.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - komodo260detail-attempt
- check_id: historical260-raw
  name: Historical medium 260 raw authentication
  required: true
  status: unavailable
  summary: Exact cited 96b77f81… response was not recovered by the bounded ignored-inclusive
    owned report/raw search. Nineteen decoded plan matches cannot authenticate that
    original response or its declared receiving normalization.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - history-inventory
  - primary
  - stock-api
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:17.155595Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/383/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:18.168872Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/383/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:19.291143Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:20.066778Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:03:29Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml:1:id:
    CultureMech:004664

    ./data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml:1:id:
    CultureMech:004664

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/source-preflight-bound/383/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:03:29Z'
  support: supports
  summary: 34 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 470525cbf7a59aae5003e270a9c053e95925fc2172e79c1208c9cfadfbe762cc
- evidence_id: standalone
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
  locator: Entire record read; only SL-6 composition transferred
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact dependency identity and source-stage boundary; parent receiving dose
    and all unrelated parent recipe/conditions are excluded.
  snapshot_sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
- evidence_id: parent-stock
  kind: record_content
  reference: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
  locator: Entire record read; only SL-6 composition transferred
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact dependency identity and source-stage boundary; parent receiving dose
    and all unrelated parent recipe/conditions are excluded.
  snapshot_sha256: 410329220111086b817fca840e50b4a41a2e3707d4bbe71df786efc17f6e6af0
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf
  locator: 'Entire page: table and preparation'
  accessed_at: '2026-10-21T20:56:16.187302Z'
  support: supports
  summary: Eight main masses, 3 mL SL-6, 1000 mL water and optional agar; explicit
    receiving procedure.
  quote: Trace element solution SL-6 3.00 ml
  snapshot_sha256: ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291
- evidence_id: stock-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf
  locator: Trace element solution SL-6 subsection only
  accessed_at: '2026-10-21T12:24:57.446428Z'
  support: supports
  summary: Seven stock solutes and water; no DSMZ 27 main dose or culture conditions
    transfer.
  quote: NiCl2 x 6 H2O 0.02 g
  snapshot_sha256: e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9
- evidence_id: stock-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/25
  locator: $.data.id/name/volume/recipe
  accessed_at: '2026-10-21T11:55:47.053559Z'
  support: supports
  summary: Current exact solution 25 raw authenticates its own attached stock claims
    and declares 1000 mL stock volume. This is distinct from the unavailable historical
    medium 260 response.
  snapshot_sha256: eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 260 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO/DSMZ accession identity only; aerobic false remains catalog metadata.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=260'\
    \ >260</a></TD>\n\t\t\t\t\t<TD>BACILLUS SCHLEGELII HETEROTROPHIC MEDIUM</TD>\n\
    \t\t\t\t\t<TD> 7.1</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\
    \t\t\t\t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/383/grounding-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 276c5dc49082f7bf3476a66ff9d85c213c157a0697723ac4a72a14db66850288
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/383/history-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 289c36cd41c9b213220893af059b456dc254eadf2226d190665fc4dab3b7bae3
- evidence_id: chebi144421
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T13:16:22.419325Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 283ce05a4ff7d7b60c46f1b8447bc5f217ea1d84543f59ad566eb9f893b768a1
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31604
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:44.987529Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 31acf125b469ffd64e2de503550d29336a7a0f99c8a3ea24b80b53bdb715e7f8
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi62947
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62947
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T17:04:23.300088Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: caa2e7e9de39722329ac91e1aa80b75bd295aba5348f48c2380c0ffc0795434b
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63675
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T09:27:41.075057Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 4c54df9f2d63f54dea26d64e4ec9fedeb486c2c2abe44b70c5c621512f1fdd3c
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91247
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T09:27:41.606984Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 8ff9a3639e1afba34c0d40072292486ff792c7b63a496d189a1cfeb2e6574890
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact pinned current CHEBI preferred-key rows; metadata source commit/hash
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: '{"CHEBI:144421": [{"label": "Fe(III) citrate", "match_type": "preferred_term",
    "identifier": "CHEBI:144421", "preferred_term": "Fe(III) citrate", "ontology_id":
    "CHEBI:144421", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31604": [{"label": "Ferric ammonium citrate",
    "match_type": "preferred_term", "identifier": "CHEBI:31604", "preferred_term":
    "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term",
    "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62947": [{"label":
    "Ammonium acetate", "match_type": "preferred_term", "identifier": "CHEBI:62947",
    "preferred_term": "Ammonium acetate", "ontology_id": "CHEBI:62947", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675":
    [{"label": "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675",
    "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O",
    "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91247": [{"label": "L-Cysteine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:91247", "preferred_term": "L-Cysteine HCl", "ontology_id":
    "CHEBI:91247", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258":
    [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258",
    "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_reviewed_medium_stock_boundaries.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact stock-boundary repair validates source identity and preserves main
    versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe;
    no parent dose transfer is authorized. Current formulation-aware merger guards
    incompatible formulas; stale generated flattening is not attributed unconditionally
    to today’s implementation.
  snapshot_sha256: fafff4038667c35c62bc6c146996d89f67c724fd3d40d3c9f4c0bc320bb599da
- evidence_id: writer-1
  kind: record_content
  reference: scripts/repair_dsmz_27_44_compositions.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact stock-boundary repair validates source identity and preserves main
    versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe;
    no parent dose transfer is authorized. Current formulation-aware merger guards
    incompatible formulas; stale generated flattening is not attributed unconditionally
    to today’s implementation.
  snapshot_sha256: 1a0a33c0831f3b18c04f60e4c47bc48e152e28c991d7ba74c8b46dd5fea0f011
- evidence_id: writer-2
  kind: record_content
  reference: scripts/import_mediadive_solutions.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact stock-boundary repair validates source identity and preserves main
    versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe;
    no parent dose transfer is authorized. Current formulation-aware merger guards
    incompatible formulas; stale generated flattening is not attributed unconditionally
    to today’s implementation.
  snapshot_sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Exact stock-boundary repair validates source identity and preserves main
    versus stock quantities. Current DSMZ 27 repair scoped its own receiving recipe;
    no parent dose transfer is authorized. Current formulation-aware merger guards
    incompatible formulas; stale generated flattening is not attributed unconditionally
    to today’s implementation.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml;
    data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml;
    data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:58.499891"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:58.499891"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: mediadive260api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/260
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.847495Z'
  support: context_only
  summary: Preserved optional current access limitation for mediadive260api; primary/stock
    evidence remains usable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive260api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/260
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:57:44.840039Z'
  support: context_only
  summary: Preserved optional current access limitation for mediadive260api_retry;
    primary/stock evidence remains usable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive27api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/27
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.860272Z'
  support: context_only
  summary: Preserved optional current access limitation for mediadive27api; primary/stock
    evidence remains usable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive27api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/27
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:57:44.845375Z'
  support: context_only
  summary: Preserved optional current access limitation for mediadive27api_retry;
    primary/stock evidence remains usable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo260detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=260
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.547258Z'
  support: context_only
  summary: Preserved optional current access limitation for komodo260detail; primary/stock
    evidence remains usable.
  snapshot_sha256: 22d84ff0e550dba380afa5fc557c49af8c0882a90371b477d4bba02699aa0eb8
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/383/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:03:29Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 80666d071334d070797b265818d96b4183723e5a86126be5b8c985170b42ca27
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact recipient and stock identities
  outcome: supported
  summary: CultureMech:004664 is the KOMODO/generated target and CultureMech:001359
    the maintained DSMZ 260 source. Parent SOURCE_DUPLICATE links resolve, but their
    old identical-signature prose is stale after the DSMZ stock repair. SL-6 is solution
    25; DSMZ 27 contributes only its named subsection.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - primary
  - stock-primary
  - stock-api
  - catalog
  - standalone
  - parent-stock
- assessment_id: stock-boundary
  area: completeness
  topic: Layer-specific stock and preparation recovery
  outcome: concern
  summary: DSMZ owner already has nine main solutes, main water, 3 mL SL-6 and its
    eight-member composition, plus full receiving preparation. Target/KOMODO are still
    flat and omit water/dose/procedure. Parent DSMZ 27 1 mL dose, Fe-citrate/B12/resazurin,
    pH 6.8, nitrogen and light are explicitly excluded. Quantity coverage of that
    dependency is only solutions[2].composition; its other amounts are not receiving-medium
    additions.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - primary
  - stock-primary
  - stock-api
  - record
  - owner-0
  - owner-1
  - quantity-inventory
- assessment_id: grounding
  area: grounding
  topic: Canonical keys versus supplied forms and provider identities
  outcome: concern
  summary: All target primary and current secondary slots are populated (16/16 each),
    but linkage completeness does not establish chemical correctness. Nickel CHEBI:34887
    has Cl2Ni, inconsistent with the printed hexahydrate. Exact current CHEBI-based
    secondary rows are inventoried separately from provider compound/solution IDs.
    The parent cobalt note about dichloride is historical wording; its current hexahydrate
    ID is correct.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - grounding-inventory
  - mim
  - stock-primary
  - stock-api
  - chebi34887
  - chebi53503
  - chebi86158
- assessment_id: classification
  area: scope
  topic: Undefined mixture and selected solid branch
  outcome: concern
  summary: Ferric ammonium citrate is explicitly an indefinite-composition mixture,
    so an unqualified DEFINED composition claim is unsupported; retain known quantitative
    ingredients and assess a partly defined classification rather than inventing a
    supplier formula. Optional agar supports the selected solid branch. Catalog aerobic
    false and medium title do not demonstrate an anaerobic requirement or organism
    growth.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - record
  - primary
  - catalog
  - chebi31604
- assessment_id: history-source
  area: evidence
  topic: Current exact stock raw versus unavailable historical receiving raw
  outcome: concern
  summary: Nineteen DSMZ-owner amount objects cite the unavailable October 7 medium
    260 response 96b77f81…; decoded plan equality is derivative correspondence only.
    Eight standalone stock objects match current exact raw/hash eaab23d6… . Same-hash
    current primary PDFs authenticate those PDF representations, not the missing old
    API. Keep old access times and current reuse times distinct.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - history-inventory
  - primary
  - stock-primary
  - stock-api
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 27 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:004664
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Na2HPO4 x 2 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"Na2HPO4 x 2 H2O 4.50 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 4.5,\n \
    \     \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 4.5,\n      \"\
    stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n\
    \    \"component_or_context\": \"KH2PO4\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 1.50 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 1.5,\n \
    \     \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 1.5,\n      \"\
    stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n\
    \    \"component_or_context\": \"NH4Cl\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"NH4Cl 1.00 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 1,\n   \
    \   \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 1,\n      \"stage\"\
    : \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n\
    \    \"component_or_context\": \"MnSO4 x H2O\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"MnSO4 x H2O 0.01 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 0.01,\n\
    \      \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 0.01,\n     \
    \ \"stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n\
    \    \"component_or_context\": \"MgSO4 x 7 H2O\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.20 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 0.2,\n \
    \     \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 0.2,\n      \"\
    stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n\
    \    \"component_or_context\": \"CaCl2 x 2 H2O\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.01 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 0.01,\n\
    \      \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 0.01,\n     \
    \ \"stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n\
    \    \"component_or_context\": \"Ferric ammonium citrate\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"Ferric ammonium citrate 5.00 mg\",\n    \
    \    \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 5,\n   \
    \   \"literal_unit\": \"mg\",\n      \"existing_nominal_g_L\": 0.005,\n      \"\
    stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral after 5 mg = 0.005 g conversion. Historical provider 1000 mL normalization\
    \ is not independently authenticated; retain that distinction instead of asserting\
    \ a measured final litre. Existing DSMZ evidence is derivative-only; target/KOMODO\
    \ have none. Optional agar supports the selected solid branch only.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"Na-pyruvate\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"Na-Pyruvate 1.50 g\",\n        \"snapshot_sha256\"\
    : \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\",\n    \
    \    \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 1.5,\n \
    \     \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 1.5,\n      \"\
    stage\": \"main printed batch\",\n      \"optional\": false,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n\
    \    \"component_or_context\": \"Optional agar\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table / optional agar sentence\"\
    ,\n        \"exact_source_quote\": \"Agar if necessary 15.0 g.\",\n        \"\
    snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"literal_amount\": 15,\n  \
    \    \"literal_unit\": \"g\",\n      \"existing_nominal_g_L\": 15,\n      \"stage\"\
    : \"main printed batch\",\n      \"optional\": true,\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Exact source batch mass matches the nominal\
    \ numeral. Historical provider 1000 mL normalization is not independently authenticated;\
    \ retain that distinction instead of asserting a measured final litre. Existing\
    \ DSMZ evidence is derivative-only; target/KOMODO have none. Optional agar supports\
    \ the selected solid branch only.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n\
    \    \"component_or_context\": \"Main water\",\n    \"decision\": \"add\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_mL\": 1000,\n     \
    \ \"stage\": \"main water input\"\n    },\n    \"rationale\": \"The maintained\
    \ owner already stores correct 1 L batch water. Restore missing water in other\
    \ layers without treating water plus 3 mL stock as a measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"SL-6\
    \ receiving aliquot\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 table; see medium 27\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-6 3.00 ml\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_mL\": 3,\n      \"\
    amount_L\": 0.003,\n      \"stage\": \"add SL-6 to main batch\"\n    },\n    \"\
    rationale\": \"Current primary directly supports the existing DSMZ dose. The parent\
    \ DSMZ 27 dose of 1 mL is excluded. No final-medium concentration is calculated.\"\
    \n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\": \"SL-6\
    \ ZnSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.10\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 7 H2O 0.10 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"ZnSO4 x 7 H2O\\\",\\n                \\\"compound_id\\\": 35,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.1,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.347752,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.1,\n      \"\
    provider_stock_g_L\": 0.1,\n      \"provider_stock_volume_mL\": 1000,\n      \"\
    stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock masses\
    \ agree across primary and current stock API. Correct generated/KOMODO scope while\
    \ retaining repaired DSMZ nesting; quantitative evidence does not validate chemical\
    \ form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"\
    component_or_context\": \"SL-6 MnCl2 x 4 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 0.03 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"MnCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 36,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.03,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.03,\\n                \\\"mmol_l\\\
    \": 0.151588,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.03,\n      \"\
    provider_stock_g_L\": 0.03,\n      \"provider_stock_volume_mL\": 1000,\n     \
    \ \"stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock\
    \ masses agree across primary and current stock API. Correct generated/KOMODO\
    \ scope while retaining repaired DSMZ nesting; quantitative evidence does not\
    \ validate chemical form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q14\",\n    \"component_or_context\": \"SL-6 H3BO3\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.30\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"H3BO3 0.30 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"H3BO3\\\",\\n                \\\"compound_id\\\": 37,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 0.3,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 0.3,\\n                \\\"mmol_l\\\": 4.85123,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\",\n    \
    \    \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"amount_g\": 0.3,\n      \"provider_stock_g_L\"\
    : 0.3,\n      \"provider_stock_volume_mL\": 1000,\n      \"stage\": \"SL-6 stock\
    \ only\"\n    },\n    \"rationale\": \"All seven stock masses agree across primary\
    \ and current stock API. Correct generated/KOMODO scope while retaining repaired\
    \ DSMZ nesting; quantitative evidence does not validate chemical form or provider\
    \ mmol/L.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"SL-6 CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock scope;\
    \ do not retain as a direct final-medium rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.20\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 0.20 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.2,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\
    \": 1.54037,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.2,\n      \"\
    provider_stock_g_L\": 0.2,\n      \"provider_stock_volume_mL\": 1000,\n      \"\
    stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock masses\
    \ agree across primary and current stock API. Correct generated/KOMODO scope while\
    \ retaining repaired DSMZ nesting; quantitative evidence does not validate chemical\
    \ form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"\
    component_or_context\": \"SL-6 CuCl2 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 0.01 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"CuCl2 x 2 H2O\\\",\\n                \\\"compound_id\\\": 39,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.01,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.01,\\n                \\\"mmol_l\\\
    \": 0.0586569,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.01,\n      \"\
    provider_stock_g_L\": 0.01,\n      \"provider_stock_volume_mL\": 1000,\n     \
    \ \"stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock\
    \ masses agree across primary and current stock API. Correct generated/KOMODO\
    \ scope while retaining repaired DSMZ nesting; quantitative evidence does not\
    \ validate chemical form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q17\",\n    \"component_or_context\": \"SL-6 NiCl2 x 6 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.02 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"NiCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 40,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.02,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\
    \": 0.154322,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.02,\n      \"\
    provider_stock_g_L\": 0.02,\n      \"provider_stock_volume_mL\": 1000,\n     \
    \ \"stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock\
    \ masses agree across primary and current stock API. Correct generated/KOMODO\
    \ scope while retaining repaired DSMZ nesting; quantitative evidence does not\
    \ validate chemical form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q18\",\n    \"component_or_context\": \"SL-6 Na2MoO4 x 2 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore stock\
    \ scope; do not retain as a direct final-medium rate.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Correct existing stock scope; cited medium raw remains unavailable.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"rationale\": \"Attached exact\
    \ solution 25 raw/hash matches this mass rate.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 subsection\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 0.03 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.03,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.03,\\n                \\\"mmol_l\\\
    \": 0.123993,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount_g\": 0.03,\n      \"\
    provider_stock_g_L\": 0.03,\n      \"provider_stock_volume_mL\": 1000,\n     \
    \ \"stage\": \"SL-6 stock only\"\n    },\n    \"rationale\": \"All seven stock\
    \ masses agree across primary and current stock API. Correct generated/KOMODO\
    \ scope while retaining repaired DSMZ nesting; quantitative evidence does not\
    \ validate chemical form or provider mmol/L.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q19\",\n    \"component_or_context\": \"SL-6 water\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n    \
    \    \"decision\": \"verified\",\n        \"rationale\": \"\"\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1000.00\",\n          \"unit\": \"\
    ML_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-6 final row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      },\n      {\n\
    \        \"source_key\": \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\"\
    ,\n        \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_input_mL\": 1000,\n\
    \      \"provider_stock_volume_mL\": 1000\n    },\n    \"rationale\": \"DSMZ and\
    \ standalone definitions correctly retain 1 L; parent 1000 ML_PER_L is stock-normalization\
    \ notation. Record literal water input and API-declared volume separately, without\
    \ inferring primary final-volume make-up.\"\n  },\n  {\n    \"quantity_id\": \"\
    q20\",\n    \"component_or_context\": \"Standalone placeholder\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution25\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/25\"\
    ,\n        \"source_locator\": \"$.data.name\",\n        \"exact_source_quote\"\
    : \"\\\"name\\\": \\\"Trace element solution SL-6\\\"\",\n        \"snapshot_sha256\"\
    : \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\",\n    \
    \    \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"placeholder_quantity\": null\n  \
    \  },\n    \"rationale\": \"VARIABLE See source for composition and the incomplete-composition\
    \ flag are stale alongside populated composition; they are not another ingredient\
    \ or dose.\"\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Main pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts\
    \ in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without\
    \ agitation at 65°C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.1,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.1,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.1,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz260\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.1.\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH\": 7.1\n    },\n    \"\
    rationale\": \"Source instruction is specific to DSMZ 260. Preserve the maintained\
    \ owner’s existing text and add source-scoped preparation to stale layers. Incubation\
    \ instruction is not a strain-specific growth assertion.\"\n  },\n  {\n    \"\
    quantity_id\": \"q22\",\n    \"component_or_context\": \"Dispensing\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n     \
    \   \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts\
    \ in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without\
    \ agitation at 65°C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Distribute in 30 - 50 ml amounts in\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"aliquot_range_mL\": [\n  \
    \      30,\n        50\n      ],\n      \"vessel\": \"Erlenmeyer flask\"\n   \
    \ },\n    \"rationale\": \"Source instruction is specific to DSMZ 260. Preserve\
    \ the maintained owner’s existing text and add source-scoped preparation to stale\
    \ layers. Incubation instruction is not a strain-specific growth assertion.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\": \"Sterilization\
    \ duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts\
    \ in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without\
    \ agitation at 65°C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"sterilize for 15 minutes\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"duration_min\": 15\n    },\n\
    \    \"rationale\": \"Source instruction is specific to DSMZ 260. Preserve the\
    \ maintained owner’s existing text and add source-scoped preparation to stale\
    \ layers. Incubation instruction is not a strain-specific growth assertion.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\": \"Sterilization\
    \ temperature\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts\
    \ in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without\
    \ agitation at 65°C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"at 121C.\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121\n   \
    \ },\n    \"rationale\": \"Source instruction is specific to DSMZ 260. Preserve\
    \ the maintained owner’s existing text and add source-scoped preparation to stale\
    \ layers. Incubation instruction is not a strain-specific growth assertion.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\": \"Incubation\
    \ temperature and agitation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts\
    \ in Erlenmeyer flasks and sterilize for 15 minutes at 121°C. Incubate without\
    \ agitation at 65°C.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz260\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"65C.\",\n        \"snapshot_sha256\": \"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291\"\
    ,\n        \"parsed_text_sha256\": \"400160156a93ea0a3d43544c7168a79844a662a630658fe3cd5d3f81eda6eca6\"\
    ,\n        \"accessed_at\": \"2026-10-21T20:56:16.187302Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 65,\n   \
    \   \"agitation\": \"without agitation\"\n    },\n    \"rationale\": \"Source\
    \ instruction is specific to DSMZ 260. Preserve the maintained owner’s existing\
    \ text and add source-scoped preparation to stale layers. Incubation instruction\
    \ is not a strain-specific growth assertion.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q26\",\n    \"component_or_context\": \"Cobalt hexahydrate provider molarity\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].evidence[0].snippet\"\
    ,\n        \"stored\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 38,\\n                        \\\"amount\\\
    \": 0.2,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.2,\\n                        \\\"mmol_l\\\": 1.54037,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"decision\": \"unsupported\",\n        \"rationale\": \"Retain historical\
    \ quote unchanged; do not endorse its mmol_l.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[3].evidence[0].snippet\",\n        \"\
    stored\": \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\\
    n                \\\"solution\\\": null,\\n                \\\"solution_id\\\"\
    : null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 0.2,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\
    \": 1.54037,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"decision\": \"unsupported\",\n        \"rationale\": \"Exact raw authentication\
    \ does not establish arithmetic correctness.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution25\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/25\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"CoCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 38,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.2,\\n                \\\"unit\\\": \\\"g\\\",\\n     \
    \           \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\": 1.54037,\\n  \
    \              \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\",\n    \
    \    \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      },\n      {\n   \
    \     \"source_key\": \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"SL-6 supplied hydrate row\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 0.20 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"provider_mmol_L\": 1.54037,\n\
    \      \"hydrate_formula_mass_g_mol\": 237.929,\n      \"calculated_stock_mmol_L\"\
    : 0.8405868977720244,\n      \"calculation\": \"g/L * 1000 / supplied-hydrate\
    \ formula mass\",\n      \"receiving_molarity\": null\n    },\n    \"rationale\"\
    : \"Provider molarity corresponds approximately to anhydrous chloride, contrary\
    \ to its hexahydrate name. Retain mass quantities; label this calculation and\
    \ reject copying the provider molarity as verified. Nickel mass adds six water\
    \ formula masses to the pinned anhydrous term; cobalt uses the pinned hexahydrate\
    \ mass.\"\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Nickel hexahydrate provider molarity\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].evidence[0].snippet\"\
    ,\n        \"stored\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 40,\\n                        \\\"amount\\\
    \": 0.02,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.154322,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"decision\": \"unsupported\",\n        \"rationale\": \"Retain historical\
    \ quote unchanged; do not endorse its mmol_l.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[5].evidence[0].snippet\",\n        \"\
    stored\": \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 40,\\\
    n                \\\"solution\\\": null,\\n                \\\"solution_id\\\"\
    : null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 0.02,\\n                \\\"unit\\\
    \": \\\"g\\\",\\n                \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\
    \": 0.154322,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"decision\": \"unsupported\",\n        \"rationale\": \"Exact raw authentication\
    \ does not establish arithmetic correctness.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution25\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/25\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"NiCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 40,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.02,\\n                \\\"unit\\\": \\\"g\\\",\\n    \
    \            \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\": 0.154322,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c\",\n    \
    \    \"accessed_at\": \"2026-10-21T11:55:47.053559Z\"\n      },\n      {\n   \
    \     \"source_key\": \"dsmz27\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf\"\
    ,\n        \"source_locator\": \"SL-6 supplied hydrate row\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.02 g\",\n        \"snapshot_sha256\": \"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9\"\
    ,\n        \"parsed_text_sha256\": \"b415a9395e1d5939bf5a0c1a234a3aa35c252767c9e228110d2f1adaa41728af\"\
    ,\n        \"accessed_at\": \"2026-10-21T12:24:57.446428Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"provider_mmol_L\": 0.154322,\n\
    \      \"hydrate_formula_mass_g_mol\": 237.689,\n      \"calculated_stock_mmol_L\"\
    : 0.08414356575188588,\n      \"calculation\": \"g/L * 1000 / supplied-hydrate\
    \ formula mass\",\n      \"receiving_molarity\": null\n    },\n    \"rationale\"\
    : \"Provider molarity corresponds approximately to anhydrous chloride, contrary\
    \ to its hexahydrate name. Retain mass quantities; label this calculation and\
    \ reject copying the provider molarity as verified. Nickel mass adds six water\
    \ formula masses to the pinned anhydrous term; cobalt uses the pinned hexahydrate\
    \ mass.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.004664.stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Seven SL-6 rates remain at the wrong receiving scope
  description: Target/KOMODO store all seven stock g/L values as direct medium ingredients
    and omit the 3 mL aliquot and water. The maintained DSMZ owner has already repaired
    this topology.
  target_ids:
  - CultureMech:004664
  field_paths:
  - ingredients[9]
  - solutions
  - preparation_steps
  evidence_ids:
  - primary
  - stock-primary
  - owner-1
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
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
  issue_key: culturemech.004664.nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: SL-6 nickel hexahydrate uses an anhydrous identifier
  description: The source NiCl2 x 6 H2O is linked to CHEBI:34887 Cl2Ni in target,
    both owners, standalone stock and parent SL-6. Correct canonical labels do not
    resolve this supplied-form mismatch.
  target_ids:
  - CultureMech:004664
  field_paths:
  - ingredients[14].term
  - solutions[0].composition[5].term
  - composition[5].chebi_term
  evidence_ids:
  - stock-primary
  - grounding-inventory
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
    role: scoped maintained SL-6 dependency
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.004664.historical-and-derived-quantity
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Historical receiving claims and provider molarity need explicit limits
  description: Historical medium 260 raw is unavailable. Current stock raw is authentic
    but cobalt/nickel mmol_l values disagree with the named hydrated compounds. Original
    evidence must be preserved with an appended scoped assessment.
  target_ids:
  - CultureMech:004664
  field_paths:
  - evidence
  - solutions[0].composition
  - references
  evidence_ids:
  - history-inventory
  - stock-api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.004664.defined-composition
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Unqualified defined classification conflicts with ferric ammonium citrate
  description: The asserted ferric ammonium citrate term explicitly describes an indefinite-composition
    mixture; exact mass does not define its chemical stoichiometry.
  target_ids:
  - CultureMech:004664
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - primary
  - chebi31604
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.004664.dependency-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Stock placeholder and historical metadata are stale
  description: Standalone SL-6 retains VARIABLE/incomplete-composition despite its
    populated composition. Target/KOMODO history includes malformed/naive times and
    duplicate-link prose no longer describes equal current formulas; parent cobalt
    note is stale relative to its correct current ID.
  target_ids:
  - CultureMech:004664
  field_paths:
  - ingredients[0].concentration
  - data_quality_flags
  - curation_history
  - parent_media
  - variant_children
  evidence_ids:
  - standalone
  - parent-stock
  - history-inventory
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
    role: scoped maintained SL-6 dependency
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Preserve the repaired DSMZ owner; reconcile the KOMODO layer and missing
    source-scoped preparation before authorized regeneration. Retain stock mass rates
    without assuming final medium volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004664
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
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
  description: Resolve an exact source-form identifier and corresponding current secondary
    mapping for the supplied hydrate, preserving amount and stock scope. Do not replace
    correctly grounded cobalt or calcium hydrates.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004664
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
    role: scoped maintained SL-6 dependency
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
  description: Recover the cited receiving raw or retain partial historical authentication;
    attach exact primary/stock support and flag provider molarity without rewriting
    old snippets or transferring unsupported derived values.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004664
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
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
  description: Review both classification fields using the exact indefinite mixture
    and selected agar branch; retain known constituents and avoid a guessed supplier
    formulation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004664
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
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
  description: Reconcile dependency placeholder/flag and current relationship description;
    append honest time provenance without inventing missing timezones, preserving
    all historical events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:004664
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped maintained SL-6 dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml
    role: scoped maintained SL-6 dependency
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
- Preserved optional current access limitation for mediadive260api; primary/stock
  evidence remains usable.
- Preserved optional current access limitation for mediadive260api_retry; primary/stock
  evidence remains usable.
- Preserved optional current access limitation for mediadive27api; primary/stock evidence
  remains usable.
- Preserved optional current access limitation for mediadive27api_retry; primary/stock
  evidence remains usable.
- Preserved optional current access limitation for komodo260detail; primary/stock
  evidence remains usable.
- Partial completion rests on required historical medium 260 correspondence, not optional
  current API/KOMODO failure alone. Primary water input is not a measured final volume;
  no downstream SL-6 concentration is asserted.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-039
- generated-medium
```
