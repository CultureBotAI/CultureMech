# Source and formulation review: bhi_2_medium (CultureMech:002815)

- Review: 20261022T003032Z-culturemech-002815-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T00:25:04Z
- Finished UTC: 2026-10-22T00:30:32Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 467 and DSM 217 plus basal DSM 215 support an opaque 37 g BHI product with casein hydrolysate, glucose, yeast extract and listed water. All four selected layers retain unverified commercial constituents and omit water. JCM sterilization belongs only to its source scope; manufacturer composition and historical API responses remain unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 423; batch 043 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-two task batches contain 420 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 423 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002815 | data/merge_yaml/merged/BHI_2_MEDIUM.yaml | generated | bhi_2_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002815 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002815 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/423/strict.tsv |
| validate-terms | passed | True | CultureMech:002815 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002815 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002815 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: bd237500 | unavailable | True | CultureMech:002815 | Exact manufacturer product/IFU/manual attempts are unusable; the inherited six-component BHI expansion and tissue-source quantities remain unauthenticated for this product edition. |
| Exact source content access: mediadive217api | unavailable | True | CultureMech:002815 | Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a remains unrecovered within the bounded source search. Local plan/report projections are derivative only. |
| Exact source content access: mediadiveJ467api | unavailable | False | CultureMech:002815 | Current J467 API returned503. Available JCM467 primary supports its printed recipe independently; the historical response cited in the local report is not authenticated by current primary agreement. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002815.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:002815.

7 distinct bound ontology IDs have matching nonobsolete labels; 0 provider-ID slots lack successful identifier verification. All 1 asserted current CHEBI secondary keys have exact index rows; 0 legacy slots are recorded separately. Target primary linkage is 7/9 (77.78%) and current secondary linkage is 1/9 (11.11%), on a 0–100 linkage scale, not a correctness score. Brain/heart anatomy and proteose-peptone class identity do not authenticate a commercial BHI composition.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:002815.

23 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Three exact maintained sources and excluded TOGO namesakes

identity: supported. Targets: CultureMech:002815.

Selected CultureMech:002815 has JCM_J467_BHI_2_MEDIUM, KOMODO217 CultureMech:004427 and DSM217 CultureMech:001319 contributors. TOGO M2441 and M468 namesakes and their generated views are excluded. Current JCM467 and DSM217/215 nominal formulas correspond, while each source retains its own preparation and evidence scope.

### Opaque product and explicit additional glucose

representation: concern. Targets: CultureMech:002815.

The inherited dextrose 2 G_PER_L constituent is not an independently printed addition. Added glucose 5 g belongs to the receiving recipe; do not sum those as 7 g of source-supported additions. The local CHEBI:17234 glucose term is generic and compatible with the unqualified added glucose; no stereochemical mismatch is inferred from the unsupported constituent term CHEBI:17634.

### Batch amounts and missing solvent

quantity: concern. Targets: CultureMech:002815.

All four selected layers omit the listed water and BHI product. Added casein hydrolysate 10, glucose 5 and yeast extract 5 match nominal batch mass numerals, but the stored g/L basis lacks an explicit final-volume declaration. No density, final makeup or independent constituent composition is inferred.

### Explicit JCM default versus unspecified DSM procedure

representation: concern. Targets: CultureMech:002815.

Only the JCM467 page explicitly supplies 121 °C for 15 min; its maintained JCM owner and generated target omit that source-specific preparation. The DSM215/217 pages do not provide a sterilization cycle or pH, and no JCM default is automatically assigned to the DSM or KOMODO owner.

### Classification and biological evidence

scope: supported. Targets: CultureMech:002815.

Complex/undefined liquid classification fits the supplied BHI and additions. Generic cultivation application and catalogue flags are not strain-specific growth or oxygen requirements. No incubation temperature or pH is asserted from the commercial-constituent note.

### Historical derivative plans and present claims

evidence: unknown. Targets: CultureMech:002815.

The local historical reports retain unresolved decisions and decoded source rows, with distinct 217 and J467 response hashes. No ingredient amount evidence objects are attached in the current selected layers. Current primary agreement does not authenticate those historical responses or prove historical source-version equality.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002815.

19 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Calf brains",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q2",
    "subject": "Beef heart",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q3",
    "subject": "Proteose peptone",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q4",
    "subject": "Dextrose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q5",
    "subject": "Sodium chloride",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q6",
    "subject": "Disodium phosphate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "The individual BHI constituent identity and concentration are not established by the opaque product recipe."
  },
  {
    "decision_id": "q7",
    "subject": "Casein hydrolysate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "The nominal source batch mass is supported; the stored final-volume rate remains unsupported because listed water does not declare measured final volume. No attached matching amount evidence exists."
  },
  {
    "decision_id": "q8",
    "subject": "Glucose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "The nominal source batch mass is supported; the stored final-volume rate remains unsupported because listed water does not declare measured final volume. No attached matching amount evidence exists."
  },
  {
    "decision_id": "q9",
    "subject": "Yeast extract",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "The nominal source batch mass is supported; the stored final-volume rate remains unsupported because listed water does not declare measured final volume. No attached matching amount evidence exists."
  },
  {
    "decision_id": "q10",
    "subject": "Tissue-source 200 g/L",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "This internal commercial-product quantity or pH claim is not established for the exact supplied product edition."
  },
  {
    "decision_id": "q11",
    "subject": "Tissue-source 250 g/L",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "This internal commercial-product quantity or pH claim is not established for the exact supplied product edition."
  },
  {
    "decision_id": "q12",
    "subject": "Product pH 7.4 ± 0.2",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "This internal commercial-product quantity or pH claim is not established for the exact supplied product edition."
  },
  {
    "decision_id": "q13",
    "subject": "Missing opaque BHI 37 g batch component",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "Restore the source batch product amount without replacing it by an unverified internal composition or final-volume rate."
  },
  {
    "decision_id": "q14",
    "subject": "Missing water 1000 ml component",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 water row",
        "exact_source_quote": "Distilled water                          1000.0   ml",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      }
    ],
    "rationale": "Restore the exact listed water component; this is not an explicit makeup instruction."
  },
  {
    "decision_id": "q15",
    "subject": "Casein hydrolysate source batch addition 10 g",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "Preserve this explicit receiving-medium batch addition separately from the unsupported stored per-litre basis and BHI internal constituent assertions."
  },
  {
    "decision_id": "q16",
    "subject": "Glucose source batch addition 5 g",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "Preserve this explicit receiving-medium batch addition separately from the unsupported stored per-litre basis and BHI internal constituent assertions."
  },
  {
    "decision_id": "q17",
    "subject": "Yeast extract source batch addition 5 g",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "Preserve this explicit receiving-medium batch addition separately from the unsupported stored per-litre basis and BHI internal constituent assertions."
  },
  {
    "decision_id": "q18",
    "subject": "JCM467 sterilization 121 °C for 15 min",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm467",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467",
        "source_locator": "Page default before467",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "ef354e7bb1ca821b1cacab2bbdd4567c4016de2bdca1faf2b28e47d7b0625efa",
        "parsed_text_sha256": "4fa901b0da5eb139d71b4d9a4d95de0a14040d1ea985f6a55e429e44565f6237"
      }
    ],
    "rationale": "The JCM source default applies to the JCM maintained owner and its generated representation. It is not independently printed by the DSM source or transferred to other owners."
  },
  {
    "decision_id": "q19",
    "subject": "Generic pH and incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BHI_2_MEDIUM.yaml",
        "field_path": "temperature",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
        "field_path": "temperature",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
        "field_path": "temperature",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
        "field_path": "temperature",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215Basal",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf",
        "source_locator": "Basal215 product row",
        "exact_source_quote": "Brain Heart Infusion (Difco)               37.0    g",
        "snapshot_sha256": "2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5",
        "parsed_text_sha256": "85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9"
      },
      {
        "source_key": "dsmz217",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf",
        "source_locator": "Complete primary sentence",
        "exact_source_quote": "To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast extract.",
        "snapshot_sha256": "45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00",
        "parsed_text_sha256": "cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c"
      }
    ],
    "rationale": "The exact collection texts do not print these cultivation values. Commercial-constituent pH and JCM autoclaving temperature are distinct scopes."
  }
]

## Findings

### f1: Opaque BHI replaced by unverified constituent additions

major / open / confirmed; issue key: culturemech.002815.commercial-expansion.

All selected layers replace the supplied BHI 37 g product with six unsupported constituents. Inherited dextrose 2 G_PER_L cannot be added to the source glucose 5 g as though both were independently specified additions.

### f2: Listed solvent omitted from every selected layer

major / open / confirmed; issue key: culturemech.002815.missing-water.

Both exact collection routes list water 1 L/1000 ml. All selected layers omit that component, leaving the supplied preparation incomplete and the normalized rate basis unverified.

### f3: JCM source sterilization absent

minor / open / confirmed; issue key: culturemech.002815.jcm-sterilization-missing.

The JCM467 source explicitly supplies its page default 121 °C for 15 min. The JCM maintained owner and target omit it; the DSM/KOMODO sources do not independently prescribe this cycle.

## Recommended Actions And Acceptance Checks

### a1

Restore opaque BHI and separate source-supported additions in each maintained contributor; preserve unresolved manufacturer composition and avoid unsupported glucose totals.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the listed water component in each maintained source, retain unknown measured final volume and add exact claim-level source support.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add the scoped JCM sterilization instruction to the JCM owner and preserve source-specific preparation in authorized regeneration; do not impose it on the DSM route.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHI_2_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/bhi_2_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHI_2_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHI_2_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch043/423/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/423/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHI_2_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHI_2_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BHI_2_MEDIUM.yaml:1:id: CultureMech:002815<br>./data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml:1:id: CultureMech:002815<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch043/source-preflight-bound/423/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 27 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch043/423/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17234": [{"label": "(2R,3S,4R,5R)-2,3,4,5,6-pentahydroxyhexanal", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aldehydo-D-gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aldehydo-D-gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "D-glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "D-GLUCOSE IN LINEAR FORM", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "DL-glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D­glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glc", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glukose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BHI_2_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml; data/normalized_yaml/bacterial/bhi_2_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml", "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml", "events": 6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:12.864710"}]}, {"input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml", "events": 5, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch043/423/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch043/423/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary-supplement | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf; Complete primary sentence | supports | Exact DSM217 adds three named batch masses to basal215. |
| primary-product | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf; Basal215 table product row | supports | Opaque BHI is a supplied product, not six established individual medium ingredients. |
| primary-water | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf; Basal215 table water row | supports | The source lists 1000 ml water without a measured-final-volume or makeup instruction. |
| jcm-identity | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467; JCM467 title and full five-row table | supports | JCM467 independently lists BHI 37 g, casein hydrolysate 10 g, glucose 5 g, yeast extract 5 g and water 1 L; nominal formula correspondence is separate from source procedure. |
| jcm-sterilization | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467; Page default preceding467 | supports | Explicit JCM page default only; not transferred to DSM/KOMODO owners. |
| catalog-identity | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact217 row and header | supports | KOMODO217 maps to DSM217; catalogue aerobic flag does not prescribe gas. |
| secondary-product | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Current secondary article composition | context_only | This secondary BHI agar formula is not authenticated exact product237500 edition evidence. |
| bd237500-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.237500; Preserved exact public retrieval result | context_only | Exact manufacturer product/IFU/manual attempts are unusable; the inherited six-component BHI expansion and tissue-source quantities remain unauthenticated for this product edition. |
| mediadive217api-attempt | https://mediadive.dsmz.de/rest/medium/217; Preserved exact public retrieval result | context_only | Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a remains unrecovered within the bounded source search. Local plan/report projections are derivative only. |
| mediadiveJ467api-attempt | https://mediadive.dsmz.de/rest/medium/J467; Preserved exact public retrieval result | context_only | Current J467 API returned503. Available JCM467 primary supports its printed recipe independently; the historical response cited in the local report is not authenticated by current primary agreement. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch043/423/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact manufacturer product/IFU/manual attempts are unusable; the inherited six-component BHI expansion and tissue-source quantities remain unauthenticated for this product edition.
- Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a remains unrecovered within the bounded source search. Local plan/report projections are derivative only.
- Current J467 API returned503. Available JCM467 primary supports its printed recipe independently; the historical response cited in the local report is not authenticated by current primary agreement.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T003032Z-culturemech-002815-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bhi_2_medium (CultureMech:002815)'
started_at: '2026-10-22T00:25:04Z'
finished_at: '2026-10-22T00:30:32Z'
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
summary: JCM 467 and DSM 217 plus basal DSM 215 support an opaque 37 g BHI product
  with casein hydrolysate, glucose, yeast extract and listed water. All four selected
  layers retain unverified commercial constituents and omit water. JCM sterilization
  belongs only to its source scope; manufacturer composition and historical API responses
  remain unresolved.
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
  - path: data/merge_yaml/merged/BHI_2_MEDIUM.yaml
    sha256: 75bafac21391424b9b6c58423fa594b24c89a11e0bb0f55859da277a3608f220
    role: target
  - path: data/merge_yaml/merged/bhi_2_medium__b5331467.yaml
    sha256: 3f25023d3cc09d916a5e4420425aaf151f148d9718b299aab1c73a6c4b370f1f
    role: context
  - path: data/merge_yaml/merged/bhi_2_medium__c2263538.yaml
    sha256: 5dd8e691756462e4c4ec608718143579803b3a162067fd1c41c14726654f4816
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    sha256: b583087d1582bd14b83282d28b4b365e123b9ba1abac009d3bd8eb3b9926d528
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    sha256: 54fe87be1f0098395a13c31f12204610abce55993412f7e7a4b407c6f4710963
    role: context
  - path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
    sha256: f894329ff1eaa1d399fc1153eac630b260cd47a4f1271e78c50bea78441fd564
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
    sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_217_BHI_2_medium.yaml.md
    sha256: 7369d6e110fac271e9a09ffac68b734a9dfb80d5d876766df1cb4e48dba886d8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bhi_2_medium.yaml.md
    sha256: 065ce910c3c3562b5567ce66e632e8c6c5961f726d330d638009f01f8efd6015
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/plan.json
    sha256: 2a664ea8af07a25caadaa3e00421ae8eaa883ddd3e42c83f5013b3bf303c789b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J467_BHI_2_MEDIUM.yaml.md
    sha256: 5268cac388f4977c1f99e05db1f0269087fe6a77666bcf723cb8592fc30df207
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  selection: Task review 423; batch 043 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:002815
targets:
- target_id: CultureMech:002815
  path: data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  label: bhi_2_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHI_2_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch043/423/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/423/strict.tsv"
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002815
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
  - CultureMech:002815
- check_id: bd237500-source-access
  name: 'Exact source content access: bd237500'
  required: true
  status: unavailable
  summary: Exact manufacturer product/IFU/manual attempts are unusable; the inherited
    six-component BHI expansion and tissue-source quantities remain unauthenticated
    for this product edition.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - bd237500-attempt
- check_id: mediadive217api-source-access
  name: 'Exact source content access: mediadive217api'
  required: true
  status: unavailable
  summary: Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a
    remains unrecovered within the bounded source search. Local plan/report projections
    are derivative only.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - mediadive217api-attempt
- check_id: mediadiveJ467api-source-access
  name: 'Exact source content access: mediadiveJ467api'
  required: false
  status: unavailable
  summary: Current J467 API returned503. Available JCM467 primary supports its printed
    recipe independently; the historical response cited in the local report is not
    authenticated by current primary agreement.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - mediadiveJ467api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/bhi_2_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:41.481436Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHI_2_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch043/423/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:42.489348Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/423/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:43.580680Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHI_2_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:44.292649Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T00:30:31Z'
  support: supports
  summary: './data/merge_yaml/merged/BHI_2_MEDIUM.yaml:1:id: CultureMech:002815

    ./data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml:1:id: CultureMech:002815

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/source-preflight-bound/423/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T00:30:31Z'
  support: supports
  summary: 27 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e1ea2c615133ce74f7ff4f092732395d82658ec0c3c8aa3ddb1a905a22cd65d8
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/423/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: 2e66ba4bbc95495ea197e8c6ed4f01e65ca5d8482c84ccf1e3906ec02a5fd5bf
- evidence_id: uberon0000955
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:25.122940Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: ce200fe58b82652d0f04310c92d23633919fa6ad6aee2a17c6b25c2e490a8877
- evidence_id: uberon0000948
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:24.915343Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: c658bbcacd89befa47e3bd4859f176db247b3ce67483b6590c91d0865d41aed4
- evidence_id: micro0000180
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:24.290496Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: b3a39a531c5ab5508a297228d13ba81c99899b041d5292a9d668eded939bfe73
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17234":
    [{"label": "(2R,3S,4R,5R)-2,3,4,5,6-pentahydroxyhexanal", "match_type": "synonym",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aldehydo-D-gluco-hexose",
    "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose",
    "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "aldehydo-D-gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234",
    "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED",
    "ambiguity": "unique"}, {"label": "D-glucose", "match_type": "synonym", "identifier":
    "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "D-GLUCOSE IN LINEAR FORM",
    "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose",
    "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "DL-glucose", "match_type": "synonym", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "D­glucose", "match_type": "synonym", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Glc", "match_type": "synonym", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "gluco-hexose", "match_type": "synonym",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "glucose",
    "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term":
    "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "glucose", "match_type": "synonym", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Glukose", "match_type": "synonym", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHI_2_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml;
    data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml; data/normalized_yaml/bacterial/bhi_2_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml",
    "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml",
    "events": 6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:12.864710"}]}, {"input": "data/normalized_yaml/bacterial/bhi_2_medium.yaml",
    "events": 5, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/423/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 63d17e29d46bbd089868a50440048ca459577a49c73cd99660c8ef45b02ea5e1
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/423/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: e244698e31cc17712317db2aec508ea9c989204ff66f86376cc64eac3f4a95d7
- evidence_id: primary-supplement
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf
  locator: Complete primary sentence
  accessed_at: '2026-10-22T00:02:26.715182Z'
  support: supports
  summary: Exact DSM217 adds three named batch masses to basal215.
  quote: To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast
    extract.
  snapshot_sha256: 45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00
- evidence_id: primary-product
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf
  locator: Basal215 table product row
  accessed_at: '2026-10-22T00:04:48.178932Z'
  support: supports
  summary: Opaque BHI is a supplied product, not six established individual medium
    ingredients.
  quote: Brain Heart Infusion (Difco)               37.0    g
  snapshot_sha256: 2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5
- evidence_id: primary-water
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf
  locator: Basal215 table water row
  accessed_at: '2026-10-22T00:04:48.178932Z'
  support: supports
  summary: The source lists 1000 ml water without a measured-final-volume or makeup
    instruction.
  quote: Distilled water                          1000.0   ml
  snapshot_sha256: 2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5
- evidence_id: jcm-identity
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467
  locator: JCM467 title and full five-row table
  accessed_at: '2026-10-22T00:02:26.165277Z'
  support: supports
  summary: JCM467 independently lists BHI 37 g, casein hydrolysate 10 g, glucose 5
    g, yeast extract 5 g and water 1 L; nominal formula correspondence is separate
    from source procedure.
  quote: 467   BHI/2 MEDIUM
  snapshot_sha256: ef354e7bb1ca821b1cacab2bbdd4567c4016de2bdca1faf2b28e47d7b0625efa
- evidence_id: jcm-sterilization
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467
  locator: Page default preceding467
  accessed_at: '2026-10-22T00:02:26.165277Z'
  support: supports
  summary: Explicit JCM page default only; not transferred to DSM/KOMODO owners.
  quote: Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.
  snapshot_sha256: ef354e7bb1ca821b1cacab2bbdd4567c4016de2bdca1faf2b28e47d7b0625efa
- evidence_id: catalog-identity
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact217 row and header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO217 maps to DSM217; catalogue aerobic flag does not prescribe gas.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=217'\
    \ >217</a></TD>\n\t\t\t\t\t<TD>BHI/2 medium</TD>\n\t\t\t\t\t<TD>null</TD>\n\t\t\
    \t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: secondary-product
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Current secondary article composition
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: context_only
  summary: This secondary BHI agar formula is not authenticated exact product237500
    edition evidence.
  quote: HM infusion powder 12.500 BHI powder 5.000
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: bd237500-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.237500
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:04.060812Z'
  support: context_only
  summary: Exact manufacturer product/IFU/manual attempts are unusable; the inherited
    six-component BHI expansion and tissue-source quantities remain unauthenticated
    for this product edition.
  snapshot_sha256: 98f5e49148f7da45d2d1ec9ea7d172730bfbeb67c73f74886103fb2499b3b79a
- evidence_id: mediadive217api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/217
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:02:26.760685Z'
  support: context_only
  summary: Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a
    remains unrecovered within the bounded source search. Local plan/report projections
    are derivative only.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ467api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J467
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:02:26.254646Z'
  support: context_only
  summary: Current J467 API returned503. Available JCM467 primary supports its printed
    recipe independently; the historical response cited in the local report is not
    authenticated by current primary agreement.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/423/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T00:30:31Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 246f2939fac6a632a4abb7f0c035f802f332dca217bbe3b4ad34600a08b48ddf
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: supported
  summary: 7 distinct bound ontology IDs have matching nonobsolete labels; 0 provider-ID
    slots lack successful identifier verification. All 1 asserted current CHEBI secondary
    keys have exact index rows; 0 legacy slots are recorded separately. Target primary
    linkage is 7/9 (77.78%) and current secondary linkage is 1/9 (11.11%), on a 0–100
    linkage scale, not a correctness score. Brain/heart anatomy and proteose-peptone
    class identity do not authenticate a commercial BHI composition.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - grounding-inventory
  - mim
  - uberon0000955
  - uberon0000948
  - micro0000180
  - chebi17634
  - chebi26710
  - chebi34683
  - chebi17234
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: identity
  area: identity
  topic: Three exact maintained sources and excluded TOGO namesakes
  outcome: supported
  summary: Selected CultureMech:002815 has JCM_J467_BHI_2_MEDIUM, KOMODO217 CultureMech:004427
    and DSM217 CultureMech:001319 contributors. TOGO M2441 and M468 namesakes and
    their generated views are excluded. Current JCM467 and DSM217/215 nominal formulas
    correspond, while each source retains its own preparation and evidence scope.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - record
  - jcm-identity
  - primary-supplement
  - catalog-identity
  - owner-0
  - owner-1
  - owner-2
- assessment_id: formulation
  area: representation
  topic: Opaque product and explicit additional glucose
  outcome: concern
  summary: The inherited dextrose 2 G_PER_L constituent is not an independently printed
    addition. Added glucose 5 g belongs to the receiving recipe; do not sum those
    as 7 g of source-supported additions. The local CHEBI:17234 glucose term is generic
    and compatible with the unqualified added glucose; no stereochemical mismatch
    is inferred from the unsupported constituent term CHEBI:17634.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - primary-product
  - primary-supplement
  - chebi17234
  - chebi17634
- assessment_id: basis
  area: quantity
  topic: Batch amounts and missing solvent
  outcome: concern
  summary: All four selected layers omit the listed water and BHI product. Added casein
    hydrolysate 10, glucose 5 and yeast extract 5 match nominal batch mass numerals,
    but the stored g/L basis lacks an explicit final-volume declaration. No density,
    final makeup or independent constituent composition is inferred.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - primary-product
  - primary-water
  - primary-supplement
- assessment_id: preparation
  area: representation
  topic: Explicit JCM default versus unspecified DSM procedure
  outcome: concern
  summary: Only the JCM467 page explicitly supplies 121 °C for 15 min; its maintained
    JCM owner and generated target omit that source-specific preparation. The DSM215/217
    pages do not provide a sterilization cycle or pH, and no JCM default is automatically
    assigned to the DSM or KOMODO owner.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - jcm-sterilization
  - primary-supplement
  - primary-product
- assessment_id: biology
  area: scope
  topic: Classification and biological evidence
  outcome: supported
  summary: Complex/undefined liquid classification fits the supplied BHI and additions.
    Generic cultivation application and catalogue flags are not strain-specific growth
    or oxygen requirements. No incubation temperature or pH is asserted from the commercial-constituent
    note.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - record
  - jcm-identity
  - primary-supplement
- assessment_id: history-source
  area: evidence
  topic: Historical derivative plans and present claims
  outcome: unknown
  summary: The local historical reports retain unresolved decisions and decoded source
    rows, with distinct 217 and J467 response hashes. No ingredient amount evidence
    objects are attached in the current selected layers. Current primary agreement
    does not authenticate those historical responses or prove historical source-version
    equality.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - historical-inventory
  - mediadive217api-attempt
  - mediadiveJ467api-attempt
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 19 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002815
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Calf brains\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"subject\": \"Beef heart\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"Proteose peptone\",\n \
    \   \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.0\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q4\",\n    \"subject\": \"Dextrose\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q5\",\n    \"subject\": \"Sodium chloride\",\n  \
    \  \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q6\",\n    \"subject\": \"Disodium phosphate\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"The individual BHI constituent identity\
    \ and concentration are not established by the opaque product recipe.\"\n  },\n\
    \  {\n    \"decision_id\": \"q7\",\n    \"subject\": \"Casein hydrolysate\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz217\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\"\
    ,\n        \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"The nominal source batch mass is supported;\
    \ the stored final-volume rate remains unsupported because listed water does not\
    \ declare measured final volume. No attached matching amount evidence exists.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\": \"Glucose\",\n   \
    \ \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz217\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\"\
    ,\n        \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"The nominal source batch mass is supported;\
    \ the stored final-volume rate remains unsupported because listed water does not\
    \ declare measured final volume. No attached matching amount evidence exists.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"Yeast extract\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz217\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\"\
    ,\n        \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"The nominal source batch mass is supported;\
    \ the stored final-volume rate remains unsupported because listed water does not\
    \ declare measured final volume. No attached matching amount evidence exists.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\": \"Tissue-source 200\
    \ g/L\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion from 200\
    \ g/L; Tissue infusion - source material is calf brain tissue; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].notes\",\n        \"stored\": \"infusion from 200 g/L; Tissue\
    \ infusion - source material is calf brain tissue; Constituent of Brain Heart\
    \ Infusion commercial product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].notes\",\n        \"stored\": \"infusion from 200 g/L; Tissue\
    \ infusion - source material is calf brain tissue; Constituent of Brain Heart\
    \ Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz215Basal\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\",\n        \"\
    source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\": \"\
    Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"This internal commercial-product quantity\
    \ or pH claim is not established for the exact supplied product edition.\"\n \
    \ },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Tissue-source 250\
    \ g/L\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion from 250\
    \ g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].notes\",\n        \"stored\": \"infusion from 250 g/L; Tissue\
    \ infusion - source material is beef/ox heart tissue; Constituent of Brain Heart\
    \ Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz215Basal\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\",\n        \"\
    source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\": \"\
    Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"This internal commercial-product quantity\
    \ or pH claim is not established for the exact supplied product edition.\"\n \
    \ },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Product pH 7.4 ±\
    \ 0.2\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH buffer (final\
    \ pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz215Basal\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"This internal commercial-product quantity\
    \ or pH claim is not established for the exact supplied product edition.\"\n \
    \ },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Missing opaque BHI\
    \ 37 g batch component\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215Basal\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the source batch product amount\
    \ without replacing it by an unverified internal composition or final-volume rate.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"Missing water 1000\
    \ ml component\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215Basal\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water                          1000.0   ml\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact listed water component;\
    \ this is not an explicit makeup instruction.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"subject\": \"Casein hydrolysate source batch addition 10 g\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz217\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\",\n        \"\
    source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit receiving-medium\
    \ batch addition separately from the unsupported stored per-litre basis and BHI\
    \ internal constituent assertions.\"\n  },\n  {\n    \"decision_id\": \"q16\"\
    ,\n    \"subject\": \"Glucose source batch addition 5 g\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz217\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\"\
    ,\n        \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit receiving-medium\
    \ batch addition separately from the unsupported stored per-litre basis and BHI\
    \ internal constituent assertions.\"\n  },\n  {\n    \"decision_id\": \"q17\"\
    ,\n    \"subject\": \"Yeast extract source batch addition 5 g\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz217\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\"\
    ,\n        \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit receiving-medium\
    \ batch addition separately from the unsupported stored per-litre basis and BHI\
    \ internal constituent assertions.\"\n  },\n  {\n    \"decision_id\": \"q18\"\
    ,\n    \"subject\": \"JCM467 sterilization 121 °C for 15 min\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm467\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=467\"\
    ,\n        \"source_locator\": \"Page default before467\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"ef354e7bb1ca821b1cacab2bbdd4567c4016de2bdca1faf2b28e47d7b0625efa\"\
    ,\n        \"parsed_text_sha256\": \"4fa901b0da5eb139d71b4d9a4d95de0a14040d1ea985f6a55e429e44565f6237\"\
    \n      }\n    ],\n    \"rationale\": \"The JCM source default applies to the\
    \ JCM maintained owner and its generated representation. It is not independently\
    \ printed by the DSM source or transferred to other owners.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q19\",\n    \"subject\": \"Generic pH and incubation temperature\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\",\n        \"\
    field_path\": \"ph_value\",\n        \"stored\": null\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\",\n     \
    \   \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n        \"\
    field_path\": \"ph_range\",\n        \"stored\": null\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHI_2_MEDIUM.yaml\",\n \
    \       \"field_path\": \"temperature\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml\"\
    ,\n        \"field_path\": \"temperature\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_2_medium.yaml\"\
    ,\n        \"field_path\": \"temperature\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215Basal\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215.pdf\"\
    ,\n        \"source_locator\": \"Basal215 product row\",\n        \"exact_source_quote\"\
    : \"Brain Heart Infusion (Difco)               37.0    g\",\n        \"snapshot_sha256\"\
    : \"2e9549379b1decf70b72e2d27ca9604f6f8e169ba11675daefc8953a43de1ba5\",\n    \
    \    \"parsed_text_sha256\": \"85075a982033409b763f9deb01882672c8e99b878b0603f1486928a7591529b9\"\
    \n      },\n      {\n        \"source_key\": \"dsmz217\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium217.pdf\",\n    \
    \    \"source_locator\": \"Complete primary sentence\",\n        \"exact_source_quote\"\
    : \"To medium 215 add 10.0 g casein hydrolysate, 5.0 g glucose and 5.0 g yeast\
    \ extract.\",\n        \"snapshot_sha256\": \"45e8877175c4f69f6c597623dd79f223343b0764e11a721a4c971cabd150ed00\"\
    ,\n        \"parsed_text_sha256\": \"cd485180231887bb746194da33630a31fa196ec6136a8a5a8f41ce648dc71d9c\"\
    \n      }\n    ],\n    \"rationale\": \"The exact collection texts do not print\
    \ these cultivation values. Commercial-constituent pH and JCM autoclaving temperature\
    \ are distinct scopes.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.002815.commercial-expansion
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Opaque BHI replaced by unverified constituent additions
  description: All selected layers replace the supplied BHI 37 g product with six
    unsupported constituents. Inherited dextrose 2 G_PER_L cannot be added to the
    source glucose 5 g as though both were independently specified additions.
  target_ids:
  - CultureMech:002815
  field_paths:
  - ingredients
  - notes
  evidence_ids:
  - primary-product
  - primary-supplement
  - secondary-product
  - bd237500-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
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
  issue_key: culturemech.002815.missing-water
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Listed solvent omitted from every selected layer
  description: Both exact collection routes list water 1 L/1000 ml. All selected layers
    omit that component, leaving the supplied preparation incomplete and the normalized
    rate basis unverified.
  target_ids:
  - CultureMech:002815
  field_paths:
  - ingredients
  evidence_ids:
  - primary-water
  - jcm-identity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
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
  issue_key: culturemech.002815.jcm-sterilization-missing
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: JCM source sterilization absent
  description: The JCM467 source explicitly supplies its page default 121 °C for 15
    min. The JCM maintained owner and target omit it; the DSM/KOMODO sources do not
    independently prescribe this cycle.
  target_ids:
  - CultureMech:002815
  field_paths:
  - preparation_steps
  evidence_ids:
  - jcm-sterilization
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore opaque BHI and separate source-supported additions in each
    maintained contributor; preserve unresolved manufacturer composition and avoid
    unsupported glucose totals.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002815
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
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
  description: Restore the listed water component in each maintained source, retain
    unknown measured final volume and add exact claim-level source support.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002815
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_2_medium.yaml
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
  description: Add the scoped JCM sterilization instruction to the JCM owner and preserve
    source-specific preparation in authorized regeneration; do not impose it on the
    DSM route.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002815
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J467_BHI_2_MEDIUM.yaml
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
- Exact manufacturer product/IFU/manual attempts are unusable; the inherited six-component
  BHI expansion and tissue-source quantities remain unauthenticated for this product
  edition.
- Current API217 returned503; original historical API217 SHA df0125ba5c7391ece64b420d65138a9a48f67b1f847f4e99645d7cb70fd1bd5a
  remains unrecovered within the bounded source search. Local plan/report projections
  are derivative only.
- Current J467 API returned503. Available JCM467 primary supports its printed recipe
  independently; the historical response cited in the local report is not authenticated
  by current primary agreement.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-043
- generated-medium
```
