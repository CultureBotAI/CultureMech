# Source and formulation review: bicarbonate_buffered_medium (CultureMech:007689)

- Review: 20261022T003626Z-culturemech-007689-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T00:25:08Z
- Finished UTC: 2026-10-22T00:36:26Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record combines distinct glycerol, citrate and maltose substrate variants and retains obsolete empty stocks, volume-as-mass units, resazurin mg-as-g and an anhydrous phosphate mapping. September maintained-owner repairs already restore nine named stocks, correct main units/hydrate and preparation. Remaining owner concerns are unqualified percentages represented as w/v, unsupported final-volume denominators, source-specific maltose grounding and a current MIM correspondence gap. Preserve source stages and credit those repairs.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 427; batch 043 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-two task batches contain 420 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 423 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007689 | data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml | generated | bicarbonate_buffered_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007689 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007689 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/427/strict.tsv |
| validate-terms | passed | True | CultureMech:007689 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007689 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007689 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Current MIM secondary correspondence for selected M1168 maltose | unavailable | True | CultureMech:007689 | The exact pinned current index has no CHEBI:18167 preferred MAPPED row. Historical derivation and source anomer remain unresolved; no guessed mapping replacement. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007689.

The four documented recipes completed; interpret the scope of each separately.

### All selected-layer ontology slots and current MIM correspondence

grounding: concern. Targets: CultureMech:007689.

38 distinct selected-layer IDs have exact nonobsolete OLS labels. Target has 8/9 primary links and 5/9 secondary links; optional missing links are not automatically errors. The M1168 alpha-maltose secondary key CHEBI:18167 has no exact current preferred MAPPED row in the pinned index. This current negative lookup does not establish historical provenance. All other asserted current secondary keys have exact preferred rows. Excluded-parent legacy001072 is outside this review transfer.

### Source forms and specificity

grounding: concern. Targets: CultureMech:007689.

The generated Na2HPO4·2H2O is mapped to anhydrous CHEBI:34683; all four maintained owners correctly use dihydrate CHEBI:91258. Explicit Fe tetrahydrate, Mn tetrahydrate, Co hexahydrate, Cu dihydrate, Ni hexahydrate, Mo dihydrate, Se pentahydrate, W dihydrate, Mg hexahydrate, Ca dihydrate and sulfide nonahydrate agree with their maintained terms. HCl, phosphate, ammonium chloride, NaCl, bicarbonate, NaOH, boric acid, zinc chloride, glycerol and trisodium citrate match source precision. Generic maltose does not establish alpha-maltose specifically; seek anomer evidence without claiming a different anomer is required. Generic calcium pantothenate and lipoic acid do not establish a stereochemical contradiction; retain source precision. Yeast extract is complex. Resazurin is unqualified here, so do not import another medium’s sodium-salt finding.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007689.

66 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Scoped parent history versus selected quantity evidence

provenance: supported. Targets: CultureMech:007689.

Current primary/provider comparisons are independent of historical claims. The complete bound history inventory preserves each claim’s cited-hash and quotation status; none is promoted from excluded parent scope. Five October 5 inventory reports have zero source-checked claims and supply only derivative triage context. No raw authentication is inferred from those reports. Selected owners carry source/notes but no attached quantity evidence.

### Separate substrate variants and generated merge scope

identity: concern. Targets: CultureMech:007689.

The exact four maintained contributors contain two glycerol records, one citrate variant and one maltose variant. Current provider rows and JCM substrate branches do not support merging these into one glycerol-labelled formula. A common base may be represented separately with explicit variants, while duplicate glycerol identities require their own equivalence evidence. Source strain mentions identify substrate instructions, not automatic empirical growth assertions.

### Maintained preparation credit and generated loss

completeness: concern. Targets: CultureMech:007689.

All four owners already retain five preparation steps, valid global 121°C/15 min sterilization, filter-sterilized vitamins and bicarbonate, anaerobic gas ratio and pre-use sulfide addition. The generated target omits those arrays and retains ten Unknown solution placeholders. Do not call the maintained cycle invented or transfer parent-medium pH/sulfur/steam steps.

### Scoped stock dependency and receiving-owner distinction

grounding: concern. Targets: CultureMech:007689.

M180 trace solutions[1].composition[4] cobalt and [5] nickel retain CHEBI:35696/34887 anhydrous terms against explicit hexahydrates. The four receiving owners correctly use CHEBI:53503/53542. M180 batch-volume repairs and authenticated water/reagent claims are credited; unrelated M180 base and M190 minerals/sulfide remain excluded. M431 transfers only ingredients[27:30], with mixed water excluded.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007689.

78 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Distilled water",
    "stage": "Generated main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "930",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "930.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[9]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Distilled water                                        ",
          " 930.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 930,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives 930 ml water, not 930 g/L. Correct the volume dimension without claiming a final litre or using an assumed density."
  },
  {
    "decision_id": "q2",
    "name": "Yeast extract",
    "stage": "Generated main batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.1",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[7]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Yeast extract                                            ",
          " 0.1    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives a batch amount, not this final-volume rate. Preserve the printed amount and establish a denominator before normalization."
  },
  {
    "decision_id": "q3",
    "name": "NaCl",
    "stage": "Generated main batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.3",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " NaCl                                                     ",
          " 0.3    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives a batch amount, not this final-volume rate. Preserve the printed amount and establish a denominator before normalization."
  },
  {
    "decision_id": "q4",
    "name": "KH2PO4",
    "stage": "Generated main batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.41",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " KH2PO4 ",
          " 0.41   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.41,\n          \"unit\": \"g\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives a batch amount, not this final-volume rate. Preserve the printed amount and establish a denominator before normalization."
  },
  {
    "decision_id": "q5",
    "name": "NH4Cl",
    "stage": "Generated main batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.3",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " NH4Cl                                                 ",
          " 0.3    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives a batch amount, not this final-volume rate. Preserve the printed amount and establish a denominator before normalization."
  },
  {
    "decision_id": "q6",
    "name": "Resazurin",
    "stage": "Generated main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.5",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[8]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Resazurin                                                ",
          " 0.5    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives 0.5 mg resazurin, not 0.5 g. Correct the mass scale without assuming a final litre."
  },
  {
    "decision_id": "q7",
    "name": "Na2HPO4・2H2O",
    "stage": "Generated main batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.53",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Na2HPO4·2H2O                              ",
          " 0.53   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Na2HPO4・2H2O\",\n          \"volume\": 0.53,\n          \"unit\": \"g\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      }
    ],
    "interpretation": "The source gives a batch amount, not this final-volume rate. Preserve the printed amount and establish a denominator before normalization."
  },
  {
    "decision_id": "q8",
    "name": "Carbon dioxide gas",
    "stage": "Generated gas context",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_ratio_N2_CO2": "4:1 v/v",
      "absolute_gas_amount": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Base and dispensing paragraphs",
        "exact_source_quote": "(4:1, v/v) gas mixture",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "Absolute gas volume and flow are not specified. VARIABLE does not encode the explicit gas ratio; preserve the ratio in preparation without inventing a concentration."
  },
  {
    "decision_id": "q9",
    "name": "Nitrogen gas",
    "stage": "Generated gas context",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_ratio_N2_CO2": "4:1 v/v",
      "absolute_gas_amount": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Base and dispensing paragraphs",
        "exact_source_quote": "(4:1, v/v) gas mixture",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "Absolute gas volume and flow are not specified. VARIABLE does not encode the explicit gas ratio; preserve the ratio in preparation without inventing a concentration."
  },
  {
    "decision_id": "q10",
    "name": "Na2HPO4 x 2H2O",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.53",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Na2HPO4·2H2O                              ",
          " 0.53   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q11",
    "name": "KH2PO4",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.41",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " KH2PO4 ",
          " 0.41   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q12",
    "name": "NH4Cl",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.3",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " NH4Cl                                                 ",
          " 0.3    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q13",
    "name": "NaCl",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.3",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " NaCl                                                     ",
          " 0.3    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q14",
    "name": "Yeast extract",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.1",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[7]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Yeast extract                                            ",
          " 0.1    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q15",
    "name": "Resazurin",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.5",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[8]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Resazurin                                                ",
          " 0.5    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q16",
    "name": "Distilled water",
    "stage": "Four maintained main batches",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "930.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "930.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "930.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "930.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "930.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[9]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Distilled water                                        ",
          " 930.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "Maintained value and numerator unit match the printed amount, including corrected mg resazurin and ml water. The per-litre denominator remains unsupported: the source does not declare final or make-up volume. This is a basis gap, not proof the printed numerical mass is wrong. Attach evidence only after the basis is resolved."
  },
  {
    "decision_id": "q17",
    "name": "Carbon dioxide gas",
    "stage": "Four maintained gas entries",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_ratio_N2_CO2": "4:1 v/v",
      "absolute_amount": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Base and dispensing paragraphs",
        "exact_source_quote": "(4:1, v/v) gas mixture",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The maintained notes retain the ratio. No absolute gas amount or empirical growth observation is supplied."
  },
  {
    "decision_id": "q18",
    "name": "Nitrogen gas",
    "stage": "Four maintained gas entries",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_ratio_N2_CO2": "4:1 v/v",
      "absolute_amount": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Base and dispensing paragraphs",
        "exact_source_quote": "(4:1, v/v) gas mixture",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The maintained notes retain the ratio. No absolute gas amount or empirical growth observation is supplied."
  },
  {
    "decision_id": "q19",
    "name": "FeCl2 solution (see Medium [M180])",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " FeCl2 solution (see Medium No. 187)                 ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q20",
    "name": "Trace element solution (see Medium [M180])",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[5]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace element solution (see Medium No. 187)            ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q21",
    "name": "Selenite--tungstate solution (see Medium [M431])",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.5",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[6]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Selenite-tungstate solution (see Medium No. 431)      ",
          " 0.5    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q22",
    "name": "8% NaHCO3 solution*",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "50.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 8% NaHCO3 solution*                                 ",
          " 50.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q23",
    "name": "10% CaCl2・2H2O solution",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% CaCl2·2H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q24",
    "name": "10% MgCl2・6H2O solution",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% MgCl2·6H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q25",
    "name": "Trace vitamins (see Medium [M190])",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace vitamins* (see Medium No. 197)                  ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q26",
    "name": "Substrate solution (see below)",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Substrate solution (see below)                          ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q27",
    "name": "5% Na2S・9H2O solution",
    "stage": "Generated empty stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_dose_ml_per_litre": "10",
      "stock_label": "5% Na2S·9H2O",
      "percent_basis": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[2].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 5% Na2S·9H2O solution                      ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Pre-use sulfide paragraph",
        "exact_source_quote": "Prior to use, add per liter the following solution",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The listed ml addition was represented as G_PER_L. Restore the volume and named composition, preserving the source stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions are batch volumes. Do not transfer complete parent recipes."
  },
  {
    "decision_id": "q28",
    "name": "glycerin solution",
    "stage": "Generated duplicate substrate placeholder",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml",
        "field_path": "solutions[9].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "stock_strength": "1 M glycerin",
      "dose": "10 ml in the printed batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Substrate Solution",
        "exact_source_quote": "For strain JCM 30818, 1 M glycerin solution;",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Substrate solution (see below)                          ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "This empty VARIABLE placeholder duplicates the substrate addition without its molarity. Replace through the correct substrate branch; do not add it as a second independent dose."
  },
  {
    "decision_id": "q29",
    "name": "FeCl2 solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " FeCl2 solution (see Medium No. 187)                 ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q30",
    "name": "Trace element solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[5]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace element solution (see Medium No. 187)            ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q31",
    "name": "Selenite-tungstate solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.5",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[6]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Selenite-tungstate solution (see Medium No. 431)      ",
          " 0.5    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q32",
    "name": "10% MgCl2 x 6H2O solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% MgCl2·6H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q33",
    "name": "10% CaCl2 x 2H2O solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% CaCl2·2H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q34",
    "name": "Trace vitamins",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace vitamins* (see Medium No. 197)                  ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q35",
    "name": "8% NaHCO3 solution",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "50.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "50.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "50.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "50.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "50.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 8% NaHCO3 solution*                                 ",
          " 50.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q36",
    "name": "Variant-specific substrate stock",
    "stage": "Four maintained stock additions",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Substrate solution (see below)                          ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The owner correctly restores a volume numerator and stock identity, but a printed batch ml dose does not establish ML_PER_L. Preserve the actual batch dose until final-volume normalization is evidenced."
  },
  {
    "decision_id": "q37",
    "name": "5% Na2S x 9H2O solution",
    "stage": "Four maintained stock additions",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "ML_PER_L",
      "scope": "pre-use dose, expressly per litre"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[2].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 5% Na2S·9H2O solution                      ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Pre-use sulfide paragraph",
        "exact_source_quote": "Prior to use, add per liter the following solution",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The explicitly per-litre pre-use sulfide dose matches the stored value/unit but lacks attached evidence; percentage basis is separately unknown."
  },
  {
    "decision_id": "q38",
    "name": "HCl",
    "stage": "FeCl2 solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " 25% HCl (7.7 M)                                       ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q39",
    "name": "FeCl2 x 4H2O",
    "stage": "FeCl2 solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.5",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " FeCl2·4H2O                                  ",
          " 1.5    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q40",
    "name": "Distilled water",
    "stage": "FeCl2 solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "990.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "990.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "990.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "990.0",
          "unit": "ML_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "990.0",
      "printed_unit": "ml",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " Distilled water                                       ",
          " 990.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q41",
    "name": "ZnCl2",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "70.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "70.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "70.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "70.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "70.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[0]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " ZnCl2 ",
          " 70.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q42",
    "name": "MnCl2 x 4H2O",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "100.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "100.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "100.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "100.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "100.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[1]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " MnCl2·4H2O                                ",
          " 100.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q43",
    "name": "H3BO3",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "6.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[2]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " H3BO3 ",
          " 6.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q44",
    "name": "CoCl2 x 6H2O",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": {
          "value": "190.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": {
          "value": "190.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": {
          "value": "190.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": {
          "value": "190.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "190.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[3]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " CoCl2·6H2O                                ",
          " 190.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q45",
    "name": "CuCl2 x 2H2O",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[4]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " CuCl2·2H2O                                  ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q46",
    "name": "NiCl2 x 6H2O",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": {
          "value": "24.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": {
          "value": "24.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": {
          "value": "24.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": {
          "value": "24.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "24.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[5]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " NiCl2·6H2O                                 ",
          " 24.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q47",
    "name": "Na2MoO4 x 2H2O",
    "stage": "Trace element solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": {
          "value": "36.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": {
          "value": "36.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": {
          "value": "36.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": {
          "value": "36.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "36.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[6]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " Na2MoO4·2H2O                            ",
          " 36.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q48",
    "name": "Distilled water",
    "stage": "Trace element solution preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "L",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2].row[7]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L        "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The literal 1 L water input agrees with the stored L amount and lacks attached evidence. It does not declare final stock volume."
  },
  {
    "decision_id": "q49",
    "name": "NaOH",
    "stage": "Selenite-tungstate solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.4",
      "printed_unit": "g",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table[3].row[0]",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_source_cells": [
          " NaOH                                                    ",
          " 0.4    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q50",
    "name": "Na2SeO3 x 5H2O",
    "stage": "Selenite-tungstate solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[1].concentration",
        "stored": {
          "value": "6.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "6.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table[3].row[1]",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_source_cells": [
          " Na2SeO3·5H2O                             ",
          " 6.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q51",
    "name": "Na2WO4 x 2H2O",
    "stage": "Selenite-tungstate solution preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "8.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "8.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "8.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[2].concentration",
        "stored": {
          "value": "8.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "8.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table[3].row[2]",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_source_cells": [
          " Na2WO4·2H2O                              ",
          " 8.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q52",
    "name": "Distilled water",
    "stage": "Selenite-tungstate solution preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[2].composition[3].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "L",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table[3].row[3]",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_source_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L        "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The literal 1 L water input agrees with the stored L amount and lacks attached evidence. It does not declare final stock volume."
  },
  {
    "decision_id": "q53",
    "name": "Biotin",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[0].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[0].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[0].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[0].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Biotin                                                  ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q54",
    "name": "Folic acid",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[1].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[1].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[1].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[1].concentration",
        "stored": {
          "value": "2.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "2.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Folic acid                                              ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q55",
    "name": "Pyridoxine HCl",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[2].concentration",
        "stored": {
          "value": "10.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "10.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Pyridoxine·HCl                                   ",
          " 10.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q56",
    "name": "Thiamine HCl",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[3].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[3].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[3].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[3].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Thiamine·HCl                                      ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q57",
    "name": "Riboflavin",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[4].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[4]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Riboflavin                                              ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q58",
    "name": "Nicotinic acid",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[5]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Nicotinic acid                                          ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q59",
    "name": "Calcium pantothenate",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[6].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[6]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Calcium pantothenate                                    ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q60",
    "name": "Vitamin B12",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "0.1",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[7]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Vitamin B12 ",
          " 0.1    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q61",
    "name": "p-Aminobenzoic acid",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[8].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[8].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[8].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[8].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[8]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " p-Aminobenzoic acid                             ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q62",
    "name": "Lipoic acid",
    "stage": "Trace vitamins preparation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[9].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[9].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[9].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[9].concentration",
        "stored": {
          "value": "5.0",
          "unit": "MG_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "5.0",
      "printed_unit": "mg",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[9]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Lipoic acid                                             ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The numerical numerator matches this printed stock preparation amount, but listed water does not establish final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be conditional on a separately established stock volume."
  },
  {
    "decision_id": "q63",
    "name": "Distilled water",
    "stage": "Trace vitamins preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[10].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[10].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[10].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[5].composition[10].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": "1.0",
      "printed_unit": "L",
      "final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table[1].row[10]",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_source_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The literal 1 L water input agrees with the stored L amount and lacks attached evidence. It does not declare final stock volume."
  },
  {
    "decision_id": "q64",
    "name": "MgCl2 x 6H2O",
    "stage": "Unqualified percentage stock",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[3].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      }
    ],
    "desired": {
      "literal_stock_label": "10% MgCl2·6H2O solution",
      "percentage_basis": null,
      "structured_unit": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% MgCl2·6H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The source and provider print only %. PERCENT_W_V adds an unsupported mass/volume basis. Preserve the literal source text; no generic PERCENT enum exists, and do not derive delivered mass or silently select w/w, w/v or v/v."
  },
  {
    "decision_id": "q65",
    "name": "CaCl2 x 2H2O",
    "stage": "Unqualified percentage stock",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[4].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        }
      }
    ],
    "desired": {
      "literal_stock_label": "10% CaCl2·2H2O solution",
      "percentage_basis": null,
      "structured_unit": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% CaCl2·2H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The source and provider print only %. PERCENT_W_V adds an unsupported mass/volume basis. Preserve the literal source text; no generic PERCENT enum exists, and do not derive delivered mass or silently select w/w, w/v or v/v."
  },
  {
    "decision_id": "q66",
    "name": "NaHCO3",
    "stage": "Unqualified percentage stock",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].composition[0].concentration",
        "stored": {
          "value": "8.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].composition[0].concentration",
        "stored": {
          "value": "8.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].composition[0].concentration",
        "stored": {
          "value": "8.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[6].composition[0].concentration",
        "stored": {
          "value": "8.0",
          "unit": "PERCENT_W_V"
        }
      }
    ],
    "desired": {
      "literal_stock_label": "8% NaHCO3 solution*",
      "percentage_basis": null,
      "structured_unit": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 8% NaHCO3 solution*                                 ",
          " 50.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The source and provider print only %. PERCENT_W_V adds an unsupported mass/volume basis. Preserve the literal source text; no generic PERCENT enum exists, and do not derive delivered mass or silently select w/w, w/v or v/v."
  },
  {
    "decision_id": "q67",
    "name": "Na2S x 9H2O",
    "stage": "Unqualified percentage stock",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].composition[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].composition[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].composition[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[8].composition[0].concentration",
        "stored": {
          "value": "5.0",
          "unit": "PERCENT_W_V"
        }
      }
    ],
    "desired": {
      "literal_stock_label": "5% Na2S·9H2O solution",
      "percentage_basis": null,
      "structured_unit": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[2].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 5% Na2S·9H2O solution                      ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The source and provider print only %. PERCENT_W_V adds an unsupported mass/volume basis. Preserve the literal source text; no generic PERCENT enum exists, and do not derive delivered mass or silently select w/w, w/v or v/v."
  },
  {
    "decision_id": "q68",
    "name": "Substrate molarity",
    "stage": "Separate maintained substrate variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].composition[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "MOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].composition[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "MOLAR"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "MOLAR"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Substrate Solution",
        "exact_source_quote": "For strain JCM 30818, 1 M glycerin solution;",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      },
      {
        "source_key": "togoM1165",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"glycerin solution\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded"
      },
      {
        "source_key": "togoM1166",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1166",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"glycerin solution\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "1451dc904dc66b7c897bb01d224a8077cc624e5119ccd5f8474917ff01c6a8c2"
      }
    ],
    "interpretation": "The stock molarity is explicit and matches the local value/unit, but no attached quantity evidence is present. Keep glycerol, citrate and maltose separate. This does not verify final-medium molarity or transfer strain growth assertions. Maltose alpha specificity is assessed separately."
  },
  {
    "decision_id": "q69",
    "name": "Substrate molarity",
    "stage": "Separate maintained substrate variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].composition[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "MOLAR"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "MOLAR"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Substrate Solution",
        "exact_source_quote": "For strain JCM 31247, 1 M trisodium citrate solution;",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      },
      {
        "source_key": "togoM1167",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1167",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"trisodium citrate solution\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "01960fd3197481fac39bd4517bdf47c7459c1afbd5f965fabed8f2ac29aececc"
      }
    ],
    "interpretation": "The stock molarity is explicit and matches the local value/unit, but no attached quantity evidence is present. Keep glycerol, citrate and maltose separate. This does not verify final-medium molarity or transfer strain growth assertions. Maltose alpha specificity is assessed separately."
  },
  {
    "decision_id": "q70",
    "name": "Substrate molarity",
    "stage": "Separate maintained substrate variant",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[7].composition[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "MOLAR"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "MOLAR"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Substrate Solution",
        "exact_source_quote": "For strain JCM 31248, 1 M maltose solution;",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      },
      {
        "source_key": "togoM1168",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1168",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"maltose solution\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "e69bbcbf0e059c3c769bfb91a9f7bf5a8d2237c3a5eb0b13edcb85c7e4c3ded7"
      }
    ],
    "interpretation": "The stock molarity is explicit and matches the local value/unit, but no attached quantity evidence is present. Keep glycerol, citrate and maltose separate. This does not verify final-medium molarity or transfer strain growth assertions. Maltose alpha specificity is assessed separately."
  },
  {
    "decision_id": "q71",
    "name": "Global autoclave cycle",
    "stage": "Preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "temperature": {
            "value": 121.0,
            "unit": "CELSIUS"
          },
          "duration": "15 min",
          "notes": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "temperature": {
            "value": 121.0,
            "unit": "CELSIUS"
          },
          "duration": "15 min",
          "notes": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "temperature": {
            "value": 121.0,
            "unit": "CELSIUS"
          },
          "duration": "15 min",
          "notes": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "temperature": {
            "value": 121.0,
            "unit": "CELSIUS"
          },
          "duration": "15 min",
          "notes": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
        }
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Global header",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The global 121°C, 15 min instruction supports the maintained base sterilization cycle. The 50/120 ml vessel example is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored under nitrogen. No incubation temperature, pH or empirical growth rate is established by these instructions."
  },
  {
    "decision_id": "q72",
    "name": "Gas ratio",
    "stage": "Preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Base/dispensing paragraphs",
        "exact_source_quote": "(4:1, v/v) gas mixture",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The global 121°C, 15 min instruction supports the maintained base sterilization cycle. The 50/120 ml vessel example is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored under nitrogen. No incubation temperature, pH or empirical growth rate is established by these instructions."
  },
  {
    "decision_id": "q73",
    "name": "Example dispensing volumes",
    "stage": "Preparation",
    "decision": "add",
    "local_fields": [],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Dispensing example",
        "exact_source_quote": "50 ml of the medium in 120 ml serum bottle",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The global 121°C, 15 min instruction supports the maintained base sterilization cycle. The 50/120 ml vessel example is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored under nitrogen. No incubation temperature, pH or empirical growth rate is established by these instructions."
  },
  {
    "decision_id": "q74",
    "name": "Pre-use stock handling",
    "stage": "Preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored under N2."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored under N2."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored under N2."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored under N2."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Pre-use sulfide paragraph",
        "exact_source_quote": "autoclaved and stored under a N\n2\n atmosphere",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "The global 121°C, 15 min instruction supports the maintained base sterilization cycle. The 50/120 ml vessel example is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored under nitrogen. No incubation temperature, pH or empirical growth rate is established by these instructions."
  },
  {
    "decision_id": "q75",
    "name": "Fe stock acid strength",
    "stage": "FeCl2 stock only",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "JCM Medium 187 prepares the stock with 25% HCl (7.7 M)."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "JCM Medium 187 prepares the stock with 25% HCl (7.7 M)."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "JCM Medium 187 prepares the stock with 25% HCl (7.7 M)."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "JCM Medium 187 prepares the stock with 25% HCl (7.7 M)."
      }
    ],
    "desired": {
      "molarity": "7.7 M",
      "literal_percentage": "25%",
      "percentage_basis": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "decoded_source_cells": [
          " 25% HCl (7.7 M)                                       ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The source explicitly gives 25% HCl (7.7 M). Molarity is stated, percentage basis is not. This is the acid reagent used for this stock, not acid added directly to the main medium."
  },
  {
    "decision_id": "q76",
    "name": "Sterilization split and unquantified solvents",
    "stage": "Post-cooling stocks",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization.notes",
        "stored": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization.notes",
        "stored": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization.notes",
        "stored": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
        "field_path": "sterilization.notes",
        "stored": "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding after cooling."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Post-cooling paragraph",
        "exact_source_quote": "autoclaved or *filter-sterilized",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace vitamins* (see Medium No. 197)                  ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 8% NaHCO3 solution*                                 ",
          " 50.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "The starred vitamin and bicarbonate solutions are filter-sterilized. Other added solutions are autoclaved. Water or other solvent amounts for the percentage and molar stocks are not given; do not create water amounts. The base has no specified pH or cultivation temperature."
  },
  {
    "decision_id": "q77",
    "name": "Separate methanol option",
    "stage": "Excluded substrate branch",
    "decision": "not_quantified",
    "local_fields": [],
    "desired": {
      "source_only": "2 M methanol for JCM 35360"
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "Substrate Solution",
        "exact_source_quote": "For strain JCM 35360, 2 M methanol solution.",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "parsed_text_sha256": "ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6"
      }
    ],
    "interpretation": "This is a separate source option, not any of the four selected maintained substrate identities. Do not add it to the generated glycerol/citrate/maltose mixture or infer growth merely from a strain mention."
  },
  {
    "decision_id": "q78",
    "name": "Batch-volume arithmetic",
    "stage": "Basis limit",
    "decision": "not_quantified",
    "local_fields": [],
    "desired": {
      "sum_of_printed_initial_and_postcooling_volumes_ml": "1004.5",
      "measured_final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[9]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Distilled water                                        ",
          " 930.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " FeCl2 solution (see Medium No. 187)                 ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[5]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace element solution (see Medium No. 187)            ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[0].row[6]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Selenite-tungstate solution (see Medium No. 431)      ",
          " 0.5    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[0]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% MgCl2·6H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[1]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 10% CaCl2·2H2O solution                     ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[2]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Trace vitamins* (see Medium No. 197)                  ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[3]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " 8% NaHCO3 solution*                                 ",
          " 50.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      },
      {
        "source_key": "jcm1095",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095",
        "source_locator": "HTML table[1].row[4]",
        "snapshot_sha256": "a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca",
        "decoded_source_cells": [
          " Substrate solution (see below)                          ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cell text, independently re-extracted from bound raw HTML; not a literal raw quotation."
      }
    ],
    "interpretation": "930 + 1 + 1 + 0.5 + 1 + 1 + 10 + 50 + 10 = 1004.5 ml before the separately per-litre sulfide dose. This sum is conditional bookkeeping, not measured final volume. No receiving or stock denominator is silently set to 1 L."
  }
]

## Findings

### f1: Distinct substrate formulations are merged

blocker / open / confirmed; issue key: culturemech.007689.substrate-variant-conflation.

The generated target combines glycerol, citrate and maltose contributors as duplicate recipes. Their common base is not complete formulation equivalence.

### f2: Generated units and empty stock placeholders supersede maintained repairs

major / open / confirmed; issue key: culturemech.007689.stale-units-and-empty-stocks.

The target uses mass units for water and stock volumes, changes 0.5 mg resazurin to 0.5 g, and retains ten empty Unknown solution rows. Owners already restore correct numerator units, nine named stocks and substrate strengths.

### f3: Final-volume rates and w/v bases exceed printed source precision

major / open / provisional; issue key: culturemech.007689.unsupported-denominators-and-percent.

Owners append per-litre denominators to printed batch masses/doses and PERCENT_W_V to unqualified percentages. Listed water or arithmetic addition does not establish final volume. Only the pre-use sulfide dose explicitly says per litre; substrate molarity is separately explicit.

### f4: The generated phosphate term omits two waters

major / open / confirmed; issue key: culturemech.007689.phosphate-hydrate.

The target source name and primary row specify Na2HPO4·2H2O but the primary term is anhydrous CHEBI:34683. All maintained owners already use CHEBI:91258 dihydrate.

### f5: Maltose anomer and current secondary correspondence need evidence

major / open / provisional; issue key: culturemech.007689.maltose-correspondence.

Source generic maltose does not establish alpha specificity, and the selected owner secondary CHEBI:18167 lacks a current preferred MIM row. This is not proof that beta-maltose is required or that the historical link never existed.

### f6: Generated projection omits retained preparation

major / open / confirmed; issue key: culturemech.007689.generated-preparation-loss.

The target lacks the five maintained preparation steps and valid sterilization details, including staged filtration and anaerobic handling.

### f7: Supported molarities, water inputs and explicit dose lack attached evidence

minor / open / confirmed; issue key: culturemech.007689.claim-evidence-linkage.

Source and notes are present in owners, but claim-level evidence is absent. Evidence-only decisions are restricted to exact L water inputs, explicit molarity, per-litre sulfide dose and retained preparation; unsupported final-volume rates are not marked verified.

### f8: Transferred stock dependency retains two anhydrous mappings

major / open / confirmed; issue key: culturemech.007689.m180-dependency-hydrates.

Only the maintained M180 trace dependency still maps named cobalt and nickel hexahydrates to anhydrous concepts; receiving owners already repaired these forms.

## Recommended Actions And Acceptance Checks

### a1

Separate exact substrate variants and preserve both glycerol source identities until equivalence is evidenced; regenerate after maintained corrections.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Regenerate from the corrected maintained structure after preserving exact batch units and explicit stock scopes; do not reintroduce duplicated substrate or full parent formulas.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain printed batch quantities and literal percentage labels; establish denominator and percentage basis before deriving concentrations or delivered solute amounts. Preserve the explicitly per-litre sulfide dose and molar substrate strengths.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the corrected maintained dihydrate mapping during regeneration; do not change source mass by an unrequested molar conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Resolve source anomer precision and documented MIM correspondence at this exact maintained slot; do not guess a replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve the current supported preparation and collection references in a regenerated variant-aware projection.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a7

Attach short exact source rows and locators to supported claims after resolving the substantive basis/form issues.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a8

Correct these exact dependency slots with source-supported hydrates, preserving the separately correct receiving-owner slots and existing batch-quantity evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch043/427/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch043/427/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml:1:id: CultureMech:007689<br>./data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml:1:id: CultureMech:007689<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch043/source-preflight-bound/427/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 64 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| jcm1095 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095; Complete main recipe, global sterilization instruction and four separate substrate branches | supports | Read at the named scope. Parent basal media, unrelated stocks, pH and growth instructions do not transfer. Printed water quantities are not declarations of final stock volume. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; Only FeCl2 solution and trace element solution subsections | supports | Read at the named scope. Parent basal media, unrelated stocks, pH and growth instructions do not transfer. Printed water quantities are not declarations of final stock volume. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Only Trace vitamins subsection | supports | Read at the named scope. Parent basal media, unrelated stocks, pH and growth instructions do not transfer. Printed water quantities are not declarations of final stock volume. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Only Selenite-tungstate solution subsection | supports | Read at the named scope. Parent basal media, unrelated stocks, pH and growth instructions do not transfer. Printed water quantities are not declarations of final stock volume. |
| togoM1165 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165; All four components and preparation comments | supports | Provider rows preserve the individual glycerol/citrate/maltose branch. They corroborate batch amounts, unspecified percentage bases and explicit substrate molarity; they do not establish a final litre. |
| togoM1166 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1166; All four components and preparation comments | supports | Provider rows preserve the individual glycerol/citrate/maltose branch. They corroborate batch amounts, unspecified percentage bases and explicit substrate molarity; they do not establish a final litre. |
| togoM1167 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1167; All four components and preparation comments | supports | Provider rows preserve the individual glycerol/citrate/maltose branch. They corroborate batch amounts, unspecified percentage bases and explicit substrate molarity; they do not establish a final litre. |
| togoM1168 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1168; All four components and preparation comments | supports | Provider rows preserve the individual glycerol/citrate/maltose branch. They corroborate batch amounts, unspecified percentage bases and explicit substrate molarity; they do not establish a final litre. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:131361 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:15377 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:15940 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:15956 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:16494 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:16526 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:17015 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:176843 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:17754 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:17883 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:17997 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi18167 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:18167 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:26710 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:27470 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:30753 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:30961 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:31206 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:31345 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:32139 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:32145 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:33118 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:34683 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:49105 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:49976 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:53258 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:53503 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:53542 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:63036 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:63939 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:75213 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:76209 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:86158 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:86249 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:86318 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:86345 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:86368 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:8806 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS ID, label, obsolete status and scientific properties; source form assessed separately | supports | CHEBI:91258 has the asserted canonical label. Label validity does not establish a specific hydrate, anomer or source formulation. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete exact-key current index scan plus metadata | context_only | {"sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "matched_rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16526": [{"label": "Carbon dioxide gas", "match_type": "preferred_term", "identifier": "CHEBI:16526", "preferred_term": "Carbon dioxide gas", "ontology_id": "CHEBI:16526", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17997": [{"label": "Nitrogen gas", "match_type": "preferred_term", "identifier": "CHEBI:17997", "preferred_term": "Nitrogen gas", "ontology_id": "CHEBI:17997", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:18167": [], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53542": [{"label": "Nickel (II) chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53542", "preferred_term": "Nickel (II) chloride hexahydrate", "ontology_id": "CHEBI:53542", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "no_current_preferred_row": ["CHEBI:18167"]} |
| history-metadata | data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| scoped-history | /private/tmp/culturemech-review-work-batch043/427/scoped-history-inventory.json; All preserved parent evidence objects with exact transfer scope and authentication mode | context_only | Transferred sections are M180 Fe/trace, M190 vitamins and M431 Se/W only. The excluded M190 sulfide snippet cites recovered raw but is not a literal formatted match; it is not raw-unrecovered and is not transferred. Whole-parent recipes and mixed water are excluded. |
| writer-0 | scripts/repair_togo_m1165_m1168_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current repair signature guards and explicit units/stock builders are context. September maintained repair is credited; August generated projection is stale. Present guarded merger behavior is not asserted as historical execution proof. |
| writer-1 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current repair signature guards and explicit units/stock builders are context. September maintained repair is credited; August generated projection is stale. Present guarded merger behavior is not asserted as historical execution proof. |
| m180-dependency | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; Only solutions[0] Fe stock and solutions[1] trace stock; exact current bytes | context_only | This maintained dependency already withdraws unsupported per-litre masses and preserves batch water/dose evidence. Its trace cobalt and nickel terms remain anhydrous despite explicit hexahydrate names. Receiving M1165–M1168 owners use the correct hydrate terms; the dependency issue is not attributed to them. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact ontology formula and canonical label | supports | The anhydrous salt term differs from the source hexahydrate; receiving-owner hydrate terms are separately correct. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact ontology formula and canonical label | supports | The anhydrous salt term differs from the source hexahydrate; receiving-owner hydrate terms are separately correct. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch043/427/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Coverage is partial because selected M1168 maltose source specificity/current secondary correspondence and final-volume/percentage bases remain unresolved. No historical lineage is inferred from the current missing index key.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T003626Z-culturemech-007689-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bicarbonate_buffered_medium (CultureMech:007689)'
started_at: '2026-10-22T00:25:08Z'
finished_at: '2026-10-22T00:36:26Z'
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
summary: The generated record combines distinct glycerol, citrate and maltose substrate
  variants and retains obsolete empty stocks, volume-as-mass units, resazurin mg-as-g
  and an anhydrous phosphate mapping. September maintained-owner repairs already restore
  nine named stocks, correct main units/hydrate and preparation. Remaining owner concerns
  are unqualified percentages represented as w/v, unsupported final-volume denominators,
  source-specific maltose grounding and a current MIM correspondence gap. Preserve
  source stages and credit those repairs.
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
  - path: data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
    sha256: 455909be1adbc69ff6fe51ba0acacd514068277ac22eaa1456945003caa0db47
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    sha256: ca5dd6f4f5f6669444674390155416522096b78da655b3576ca65f64ca2115f5
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    sha256: a270da0237cf943052740e0ded84856fe93f15c51c2082160e0ecbde9c8dada8
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    sha256: 394a4ae54f395f2cdb578ff1038cb1e4f34ca879b9d7c50cdb753919501d8e61
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    sha256: c5c0c056ba9d6a908c45c0feebbfec0faccb8d51672e8f638bc96e207178b55c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.md
    sha256: 9985212f03200d875aeef2bfa98a0bdfdcbf0fdf168d07915500c701705ae150
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.md
    sha256: 1b32653a99d111b8ec69b05f834ace3807e019b3cc7723f2e0bf0bc4cd0d9f78
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.md
    sha256: 74dcdd0686079c0768b9304dc8dd66a54ea5e0dff4df3f344fb8eb37ee8f8d21
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.md
    sha256: 2dad9b0fb62d3c63e64205f772e9b7e1f436a409d53133fe7c4c2156c73a3ad5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.md
    sha256: b23f29fd1c779e5e0f78093f139755019822c7eb3cde67b351098dfcc547b4be
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
  - path: scripts/repair_togo_m1165_m1168_score15.py
    sha256: 08dae90131117e7eef89a6244202d750923bb60a00127669d14efe59f64d2f30
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
  selection: Task review 427; batch 043 item 7 of 10, selected in Python lexicographic
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
  - CultureMech:007689
targets:
- target_id: CultureMech:007689
  path: data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  label: bicarbonate_buffered_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/427/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/427/strict.tsv"
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007689
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
  - CultureMech:007689
- check_id: maltose-current-mim
  name: Current MIM secondary correspondence for selected M1168 maltose
  required: true
  status: unavailable
  summary: The exact pinned current index has no CHEBI:18167 preferred MAPPED row.
    Historical derivation and source anomer remain unresolved; no guessed mapping
    replacement.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - mim
  - chebi18167
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:55.501688Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch043/427/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:56.475592Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-043/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch043/427/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:57.572696Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T00:25:58.311196Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T00:36:25Z'
  support: supports
  summary: './data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml:1:id: CultureMech:007689

    ./data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml:1:id:
    CultureMech:007689

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/source-preflight-bound/427/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T00:36:25Z'
  support: supports
  summary: 64 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 06aa20a4a88fd71a3422e38c903f54b5e19782f7008f8eb22e36210398f453f8
- evidence_id: jcm1095
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095
  locator: Complete main recipe, global sterilization instruction and four separate
    substrate branches
  accessed_at: '2026-10-22T00:07:26.266169Z'
  support: supports
  summary: Read at the named scope. Parent basal media, unrelated stocks, pH and growth
    instructions do not transfer. Printed water quantities are not declarations of
    final stock volume.
  snapshot_sha256: a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: Only FeCl2 solution and trace element solution subsections
  accessed_at: '2026-10-21T10:33:40.897866Z'
  support: supports
  summary: Read at the named scope. Parent basal media, unrelated stocks, pH and growth
    instructions do not transfer. Printed water quantities are not declarations of
    final stock volume.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Only Trace vitamins subsection
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Read at the named scope. Parent basal media, unrelated stocks, pH and growth
    instructions do not transfer. Printed water quantities are not declarations of
    final stock volume.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Only Selenite-tungstate solution subsection
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Read at the named scope. Parent basal media, unrelated stocks, pH and growth
    instructions do not transfer. Printed water quantities are not declarations of
    final stock volume.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: togoM1165
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165
  locator: All four components and preparation comments
  accessed_at: '2026-10-22T00:07:25.321195Z'
  support: supports
  summary: Provider rows preserve the individual glycerol/citrate/maltose branch.
    They corroborate batch amounts, unspecified percentage bases and explicit substrate
    molarity; they do not establish a final litre.
  snapshot_sha256: af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded
- evidence_id: togoM1166
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1166
  locator: All four components and preparation comments
  accessed_at: '2026-10-22T00:07:25.321157Z'
  support: supports
  summary: Provider rows preserve the individual glycerol/citrate/maltose branch.
    They corroborate batch amounts, unspecified percentage bases and explicit substrate
    molarity; they do not establish a final litre.
  snapshot_sha256: 1451dc904dc66b7c897bb01d224a8077cc624e5119ccd5f8474917ff01c6a8c2
- evidence_id: togoM1167
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1167
  locator: All four components and preparation comments
  accessed_at: '2026-10-22T00:07:25.321314Z'
  support: supports
  summary: Provider rows preserve the individual glycerol/citrate/maltose branch.
    They corroborate batch amounts, unspecified percentage bases and explicit substrate
    molarity; they do not establish a final litre.
  snapshot_sha256: 01960fd3197481fac39bd4517bdf47c7459c1afbd5f965fabed8f2ac29aececc
- evidence_id: togoM1168
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1168
  locator: All four components and preparation comments
  accessed_at: '2026-10-22T00:07:25.321490Z'
  support: supports
  summary: Provider rows preserve the individual glycerol/citrate/maltose branch.
    They corroborate batch amounts, unspecified percentage bases and explicit substrate
    molarity; they do not establish a final litre.
  snapshot_sha256: e69bbcbf0e059c3c769bfb91a9f7bf5a8d2237c3a5eb0b13edcb85c7e4c3ded7
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 has the asserted canonical label. Label validity does not
    establish a specific hydrate, anomer or source formulation.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 has the asserted canonical label. Label validity does not
    establish a specific hydrate, anomer or source formulation.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:35.442871Z'
  support: supports
  summary: CHEBI:17754 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi18167
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:27.439061Z'
  support: supports
  summary: CHEBI:18167 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: e5f8ffe560badeedcb0ca1b3895a1cbb9913d56e11224fa91ffb77fa8a383199
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi53542
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T07:33:31.075912Z'
  support: supports
  summary: CHEBI:53542 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS ID, label, obsolete status and scientific properties; source
    form assessed separately
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: CHEBI:91258 has the asserted canonical label. Label validity does not establish
    a specific hydrate, anomer or source formulation.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete exact-key current index scan plus metadata
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: '{"sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "matched_rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water",
    "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956":
    [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:16526": [{"label": "Carbon dioxide gas", "match_type": "preferred_term",
    "identifier": "CHEBI:16526", "preferred_term": "Carbon dioxide gas", "ontology_id":
    "CHEBI:16526", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015":
    [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015",
    "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier":
    "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id":
    "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17997":
    [{"label": "Nitrogen gas", "match_type": "preferred_term", "identifier": "CHEBI:17997",
    "preferred_term": "Nitrogen gas", "ontology_id": "CHEBI:17997", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:18167": [], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label":
    "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label":
    "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345",
    "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145":
    [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145",
    "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label":
    "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258",
    "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53542": [{"label": "Nickel (II) chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53542", "preferred_term":
    "Nickel (II) chloride hexahydrate", "ontology_id": "CHEBI:53542", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806":
    [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term":
    "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, "no_current_preferred_row": ["CHEBI:18167"]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml;
    data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml;
    data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml",
    "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml",
    "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml",
    "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml",
    "events": 13, "timestamp_issues": []}]'
- evidence_id: scoped-history
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/427/scoped-history-inventory.json
  locator: All preserved parent evidence objects with exact transfer scope and authentication
    mode
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Transferred sections are M180 Fe/trace, M190 vitamins and M431 Se/W only.
    The excluded M190 sulfide snippet cites recovered raw but is not a literal formatted
    match; it is not raw-unrecovered and is not transferred. Whole-parent recipes
    and mixed water are excluded.
  snapshot_sha256: 89195b0de99c87bb0ce4b62895a10d4a165bffb8bdde7ea0a1a17c21d39c65cd
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_togo_m1165_m1168_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Current repair signature guards and explicit units/stock builders are context.
    September maintained repair is credited; August generated projection is stale.
    Present guarded merger behavior is not asserted as historical execution proof.
  snapshot_sha256: 08dae90131117e7eef89a6244202d750923bb60a00127669d14efe59f64d2f30
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Current repair signature guards and explicit units/stock builders are context.
    September maintained repair is credited; August generated projection is stale.
    Present guarded merger behavior is not asserted as historical execution proof.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: m180-dependency
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: Only solutions[0] Fe stock and solutions[1] trace stock; exact current
    bytes
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: This maintained dependency already withdraws unsupported per-litre masses
    and preserves batch water/dose evidence. Its trace cobalt and nickel terms remain
    anhydrous despite explicit hexahydrate names. Receiving M1165–M1168 owners use
    the correct hydrate terms; the dependency issue is not attributed to them.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact ontology formula and canonical label
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: The anhydrous salt term differs from the source hexahydrate; receiving-owner
    hydrate terms are separately correct.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact ontology formula and canonical label
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: The anhydrous salt term differs from the source hexahydrate; receiving-owner
    hydrate terms are separately correct.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch043/427/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T00:36:25Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 47bf2776f5c0a53659d931aab4d49594460609301bcc8773261654a27709f6c5
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All selected-layer ontology slots and current MIM correspondence
  outcome: concern
  summary: 38 distinct selected-layer IDs have exact nonobsolete OLS labels. Target
    has 8/9 primary links and 5/9 secondary links; optional missing links are not
    automatically errors. The M1168 alpha-maltose secondary key CHEBI:18167 has no
    exact current preferred MAPPED row in the pinned index. This current negative
    lookup does not establish historical provenance. All other asserted current secondary
    keys have exact preferred rows. Excluded-parent legacy001072 is outside this review
    transfer.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - record
  - mim
  - chebi131361
  - chebi15377
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi16526
  - chebi17015
  - chebi176843
  - chebi17754
  - chebi17883
  - chebi17997
  - chebi18167
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi32145
  - chebi33118
  - chebi34683
  - chebi49105
  - chebi49976
  - chebi53258
  - chebi53503
  - chebi53542
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91258
- assessment_id: forms
  area: grounding
  topic: Source forms and specificity
  outcome: concern
  summary: The generated Na2HPO4·2H2O is mapped to anhydrous CHEBI:34683; all four
    maintained owners correctly use dihydrate CHEBI:91258. Explicit Fe tetrahydrate,
    Mn tetrahydrate, Co hexahydrate, Cu dihydrate, Ni hexahydrate, Mo dihydrate, Se
    pentahydrate, W dihydrate, Mg hexahydrate, Ca dihydrate and sulfide nonahydrate
    agree with their maintained terms. HCl, phosphate, ammonium chloride, NaCl, bicarbonate,
    NaOH, boric acid, zinc chloride, glycerol and trisodium citrate match source precision.
    Generic maltose does not establish alpha-maltose specifically; seek anomer evidence
    without claiming a different anomer is required. Generic calcium pantothenate
    and lipoic acid do not establish a stereochemical contradiction; retain source
    precision. Yeast extract is complex. Resazurin is unqualified here, so do not
    import another medium’s sodium-salt finding.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - jcm1095
  - jcm187
  - jcm197
  - jcm431
  - chebi131361
  - chebi15377
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi16526
  - chebi17015
  - chebi176843
  - chebi17754
  - chebi17883
  - chebi17997
  - chebi18167
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi32145
  - chebi33118
  - chebi34683
  - chebi49105
  - chebi49976
  - chebi53258
  - chebi53503
  - chebi53542
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91258
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 66 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
  - owner-3
- assessment_id: history-source
  area: provenance
  topic: Scoped parent history versus selected quantity evidence
  outcome: supported
  summary: Current primary/provider comparisons are independent of historical claims.
    The complete bound history inventory preserves each claim’s cited-hash and quotation
    status; none is promoted from excluded parent scope. Five October 5 inventory
    reports have zero source-checked claims and supply only derivative triage context.
    No raw authentication is inferred from those reports. Selected owners carry source/notes
    but no attached quantity evidence.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - scoped-history
  - record
  - owner-0
  - owner-1
  - owner-2
  - owner-3
- assessment_id: identity
  area: identity
  topic: Separate substrate variants and generated merge scope
  outcome: concern
  summary: The exact four maintained contributors contain two glycerol records, one
    citrate variant and one maltose variant. Current provider rows and JCM substrate
    branches do not support merging these into one glycerol-labelled formula. A common
    base may be represented separately with explicit variants, while duplicate glycerol
    identities require their own equivalence evidence. Source strain mentions identify
    substrate instructions, not automatic empirical growth assertions.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - record
  - jcm1095
  - owner-0
  - owner-1
  - owner-2
  - owner-3
- assessment_id: preparation
  area: completeness
  topic: Maintained preparation credit and generated loss
  outcome: concern
  summary: All four owners already retain five preparation steps, valid global 121°C/15
    min sterilization, filter-sterilized vitamins and bicarbonate, anaerobic gas ratio
    and pre-use sulfide addition. The generated target omits those arrays and retains
    ten Unknown solution placeholders. Do not call the maintained cycle invented or
    transfer parent-medium pH/sulfur/steam steps.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - record
  - jcm1095
  - owner-0
  - owner-1
  - owner-2
  - owner-3
- assessment_id: dependency-forms
  area: grounding
  topic: Scoped stock dependency and receiving-owner distinction
  outcome: concern
  summary: M180 trace solutions[1].composition[4] cobalt and [5] nickel retain CHEBI:35696/34887
    anhydrous terms against explicit hexahydrates. The four receiving owners correctly
    use CHEBI:53503/53542. M180 batch-volume repairs and authenticated water/reagent
    claims are credited; unrelated M180 base and M190 minerals/sulfide remain excluded.
    M431 transfers only ingredients[27:30], with mixed water excluded.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - m180-dependency
  - jcm187
  - chebi35696
  - chebi34887
  - scoped-history
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 78 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007689
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Distilled water\"\
    ,\n    \"stage\": \"Generated main batch\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"930\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"930.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[9]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                         \",\n          \" 930.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 930,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\n      }\n\
    \    ],\n    \"interpretation\": \"The source gives 930 ml water, not 930 g/L.\
    \ Correct the volume dimension without claiming a final litre or using an assumed\
    \ density.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"name\": \"Yeast extract\"\
    ,\n    \"stage\": \"Generated main batch\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.1\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[7]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Yeast extract                 \
    \                           \",\n          \" 0.1    \",\n          \" g  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\n      }\n\
    \    ],\n    \"interpretation\": \"The source gives a batch amount, not this final-volume\
    \ rate. Preserve the printed amount and establish a denominator before normalization.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"NaCl\",\n    \"stage\"\
    : \"Generated main batch\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.3\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" NaCl                          \
    \                           \",\n          \" 0.3    \",\n          \" g  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 0.3,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives a batch amount,\
    \ not this final-volume rate. Preserve the printed amount and establish a denominator\
    \ before normalization.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\"\
    : \"KH2PO4\",\n    \"stage\": \"Generated main batch\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.41\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" KH2PO4 \",\n          \" 0.41   \"\
    ,\n          \" g  \"\n        ],\n        \"representation\": \"Exact decoded\
    \ DOM cell text, independently re-extracted from bound raw HTML; not a literal\
    \ raw quotation.\"\n      },\n      {\n        \"source_key\": \"togoM1165\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.41,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives a batch amount,\
    \ not this final-volume rate. Preserve the printed amount and establish a denominator\
    \ before normalization.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"name\"\
    : \"NH4Cl\",\n    \"stage\": \"Generated main batch\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.3\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[2]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" NH4Cl                         \
    \                        \",\n          \" 0.3    \",\n          \" g  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives a batch amount,\
    \ not this final-volume rate. Preserve the printed amount and establish a denominator\
    \ before normalization.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"name\"\
    : \"Resazurin\",\n    \"stage\": \"Generated main batch\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.5\"\
    ,\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[8]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Resazurin                     \
    \                           \",\n          \" 0.5    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives 0.5 mg resazurin,\
    \ not 0.5 g. Correct the mass scale without assuming a final litre.\"\n  },\n\
    \  {\n    \"decision_id\": \"q7\",\n    \"name\": \"Na2HPO4・2H2O\",\n    \"stage\"\
    : \"Generated main batch\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.53\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Na2HPO4·2H2O                  \
    \            \",\n          \" 0.53   \",\n          \" g  \"\n        ],\n  \
    \      \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      },\n      {\n   \
    \     \"source_key\": \"togoM1165\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2HPO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.53,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\n      }\n\
    \    ],\n    \"interpretation\": \"The source gives a batch amount, not this final-volume\
    \ rate. Preserve the printed amount and establish a denominator before normalization.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"Carbon dioxide gas\"\
    ,\n    \"stage\": \"Generated gas context\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_ratio_N2_CO2\": \"\
    4:1 v/v\",\n      \"absolute_gas_amount\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Base and dispensing paragraphs\",\n        \"exact_source_quote\": \"(4:1,\
    \ v/v) gas mixture\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"Absolute gas volume and flow are\
    \ not specified. VARIABLE does not encode the explicit gas ratio; preserve the\
    \ ratio in preparation without inventing a concentration.\"\n  },\n  {\n    \"\
    decision_id\": \"q9\",\n    \"name\": \"Nitrogen gas\",\n    \"stage\": \"Generated\
    \ gas context\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_ratio_N2_CO2\": \"\
    4:1 v/v\",\n      \"absolute_gas_amount\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Base and dispensing paragraphs\",\n        \"exact_source_quote\": \"(4:1,\
    \ v/v) gas mixture\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"Absolute gas volume and flow are\
    \ not specified. VARIABLE does not encode the explicit gas ratio; preserve the\
    \ ratio in preparation without inventing a concentration.\"\n  },\n  {\n    \"\
    decision_id\": \"q10\",\n    \"name\": \"Na2HPO4 x 2H2O\",\n    \"stage\": \"\
    Four maintained main batches\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.53\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Na2HPO4·2H2O                  \
    \            \",\n          \" 0.53   \",\n          \" g  \"\n        ],\n  \
    \      \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"Maintained value and numerator unit match the printed amount,\
    \ including corrected mg resazurin and ml water. The per-litre denominator remains\
    \ unsupported: the source does not declare final or make-up volume. This is a\
    \ basis gap, not proof the printed numerical mass is wrong. Attach evidence only\
    \ after the basis is resolved.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n \
    \   \"name\": \"KH2PO4\",\n    \"stage\": \"Four maintained main batches\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.41\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" KH2PO4 \",\n          \" 0.41   \"\
    ,\n          \" g  \"\n        ],\n        \"representation\": \"Exact decoded\
    \ DOM cell text, independently re-extracted from bound raw HTML; not a literal\
    \ raw quotation.\"\n      }\n    ],\n    \"interpretation\": \"Maintained value\
    \ and numerator unit match the printed amount, including corrected mg resazurin\
    \ and ml water. The per-litre denominator remains unsupported: the source does\
    \ not declare final or make-up volume. This is a basis gap, not proof the printed\
    \ numerical mass is wrong. Attach evidence only after the basis is resolved.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"name\": \"NH4Cl\",\n    \"stage\"\
    : \"Four maintained main batches\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.3\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[2]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" NH4Cl                         \
    \                        \",\n          \" 0.3    \",\n          \" g  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"Maintained value and numerator unit match the\
    \ printed amount, including corrected mg resazurin and ml water. The per-litre\
    \ denominator remains unsupported: the source does not declare final or make-up\
    \ volume. This is a basis gap, not proof the printed numerical mass is wrong.\
    \ Attach evidence only after the basis is resolved.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"NaCl\",\n    \"stage\": \"Four maintained main batches\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.3\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" NaCl                          \
    \                           \",\n          \" 0.3    \",\n          \" g  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"Maintained value and numerator unit match the\
    \ printed amount, including corrected mg resazurin and ml water. The per-litre\
    \ denominator remains unsupported: the source does not declare final or make-up\
    \ volume. This is a basis gap, not proof the printed numerical mass is wrong.\
    \ Attach evidence only after the basis is resolved.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Four maintained\
    \ main batches\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.1\"\
    ,\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"HTML table[0].row[7]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Yeast extract                 \
    \                           \",\n          \" 0.1    \",\n          \" g  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"Maintained value and numerator unit match the\
    \ printed amount, including corrected mg resazurin and ml water. The per-litre\
    \ denominator remains unsupported: the source does not declare final or make-up\
    \ volume. This is a basis gap, not proof the printed numerical mass is wrong.\
    \ Attach evidence only after the basis is resolved.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"name\": \"Resazurin\",\n    \"stage\": \"Four maintained main\
    \ batches\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.5\"\
    ,\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[8]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Resazurin                     \
    \                           \",\n          \" 0.5    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"Maintained value and numerator unit match the\
    \ printed amount, including corrected mg resazurin and ml water. The per-litre\
    \ denominator remains unsupported: the source does not declare final or make-up\
    \ volume. This is a basis gap, not proof the printed numerical mass is wrong.\
    \ Attach evidence only after the basis is resolved.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"Four maintained\
    \ main batches\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"930.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"930.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"930.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"930.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    930.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[9]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                         \",\n          \" 930.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"Maintained value and numerator unit match the\
    \ printed amount, including corrected mg resazurin and ml water. The per-litre\
    \ denominator remains unsupported: the source does not declare final or make-up\
    \ volume. This is a basis gap, not proof the printed numerical mass is wrong.\
    \ Attach evidence only after the basis is resolved.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Carbon dioxide gas\",\n    \"stage\": \"Four maintained\
    \ gas entries\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_ratio_N2_CO2\": \"\
    4:1 v/v\",\n      \"absolute_amount\": null\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Base and dispensing paragraphs\",\n        \"exact_source_quote\": \"(4:1,\
    \ v/v) gas mixture\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained notes retain the ratio.\
    \ No absolute gas amount or empirical growth observation is supplied.\"\n  },\n\
    \  {\n    \"decision_id\": \"q18\",\n    \"name\": \"Nitrogen gas\",\n    \"stage\"\
    : \"Four maintained gas entries\",\n    \"decision\": \"not_quantified\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_ratio_N2_CO2\": \"\
    4:1 v/v\",\n      \"absolute_amount\": null\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Base and dispensing paragraphs\",\n        \"exact_source_quote\": \"(4:1,\
    \ v/v) gas mixture\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained notes retain the ratio.\
    \ No absolute gas amount or empirical growth observation is supplied.\"\n  },\n\
    \  {\n    \"decision_id\": \"q19\",\n    \"name\": \"FeCl2 solution (see Medium\
    \ [M180])\",\n    \"stage\": \"Generated empty stock addition\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" FeCl2 solution (see Medium No.\
    \ 187)                 \",\n          \" 1.0    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q20\",\n    \"name\": \"Trace element solution (see Medium\
    \ [M180])\",\n    \"stage\": \"Generated empty stock addition\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[5]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace element solution (see Medium\
    \ No. 187)            \",\n          \" 1.0    \",\n          \" ml  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q21\",\n    \"name\": \"Selenite--tungstate solution (see\
    \ Medium [M431])\",\n    \"stage\": \"Generated empty stock addition\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"printed_batch_amount\": \"0.5\",\n      \"printed_unit\"\
    : \"ml\",\n      \"final_volume\": null\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[6]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Selenite-tungstate solution (see\
    \ Medium No. 431)      \",\n          \" 0.5    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q22\",\n    \"name\": \"8% NaHCO3 solution*\",\n    \"\
    stage\": \"Generated empty stock addition\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"50.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 8% NaHCO3 solution*           \
    \                      \",\n          \" 50.0    \",\n          \" ml  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q23\",\n    \"name\": \"10% CaCl2・2H2O solution\",\n  \
    \  \"stage\": \"Generated empty stock addition\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% CaCl2·2H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The listed ml addition was represented as G_PER_L. Restore\
    \ the volume and named composition, preserving the source stage. Only the pre-use\
    \ sulfide paragraph explicitly supplies a per-litre dose; other additions are\
    \ batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n    \"\
    decision_id\": \"q24\",\n    \"name\": \"10% MgCl2・6H2O solution\",\n    \"stage\"\
    : \"Generated empty stock addition\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% MgCl2·6H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The listed ml addition was represented as G_PER_L. Restore\
    \ the volume and named composition, preserving the source stage. Only the pre-use\
    \ sulfide paragraph explicitly supplies a per-litre dose; other additions are\
    \ batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n    \"\
    decision_id\": \"q25\",\n    \"name\": \"Trace vitamins (see Medium [M190])\"\
    ,\n    \"stage\": \"Generated empty stock addition\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"10.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[2]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace vitamins* (see Medium No.\
    \ 197)                  \",\n          \" 10.0    \",\n          \" ml  \"\n \
    \       ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q26\",\n    \"name\": \"Substrate solution (see below)\"\
    ,\n    \"stage\": \"Generated empty stock addition\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"10.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Substrate solution (see below)\
    \                          \",\n          \" 10.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The listed ml addition was represented as G_PER_L.\
    \ Restore the volume and named composition, preserving the source stage. Only\
    \ the pre-use sulfide paragraph explicitly supplies a per-litre dose; other additions\
    \ are batch volumes. Do not transfer complete parent recipes.\"\n  },\n  {\n \
    \   \"decision_id\": \"q27\",\n    \"name\": \"5% Na2S・9H2O solution\",\n    \"\
    stage\": \"Generated empty stock addition\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_dose_ml_per_litre\": \"10\"\
    ,\n      \"stock_label\": \"5% Na2S·9H2O\",\n      \"percent_basis\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[2].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 5% Na2S·9H2O solution         \
    \             \",\n          \" 10.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      },\n      {\n   \
    \     \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Pre-use sulfide paragraph\",\n        \"exact_source_quote\"\
    : \"Prior to use, add per liter the following solution\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The listed ml addition was represented\
    \ as G_PER_L. Restore the volume and named composition, preserving the source\
    \ stage. Only the pre-use sulfide paragraph explicitly supplies a per-litre dose;\
    \ other additions are batch volumes. Do not transfer complete parent recipes.\"\
    \n  },\n  {\n    \"decision_id\": \"q28\",\n    \"name\": \"glycerin solution\"\
    ,\n    \"stage\": \"Generated duplicate substrate placeholder\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"stock_strength\": \"1 M\
    \ glycerin\",\n      \"dose\": \"10 ml in the printed batch\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n \
    \       \"source_locator\": \"Substrate Solution\",\n        \"exact_source_quote\"\
    : \"For strain JCM 30818, 1 M glycerin solution;\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      },\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"HTML table[1].row[4]\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"decoded_source_cells\": [\n          \" Substrate solution (see below)\
    \                          \",\n          \" 10.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"This empty VARIABLE placeholder duplicates\
    \ the substrate addition without its molarity. Replace through the correct substrate\
    \ branch; do not add it as a second independent dose.\"\n  },\n  {\n    \"decision_id\"\
    : \"q29\",\n    \"name\": \"FeCl2 solution\",\n    \"stage\": \"Four maintained\
    \ stock additions\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" FeCl2 solution (see Medium No.\
    \ 187)                 \",\n          \" 1.0    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q30\",\n    \"name\": \"Trace element solution\"\
    ,\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[5]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace element solution (see Medium\
    \ No. 187)            \",\n          \" 1.0    \",\n          \" ml  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q31\",\n    \"name\": \"Selenite-tungstate\
    \ solution\",\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"0.5\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[6]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Selenite-tungstate solution (see\
    \ Medium No. 431)      \",\n          \" 0.5    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q32\",\n    \"name\": \"10% MgCl2 x 6H2O solution\"\
    ,\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% MgCl2·6H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The owner correctly restores a volume numerator and stock\
    \ identity, but a printed batch ml dose does not establish ML_PER_L. Preserve\
    \ the actual batch dose until final-volume normalization is evidenced.\"\n  },\n\
    \  {\n    \"decision_id\": \"q33\",\n    \"name\": \"10% CaCl2 x 2H2O solution\"\
    ,\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"1.0\"\
    ,\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% CaCl2·2H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The owner correctly restores a volume numerator and stock\
    \ identity, but a printed batch ml dose does not establish ML_PER_L. Preserve\
    \ the actual batch dose until final-volume normalization is evidenced.\"\n  },\n\
    \  {\n    \"decision_id\": \"q34\",\n    \"name\": \"Trace vitamins\",\n    \"\
    stage\": \"Four maintained stock additions\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    10.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[2]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace vitamins* (see Medium No.\
    \ 197)                  \",\n          \" 10.0    \",\n          \" ml  \"\n \
    \       ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q35\",\n    \"name\": \"8% NaHCO3 solution\"\
    ,\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    50.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 8% NaHCO3 solution*           \
    \                      \",\n          \" 50.0    \",\n          \" ml  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q36\",\n    \"name\": \"Variant-specific substrate\
    \ stock\",\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": \"\
    10.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Substrate solution (see below)\
    \                          \",\n          \" 10.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The owner correctly restores a volume numerator\
    \ and stock identity, but a printed batch ml dose does not establish ML_PER_L.\
    \ Preserve the actual batch dose until final-volume normalization is evidenced.\"\
    \n  },\n  {\n    \"decision_id\": \"q37\",\n    \"name\": \"5% Na2S x 9H2O solution\"\
    ,\n    \"stage\": \"Four maintained stock additions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"\
    unit\": \"ML_PER_L\",\n      \"scope\": \"pre-use dose, expressly per litre\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1095\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[2].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 5% Na2S·9H2O solution         \
    \             \",\n          \" 10.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      },\n      {\n   \
    \     \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Pre-use sulfide paragraph\",\n        \"exact_source_quote\"\
    : \"Prior to use, add per liter the following solution\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The explicitly per-litre pre-use\
    \ sulfide dose matches the stored value/unit but lacks attached evidence; percentage\
    \ basis is separately unknown.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n \
    \   \"name\": \"HCl\",\n    \"stage\": \"FeCl2 solution preparation\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"ML_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"10.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" 25% HCl (7.7 M)               \
    \                        \",\n          \" 10.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"name\": \"\
    FeCl2 x 4H2O\",\n    \"stage\": \"FeCl2 solution preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.5\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" FeCl2·4H2O                    \
    \              \",\n          \" 1.5    \",\n          \" g  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"FeCl2 solution preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"990.0\",\n          \"unit\": \"\
    ML_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"990.0\",\n          \"unit\": \"\
    ML_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"990.0\",\n          \"unit\": \"\
    ML_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"990.0\",\n          \"unit\": \"\
    ML_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"990.0\",\n      \"printed_unit\": \"ml\",\n      \"final_volume\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1].row[2]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                        \",\n          \" 990.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"name\": \"\
    ZnCl2\",\n    \"stage\": \"Trace element solution preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"70.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"70.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"70.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"70.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"70.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[0]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" ZnCl2 \",\n          \" 70.0    \"\
    ,\n          \" mg  \"\n        ],\n        \"representation\": \"Exact decoded\
    \ DOM cell text, independently re-extracted from bound raw HTML; not a literal\
    \ raw quotation.\"\n      }\n    ],\n    \"interpretation\": \"The numerical numerator\
    \ matches this printed stock preparation amount, but listed water does not establish\
    \ final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L\
    \ or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be\
    \ conditional on a separately established stock volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q42\",\n    \"name\": \"MnCl2 x 4H2O\",\n    \"stage\": \"Trace element solution\
    \ preparation\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"100.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"100.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"100.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"100.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"100.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[1]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" MnCl2·4H2O                    \
    \            \",\n          \" 100.0    \",\n          \" mg  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q43\",\n    \"name\": \"\
    H3BO3\",\n    \"stage\": \"Trace element solution preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"6.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[2]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" H3BO3 \",\n          \" 6.0    \"\
    ,\n          \" mg  \"\n        ],\n        \"representation\": \"Exact decoded\
    \ DOM cell text, independently re-extracted from bound raw HTML; not a literal\
    \ raw quotation.\"\n      }\n    ],\n    \"interpretation\": \"The numerical numerator\
    \ matches this printed stock preparation amount, but listed water does not establish\
    \ final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L\
    \ or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be\
    \ conditional on a separately established stock volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q44\",\n    \"name\": \"CoCl2 x 6H2O\",\n    \"stage\": \"Trace element solution\
    \ preparation\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"190.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"190.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"190.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"190.0\",\n          \"unit\": \"\
    MG_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"190.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[3]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" CoCl2·6H2O                    \
    \            \",\n          \" 190.0    \",\n          \" mg  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q45\",\n    \"name\": \"\
    CuCl2 x 2H2O\",\n    \"stage\": \"Trace element solution preparation\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"2.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[4]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" CuCl2·2H2O                    \
    \              \",\n          \" 2.0    \",\n          \" mg  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q46\",\n    \"name\": \"\
    NiCl2 x 6H2O\",\n    \"stage\": \"Trace element solution preparation\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"24.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"24.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"24.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"24.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"24.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[5]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" NiCl2·6H2O                    \
    \             \",\n          \" 24.0    \",\n          \" mg  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q47\",\n    \"name\": \"\
    Na2MoO4 x 2H2O\",\n    \"stage\": \"Trace element solution preparation\",\n  \
    \  \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"36.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"36.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"36.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"36.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"36.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[6]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" Na2MoO4·2H2O                  \
    \          \",\n          \" 36.0    \",\n          \" mg  \"\n        ],\n  \
    \      \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q48\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Trace element solution preparation\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.0\",\n      \"printed_unit\": \"L\",\n      \"final_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2].row[7]\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                          \",\n          \" 1.0    \",\n          \" L      \
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cell text,\
    \ independently re-extracted from bound raw HTML; not a literal raw quotation.\"\
    \n      }\n    ],\n    \"interpretation\": \"The literal 1 L water input agrees\
    \ with the stored L amount and lacks attached evidence. It does not declare final\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q49\",\n    \"name\": \"\
    NaOH\",\n    \"stage\": \"Selenite-tungstate solution preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"0.4\",\n      \"printed_unit\": \"g\",\n      \"final_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table[3].row[0]\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"decoded_source_cells\": [\n          \" NaOH                          \
    \                          \",\n          \" 0.4    \",\n          \" g  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q50\",\n    \"name\": \"\
    Na2SeO3 x 5H2O\",\n    \"stage\": \"Selenite-tungstate solution preparation\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"6.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"6.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table[3].row[1]\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"decoded_source_cells\": [\n          \" Na2SeO3·5H2O                  \
    \           \",\n          \" 6.0    \",\n          \" mg  \"\n        ],\n  \
    \      \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q51\",\n    \"name\": \"\
    Na2WO4 x 2H2O\",\n    \"stage\": \"Selenite-tungstate solution preparation\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"8.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table[3].row[2]\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"decoded_source_cells\": [\n          \" Na2WO4·2H2O                   \
    \           \",\n          \" 8.0    \",\n          \" mg  \"\n        ],\n  \
    \      \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The numerical numerator matches this printed stock preparation\
    \ amount, but listed water does not establish final stock volume. Retain batch\
    \ g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Selenite-tungstate solution preparation\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.0\",\n      \"printed_unit\": \"L\",\n      \"final_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table[3].row[3]\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                          \",\n          \" 1.0    \",\n          \" L      \
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cell text,\
    \ independently re-extracted from bound raw HTML; not a literal raw quotation.\"\
    \n      }\n    ],\n    \"interpretation\": \"The literal 1 L water input agrees\
    \ with the stored L amount and lacks attached evidence. It does not declare final\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q53\",\n    \"name\": \"\
    Biotin\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"2.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Biotin                        \
    \                          \",\n          \" 2.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n    \"name\": \"\
    Folic acid\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"2.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Folic acid                    \
    \                          \",\n          \" 2.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q55\",\n    \"name\": \"\
    Pyridoxine HCl\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"10.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[2]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Pyridoxine·HCl                \
    \                   \",\n          \" 10.0    \",\n          \" mg  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"name\": \"\
    Thiamine HCl\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Thiamine·HCl                  \
    \                    \",\n          \" 5.0    \",\n          \" mg  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q57\",\n    \"name\": \"\
    Riboflavin\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[4].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[4]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Riboflavin                    \
    \                          \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n    \"name\": \"\
    Nicotinic acid\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[5]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Nicotinic acid                \
    \                          \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q59\",\n    \"name\": \"\
    Calcium pantothenate\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[6].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[6]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Calcium pantothenate          \
    \                          \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q60\",\n    \"name\": \"\
    Vitamin B12\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[7].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"0.1\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[7]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Vitamin B12 \",\n          \" 0.1    \"\
    ,\n          \" mg  \"\n        ],\n        \"representation\": \"Exact decoded\
    \ DOM cell text, independently re-extracted from bound raw HTML; not a literal\
    \ raw quotation.\"\n      }\n    ],\n    \"interpretation\": \"The numerical numerator\
    \ matches this printed stock preparation amount, but listed water does not establish\
    \ final stock volume. Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L\
    \ or ML_PER_L as source-verified. Any dose-to-delivered-mass arithmetic must be\
    \ conditional on a separately established stock volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q61\",\n    \"name\": \"p-Aminobenzoic acid\",\n    \"stage\": \"Trace vitamins\
    \ preparation\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[8].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[8].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[8].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[8].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[8]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" p-Aminobenzoic acid           \
    \                  \",\n          \" 5.0    \",\n          \" mg  \"\n       \
    \ ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q62\",\n    \"name\": \"\
    Lipoic acid\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[9].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[9].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[9].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[9].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"MG_PER_L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"5.0\",\n      \"printed_unit\": \"mg\",\n      \"final_volume\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[9]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Lipoic acid                   \
    \                          \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The numerical numerator matches this printed\
    \ stock preparation amount, but listed water does not establish final stock volume.\
    \ Retain batch g/mg/ml rather than treating G_PER_L, MG_PER_L or ML_PER_L as source-verified.\
    \ Any dose-to-delivered-mass arithmetic must be conditional on a separately established\
    \ stock volume.\"\n  },\n  {\n    \"decision_id\": \"q63\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Trace vitamins preparation\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[5].composition[10].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[10].concentration\",\n \
    \       \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[10].concentration\",\n \
    \       \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition[10].concentration\",\n \
    \       \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\"\
    : \"1.0\",\n      \"printed_unit\": \"L\",\n      \"final_volume\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table[1].row[10]\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                          \",\n          \" 1.0    \",\n          \" L  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The literal 1 L water input agrees with the\
    \ stored L amount and lacks attached evidence. It does not declare final stock\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q64\",\n    \"name\": \"MgCl2 x\
    \ 6H2O\",\n    \"stage\": \"Unqualified percentage stock\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"literal_stock_label\"\
    : \"10% MgCl2·6H2O solution\",\n      \"percentage_basis\": null,\n      \"structured_unit\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% MgCl2·6H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The source and provider print only %. PERCENT_W_V adds an\
    \ unsupported mass/volume basis. Preserve the literal source text; no generic\
    \ PERCENT enum exists, and do not derive delivered mass or silently select w/w,\
    \ w/v or v/v.\"\n  },\n  {\n    \"decision_id\": \"q65\",\n    \"name\": \"CaCl2\
    \ x 2H2O\",\n    \"stage\": \"Unqualified percentage stock\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"literal_stock_label\"\
    : \"10% CaCl2·2H2O solution\",\n      \"percentage_basis\": null,\n      \"structured_unit\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% CaCl2·2H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The source and provider print only %. PERCENT_W_V adds an\
    \ unsupported mass/volume basis. Preserve the literal source text; no generic\
    \ PERCENT enum exists, and do not derive delivered mass or silently select w/w,\
    \ w/v or v/v.\"\n  },\n  {\n    \"decision_id\": \"q66\",\n    \"name\": \"NaHCO3\"\
    ,\n    \"stage\": \"Unqualified percentage stock\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"8.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"literal_stock_label\"\
    : \"8% NaHCO3 solution*\",\n      \"percentage_basis\": null,\n      \"structured_unit\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 8% NaHCO3 solution*           \
    \                      \",\n          \" 50.0    \",\n          \" ml  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The source and provider print only %. PERCENT_W_V\
    \ adds an unsupported mass/volume basis. Preserve the literal source text; no\
    \ generic PERCENT enum exists, and do not derive delivered mass or silently select\
    \ w/w, w/v or v/v.\"\n  },\n  {\n    \"decision_id\": \"q67\",\n    \"name\":\
    \ \"Na2S x 9H2O\",\n    \"stage\": \"Unqualified percentage stock\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"literal_stock_label\"\
    : \"5% Na2S·9H2O solution\",\n      \"percentage_basis\": null,\n      \"structured_unit\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[2].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 5% Na2S·9H2O solution         \
    \             \",\n          \" 10.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      }\n    ],\n    \"\
    interpretation\": \"The source and provider print only %. PERCENT_W_V adds an\
    \ unsupported mass/volume basis. Preserve the literal source text; no generic\
    \ PERCENT enum exists, and do not derive delivered mass or silently select w/w,\
    \ w/v or v/v.\"\n  },\n  {\n    \"decision_id\": \"q68\",\n    \"name\": \"Substrate\
    \ molarity\",\n    \"stage\": \"Separate maintained substrate variant\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"MOLAR\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"MOLAR\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n  \
    \    \"unit\": \"MOLAR\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Substrate Solution\",\n        \"exact_source_quote\"\
    : \"For strain JCM 30818, 1 M glycerin solution;\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      },\n      {\n        \"source_key\": \"togoM1165\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1165\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"glycerin solution\\\",\\n          \\\"conc_value\\\
    \": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"af0c9fc4ed26725659f4832cae8c9bf8c36d514b4241b6c0b889d2ec0c173ded\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1166\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1166\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"glycerin solution\\\",\\n          \\\"conc_value\\\
    \": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"1451dc904dc66b7c897bb01d224a8077cc624e5119ccd5f8474917ff01c6a8c2\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stock molarity is explicit and matches\
    \ the local value/unit, but no attached quantity evidence is present. Keep glycerol,\
    \ citrate and maltose separate. This does not verify final-medium molarity or\
    \ transfer strain growth assertions. Maltose alpha specificity is assessed separately.\"\
    \n  },\n  {\n    \"decision_id\": \"q69\",\n    \"name\": \"Substrate molarity\"\
    ,\n    \"stage\": \"Separate maintained substrate variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[7].composition[0].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"MOLAR\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n  \
    \    \"unit\": \"MOLAR\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Substrate Solution\",\n        \"exact_source_quote\"\
    : \"For strain JCM 31247, 1 M trisodium citrate solution;\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      },\n      {\n        \"source_key\": \"togoM1167\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1167\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"trisodium citrate solution\\\",\\n          \\\
    \"conc_value\\\": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"01960fd3197481fac39bd4517bdf47c7459c1afbd5f965fabed8f2ac29aececc\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stock molarity is explicit and matches\
    \ the local value/unit, but no attached quantity evidence is present. Keep glycerol,\
    \ citrate and maltose separate. This does not verify final-medium molarity or\
    \ transfer strain growth assertions. Maltose alpha specificity is assessed separately.\"\
    \n  },\n  {\n    \"decision_id\": \"q70\",\n    \"name\": \"Substrate molarity\"\
    ,\n    \"stage\": \"Separate maintained substrate variant\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[7].composition[0].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"1.0\",\n          \"unit\": \"MOLAR\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n  \
    \    \"unit\": \"MOLAR\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Substrate Solution\",\n        \"exact_source_quote\"\
    : \"For strain JCM 31248, 1 M maltose solution;\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      },\n      {\n        \"source_key\": \"togoM1168\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1168\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"maltose solution\\\",\\n          \\\"conc_value\\\
    \": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"e69bbcbf0e059c3c769bfb91a9f7bf5a8d2237c3a5eb0b13edcb85c7e4c3ded7\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stock molarity is explicit and matches\
    \ the local value/unit, but no attached quantity evidence is present. Keep glycerol,\
    \ citrate and maltose separate. This does not verify final-medium molarity or\
    \ transfer strain growth assertions. Maltose alpha specificity is assessed separately.\"\
    \n  },\n  {\n    \"decision_id\": \"q71\",\n    \"name\": \"Global autoclave cycle\"\
    ,\n    \"stage\": \"Preparation\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"temperature\": {\n            \"value\"\
    : 121.0,\n            \"unit\": \"CELSIUS\"\n          },\n          \"duration\"\
    : \"15 min\",\n          \"notes\": \"Autoclave the base under N2-CO2; filter-sterilize\
    \ Trace vitamins and NaHCO3 before adding after cooling.\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"temperature\": {\n            \"value\"\
    : 121.0,\n            \"unit\": \"CELSIUS\"\n          },\n          \"duration\"\
    : \"15 min\",\n          \"notes\": \"Autoclave the base under N2-CO2; filter-sterilize\
    \ Trace vitamins and NaHCO3 before adding after cooling.\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"temperature\": {\n            \"value\"\
    : 121.0,\n            \"unit\": \"CELSIUS\"\n          },\n          \"duration\"\
    : \"15 min\",\n          \"notes\": \"Autoclave the base under N2-CO2; filter-sterilize\
    \ Trace vitamins and NaHCO3 before adding after cooling.\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"temperature\": {\n            \"value\"\
    : 121.0,\n            \"unit\": \"CELSIUS\"\n          },\n          \"duration\"\
    : \"15 min\",\n          \"notes\": \"Autoclave the base under N2-CO2; filter-sterilize\
    \ Trace vitamins and NaHCO3 before adding after cooling.\"\n        }\n      }\n\
    \    ],\n    \"desired\": null,\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Global header\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The global 121°C, 15 min instruction\
    \ supports the maintained base sterilization cycle. The 50/120 ml vessel example\
    \ is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored\
    \ under nitrogen. No incubation temperature, pH or empirical growth rate is established\
    \ by these instructions.\"\n  },\n  {\n    \"decision_id\": \"q72\",\n    \"name\"\
    : \"Gas ratio\",\n    \"stage\": \"Preparation\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.\"\n    \
    \  }\n    ],\n    \"desired\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Base/dispensing paragraphs\",\n        \"exact_source_quote\"\
    : \"(4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The global 121°C, 15 min instruction\
    \ supports the maintained base sterilization cycle. The 50/120 ml vessel example\
    \ is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored\
    \ under nitrogen. No incubation temperature, pH or empirical growth rate is established\
    \ by these instructions.\"\n  },\n  {\n    \"decision_id\": \"q73\",\n    \"name\"\
    : \"Example dispensing volumes\",\n    \"stage\": \"Preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [],\n    \"desired\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Dispensing example\",\n        \"exact_source_quote\": \"50 ml of the medium\
    \ in 120 ml serum bottle\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The global 121°C, 15 min instruction\
    \ supports the maintained base sterilization cycle. The 50/120 ml vessel example\
    \ is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored\
    \ under nitrogen. No incubation temperature, pH or empirical growth rate is established\
    \ by these instructions.\"\n  },\n  {\n    \"decision_id\": \"q74\",\n    \"name\"\
    : \"Pre-use stock handling\",\n    \"stage\": \"Preparation\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : \"Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored\
    \ under N2.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : \"Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored\
    \ under N2.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : \"Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored\
    \ under N2.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : \"Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved and stored\
    \ under N2.\"\n      }\n    ],\n    \"desired\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Pre-use sulfide paragraph\",\n        \"exact_source_quote\": \"autoclaved\
    \ and stored under a N\\n2\\n atmosphere\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"The global 121°C, 15 min instruction\
    \ supports the maintained base sterilization cycle. The 50/120 ml vessel example\
    \ is not final batch volume. Gas ratio is explicitly v/v; pre-use sulfide is stored\
    \ under nitrogen. No incubation temperature, pH or empirical growth rate is established\
    \ by these instructions.\"\n  },\n  {\n    \"decision_id\": \"q75\",\n    \"name\"\
    : \"Fe stock acid strength\",\n    \"stage\": \"FeCl2 stock only\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"JCM Medium 187 prepares the stock with 25% HCl (7.7 M).\"\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"JCM Medium 187 prepares the stock with 25% HCl (7.7 M).\"\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"JCM Medium 187 prepares the stock with 25% HCl (7.7 M).\"\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"JCM Medium 187 prepares the stock with 25% HCl (7.7 M).\"\n      }\n    ],\n\
    \    \"desired\": {\n      \"molarity\": \"7.7 M\",\n      \"literal_percentage\"\
    : \"25%\",\n      \"percentage_basis\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm187\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\",\n        \"source_locator\"\
    : \"HTML table[1].row[0]\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"decoded_source_cells\": [\n          \" 25% HCl (7.7 M)         \
    \                              \",\n          \" 10.0    \",\n          \" ml\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cell text,\
    \ independently re-extracted from bound raw HTML; not a literal raw quotation.\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly gives 25% HCl\
    \ (7.7 M). Molarity is stated, percentage basis is not. This is the acid reagent\
    \ used for this stock, not acid added directly to the main medium.\"\n  },\n \
    \ {\n    \"decision_id\": \"q76\",\n    \"name\": \"Sterilization split and unquantified\
    \ solvents\",\n    \"stage\": \"Post-cooling stocks\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization.notes\",\n        \"stored\": \"Autoclave\
    \ the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding\
    \ after cooling.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization.notes\",\n        \"stored\": \"Autoclave\
    \ the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding\
    \ after cooling.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization.notes\",\n        \"stored\": \"Autoclave\
    \ the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding\
    \ after cooling.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization.notes\",\n        \"stored\": \"Autoclave\
    \ the base under N2-CO2; filter-sterilize Trace vitamins and NaHCO3 before adding\
    \ after cooling.\"\n      }\n    ],\n    \"desired\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"Post-cooling paragraph\",\n        \"exact_source_quote\": \"autoclaved or\
    \ *filter-sterilized\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      },\n      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\",\n        \"source_locator\"\
    : \"HTML table[1].row[2]\",\n        \"snapshot_sha256\": \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\"\
    ,\n        \"decoded_source_cells\": [\n          \" Trace vitamins* (see Medium\
    \ No. 197)                  \",\n          \" 10.0    \",\n          \" ml  \"\
    \n        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 8% NaHCO3 solution*           \
    \                      \",\n          \" 50.0    \",\n          \" ml  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"The starred vitamin and bicarbonate solutions\
    \ are filter-sterilized. Other added solutions are autoclaved. Water or other\
    \ solvent amounts for the percentage and molar stocks are not given; do not create\
    \ water amounts. The base has no specified pH or cultivation temperature.\"\n\
    \  },\n  {\n    \"decision_id\": \"q77\",\n    \"name\": \"Separate methanol option\"\
    ,\n    \"stage\": \"Excluded substrate branch\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"source_only\": \"2 M\
    \ methanol for JCM 35360\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"Substrate Solution\",\n        \"exact_source_quote\"\
    : \"For strain JCM 35360, 2 M methanol solution.\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"parsed_text_sha256\": \"ff564f75d0e5097af03cc5d0a83d3228e7dd9eabeeea52becaaca9a3562d92f6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a separate source option,\
    \ not any of the four selected maintained substrate identities. Do not add it\
    \ to the generated glycerol/citrate/maltose mixture or infer growth merely from\
    \ a strain mention.\"\n  },\n  {\n    \"decision_id\": \"q78\",\n    \"name\"\
    : \"Batch-volume arithmetic\",\n    \"stage\": \"Basis limit\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [],\n    \"desired\": {\n      \"\
    sum_of_printed_initial_and_postcooling_volumes_ml\": \"1004.5\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[9]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Distilled water               \
    \                         \",\n          \" 930.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" FeCl2 solution (see Medium No.\
    \ 187)                 \",\n          \" 1.0    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[5]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace element solution (see Medium\
    \ No. 187)            \",\n          \" 1.0    \",\n          \" ml  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[0].row[6]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Selenite-tungstate solution (see\
    \ Medium No. 431)      \",\n          \" 0.5    \",\n          \" ml  \"\n   \
    \     ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[0]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% MgCl2·6H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      },\n      {\n   \
    \     \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[1]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 10% CaCl2·2H2O solution       \
    \              \",\n          \" 1.0    \",\n          \" ml  \"\n        ],\n\
    \        \"representation\": \"Exact decoded DOM cell text, independently re-extracted\
    \ from bound raw HTML; not a literal raw quotation.\"\n      },\n      {\n   \
    \     \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[2]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Trace vitamins* (see Medium No.\
    \ 197)                  \",\n          \" 10.0    \",\n          \" ml  \"\n \
    \       ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[3]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" 8% NaHCO3 solution*           \
    \                      \",\n          \" 50.0    \",\n          \" ml  \"\n  \
    \      ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      },\n\
    \      {\n        \"source_key\": \"jcm1095\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095\"\
    ,\n        \"source_locator\": \"HTML table[1].row[4]\",\n        \"snapshot_sha256\"\
    : \"a33afcc48f25650dc656f3c9f63aebbb02b063d4c839761b3c92c228c9290dca\",\n    \
    \    \"decoded_source_cells\": [\n          \" Substrate solution (see below)\
    \                          \",\n          \" 10.0    \",\n          \" ml  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cell text, independently\
    \ re-extracted from bound raw HTML; not a literal raw quotation.\"\n      }\n\
    \    ],\n    \"interpretation\": \"930 + 1 + 1 + 0.5 + 1 + 1 + 10 + 50 + 10 =\
    \ 1004.5 ml before the separately per-litre sulfide dose. This sum is conditional\
    \ bookkeeping, not measured final volume. No receiving or stock denominator is\
    \ silently set to 1 L.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.007689.substrate-variant-conflation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Distinct substrate formulations are merged
  description: The generated target combines glycerol, citrate and maltose contributors
    as duplicate recipes. Their common base is not complete formulation equivalence.
  target_ids:
  - CultureMech:007689
  field_paths:
  - merged_from
  - solutions
  evidence_ids:
  - record
  - jcm1095
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.5
  native_severity: P2
  normalization_reason: P2.5 is escalated to blocker because different supplied carbon
    substrates define incompatible formulations within one generated target.
- finding_id: f2
  issue_key: culturemech.007689.stale-units-and-empty-stocks
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated units and empty stock placeholders supersede maintained repairs
  description: The target uses mass units for water and stock volumes, changes 0.5
    mg resazurin to 0.5 g, and retains ten empty Unknown solution rows. Owners already
    restore correct numerator units, nine named stocks and substrate strengths.
  target_ids:
  - CultureMech:007689
  field_paths:
  - ingredients[0].concentration
  - ingredients[5].concentration
  - solutions
  evidence_ids:
  - record
  - jcm1095
  - jcm187
  - jcm197
  - jcm431
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  issue_key: culturemech.007689.unsupported-denominators-and-percent
  category: quantity
  severity: major
  status: open
  certainty: provisional
  title: Final-volume rates and w/v bases exceed printed source precision
  description: Owners append per-litre denominators to printed batch masses/doses
    and PERCENT_W_V to unqualified percentages. Listed water or arithmetic addition
    does not establish final volume. Only the pre-use sulfide dose explicitly says
    per litre; substrate molarity is separately explicit.
  target_ids:
  - CultureMech:007689
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - jcm1095
  - jcm187
  - jcm197
  - jcm431
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.007689.phosphate-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The generated phosphate term omits two waters
  description: The target source name and primary row specify Na2HPO4·2H2O but the
    primary term is anhydrous CHEBI:34683. All maintained owners already use CHEBI:91258
    dihydrate.
  target_ids:
  - CultureMech:007689
  field_paths:
  - ingredients[6].term
  evidence_ids:
  - record
  - jcm1095
  - chebi34683
  - chebi91258
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  issue_key: culturemech.007689.maltose-correspondence
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Maltose anomer and current secondary correspondence need evidence
  description: Source generic maltose does not establish alpha specificity, and the
    selected owner secondary CHEBI:18167 lacks a current preferred MIM row. This is
    not proof that beta-maltose is required or that the historical link never existed.
  target_ids:
  - CultureMech:007689
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml::solutions[7].composition[0].term
  - data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml::solutions[7].composition[0].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm1095
  - chebi18167
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.007689.generated-preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated projection omits retained preparation
  description: The target lacks the five maintained preparation steps and valid sterilization
    details, including staged filtration and anaerobic handling.
  target_ids:
  - CultureMech:007689
  field_paths:
  - preparation_steps
  - sterilization
  - references
  evidence_ids:
  - record
  - jcm1095
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f7
  issue_key: culturemech.007689.claim-evidence-linkage
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported molarities, water inputs and explicit dose lack attached evidence
  description: Source and notes are present in owners, but claim-level evidence is
    absent. Evidence-only decisions are restricted to exact L water inputs, explicit
    molarity, per-litre sulfide dose and retained preparation; unsupported final-volume
    rates are not marked verified.
  target_ids:
  - CultureMech:007689
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - jcm1095
  - jcm187
  - jcm197
  - jcm431
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: This P4.3 minor exception addresses missing traceability on
    otherwise supported claims; substantive unit, basis, identity and form defects
    are separately graded major or blocker.
- finding_id: f8
  issue_key: culturemech.007689.m180-dependency-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Transferred stock dependency retains two anhydrous mappings
  description: Only the maintained M180 trace dependency still maps named cobalt and
    nickel hexahydrates to anhydrous concepts; receiving owners already repaired these
    forms.
  target_ids:
  - CultureMech:007689
  field_paths:
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - m180-dependency
  - jcm187
  - chebi35696
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: authoritative normalized stock dependency
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Separate exact substrate variants and preserve both glycerol source
    identities until equivalence is evidenced; regenerate after maintained corrections.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  description: Regenerate from the corrected maintained structure after preserving
    exact batch units and explicit stock scopes; do not reintroduce duplicated substrate
    or full parent formulas.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  description: Retain printed batch quantities and literal percentage labels; establish
    denominator and percentage basis before deriving concentrations or delivered solute
    amounts. Preserve the explicitly per-litre sulfide dose and molar substrate strengths.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  description: Preserve the corrected maintained dihydrate mapping during regeneration;
    do not change source mass by an unrequested molar conversion.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  description: Resolve source anomer precision and documented MIM correspondence at
    this exact maintained slot; do not guess a replacement.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
- action_id: a6
  description: Preserve the current supported preparation and collection references
    in a regenerated variant-aware projection.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
  description: Attach short exact source rows and locators to supported claims after
    resolving the substantive basis/form issues.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml
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
- action_id: a8
  description: Correct these exact dependency slots with source-supported hydrates,
    preserving the separately correct receiving-owner slots and existing batch-quantity
    evidence.
  finding_ids:
  - f8
  target_ids:
  - CultureMech:007689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: authoritative normalized stock dependency
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
- Coverage is partial because selected M1168 maltose source specificity/current secondary
  correspondence and final-volume/percentage bases remain unresolved. No historical
  lineage is inferred from the current missing index key.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-043
- generated-medium
```
