# Source and formulation review: blood_agar_ii (CultureMech:004616)

- Review: 20261022T012524Z-culturemech-004616-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T01:04:16Z
- Finished UTC: 2026-10-22T01:25:24Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Blood Agar II is DSM245 basal medium220 plus an unqualified5% sheep-blood supplement. KOMODO245 separately reports50g/L and explicit per-litre basal rates; this provider representation does not establish the primary percentage basis. The external DSM101 match is wrong, owner FOODON labels differ from canonical labels, and the generated record omits the owners’ newer grounding and preparation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 432; batch 044 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-three task batches contain 430 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 433 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004616 | data/merge_yaml/merged/BLOOD_AGAR_II.yaml | generated | blood_agar_ii |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004616 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004616 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/432/strict.tsv |
| validate-terms | passed | True | CultureMech:004616 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004616 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004616 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive245api | unavailable | False | CultureMech:004616 | The current exact DSM245 API returned503. Historical local plan strings are derivative evidence and do not authenticate the original response; primary245/220 and current KOMODO245 remain available. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004616.

The four documented recipes completed; interpret the scope of each separately.

### Current identifiers, canonical labels and exact source forms

grounding: concern. Targets: CultureMech:004616.

16 asserted primary/secondary slots and 4 distinct captured IDs checked; 4 literal label differences. All 6 current secondary assertions join exact preferred-term MIM rows; no selected legacy ID slots. Target direct ingredient linkage is 2/5 primary (40.00%) and 2/5 secondary (40.00%) on a 0–100 linkage scale, not an accuracy score. The two maintained owners now carry FOODON03315719 and03315720, but their labels Casein peptone/Soy peptone differ from canonical mammalian milk protein (hydrolyzed)/vegetable protein, hydrolyzed. These broad material IDs are not nonexistent; preferred ingredient names should retain the more specific source wording while canonical labels are corrected. Generated casein/soy rows omit the newer term nodes. Sodium chloride and agar forms are supported; no universal identity is invented for blood or mixed peptones.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:004616.

21 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Attached evidence, historical derivatives and source versions

evidence: concern. Targets: CultureMech:004616.

Full target and both maintained-owner history/evidence arrays inspected. No local concentration evidence is attached. Relevant historical DSM245/KOMODO245 report decisions withheld claims on stock/percentage scope and remain derivative leads, not recovered original responses. Current owner grounding repairs are credited; target predates them. The older review is a prior observation, not source authority or a structured finding superseded here. Malformed .fZ and naive timestamps are preserved.

### DSM245/KOMODO245 and external graph link

identity: concern. Targets: CultureMech:004616.

The selected source identity is245 and its basal dependency is220. The stored kg_microbe_match points to101, whose formula differs materially. No exact replacement KG correspondence is invented from the source accession alone.

### Preparation, pH and growth scope

completeness: concern. Targets: CultureMech:004616.

Basal pH7.3 is supported, but its scope and basal water are not represented clearly in the generated target. DSM245 supplies no sterilization cycle, post-blood pH measurement or growth experiment. Named220 strain exceptions are excluded.

### Classification and duplicate lineage

scope: supported. Targets: CultureMech:004616.

Complex, undefined solid agar is compatible with the inspected blood-supplemented basal recipe. Source-duplicate provenance is supported at accession level; this does not resolve percentage semantics or establish organism growth.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:004616.

11 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "topic": "Sheep-blood percentage and provider mass rate",
    "decision": "conflict",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "PERCENT_W_V"
        },
        "decision": "conflict",
        "rationale": "DSM245 states5% without w/v, v/v or w/w. Preserve that unresolved basis; do not assume density. KOMODO separately reports50g/L, arithmetically5g per100ml, which can support a provider-scoped5%w/v representation but cannot retrospectively define DSM wording. No local attached claim evidence authenticates either representation."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "PERCENT_W_V"
        },
        "decision": "evidence_only",
        "rationale": "The current KOMODO table explicitly gives50g/L, equivalent to5g/100ml. Add exact provider-scoped evidence to this numerical representation; retain the unresolved DSM percentage basis and do not imply a density conversion."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "5",
          "unit": "PERCENT_W_V"
        },
        "decision": "unsupported",
        "rationale": "The DSM source has an unspecified5% basis, so PERCENT_W_V is not established by that primary. Retain the literal percentage without guessing v/v or converting it to a mass rate."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz245",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf",
        "source_locator": "Extracted text line 4",
        "exact_source_quote": "Medium 220 supplemented with 5% defibrinated sheep blood.",
        "snapshot_sha256": "3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19",
        "parsed_text_sha256": "eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list heading",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list, sheep-blood row",
        "exact_source_quote": "defibrinated sheep blood\ndefibrinated sheep blood\nrich-blood#\n50.00",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      }
    ],
    "rationale": "DSM245 states5% without w/v, v/v or w/w. Preserve that unresolved basis; do not assume density. KOMODO separately reports50g/L, arithmetically5g per100ml, which can support a provider-scoped5%w/v representation but cannot retrospectively define DSM wording. No local attached claim evidence authenticates either representation."
  },
  {
    "quantity_id": "q2",
    "topic": "Casein peptone — basal versus final basis",
    "decision": "evidence_only",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The basal mass is supported, but its stored final-medium G_PER_L basis is not independently established by DSM245/220. Preserve basal recipe scope and unknown supplemented final volume; a provider assertion is not a measurement or raw authentication of this historical DSM layer."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 4",
        "exact_source_quote": "Peptone from casein                                           15.0       g",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list heading",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Exact named metabolite row",
        "exact_source_quote": "Peptone from casein\nTryptone\nrich-peptone#\n15.00",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      }
    ],
    "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
  },
  {
    "quantity_id": "q3",
    "topic": "Soy peptone — basal versus final basis",
    "decision": "evidence_only",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The basal mass is supported, but its stored final-medium G_PER_L basis is not independently established by DSM245/220. Preserve basal recipe scope and unknown supplemented final volume; a provider assertion is not a measurement or raw authentication of this historical DSM layer."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 5",
        "exact_source_quote": "Peptone from soymeal                                           5.0       g",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list heading",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Exact named metabolite row",
        "exact_source_quote": "Peptone from soymeal\nPeptone from soy\nrich-peptone#\n5.00",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      }
    ],
    "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
  },
  {
    "quantity_id": "q4",
    "topic": "NaCl — basal versus final basis",
    "decision": "evidence_only",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The basal mass is supported, but its stored final-medium G_PER_L basis is not independently established by DSM245/220. Preserve basal recipe scope and unknown supplemented final volume; a provider assertion is not a measurement or raw authentication of this historical DSM layer."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 6",
        "exact_source_quote": "NaCl                                                           5.0       g",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list heading",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Exact named metabolite row",
        "exact_source_quote": "NaCl\nNaCl\nSEED-cpd00099#cpd00971##\n5.00",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      }
    ],
    "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
  },
  {
    "quantity_id": "q5",
    "topic": "Agar — basal versus final basis",
    "decision": "evidence_only",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The basal mass is supported, but its stored final-medium G_PER_L basis is not independently established by DSM245/220. Preserve basal recipe scope and unknown supplemented final volume; a provider assertion is not a measurement or raw authentication of this historical DSM layer."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 7",
        "exact_source_quote": "Agar                                                          15.0       g",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Metabolites list heading",
        "exact_source_quote": "Gram &amp; Mol amounts are per Liter of medium.",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      },
      {
        "source_key": "komodoDetail245",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245",
        "source_locator": "Exact named metabolite row",
        "exact_source_quote": "Agar\nAgar\nSEED-cpd13334###\n15.00",
        "snapshot_sha256": "c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011",
        "parsed_text_sha256": "2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4"
      }
    ],
    "rationale": "The explicit current KOMODO per-litre rate matches this number and unit, but no concentration evidence is attached. Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml water; blood supplementation and an unstated final volume prevent treating that batch alone as measured final Blood Agar II concentration."
  },
  {
    "quantity_id": "q6",
    "topic": "Basal pH7.3",
    "decision": "evidence_only",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only",
        "rationale": "The scalar7.3 is the basal220 adjustment. Attach that scope; do not state that pH was measured after blood addition or as a growth optimum."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only",
        "rationale": "The scalar7.3 is the basal220 adjustment. Attach that scope; do not state that pH was measured after blood addition or as a growth optimum."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "ph_value",
        "stored": 7.3,
        "decision": "evidence_only",
        "rationale": "The scalar7.3 is the basal220 adjustment. Attach that scope; do not state that pH was measured after blood addition or as a growth optimum."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 10",
        "exact_source_quote": "Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid Cm131).",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      }
    ],
    "rationale": "The scalar7.3 is the basal220 adjustment. Attach that scope; do not state that pH was measured after blood addition or as a growth optimum."
  },
  {
    "quantity_id": "q7",
    "topic": "Basal water1000ml, missing recipe context",
    "decision": "add",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Document the basal220 water input and its relationship to blood supplementation. Preserve the existing DSM pH step, but separate its Tryptone Soya Agar identity sentence from the supplemented-medium identity. Do not infer1000ml measured final supplemented volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Document the basal220 water input and its relationship to blood supplementation. Preserve the existing DSM pH step, but separate its Tryptone Soya Agar identity sentence from the supplemented-medium identity. Do not infer1000ml measured final supplemented volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid CM 131)."
          }
        ],
        "decision": "add",
        "rationale": "Document the basal220 water input and its relationship to blood supplementation. Preserve the existing DSM pH step, but separate its Tryptone Soya Agar identity sentence from the supplemented-medium identity. Do not infer1000ml measured final supplemented volume."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 8",
        "exact_source_quote": "Distilled water                                             1000.0      ml",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "dsmz245",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf",
        "source_locator": "Extracted text line 4",
        "exact_source_quote": "Medium 220 supplemented with 5% defibrinated sheep blood.",
        "snapshot_sha256": "3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19",
        "parsed_text_sha256": "eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316"
      }
    ],
    "rationale": "Document the basal220 water input and its relationship to blood supplementation. Preserve the existing DSM pH step, but separate its Tryptone Soya Agar identity sentence from the supplemented-medium identity. Do not infer1000ml measured final supplemented volume."
  },
  {
    "quantity_id": "q8",
    "topic": "Existing DSM basal preparation wording",
    "decision": "correct",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid CM 131).",
        "decision": "correct",
        "rationale": "Keep pH7.3 as basal preparation; scope “Medium is identical with Tryptone Soya Agar” to unsupplemented220, not to the blood-supplemented245 formulation."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 10",
        "exact_source_quote": "Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid Cm131).",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      },
      {
        "source_key": "dsmz245",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf",
        "source_locator": "Extracted text line 4",
        "exact_source_quote": "Medium 220 supplemented with 5% defibrinated sheep blood.",
        "snapshot_sha256": "3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19",
        "parsed_text_sha256": "eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316"
      }
    ],
    "rationale": "Keep pH7.3 as basal preparation; scope “Medium is identical with Tryptone Soya Agar” to unsupplemented220, not to the blood-supplemented245 formulation."
  },
  {
    "quantity_id": "q9",
    "topic": "Named DSM21449/21450 NaCl10g/L — excluded variant",
    "decision": "unsupported",
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 13",
        "exact_source_quote": " NaCl                                                          10.0    g/L",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      }
    ],
    "rationale": "This parent-medium instruction applies only to its named strain variant. No matching target strain is asserted; do not transfer this supplement to Blood Agar II."
  },
  {
    "quantity_id": "q10",
    "topic": "Named DSM21449/21450 MnSO4 10mg/L — excluded variant",
    "decision": "unsupported",
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 14",
        "exact_source_quote": " MnSO4                                                         10.0   mg/L",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      }
    ],
    "rationale": "This parent-medium instruction applies only to its named strain variant. No matching target strain is asserted; do not transfer this supplement to Blood Agar II."
  },
  {
    "quantity_id": "q11",
    "topic": "Named DSM5746 methanol10ml/L — excluded variant",
    "decision": "unsupported",
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz220Context",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf",
        "source_locator": "Extracted text line 17",
        "exact_source_quote": " Methanol                                                      10.0   ml/L",
        "snapshot_sha256": "7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8",
        "parsed_text_sha256": "311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547"
      }
    ],
    "rationale": "This parent-medium instruction applies only to its named strain variant. No matching target strain is asserted; do not transfer this supplement to Blood Agar II."
  }
]

## Findings

### f1: Resolve the incorrect DSM101 graph match

major / open / confirmed; issue key: culturemech.004616.wrong-kg101.

The target and both maintained owners point to mediadive.medium:101, a different nutrient/salt medium. DSM245 explicitly delegates to220 plus sheep blood.

### f2: Keep the DSM percentage unresolved and distinguish provider rates

major / open / confirmed; issue key: culturemech.004616.blood-basis-and-basal-scope.

Primary5% lacks a basis while KOMODO explicitly gives50g/L. Flattened basal amounts also lack the DSM supplemented final-volume basis; available provider rates must remain provider-scoped.

### f3: Correct owner canonical labels and carry forward grounded source detail

minor / open / confirmed; issue key: culturemech.004616.canonical-foodon-labels.

Both current owners added FOODON terms, but four asserted label slots use ingredient names rather than the captured canonical labels. The generated record omits these newer terms.

### f4: Attach stage-specific claims and preserve historical limits

minor / open / confirmed; issue key: culturemech.004616.source-linkage-history.

No concentration evidence is attached, basal identity text is unscoped, and the current source version cannot authenticate the unavailable historical API. Historical timestamp defects remain explicit.

## Recommended Actions And Acceptance Checks

### a1

Remove or correct the external match only after verifying the exact intended KG record; do not auto-substitute a plausible accession.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain both exact source representations with scoped evidence, resolve the primary percentage before assigning a basis, and preserve basal versus supplemented stages without density/final-volume assumptions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain Casein peptone/Soy peptone as preferred names, review the broad material IDs, use exact canonical term labels and regenerate only after source corrections.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add exact source claims at ingredient/root stock scope, preserve old events, and label basal identity/preparation separately from the supplemented medium.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BLOOD_AGAR_II.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/blood_agar_ii.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BLOOD_AGAR_II.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BLOOD_AGAR_II.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch044/432/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/432/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BLOOD_AGAR_II.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BLOOD_AGAR_II.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BLOOD_AGAR_II.yaml:1:id: CultureMech:004616<br>./data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml:1:id: CultureMech:004616<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch044/source-preflight-bound/432/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 12 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| main | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf; Full source identity, formulation and scoped preparation | supports | Exact DSM245 definition delegates the basal recipe to220 and states5% defibrinated sheep blood without a percentage basis. |
| basal220 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf; Full source identity, formulation and scoped preparation | supports | Complete basal220 batch, pH and separate named-strain exceptions read. Water1000ml is a recipe input; no final supplemented volume is established. |
| provider245 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245; Full source identity, formulation and scoped preparation | supports | Exact KOMODO245 table explicitly reports gram and molar amounts per litre. Sheep blood50g/L is a provider claim, not proof that DSM245 meant w/v. |
| wrong101 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium101.pdf; Full source identity, formulation and scoped preparation | supports | DSM101 is nutrient agar/broth with30g NaCl and a different peptone/meat formula; it is not DSM245 blood agar. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Full source identity, formulation and scoped preparation | supports | Exact KOMODO245 catalog identity and DSM245 instructions link inspected. |
| mediadive245api-attempt | https://mediadive.dsmz.de/rest/medium/245; Preserved exact public retrieval result | context_only | The current exact DSM245 API returned503. Historical local plan strings are derivative evidence and do not authenticate the original response; primary245/220 and current KOMODO245 remain available. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Full source identity, formulation and scoped preparation | supports | CHEBI:26710 resolves to sodium chloride. Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Full source identity, formulation and scoped preparation | supports | CHEBI:2509 resolves to agar. Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| foodon03315719 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315719; Full source identity, formulation and scoped preparation | supports | FOODON:03315719 resolves to mammalian milk protein (hydrolyzed). Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| foodon03315720 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720; Full source identity, formulation and scoped preparation | supports | FOODON:03315720 resolves to vegetable protein, hydrolyzed. Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch044/432/grounding-inventory.json; Every asserted primary/secondary slot; exact captured OLS objects and pinned current MIM rows | context_only | Complete local slot correspondence, canonical labels and supplied-form distinctions. No invented IDs for unresolved complex products. |
| history-metadata | data/merge_yaml/merged/BLOOD_AGAR_II.yaml; data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml; data/normalized_yaml/bacterial/blood_agar_ii.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.579568"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.579568"}]}, {"input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml", "events": 6, "timestamp_issues": []}] |
| history-evidence | /private/tmp/culturemech-review-work-batch044/432/history-evidence-inventory.json; Full current history/evidence arrays and exact relevant historical report joins | context_only | Full target and both maintained-owner history/evidence arrays inspected. No local concentration evidence is attached. Relevant historical DSM245/KOMODO245 report decisions withheld claims on stock/percentage scope and remain derivative leads, not recovered original responses. Current owner grounding repairs are credited; target predates them. The older review is a prior observation, not source authority or a structured finding superseded here. Malformed .fZ and naive timestamps are preserved. |
| writer-0 | scripts/repair_bacterial_score10_exact_terms_batch2.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant casein/soy mapping constants and repair functions, current exact-formulation merge guards and target/owner differences inspected. Current code is not assumed to have caused older copied labels or loss of fields. |
| writer-1 | scripts/repair_komodo_jcm_score10_exact_terms.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant casein/soy mapping constants and repair functions, current exact-formulation merge guards and target/owner differences inspected. Current code is not assumed to have caused older copied labels or loss of fields. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant casein/soy mapping constants and repair functions, current exact-formulation merge guards and target/owner differences inspected. Current code is not assumed to have caused older copied labels or loss of fields. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant casein/soy mapping constants and repair functions, current exact-formulation merge guards and target/owner differences inspected. Current code is not assumed to have caused older copied labels or loss of fields. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch044/432/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current exact DSM245 API returned503. Historical local plan strings are derivative evidence and do not authenticate the original response; primary245/220 and current KOMODO245 remain available.
- DSM245 percentage basis and measured final supplemented volume remain unknown. Current KOMODO rates do not prove what the historical DSM import meant.
- An exact replacement KG-Microbe identity was not verified. No incubation or strain-specific growth claim is established by these recipe sources.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012524Z-culturemech-004616-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: blood_agar_ii (CultureMech:004616)'
started_at: '2026-10-22T01:04:16Z'
finished_at: '2026-10-22T01:25:24Z'
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
summary: Blood Agar II is DSM245 basal medium220 plus an unqualified5% sheep-blood
  supplement. KOMODO245 separately reports50g/L and explicit per-litre basal rates;
  this provider representation does not establish the primary percentage basis. The
  external DSM101 match is wrong, owner FOODON labels differ from canonical labels,
  and the generated record omits the owners’ newer grounding and preparation.
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
  - path: data/merge_yaml/merged/BLOOD_AGAR_II.yaml
    sha256: d9133a7de330047c18a2ebdb0da9debc1ae2a29b614aa8bb1f6193a2901d0a69
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    sha256: 64efad30588c9f1e9b70c7ba1512b7bda95274f46f55a1dbc72aff16ee39935a
    role: context
  - path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
    sha256: a282b59c07987e8db8f372d7fec2a1cc31379cad10f7da5ab5d878564f2f55c8
    role: context
  - path: data/normalized_yaml/bacterial/caso_agar_merck_105458.yaml
    sha256: 0ba7e31982fb89c2aea1c6da35f01d304dbeec61c3115c20a8ad13665e4b7b1d
    role: context
  - path: data/normalized_yaml/bacterial/nutrient_agar_or_broth_with_nacl.yaml
    sha256: 90e226b2703096c9fe8bd8123959ca60c8bda9703eaf4df75ee50df870c5a774
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml.md
    sha256: 5a927bc8d3905aa773701ea4b5a55b51764156965e13c060cea4349465b15482
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/blood_agar_ii.yaml.md
    sha256: f091167edfca8699a11d5cfc72bfcf428589f88b27be011fa6fa4c660ebb5034
    role: context
  - path: reports/yaml_record_review/20260921T223151Z-BLOOD_AGAR_II.md
    sha256: bf551d0ce1a54aafc8cf3780d13d93f95142d0e647ca2b8e8738e2dbc7a7bffd
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_bacterial_score10_exact_terms_batch2.py
    sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
    role: context
  - path: scripts/repair_komodo_jcm_score10_exact_terms.py
    sha256: 0a38691e1964c28eec4502848e014223d36fc1fa90ebf7d78764034adf5bc973
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
  selection: Task review 432; batch 044 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:004616
targets:
- target_id: CultureMech:004616
  path: data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  label: blood_agar_ii
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BLOOD_AGAR_II.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch044/432/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/432/strict.tsv"
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004616
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
  - CultureMech:004616
- check_id: mediadive245api-source-access
  name: 'Exact source content access: mediadive245api'
  required: false
  status: unavailable
  summary: The current exact DSM245 API returned503. Historical local plan strings
    are derivative evidence and do not authenticate the original response; primary245/220
    and current KOMODO245 remain available.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - mediadive245api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/blood_agar_ii.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:42.459866Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BLOOD_AGAR_II.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch044/432/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:43.923818Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/432/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:45.541706Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BLOOD_AGAR_II.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:46.506881Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T01:25:23Z'
  support: supports
  summary: './data/merge_yaml/merged/BLOOD_AGAR_II.yaml:1:id: CultureMech:004616

    ./data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml:1:id: CultureMech:004616

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/source-preflight-bound/432/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T01:25:23Z'
  support: supports
  summary: 12 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: ed6080fcfcd7f8a68c17dff66ca95d6e131a4339216d6ea695a25e75b44c28fa
- evidence_id: main
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:52.317936Z'
  support: supports
  summary: Exact DSM245 definition delegates the basal recipe to220 and states5% defibrinated
    sheep blood without a percentage basis.
  quote: Medium 220 supplemented with 5% defibrinated sheep blood.
  snapshot_sha256: 3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19
- evidence_id: basal220
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:54.971324Z'
  support: supports
  summary: Complete basal220 batch, pH and separate named-strain exceptions read.
    Water1000ml is a recipe input; no final supplemented volume is established.
  snapshot_sha256: 7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8
- evidence_id: provider245
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:54:34.862440Z'
  support: supports
  summary: Exact KOMODO245 table explicitly reports gram and molar amounts per litre.
    Sheep blood50g/L is a provider claim, not proof that DSM245 meant w/v.
  quote: Gram & Mol amounts are per Liter of medium.
  snapshot_sha256: c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011
- evidence_id: wrong101
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium101.pdf
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:55.103419Z'
  support: supports
  summary: DSM101 is nutrient agar/broth with30g NaCl and a different peptone/meat
    formula; it is not DSM245 blood agar.
  snapshot_sha256: 5a064af3627f3bdcd449cf9e72ccdc2741fb3813d305dff47af4010262b0f114
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Exact KOMODO245 catalog identity and DSM245 instructions link inspected.
  quote: BLOOD AGAR II
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive245api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/245
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T00:53:52.946734Z'
  support: context_only
  summary: The current exact DSM245 API returned503. Historical local plan strings
    are derivative evidence and do not authenticate the original response; primary245/220
    and current KOMODO245 remain available.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Full captured scientific properties,
    annotations and synonyms inspected; identifier validity is separate from exact
    supplied-form support.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Full captured scientific properties, annotations
    and synonyms inspected; identifier validity is separate from exact supplied-form
    support.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: foodon03315719
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315719
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-21T08:42:32.147808Z'
  support: supports
  summary: FOODON:03315719 resolves to mammalian milk protein (hydrolyzed). Full captured
    scientific properties, annotations and synonyms inspected; identifier validity
    is separate from exact supplied-form support.
  snapshot_sha256: 003d7d18eee340eb5c43ae7608d034459540ad736e2eca09a4c08e70afa766fe
- evidence_id: foodon03315720
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:55.541194Z'
  support: supports
  summary: FOODON:03315720 resolves to vegetable protein, hydrolyzed. Full captured
    scientific properties, annotations and synonyms inspected; identifier validity
    is separate from exact supplied-form support.
  snapshot_sha256: aa063e8b88177611aba640828e84d3982b1b3b1c65b11647d89c9efbf6274c25
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/432/grounding-inventory.json
  locator: Every asserted primary/secondary slot; exact captured OLS objects and pinned
    current MIM rows
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Complete local slot correspondence, canonical labels and supplied-form
    distinctions. No invented IDs for unresolved complex products.
  snapshot_sha256: 992a60afceded9886f5a49e94c80af667b66abec3d7cae2a44752d4300ee2b84
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BLOOD_AGAR_II.yaml; data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml;
    data/normalized_yaml/bacterial/blood_agar_ii.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:58.579568"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:58.579568"}]}, {"input": "data/normalized_yaml/bacterial/blood_agar_ii.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: history-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/432/history-evidence-inventory.json
  locator: Full current history/evidence arrays and exact relevant historical report
    joins
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Full target and both maintained-owner history/evidence arrays inspected.
    No local concentration evidence is attached. Relevant historical DSM245/KOMODO245
    report decisions withheld claims on stock/percentage scope and remain derivative
    leads, not recovered original responses. Current owner grounding repairs are credited;
    target predates them. The older review is a prior observation, not source authority
    or a structured finding superseded here. Malformed .fZ and naive timestamps are
    preserved.
  snapshot_sha256: 7fd4b46597db7da2ca6d4922b58f4fb13f9995dd356824dfca90733e8d3bad74
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_bacterial_score10_exact_terms_batch2.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Relevant casein/soy mapping constants and repair functions, current exact-formulation
    merge guards and target/owner differences inspected. Current code is not assumed
    to have caused older copied labels or loss of fields.
  snapshot_sha256: b598b051c7cbec73cb52d49e116d8d1c33c052e3d9cf74877041ce1e58a16a44
- evidence_id: writer-1
  kind: record_content
  reference: scripts/repair_komodo_jcm_score10_exact_terms.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Relevant casein/soy mapping constants and repair functions, current exact-formulation
    merge guards and target/owner differences inspected. Current code is not assumed
    to have caused older copied labels or loss of fields.
  snapshot_sha256: 0a38691e1964c28eec4502848e014223d36fc1fa90ebf7d78764034adf5bc973
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Relevant casein/soy mapping constants and repair functions, current exact-formulation
    merge guards and target/owner differences inspected. Current code is not assumed
    to have caused older copied labels or loss of fields.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Relevant casein/soy mapping constants and repair functions, current exact-formulation
    merge guards and target/owner differences inspected. Current code is not assumed
    to have caused older copied labels or loss of fields.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/432/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T01:25:23Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 52c97bd6ca1b922394f6e3b08ef33d390ac180d510f6db7fcffcaeca96fdf814
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Current identifiers, canonical labels and exact source forms
  outcome: concern
  summary: 16 asserted primary/secondary slots and 4 distinct captured IDs checked;
    4 literal label differences. All 6 current secondary assertions join exact preferred-term
    MIM rows; no selected legacy ID slots. Target direct ingredient linkage is 2/5
    primary (40.00%) and 2/5 secondary (40.00%) on a 0–100 linkage scale, not an accuracy
    score. The two maintained owners now carry FOODON03315719 and03315720, but their
    labels Casein peptone/Soy peptone differ from canonical mammalian milk protein
    (hydrolyzed)/vegetable protein, hydrolyzed. These broad material IDs are not nonexistent;
    preferred ingredient names should retain the more specific source wording while
    canonical labels are corrected. Generated casein/soy rows omit the newer term
    nodes. Sodium chloride and agar forms are supported; no universal identity is
    invented for blood or mixed peptones.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - record
  - grounding-inventory
  - chebi26710
  - chebi2509
  - foodon03315719
  - foodon03315720
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 21 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: evidence-placement
  area: evidence
  topic: Attached evidence, historical derivatives and source versions
  outcome: concern
  summary: Full target and both maintained-owner history/evidence arrays inspected.
    No local concentration evidence is attached. Relevant historical DSM245/KOMODO245
    report decisions withheld claims on stock/percentage scope and remain derivative
    leads, not recovered original responses. Current owner grounding repairs are credited;
    target predates them. The older review is a prior observation, not source authority
    or a structured finding superseded here. Malformed .fZ and naive timestamps are
    preserved.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - record
  - history-evidence
  - bound-source-integrity
- assessment_id: identity
  area: identity
  topic: DSM245/KOMODO245 and external graph link
  outcome: concern
  summary: The selected source identity is245 and its basal dependency is220. The
    stored kg_microbe_match points to101, whose formula differs materially. No exact
    replacement KG correspondence is invented from the source accession alone.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - main
  - basal220
  - provider245
  - wrong101
- assessment_id: conditions
  area: completeness
  topic: Preparation, pH and growth scope
  outcome: concern
  summary: Basal pH7.3 is supported, but its scope and basal water are not represented
    clearly in the generated target. DSM245 supplies no sterilization cycle, post-blood
    pH measurement or growth experiment. Named220 strain exceptions are excluded.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - main
  - basal220
  - record
- assessment_id: classification
  area: scope
  topic: Classification and duplicate lineage
  outcome: supported
  summary: Complex, undefined solid agar is compatible with the inspected blood-supplemented
    basal recipe. Source-duplicate provenance is supported at accession level; this
    does not resolve percentage semantics or establish organism growth.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - main
  - provider245
  - catalog
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 11 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:004616
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"topic\": \"Sheep-blood percentage\
    \ and provider mass rate\",\n    \"decision\": \"conflict\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    PERCENT_W_V\"\n        },\n        \"decision\": \"conflict\",\n        \"rationale\"\
    : \"DSM245 states5% without w/v, v/v or w/w. Preserve that unresolved basis; do\
    \ not assume density. KOMODO separately reports50g/L, arithmetically5g per100ml,\
    \ which can support a provider-scoped5%w/v representation but cannot retrospectively\
    \ define DSM wording. No local attached claim evidence authenticates either representation.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"PERCENT_W_V\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ current KOMODO table explicitly gives50g/L, equivalent to5g/100ml. Add exact\
    \ provider-scoped evidence to this numerical representation; retain the unresolved\
    \ DSM percentage basis and do not imply a density conversion.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"PERCENT_W_V\"\n      \
    \  },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"The DSM\
    \ source has an unspecified5% basis, so PERCENT_W_V is not established by that\
    \ primary. Retain the literal percentage without guessing v/v or converting it\
    \ to a mass rate.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz245\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf\"\
    ,\n        \"source_locator\": \"Extracted text line 4\",\n        \"exact_source_quote\"\
    : \"Medium 220 supplemented with 5% defibrinated sheep blood.\",\n        \"snapshot_sha256\"\
    : \"3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19\",\n    \
    \    \"parsed_text_sha256\": \"eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list heading\",\n        \"exact_source_quote\"\
    : \"Gram & Mol amounts are per Liter of medium.\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list, sheep-blood row\",\n      \
    \  \"exact_source_quote\": \"defibrinated sheep blood\\ndefibrinated sheep blood\\\
    nrich-blood#\\n50.00\",\n        \"snapshot_sha256\": \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\"\
    ,\n        \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      }\n    ],\n    \"rationale\": \"DSM245 states5% without w/v, v/v or w/w.\
    \ Preserve that unresolved basis; do not assume density. KOMODO separately reports50g/L,\
    \ arithmetically5g per100ml, which can support a provider-scoped5%w/v representation\
    \ but cannot retrospectively define DSM wording. No local attached claim evidence\
    \ authenticates either representation.\"\n  },\n  {\n    \"quantity_id\": \"q2\"\
    ,\n    \"topic\": \"Casein peptone — basal versus final basis\",\n    \"decision\"\
    : \"evidence_only\",\n    \"layer_decisions\": [\n      {\n        \"input\":\
    \ \"target\",\n        \"field_path\": \"ingredients[1].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The explicit current KOMODO per-litre rate matches this number and unit, but\
    \ no concentration evidence is attached. Retain exact provider scope. DSM220 instead\
    \ gives a basal batch amount with1000ml water; blood supplementation and an unstated\
    \ final volume prevent treating that batch alone as measured final Blood Agar\
    \ II concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The explicit\
    \ current KOMODO per-litre rate matches this number and unit, but no concentration\
    \ evidence is attached. Retain exact provider scope. DSM220 instead gives a basal\
    \ batch amount with1000ml water; blood supplementation and an unstated final volume\
    \ prevent treating that batch alone as measured final Blood Agar II concentration.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The basal mass\
    \ is supported, but its stored final-medium G_PER_L basis is not independently\
    \ established by DSM245/220. Preserve basal recipe scope and unknown supplemented\
    \ final volume; a provider assertion is not a measurement or raw authentication\
    \ of this historical DSM layer.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 4\",\n        \"exact_source_quote\"\
    : \"Peptone from casein                                           15.0       g\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list heading\",\n        \"exact_source_quote\"\
    : \"Gram & Mol amounts are per Liter of medium.\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Exact named metabolite row\",\n        \"exact_source_quote\"\
    : \"Peptone from casein\\nTryptone\\nrich-peptone#\\n15.00\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit current KOMODO per-litre\
    \ rate matches this number and unit, but no concentration evidence is attached.\
    \ Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml\
    \ water; blood supplementation and an unstated final volume prevent treating that\
    \ batch alone as measured final Blood Agar II concentration.\"\n  },\n  {\n  \
    \  \"quantity_id\": \"q3\",\n    \"topic\": \"Soy peptone — basal versus final\
    \ basis\",\n    \"decision\": \"evidence_only\",\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The explicit current KOMODO per-litre rate matches this number and unit, but\
    \ no concentration evidence is attached. Retain exact provider scope. DSM220 instead\
    \ gives a basal batch amount with1000ml water; blood supplementation and an unstated\
    \ final volume prevent treating that batch alone as measured final Blood Agar\
    \ II concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The explicit\
    \ current KOMODO per-litre rate matches this number and unit, but no concentration\
    \ evidence is attached. Retain exact provider scope. DSM220 instead gives a basal\
    \ batch amount with1000ml water; blood supplementation and an unstated final volume\
    \ prevent treating that batch alone as measured final Blood Agar II concentration.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The basal mass\
    \ is supported, but its stored final-medium G_PER_L basis is not independently\
    \ established by DSM245/220. Preserve basal recipe scope and unknown supplemented\
    \ final volume; a provider assertion is not a measurement or raw authentication\
    \ of this historical DSM layer.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 5\",\n        \"exact_source_quote\"\
    : \"Peptone from soymeal                                           5.0       g\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list heading\",\n        \"exact_source_quote\"\
    : \"Gram & Mol amounts are per Liter of medium.\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Exact named metabolite row\",\n        \"exact_source_quote\"\
    : \"Peptone from soymeal\\nPeptone from soy\\nrich-peptone#\\n5.00\",\n      \
    \  \"snapshot_sha256\": \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\"\
    ,\n        \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit current KOMODO per-litre\
    \ rate matches this number and unit, but no concentration evidence is attached.\
    \ Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml\
    \ water; blood supplementation and an unstated final volume prevent treating that\
    \ batch alone as measured final Blood Agar II concentration.\"\n  },\n  {\n  \
    \  \"quantity_id\": \"q4\",\n    \"topic\": \"NaCl — basal versus final basis\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The explicit current KOMODO per-litre rate matches this number and unit, but\
    \ no concentration evidence is attached. Retain exact provider scope. DSM220 instead\
    \ gives a basal batch amount with1000ml water; blood supplementation and an unstated\
    \ final volume prevent treating that batch alone as measured final Blood Agar\
    \ II concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The explicit\
    \ current KOMODO per-litre rate matches this number and unit, but no concentration\
    \ evidence is attached. Retain exact provider scope. DSM220 instead gives a basal\
    \ batch amount with1000ml water; blood supplementation and an unstated final volume\
    \ prevent treating that batch alone as measured final Blood Agar II concentration.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The basal mass\
    \ is supported, but its stored final-medium G_PER_L basis is not independently\
    \ established by DSM245/220. Preserve basal recipe scope and unknown supplemented\
    \ final volume; a provider assertion is not a measurement or raw authentication\
    \ of this historical DSM layer.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 6\",\n        \"exact_source_quote\"\
    : \"NaCl                                                           5.0       g\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list heading\",\n        \"exact_source_quote\"\
    : \"Gram & Mol amounts are per Liter of medium.\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Exact named metabolite row\",\n        \"exact_source_quote\"\
    : \"NaCl\\nNaCl\\nSEED-cpd00099#cpd00971##\\n5.00\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit current KOMODO per-litre\
    \ rate matches this number and unit, but no concentration evidence is attached.\
    \ Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml\
    \ water; blood supplementation and an unstated final volume prevent treating that\
    \ batch alone as measured final Blood Agar II concentration.\"\n  },\n  {\n  \
    \  \"quantity_id\": \"q5\",\n    \"topic\": \"Agar — basal versus final basis\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"15\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The explicit current KOMODO per-litre rate matches this number and unit, but\
    \ no concentration evidence is attached. Retain exact provider scope. DSM220 instead\
    \ gives a basal batch amount with1000ml water; blood supplementation and an unstated\
    \ final volume prevent treating that batch alone as measured final Blood Agar\
    \ II concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The explicit\
    \ current KOMODO per-litre rate matches this number and unit, but no concentration\
    \ evidence is attached. Retain exact provider scope. DSM220 instead gives a basal\
    \ batch amount with1000ml water; blood supplementation and an unstated final volume\
    \ prevent treating that batch alone as measured final Blood Agar II concentration.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The basal mass\
    \ is supported, but its stored final-medium G_PER_L basis is not independently\
    \ established by DSM245/220. Preserve basal recipe scope and unknown supplemented\
    \ final volume; a provider assertion is not a measurement or raw authentication\
    \ of this historical DSM layer.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 7\",\n        \"exact_source_quote\"\
    : \"Agar                                                          15.0       g\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Metabolites list heading\",\n        \"exact_source_quote\"\
    : \"Gram & Mol amounts are per Liter of medium.\",\n        \"snapshot_sha256\"\
    : \"c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n    \
    \    \"parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail245\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245\"\
    ,\n        \"source_locator\": \"Exact named metabolite row\",\n        \"exact_source_quote\"\
    : \"Agar\\nAgar\\nSEED-cpd13334###\\n15.00\",\n        \"snapshot_sha256\": \"\
    c7657c6d573267d99ba1e19c0ffb13e04f63765a6b219d56965c5f4c4afb3011\",\n        \"\
    parsed_text_sha256\": \"2708881797064ee51f0218dfa11bfac47bf62da2c379c739779641d8436326f4\"\
    \n      }\n    ],\n    \"rationale\": \"The explicit current KOMODO per-litre\
    \ rate matches this number and unit, but no concentration evidence is attached.\
    \ Retain exact provider scope. DSM220 instead gives a basal batch amount with1000ml\
    \ water; blood supplementation and an unstated final volume prevent treating that\
    \ batch alone as measured final Blood Agar II concentration.\"\n  },\n  {\n  \
    \  \"quantity_id\": \"q6\",\n    \"topic\": \"Basal pH7.3\",\n    \"decision\"\
    : \"evidence_only\",\n    \"layer_decisions\": [\n      {\n        \"input\":\
    \ \"target\",\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The scalar7.3\
    \ is the basal220 adjustment. Attach that scope; do not state that pH was measured\
    \ after blood addition or as a growth optimum.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\",\n \
    \       \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The scalar7.3 is the basal220 adjustment.\
    \ Attach that scope; do not state that pH was measured after blood addition or\
    \ as a growth optimum.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"The scalar7.3 is the\
    \ basal220 adjustment. Attach that scope; do not state that pH was measured after\
    \ blood addition or as a growth optimum.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 10\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid Cm131).\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      }\n    ],\n    \"rationale\": \"The scalar7.3 is the basal220 adjustment.\
    \ Attach that scope; do not state that pH was measured after blood addition or\
    \ as a growth optimum.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"topic\"\
    : \"Basal water1000ml, missing recipe context\",\n    \"decision\": \"add\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"rationale\": \"Document the basal220 water input\
    \ and its relationship to blood supplementation. Preserve the existing DSM pH\
    \ step, but separate its Tryptone Soya Agar identity sentence from the supplemented-medium\
    \ identity. Do not infer1000ml measured final supplemented volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Document the basal220\
    \ water input and its relationship to blood supplementation. Preserve the existing\
    \ DSM pH step, but separate its Tryptone Soya Agar identity sentence from the\
    \ supplemented-medium identity. Do not infer1000ml measured final supplemented\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"ADJUST_PH\"\
    ,\n            \"description\": \"Adjust pH to 7.3. Medium is identical with Tryptone\
    \ Soya Agar (Oxoid CM 131).\"\n          }\n        ],\n        \"decision\":\
    \ \"add\",\n        \"rationale\": \"Document the basal220 water input and its\
    \ relationship to blood supplementation. Preserve the existing DSM pH step, but\
    \ separate its Tryptone Soya Agar identity sentence from the supplemented-medium\
    \ identity. Do not infer1000ml measured final supplemented volume.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz220Context\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\"\
    ,\n        \"source_locator\": \"Extracted text line 8\",\n        \"exact_source_quote\"\
    : \"Distilled water                                             1000.0      ml\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"dsmz245\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 4\",\n        \"exact_source_quote\"\
    : \"Medium 220 supplemented with 5% defibrinated sheep blood.\",\n        \"snapshot_sha256\"\
    : \"3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19\",\n    \
    \    \"parsed_text_sha256\": \"eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316\"\
    \n      }\n    ],\n    \"rationale\": \"Document the basal220 water input and\
    \ its relationship to blood supplementation. Preserve the existing DSM pH step,\
    \ but separate its Tryptone Soya Agar identity sentence from the supplemented-medium\
    \ identity. Do not infer1000ml measured final supplemented volume.\"\n  },\n \
    \ {\n    \"quantity_id\": \"q8\",\n    \"topic\": \"Existing DSM basal preparation\
    \ wording\",\n    \"decision\": \"correct\",\n    \"layer_decisions\": [\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/blood_agar_ii.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid CM 131).\"\
    ,\n        \"decision\": \"correct\",\n        \"rationale\": \"Keep pH7.3 as\
    \ basal preparation; scope “Medium is identical with Tryptone Soya Agar” to unsupplemented220,\
    \ not to the blood-supplemented245 formulation.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 10\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid Cm131).\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      },\n      {\n        \"source_key\": \"dsmz245\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 4\",\n        \"exact_source_quote\"\
    : \"Medium 220 supplemented with 5% defibrinated sheep blood.\",\n        \"snapshot_sha256\"\
    : \"3fcf183526b31ca003104e094239c1cdc738060c47d3b28c8b24fdf71d5d7b19\",\n    \
    \    \"parsed_text_sha256\": \"eef006d62ca1a711facfd81a2ce4eef59a22026f679bf984185c29f8c3884316\"\
    \n      }\n    ],\n    \"rationale\": \"Keep pH7.3 as basal preparation; scope\
    \ “Medium is identical with Tryptone Soya Agar” to unsupplemented220, not to the\
    \ blood-supplemented245 formulation.\"\n  },\n  {\n    \"quantity_id\": \"q9\"\
    ,\n    \"topic\": \"Named DSM21449/21450 NaCl10g/L — excluded variant\",\n   \
    \ \"decision\": \"unsupported\",\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 13\",\n        \"exact_source_quote\"\
    : \" NaCl                                                          10.0    g/L\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      }\n    ],\n    \"rationale\": \"This parent-medium instruction applies\
    \ only to its named strain variant. No matching target strain is asserted; do\
    \ not transfer this supplement to Blood Agar II.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q10\",\n    \"topic\": \"Named DSM21449/21450 MnSO4 10mg/L — excluded variant\"\
    ,\n    \"decision\": \"unsupported\",\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 14\",\n        \"exact_source_quote\"\
    : \" MnSO4                                                         10.0   mg/L\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      }\n    ],\n    \"rationale\": \"This parent-medium instruction applies\
    \ only to its named strain variant. No matching target strain is asserted; do\
    \ not transfer this supplement to Blood Agar II.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q11\",\n    \"topic\": \"Named DSM5746 methanol10ml/L — excluded variant\"\
    ,\n    \"decision\": \"unsupported\",\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz220Context\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium220.pdf\",\n    \
    \    \"source_locator\": \"Extracted text line 17\",\n        \"exact_source_quote\"\
    : \" Methanol                                                      10.0   ml/L\"\
    ,\n        \"snapshot_sha256\": \"7ad4784ef10067569e736bf92c134dbaa39c6128106efe804ed595a1c42c40b8\"\
    ,\n        \"parsed_text_sha256\": \"311b355854b9882d5ccf2bcfdf2e673b76d35eb245fb5fdebcd38a92f6da2547\"\
    \n      }\n    ],\n    \"rationale\": \"This parent-medium instruction applies\
    \ only to its named strain variant. No matching target strain is asserted; do\
    \ not transfer this supplement to Blood Agar II.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.004616.wrong-kg101
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the incorrect DSM101 graph match
  description: The target and both maintained owners point to mediadive.medium:101,
    a different nutrient/salt medium. DSM245 explicitly delegates to220 plus sheep
    blood.
  target_ids:
  - CultureMech:004616
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - main
  - basal220
  - wrong101
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.5
  native_severity: P2
  normalization_reason: P2.5 is normalized to major because this is an incorrect cross-medium
    equivalence link, not merely redundant duplicate storage; the selected245 target
    identity remains recoverable.
- finding_id: f2
  issue_key: culturemech.004616.blood-basis-and-basal-scope
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Keep the DSM percentage unresolved and distinguish provider rates
  description: Primary5% lacks a basis while KOMODO explicitly gives50g/L. Flattened
    basal amounts also lack the DSM supplemented final-volume basis; available provider
    rates must remain provider-scoped.
  target_ids:
  - CultureMech:004616
  field_paths:
  - ingredients[0].concentration
  - ingredients
  - preparation_steps
  evidence_ids:
  - main
  - basal220
  - provider245
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
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
  issue_key: culturemech.004616.canonical-foodon-labels
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Correct owner canonical labels and carry forward grounded source detail
  description: Both current owners added FOODON terms, but four asserted label slots
    use ingredient names rather than the captured canonical labels. The generated
    record omits these newer terms.
  target_ids:
  - CultureMech:004616
  field_paths:
  - ingredients[1].term
  - ingredients[2].term
  evidence_ids:
  - grounding-inventory
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.004616.source-linkage-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach stage-specific claims and preserve historical limits
  description: No concentration evidence is attached, basal identity text is unscoped,
    and the current source version cannot authenticate the unavailable historical
    API. Historical timestamp defects remain explicit.
  target_ids:
  - CultureMech:004616
  field_paths:
  - ingredients
  - references
  - curation_history
  - preparation_steps
  evidence_ids:
  - history-evidence
  - history-metadata
  - basal220
  - provider245
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is elevated to minor because specific provider-versus-primary
    and basal-versus-final claims lack recoverable linkage despite supported literal
    numbers; historical access gaps are reported separately.
actions:
- action_id: a1
  description: Remove or correct the external match only after verifying the exact
    intended KG record; do not auto-substitute a plausible accession.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004616
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
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
  description: Retain both exact source representations with scoped evidence, resolve
    the primary percentage before assigning a basis, and preserve basal versus supplemented
    stages without density/final-volume assumptions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004616
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
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
  description: Retain Casein peptone/Soy peptone as preferred names, review the broad
    material IDs, use exact canonical term labels and regenerate only after source
    corrections.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004616
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
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
  description: Add exact source claims at ingredient/root stock scope, preserve old
    events, and label basal identity/preparation separately from the supplemented
    medium.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004616
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_ii.yaml
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
- The current exact DSM245 API returned503. Historical local plan strings are derivative
  evidence and do not authenticate the original response; primary245/220 and current
  KOMODO245 remain available.
- DSM245 percentage basis and measured final supplemented volume remain unknown. Current
  KOMODO rates do not prove what the historical DSM import meant.
- An exact replacement KG-Microbe identity was not verified. No incubation or strain-specific
  growth claim is established by these recipe sources.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-044
- generated-medium
```
