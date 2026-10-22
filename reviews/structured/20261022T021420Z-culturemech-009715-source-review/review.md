# Source and formulation review: brain_heart_infusion_agar_with_soil_extract (CultureMech:009715)

- Review: 20261022T021420Z-culturemech-009715-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T02:02:38Z
- Finished UTC: 2026-10-22T02:14:20Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated soil-extract record combines six maintained contributors from four distinct collection formulations. Current primaries support opaque BHI product amounts, separate glucose/salt/agar additions and a 1 L soil-extract input; they do not authenticate the shared commercial constituent expansion or tissue-equivalence claims.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 444; batch 045 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-four task batches contain 440 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 443 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009715 | data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml | generated | brain_heart_infusion_agar_with_soil_extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009715 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009715 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/444/strict.tsv |
| validate-terms | passed | True | CultureMech:009715 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009715 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009715 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive82api | unavailable | False | CultureMech:009715 | The exact current MediaDive82 request returned HTTP503. Complete collection primaries and current provider text remain available; no failed response authenticates historical amounts. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009715.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:009715.

8 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly. 3/3 asserted current secondary keys have exact pinned index rows. Target primary linkage is 8/8 (100.00%) and current secondary linkage is 2/8 (25.00%) on a 0–100 linkage scale, not a correctness score. Current missing keys do not prove historical invalidity; compatible generic source wording does not establish a stereochemical conflict.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:009715.

46 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Four collection formulations in one generated contributor set

identity: concern. Targets: CultureMech:009715.

DSM82 uses 18.5 g BHI plus 5 g glucose and 12 g agar. JCM28 uses 37 g BHI and 15 g agar in 1 L water; JCM263 additionally uses 20 g NaCl. JCM342/M337 instead uses 37 g BHI and 15 g agar with 1 L soil extract. The generated record retains DSM82 glucose/agar amounts under the soil-extract identity. All six exact current contributors are preserved for repair responsibility, not declared formulation-equivalent.

### Opaque BHI product versus ingredient expansion

quantity: concern. Targets: CultureMech:009715.

None of these collection recipes supplies the six expanded commercial constituents as individually measured quantities. The shared 200/250 g tissue notes and 10/2/5/2.5 g/L constituent rates are not authenticated for the exact products and recipe doses. Anatomical UBERON brain/heart terms identify tissues, not commercial infusion equivalence. Restore the collection-specific opaque product amount unless exact product/version evidence independently justifies a scoped expansion.

### Receiving soil extract and scoped stock preparation

representation: concern. Targets: CultureMech:009715.

The target and M337 owner store 1 G_PER_L of an empty unnamed soil solution; JCM342 owner retains the stock procedure but omits the 1 L receiving descriptor. Only JCM102 soil preparation transfers: 400 g air-dried garden soil in 1 L tap water, 121 C for 1 hour, then sedimentation and centrifugation. Its main 250 ml extract/750 ml water dose and pH 7.0 are outside this medium. The repaired M94 stock structure is useful, but its 400 G_PER_L soil field does not establish final recovered-extract volume.

### Source-specific sterilization and endpoints

representation: concern. Targets: CultureMech:009715.

JCM28/263/342 pages explicitly supply the default 121°C for 15 minutes. That main-medium default is separate from the JCM102 soil extraction at 121 C for 1 hour and is not transferred to DSM82, whose captured primary does not specify a cycle. The secondary article pH 7.4±0.2 at 25°C and parent JCM102 pH 7.0 do not establish the receiving soil-medium pH or incubation temperature.

### Resolvable labels do not authenticate commercial constituents

grounding: supported. Targets: CultureMech:009715.

Current primary and secondary ontology labels are retained exactly in the grounding sidecar. MICRO peptone class membership, UBERON anatomy, D-glucose and generic glucose identities do not establish the exact BHI supplier composition or justify adding DSM82 glucose to the soil recipe. No hydrate or stereochemical contradiction is invented from generic source wording.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009715.

31 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Unverified expanded BHI constituent: Calf brains",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q2",
    "subject": "Unverified expanded BHI constituent: Beef heart",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q3",
    "subject": "Unverified expanded BHI constituent: Proteose peptone",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q4",
    "subject": "Unverified expanded BHI constituent: Dextrose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q5",
    "subject": "Unverified expanded BHI constituent: Sodium chloride",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q6",
    "subject": "Unverified expanded BHI constituent: Disodium phosphate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary article composition, not exact-product equivalence",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "The collection primary supplies opaque BHI product mass rather than this constituent amount or basis. The secondary formula does not authenticate exact supplier/version equivalence, 200/250 g tissue extraction claims, or identical constituent rates at both 18.5 g and 37 g product doses. Retain the local assertion as unsupported; do not guess a replacement constituent amount."
  },
  {
    "decision_id": "q7",
    "subject": "Generated soil recipe glucose from a different formula",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Glucose'",
        "exact_source_quote": "Glucose                                     5.0    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      }
    ],
    "rationale": "The 5 g glucose belongs to DSM82 and is absent from JCM342 soil-medium ingredients. It is not a justified addition to the target soil recipe."
  },
  {
    "decision_id": "q8",
    "subject": "DSM82 glucose normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Glucose'",
        "exact_source_quote": "Glucose                                     5.0    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "komodoDetail82",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82",
        "source_locator": "Current provider82 declared g/L row",
        "exact_source_quote": "Glucose\nD-Glucose\nSEED-cpd00027###\n5.00",
        "snapshot_sha256": "5299db8752ce476d2d1d14cf536d9b0b364f8c968992fe7a95fd9fa1e8dcfb66",
        "parsed_text_sha256": "16422df41da1fac5d6a17c07fa45fe4c415200fd95d0ac0a2e43fe2e053d568e"
      }
    ],
    "rationale": "DSM82 prints 5 g batch glucose with 1000 ml listed water. Independently, the exact current KOMODO82 table declares 5 g/L and its source link identifies the same DSM82 formulation represented by both maintained owners. The value and G_PER_L basis are supported as a provider-declared normalization, with missing attached claim evidence. This does not authenticate measured final volume or recover the historical API bytes."
  },
  {
    "decision_id": "q9",
    "subject": "Generated agar inherited from DSM82",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 agar batch row",
        "exact_source_quote": "Agar\n15.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Agar'",
        "exact_source_quote": "Agar                                       12.0    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      }
    ],
    "rationale": "JCM342 supports 15 g agar batch mass; the generated 12 G_PER_L belongs to DSM82. Correct the formulation identity and retain 15 g as a source batch amount without inventing a final-volume denominator."
  },
  {
    "decision_id": "q10",
    "subject": "DSM82 agar normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Agar'",
        "exact_source_quote": "Agar                                       12.0    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "komodoDetail82",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82",
        "source_locator": "Current provider82 declared g/L row",
        "exact_source_quote": "Agar\nAgar\nSEED-cpd13334###\n12.00",
        "snapshot_sha256": "5299db8752ce476d2d1d14cf536d9b0b364f8c968992fe7a95fd9fa1e8dcfb66",
        "parsed_text_sha256": "16422df41da1fac5d6a17c07fa45fe4c415200fd95d0ac0a2e43fe2e053d568e"
      }
    ],
    "rationale": "The primary supplies 12 g batch agar. Independently, the exact current KOMODO82 table declares 12 g/L and links the same DSM82 formulation represented by both maintained owners. The value and G_PER_L basis are supported as provider-declared normalization, with missing attached claim evidence. This does not establish measured final volume, authenticate historical API bytes, or transfer the agar dose to the soil formulation."
  },
  {
    "decision_id": "q11",
    "subject": "Plain BHI agar batch basis",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm28",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28",
        "source_locator": "Plain BHI agar row",
        "exact_source_quote": "Agar\n15.0\ng",
        "snapshot_sha256": "4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071",
        "parsed_text_sha256": "6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113"
      }
    ],
    "rationale": "The primary supplies 15 g agar with a listed 1 L liquid input, not an explicit measured final-litre concentration. Preserve the supported batch mass and the specific water or extract solvent."
  },
  {
    "decision_id": "q12",
    "subject": "Salt-added BHI agar batch basis",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm263",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263",
        "source_locator": "Salt-added BHI agar row",
        "exact_source_quote": "Agar\n15.0\ng",
        "snapshot_sha256": "fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1",
        "parsed_text_sha256": "b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8"
      }
    ],
    "rationale": "The primary supplies 15 g agar with a listed 1 L liquid input, not an explicit measured final-litre concentration. Preserve the supported batch mass and the specific water or extract solvent."
  },
  {
    "decision_id": "q13",
    "subject": "Soil BHI agar batch basis",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "Soil BHI agar row",
        "exact_source_quote": "Agar\n15.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "The primary supplies 15 g agar with a listed 1 L liquid input, not an explicit measured final-litre concentration. Preserve the supported batch mass and the specific water or extract solvent."
  },
  {
    "decision_id": "q14",
    "subject": "JCM263 separate sodium chloride addition",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm263",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263",
        "source_locator": "JCM263 additional NaCl row",
        "exact_source_quote": "NaCl\n20.0\ng",
        "snapshot_sha256": "fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1",
        "parsed_text_sha256": "b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8"
      }
    ],
    "rationale": "The 20 g addition is explicit in this branch. The title 2% does not by itself establish a percentage basis or measured final volume, and the unsupported expanded 5 g/L sodium chloride cannot simply be summed into it."
  },
  {
    "decision_id": "q15",
    "subject": "Soil BHI product",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "12",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Agar",
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solidifying component",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "Soil BHI product primary batch row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "Restore the exact opaque 37 g product batch descriptor at this branch. Expanded constituents cannot substitute for authenticated product identity or mass."
  },
  {
    "decision_id": "q16",
    "subject": "Plain BHI product",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm28",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28",
        "source_locator": "Plain BHI product primary batch row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071",
        "parsed_text_sha256": "6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113"
      }
    ],
    "rationale": "Restore the exact opaque 37 g product batch descriptor at this branch. Expanded constituents cannot substitute for authenticated product identity or mass."
  },
  {
    "decision_id": "q17",
    "subject": "Salt-added BHI product",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm263",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263",
        "source_locator": "Salt-added BHI product primary batch row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1",
        "parsed_text_sha256": "b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8"
      }
    ],
    "rationale": "Restore the exact opaque 37 g product batch descriptor at this branch. Expanded constituents cannot substitute for authenticated product identity or mass."
  },
  {
    "decision_id": "q18",
    "subject": "DSM82 opaque product",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "12",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "12",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      }
    ],
    "rationale": "Restore the exact 18.5 g opaque BHI batch amount. Do not halve or otherwise rescale an unverified 37 g commercial constituent expansion."
  },
  {
    "decision_id": "q19",
    "subject": "DSM82 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "12",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "12",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Distilled water'",
        "exact_source_quote": "Distilled water                          1000.0   ml",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      }
    ],
    "rationale": "Add the explicitly listed 1000 ml or 1 L water as a batch liquid input. It is not an instruction to make the complete preparation up to that final volume."
  },
  {
    "decision_id": "q20",
    "subject": "JCM28 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm28",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28",
        "source_locator": "JCM28 water row",
        "exact_source_quote": "Distilled water\n1.0\nL",
        "snapshot_sha256": "4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071",
        "parsed_text_sha256": "6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113"
      }
    ],
    "rationale": "Add the explicitly listed 1000 ml or 1 L water as a batch liquid input. It is not an instruction to make the complete preparation up to that final volume."
  },
  {
    "decision_id": "q21",
    "subject": "JCM263 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Calf brains",
            "term": {
              "id": "UBERON:0000955",
              "label": "brain"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Beef heart",
            "term": {
              "id": "UBERON:0000948",
              "label": "heart"
            },
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Proteose peptone",
            "term": {
              "id": "MICRO:0000180",
              "label": "proteose peptone"
            },
            "concentration": {
              "value": "10.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Enzymatic digest of animal protein providing amino acids and peptides; Constituent of Brain Heart Infusion commercial product"
          },
          {
            "preferred_term": "Dextrose",
            "term": {
              "id": "CHEBI:17634",
              "label": "D-glucose"
            },
            "concentration": {
              "value": "2.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Carbon/energy source; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "D-glucose",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "dextrose",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Sodium chloride",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "5.0",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "Maintains osmotic equilibrium; Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "NaCl",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "table salt",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "Disodium phosphate",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "2.5",
              "unit": "G_PER_L"
            },
            "supplier_catalog": {
              "supplier_name": "Difco/BD Brain Heart Infusion",
              "catalog_number": "237500",
              "product_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/"
            },
            "notes": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product",
            "synonyms": [
              {
                "synonym_text": "Na2HPO4",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "disodium hydrogen phosphate",
                "synonym_type": "EXACT"
              },
              {
                "synonym_text": "sodium phosphate dibasic",
                "synonym_type": "EXACT"
              }
            ]
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm263",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263",
        "source_locator": "JCM263 water row",
        "exact_source_quote": "Distilled water\n1.0\nL",
        "snapshot_sha256": "fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1",
        "parsed_text_sha256": "b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8"
      }
    ],
    "rationale": "Add the explicitly listed 1000 ml or 1 L water as a batch liquid input. It is not an instruction to make the complete preparation up to that final volume."
  },
  {
    "decision_id": "q22",
    "subject": "Receiving soil-extract volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 soil-extract volume and dependency",
        "exact_source_quote": "Soil extract (See Medium No.\n102\n)\n1.0\nL",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "The target and TOGO owner store 1 G_PER_L, but the primary gives 1 L soil extract. Represent the volume and resolve the named stock instead of retaining a mass-rate stub."
  },
  {
    "decision_id": "q23",
    "subject": "JCM342 owner missing soil-extract descriptor",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 soil-extract volume and dependency",
        "exact_source_quote": "Soil extract (See Medium No.\n102\n)\n1.0\nL",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "The owner retains the stock procedure but lacks the explicit 1 L receiving addition. Add the source descriptor with its exact dependency and volume."
  },
  {
    "decision_id": "q24",
    "subject": "Soil stock 400 g starting material",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "400.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm102",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102",
        "source_locator": "Only JCM102 soil-extract subsection",
        "exact_source_quote": "Suspend 400 g of air-dried garden       soil in 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant after sedimentation       for a few hours and centrifugation.",
        "snapshot_sha256": "cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c",
        "parsed_text_sha256": "ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1"
      }
    ],
    "rationale": "The source gives 400 g starting soil in 1 L tap water, not 400 g/L of recovered extract. Extraction, settling and centrifugation do not specify the recovered final stock volume. Preserve the batch mass and do not promote the repaired stock rate."
  },
  {
    "decision_id": "q25",
    "subject": "Soil stock 1 L tap water",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm102",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102",
        "source_locator": "Only JCM102 soil-extract subsection",
        "exact_source_quote": "Suspend 400 g of air-dried garden       soil in 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant after sedimentation       for a few hours and centrifugation.",
        "snapshot_sha256": "cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c",
        "parsed_text_sha256": "ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1"
      }
    ],
    "rationale": "The local 1 L stock-water value and unit match the primary input exactly; claim-level evidence is absent. This is distinct from the receiving 1 L soil extract."
  },
  {
    "decision_id": "q26",
    "subject": "Soil extraction cycle and physical separation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Suspend 400 g of air-dried garden soil in 1.0 L of tap water and autoclave at 121C for 1 hr. Use the clear supernatant after sedimentation for a few hours and centrifugation."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Suspend 400 g air-dried garden soil in 1.0 L tap water and autoclave at 121 C for 1 hr. Use the clear supernatant after sedimentation for a few hours and centrifugation."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Suspend 400 g air-dried garden soil in 1.0 L tap water and autoclave at 121 C for 1 hr to prepare Soil extract."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Let the soil slurry sediment for a few hours, then centrifuge and use the clear supernatant as Soil extract."
      },
      {
        "input": "data/normalized_yaml/bacterial/nutrient_agar_with_25_soil_extract.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Suspend 400 g of air-dried garden soil in 1.0 L of tap water and autoclave at 121C for 1 hr. Use the clear supernatant after sedimentation for a few hours and centrifugation."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm102",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102",
        "source_locator": "Only JCM102 soil-extract subsection",
        "exact_source_quote": "Suspend 400 g of air-dried garden       soil in 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant after sedimentation       for a few hours and centrifugation.",
        "snapshot_sha256": "cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c",
        "parsed_text_sha256": "ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1"
      }
    ],
    "rationale": "Preserved procedure matches 121 C for 1 hour, qualitative sedimentation for a few hours, centrifugation and clear-supernatant recovery. Attach exact support; do not invent centrifuge speed, sedimentation duration, or recovered yield."
  },
  {
    "decision_id": "q27",
    "subject": "Missing soil-stock structure and preparation in generated/TOGO recipe",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm102",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102",
        "source_locator": "Only JCM102 soil-extract subsection",
        "exact_source_quote": "Suspend 400 g of air-dried garden       soil in 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant after sedimentation       for a few hours and centrifugation.",
        "snapshot_sha256": "cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c",
        "parsed_text_sha256": "ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1"
      },
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 soil-extract volume and dependency",
        "exact_source_quote": "Soil extract (See Medium No.\n102\n)\n1.0\nL",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "Populate only the named soil-stock procedure, its 400 g starting soil and 1 L water. The parent medium main ingredients, 250 ml extract dose, 750 ml water and pH 7.0 remain excluded."
  },
  {
    "decision_id": "q28",
    "subject": "Plain main-medium sterilization",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm28",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28",
        "source_locator": "JCM page explicit default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071",
        "parsed_text_sha256": "6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113"
      }
    ],
    "rationale": "Add the source-specific main-medium 121°C, 15-minute default, separately from soil-stock extraction at 121 C for 1 hour. This JCM default is not transferred to DSM82."
  },
  {
    "decision_id": "q29",
    "subject": "Salt-added main-medium sterilization",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm263",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263",
        "source_locator": "JCM page explicit default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1",
        "parsed_text_sha256": "b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8"
      }
    ],
    "rationale": "Add the source-specific main-medium 121°C, 15-minute default, separately from soil-stock extraction at 121 C for 1 hour. This JCM default is not transferred to DSM82."
  },
  {
    "decision_id": "q30",
    "subject": "Soil main-medium sterilization",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Suspend 400 g of air-dried garden soil in 1.0 L of tap water and autoclave at 121C for 1 hr. Use the clear supernatant after sedimentation for a few hours and centrifugation."
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM page explicit default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      }
    ],
    "rationale": "Add the source-specific main-medium 121°C, 15-minute default, separately from soil-stock extraction at 121 C for 1 hour. This JCM default is not transferred to DSM82."
  },
  {
    "decision_id": "q31",
    "subject": "Receiving pH and incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm342",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342",
        "source_locator": "JCM342 opaque product row",
        "exact_source_quote": "Brain heart infusion broth (BD-Difco)\n37.0\ng",
        "snapshot_sha256": "0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635",
        "parsed_text_sha256": "ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd"
      },
      {
        "source_key": "dsmz82",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf",
        "source_locator": "Exact extracted source line containing 'Brain heart infusion'",
        "exact_source_quote": "Brain heart infusion                       18.5    g",
        "snapshot_sha256": "10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347",
        "parsed_text_sha256": "4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Secondary comparison formula only",
        "exact_source_quote": "Final pH (at 25°C): 7.4±0.2",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "rationale": "These collection primaries do not establish a receiving pH or incubation temperature. The local product note pH 7.4±0.2 belongs to an unverified secondary formulation; 25°C is a measurement condition, not growth temperature. Parent JCM102 pH 7.0 stays excluded."
  }
]

## Findings

### f1: Separate the soil recipe from plain, salt-added and glucose BHI

blocker / open / confirmed; issue key: bhi-soil-contributor-formulation-mixture.

The generated soil-medium identity carries DSM82 glucose/agar amounts while its six contributors represent four distinct primary formulations. The current conservative merger already guards scientific equality, so this is a stale generated-membership and owner-identity repair, not proof of a current blind merge.

### f2: Restore source-specific opaque BHI product amounts

major / open / confirmed; issue key: bhi-commercial-expansion-unverified.

The shared expanded constituents and 200/250 g tissue-equivalence notes lack exact product/version support. DSM82 needs 18.5 g product while the JCM branches use 37 g; a generic secondary article cannot authenticate identical expanded rates across both.

### f3: Restore the 1 L soil-extract addition and scoped stock

major / open / confirmed; issue key: bhi-soil-volume-stock-structure.

The generated and TOGO descriptors are 1 G_PER_L empty solutions, while the JCM owner lacks the addition despite retaining its stock preparation. The named M94 stock 400 G_PER_L field also overstates recovered-extract basis.

### f4: Attach branch-specific amounts and preparation without inherited endpoints

major / open / confirmed; issue key: bhi-source-stage-preparation-evidence.

Opaque product quantities, water or soil volumes, agar branches and main sterilization are incomplete or unlinked. Source batch amounts must remain distinct from normalized provider rates and unsupported final-volume, pH and incubation assumptions.

### f5: Retain unresolved historical timestamp precision

minor / open / confirmed; issue key: bhi-soil-history-timestamp-shape.

Malformed or timezone-absent history values remain historical assertions. Current code and current source responses do not establish their execution times or exact original source bytes.

## Recommended Actions And Acceptance Checks

### a1

Repair each maintained formulation and exact source identity, then regenerate through the existing conservative gate and verify correct contributor membership and freshness.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Use exact source product masses and preserve any independently supported expansion only with exact supplier/version evidence and explicit amount basis. Do not invent tissue yields or rescale unsupported constituent values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent receiving soil extract as 1 L, link only the exact soil subsection, retain 400 g soil plus 1 L tap water and separate the 121 C one-hour extraction from main-medium sterilization. Keep stock recovered volume unknown.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact claim-level evidence for each branch and its source stages; preserve unavailable or unestablished basis rather than converting listed water to measured final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Append an evidenced clarification if recoverable while preserving original events and derivative report distinctions.

- No inferred UTC normalization or historical execution claim.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/bhi_glucose_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-4 | data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-5 | data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch045/444/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/444/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml:1:id: CultureMech:009715<br>./data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml:1:id: CultureMech:009715<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch045/source-preflight-bound/444/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 24 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch045/444/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17234": [{"label": "(2R,3S,4R,5R)-2,3,4,5,6-pentahydroxyhexanal", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aldehydo-D-gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aldehydo-D-gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "D-glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "D-GLUCOSE IN LINEAR FORM", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "DL-glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D­glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glc", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "gluco-hexose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "glucose", "ontology_id": "CHEBI:17234", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "glucose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Glukose", "match_type": "synonym", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml; data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml; data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml; data/normalized_yaml/bacterial/bhi_glucose_medium.yaml; data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml; data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml; data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml", "events": 6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.195664"}]}, {"input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml", "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml", "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml", "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml", "events": 5, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch045/444/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch045/444/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| dsm82 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf; Complete exact collection primary; JCM102 only its soil-extract subsection transfers | supports | Read exact recipe identity, batch units and scoped preparation. JCM102 main recipe, 25% dose and pH 7.0 are excluded from the receiving medium. |
| j28 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28; Complete exact collection primary; JCM102 only its soil-extract subsection transfers | supports | Read exact recipe identity, batch units and scoped preparation. JCM102 main recipe, 25% dose and pH 7.0 are excluded from the receiving medium. |
| j263 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263; Complete exact collection primary; JCM102 only its soil-extract subsection transfers | supports | Read exact recipe identity, batch units and scoped preparation. JCM102 main recipe, 25% dose and pH 7.0 are excluded from the receiving medium. |
| j342 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342; Complete exact collection primary; JCM102 only its soil-extract subsection transfers | supports | Read exact recipe identity, batch units and scoped preparation. JCM102 main recipe, 25% dose and pH 7.0 are excluded from the receiving medium. |
| soil102 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102; Complete exact collection primary; JCM102 only its soil-extract subsection transfers | supports | Read exact recipe identity, batch units and scoped preparation. JCM102 main recipe, 25% dose and pH 7.0 are excluded from the receiving medium. |
| provider82 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82; Exact current medium 82 header and metabolite table | supports | Provider expressly labels 18.50 g/L BHI, 5.00 g/L glucose and 12.00 g/L agar as its normalized formulation. This does not establish equivalence to the 37 g BHI soil recipe or measured final volume of the primary batch. |
| provider337 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M337; Exact M337 identity and components | supports | Provider corroborates JCM342 identity and its soil-extract reference; it is not DSM82 or the plain/salt-added BHI formula. |
| supplier-comparison | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Current secondary BHI composition article | supports | This secondary article lists HM infusion powder and BHI powder, not authenticated 200 g calf-brain/250 g beef-heart equivalents or a manufacturer-verified BD237500 formula. Its preparation applies to its own formulation. |
| mediadive82api-attempt | https://mediadive.dsmz.de/rest/medium/82; Preserved exact public retrieval result | context_only | The exact current MediaDive82 request returned HTTP503. Complete collection primaries and current provider text remain available; no failed response authenticates historical amounts. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current group_formulations and conservative scientific-field equality are already shipped. This stale contributor mixture is not evidence that the current CLI blindly merges ingredient sets. Repair exact owner identity/stock structure and verify authorized regenerated membership and freshness. Current composition-resolution code is context, not proof of historical execution. |
| writer-1 | src/culturemech/merge/matcher.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current group_formulations and conservative scientific-field equality are already shipped. This stale contributor mixture is not evidence that the current CLI blindly merges ingredient sets. Repair exact owner identity/stock structure and verify authorized regenerated membership and freshness. Current composition-resolution code is context, not proof of historical execution. |
| writer-2 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current group_formulations and conservative scientific-field equality are already shipped. This stale contributor mixture is not evidence that the current CLI blindly merges ingredient sets. Repair exact owner identity/stock structure and verify authorized regenerated membership and freshness. Current composition-resolution code is context, not proof of historical execution. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current group_formulations and conservative scientific-field equality are already shipped. This stale contributor mixture is not evidence that the current CLI blindly merges ingredient sets. Repair exact owner identity/stock structure and verify authorized regenerated membership and freshness. Current composition-resolution code is context, not proof of historical execution. |
| writer-4 | scripts/resolve_komodo_compositions.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current group_formulations and conservative scientific-field equality are already shipped. This stale contributor mixture is not evidence that the current CLI blindly merges ingredient sets. Repair exact owner identity/stock structure and verify authorized regenerated membership and freshness. Current composition-resolution code is context, not proof of historical execution. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch045/444/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact current MediaDive82 request returned HTTP503. Complete collection primaries and current provider text remain available; no failed response authenticates historical amounts.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021420Z-culturemech-009715-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: brain_heart_infusion_agar_with_soil_extract
  (CultureMech:009715)'
started_at: '2026-10-22T02:02:38Z'
finished_at: '2026-10-22T02:14:20Z'
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
summary: The generated soil-extract record combines six maintained contributors from
  four distinct collection formulations. Current primaries support opaque BHI product
  amounts, separate glucose/salt/agar additions and a 1 L soil-extract input; they
  do not authenticate the shared commercial constituent expansion or tissue-equivalence
  claims.
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
  - path: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
    sha256: ff3be9dc3c68509bbcf6c71a88a575f25508851c1db39933f0c11c098bf268c7
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    sha256: c0cf88eb37b361f0d2c193b7ad283a0bfe06b37a830eb601ae4cd1048435695a
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    sha256: 7f9aaabfff9aa5283dd607a68637f206f6bef73c54207303de80056d1e480adf
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml
    sha256: 8650e143c0e218a6bece56c476e93cc250dd9fa9a48ddbb11a36acfce5440649
    role: context
  - path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    sha256: b8fb47461b049bfa28af88a4609cc675642b7cf1b242b6bed9681073f1a61eb0
    role: context
  - path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    sha256: 4abe0e48997b9527d15db7d0079a9e578e78814e950aaea802bf7956c57a72ee
    role: context
  - path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    sha256: 82fd164b008ed0578ed7cd7d74002b9719f3a4662035edce53a499ccf39155b8
    role: context
  - path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
    sha256: a361b9f9c76011c057b23ce824a29cdc1920a3e35bd6b4df9682977eae875370
    role: context
  - path: data/normalized_yaml/bacterial/nutrient_agar_with_25_soil_extract.yaml
    sha256: 44b9cbc64f1989491403372ea57d45faf5cd0fb89751416eecb37a144a30b3d8
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json
    sha256: 7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml.md
    sha256: d1979f98d99344d989a5ebed71123870f8fed118d4f8ed3c8f846ded0aefbf4b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bhi_glucose_medium.yaml.md
    sha256: 45ed0e6afd8a3888df252092081e7b921921157e2176dc9d8e02fea123cafae5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/plan.json
    sha256: 2a664ea8af07a25caadaa3e00421ae8eaa883ddd3e42c83f5013b3bf303c789b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/brain_heart_infusion_agar.yaml.md
    sha256: 90ab59d0248507dc48f77afa5e7dcec2b5bf403bdd09309d8bf55f302a0dd2e4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml.md
    sha256: 5592928bfcfcdb1b93dfef18ab1bc160cc7b5f2c400250f0ee27ad547267722a
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml.md
    sha256: 7b4fe08b779f0a65220845516a1ff51b916ee7c4f275222db5c2f66acb5cf64c
    role: context
  - path: reports/yaml_record_review/20260921T234431Z-BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.md
    sha256: 8300002c3be6227b095be5aef1cf8bbc1c8719983aa96d5412042be23bfa57b6
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
  selection: Task review 444; batch 045 item 4 of 10, selected in Python lexicographic
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
  - CultureMech:009715
targets:
- target_id: CultureMech:009715
  path: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  label: brain_heart_infusion_agar_with_soil_extract
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/444/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/444/strict.tsv"
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009715
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
  - CultureMech:009715
- check_id: mediadive82api-source-access
  name: 'Exact source content access: mediadive82api'
  required: false
  status: unavailable
  summary: The exact current MediaDive82 request returned HTTP503. Complete collection
    primaries and current provider text remain available; no failed response authenticates
    historical amounts.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - mediadive82api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:18.876933Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/444/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:20.367626Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/444/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:22.085460Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:23.114016Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T02:11:40Z'
  support: supports
  summary: './data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml:1:id:
    CultureMech:009715

    ./data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml:1:id:
    CultureMech:009715

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/source-preflight-bound/444/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T02:11:40Z'
  support: supports
  summary: 24 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a1f9d94430181f14144478a7a7f3fe627d69f520f26cb5e0ae81f3a8c068d2d6
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/444/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: 4c00caabd2cf0541b19b48b13caf0ccd898a86ff3b51af3d1bda5e98856166f1
- evidence_id: uberon0000955
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:25.122940Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: ce200fe58b82652d0f04310c92d23633919fa6ad6aee2a17c6b25c2e490a8877
- evidence_id: uberon0000948
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:24.915343Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: c658bbcacd89befa47e3bd4859f176db247b3ce67483b6590c91d0865d41aed4
- evidence_id: micro0000180
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:24.290496Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: b3a39a531c5ab5508a297228d13ba81c99899b041d5292a9d668eded939bfe73
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
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
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:31.535358Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:37.629610Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T02:11:40Z'
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
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if
    needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Agar (BD)", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Agar (if needed)*", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Molecular
    Genetics)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Agar (Purified)", "match_type": "synonym", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)", "match_type":
    "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bacteriological
    Agar", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl
    (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type":
    "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type":
    "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy":
    []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml;
    data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml; data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml;
    data/normalized_yaml/bacterial/bhi_glucose_medium.yaml; data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml;
    data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml; data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml", "events":
    6, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value":
    "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.195664"}]},
    {"input": "data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml",
    "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bhi_glucose_medium.yaml",
    "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml",
    "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml",
    "events": 5, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml",
    "events": 5, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/444/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: fd160cab7acbfaf5b979af64423dd8567b6f71fa01e881fc032486007b057fe0
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/444/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: 11ed48bd95bfbab212cb63c6d63c5e259e0261fcdbac61e6e8443e5812758d2c
- evidence_id: dsm82
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf
  locator: Complete exact collection primary; JCM102 only its soil-extract subsection
    transfers
  accessed_at: '2026-10-22T01:49:19.461146Z'
  support: supports
  summary: Read exact recipe identity, batch units and scoped preparation. JCM102
    main recipe, 25% dose and pH 7.0 are excluded from the receiving medium.
  quote: 82. BHI-GLUCOSE MEDIUM
  snapshot_sha256: 10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347
- evidence_id: j28
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28
  locator: Complete exact collection primary; JCM102 only its soil-extract subsection
    transfers
  accessed_at: '2026-10-22T01:49:20.532600Z'
  support: supports
  summary: Read exact recipe identity, batch units and scoped preparation. JCM102
    main recipe, 25% dose and pH 7.0 are excluded from the receiving medium.
  quote: BRAIN HEART INFUSION AGAR
  snapshot_sha256: 4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071
- evidence_id: j263
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263
  locator: Complete exact collection primary; JCM102 only its soil-extract subsection
    transfers
  accessed_at: '2026-10-22T01:49:20.893431Z'
  support: supports
  summary: Read exact recipe identity, batch units and scoped preparation. JCM102
    main recipe, 25% dose and pH 7.0 are excluded from the receiving medium.
  quote: BRAIN HEART INFUSION AGAR WITH 2% NaCl
  snapshot_sha256: fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1
- evidence_id: j342
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342
  locator: Complete exact collection primary; JCM102 only its soil-extract subsection
    transfers
  accessed_at: '2026-10-22T01:49:21.102156Z'
  support: supports
  summary: Read exact recipe identity, batch units and scoped preparation. JCM102
    main recipe, 25% dose and pH 7.0 are excluded from the receiving medium.
  quote: BRAIN HEART INFUSION AGAR WITH SOIL EXTRACT
  snapshot_sha256: 0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635
- evidence_id: soil102
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102
  locator: Complete exact collection primary; JCM102 only its soil-extract subsection
    transfers
  accessed_at: '2026-10-22T01:51:09.328831Z'
  support: supports
  summary: Read exact recipe identity, batch units and scoped preparation. JCM102
    main recipe, 25% dose and pH 7.0 are excluded from the receiving medium.
  quote: NUTRIENT AGAR WITH 25% SOIL EXTRACT
  snapshot_sha256: cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c
- evidence_id: provider82
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82
  locator: Exact current medium 82 header and metabolite table
  accessed_at: '2026-10-22T01:51:11.852566Z'
  support: supports
  summary: Provider expressly labels 18.50 g/L BHI, 5.00 g/L glucose and 12.00 g/L
    agar as its normalized formulation. This does not establish equivalence to the
    37 g BHI soil recipe or measured final volume of the primary batch.
  snapshot_sha256: 5299db8752ce476d2d1d14cf536d9b0b364f8c968992fe7a95fd9fa1e8dcfb66
- evidence_id: provider337
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M337
  locator: Exact M337 identity and components
  accessed_at: '2026-10-22T01:49:21.470297Z'
  support: supports
  summary: Provider corroborates JCM342 identity and its soil-extract reference; it
    is not DSM82 or the plain/salt-added BHI formula.
  snapshot_sha256: 5fe97402cf44c7b20146666401c4a0fc3e71af9881b845fc1b03de8e3706a235
- evidence_id: supplier-comparison
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Current secondary BHI composition article
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: supports
  summary: This secondary article lists HM infusion powder and BHI powder, not authenticated
    200 g calf-brain/250 g beef-heart equivalents or a manufacturer-verified BD237500
    formula. Its preparation applies to its own formulation.
  quote: HM infusion powder 12.500 BHI powder 5.000
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: mediadive82api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/82
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:49:20.002868Z'
  support: context_only
  summary: The exact current MediaDive82 request returned HTTP503. Complete collection
    primaries and current provider text remain available; no failed response authenticates
    historical amounts.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Current group_formulations and conservative scientific-field equality are
    already shipped. This stale contributor mixture is not evidence that the current
    CLI blindly merges ingredient sets. Repair exact owner identity/stock structure
    and verify authorized regenerated membership and freshness. Current composition-resolution
    code is context, not proof of historical execution.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Current group_formulations and conservative scientific-field equality are
    already shipped. This stale contributor mixture is not evidence that the current
    CLI blindly merges ingredient sets. Repair exact owner identity/stock structure
    and verify authorized regenerated membership and freshness. Current composition-resolution
    code is context, not proof of historical execution.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Current group_formulations and conservative scientific-field equality are
    already shipped. This stale contributor mixture is not evidence that the current
    CLI blindly merges ingredient sets. Repair exact owner identity/stock structure
    and verify authorized regenerated membership and freshness. Current composition-resolution
    code is context, not proof of historical execution.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Current group_formulations and conservative scientific-field equality are
    already shipped. This stale contributor mixture is not evidence that the current
    CLI blindly merges ingredient sets. Repair exact owner identity/stock structure
    and verify authorized regenerated membership and freshness. Current composition-resolution
    code is context, not proof of historical execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:11:40Z'
  support: context_only
  summary: Current group_formulations and conservative scientific-field equality are
    already shipped. This stale contributor mixture is not evidence that the current
    CLI blindly merges ingredient sets. Repair exact owner identity/stock structure
    and verify authorized regenerated membership and freshness. Current composition-resolution
    code is context, not proof of historical execution.
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/444/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T02:13:06Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c8ab3ff50811b0aa8165224f4a55968b72221d3fd9a056af548400108157adb0
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: supported
  summary: 8 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label
    mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly.
    3/3 asserted current secondary keys have exact pinned index rows. Target primary
    linkage is 8/8 (100.00%) and current secondary linkage is 2/8 (25.00%) on a 0–100
    linkage scale, not a correctness score. Current missing keys do not prove historical
    invalidity; compatible generic source wording does not establish a stereochemical
    conflict.
  target_ids:
  - CultureMech:009715
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
  - chebi2509
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 46 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
- assessment_id: identity
  area: identity
  topic: Four collection formulations in one generated contributor set
  outcome: concern
  summary: DSM82 uses 18.5 g BHI plus 5 g glucose and 12 g agar. JCM28 uses 37 g BHI
    and 15 g agar in 1 L water; JCM263 additionally uses 20 g NaCl. JCM342/M337 instead
    uses 37 g BHI and 15 g agar with 1 L soil extract. The generated record retains
    DSM82 glucose/agar amounts under the soil-extract identity. All six exact current
    contributors are preserved for repair responsibility, not declared formulation-equivalent.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - dsm82
  - j28
  - j263
  - j342
  - provider337
  - record
- assessment_id: product
  area: quantity
  topic: Opaque BHI product versus ingredient expansion
  outcome: concern
  summary: None of these collection recipes supplies the six expanded commercial constituents
    as individually measured quantities. The shared 200/250 g tissue notes and 10/2/5/2.5
    g/L constituent rates are not authenticated for the exact products and recipe
    doses. Anatomical UBERON brain/heart terms identify tissues, not commercial infusion
    equivalence. Restore the collection-specific opaque product amount unless exact
    product/version evidence independently justifies a scoped expansion.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - dsm82
  - j28
  - j263
  - j342
  - supplier-comparison
  - grounding-inventory
- assessment_id: soil
  area: representation
  topic: Receiving soil extract and scoped stock preparation
  outcome: concern
  summary: 'The target and M337 owner store 1 G_PER_L of an empty unnamed soil solution;
    JCM342 owner retains the stock procedure but omits the 1 L receiving descriptor.
    Only JCM102 soil preparation transfers: 400 g air-dried garden soil in 1 L tap
    water, 121 C for 1 hour, then sedimentation and centrifugation. Its main 250 ml
    extract/750 ml water dose and pH 7.0 are outside this medium. The repaired M94
    stock structure is useful, but its 400 G_PER_L soil field does not establish final
    recovered-extract volume.'
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - j342
  - soil102
  - record
  - provider337
- assessment_id: preparation
  area: representation
  topic: Source-specific sterilization and endpoints
  outcome: concern
  summary: JCM28/263/342 pages explicitly supply the default 121°C for 15 minutes.
    That main-medium default is separate from the JCM102 soil extraction at 121 C
    for 1 hour and is not transferred to DSM82, whose captured primary does not specify
    a cycle. The secondary article pH 7.4±0.2 at 25°C and parent JCM102 pH 7.0 do
    not establish the receiving soil-medium pH or incubation temperature.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - j28
  - j263
  - j342
  - soil102
  - dsm82
  - supplier-comparison
- assessment_id: forms
  area: grounding
  topic: Resolvable labels do not authenticate commercial constituents
  outcome: supported
  summary: Current primary and secondary ontology labels are retained exactly in the
    grounding sidecar. MICRO peptone class membership, UBERON anatomy, D-glucose and
    generic glucose identities do not establish the exact BHI supplier composition
    or justify adding DSM82 glucose to the soil recipe. No hydrate or stereochemical
    contradiction is invented from generic source wording.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - grounding-inventory
  - mim
  - supplier-comparison
  - j342
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 31 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009715
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Unverified expanded\
    \ BHI constituent: Calf brains\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion from\
    \ 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\",\n\
    \        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm342\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\",\n        \"source_locator\"\
    : \"JCM342 opaque product row\",\n        \"exact_source_quote\": \"Brain heart\
    \ infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q2\"\
    ,\n    \"subject\": \"Unverified expanded BHI constituent: Beef heart\",\n   \
    \ \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion from\
    \ 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\",\n\
    \        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm342\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\",\n        \"source_locator\"\
    : \"JCM342 opaque product row\",\n        \"exact_source_quote\": \"Brain heart\
    \ infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q3\"\
    ,\n    \"subject\": \"Unverified expanded BHI constituent: Proteose peptone\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic digest of animal\
    \ protein providing amino acids and peptides; Constituent of Brain Heart Infusion\
    \ commercial product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Enzymatic\
    \ digest of animal protein providing amino acids and peptides; Constituent of\
    \ Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm342\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\",\n        \"source_locator\"\
    : \"JCM342 opaque product row\",\n        \"exact_source_quote\": \"Brain heart\
    \ infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q4\"\
    ,\n    \"subject\": \"Unverified expanded BHI constituent: Dextrose\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Carbon/energy\
    \ source; Constituent of Brain Heart Infusion commercial product\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm342\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 opaque product row\",\n        \"exact_source_quote\"\
    : \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q5\"\
    ,\n    \"subject\": \"Unverified expanded BHI constituent: Sodium chloride\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Maintains\
    \ osmotic equilibrium; Constituent of Brain Heart Infusion commercial product\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 opaque product row\",\n        \"exact_source_quote\"\
    : \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q6\"\
    ,\n    \"subject\": \"Unverified expanded BHI constituent: Disodium phosphate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 opaque product row\",\n        \"exact_source_quote\"\
    : \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary article composition, not exact-product\
    \ equivalence\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000 Proteose peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride\
    \ 5.000 Disodium phosphate 2.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"The collection primary supplies opaque\
    \ BHI product mass rather than this constituent amount or basis. The secondary\
    \ formula does not authenticate exact supplier/version equivalence, 200/250 g\
    \ tissue extraction claims, or identical constituent rates at both 18.5 g and\
    \ 37 g product doses. Retain the local assertion as unsupported; do not guess\
    \ a replacement constituent amount.\"\n  },\n  {\n    \"decision_id\": \"q7\"\
    ,\n    \"subject\": \"Generated soil recipe glucose from a different formula\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 opaque product row\",\n        \"exact_source_quote\"\
    : \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Glucose'\",\n\
    \        \"exact_source_quote\": \"Glucose                                   \
    \  5.0    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      }\n    ],\n    \"rationale\": \"The 5 g glucose belongs to DSM82 and is\
    \ absent from JCM342 soil-medium ingredients. It is not a justified addition to\
    \ the target soil recipe.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\"\
    : \"DSM82 glucose normalization\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz82\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Glucose'\"\
    ,\n        \"exact_source_quote\": \"Glucose                                 \
    \    5.0    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail82\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82\"\
    ,\n        \"source_locator\": \"Current provider82 declared g/L row\",\n    \
    \    \"exact_source_quote\": \"Glucose\\nD-Glucose\\nSEED-cpd00027###\\n5.00\"\
    ,\n        \"snapshot_sha256\": \"5299db8752ce476d2d1d14cf536d9b0b364f8c968992fe7a95fd9fa1e8dcfb66\"\
    ,\n        \"parsed_text_sha256\": \"16422df41da1fac5d6a17c07fa45fe4c415200fd95d0ac0a2e43fe2e053d568e\"\
    \n      }\n    ],\n    \"rationale\": \"DSM82 prints 5 g batch glucose with 1000\
    \ ml listed water. Independently, the exact current KOMODO82 table declares 5\
    \ g/L and its source link identifies the same DSM82 formulation represented by\
    \ both maintained owners. The value and G_PER_L basis are supported as a provider-declared\
    \ normalization, with missing attached claim evidence. This does not authenticate\
    \ measured final volume or recover the historical API bytes.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q9\",\n    \"subject\": \"Generated agar inherited from\
    \ DSM82\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 agar batch row\",\n        \"exact_source_quote\"\
    : \"Agar\\n15.0\\ng\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Agar'\",\n \
    \       \"exact_source_quote\": \"Agar                                       12.0\
    \    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      }\n    ],\n    \"rationale\": \"JCM342 supports 15 g agar batch mass;\
    \ the generated 12 G_PER_L belongs to DSM82. Correct the formulation identity\
    \ and retain 15 g as a source batch amount without inventing a final-volume denominator.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\": \"DSM82 agar normalization\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz82\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Agar'\"\
    ,\n        \"exact_source_quote\": \"Agar                                    \
    \   12.0    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail82\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=82\"\
    ,\n        \"source_locator\": \"Current provider82 declared g/L row\",\n    \
    \    \"exact_source_quote\": \"Agar\\nAgar\\nSEED-cpd13334###\\n12.00\",\n   \
    \     \"snapshot_sha256\": \"5299db8752ce476d2d1d14cf536d9b0b364f8c968992fe7a95fd9fa1e8dcfb66\"\
    ,\n        \"parsed_text_sha256\": \"16422df41da1fac5d6a17c07fa45fe4c415200fd95d0ac0a2e43fe2e053d568e\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supplies 12 g batch agar.\
    \ Independently, the exact current KOMODO82 table declares 12 g/L and links the\
    \ same DSM82 formulation represented by both maintained owners. The value and\
    \ G_PER_L basis are supported as provider-declared normalization, with missing\
    \ attached claim evidence. This does not establish measured final volume, authenticate\
    \ historical API bytes, or transfer the agar dose to the soil formulation.\"\n\
    \  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Plain BHI agar batch\
    \ basis\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm28\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28\"\
    ,\n        \"source_locator\": \"Plain BHI agar row\",\n        \"exact_source_quote\"\
    : \"Agar\\n15.0\\ng\",\n        \"snapshot_sha256\": \"4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071\"\
    ,\n        \"parsed_text_sha256\": \"6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supplies 15 g agar with a\
    \ listed 1 L liquid input, not an explicit measured final-litre concentration.\
    \ Preserve the supported batch mass and the specific water or extract solvent.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Salt-added BHI\
    \ agar batch basis\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm263\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263\"\
    ,\n        \"source_locator\": \"Salt-added BHI agar row\",\n        \"exact_source_quote\"\
    : \"Agar\\n15.0\\ng\",\n        \"snapshot_sha256\": \"fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1\"\
    ,\n        \"parsed_text_sha256\": \"b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supplies 15 g agar with a\
    \ listed 1 L liquid input, not an explicit measured final-litre concentration.\
    \ Preserve the supported batch mass and the specific water or extract solvent.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Soil BHI agar batch\
    \ basis\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"Soil BHI agar row\",\n        \"exact_source_quote\"\
    : \"Agar\\n15.0\\ng\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supplies 15 g agar with a\
    \ listed 1 L liquid input, not an explicit measured final-litre concentration.\
    \ Preserve the supported batch mass and the specific water or extract solvent.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"JCM263 separate\
    \ sodium chloride addition\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm263\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263\"\
    ,\n        \"source_locator\": \"JCM263 additional NaCl row\",\n        \"exact_source_quote\"\
    : \"NaCl\\n20.0\\ng\",\n        \"snapshot_sha256\": \"fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1\"\
    ,\n        \"parsed_text_sha256\": \"b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8\"\
    \n      }\n    ],\n    \"rationale\": \"The 20 g addition is explicit in this\
    \ branch. The title 2% does not by itself establish a percentage basis or measured\
    \ final volume, and the unsupported expanded 5 g/L sodium chloride cannot simply\
    \ be summed into it.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"subject\"\
    : \"Soil BHI product\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Agar\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:2509\",\n            \
    \  \"label\": \"agar\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"12\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n        \
    \  }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Agar\",\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Solidifying component\",\n    \
    \        \"term\": {\n              \"id\": \"CHEBI:2509\",\n              \"\
    label\": \"agar\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calf brains\",\n            \"term\": {\n              \"id\": \"UBERON:0000955\"\
    ,\n              \"label\": \"brain\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"Soil BHI product primary batch row\",\n     \
    \   \"exact_source_quote\": \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\"\
    ,\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact opaque 37 g product\
    \ batch descriptor at this branch. Expanded constituents cannot substitute for\
    \ authenticated product identity or mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q16\",\n    \"subject\": \"Plain BHI product\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm28\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28\"\
    ,\n        \"source_locator\": \"Plain BHI product primary batch row\",\n    \
    \    \"exact_source_quote\": \"Brain heart infusion broth (BD-Difco)\\n37.0\\\
    ng\",\n        \"snapshot_sha256\": \"4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071\"\
    ,\n        \"parsed_text_sha256\": \"6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact opaque 37 g product\
    \ batch descriptor at this branch. Expanded constituents cannot substitute for\
    \ authenticated product identity or mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q17\",\n    \"subject\": \"Salt-added BHI product\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"NaCl\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\",\n\
    \              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"20\",\n              \"unit\":\
    \ \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm263\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263\"\
    ,\n        \"source_locator\": \"Salt-added BHI product primary batch row\",\n\
    \        \"exact_source_quote\": \"Brain heart infusion broth (BD-Difco)\\n37.0\\\
    ng\",\n        \"snapshot_sha256\": \"fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1\"\
    ,\n        \"parsed_text_sha256\": \"b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact opaque 37 g product\
    \ batch descriptor at this branch. Expanded constituents cannot substitute for\
    \ authenticated product identity or mass.\"\n  },\n  {\n    \"decision_id\": \"\
    q18\",\n    \"subject\": \"DSM82 opaque product\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Agar\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:2509\",\n            \
    \  \"label\": \"agar\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"12\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n        \
    \  }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Agar\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:2509\",\n            \
    \  \"label\": \"agar\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"12\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n        \
    \  }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz82\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Brain\
    \ heart infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion \
    \                      18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the exact 18.5 g opaque BHI batch\
    \ amount. Do not halve or otherwise rescale an unverified 37 g commercial constituent\
    \ expansion.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"subject\": \"\
    DSM82 water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Agar\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:2509\",\n            \
    \  \"label\": \"agar\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"12\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n        \
    \  }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Agar\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:2509\",\n            \
    \  \"label\": \"agar\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"12\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n        \
    \  }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz82\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Distilled\
    \ water'\",\n        \"exact_source_quote\": \"Distilled water               \
    \           1000.0   ml\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicitly listed 1000 ml or 1\
    \ L water as a batch liquid input. It is not an instruction to make the complete\
    \ preparation up to that final volume.\"\n  },\n  {\n    \"decision_id\": \"q20\"\
    ,\n    \"subject\": \"JCM28 water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm28\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28\"\
    ,\n        \"source_locator\": \"JCM28 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water\\n1.0\\nL\",\n        \"snapshot_sha256\": \"4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071\"\
    ,\n        \"parsed_text_sha256\": \"6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicitly listed 1000 ml or 1\
    \ L water as a batch liquid input. It is not an instruction to make the complete\
    \ preparation up to that final volume.\"\n  },\n  {\n    \"decision_id\": \"q21\"\
    ,\n    \"subject\": \"JCM263 water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Calf brains\",\n            \"term\": {\n\
    \              \"id\": \"UBERON:0000955\",\n              \"label\": \"brain\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    variable\",\n              \"unit\": \"VARIABLE\"\n            },\n          \
    \  \"supplier_catalog\": {\n              \"supplier_name\": \"Difco/BD Brain\
    \ Heart Infusion\",\n              \"catalog_number\": \"237500\",\n         \
    \     \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 200 g/L; Tissue infusion\
    \ - source material is calf brain tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Beef heart\",\n            \"term\": {\n              \"id\": \"UBERON:0000948\"\
    ,\n              \"label\": \"heart\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"infusion from 250 g/L; Tissue infusion\
    \ - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion\
    \ commercial product\"\n          },\n          {\n            \"preferred_term\"\
    : \"Proteose peptone\",\n            \"term\": {\n              \"id\": \"MICRO:0000180\"\
    ,\n              \"label\": \"proteose peptone\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"10.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Enzymatic digest of animal protein\
    \ providing amino acids and peptides; Constituent of Brain Heart Infusion commercial\
    \ product\"\n          },\n          {\n            \"preferred_term\": \"Dextrose\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:17634\",\n         \
    \     \"label\": \"D-glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2.0\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"supplier_catalog\": {\n              \"supplier_name\"\
    : \"Difco/BD Brain Heart Infusion\",\n              \"catalog_number\": \"237500\"\
    ,\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Carbon/energy source; Constituent of\
    \ Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n  \
    \            {\n                \"synonym_text\": \"glucose\",\n             \
    \   \"synonym_type\": \"EXACT\"\n              },\n              {\n         \
    \       \"synonym_text\": \"D-glucose\",\n                \"synonym_type\": \"\
    EXACT\"\n              },\n              {\n                \"synonym_text\":\
    \ \"dextrose\",\n                \"synonym_type\": \"EXACT\"\n              }\n\
    \            ]\n          },\n          {\n            \"preferred_term\": \"\
    Sodium chloride\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\"\
    ,\n              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"5.0\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"supplier_catalog\": {\n         \
    \     \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n              \"\
    catalog_number\": \"237500\",\n              \"product_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    \n            },\n            \"notes\": \"Maintains osmotic equilibrium; Constituent\
    \ of Brain Heart Infusion commercial product\",\n            \"synonyms\": [\n\
    \              {\n                \"synonym_text\": \"NaCl\",\n              \
    \  \"synonym_type\": \"EXACT\"\n              },\n              {\n          \
    \      \"synonym_text\": \"table salt\",\n                \"synonym_type\": \"\
    EXACT\"\n              }\n            ]\n          },\n          {\n         \
    \   \"preferred_term\": \"Disodium phosphate\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.5\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"supplier_catalog\"\
    : {\n              \"supplier_name\": \"Difco/BD Brain Heart Infusion\",\n   \
    \           \"catalog_number\": \"237500\",\n              \"product_url\": \"\
    https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\n            },\n  \
    \          \"notes\": \"pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart\
    \ Infusion commercial product\",\n            \"synonyms\": [\n              {\n\
    \                \"synonym_text\": \"Na2HPO4\",\n                \"synonym_type\"\
    : \"EXACT\"\n              },\n              {\n                \"synonym_text\"\
    : \"disodium hydrogen phosphate\",\n                \"synonym_type\": \"EXACT\"\
    \n              },\n              {\n                \"synonym_text\": \"sodium\
    \ phosphate dibasic\",\n                \"synonym_type\": \"EXACT\"\n        \
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"NaCl\",\n            \"term\": {\n              \"id\": \"CHEBI:26710\",\n\
    \              \"label\": \"sodium chloride\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"20\",\n              \"unit\":\
    \ \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            }\n\
    \          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm263\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263\"\
    ,\n        \"source_locator\": \"JCM263 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water\\n1.0\\nL\",\n        \"snapshot_sha256\": \"fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1\"\
    ,\n        \"parsed_text_sha256\": \"b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicitly listed 1000 ml or 1\
    \ L water as a batch liquid input. It is not an instruction to make the complete\
    \ preparation up to that final volume.\"\n  },\n  {\n    \"decision_id\": \"q22\"\
    ,\n    \"subject\": \"Receiving soil-extract volume\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 soil-extract volume and dependency\",\n\
    \        \"exact_source_quote\": \"Soil extract (See Medium No.\\n102\\n)\\n1.0\\\
    nL\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"The target and TOGO owner store 1 G_PER_L,\
    \ but the primary gives 1 L soil extract. Represent the volume and resolve the\
    \ named stock instead of retaining a mass-rate stub.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"subject\": \"JCM342 owner missing soil-extract descriptor\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm342\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 soil-extract volume and dependency\",\n\
    \        \"exact_source_quote\": \"Soil extract (See Medium No.\\n102\\n)\\n1.0\\\
    nL\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"The owner retains the stock procedure\
    \ but lacks the explicit 1 L receiving addition. Add the source descriptor with\
    \ its exact dependency and volume.\"\n  },\n  {\n    \"decision_id\": \"q24\"\
    ,\n    \"subject\": \"Soil stock 400 g starting material\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"400.0\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm102\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102\"\
    ,\n        \"source_locator\": \"Only JCM102 soil-extract subsection\",\n    \
    \    \"exact_source_quote\": \"Suspend 400 g of air-dried garden       soil in\
    \ 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant\
    \ after sedimentation       for a few hours and centrifugation.\",\n        \"\
    snapshot_sha256\": \"cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c\"\
    ,\n        \"parsed_text_sha256\": \"ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1\"\
    \n      }\n    ],\n    \"rationale\": \"The source gives 400 g starting soil in\
    \ 1 L tap water, not 400 g/L of recovered extract. Extraction, settling and centrifugation\
    \ do not specify the recovered final stock volume. Preserve the batch mass and\
    \ do not promote the repaired stock rate.\"\n  },\n  {\n    \"decision_id\": \"\
    q25\",\n    \"subject\": \"Soil stock 1 L tap water\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm102\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102\"\
    ,\n        \"source_locator\": \"Only JCM102 soil-extract subsection\",\n    \
    \    \"exact_source_quote\": \"Suspend 400 g of air-dried garden       soil in\
    \ 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant\
    \ after sedimentation       for a few hours and centrifugation.\",\n        \"\
    snapshot_sha256\": \"cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c\"\
    ,\n        \"parsed_text_sha256\": \"ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1\"\
    \n      }\n    ],\n    \"rationale\": \"The local 1 L stock-water value and unit\
    \ match the primary input exactly; claim-level evidence is absent. This is distinct\
    \ from the receiving 1 L soil extract.\"\n  },\n  {\n    \"decision_id\": \"q26\"\
    ,\n    \"subject\": \"Soil extraction cycle and physical separation\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Suspend 400 g of air-dried garden soil in 1.0 L of tap water and autoclave\
    \ at 121C for 1 hr. Use the clear supernatant after sedimentation for a few hours\
    \ and centrifugation.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Suspend 400 g air-dried garden soil in 1.0 L tap water and autoclave at 121\
    \ C for 1 hr. Use the clear supernatant after sedimentation for a few hours and\
    \ centrifugation.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Suspend 400 g air-dried garden soil in 1.0 L tap water and autoclave at 121\
    \ C for 1 hr to prepare Soil extract.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Let the soil slurry sediment for a few hours, then centrifuge and use the\
    \ clear supernatant as Soil extract.\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/nutrient_agar_with_25_soil_extract.yaml\",\n\
    \        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Suspend 400 g of air-dried garden soil in 1.0 L of tap water and autoclave\
    \ at 121C for 1 hr. Use the clear supernatant after sedimentation for a few hours\
    \ and centrifugation.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm102\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102\"\
    ,\n        \"source_locator\": \"Only JCM102 soil-extract subsection\",\n    \
    \    \"exact_source_quote\": \"Suspend 400 g of air-dried garden       soil in\
    \ 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant\
    \ after sedimentation       for a few hours and centrifugation.\",\n        \"\
    snapshot_sha256\": \"cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c\"\
    ,\n        \"parsed_text_sha256\": \"ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1\"\
    \n      }\n    ],\n    \"rationale\": \"Preserved procedure matches 121 C for\
    \ 1 hour, qualitative sedimentation for a few hours, centrifugation and clear-supernatant\
    \ recovery. Attach exact support; do not invent centrifuge speed, sedimentation\
    \ duration, or recovered yield.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n\
    \    \"subject\": \"Missing soil-stock structure and preparation in generated/TOGO\
    \ recipe\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm102\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102\"\
    ,\n        \"source_locator\": \"Only JCM102 soil-extract subsection\",\n    \
    \    \"exact_source_quote\": \"Suspend 400 g of air-dried garden       soil in\
    \ 1.0 L of tap water and autoclave       at 121C for 1 hr. Use the clear supernatant\
    \ after sedimentation       for a few hours and centrifugation.\",\n        \"\
    snapshot_sha256\": \"cb308a7129f5dfaf9c304c9f639fa5fad5b2c9b9632436a3d06b5a5a72c9fe7c\"\
    ,\n        \"parsed_text_sha256\": \"ab94b410f59c5f187f7b1e6d0fc871f7ebed9b97fc1de1b62624e5fbb553aed1\"\
    \n      },\n      {\n        \"source_key\": \"jcm342\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\",\n        \"source_locator\"\
    : \"JCM342 soil-extract volume and dependency\",\n        \"exact_source_quote\"\
    : \"Soil extract (See Medium No.\\n102\\n)\\n1.0\\nL\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"Populate only the named soil-stock procedure,\
    \ its 400 g starting soil and 1 L water. The parent medium main ingredients, 250\
    \ ml extract dose, 750 ml water and pH 7.0 remain excluded.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q28\",\n    \"subject\": \"Plain main-medium sterilization\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm28\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=28\"\
    ,\n        \"source_locator\": \"JCM page explicit default sterilization\",\n\
    \        \"exact_source_quote\": \"Unless otherwise stated, sterilize media by\
    \ autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"4b88ed256f2e87ccdafa84ee5d30695b0b8fdc99b9a24d38b6b23d00f62c5071\"\
    ,\n        \"parsed_text_sha256\": \"6c39f130134d078f178f82ddd669b77feb777a82bc2eeedcab30149c5ee3d113\"\
    \n      }\n    ],\n    \"rationale\": \"Add the source-specific main-medium 121°C,\
    \ 15-minute default, separately from soil-stock extraction at 121 C for 1 hour.\
    \ This JCM default is not transferred to DSM82.\"\n  },\n  {\n    \"decision_id\"\
    : \"q29\",\n    \"subject\": \"Salt-added main-medium sterilization\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n  \
    \    }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm263\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=263\"\
    ,\n        \"source_locator\": \"JCM page explicit default sterilization\",\n\
    \        \"exact_source_quote\": \"Unless otherwise stated, sterilize media by\
    \ autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"fd964076661f31a99fd1cf36d4ffaa786d296416836bc8a769108d2f899775b1\"\
    ,\n        \"parsed_text_sha256\": \"b74d20505309f767e3dd7063e21e4d715e15847abbdb6143a6b85ea170387af8\"\
    \n      }\n    ],\n    \"rationale\": \"Add the source-specific main-medium 121°C,\
    \ 15-minute default, separately from soil-stock extraction at 121 C for 1 hour.\
    \ This JCM default is not transferred to DSM82.\"\n  },\n  {\n    \"decision_id\"\
    : \"q30\",\n    \"subject\": \"Soil main-medium sterilization\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Suspend 400 g of air-dried garden soil in 1.0\
    \ L of tap water and autoclave at 121C for 1 hr. Use the clear supernatant after\
    \ sedimentation for a few hours and centrifugation.\"\n          }\n        ]\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM page explicit default sterilization\",\n\
    \        \"exact_source_quote\": \"Unless otherwise stated, sterilize media by\
    \ autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\"\
    ,\n        \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      }\n    ],\n    \"rationale\": \"Add the source-specific main-medium 121°C,\
    \ 15-minute default, separately from soil-stock extraction at 121 C for 1 hour.\
    \ This JCM default is not transferred to DSM82.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"subject\": \"Receiving pH and incubation temperature\",\n  \
    \  \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bhi_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm342\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342\"\
    ,\n        \"source_locator\": \"JCM342 opaque product row\",\n        \"exact_source_quote\"\
    : \"Brain heart infusion broth (BD-Difco)\\n37.0\\ng\",\n        \"snapshot_sha256\"\
    : \"0849ae7f188c52bd4b89885bf06254bb47ff1296c7c761828d5bfeb4cbc2e635\",\n    \
    \    \"parsed_text_sha256\": \"ab34339b45c8b2eccd80befb24da0e82549e4bd5e5b9c6b484aa726876f5e3fd\"\
    \n      },\n      {\n        \"source_key\": \"dsmz82\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium82.pdf\",\n     \
    \   \"source_locator\": \"Exact extracted source line containing 'Brain heart\
    \ infusion'\",\n        \"exact_source_quote\": \"Brain heart infusion       \
    \                18.5    g\",\n        \"snapshot_sha256\": \"10c4322a34d845352682f2df460c7757990e3ade220c0932bb3bf225df6ef347\"\
    ,\n        \"parsed_text_sha256\": \"4c599140d1b96e016541dae98dc24a0ba62fca8303f0e94baf20a05c98e3d8c2\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"Secondary comparison formula only\",\n        \"\
    exact_source_quote\": \"Final pH (at 25°C): 7.4±0.2\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"rationale\": \"These collection primaries do not establish\
    \ a receiving pH or incubation temperature. The local product note pH 7.4±0.2\
    \ belongs to an unverified secondary formulation; 25°C is a measurement condition,\
    \ not growth temperature. Parent JCM102 pH 7.0 stays excluded.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: bhi-soil-contributor-formulation-mixture
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Separate the soil recipe from plain, salt-added and glucose BHI
  description: The generated soil-medium identity carries DSM82 glucose/agar amounts
    while its six contributors represent four distinct primary formulations. The current
    conservative merger already guards scientific equality, so this is a stale generated-membership
    and owner-identity repair, not proof of a current blind merge.
  target_ids:
  - CultureMech:009715
  field_paths:
  - ingredients
  - solutions
  - notes
  evidence_ids:
  - dsm82
  - j28
  - j263
  - j342
  - provider337
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  issue_key: bhi-commercial-expansion-unverified
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore source-specific opaque BHI product amounts
  description: The shared expanded constituents and 200/250 g tissue-equivalence notes
    lack exact product/version support. DSM82 needs 18.5 g product while the JCM branches
    use 37 g; a generic secondary article cannot authenticate identical expanded rates
    across both.
  target_ids:
  - CultureMech:009715
  field_paths:
  - ingredients
  evidence_ids:
  - dsm82
  - j28
  - j263
  - j342
  - supplier-comparison
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  issue_key: bhi-soil-volume-stock-structure
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore the 1 L soil-extract addition and scoped stock
  description: The generated and TOGO descriptors are 1 G_PER_L empty solutions, while
    the JCM owner lacks the addition despite retaining its stock preparation. The
    named M94 stock 400 G_PER_L field also overstates recovered-extract basis.
  target_ids:
  - CultureMech:009715
  field_paths:
  - solutions
  - preparation_steps
  evidence_ids:
  - j342
  - soil102
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml
    role: Maintained named soil-stock dependency; only solutions[0].composition and
      stock preparation require this scoped follow-up, not the parent medium
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: bhi-source-stage-preparation-evidence
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Attach branch-specific amounts and preparation without inherited endpoints
  description: Opaque product quantities, water or soil volumes, agar branches and
    main sterilization are incomplete or unlinked. Source batch amounts must remain
    distinct from normalized provider rates and unsupported final-volume, pH and incubation
    assumptions.
  target_ids:
  - CultureMech:009715
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - ph_value
  - temperature_value
  evidence_ids:
  - dsm82
  - j28
  - j263
  - j342
  - soil102
  - provider82
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  issue_key: bhi-soil-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retain unresolved historical timestamp precision
  description: Malformed or timezone-absent history values remain historical assertions.
    Current code and current source responses do not establish their execution times
    or exact original source bytes.
  target_ids:
  - CultureMech:009715
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-full
  - historical-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  description: Repair each maintained formulation and exact source identity, then
    regenerate through the existing conservative gate and verify correct contributor
    membership and freshness.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009715
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  description: Use exact source product masses and preserve any independently supported
    expansion only with exact supplier/version evidence and explicit amount basis.
    Do not invent tissue yields or rescale unsupported constituent values.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009715
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  description: Represent receiving soil extract as 1 L, link only the exact soil subsection,
    retain 400 g soil plus 1 L tap water and separate the 121 C one-hour extraction
    from main-medium sterilization. Keep stock recovered volume unknown.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009715
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml
    role: Maintained named soil-stock dependency; only solutions[0].composition and
      stock preparation require this scoped follow-up, not the parent medium
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
  description: Attach exact claim-level evidence for each branch and its source stages;
    preserve unavailable or unestablished basis rather than converting listed water
    to measured final volume.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009715
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
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
  description: Append an evidenced clarification if recoverable while preserving original
    events and derivative report distinctions.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009715
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - No inferred UTC normalization or historical execution claim.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The exact current MediaDive82 request returned HTTP503. Complete collection primaries
  and current provider text remain available; no failed response authenticates historical
  amounts.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-045
- generated-medium
```
