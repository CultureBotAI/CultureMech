# Source and formulation review: bhis (CultureMech:009362)

- Review: 20261021T235451Z-culturemech-009362-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:44:39Z
- Finished UTC: 2026-10-21T23:54:51Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact TOGO M2814 specifies hemin and menadione in micrograms per millilitre, exposing a 1000-fold unit error in both local layers. Its 1 L BHI agar component was replaced by an unauthenticated commercial-product expansion. Current secondary composition and preparation are not an authenticated specification for catalog 237500; the original BHIS paper remains unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 414; batch 042 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-one task batches contain 410 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 413 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009362 | data/merge_yaml/merged/BHIS.yaml | generated | bhis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009362 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009362 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/414/strict.tsv |
| validate-terms | passed | True | CultureMech:009362 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009362 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009362 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: bd237500 | unavailable | True | CultureMech:009362 | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| Exact source content access: bd237500bio | unavailable | False | CultureMech:009362 | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| Exact source content access: bd237500ifu | unavailable | False | CultureMech:009362 | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| Exact source content access: bd237500ifuCurrentHost | unavailable | False | CultureMech:009362 | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| Exact source content access: bdmanual | unavailable | False | CultureMech:009362 | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| Exact source content access: bhisObserved2001DOI | unavailable | True | CultureMech:009362 | Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived candidate identity remains a lead; original methods were not read. A separate 1999 result and ambiguous search-PDF microgram rendering do not authenticate the original BHIS formula. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009362.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009362.

8 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary and 2/8 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%; secondary 25.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009362.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact M2814 identity and namesake exclusion

identity: supported. Targets: CultureMech:009362.

CultureMech:009362 is the bacterial TOGO M2814 record, with one exact maintained owner. The similarly named specialized CultureMech:015493 is a distinct liquid FEBA/CultureBotHT formulation and its Brachyspira strain/growth evidence is excluded. Current M2814 supports an agar-based recipe; it does not identify the expanded commercial product or a particular strain.

### Original microgram-per-millilitre units

quantity: concern. Targets: CultureMech:009362.

TOGO supplies 50 ug/ml hemin and 0.5 ug/ml menadione. Multiplication by 1000 ml/L and 0.000001 g/ug gives 0.05 g/L and 0.0005 g/L. The local 50 and 0.5 G_PER_L are each 1000-fold larger. This comparison uses explicit receiving concentrations and does not infer a stock dilution or final volume.

### Commercial base and constituent stages

representation: concern. Targets: CultureMech:009362.

Provider specifies 1 L Brain heart infusion (BHI) agar. Both local layers instead expand a claimed Difco/BD 237500 base into tissue placeholders and four numerical constituents, omit the source base dose, and omit an explicit gelling component despite SOLID_AGAR. The secondary article has HM infusion powder and BHI powder, not evidence for 200/250 g tissue inputs. Its matching proteose/glucose/salt numerals do not prove product equivalence. Preserve the known source base stage while resolving the exact commercial form; do not substitute secondary composition or invent an agar dose.

### Chemical, anatomy and mixture identity limits

grounding: supported. Targets: CultureMech:009362.

All asserted labels match current ontology labels, including lowercase proteose peptone. Hemin and menadione identities are consistent with the source names; their quantities are separately wrong. UBERON anatomy does not authenticate infusion yield or tissue input amount. Proteose peptone is a mixture, and the secondary glucose/phosphate names do not establish a specific catalog formulation. Only the two asserted CHEBI-based secondary identities are checked against the current MIM index; no absent linkage or historical legacy claim is invented.

### Preparation, pH and biological scope

completeness: unknown. Targets: CultureMech:009362.

The provider comment supplies a qualitative anaerobic context for unnamed B. fragilis strains on BHIS plates; the parenthetical PMID 2037368 belongs to the alternative basal medium. No strain-level growth result, generic incubation temperature, gas proportion or complete preparation is established. Local pH 7.4 ± 0.2 appears only in commercial constituent notes and has secondary comparison support, not authenticated M2814/product support. Secondary sterilization and fungal procedures are not transferred.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009362.

19 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Hemin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Hemin\",\n          \"volume\": 50,\n          \"unit\": \"ug/ml\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "Original source concentration × 1000 ml/L × 0.000001 g/ug = 0.05 g/L. The local numeral retained in G_PER_L is 1000-fold too large. Preserve literal ug/ml evidence; no stock or medium-volume assumption is involved."
  },
  {
    "decision_id": "q2",
    "subject": "Menadione",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Menadione\",\n          \"volume\": 0.5,\n          \"unit\": \"ug/ml\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "Original source concentration × 1000 ml/L × 0.000001 g/ug = 0.0005 g/L. The local numeral retained in G_PER_L is 1000-fold too large. Preserve literal ug/ml evidence; no stock or medium-volume assumption is involved."
  },
  {
    "decision_id": "q3",
    "subject": "Calf brains tissue placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[2].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[2].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary composition table; distinct powder description",
        "exact_source_quote": "HM infusion powder 12.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "VARIABLE is a local placeholder, not a source declaration of a fixed or titrated amount. Neither the exact TOGO base nor the cited secondary powder row establishes the local tissue input or a tissue-to-infusion conversion. Preserve the unsupported local claim without substituting powder mass."
  },
  {
    "decision_id": "q4",
    "subject": "Beef heart tissue placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[3].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[3].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary composition table; distinct powder description",
        "exact_source_quote": "BHI powder 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "VARIABLE is a local placeholder, not a source declaration of a fixed or titrated amount. Neither the exact TOGO base nor the cited secondary powder row establishes the local tissue input or a tissue-to-infusion conversion. Preserve the unsupported local claim without substituting powder mass."
  },
  {
    "decision_id": "q5",
    "subject": "Proteose peptone expanded product constituent",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[4].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[4].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table unit heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary BHI agar table row",
        "exact_source_quote": "Proteose peptone 10.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The secondary table has the same numerical g/L rate, but exact M2814-to-catalog-product equivalence and product version are unestablished. This does not authenticate the stored receiving-medium constituent rate. Do not replace or rescale it from an adjacent formulation."
  },
  {
    "decision_id": "q6",
    "subject": "Dextrose expanded product constituent",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[5].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[5].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table unit heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary BHI agar table row",
        "exact_source_quote": "Dextrose (Glucose) 2.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The secondary table has the same numerical g/L rate, but exact M2814-to-catalog-product equivalence and product version are unestablished. This does not authenticate the stored receiving-medium constituent rate. Do not replace or rescale it from an adjacent formulation."
  },
  {
    "decision_id": "q7",
    "subject": "Sodium chloride expanded product constituent",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[6].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[6].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table unit heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary BHI agar table row",
        "exact_source_quote": "Sodium chloride 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The secondary table has the same numerical g/L rate, but exact M2814-to-catalog-product equivalence and product version are unestablished. This does not authenticate the stored receiving-medium constituent rate. Do not replace or rescale it from an adjacent formulation."
  },
  {
    "decision_id": "q8",
    "subject": "Disodium phosphate expanded product constituent",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[7].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[7].supplier_catalog",
        "stored": {
          "supplier_name": "Difco/BD Brain Heart Infusion",
          "catalog_number": "237500",
          "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table unit heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary BHI agar table row",
        "exact_source_quote": "Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The secondary table has the same numerical g/L rate, but exact M2814-to-catalog-product equivalence and product version are unestablished. This does not authenticate the stored receiving-medium constituent rate. Do not replace or rescale it from an adjacent formulation."
  },
  {
    "decision_id": "q9",
    "subject": "Source BHI agar base dose",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The exact provider explicitly names 1 L BHI agar as the base component. Restore this source-stage context during authorized curation; it is neither distilled water nor a measured final-volume declaration after supplements."
  },
  {
    "decision_id": "q10",
    "subject": "Solid agar state",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The named agar base supports the selected solid state, but the local representation lacks matching claim-level source linkage and an identifiable agar-containing base. No gelling-agent mass is inferred."
  },
  {
    "decision_id": "q11",
    "subject": "Commercial constituent pH note",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ph",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ph",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "ph_range",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table final sentence",
        "exact_source_quote": "Final pH (at 25°C): 7.4±0.2",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The local note matches a secondary BHI agar pH statement. Catalog version and exact base equivalence remain unverified; no M2814 pH is established, and 25 °C is a measurement qualifier, not incubation."
  },
  {
    "decision_id": "q12",
    "subject": "Generic incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "temperature",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "temperature",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "B. fragilis strains were grown anaerobically in basal medium (PMID: 2037368) or on brain heart infusion (BHI) agar plates supplemented with 50 μg of hemin and 0.5 μg of menadione (BHIS) per ml.",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The provider gives no incubation temperature. Source silence is insufficient evidence, not an explicit no-fixed-amount statement; do not transfer fungal or namesake conditions."
  },
  {
    "decision_id": "q13",
    "subject": "Generic preparation steps",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhis.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2814original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "B. fragilis strains were grown anaerobically in basal medium (PMID: 2037368) or on brain heart infusion (BHI) agar plates supplemented with 50 μg of hemin and 0.5 μg of menadione (BHIS) per ml.",
        "snapshot_sha256": "24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb"
      }
    ],
    "rationale": "The exact source comment is not a full preparation protocol. Secondary procedures remain comparison context and cannot populate this field without product/formulation correspondence."
  },
  {
    "decision_id": "q14",
    "subject": "Secondary HM infusion powder comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table row",
        "exact_source_quote": "HM infusion powder 12.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Retained as an exact secondary source quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield equivalence is established."
  },
  {
    "decision_id": "q15",
    "subject": "Secondary BHI powder comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table row",
        "exact_source_quote": "BHI powder 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Retained as an exact secondary source quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield equivalence is established."
  },
  {
    "decision_id": "q16",
    "subject": "Secondary agar comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table heading",
        "exact_source_quote": "Ingredients Gms/liter",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary table row",
        "exact_source_quote": "Agar 15.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Retained as an exact secondary source quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield equivalence is established."
  },
  {
    "decision_id": "q17",
    "subject": "Secondary reconstitution comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary Preparation and Method of Use",
        "exact_source_quote": "Suspend 52.0 grams in 1000 ml distilled water.",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Exact secondary preparation quantity is recorded only to preserve source scope. It is not authenticated for M2814 or catalog 237500 and is not a proposed operational instruction."
  },
  {
    "decision_id": "q18",
    "subject": "Secondary sterilization comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary Preparation and Method of Use",
        "exact_source_quote": "Sterilize by autoclaving at 15 lbs pressure (121°C) for 15 minutes.",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Exact secondary preparation quantity is recorded only to preserve source scope. It is not authenticated for M2814 or catalog 237500 and is not a proposed operational instruction."
  },
  {
    "decision_id": "q19",
    "subject": "Secondary cooling comparison only",
    "decision": "unsupported",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary Preparation and Method of Use",
        "exact_source_quote": "Cool to 45-50°C.",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "Exact secondary preparation quantity is recorded only to preserve source scope. It is not authenticated for M2814 or catalog 237500 and is not a proposed operational instruction."
  }
]

## Findings

### f1: Hemin and menadione retain microgram numerals as grams per litre

major / open / confirmed; issue key: culturemech.009362.microgram-per-ml-conversion.

Both local layers store 50 G_PER_L hemin and 0.5 G_PER_L menadione. Exact M2814 structured rows and comment specify ug/ml, yielding 0.05 and 0.0005 g/L. Current importer defaulting is a reproducible code-reading risk, not proven historical causation.

### f2: Source BHI agar stage is obscured by an unverified commercial expansion

major / open / confirmed; issue key: culturemech.009362.unverified-commercial-expansion.

The source names 1 L BHI agar. Current target and owner instead assert a catalog 237500 constituent expansion with unsupported 200/250 g tissue notes and omit the base dose. The cited secondary article does not establish this catalog formulation; matching constituent numerals do not resolve the mismatch in source scope.

### f3: Original BHIS paper and strain scope remain unresolved

major / open / confirmed; issue key: culturemech.009362.original-paper-scope-unresolved.

TOGO src_url is empty. The comment cites PMID 2037368 for an alternative basal medium; it is not evidence that this PMID authenticates BHIS. The observed 2001 DOI candidate could not be read, and no strain-specific cultivation assertion can be taken from the unrelated specialized BHIS record.

## Recommended Actions And Acceptance Checks

### a1

Correct only the verified unit-conversion error in the maintained owner under separately authorized curation, attach exact provider evidence and inspect the importer unit fallback before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the exact source base/dose and resolve manufacturer, product form and version before retaining any constituent expansion. Do not invent tissue yield or transfer secondary agar/preparation amounts. Add claim-level evidence and preserve prior history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the exact original BHIS publication and its formulation/strain scope before adding paper-backed growth or preparation evidence. Keep current provider comparisons separate from original-paper authentication.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHIS.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/bhis.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHIS.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHIS.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch042/414/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/414/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHIS.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHIS.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BHIS.yaml:1:id: CultureMech:009362<br>./data/normalized_yaml/bacterial/bhis.yaml:1:id: CultureMech:009362<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch042/source-preflight-bound/414/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 17 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch042/414/grounding-inventory.json; Complete exact-field sidecar | context_only | Every direct primary/current-secondary slot, exact OLS identity/scientific annotation and current MIM row is retained. No canonical-label drift exists in this record. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi28869 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28869; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:28869 resolves to menadione. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50385 resolves to hemin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | MICRO:0000180 resolves to proteose peptone. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | UBERON:0000948 resolves to heart. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | UBERON:0000955 resolves to brain. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:28869": [{"label": "Menadione", "match_type": "preferred_term", "identifier": "CHEBI:28869", "preferred_term": "Menadione", "ontology_id": "CHEBI:28869", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50385": [{"label": "Haemin", "match_type": "preferred_term", "identifier": "CHEBI:50385", "preferred_term": "Haemin", "ontology_id": "CHEBI:50385", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| togo-hemin | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814; $.components[0].items[0] | supports | Exact receiving-stage component name, original number and unit; distinct from a commercial constituent specification. |
| togo-menadione | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814; $.components[0].items[1] | supports | Exact receiving-stage component name, original number and unit; distinct from a commercial constituent specification. |
| togo-base | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814; $.components[0].items[2] | supports | Exact receiving-stage component name, original number and unit; distinct from a commercial constituent specification. |
| togo-comment | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814; $.comments[0].comment, paragraph_index 1 | supports | Published provider comment names anaerobic B. fragilis strains and distinguishes basal medium from BHIS plates. Its PMID attaches to basal medium; no strain, incubation temperature or commercial formula is supplied. |
| secondary-table | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Composition table and adjacent pH sentence | context_only | The cited secondary article gives a different powder-based BHI agar composition. It does not authenticate catalog 237500, a product lot/version, or the local 200/250 g tissue claims. |
| secondary-preparation | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Preparation and Method of Use, first four sentences | context_only | These are secondary BHI agar statements only. They are inventoried without applying a preparation protocol to M2814 or the unverified catalog product. |
| bd237500-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.237500; Preserved exact public retrieval result | context_only | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| bd237500bio-attempt | https://www.bdbiosciences.com/en-ca/products/reagents/dehydrated-culture-media/animal-based-culture-media/brain-heart-infusion-bhi-bottle-500g.237500; Preserved exact public retrieval result | context_only | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| bd237500ifu-attempt | https://legacy.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf; Preserved exact public retrieval result | context_only | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| bd237500ifuCurrentHost-attempt | https://www.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf; Preserved exact public retrieval result | context_only | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| bdmanual-attempt | https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf; Preserved exact public retrieval result | context_only | Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred. |
| bhisObserved2001DOI-attempt | https://doi.org/10.1128/IAI.69.7.4342-4350.2001; Preserved exact public retrieval result | context_only | Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived candidate identity remains a lead; original methods were not read. A separate 1999 result and ambiguous search-PDF microgram rendering do not authenticate the original BHIS formula. |
| history-metadata | data/merge_yaml/merged/BHIS.yaml; data/normalized_yaml/bacterial/bhis.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhis.yaml", "events": 6, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch042/414/history-inventory.json; Complete exact-field sidecar | context_only | All 13 target/owner history events are retained. The March product-expansion note is a local claim, not manufacturer authentication. |
| source-scope | /private/tmp/culturemech-review-work-batch042/414/source-scope-inventory.json; Complete exact-field sidecar | context_only | Complete TOGO formula/comments and explicit exclusions; the two historical growth objects belong only to the excluded specialized namesake and are not transferred. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L; _ingredient_from_item preserves the numeral for this case. This is a present code risk, not historical execution proof. The commercial comparison repair does not name M2814; the CultureBotHT repair explicitly targets the excluded specialized ID 015493. |
| writer-1 | scripts/repair_togo_commercial_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L; _ingredient_from_item preserves the numeral for this case. This is a present code risk, not historical execution proof. The commercial comparison repair does not name M2814; the CultureBotHT repair explicitly targets the excluded specialized ID 015493. |
| writer-2 | scripts/repair_culturebotht_bhis_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L; _ingredient_from_item preserves the numeral for this case. This is a present code risk, not historical execution proof. The commercial comparison repair does not name M2814; the CultureBotHT repair explicitly targets the excluded specialized ID 015493. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch042/414/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve its actual status and original time; no product formula, product absence or historical invalidity is inferred.
- Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived candidate identity remains a lead; original methods were not read. A separate 1999 result and ambiguous search-PDF microgram rendering do not authenticate the original BHIS formula.
- All current asserted ontology labels match; the Proteose capitalization defect in record 413 does not apply here.
- The secondary article was read as cited comparison context. Its fungal variants, antibiotics, blood additions and incubation ranges are excluded from M2814; no cross-record growth claims are added.
- This is a record audit with proposed bounded curation only. No recipe, preparation protocol, source cache or native saved review was changed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T235451Z-culturemech-009362-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bhis (CultureMech:009362)'
started_at: '2026-10-21T23:44:39Z'
finished_at: '2026-10-21T23:54:51Z'
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
summary: Exact TOGO M2814 specifies hemin and menadione in micrograms per millilitre,
  exposing a 1000-fold unit error in both local layers. Its 1 L BHI agar component
  was replaced by an unauthenticated commercial-product expansion. Current secondary
  composition and preparation are not an authenticated specification for catalog 237500;
  the original BHIS paper remains unresolved.
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
  - path: data/merge_yaml/merged/BHIS.yaml
    sha256: 4438e6725701cdbbeb7c3f7e415ed8e85f1565b9b5bbd0c04bea6beb90c2ad40
    role: target
  - path: data/normalized_yaml/bacterial/bhis.yaml
    sha256: 0acacc8bfd30711e2df753d5485e08cbfb7b85a060760b00f315a70f6d73bda3
    role: context
  - path: data/normalized_yaml/specialized/bhis.yaml
    sha256: 99440736e3f52ced80b9d46e474b71c74111e8a6f6a272b75b13a8842788ed6f
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_culturebotht_bhis_score15.py
    sha256: a600d3cf5286268fc003f713557588bab018e95fdac24bbbcdcea558753677e6
    role: context
  - path: scripts/repair_togo_commercial_score20.py
    sha256: d5e34df82098bf7558fcdd103d24d00218513488ea860952881c73240596c822
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
  - path: tests/test_togo_importer.py
    sha256: baa0eb5bdaf0bab64658eb6f64981a4fc99d7d913a6efd4ee6f223f58d1995e5
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 414; batch 042 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-one task batches
    contain 410 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 413 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009362
targets:
- target_id: CultureMech:009362
  path: data/merge_yaml/merged/BHIS.yaml
  label: bhis
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHIS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHIS.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch042/414/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/414/strict.tsv"
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHIS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHIS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009362
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
  - CultureMech:009362
- check_id: bd237500-source-access
  name: 'Exact source content access: bd237500'
  required: true
  status: unavailable
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bd237500-attempt
- check_id: bd237500bio-source-access
  name: 'Exact source content access: bd237500bio'
  required: false
  status: unavailable
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bd237500bio-attempt
- check_id: bd237500ifu-source-access
  name: 'Exact source content access: bd237500ifu'
  required: false
  status: unavailable
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bd237500ifu-attempt
- check_id: bd237500ifuCurrentHost-source-access
  name: 'Exact source content access: bd237500ifuCurrentHost'
  required: false
  status: unavailable
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bd237500ifuCurrentHost-attempt
- check_id: bdmanual-source-access
  name: 'Exact source content access: bdmanual'
  required: false
  status: unavailable
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bdmanual-attempt
- check_id: bhisObserved2001DOI-source-access
  name: 'Exact source content access: bhisObserved2001DOI'
  required: true
  status: unavailable
  summary: Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived
    candidate identity remains a lead; original methods were not read. A separate
    1999 result and ambiguous search-PDF microgram rendering do not authenticate the
    original BHIS formula.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - bhisObserved2001DOI-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHIS.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/bhis.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHIS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:05.337135Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHIS.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch042/414/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:06.341769Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/414/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHIS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:07.454002Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHIS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:08.202168Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:54:50Z'
  support: supports
  summary: './data/merge_yaml/merged/BHIS.yaml:1:id: CultureMech:009362

    ./data/normalized_yaml/bacterial/bhis.yaml:1:id: CultureMech:009362

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/source-preflight-bound/414/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:54:50Z'
  support: supports
  summary: 17 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: f8c3dbf597ade8b0ac08daa026e05c6be2cd53a31bdbd1fc5ebdd703f5f6f56e
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/414/grounding-inventory.json
  locator: Complete exact-field sidecar
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Every direct primary/current-secondary slot, exact OLS identity/scientific
    annotation and current MIM row is retained. No canonical-label drift exists in
    this record.
  snapshot_sha256: b151da8afd983e827b640396090f903bb09dc163920ee86d7d87ee01b836eb6e
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
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
- evidence_id: chebi28869
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28869
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.892502Z'
  support: supports
  summary: CHEBI:28869 resolves to menadione. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 7d5bbd9644ae17adf1a4cf5660c04a06c2db3430709c2a0d2da9a026611d9444
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi50385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.648821Z'
  support: supports
  summary: CHEBI:50385 resolves to hemin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b989203634707b89526a8664c8fa65cb4976c4cdd791427218cf01b37d17356e
- evidence_id: micro0000180
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:24.290496Z'
  support: supports
  summary: MICRO:0000180 resolves to proteose peptone. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: b3a39a531c5ab5508a297228d13ba81c99899b041d5292a9d668eded939bfe73
- evidence_id: uberon0000948
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:24.915343Z'
  support: supports
  summary: UBERON:0000948 resolves to heart. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: c658bbcacd89befa47e3bd4859f176db247b3ce67483b6590c91d0865d41aed4
- evidence_id: uberon0000955
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:25.122940Z'
  support: supports
  summary: UBERON:0000955 resolves to brain. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ce200fe58b82652d0f04310c92d23633919fa6ad6aee2a17c6b25c2e490a8877
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T23:54:50Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:28869":
    [{"label": "Menadione", "match_type": "preferred_term", "identifier": "CHEBI:28869",
    "preferred_term": "Menadione", "ontology_id": "CHEBI:28869", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:50385": [{"label": "Haemin", "match_type":
    "preferred_term", "identifier": "CHEBI:50385", "preferred_term": "Haemin", "ontology_id":
    "CHEBI:50385", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: togo-hemin
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814
  locator: $.components[0].items[0]
  accessed_at: '2026-10-21T23:23:51.208066Z'
  support: supports
  summary: Exact receiving-stage component name, original number and unit; distinct
    from a commercial constituent specification.
  quote: "\"component_name\": \"Hemin\",\n          \"volume\": 50,\n          \"\
    unit\": \"ug/ml\""
  snapshot_sha256: 24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb
- evidence_id: togo-menadione
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814
  locator: $.components[0].items[1]
  accessed_at: '2026-10-21T23:23:51.208066Z'
  support: supports
  summary: Exact receiving-stage component name, original number and unit; distinct
    from a commercial constituent specification.
  quote: "\"component_name\": \"Menadione\",\n          \"volume\": 0.5,\n       \
    \   \"unit\": \"ug/ml\""
  snapshot_sha256: 24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb
- evidence_id: togo-base
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814
  locator: $.components[0].items[2]
  accessed_at: '2026-10-21T23:23:51.208066Z'
  support: supports
  summary: Exact receiving-stage component name, original number and unit; distinct
    from a commercial constituent specification.
  quote: "\"component_name\": \"Brain heart infusion (BHI) agar\",\n          \"volume\"\
    : 1,\n          \"unit\": \"L\""
  snapshot_sha256: 24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb
- evidence_id: togo-comment
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814
  locator: $.comments[0].comment, paragraph_index 1
  accessed_at: '2026-10-21T23:23:51.208066Z'
  support: supports
  summary: Published provider comment names anaerobic B. fragilis strains and distinguishes
    basal medium from BHIS plates. Its PMID attaches to basal medium; no strain, incubation
    temperature or commercial formula is supplied.
  quote: 'B. fragilis strains were grown anaerobically in basal medium (PMID: 2037368)
    or on brain heart infusion (BHI) agar plates supplemented with 50 μg of hemin
    and 0.5 μg of menadione (BHIS) per ml.'
  snapshot_sha256: 24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb
- evidence_id: secondary-table
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Composition table and adjacent pH sentence
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: context_only
  summary: The cited secondary article gives a different powder-based BHI agar composition.
    It does not authenticate catalog 237500, a product lot/version, or the local 200/250
    g tissue claims.
  quote: 'Ingredients Gms/liter HM infusion powder 12.500 BHI powder 5.000 Proteose
    peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate
    2.500 Agar 15.000 Final pH (at 25°C): 7.4±0.2'
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: secondary-preparation
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Preparation and Method of Use, first four sentences
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: context_only
  summary: These are secondary BHI agar statements only. They are inventoried without
    applying a preparation protocol to M2814 or the unverified catalog product.
  quote: Suspend 52.0 grams in 1000 ml distilled water. Heat to boiling to dissolve
    the medium completely. Sterilize by autoclaving at 15 lbs pressure (121°C) for
    15 minutes. Cool to 45-50°C.
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: bd237500-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.237500
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:04.060812Z'
  support: context_only
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  snapshot_sha256: 98f5e49148f7da45d2d1ec9ea7d172730bfbeb67c73f74886103fb2499b3b79a
- evidence_id: bd237500bio-attempt
  kind: database
  reference: https://www.bdbiosciences.com/en-ca/products/reagents/dehydrated-culture-media/animal-based-culture-media/brain-heart-infusion-bhi-bottle-500g.237500
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:04.145147Z'
  support: context_only
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  snapshot_sha256: 820f0991d997705f9921056612c0053aeeee5721a5a6fe2eed1750cad2c18989
- evidence_id: bd237500ifu-attempt
  kind: database
  reference: https://legacy.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:00.842104Z'
  support: context_only
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
- evidence_id: bd237500ifuCurrentHost-attempt
  kind: database
  reference: https://www.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:47.611881Z'
  support: context_only
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  snapshot_sha256: bf45a24f9aa2b1afed80c3baacc612a4d85a64fe9186868cb28d6454b3962efe
- evidence_id: bdmanual-attempt
  kind: database
  reference: https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:47.611109Z'
  support: context_only
  summary: Exact manufacturer/product access did not supply a usable specification.
    Preserve its actual status and original time; no product formula, product absence
    or historical invalidity is inferred.
  snapshot_sha256: 493fda53120050f85836032324409be6c6484f90a0755ae0c6a673ba7626818b
- evidence_id: bhisObserved2001DOI-attempt
  kind: database
  reference: https://doi.org/10.1128/IAI.69.7.4342-4350.2001
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T23:28:22.035131Z'
  support: context_only
  summary: Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived
    candidate identity remains a lead; original methods were not read. A separate
    1999 result and ambiguous search-PDF microgram rendering do not authenticate the
    original BHIS formula.
  snapshot_sha256: f2288ed3ae9823bf7b190be210b718e6538127a4554dc5d425691d4ec2495a8e
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHIS.yaml; data/normalized_yaml/bacterial/bhis.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhis.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/414/history-inventory.json
  locator: Complete exact-field sidecar
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: All 13 target/owner history events are retained. The March product-expansion
    note is a local claim, not manufacturer authentication.
  snapshot_sha256: 90116968675dc0c938e1bdc3ccd6497da38f345cfc1ccb2bc295368d4972411c
- evidence_id: source-scope
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/414/source-scope-inventory.json
  locator: Complete exact-field sidecar
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Complete TOGO formula/comments and explicit exclusions; the two historical
    growth objects belong only to the excluded specialized namesake and are not transferred.
  snapshot_sha256: d3fc8ff640df3abfb5b5a79ef471d8d21b763e450d92b5c4ee3c66b266d6d0ff
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L;
    _ingredient_from_item preserves the numeral for this case. This is a present code
    risk, not historical execution proof. The commercial comparison repair does not
    name M2814; the CultureBotHT repair explicitly targets the excluded specialized
    ID 015493.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/repair_togo_commercial_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L;
    _ingredient_from_item preserves the numeral for this case. This is a present code
    risk, not historical execution proof. The commercial comparison repair does not
    name M2814; the CultureBotHT repair explicitly targets the excluded specialized
    ID 015493.
  snapshot_sha256: d5e34df82098bf7558fcdd103d24d00218513488ea860952881c73240596c822
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_culturebotht_bhis_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Current _parse_unit has no ug/ml entry and defaults unknown units to G_PER_L;
    _ingredient_from_item preserves the numeral for this case. This is a present code
    risk, not historical execution proof. The commercial comparison repair does not
    name M2814; the CultureBotHT repair explicitly targets the excluded specialized
    ID 015493.
  snapshot_sha256: a600d3cf5286268fc003f713557588bab018e95fdac24bbbcdcea558753677e6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/414/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:54:50Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 20ca661bbd452b2bba27f359a59f8204bcb56ef1c5a71816207baa93197aa659
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '8 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary
    and 2/8 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17634
  - chebi26710
  - chebi28869
  - chebi34683
  - chebi50385
  - micro0000180
  - uberon0000948
  - uberon0000955
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%;
    secondary 25.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact M2814 identity and namesake exclusion
  outcome: supported
  summary: CultureMech:009362 is the bacterial TOGO M2814 record, with one exact maintained
    owner. The similarly named specialized CultureMech:015493 is a distinct liquid
    FEBA/CultureBotHT formulation and its Brachyspira strain/growth evidence is excluded.
    Current M2814 supports an agar-based recipe; it does not identify the expanded
    commercial product or a particular strain.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - owner-0
  - togo-base
  - togo-comment
  - source-scope
- assessment_id: units
  area: quantity
  topic: Original microgram-per-millilitre units
  outcome: concern
  summary: TOGO supplies 50 ug/ml hemin and 0.5 ug/ml menadione. Multiplication by
    1000 ml/L and 0.000001 g/ug gives 0.05 g/L and 0.0005 g/L. The local 50 and 0.5
    G_PER_L are each 1000-fold larger. This comparison uses explicit receiving concentrations
    and does not infer a stock dilution or final volume.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - owner-0
  - togo-hemin
  - togo-menadione
  - quantity-inventory
  - writer-0
- assessment_id: base
  area: representation
  topic: Commercial base and constituent stages
  outcome: concern
  summary: Provider specifies 1 L Brain heart infusion (BHI) agar. Both local layers
    instead expand a claimed Difco/BD 237500 base into tissue placeholders and four
    numerical constituents, omit the source base dose, and omit an explicit gelling
    component despite SOLID_AGAR. The secondary article has HM infusion powder and
    BHI powder, not evidence for 200/250 g tissue inputs. Its matching proteose/glucose/salt
    numerals do not prove product equivalence. Preserve the known source base stage
    while resolving the exact commercial form; do not substitute secondary composition
    or invent an agar dose.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - owner-0
  - togo-base
  - secondary-table
  - bd237500-attempt
  - quantity-inventory
- assessment_id: grounding-scope
  area: grounding
  topic: Chemical, anatomy and mixture identity limits
  outcome: supported
  summary: All asserted labels match current ontology labels, including lowercase
    proteose peptone. Hemin and menadione identities are consistent with the source
    names; their quantities are separately wrong. UBERON anatomy does not authenticate
    infusion yield or tissue input amount. Proteose peptone is a mixture, and the
    secondary glucose/phosphate names do not establish a specific catalog formulation.
    Only the two asserted CHEBI-based secondary identities are checked against the
    current MIM index; no absent linkage or historical legacy claim is invented.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - grounding-inventory
  - chebi50385
  - chebi28869
  - uberon0000955
  - uberon0000948
  - micro0000180
  - mim
- assessment_id: conditions
  area: completeness
  topic: Preparation, pH and biological scope
  outcome: unknown
  summary: The provider comment supplies a qualitative anaerobic context for unnamed
    B. fragilis strains on BHIS plates; the parenthetical PMID 2037368 belongs to
    the alternative basal medium. No strain-level growth result, generic incubation
    temperature, gas proportion or complete preparation is established. Local pH 7.4
    ± 0.2 appears only in commercial constituent notes and has secondary comparison
    support, not authenticated M2814/product support. Secondary sterilization and
    fungal procedures are not transferred.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - togo-comment
  - secondary-table
  - secondary-preparation
  - bhisObserved2001DOI-attempt
  - source-scope
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 19 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009362
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Hemin\",\n  \
    \  \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BHIS.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"50\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2814original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Hemin\\\",\\n          \\\"volume\\\": 50,\\n\
    \          \\\"unit\\\": \\\"ug/ml\\\"\",\n        \"snapshot_sha256\": \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\
    \n      }\n    ],\n    \"rationale\": \"Original source concentration × 1000 ml/L\
    \ × 0.000001 g/ug = 0.05 g/L. The local numeral retained in G_PER_L is 1000-fold\
    \ too large. Preserve literal ug/ml evidence; no stock or medium-volume assumption\
    \ is involved.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\": \"\
    Menadione\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"togoM2814original\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Menadione\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"ug/ml\\\"\",\n        \"snapshot_sha256\": \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\
    \n      }\n    ],\n    \"rationale\": \"Original source concentration × 1000 ml/L\
    \ × 0.000001 g/ug = 0.0005 g/L. The local numeral retained in G_PER_L is 1000-fold\
    \ too large. Preserve literal ug/ml evidence; no stock or medium-volume assumption\
    \ is involved.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"\
    Calf brains tissue placeholder\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"field_path\"\
    : \"ingredients[2].notes\",\n        \"stored\": \"infusion from 200 g/L; Tissue\
    \ infusion - source material is calf brain tissue; Constituent of Brain Heart\
    \ Infusion commercial product\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM2814original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\"\
    : \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Secondary composition table; distinct powder description\",\n        \"exact_source_quote\"\
    : \"HM infusion powder 12.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"VARIABLE is a local placeholder, not a\
    \ source declaration of a fixed or titrated amount. Neither the exact TOGO base\
    \ nor the cited secondary powder row establishes the local tissue input or a tissue-to-infusion\
    \ conversion. Preserve the unsupported local claim without substituting powder\
    \ mass.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"subject\": \"Beef heart\
    \ tissue placeholder\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"field_path\"\
    : \"ingredients[3].notes\",\n        \"stored\": \"infusion from 250 g/L; Tissue\
    \ infusion - source material is beef/ox heart tissue; Constituent of Brain Heart\
    \ Infusion commercial product\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM2814original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\"\
    : \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Secondary composition table; distinct powder description\",\n        \"exact_source_quote\"\
    : \"BHI powder 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"VARIABLE is a local placeholder, not a\
    \ source declaration of a fixed or titrated amount. Neither the exact TOGO base\
    \ nor the cited secondary powder row establishes the local tissue input or a tissue-to-infusion\
    \ conversion. Preserve the unsupported local claim without substituting powder\
    \ mass.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"subject\": \"Proteose\
    \ peptone expanded product constituent\",\n    \"decision\": \"unsupported\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table unit heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary BHI agar table row\",\n        \"exact_source_quote\"\
    : \"Proteose peptone 10.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"togoM2814original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary table has the same numerical g/L\
    \ rate, but exact M2814-to-catalog-product equivalence and product version are\
    \ unestablished. This does not authenticate the stored receiving-medium constituent\
    \ rate. Do not replace or rescale it from an adjacent formulation.\"\n  },\n \
    \ {\n    \"decision_id\": \"q6\",\n    \"subject\": \"Dextrose expanded product\
    \ constituent\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n \
    \       \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n\
    \        \"field_path\": \"ingredients[5].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table unit heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary BHI agar table row\",\n        \"exact_source_quote\"\
    : \"Dextrose (Glucose) 2.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"togoM2814original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary table has the same numerical g/L\
    \ rate, but exact M2814-to-catalog-product equivalence and product version are\
    \ unestablished. This does not authenticate the stored receiving-medium constituent\
    \ rate. Do not replace or rescale it from an adjacent formulation.\"\n  },\n \
    \ {\n    \"decision_id\": \"q7\",\n    \"subject\": \"Sodium chloride expanded\
    \ product constituent\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n     \
    \   \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n\
    \        \"field_path\": \"ingredients[6].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table unit heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary BHI agar table row\",\n        \"exact_source_quote\"\
    : \"Sodium chloride 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"togoM2814original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary table has the same numerical g/L\
    \ rate, but exact M2814-to-catalog-product equivalence and product version are\
    \ unestablished. This does not authenticate the stored receiving-medium constituent\
    \ rate. Do not replace or rescale it from an adjacent formulation.\"\n  },\n \
    \ {\n    \"decision_id\": \"q8\",\n    \"subject\": \"Disodium phosphate expanded\
    \ product constituent\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n     \
    \   \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n\
    \        \"field_path\": \"ingredients[7].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].supplier_catalog\",\n        \"stored\"\
    : {\n          \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n       \
    \   \"catalog_number\": \"237500\",\n          \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table unit heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary BHI agar table row\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"togoM2814original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary table has the same numerical g/L\
    \ rate, but exact M2814-to-catalog-product equivalence and product version are\
    \ unestablished. This does not authenticate the stored receiving-medium constituent\
    \ rate. Do not replace or rescale it from an adjacent formulation.\"\n  },\n \
    \ {\n    \"decision_id\": \"q9\",\n    \"subject\": \"Source BHI agar base dose\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM2814original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\",\n\
    \        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The exact provider explicitly names 1 L BHI\
    \ agar as the base component. Restore this source-stage context during authorized\
    \ curation; it is neither distilled water nor a measured final-volume declaration\
    \ after supplements.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\"\
    : \"Solid agar state\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n     \
    \   \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2814original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion (BHI) agar\\\",\\n      \
    \    \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\n     \
    \ }\n    ],\n    \"rationale\": \"The named agar base supports the selected solid\
    \ state, but the local representation lacks matching claim-level source linkage\
    \ and an identifiable agar-containing base. No gelling-agent mass is inferred.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Commercial constituent\
    \ pH note\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n        \"field_path\"\
    : \"ingredients[7].notes\",\n        \"stored\": \"pH buffer (final pH 7.4 ± 0.2);\
    \ Constituent of Brain Heart Infusion commercial product\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"\
    field_path\": \"ingredients[7].notes\",\n        \"stored\": \"pH buffer (final\
    \ pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product\"\n  \
    \    },\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n \
    \       \"field_path\": \"ph\",\n        \"stored\": null\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"\
    field_path\": \"ph\",\n        \"stored\": null\n      },\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BHIS.yaml\",\n        \"field_path\": \"ph_range\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"microbenotesBHI\"\
    ,\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table final sentence\",\n        \"\
    exact_source_quote\": \"Final pH (at 25°C): 7.4±0.2\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The local note matches a secondary BHI\
    \ agar pH statement. Catalog version and exact base equivalence remain unverified;\
    \ no M2814 pH is established, and 25 °C is a measurement qualifier, not incubation.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Generic incubation\
    \ temperature\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\",\n        \"\
    field_path\": \"temperature\",\n        \"stored\": null\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\",\n        \"\
    field_path\": \"temperature\",\n        \"stored\": null\n      }\n    ],\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"togoM2814original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"B. fragilis strains were grown anaerobically in basal medium (PMID: 2037368)\
    \ or on brain heart infusion (BHI) agar plates supplemented with 50 μg of hemin\
    \ and 0.5 μg of menadione (BHIS) per ml.\",\n        \"snapshot_sha256\": \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\
    \n      }\n    ],\n    \"rationale\": \"The provider gives no incubation temperature.\
    \ Source silence is insufficient evidence, not an explicit no-fixed-amount statement;\
    \ do not transfer fungal or namesake conditions.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"subject\": \"Generic preparation steps\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhis.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2814original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2814\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"B. fragilis strains were grown anaerobically in basal medium (PMID: 2037368)\
    \ or on brain heart infusion (BHI) agar plates supplemented with 50 μg of hemin\
    \ and 0.5 μg of menadione (BHIS) per ml.\",\n        \"snapshot_sha256\": \"24cfb07c464af39e5d382a5fbe1dfa8c11dc57619dc574a4b065549cb3766acb\"\
    \n      }\n    ],\n    \"rationale\": \"The exact source comment is not a full\
    \ preparation protocol. Secondary procedures remain comparison context and cannot\
    \ populate this field without product/formulation correspondence.\"\n  },\n  {\n\
    \    \"decision_id\": \"q14\",\n    \"subject\": \"Secondary HM infusion powder\
    \ comparison only\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"microbenotesBHI\"\
    ,\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary table row\",\n        \"exact_source_quote\"\
    : \"HM infusion powder 12.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Retained as an exact secondary source\
    \ quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield\
    \ equivalence is established.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n  \
    \  \"subject\": \"Secondary BHI powder comparison only\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary table row\",\n        \"exact_source_quote\"\
    : \"BHI powder 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Retained as an exact secondary source\
    \ quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield\
    \ equivalence is established.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n  \
    \  \"subject\": \"Secondary agar comparison only\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary table heading\",\n        \"exact_source_quote\"\
    : \"Ingredients Gms/liter\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary table row\",\n        \"exact_source_quote\"\
    : \"Agar 15.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Retained as an exact secondary source\
    \ quantity, not a proposed M2814 addition. No manufacturer/version or tissue-yield\
    \ equivalence is established.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n  \
    \  \"subject\": \"Secondary reconstitution comparison only\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\":\
    \ \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Secondary Preparation and Method of Use\",\n        \"exact_source_quote\"\
    : \"Suspend 52.0 grams in 1000 ml distilled water.\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Exact secondary preparation quantity is\
    \ recorded only to preserve source scope. It is not authenticated for M2814 or\
    \ catalog 237500 and is not a proposed operational instruction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q18\",\n    \"subject\": \"Secondary sterilization comparison\
    \ only\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"microbenotesBHI\"\
    ,\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary Preparation and Method of Use\",\n\
    \        \"exact_source_quote\": \"Sterilize by autoclaving at 15 lbs pressure\
    \ (121°C) for 15 minutes.\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Exact secondary preparation quantity is\
    \ recorded only to preserve source scope. It is not authenticated for M2814 or\
    \ catalog 237500 and is not a proposed operational instruction.\"\n  },\n  {\n\
    \    \"decision_id\": \"q19\",\n    \"subject\": \"Secondary cooling comparison\
    \ only\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"microbenotesBHI\"\
    ,\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"Secondary Preparation and Method of Use\",\n\
    \        \"exact_source_quote\": \"Cool to 45-50°C.\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"Exact secondary preparation quantity is\
    \ recorded only to preserve source scope. It is not authenticated for M2814 or\
    \ catalog 237500 and is not a proposed operational instruction.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.009362.microgram-per-ml-conversion
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Hemin and menadione retain microgram numerals as grams per litre
  description: Both local layers store 50 G_PER_L hemin and 0.5 G_PER_L menadione.
    Exact M2814 structured rows and comment specify ug/ml, yielding 0.05 and 0.0005
    g/L. Current importer defaulting is a reproducible code-reading risk, not proven
    historical causation.
  target_ids:
  - CultureMech:009362
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  evidence_ids:
  - togo-hemin
  - togo-menadione
  - togo-comment
  - quantity-inventory
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: current unit parser and ingredient conversion context
  rule_id: P2 incorrect concentration units
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.009362.unverified-commercial-expansion
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Source BHI agar stage is obscured by an unverified commercial expansion
  description: The source names 1 L BHI agar. Current target and owner instead assert
    a catalog 237500 constituent expansion with unsupported 200/250 g tissue notes
    and omit the base dose. The cited secondary article does not establish this catalog
    formulation; matching constituent numerals do not resolve the mismatch in source
    scope.
  target_ids:
  - CultureMech:009362
  field_paths:
  - ingredients
  - physical_state
  - notes
  evidence_ids:
  - togo-base
  - secondary-table
  - bd237500-attempt
  - quantity-inventory
  - source-scope
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2 source-stage and product identity correspondence
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.009362.original-paper-scope-unresolved
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Original BHIS paper and strain scope remain unresolved
  description: TOGO src_url is empty. The comment cites PMID 2037368 for an alternative
    basal medium; it is not evidence that this PMID authenticates BHIS. The observed
    2001 DOI candidate could not be read, and no strain-specific cultivation assertion
    can be taken from the unrelated specialized BHIS record.
  target_ids:
  - CultureMech:009362
  field_paths:
  - media_term
  - references
  - notes
  evidence_ids:
  - togo-comment
  - bhisObserved2001DOI-attempt
  - source-scope
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2 unresolved source identity and claim scope
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Correct only the verified unit-conversion error in the maintained owner
    under separately authorized curation, attach exact provider evidence and inspect
    the importer unit fallback before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009362
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: current unit parser and ingredient conversion context
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
  description: Preserve the exact source base/dose and resolve manufacturer, product
    form and version before retaining any constituent expansion. Do not invent tissue
    yield or transfer secondary agar/preparation amounts. Add claim-level evidence
    and preserve prior history.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009362
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
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
  description: Resolve the exact original BHIS publication and its formulation/strain
    scope before adding paper-backed growth or preparation evidence. Keep current
    provider comparisons separate from original-paper authentication.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009362
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhis.yaml
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
- Exact manufacturer/product access did not supply a usable specification. Preserve
  its actual status and original time; no product formula, product absence or historical
  invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve
  its actual status and original time; no product formula, product absence or historical
  invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve
  its actual status and original time; no product formula, product absence or historical
  invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve
  its actual status and original time; no product formula, product absence or historical
  invalidity is inferred.
- Exact manufacturer/product access did not supply a usable specification. Preserve
  its actual status and original time; no product formula, product absence or historical
  invalidity is inferred.
- Observed DOI 10.1128/IAI.69.7.4342-4350.2001 returned HTTP 403. The search-derived
  candidate identity remains a lead; original methods were not read. A separate 1999
  result and ambiguous search-PDF microgram rendering do not authenticate the original
  BHIS formula.
- All current asserted ontology labels match; the Proteose capitalization defect in
  record 413 does not apply here.
- The secondary article was read as cited comparison context. Its fungal variants,
  antibiotics, blood additions and incubation ranges are excluded from M2814; no cross-record
  growth claims are added.
- This is a record audit with proposed bounded curation only. No recipe, preparation
  protocol, source cache or native saved review was changed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-042
- generated-medium
```
