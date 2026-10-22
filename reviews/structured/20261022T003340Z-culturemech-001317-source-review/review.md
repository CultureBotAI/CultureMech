# Source and formulation review: bhi_medium_for_strict_anaerobes (CultureMech:001317)

- Review: 20261022T003340Z-culturemech-001317-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T00:25:06Z
- Finished UTC: 2026-10-22T00:33:40Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The maintained DSM 215c owner already restores the opaque BHI product and water, while the generated target retains its older commercial expansion. Both retain an unsupported pH range; the owner also asserts unprinted final-volume makeup and per-litre rates. The primary supports its four batch ingredients and anoxic procedure, but provider identifiers and historical API bytes remain unverified.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 425; batch 043 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-two task batches contain 420 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 423 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001317 | data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml | generated | bhi_medium_for_strict_anaerobes |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001317 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001317 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/425/strict.tsv |
| validate-terms | passed | True | CultureMech:001317 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001317 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001317 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: bd237500 | unavailable | True | CultureMech:001317 | Retained supplier attempts do not authenticate the expanded commercial formulation still present in the target. The maintained owner already avoids that expansion. |
| Exact source content access: mediadive215capi | unavailable | True | CultureMech:001317 | Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc is not recovered within the bounded search. Decoded historical reports do not authenticate compound identifiers 186, 770, 54 or 4, or the original normalization. There are no attached ingredient amount-evidence objects in the selected target or owner. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001317.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: concern. Targets: CultureMech:001317.

9 distinct bound ontology IDs have matching nonobsolete labels; 4 provider-ID slots lack successful identifier verification. All 3 asserted current CHEBI secondary keys have exact index rows; 0 legacy slots are recorded separately. Target primary linkage is 8/8 (100.00%) and current secondary linkage is 2/8 (25.00%), on a 0–100 linkage scale, not a correctness score. Brain/heart anatomy and proteose-peptone class identity do not authenticate a commercial BHI composition.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001317.

14 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Single maintained owner and separate catalogue child

identity: supported. Targets: CultureMech:001317.

The inspected target and maintained DSM owner both have CultureMech:001317 and accession 215c. Its single contributor is bhi_medium_for_strict_anaerobes.yaml. The linked KOMODO CultureMech:004425 child is a separate record and is not an owner of this target. No child or strain-specific quantities are transferred.

### Repaired owner versus older generated formulation

representation: concern. Targets: CultureMech:001317.

The current maintained owner contains BHI, the two reducers and water, corresponding to the four primary table identities. The generated target instead retains six unverified commercial constituents and omits the opaque product and water. Its August merge history precedes the owner September repair entry. This observed difference does not establish that the current guarded merger caused the old expansion.

### Supported batch masses and unsupported normalization

quantity: concern. Targets: CultureMech:001317.

The primary prints BHI 37 g, each reducer 0.25 g and water 1000 ml. It does not print the retained pH range 7.2–7.6 or direct the operator to bring the final preparation to one litre. Matching owner mass numerals do not authenticate stored g/L or ml/L normalization. The water rate is a plausible nominal convention, but its asserted makeup basis is unsupported.

### Correct secondary chemical forms versus unverified provider IDs

grounding: unknown. Targets: CultureMech:001317.

CHEBI:91248 explicitly describes L-cysteine hydrochloride monohydrate and CHEBI:76209 sodium sulfide nonahydrate; these match the primary supplied forms. CHEBI:15377 supports water identity. Current MIM rows verify those secondary keys. The four owner mediadive.compound identifiers remain separate unresolved correspondences, not proven wrong IDs and not invented OLS lookups. Anatomy and peptone-class terms do not verify the target BHI expansion.

### Explicit anaerobic procedure and bounded variant branches

scope: supported. Targets: CultureMech:001317.

Both selected layers retain 100% N2 and sterile anoxic reducer addition after autoclaving; the owner separates the steps. Neither a numeric autoclave cycle nor incubation temperature is supplied. The catalogue aerobic flag is not a procedural override. Glycerol for DSM 10643, haemin/vitamin K1 for DSM 19851 and rumen fluid for DSM 108840 remain source-specific branches; they do not establish base-medium target organisms or universal additions.

### Local claims and original response authentication

evidence: unknown. Targets: CultureMech:001317.

The October report preserves four owner amount claims and the preparation paragraph as decoded derivative context, including original source hash and access time. The separate child report remains relationship context only. General owner references and matching current PDF text do not authenticate the historical API bytes or constitute attached claim-level amount evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001317.

30 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Generated target: Calf brains",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q2",
    "subject": "Generated target: Beef heart",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q3",
    "subject": "Generated target: Proteose peptone",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q4",
    "subject": "Generated target: Dextrose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q5",
    "subject": "Generated target: Sodium chloride",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q6",
    "subject": "Generated target: Disodium phosphate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The expanded commercial constituent is not authenticated by the opaque product table."
  },
  {
    "decision_id": "q7",
    "subject": "Generated target: L-Cysteine HCl x H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table cysteine row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                 0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The supplied-form batch mass is 0.25 g, but a measured final volume supporting the stored G_PER_L basis is not established."
  },
  {
    "decision_id": "q8",
    "subject": "Generated target: Na2S x 9 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table sulfide row",
        "exact_source_quote": "   Na2S x 9 H2O                                         0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The supplied-form batch mass is 0.25 g, but a measured final volume supporting the stored G_PER_L basis is not established."
  },
  {
    "decision_id": "q9",
    "subject": "Maintained owner: Brain heart infusion",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "37",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The four-ingredient representation and nominal batch numeral match the primary, but the stored per-litre basis is unverified. No final-volume makeup is printed; this is not a proven numerical transcription error."
  },
  {
    "decision_id": "q10",
    "subject": "Maintained owner: L-Cysteine HCl x H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table cysteine row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                 0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The four-ingredient representation and nominal batch numeral match the primary, but the stored per-litre basis is unverified. No final-volume makeup is printed; this is not a proven numerical transcription error."
  },
  {
    "decision_id": "q11",
    "subject": "Maintained owner: Na2S x 9 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table sulfide row",
        "exact_source_quote": "   Na2S x 9 H2O                                         0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The four-ingredient representation and nominal batch numeral match the primary, but the stored per-litre basis is unverified. No final-volume makeup is printed; this is not a proven numerical transcription error."
  },
  {
    "decision_id": "q12",
    "subject": "Maintained owner: Distilled water",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1000",
          "unit": "ML_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table water row",
        "exact_source_quote": "   Distilled water                                   1000.00      ml",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The four-ingredient representation and nominal batch numeral match the primary, but the stored per-litre basis is unverified. No final-volume makeup is printed; this is not a proven numerical transcription error."
  },
  {
    "decision_id": "q13",
    "subject": "Target tissue-source 200 g/L",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The exact manufacturer edition and internal product claim are not authenticated. The repaired owner no longer asserts this expansion."
  },
  {
    "decision_id": "q14",
    "subject": "Target tissue-source 250 g/L",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The exact manufacturer edition and internal product claim are not authenticated. The repaired owner no longer asserts this expansion."
  },
  {
    "decision_id": "q15",
    "subject": "Target commercial pH 7.4 ± 0.2",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The exact manufacturer edition and internal product claim are not authenticated. The repaired owner no longer asserts this expansion."
  },
  {
    "decision_id": "q16",
    "subject": "Owner ingredient note 1",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "DSMZ Medium 215c lists Brain heart infusion at 37 g/L as an opaque rich-meat product."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The note attributes a per-litre rate or final-water makeup to the source; the current primary establishes only the listed batch amount and no makeup instruction."
  },
  {
    "decision_id": "q17",
    "subject": "Owner ingredient note 2",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "DSMZ Medium 215c lists 0.25 g/L L-Cysteine HCl x H2O."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table cysteine row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                 0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The note attributes a per-litre rate or final-water makeup to the source; the current primary establishes only the listed batch amount and no makeup instruction."
  },
  {
    "decision_id": "q18",
    "subject": "Owner ingredient note 3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "DSMZ Medium 215c lists 0.25 g/L Na2S x 9 H2O."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table sulfide row",
        "exact_source_quote": "   Na2S x 9 H2O                                         0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The note attributes a per-litre rate or final-water makeup to the source; the current primary establishes only the listed batch amount and no makeup instruction."
  },
  {
    "decision_id": "q19",
    "subject": "Owner ingredient note 4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "DSMZ Medium 215c brings the recipe to one liter with distilled water."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table water row",
        "exact_source_quote": "   Distilled water                                   1000.00      ml",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The note attributes a per-litre rate or final-water makeup to the source; the current primary establishes only the listed batch amount and no makeup instruction."
  },
  {
    "decision_id": "q20",
    "subject": "Owner aggregate rate narrative",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "notes",
        "stored": "MediaDive and DSMZ Medium 215c list BHI Medium for Strict Anaerobes as 37 g/L Brain heart infusion, 0.25 g/L L-Cysteine HCl x H2O, 0.25 g/L Na2S x 9 H2O, and distilled water, prepared anoxically under 100% N2 with the reducing agents added from sterile anoxic solutions after autoclaving."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      },
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table cysteine row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                 0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      },
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table sulfide row",
        "exact_source_quote": "   Na2S x 9 H2O                                         0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      },
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table water row",
        "exact_source_quote": "   Distilled water                                   1000.00      ml",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      },
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base preparation paragraph",
        "exact_source_quote": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added\nafter autoclaving from sterile anoxic solutions prepared under N2.",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The ingredient identities and anoxic procedure are supported, but the three per-litre mass assertions are not established by the current primary denominator."
  },
  {
    "decision_id": "q21",
    "subject": "Retained pH range 7.2–7.6",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.6
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.6
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      },
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base preparation paragraph",
        "exact_source_quote": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added\nafter autoclaving from sterile anoxic solutions prepared under N2.",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Neither the current exact primary nor an authenticated historical response establishes this pH interval. No replacement value is inferred."
  },
  {
    "decision_id": "q22",
    "subject": "Opaque BHI batch representation",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table BHI row",
        "exact_source_quote": "   Brain heart infusion (DIFCO)                        37.00       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Represent the exact printed batch quantity with claim-level source attachment. This is a proposed source-bound representation, not an additional dose or a new final-volume claim."
  },
  {
    "decision_id": "q23",
    "subject": "Cysteine hydrate batch mass",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table cysteine row",
        "exact_source_quote": "   L-Cysteine HCl x H2O                                 0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Represent the exact printed batch quantity with claim-level source attachment. This is a proposed source-bound representation, not an additional dose or a new final-volume claim."
  },
  {
    "decision_id": "q24",
    "subject": "Sulfide nonahydrate batch mass",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table sulfide row",
        "exact_source_quote": "   Na2S x 9 H2O                                         0.25       g",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Represent the exact printed batch quantity with claim-level source attachment. This is a proposed source-bound representation, not an additional dose or a new final-volume claim."
  },
  {
    "decision_id": "q25",
    "subject": "Listed batch water",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base table water row",
        "exact_source_quote": "   Distilled water                                   1000.00      ml",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Represent the exact printed batch quantity with claim-level source attachment. This is a proposed source-bound representation, not an additional dose or a new final-volume claim."
  },
  {
    "decision_id": "q26",
    "subject": "100% N2 and staged sterile reducer procedure",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added after autoclaving from sterile anoxic solutions prepared under N2."
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Prepare the medium anoxically under 100% N2 gas atmosphere."
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Add L-Cysteine HCl x H2O and Na2S x 9 H2O after autoclaving from sterile anoxic solutions prepared under N2."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base preparation paragraph",
        "exact_source_quote": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added\nafter autoclaving from sterile anoxic solutions prepared under N2.",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Exact gas percentage and addition ordering are supported in both layers. General references exist on the owner, but no matching claim-level evidence is attached to these steps."
  },
  {
    "decision_id": "q27",
    "subject": "Unspecified autoclave cycle and incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml",
        "field_path": "temperature",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
        "field_path": "temperature",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "Base preparation paragraph",
        "exact_source_quote": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added\nafter autoclaving from sterile anoxic solutions prepared under N2.",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "Autoclaving is mentioned, but no temperature or duration is given. No incubation value or default cycle is inferred."
  },
  {
    "decision_id": "q28",
    "subject": "DSM 10643 glycerol 10 ml/L of 87% w/v stock",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "DSM 10643 glycerol 10 ml/L of 87% w/v stock variant paragraph",
        "exact_source_quote": "For DSM 10643: Supplement medium with 10.00 ml/l glycerol (87% w/v solution) from a\nsterile anoxic stock.",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "The explicit stock strength and dose are supported only for DSM 10643. They are excluded from the base recipe; no replacement of the base water or final-volume adjustment is inferred."
  },
  {
    "decision_id": "q29",
    "subject": "DSM 19851 haemin 10 ml/L and vitamin K1 0.2 ml/L",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "DSM 19851 haemin 10 ml/L and vitamin K1 0.2 ml/L variant paragraph",
        "exact_source_quote": "For DSM 19851: Supplement medium with 10.0 ml/l haemin and 0.2 ml/l vitamin K1\nsolution (see medium 78).",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "These are two variant-only stock doses referring to medium 78. No concentration of either stock or generic base addition is inferred."
  },
  {
    "decision_id": "q30",
    "subject": "DSM 108840 rumen-fluid amount",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz215c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf",
        "source_locator": "DSM 108840 rumen-fluid amount variant paragraph",
        "exact_source_quote": "For DSM 108840: Plus rumen fluid",
        "snapshot_sha256": "6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656",
        "parsed_text_sha256": "0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754"
      }
    ],
    "rationale": "This variant names rumen fluid without an amount. The variant is excluded from the base and no customary amount is supplied."
  }
]

## Findings

### f1: Generated formulation predates the maintained opaque-product repair

major / open / confirmed; issue key: culturemech.001317.stale-generated-expansion.

The generated target retains six unverified BHI constituents and lacks the BHI product and water entries. The maintained DSM owner already has the source-supported four-ingredient representation; it must not be described as still expanded.

### f2: Retained pH range lacks source support

major / open / confirmed; issue key: culturemech.001317.unsupported-ph.

Both target and owner retain pH 7.2–7.6, but the exact primary does not specify it and the cited historical API response is unavailable. This is an unsupported claim, not proof that a particular alternative pH is correct.

### f3: Listed water is described as final-volume makeup

major / open / confirmed; issue key: culturemech.001317.unsupported-final-basis.

The maintained owner states that DSM 215c brings the recipe to one litre and assigns per-litre rates. The exact primary only lists 1000 ml water. Matching nominal mass values do not establish measured final volume or that makeup operation. The target reducer rates retain the same unverified denominator.

## Recommended Actions And Acceptance Checks

### a1

After resolving the remaining owner source-basis gaps, regenerate from the verified maintained input. Preserve opaque BHI and do not reapply the unsupported constituent expansion or alter the separate KOMODO child.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Obtain exact source support for the range or revise the maintained owner to preserve pH as unresolved, then regenerate through the normal gated workflow.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Narrow the maintained source wording to printed batch quantities and attach exact evidence. Verify an explicit final-volume instruction before retaining normalized rates as source-authenticated; do not assume a density or different numerical recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch043/425/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/425/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml:1:id: CultureMech:001317<br>./data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml:1:id: CultureMech:001317<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch043/source-preflight-bound/425/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 23 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch043/425/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves with the asserted label. Source product and chemical-form support are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:91248": [{"label": "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Cystein-HCl", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cystein-HCl x 2 H2O (5% (w/v))", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cystein-HCl x 2 H2O (5% (w/v))", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Cysteine hydrochloride", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl x H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl·H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl∙H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl⋅H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--Cysteine HCl H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--Cysteine・HCl・H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--cysteine・HCl・H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--Cysteine・HCL・H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine HCl monohydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine HCl x H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-cysteine HCl.H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine HCl.H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-cysteine hydrochloride hydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine hydrochloride hydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine hydrochloride monohydrate", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine hydrochloride monohydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine hydrochloride--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine hydrochloride--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine monohydrate monochloride", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine monohydrate monochloride", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine-HCl x H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine-HCl·H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine・HCl・H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine・HCl・H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "disodium sulfide--water (1/9)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S . 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O (3% w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O(24% w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S ∙ 9 H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S-9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S·9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S⋅9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S・9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium monosulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfide nonahydrate", "match_type": "ontology_label", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "[OH2]", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dH2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydridooxygen", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydrogen oxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distiled water", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for liquid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for solid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "eau", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H(2)O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "HOH", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen hydroxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "oxidane", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Wasser", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "WATER", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml", "events": 7, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch043/425/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch043/425/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary-bhi | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; primary-bhi exact primary row or paragraph | supports | Exact opaque BHI product batch mass is 37 g. |
| primary-cysteine | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; primary-cysteine exact primary row or paragraph | supports | The supplied L-cysteine hydrochloride hydrate batch mass is 0.25 g. |
| primary-sulfide | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; primary-sulfide exact primary row or paragraph | supports | The supplied sodium sulfide nonahydrate batch mass is 0.25 g. |
| primary-water | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; primary-water exact primary row or paragraph | supports | The primary lists 1000 ml water; no final makeup is printed. |
| primary-preparation | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; primary-preparation exact primary row or paragraph | supports | Anoxic 100% N2 preparation and post-autoclave sterile anoxic reducer additions are explicit; temperature and time are not. |
| variant-glycerol | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; variant-glycerol exact primary row or paragraph | supports | DSM 10643-only stock dose and explicit w/v stock basis; not a generic base addition. |
| variant-haemin-k1 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; variant-haemin-k1 exact primary row or paragraph | supports | DSM 19851-only stock doses, referencing medium 78; not generic base additions. |
| variant-rumen | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf; variant-rumen exact primary row or paragraph | supports | DSM 108840-only rumen-fluid addition has no printed amount. |
| catalog-identity | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 215c row and header | context_only | The catalogue identifies DSM 215c but its IsAerobic true flag does not override the primary anoxic procedure. |
| secondary-product | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Current secondary composition table | context_only | This article does not authenticate the exact inherited commercial product expansion or historical manufacturer edition. |
| bd237500-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.237500; Preserved exact public retrieval result | context_only | Retained supplier attempts do not authenticate the expanded commercial formulation still present in the target. The maintained owner already avoids that expansion. |
| mediadive215capi-attempt | https://mediadive.dsmz.de/rest/medium/215c; Preserved exact public retrieval result | context_only | Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc is not recovered within the bounded search. Decoded historical reports do not authenticate compound identifiers 186, 770, 54 or 4, or the original normalization. There are no attached ingredient amount-evidence objects in the selected target or owner. |
| writer-0 | scripts/repair_komodo_215c_strict_anaerobes_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current exact repair writer declares the four owner ingredients, explicit pH range, per-litre notes and final-water wording. The owner history records the September repair; this code context and current-byte match do not authenticate its scientific source or prove a particular historical execution environment. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch043/425/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Retained supplier attempts do not authenticate the expanded commercial formulation still present in the target. The maintained owner already avoids that expansion.
- Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc is not recovered within the bounded search. Decoded historical reports do not authenticate compound identifiers 186, 770, 54 or 4, or the original normalization. There are no attached ingredient amount-evidence objects in the selected target or owner.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T003340Z-culturemech-001317-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bhi_medium_for_strict_anaerobes (CultureMech:001317)'
started_at: '2026-10-22T00:25:06Z'
finished_at: '2026-10-22T00:33:40Z'
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
summary: The maintained DSM 215c owner already restores the opaque BHI product and
  water, while the generated target retains its older commercial expansion. Both retain
  an unsupported pH range; the owner also asserts unprinted final-volume makeup and
  per-litre rates. The primary supports its four batch ingredients and anoxic procedure,
  but provider identifiers and historical API bytes remain unverified.
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
  - path: data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
    sha256: 52e6267d0697915227d8d8922d5a39c9023bed68b9cb86ef904c992df051243c
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES.yaml
    sha256: 424e228f8e6f4cdcc1163ee0ad427f20fdd00230d1f505406c5c8e04e0ec0a0e
    role: context
  - path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
    sha256: 49a06aefceab81f004db426f88844303951ed9220de4aecf0e43cf551cc1f68d
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES.yaml.md
    sha256: 97e5fd8b1902e1a7461cda4f1cf523f9197bd5558b501c5a242d9bede38651da
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bhi_medium_for_strict_anaerobes.yaml.md
    sha256: 328cea583d05615d20913669e5150d3745134f7fbc5217781d21fcc83c53f142
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_komodo_215c_strict_anaerobes_score15.py
    sha256: 3cfbc577f1346fa1efe5d423822ce4e45b6058238e05b3298cc31dcb5e052f0a
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
  selection: Task review 425; batch 043 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:001317
targets:
- target_id: CultureMech:001317
  path: data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  label: bhi_medium_for_strict_anaerobes
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/425/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/425/strict.tsv"
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001317
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
  - CultureMech:001317
- check_id: bd237500-source-access
  name: 'Exact source content access: bd237500'
  required: true
  status: unavailable
  summary: Retained supplier attempts do not authenticate the expanded commercial
    formulation still present in the target. The maintained owner already avoids that
    expansion.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - bd237500-attempt
- check_id: mediadive215capi-source-access
  name: 'Exact source content access: mediadive215capi'
  required: true
  status: unavailable
  summary: Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc
    is not recovered within the bounded search. Decoded historical reports do not
    authenticate compound identifiers 186, 770, 54 or 4, or the original normalization.
    There are no attached ingredient amount-evidence objects in the selected target
    or owner.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - mediadive215capi-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:48.456660Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/425/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:49.453515Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/425/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:50.561506Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:51.291180Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T00:33:39Z'
  support: supports
  summary: './data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml:1:id: CultureMech:001317

    ./data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml:1:id: CultureMech:001317

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/source-preflight-bound/425/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T00:33:39Z'
  support: supports
  summary: 23 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7746b6814ce5b0f129f6f7160cac0c52f9606f0cbeee202d2a4215309ea0cc33
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/425/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: 6d148c7cda2f68e879eee889a63131d0e55a0158df8f144285822571a0ee892d
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
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Current identifier resolves with the asserted label. Source product and
    chemical-form support are assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:91248":
    [{"label": "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "match_type":
    "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O",
    "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "match_type":
    "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride
    monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED",
    "ambiguity": "unique"}, {"label": "Cystein-HCl", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cystein-HCl x 2
    H2O (5% (w/v))", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Cystein-HCl x 2 H2O (5% (w/v))", "match_type":
    "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride
    monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Cysteine hydrochloride", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl x
    H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Cysteine-HCl·H2O", "match_type": "synonym",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cysteine-HCl∙H2O",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Cysteine-HCl⋅H2O", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--Cysteine HCl
    H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "L--Cysteine・HCl・H2O", "match_type": "synonym",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L--cysteine・HCl・H2O",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "L--Cysteine・HCL・H2O", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id":
    "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "L-Cysteine HCl monohydrate", "match_type": "synonym", "identifier": "CHEBI:91248",
    "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine HCl x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl
    x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "L-Cysteine HCl x H2O", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id":
    "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "L-cysteine HCl.H2O", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "L-cysteine HCl.H2O", "match_type": "synonym",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride monohydrate",
    "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "L-cysteine hydrochloride hydrate", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine hydrochloride
    hydrate", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine hydrochloride monohydrate",
    "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine hydrochloride monohydrate",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "L-cysteine hydrochloride--water (1/1)", "match_type": "synonym",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-cysteine
    hydrochloride--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:91248",
    "preferred_term": "L-Cysteine hydrochloride monohydrate", "ontology_id": "CHEBI:91248",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "L-Cysteine monohydrate
    monochloride", "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term":
    "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "L-Cysteine monohydrate monochloride", "match_type":
    "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine hydrochloride
    monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "L-Cysteine-HCl x H2O", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine-HCl·H2O",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "L-Cysteine・HCl・H2O", "match_type": "synonym", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "L-Cysteine・HCl・H2O",
    "match_type": "synonym", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine
    hydrochloride monohydrate", "ontology_id": "CHEBI:91248", "mapping_status": "REJECTED",
    "ambiguity": "unique"}], "CHEBI:76209": [{"label": "disodium sulfide--water (1/9)",
    "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S
    x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S . 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S
    x 9 H2O (3% w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S x 9 H2O(24% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9H2O", "match_type":
    "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S
    ∙ 9 H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S-9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S.9H2O", "match_type": "synonym",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S·9H2O",
    "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S
    x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S⋅9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S・9H2O", "match_type": "synonym",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    monosulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium sulfide nonahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    sulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15377": [{"label": "[OH2]", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acqua", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agua",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "aqua", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "dH2O", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydridooxygen",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "dihydrogen oxide", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distiled water",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distilled water", "match_type": "preferred_term", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water
    (for liquid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distilled water (for solid medium)", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "eau",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "H(2)O", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "H2O", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "HOH", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen
    hydroxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "oxidane", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Wasser", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "WATER",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml; data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/425/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 840ccb9fa3f4edcd19ae0ad034a4a11ada5e1dd49fa0655d755954a4f610512e
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/425/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: 28ae56671ebe53542a9547d3b325a2912ee9849e2fe791c120bd4f53b32002a1
- evidence_id: primary-bhi
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: primary-bhi exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: Exact opaque BHI product batch mass is 37 g.
  quote: '   Brain heart infusion (DIFCO)                        37.00       g'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: primary-cysteine
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: primary-cysteine exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: The supplied L-cysteine hydrochloride hydrate batch mass is 0.25 g.
  quote: '   L-Cysteine HCl x H2O                                 0.25       g'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: primary-sulfide
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: primary-sulfide exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: The supplied sodium sulfide nonahydrate batch mass is 0.25 g.
  quote: '   Na2S x 9 H2O                                         0.25       g'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: primary-water
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: primary-water exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: The primary lists 1000 ml water; no final makeup is printed.
  quote: '   Distilled water                                   1000.00      ml'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: primary-preparation
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: primary-preparation exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: Anoxic 100% N2 preparation and post-autoclave sterile anoxic reducer additions
    are explicit; temperature and time are not.
  quote: 'Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents
    are added

    after autoclaving from sterile anoxic solutions prepared under N2.'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: variant-glycerol
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: variant-glycerol exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: DSM 10643-only stock dose and explicit w/v stock basis; not a generic base
    addition.
  quote: 'For DSM 10643: Supplement medium with 10.00 ml/l glycerol (87% w/v solution)
    from a

    sterile anoxic stock.'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: variant-haemin-k1
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: variant-haemin-k1 exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: DSM 19851-only stock doses, referencing medium 78; not generic base additions.
  quote: 'For DSM 19851: Supplement medium with 10.0 ml/l haemin and 0.2 ml/l vitamin
    K1

    solution (see medium 78).'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: variant-rumen
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf
  locator: variant-rumen exact primary row or paragraph
  accessed_at: '2026-10-22T00:02:27.708965Z'
  support: supports
  summary: DSM 108840-only rumen-fluid addition has no printed amount.
  quote: 'For DSM 108840: Plus rumen fluid'
  snapshot_sha256: 6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656
- evidence_id: catalog-identity
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 215c row and header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: The catalogue identifies DSM 215c but its IsAerobic true flag does not
    override the primary anoxic procedure.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=215c'\
    \ >215c</a></TD>\n\t\t\t\t\t<TD>BHI medium FOR STRICT ANAEROBES</TD>\n\t\t\t\t\
    \t<TD>null</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t\
    <TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: secondary-product
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Current secondary composition table
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: context_only
  summary: This article does not authenticate the exact inherited commercial product
    expansion or historical manufacturer edition.
  quote: HM infusion powder 12.500 BHI powder 5.000
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: bd237500-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.237500
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:04.060812Z'
  support: context_only
  summary: Retained supplier attempts do not authenticate the expanded commercial
    formulation still present in the target. The maintained owner already avoids that
    expansion.
  snapshot_sha256: 98f5e49148f7da45d2d1ec9ea7d172730bfbeb67c73f74886103fb2499b3b79a
- evidence_id: mediadive215capi-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/215c
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:02:27.709148Z'
  support: context_only
  summary: Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc
    is not recovered within the bounded search. Decoded historical reports do not
    authenticate compound identifiers 186, 770, 54 or 4, or the original normalization.
    There are no attached ingredient amount-evidence objects in the selected target
    or owner.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_komodo_215c_strict_anaerobes_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: The current exact repair writer declares the four owner ingredients, explicit
    pH range, per-litre notes and final-water wording. The owner history records the
    September repair; this code context and current-byte match do not authenticate
    its scientific source or prove a particular historical execution environment.
  snapshot_sha256: 3cfbc577f1346fa1efe5d423822ce4e45b6058238e05b3298cc31dcb5e052f0a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/425/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T00:33:39Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 80cb12755dc6c6c7c10f8ad37710579801fb74e776105f7c41685b8eff8a0e7e
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: concern
  summary: 9 distinct bound ontology IDs have matching nonobsolete labels; 4 provider-ID
    slots lack successful identifier verification. All 3 asserted current CHEBI secondary
    keys have exact index rows; 0 legacy slots are recorded separately. Target primary
    linkage is 8/8 (100.00%) and current secondary linkage is 2/8 (25.00%), on a 0–100
    linkage scale, not a correctness score. Brain/heart anatomy and proteose-peptone
    class identity do not authenticate a commercial BHI composition.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - grounding-inventory
  - mim
  - uberon0000955
  - uberon0000948
  - micro0000180
  - chebi17634
  - chebi26710
  - chebi34683
  - chebi91248
  - chebi76209
  - chebi15377
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Single maintained owner and separate catalogue child
  outcome: supported
  summary: The inspected target and maintained DSM owner both have CultureMech:001317
    and accession 215c. Its single contributor is bhi_medium_for_strict_anaerobes.yaml.
    The linked KOMODO CultureMech:004425 child is a separate record and is not an
    owner of this target. No child or strain-specific quantities are transferred.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - record
  - primary-bhi
  - catalog-identity
  - owner-0
- assessment_id: stale-generation
  area: representation
  topic: Repaired owner versus older generated formulation
  outcome: concern
  summary: The current maintained owner contains BHI, the two reducers and water,
    corresponding to the four primary table identities. The generated target instead
    retains six unverified commercial constituents and omits the opaque product and
    water. Its August merge history precedes the owner September repair entry. This
    observed difference does not establish that the current guarded merger caused
    the old expansion.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - record
  - history-full
  - writer-0
  - primary-bhi
  - primary-water
  - owner-0
- assessment_id: quantity-basis
  area: quantity
  topic: Supported batch masses and unsupported normalization
  outcome: concern
  summary: The primary prints BHI 37 g, each reducer 0.25 g and water 1000 ml. It
    does not print the retained pH range 7.2–7.6 or direct the operator to bring the
    final preparation to one litre. Matching owner mass numerals do not authenticate
    stored g/L or ml/L normalization. The water rate is a plausible nominal convention,
    but its asserted makeup basis is unsupported.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - primary-bhi
  - primary-cysteine
  - primary-sulfide
  - primary-water
  - writer-0
- assessment_id: supplied-forms
  area: grounding
  topic: Correct secondary chemical forms versus unverified provider IDs
  outcome: unknown
  summary: CHEBI:91248 explicitly describes L-cysteine hydrochloride monohydrate and
    CHEBI:76209 sodium sulfide nonahydrate; these match the primary supplied forms.
    CHEBI:15377 supports water identity. Current MIM rows verify those secondary keys.
    The four owner mediadive.compound identifiers remain separate unresolved correspondences,
    not proven wrong IDs and not invented OLS lookups. Anatomy and peptone-class terms
    do not verify the target BHI expansion.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - grounding-inventory
  - mim
  - chebi91248
  - chebi76209
  - chebi15377
  - primary-cysteine
  - primary-sulfide
  - mediadive215capi-attempt
- assessment_id: preparation
  area: scope
  topic: Explicit anaerobic procedure and bounded variant branches
  outcome: supported
  summary: Both selected layers retain 100% N2 and sterile anoxic reducer addition
    after autoclaving; the owner separates the steps. Neither a numeric autoclave
    cycle nor incubation temperature is supplied. The catalogue aerobic flag is not
    a procedural override. Glycerol for DSM 10643, haemin/vitamin K1 for DSM 19851
    and rumen fluid for DSM 108840 remain source-specific branches; they do not establish
    base-medium target organisms or universal additions.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - primary-preparation
  - variant-glycerol
  - variant-haemin-k1
  - variant-rumen
  - catalog-identity
- assessment_id: historical-source
  area: evidence
  topic: Local claims and original response authentication
  outcome: unknown
  summary: The October report preserves four owner amount claims and the preparation
    paragraph as decoded derivative context, including original source hash and access
    time. The separate child report remains relationship context only. General owner
    references and matching current PDF text do not authenticate the historical API
    bytes or constitute attached claim-level amount evidence.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - historical-inventory
  - history-full
  - mediadive215capi-attempt
  - primary-preparation
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 30 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001317
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Generated target:\
    \ Calf brains\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"subject\": \"Generated target: Beef heart\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"subject\": \"Generated target: Proteose peptone\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"subject\": \"Generated target: Dextrose\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"subject\": \"Generated target: Sodium chloride\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"subject\": \"Generated target: Disodium phosphate\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The expanded commercial constituent is\
    \ not authenticated by the opaque product table.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"subject\": \"Generated target: L-Cysteine HCl x H2O\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table cysteine row\",\n        \"exact_source_quote\"\
    : \"   L-Cysteine HCl x H2O                                 0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The supplied-form batch mass is 0.25 g,\
    \ but a measured final volume supporting the stored G_PER_L basis is not established.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\": \"Generated target:\
    \ Na2S x 9 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table sulfide row\",\n        \"exact_source_quote\"\
    : \"   Na2S x 9 H2O                                         0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The supplied-form batch mass is 0.25 g,\
    \ but a measured final volume supporting the stored G_PER_L basis is not established.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"Maintained owner:\
    \ Brain heart infusion\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The four-ingredient representation and\
    \ nominal batch numeral match the primary, but the stored per-litre basis is unverified.\
    \ No final-volume makeup is printed; this is not a proven numerical transcription\
    \ error.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\": \"Maintained\
    \ owner: L-Cysteine HCl x H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table cysteine row\",\n        \"exact_source_quote\"\
    : \"   L-Cysteine HCl x H2O                                 0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The four-ingredient representation and\
    \ nominal batch numeral match the primary, but the stored per-litre basis is unverified.\
    \ No final-volume makeup is printed; this is not a proven numerical transcription\
    \ error.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Maintained\
    \ owner: Na2S x 9 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table sulfide row\",\n        \"exact_source_quote\"\
    : \"   Na2S x 9 H2O                                         0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The four-ingredient representation and\
    \ nominal batch numeral match the primary, but the stored per-litre basis is unverified.\
    \ No final-volume makeup is printed; this is not a proven numerical transcription\
    \ error.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Maintained\
    \ owner: Distilled water\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table water row\",\n        \"exact_source_quote\"\
    : \"   Distilled water                                   1000.00      ml\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The four-ingredient representation and\
    \ nominal batch numeral match the primary, but the stored per-litre basis is unverified.\
    \ No final-volume makeup is printed; this is not a proven numerical transcription\
    \ error.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Target\
    \ tissue-source 200 g/L\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n       \
    \ \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The exact manufacturer edition and internal\
    \ product claim are not authenticated. The repaired owner no longer asserts this\
    \ expansion.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"\
    Target tissue-source 250 g/L\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n       \
    \ \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The exact manufacturer edition and internal\
    \ product claim are not authenticated. The repaired owner no longer asserts this\
    \ expansion.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"subject\": \"\
    Target commercial pH 7.4 ± 0.2\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The exact manufacturer edition and internal\
    \ product claim are not authenticated. The repaired owner no longer asserts this\
    \ expansion.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"subject\": \"\
    Owner ingredient note 1\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 215c lists Brain heart infusion at 37 g/L as an opaque rich-meat product.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The note attributes a per-litre rate or\
    \ final-water makeup to the source; the current primary establishes only the listed\
    \ batch amount and no makeup instruction.\"\n  },\n  {\n    \"decision_id\": \"\
    q17\",\n    \"subject\": \"Owner ingredient note 2\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 215c lists 0.25 g/L L-Cysteine HCl x H2O.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table cysteine row\",\n        \"exact_source_quote\"\
    : \"   L-Cysteine HCl x H2O                                 0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The note attributes a per-litre rate or\
    \ final-water makeup to the source; the current primary establishes only the listed\
    \ batch amount and no makeup instruction.\"\n  },\n  {\n    \"decision_id\": \"\
    q18\",\n    \"subject\": \"Owner ingredient note 3\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 215c lists 0.25 g/L Na2S x 9 H2O.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n       \
    \ \"source_locator\": \"Base table sulfide row\",\n        \"exact_source_quote\"\
    : \"   Na2S x 9 H2O                                         0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The note attributes a per-litre rate or\
    \ final-water makeup to the source; the current primary establishes only the listed\
    \ batch amount and no makeup instruction.\"\n  },\n  {\n    \"decision_id\": \"\
    q19\",\n    \"subject\": \"Owner ingredient note 4\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 215c brings the recipe to one liter with distilled water.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table water row\",\n        \"exact_source_quote\"\
    : \"   Distilled water                                   1000.00      ml\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The note attributes a per-litre rate or\
    \ final-water makeup to the source; the current primary establishes only the listed\
    \ batch amount and no makeup instruction.\"\n  },\n  {\n    \"decision_id\": \"\
    q20\",\n    \"subject\": \"Owner aggregate rate narrative\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"MediaDive and DSMZ\
    \ Medium 215c list BHI Medium for Strict Anaerobes as 37 g/L Brain heart infusion,\
    \ 0.25 g/L L-Cysteine HCl x H2O, 0.25 g/L Na2S x 9 H2O, and distilled water, prepared\
    \ anoxically under 100% N2 with the reducing agents added from sterile anoxic\
    \ solutions after autoclaving.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      },\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n   \
    \     \"source_locator\": \"Base table cysteine row\",\n        \"exact_source_quote\"\
    : \"   L-Cysteine HCl x H2O                                 0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      },\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n   \
    \     \"source_locator\": \"Base table sulfide row\",\n        \"exact_source_quote\"\
    : \"   Na2S x 9 H2O                                         0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      },\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n   \
    \     \"source_locator\": \"Base table water row\",\n        \"exact_source_quote\"\
    : \"   Distilled water                                   1000.00      ml\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      },\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n   \
    \     \"source_locator\": \"Base preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are\
    \ added\\nafter autoclaving from sterile anoxic solutions prepared under N2.\"\
    ,\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The ingredient identities and anoxic procedure\
    \ are supported, but the three per-litre mass assertions are not established by\
    \ the current primary denominator.\"\n  },\n  {\n    \"decision_id\": \"q21\"\
    ,\n    \"subject\": \"Retained pH range 7.2–7.6\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.6\n        }\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.6\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n       \
    \ \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      },\n      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\",\n   \
    \     \"source_locator\": \"Base preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are\
    \ added\\nafter autoclaving from sterile anoxic solutions prepared under N2.\"\
    ,\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Neither the current exact primary nor\
    \ an authenticated historical response establishes this pH interval. No replacement\
    \ value is inferred.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"subject\"\
    : \"Opaque BHI batch representation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table BHI row\",\n        \"exact_source_quote\"\
    : \"   Brain heart infusion (DIFCO)                        37.00       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact printed batch quantity\
    \ with claim-level source attachment. This is a proposed source-bound representation,\
    \ not an additional dose or a new final-volume claim.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"subject\": \"Cysteine hydrate batch mass\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table cysteine row\",\n        \"exact_source_quote\"\
    : \"   L-Cysteine HCl x H2O                                 0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact printed batch quantity\
    \ with claim-level source attachment. This is a proposed source-bound representation,\
    \ not an additional dose or a new final-volume claim.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"subject\": \"Sulfide nonahydrate batch mass\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table sulfide row\",\n        \"exact_source_quote\"\
    : \"   Na2S x 9 H2O                                         0.25       g\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact printed batch quantity\
    \ with claim-level source attachment. This is a proposed source-bound representation,\
    \ not an additional dose or a new final-volume claim.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"subject\": \"Listed batch water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base table water row\",\n        \"exact_source_quote\"\
    : \"   Distilled water                                   1000.00      ml\",\n\
    \        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact printed batch quantity\
    \ with claim-level source attachment. This is a proposed source-bound representation,\
    \ not an additional dose or a new final-volume claim.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"subject\": \"100% N2 and staged sterile reducer procedure\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are\
    \ added after autoclaving from sterile anoxic solutions prepared under N2.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Prepare the medium anoxically under 100% N2 gas atmosphere.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Add L-Cysteine HCl x H2O and Na2S x 9 H2O after autoclaving from sterile anoxic\
    \ solutions prepared under N2.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz215c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are\
    \ added\\nafter autoclaving from sterile anoxic solutions prepared under N2.\"\
    ,\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Exact gas percentage and addition ordering\
    \ are supported in both layers. General references exist on the owner, but no\
    \ matching claim-level evidence is attached to these steps.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q27\",\n    \"subject\": \"Unspecified autoclave cycle and\
    \ incubation temperature\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/merge_yaml/merged/BHI_MEDIUM_FOR_STRICT_ANAEROBES.yaml\"\
    ,\n        \"field_path\": \"temperature\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml\"\
    ,\n        \"field_path\": \"temperature\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"Base preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are\
    \ added\\nafter autoclaving from sterile anoxic solutions prepared under N2.\"\
    ,\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"Autoclaving is mentioned, but no temperature\
    \ or duration is given. No incubation value or default cycle is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q28\",\n    \"subject\": \"DSM 10643 glycerol\
    \ 10 ml/L of 87% w/v stock\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"DSM 10643 glycerol 10 ml/L of 87% w/v stock variant\
    \ paragraph\",\n        \"exact_source_quote\": \"For DSM 10643: Supplement medium\
    \ with 10.00 ml/l glycerol (87% w/v solution) from a\\nsterile anoxic stock.\"\
    ,\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit stock strength and dose are\
    \ supported only for DSM 10643. They are excluded from the base recipe; no replacement\
    \ of the base water or final-volume adjustment is inferred.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q29\",\n    \"subject\": \"DSM 19851 haemin 10 ml/L and vitamin\
    \ K1 0.2 ml/L\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"DSM 19851 haemin 10 ml/L and vitamin K1 0.2 ml/L\
    \ variant paragraph\",\n        \"exact_source_quote\": \"For DSM 19851: Supplement\
    \ medium with 10.0 ml/l haemin and 0.2 ml/l vitamin K1\\nsolution (see medium\
    \ 78).\",\n        \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"These are two variant-only stock doses\
    \ referring to medium 78. No concentration of either stock or generic base addition\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"subject\": \"\
    DSM 108840 rumen-fluid amount\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz215c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf\"\
    ,\n        \"source_locator\": \"DSM 108840 rumen-fluid amount variant paragraph\"\
    ,\n        \"exact_source_quote\": \"For DSM 108840: Plus rumen fluid\",\n   \
    \     \"snapshot_sha256\": \"6ba19870fc0167e0d6f151172abcd95893462757cb1243daa15c433fa4c10656\"\
    ,\n        \"parsed_text_sha256\": \"0d8800edd168d3846034606876fc759da28f1ea2a4eb35c78fd4681cbb71a754\"\
    \n      }\n    ],\n    \"rationale\": \"This variant names rumen fluid without\
    \ an amount. The variant is excluded from the base and no customary amount is\
    \ supplied.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.001317.stale-generated-expansion
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated formulation predates the maintained opaque-product repair
  description: The generated target retains six unverified BHI constituents and lacks
    the BHI product and water entries. The maintained DSM owner already has the source-supported
    four-ingredient representation; it must not be described as still expanded.
  target_ids:
  - CultureMech:001317
  field_paths:
  - ingredients
  - notes
  - curation_history
  evidence_ids:
  - record
  - primary-bhi
  - primary-water
  - history-full
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
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
  issue_key: culturemech.001317.unsupported-ph
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Retained pH range lacks source support
  description: Both target and owner retain pH 7.2–7.6, but the exact primary does
    not specify it and the cited historical API response is unavailable. This is an
    unsupported claim, not proof that a particular alternative pH is correct.
  target_ids:
  - CultureMech:001317
  field_paths:
  - ph_range
  evidence_ids:
  - primary-preparation
  - primary-bhi
  - mediadive215capi-attempt
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
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
  issue_key: culturemech.001317.unsupported-final-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Listed water is described as final-volume makeup
  description: The maintained owner states that DSM 215c brings the recipe to one
    litre and assigns per-litre rates. The exact primary only lists 1000 ml water.
    Matching nominal mass values do not establish measured final volume or that makeup
    operation. The target reducer rates retain the same unverified denominator.
  target_ids:
  - CultureMech:001317
  field_paths:
  - ingredients
  - notes
  evidence_ids:
  - primary-water
  - primary-bhi
  - primary-cysteine
  - primary-sulfide
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: After resolving the remaining owner source-basis gaps, regenerate from
    the verified maintained input. Preserve opaque BHI and do not reapply the unsupported
    constituent expansion or alter the separate KOMODO child.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001317
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
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
  description: Obtain exact source support for the range or revise the maintained
    owner to preserve pH as unresolved, then regenerate through the normal gated workflow.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001317
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
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
  description: Narrow the maintained source wording to printed batch quantities and
    attach exact evidence. Verify an explicit final-volume instruction before retaining
    normalized rates as source-authenticated; do not assume a density or different
    numerical recipe.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001317
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_medium_for_strict_anaerobes.yaml
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
- Retained supplier attempts do not authenticate the expanded commercial formulation
  still present in the target. The maintained owner already avoids that expansion.
- Current API 215c is HTTP 503; historical response SHA 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc
  is not recovered within the bounded search. Decoded historical reports do not authenticate
  compound identifiers 186, 770, 54 or 4, or the original normalization. There are
  no attached ingredient amount-evidence objects in the selected target or owner.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-043
- generated-medium
```
