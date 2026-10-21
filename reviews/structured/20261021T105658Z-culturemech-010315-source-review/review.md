# Source and formulation review: acidiferrobacter_medium (CultureMech:010315)

- Review: 20261021T105658Z-culturemech-010315-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:43Z
- Finished UTC: 2026-10-21T10:56:58Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M898 maps exactly to JCM 861. The stored water and four stock additions use incorrect units, and the solid amounts lack a supported final-volume basis. The target omits source preparation and leaves critical stocks empty. Exact stock subsections resolve independently; dependency media, growth conditions and unresolved legacy sulfur provenance are kept separate.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 163; batch 017 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010315 | data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml | generated | acidiferrobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010315 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010315 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/163/strict.tsv |
| validate-terms | passed | True | CultureMech:010315 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010315 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010315 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact historical identity correspondence for MediaIngredientMech:001072 | unavailable | True | CultureMech:010315 | The asserted legacy sulfur ID has no exact row in the current pinned MIM index, and its exact historical identifier-to-record correspondence is unavailable. Primary elemental sulfur identity is supported; no replacement or historical nonexistence is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010315.

The four documented recipes completed; interpret the scope of each separately.

### Exact base and stock subsection identities

identity: supported. Targets: CultureMech:010315.

CultureMech:010315 denotes TOGO M898 / JCM861. M896 resolves to JCM860 Modified UBS only; M773 resolves to JCM748 trace element solution only. Neither referenced whole medium is substituted for the named stock, and no neighboring pH or organism-growth condition is inherited.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010315.

30 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "source_stage": "Receiving-medium basal solvent",
    "existing": {
      "value": "885",
      "unit": "G_PER_L"
    },
    "proposed": "Restore the 885 ml batch solvent dose; no density conversion to g/L is supported.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 basal table, distilled-water row",
        "exact_source_quote": "Distilled water 885.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 885,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ],
    "source_amount": {
      "value": 885,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "source_stage": "Receiving-medium batch mass; sulfur is separately treated then added after cooling",
    "existing": {
      "value": "26.64",
      "unit": "G_PER_L"
    },
    "proposed": "Retain the source batch mass with its addition stage. The stored G_PER_L basis is unsupported: 885+50+10+5+10=960 ml is only the sum of named liquid additions, not a measured final volume or a one-litre make-up instruction.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 basal table, exact MgSO4・7H2O row",
        "exact_source_quote": "MgSO 4 ·7H 2 O 26.64 g",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 26.64,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "source_stage": "Receiving-medium batch mass; sulfur is separately treated then added after cooling",
    "existing": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "proposed": "Retain the source batch mass with its addition stage. The stored G_PER_L basis is unsupported: 885+50+10+5+10=960 ml is only the sum of named liquid additions, not a measured final volume or a one-litre make-up instruction.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 basal table, exact Sulfur (powder) row",
        "exact_source_quote": "Sulfur (powder) 1.0 g",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Sulfur (powder)\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "ingredients[3].concentration",
    "decision": "not_quantified",
    "source_stage": "Acid dose to adjust the basal mixture before autoclaving",
    "existing": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "proposed": "Retain an unquantified sulfuric-acid dose and attach target pH/stage; no acid concentration or fixed amount is specified.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 preparation paragraph",
        "exact_source_quote": "adjust pH 1.9 with H 2 SO 4",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"H2SO4\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "source_stage": "Basal mixture before autoclaving",
    "existing": {
      "value": "50",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L; resolve only the exact named stock.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact stock-addition row",
        "exact_source_quote": "Modified UBS solution (see Medium No. 860 ) 50.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Modified UBS solution (see Medium [M896])\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ],
    "source_amount": {
      "value": 50,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[1].concentration",
    "decision": "correct",
    "source_stage": "After cooling, filter-sterilized stock",
    "existing": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L; resolve only the exact named stock.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact stock-addition row",
        "exact_source_quote": "1.0 M FeSO 4 solution (pH 2.0) 10.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"1.0 M FeSO4 solution (pH 2.0)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ],
    "source_amount": {
      "value": 10,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[2].concentration",
    "decision": "correct",
    "source_stage": "After cooling, filter-sterilized stock",
    "existing": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L; resolve only the exact named stock.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact stock-addition row",
        "exact_source_quote": "100 mM Potassium tetrathionate solution 5.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"100 mM Potassium tetrathionate solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"mM\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ],
    "source_amount": {
      "value": 5,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].concentration",
    "decision": "correct",
    "source_stage": "After cooling, filter-sterilized stock",
    "existing": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "proposed": "Represent the source ml addition per prepared batch, not G_PER_L; resolve only the exact named stock.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact stock-addition row",
        "exact_source_quote": "Trace element solution (see Medium No. 748 ) 10.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      },
      {
        "source_key": "togoM898",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (filter--sterilized) (see Medium [M773])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90"
      }
    ],
    "source_amount": {
      "value": 10,
      "unit": "ml"
    }
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[1] (stock strength)",
    "decision": "evidence_only",
    "source_stage": "FeSO4 stock before its 10 ml addition",
    "existing": null,
    "proposed": "The name already records 1.0 M; attach explicit stock-strength evidence and retain it separately from the dose. Do not infer a preparation mass or hydration state.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "1.0 M FeSO 4 solution (pH 2.0) 10.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[1] (stock pH)",
    "decision": "evidence_only",
    "source_stage": "FeSO4 stock, not receiving medium",
    "existing": null,
    "proposed": "The name already records pH 2.0 for this stock; preserve that stage and attach evidence rather than applying it to the final medium.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "1.0 M FeSO 4 solution (pH 2.0) 10.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[2] (stock strength)",
    "decision": "evidence_only",
    "source_stage": "Potassium tetrathionate stock before its 5 ml addition",
    "existing": null,
    "proposed": "The name already records 100 mM; preserve explicit stock strength separately from addition dose. No stock preparation mass is inferred.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "100 mM Potassium tetrathionate solution 5.0 ml",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "ph_value",
    "decision": "add",
    "source_stage": "Basal mixture before autoclaving",
    "existing": null,
    "proposed": "Represent target pH 1.9 at the stated stage; it is not a measured final pH.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "adjust pH 1.9 with H 2 SO 4",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "preparation_steps (sulfur steaming duration)",
    "decision": "add",
    "source_stage": "Sulfur-specific sterilization",
    "existing": null,
    "proposed": "Retain 3 hr per treatment, separate from general autoclaving.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "preparation_steps (sulfur treatment days)",
    "decision": "add",
    "source_stage": "Sulfur-specific sterilization",
    "existing": null,
    "proposed": "Retain treatment on each of 3 successive days; do not collapse this into continuous heating or apply it to stocks.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "preparation_steps (default autoclave temperature)",
    "decision": "add",
    "source_stage": "Qualified page default for basal autoclaving only",
    "existing": null,
    "proposed": "Retain 121°C with the unless-otherwise-stated qualifier; separately specified sulfur and filter-sterilized stocks are exceptions.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "preparation_steps (default autoclave duration)",
    "decision": "add",
    "source_stage": "Qualified page default for basal autoclaving only",
    "existing": null,
    "proposed": "Retain 15 min with the unless-otherwise-stated qualifier; do not apply the default to the sulfur-specific or filtered-stock stages.",
    "source_snippets": [
      {
        "source_key": "jcm861",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861",
        "source_locator": "Medium861 exact table/preparation or qualified page instruction",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8",
        "parsed_text_sha256": "13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "K 2 HPO 4 0.5 g",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "KCl 0.5 g",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "(NH 4 ) 2 SO 4 4.5 g",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 4.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "Na 2 SO 4 1.5 g",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"Na2SO4\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[0].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Modified UBS stock preparation only",
    "existing": null,
    "proposed": "Represent this stock recipe within the 50 ml stock reference; preserve source batch mass or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as final-medium g/L.",
    "source_snippets": [
      {
        "source_key": "jcm860",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860",
        "source_locator": "Medium860 Modified UBS solution subsection, exact ingredient/water row",
        "exact_source_quote": "Ca(NO 3 ) 2 ·4H 2 O 0.14 g",
        "snapshot_sha256": "adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7",
        "parsed_text_sha256": "4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3"
      },
      {
        "source_key": "togoM896",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"Ca(NO3)2・4H2O\",\n          \"volume\": 0.14,\n          \"unit\": \"g\"",
        "snapshot_sha256": "521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.08 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.08,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "H 3 BO 3 0.2 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.06 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.06,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.09 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.09,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "CuSO 4 ·5H 2 O 0.05 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "FeCl 3 ·6H 2 O 1.1 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"FeCl3・6H2O\",\n          \"volume\": 1.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  },
  {
    "input": [
      "target",
      "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml"
    ],
    "field_path": "solutions[3].composition (source-only exact stock row)",
    "decision": "add",
    "source_stage": "Filter-sterilized trace-stock preparation only",
    "existing": null,
    "proposed": "Represent this exact stock recipe within the 10 ml stock reference. Preserve supplied hydrates and unspecified x in manganese sulfate; do not use the whole Metallosphaera medium or its 2 ml dose.",
    "source_snippets": [
      {
        "source_key": "jcm748",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748",
        "source_locator": "Medium748 Trace element solution (filter-sterilized) subsection, exact ingredient/water row",
        "exact_source_quote": "MnSO 4 · x H 2 O 0.2 g",
        "snapshot_sha256": "b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52",
        "parsed_text_sha256": "891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566"
      },
      {
        "source_key": "togoM773",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:010315.

4 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/4 primary and 2/4 secondary instances; all asserted current CHEBI-keyed secondary IDs have exact pinned MIM rows. The separate legacy MediaIngredientMech:001072 correspondence remains unresolved and is not included in that current-key count. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 4: primary 100.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Direct ingredient identity and referenced-stock form boundaries

grounding: supported. Targets: CultureMech:010315.

Direct water, magnesium sulfate heptahydrate, elemental sulfur and sulfuric acid identities match the named source species at their stated specificity. Sulfur powder remains a physical-form qualifier. Referenced stock salts must retain their primary hydrate labels: the M773 dependency’s cobalt dichloride term does not represent hexahydrate, and MnSO4 xH2O has unspecified hydration that must not be replaced by a fixed hydrate or used for mass-to-mole conversion. These dependency issues are bounded context for resolving the empty target stock.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010315.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source-specific preparation and pH

completeness: concern. Targets: CultureMech:010315.

The primary excludes sulfur during basal autoclaving, states basal pH 1.9, gives sulfur-specific treatment and adds sulfur plus filter-sterilized stocks after cooling. Both target and owner omit all preparation_steps and ph_value. The table and preparation claims are represented separately in the complete quantity inventory; unspecified acid dose, measured final volume and stock preparation masses remain unresolved.

### Physical state and inherited complexity classification

scope: concern. Targets: CultureMech:010315.

The source is a liquid mineral/sulfur formulation with specified salt stocks; it states no complex biological mixture. COMPLEX / UNDEFINED requires reassessment after the empty stocks are represented, without promoting a fully defined classification while hydration/specification limits remain. Bacterial category and generic cultivation application are metadata, not experimental evidence for a named organism or strain.

## Findings

### f1: Source batch doses are misrepresented as per-litre mass concentrations

blocker / open / confirmed; issue key: culturemech.010315.dose-volume-basis.

Water 885 ml and stock additions 50/10/5/10 ml are all stored as G_PER_L. Magnesium sulfate 26.64 g and sulfur 1 g are source batch masses, while the source gives no 1 L final make-up. The named liquid additions sum to 960 ml before unquantified acid, solids and volume effects; that sum is not measured final volume. Reading these fields as final concentrations changes the represented formulation.

### f2: Empty stock nodes omit exact accessible referenced compositions

major / open / confirmed; issue key: culturemech.010315.unresolved-stock-compositions.

All four stocks have empty composition and Unknown solution names. Modified UBS resolves specifically to JCM860’s stock subsection, and trace solution to JCM748’s filtered stock subsection; their exact salts/solvent are available. FeSO4 and tetrathionate strengths are present in names but not evidence-linked structured stock context. Copying entire local dependency media would import unrelated ingredients/conditions and known inherited representation/form errors.

### f3: Distinct sulfur and stock preparation stages and basal pH are absent

major / open / confirmed; issue key: culturemech.010315.preparation-omitted.

The entire source preparation is missing from both local layers: basal pH 1.9, exclusion of sulfur from autoclaving, sulfur-specific treatment, then post-cooling sulfur and filtered-stock additions. The stock name’s pH 2.0 is specific to FeSO4 and cannot replace the base pH. The qualified general sterilization instruction is distinct from explicitly stated exceptions.

### f4: The legacy sulfur secondary identifier is unresolved in the pinned index

minor / open / confirmed; issue key: culturemech.010315.legacy-sulfur-link.

Elemental sulfur CHEBI:33403 is a supported primary identity, but MediaIngredientMech:001072 remains an unverified historical secondary link. The complete current pinned index has no exact identifier row. The absence is limited to this snapshot and does not prove historical nonexistence or justify a guessed replacement.

### f5: Inherited COMPLEX and UNDEFINED labels lack source-specific support

minor / open / confirmed; issue key: culturemech.010315.classification-support.

The exact basal and referenced-stock sources contain named mineral compounds and elemental sulfur rather than an identified complex biological ingredient. Missing local stock representation does not itself make the scientific recipe complex. Unresolved hydrate/specification details remain distinct from classification.

## Recommended Actions And Acceptance Checks

### a1

Restore exact batch masses, ml doses and preparation-stage basis in the normalized owner, then regenerate through maintained code. Do not use solvent density, assume 1 L final volume or derive final molarity from the incomplete volume specification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the exact named stock recipes/typed references and explicit strength/dose distinction. Preserve CoCl2 hexahydrate and unspecified manganese sulfate hydration; leave unspecified FeSO4/tetrathionate preparation masses unguessed. Do not flatten dependency media into this target.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore exact source preparation and evidence at each stage, keeping basal pH, stock pH, separate sulfur treatment and filtered additions distinct. Retain unquantified acid dose and avoid invented operating details.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover an exact historical catalog mapping or retain the secondary link as unresolved with provenance; any later migration must use a verified exact identity while preserving the supported primary sulfur term.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reassess and evidence the medium/composition enums after resolving scoped stocks, preserving LIQUID and avoiding unverified organism/growth claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/163/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/163/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml:1:id: CultureMech:010315<br>./data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml:1:id: CultureMech:010315<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/163/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 24 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861; Medium861 entire formulation and preparation, including qualified page sterilization instruction | supports | Full exact receiving-medium table, post-cooling additions and sulfur-specific preparation inspected. Known liquid additions total 960 ml; no one-litre final make-up statement is supplied. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898; $.meta; $.components[0:2]; $.comments[0] | supports | TOGO source identifier JCM_M861 and source URL match; two main-recipe stages retain original g/ml amounts, FeSO4 strength/pH and tetrathionate strength. |
| ubs-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860; Only Modified UBS solution subsection | supports | The five salts and 1 L water define Modified UBS. Ferrovum basal composition, pH 2.3 and the JCM30830 pH 1.7 comment are outside this target’s scope. |
| ubs-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896; $.meta; $.components[2] only | supports | Exact M896/JCM860 cross-reference resolves to the Modified UBS stock subsection; the entire Ferrovum medium is not the added stock. |
| trace-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748; Only Trace element solution (filter-sterilized) subsection | supports | Seven specified trace solutes plus 1 L water define the referenced stock. The Metallosphaera basal recipe, pH 3.5 and its 2 ml stock dose do not apply to this target. |
| trace-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773; $.meta; $.components[1] only | supports | Exact M773/JCM748 source mapping and trace-stock subsection resolve; variable MnSO4 xH2O remains variable hydration and CoCl2 is hexahydrate. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/163/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33403 resolves to elemental sulfur. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| ubs-local | data/normalized_yaml/bacterial/TOGO_M896_Ferrovum_Medium.yaml; Complete dependency record read; only named stock subsection used as source context | context_only | Current owner flattens its Modified UBS salts among Ferrovum ingredients and conflates water; it is not a safe source of receiving-medium concentrations. |
| trace-local | data/normalized_yaml/archaea/TOGO_M773_Metallosphaera_Cuprina_Medium.yaml; Complete dependency record read; only named stock subsection used as source context | context_only | Current owner flattens trace salts among Metallosphaera ingredients and contains inherited wrong dose/water units; its basal ingredients/pH are outside this target. |
| stock-chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:131527 / dipotassium hydrogen phosphate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:32588 / potassium chloride: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:62946 / ammonium sulfate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:32149 / sodium sulfate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi86159 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:86159 / calcium nitrate tetrahydrate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:75213 / sodium molybdate dihydrate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:33118 / boric acid: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:35696 / cobalt dichloride: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:32312 / zinc sulfate heptahydrate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:31440 / copper(II) sulfate pentahydrate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:86254 / iron trichloride hexahydrate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| stock-chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS ID, label and available supplied-form annotations for referenced stock context | supports | CHEBI:86360 / manganese(II) sulfate: metadata inspected separately from the source stock recipe; not automatic approval of a dependency grounding. |
| legacy-sulfur-index | src/culturemech/data/mediaingredientmech/label_index.csv; All pinned index rows / identifier column; exact legacy key search, ignored files included | context_only | The asserted legacy MediaIngredientMech:001072 does not occur in the complete current pinned index. This does not establish that it never existed or disprove the primary elemental-sulfur identity; the historical identifier-to-record mapping remains unresolved. |
| history-metadata | data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source-stage parser, formulation merge, duplicate handling and pinned MIM resolver inspected as maintenance context. No historical replay or current regeneration was executed; old history entries remain append-only. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source-stage parser, formulation merge, duplicate handling and pinned MIM resolver inspected as maintenance context. No historical replay or current regeneration was executed; old history entries remain append-only. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source-stage parser, formulation merge, duplicate handling and pinned MIM resolver inspected as maintenance context. No historical replay or current regeneration was executed; old history entries remain append-only. |
| writer-3 | src/culturemech/ingredients/mim_label_index.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source-stage parser, formulation merge, duplicate handling and pinned MIM resolver inspected as maintenance context. No historical replay or current regeneration was executed; old history entries remain append-only. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required exact historical correspondence for the asserted legacy MediaIngredientMech:001072 could not be verified. This makes completion partial; it does not alter the independently supported elemental-sulfur primary identity or the assessed source formulation.
- No final-volume normalization, sulfuric-acid strength/dose, fixed MnSO4 hydration, missing stock preparation mass, growth temperature or strain-specific outcome was inferred. Exact referenced stock subsections were assessed; the two entire dependency media were not promoted to independently reviewed records. Legacy MIM absence is bounded to the pinned current index, not all historical releases.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105658Z-culturemech-010315-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidiferrobacter_medium (CultureMech:010315)'
started_at: '2026-10-21T10:48:43Z'
finished_at: '2026-10-21T10:56:58Z'
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
summary: TOGO M898 maps exactly to JCM 861. The stored water and four stock additions
  use incorrect units, and the solid amounts lack a supported final-volume basis.
  The target omits source preparation and leaves critical stocks empty. Exact stock
  subsections resolve independently; dependency media, growth conditions and unresolved
  legacy sulfur provenance are kept separate.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
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
  - path: data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
    sha256: 92f461896c094b7ecfa9d80cd98b27fab8450e75412f39bce7b0fbb9fbbfcb77
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M773_Metallosphaera_Cuprina_Medium.yaml
    sha256: 859143e9b090e700a27e3123caeebcea2b8afca6fe52cd32feb7afe511c46580
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M896_Ferrovum_Medium.yaml
    sha256: 8887b4aae70848f560752e8f1ebcf3594d42c645cd41ba1d3983daeef04e0c7c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
    sha256: 4f5bfb365f85a5d2043ea2e4bdd6a015a8c227cd9e995b8310efc635b635d523
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 163; batch 017 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010315
targets:
- target_id: CultureMech:010315
  path: data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  label: acidiferrobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/163/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/163/strict.tsv"
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010315
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
  - CultureMech:010315
- check_id: legacy-mim-historical-correspondence
  name: Exact historical identity correspondence for MediaIngredientMech:001072
  required: true
  status: unavailable
  summary: The asserted legacy sulfur ID has no exact row in the current pinned MIM
    index, and its exact historical identifier-to-record correspondence is unavailable.
    Primary elemental sulfur identity is supported; no replacement or historical nonexistence
    is inferred.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - legacy-sulfur-index
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:13.466885Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/163/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:15.054580Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/163/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:17.138940Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:18.205782Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:56:56Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml:1:id: CultureMech:010315

    ./data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml:1:id:
    CultureMech:010315

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/163/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:56:56Z'
  support: supports
  summary: 24 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: dec37dcae4922bc8ff473562110c99e43fe5f1e49099487989de4c1b40257184
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861
  locator: Medium861 entire formulation and preparation, including qualified page
    sterilization instruction
  accessed_at: '2026-10-21T10:33:41.650912Z'
  support: supports
  summary: Full exact receiving-medium table, post-cooling additions and sulfur-specific
    preparation inspected. Known liquid additions total 960 ml; no one-litre final
    make-up statement is supplied.
  snapshot_sha256: fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898
  locator: $.meta; $.components[0:2]; $.comments[0]
  accessed_at: '2026-10-21T10:33:40.276720Z'
  support: supports
  summary: TOGO source identifier JCM_M861 and source URL match; two main-recipe stages
    retain original g/ml amounts, FeSO4 strength/pH and tetrathionate strength.
  snapshot_sha256: ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90
- evidence_id: ubs-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860
  locator: Only Modified UBS solution subsection
  accessed_at: '2026-10-21T10:33:41.473380Z'
  support: supports
  summary: The five salts and 1 L water define Modified UBS. Ferrovum basal composition,
    pH 2.3 and the JCM30830 pH 1.7 comment are outside this target’s scope.
  snapshot_sha256: adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7
- evidence_id: ubs-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896
  locator: $.meta; $.components[2] only
  accessed_at: '2026-10-21T10:33:40.263338Z'
  support: supports
  summary: Exact M896/JCM860 cross-reference resolves to the Modified UBS stock subsection;
    the entire Ferrovum medium is not the added stock.
  snapshot_sha256: 521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748
  locator: Only Trace element solution (filter-sterilized) subsection
  accessed_at: '2026-10-21T10:33:41.086942Z'
  support: supports
  summary: Seven specified trace solutes plus 1 L water define the referenced stock.
    The Metallosphaera basal recipe, pH 3.5 and its 2 ml stock dose do not apply to
    this target.
  snapshot_sha256: b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52
- evidence_id: trace-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773
  locator: $.meta; $.components[1] only
  accessed_at: '2026-10-21T10:33:39.509512Z'
  support: supports
  summary: Exact M773/JCM748 source mapping and trace-stock subsection resolve; variable
    MnSO4 xH2O remains variable hydration and CoCl2 is hexahydrate.
  snapshot_sha256: 56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/163/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: f5d860de32ade14bac66f75f61802d2d3e212042c57307a6e327258a9ebc4a2d
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi33403
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:26:28.748668Z'
  support: supports
  summary: CHEBI:33403 resolves to elemental sulfur. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T10:56:56Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id":
    "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: ubs-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M896_Ferrovum_Medium.yaml
  locator: Complete dependency record read; only named stock subsection used as source
    context
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current owner flattens its Modified UBS salts among Ferrovum ingredients
    and conflates water; it is not a safe source of receiving-medium concentrations.
  snapshot_sha256: 8887b4aae70848f560752e8f1ebcf3594d42c645cd41ba1d3983daeef04e0c7c
- evidence_id: trace-local
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M773_Metallosphaera_Cuprina_Medium.yaml
  locator: Complete dependency record read; only named stock subsection used as source
    context
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current owner flattens trace salts among Metallosphaera ingredients and
    contains inherited wrong dose/water units; its basal ingredients/pH are outside
    this target.
  snapshot_sha256: 859143e9b090e700a27e3123caeebcea2b8afca6fe52cd32feb7afe511c46580
- evidence_id: stock-chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: 'CHEBI:131527 / dipotassium hydrogen phosphate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: stock-chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: 'CHEBI:32588 / potassium chloride: metadata inspected separately from the
    source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: stock-chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: 'CHEBI:62946 / ammonium sulfate: metadata inspected separately from the
    source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: stock-chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: 'CHEBI:32149 / sodium sulfate: metadata inspected separately from the source
    stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: stock-chebi86159
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T10:33:40.461439Z'
  support: supports
  summary: 'CHEBI:86159 / calcium nitrate tetrahydrate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: d2b0e9caef5876c00ed00136113d600d34a071b137bdd8c661c734ad5435682f
- evidence_id: stock-chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: 'CHEBI:75213 / sodium molybdate dihydrate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: stock-chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: 'CHEBI:33118 / boric acid: metadata inspected separately from the source
    stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: stock-chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: 'CHEBI:35696 / cobalt dichloride: metadata inspected separately from the
    source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: stock-chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: 'CHEBI:32312 / zinc sulfate heptahydrate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: stock-chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: 'CHEBI:31440 / copper(II) sulfate pentahydrate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: stock-chebi86254
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-21T08:17:30.289392Z'
  support: supports
  summary: 'CHEBI:86254 / iron trichloride hexahydrate: metadata inspected separately
    from the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: 89afba545ad02f24a850933df154af25dee37357b583f82de13866b44f18d683
- evidence_id: stock-chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS ID, label and available supplied-form annotations for referenced
    stock context
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: 'CHEBI:86360 / manganese(II) sulfate: metadata inspected separately from
    the source stock recipe; not automatic approval of a dependency grounding.'
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: legacy-sulfur-index
  kind: search
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All pinned index rows / identifier column; exact legacy key search, ignored
    files included
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: The asserted legacy MediaIngredientMech:001072 does not occur in the complete
    current pinned index. This does not establish that it never existed or disprove
    the primary elemental-sulfur identity; the historical identifier-to-record mapping
    remains unresolved.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
  search_scope: Complete explicitly named pinned label_index.csv, exact identifier
    equality plus rg --no-ignore --hidden -F MediaIngredientMech:001072. Current snapshot
    only; no claim of exhaustive historical catalog coverage.
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml", "events":
    12, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current source-stage parser, formulation merge, duplicate handling and
    pinned MIM resolver inspected as maintenance context. No historical replay or
    current regeneration was executed; old history entries remain append-only.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current source-stage parser, formulation merge, duplicate handling and
    pinned MIM resolver inspected as maintenance context. No historical replay or
    current regeneration was executed; old history entries remain append-only.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current source-stage parser, formulation merge, duplicate handling and
    pinned MIM resolver inspected as maintenance context. No historical replay or
    current regeneration was executed; old history entries remain append-only.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/ingredients/mim_label_index.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:56:56Z'
  support: context_only
  summary: Current source-stage parser, formulation merge, duplicate handling and
    pinned MIM resolver inspected as maintenance context. No historical replay or
    current regeneration was executed; old history entries remain append-only.
  snapshot_sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact base and stock subsection identities
  outcome: supported
  summary: CultureMech:010315 denotes TOGO M898 / JCM861. M896 resolves to JCM860
    Modified UBS only; M773 resolves to JCM748 trace element solution only. Neither
    referenced whole medium is substituted for the named stock, and no neighboring
    pH or organism-growth condition is inherited.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - ubs-primary
  - ubs-provider
  - trace-primary
  - trace-provider
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 30 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Receiving-medium basal solvent\",\n  \
    \  \"existing\": {\n      \"value\": \"885\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"proposed\": \"Restore the 885 ml batch solvent dose; no density\
    \ conversion to g/L is supported.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 basal table, distilled-water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 885.0 ml\",\n        \"snapshot_sha256\"\
    : \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\",\n    \
    \    \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 885,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"value\": 885,\n      \"unit\": \"ml\"\
    \n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Receiving-medium batch mass; sulfur is\
    \ separately treated then added after cooling\",\n    \"existing\": {\n      \"\
    value\": \"26.64\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"\
    Retain the source batch mass with its addition stage. The stored G_PER_L basis\
    \ is unsupported: 885+50+10+5+10=960 ml is only the sum of named liquid additions,\
    \ not a measured final volume or a one-litre make-up instruction.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 basal table, exact MgSO4・7H2O row\",\n        \"exact_source_quote\"\
    : \"MgSO 4 ·7H 2 O 26.64 g\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 26.64,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Receiving-medium batch mass; sulfur is\
    \ separately treated then added after cooling\",\n    \"existing\": {\n      \"\
    value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": \"Retain\
    \ the source batch mass with its addition stage. The stored G_PER_L basis is unsupported:\
    \ 885+50+10+5+10=960 ml is only the sum of named liquid additions, not a measured\
    \ final volume or a one-litre make-up instruction.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 basal table, exact Sulfur (powder) row\",\n        \"exact_source_quote\"\
    : \"Sulfur (powder) 1.0 g\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sulfur (powder)\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ingredients[3].concentration\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_stage\": \"Acid dose to adjust the basal mixture\
    \ before autoclaving\",\n    \"existing\": {\n      \"value\": \"variable\",\n\
    \      \"unit\": \"VARIABLE\"\n    },\n    \"proposed\": \"Retain an unquantified\
    \ sulfuric-acid dose and attach target pH/stage; no acid concentration or fixed\
    \ amount is specified.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 preparation paragraph\",\n        \"\
    exact_source_quote\": \"adjust pH 1.9 with H 2 SO 4\",\n        \"snapshot_sha256\"\
    : \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\",\n    \
    \    \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\"\",\n        \"snapshot_sha256\": \"\
    ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\n      }\n\
    \    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Basal mixture before autoclaving\",\n\
    \    \"existing\": {\n      \"value\": \"50\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L; resolve only the exact named stock.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact stock-addition row\",\n        \"exact_source_quote\": \"\
    Modified UBS solution (see Medium No. 860 ) 50.0 ml\",\n        \"snapshot_sha256\"\
    : \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\",\n    \
    \    \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Modified UBS solution (see Medium [M896])\\\"\
    ,\\n          \\\"volume\\\": 50,\\n          \\\"unit\\\": \\\"ml\\\"\",\n  \
    \      \"snapshot_sha256\": \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 50,\n      \"unit\"\
    : \"ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"After cooling, filter-sterilized stock\"\
    ,\n    \"existing\": {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L; resolve only the exact named stock.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact stock-addition row\",\n        \"exact_source_quote\": \"\
    1.0 M FeSO 4 solution (pH 2.0) 10.0 ml\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1.0 M FeSO4 solution (pH 2.0)\\\",\\n        \
    \  \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"\
    conc_value\\\": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\n     \
    \ }\n    ],\n    \"source_amount\": {\n      \"value\": 10,\n      \"unit\": \"\
    ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[2].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"After cooling, filter-sterilized stock\"\
    ,\n    \"existing\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L; resolve only the exact named stock.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact stock-addition row\",\n        \"exact_source_quote\": \"\
    100 mM Potassium tetrathionate solution 5.0 ml\",\n        \"snapshot_sha256\"\
    : \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\",\n    \
    \    \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"100 mM Potassium tetrathionate solution\\\",\\\
    n          \\\"volume\\\": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n       \
    \   \\\"conc_value\\\": 100,\\n          \\\"conc_unit\\\": \\\"mM\\\"\",\n  \
    \      \"snapshot_sha256\": \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 5,\n      \"unit\"\
    : \"ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"After cooling, filter-sterilized stock\"\
    ,\n    \"existing\": {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": \"Represent the source ml addition per prepared batch,\
    \ not G_PER_L; resolve only the exact named stock.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact stock-addition row\",\n        \"exact_source_quote\": \"\
    Trace element solution (see Medium No. 748 ) 10.0 ml\",\n        \"snapshot_sha256\"\
    : \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\",\n    \
    \    \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      },\n      {\n        \"source_key\": \"togoM898\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M898\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (filter--sterilized) (see\
    \ Medium [M773])\\\",\\n          \\\"volume\\\": 10,\\n          \\\"unit\\\"\
    : \\\"ml\\\"\",\n        \"snapshot_sha256\": \"ae8e03055ab58e77c0a91d08915a78f82e77489801e83009974ed33523967c90\"\
    \n      }\n    ],\n    \"source_amount\": {\n      \"value\": 10,\n      \"unit\"\
    : \"ml\"\n    }\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[1] (stock strength)\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"FeSO4 stock before its 10 ml addition\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"The name already records 1.0 M;\
    \ attach explicit stock-strength evidence and retain it separately from the dose.\
    \ Do not infer a preparation mass or hydration state.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact table/preparation or qualified page instruction\",\n     \
    \   \"exact_source_quote\": \"1.0 M FeSO 4 solution (pH 2.0) 10.0 ml\",\n    \
    \    \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[1] (stock pH)\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"source_stage\": \"FeSO4 stock, not receiving medium\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"The name already records pH 2.0\
    \ for this stock; preserve that stage and attach evidence rather than applying\
    \ it to the final medium.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 exact table/preparation or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"1.0 M FeSO 4 solution\
    \ (pH 2.0) 10.0 ml\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[2] (stock strength)\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Potassium tetrathionate stock before\
    \ its 5 ml addition\",\n    \"existing\": null,\n    \"proposed\": \"The name\
    \ already records 100 mM; preserve explicit stock strength separately from addition\
    \ dose. No stock preparation mass is inferred.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 exact table/preparation or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"100 mM Potassium tetrathionate\
    \ solution 5.0 ml\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"ph_value\",\n    \"decision\": \"add\",\n    \"\
    source_stage\": \"Basal mixture before autoclaving\",\n    \"existing\": null,\n\
    \    \"proposed\": \"Represent target pH 1.9 at the stated stage; it is not a\
    \ measured final pH.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 exact table/preparation or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"adjust pH 1.9 with H\
    \ 2 SO 4\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (sulfur steaming duration)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Sulfur-specific sterilization\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"Retain 3 hr per treatment, separate\
    \ from general autoclaving.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 exact table/preparation or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"Steam sulfur for 3 hr\
    \ on each of 3 successive days.\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (sulfur treatment days)\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"Sulfur-specific sterilization\"\
    ,\n    \"existing\": null,\n    \"proposed\": \"Retain treatment on each of 3\
    \ successive days; do not collapse this into continuous heating or apply it to\
    \ stocks.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm861\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\"\
    ,\n        \"source_locator\": \"Medium861 exact table/preparation or qualified\
    \ page instruction\",\n        \"exact_source_quote\": \"Steam sulfur for 3 hr\
    \ on each of 3 successive days.\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (default autoclave temperature)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Qualified page default\
    \ for basal autoclaving only\",\n    \"existing\": null,\n    \"proposed\": \"\
    Retain 121°C with the unless-otherwise-stated qualifier; separately specified\
    \ sulfur and filter-sterilized stocks are exceptions.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact table/preparation or qualified page instruction\",\n     \
    \   \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"preparation_steps (default autoclave duration)\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Qualified page default\
    \ for basal autoclaving only\",\n    \"existing\": null,\n    \"proposed\": \"\
    Retain 15 min with the unless-otherwise-stated qualifier; do not apply the default\
    \ to the sulfur-specific or filtered-stock stages.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm861\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=861\",\n        \"source_locator\"\
    : \"Medium861 exact table/preparation or qualified page instruction\",\n     \
    \   \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"fb92b120013521c7c428c4b6e2e762f5040934717c2c4e76cbe9ef89e8b766e8\"\
    ,\n        \"parsed_text_sha256\": \"13f1437d082221065ea90c425fa13a092bcc868f4f01e5bce0a0eef8520dac41\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"Distilled water 1.0\
    \ L\",\n        \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"K 2 HPO 4 0.5 g\"\
    ,\n        \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"KCl 0.5 g\",\n  \
    \      \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.5,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"(NH 4 ) 2 SO 4 4.5\
    \ g\",\n        \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4\\\",\\n          \\\"volume\\\": 4.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"Na 2 SO 4 1.5 g\"\
    ,\n        \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SO4\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[0].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Modified UBS stock\
    \ preparation only\",\n    \"existing\": null,\n    \"proposed\": \"Represent\
    \ this stock recipe within the 50 ml stock reference; preserve source batch mass\
    \ or 1 L solvent. Do not import Ferrovum basal ingredients or normalize this as\
    \ final-medium g/L.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm860\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=860\"\
    ,\n        \"source_locator\": \"Medium860 Modified UBS solution subsection, exact\
    \ ingredient/water row\",\n        \"exact_source_quote\": \"Ca(NO 3 ) 2 ·4H 2\
    \ O 0.14 g\",\n        \"snapshot_sha256\": \"adf267db317aa0846635c08cd5759d04f0e66f5a9b130bbca96d2b08e9da76d7\"\
    ,\n        \"parsed_text_sha256\": \"4f5b4cb606b0a22a0c519b102d7b40ee9f6cbc920c7b9e9957aca82800727ba3\"\
    \n      },\n      {\n        \"source_key\": \"togoM896\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M896\",\n \
    \       \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Ca(NO3)2・4H2O\\\",\\n          \\\"volume\\\"\
    : 0.14,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    521e7d99537221c1fda7d7abc2f8ff4dab08bdac0f36a76233b656db143b8de0\"\n      }\n\
    \    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    Na 2 MoO 4 ·2H 2 O 0.08 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.08,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\n      }\n\
    \    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    H 3 BO 3 0.2 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    CoCl 2 ·6H 2 O 0.06 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 0.06,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    ZnSO 4 ·7H 2 O 0.09 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.09,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    CuSO 4 ·5H 2 O 0.05 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    FeCl 3 ·6H 2 O 1.1 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl3・6H2O\\\",\\n          \\\"volume\\\": 1.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": [\n      \"target\",\n      \"data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml\"\
    \n    ],\n    \"field_path\": \"solutions[3].composition (source-only exact stock\
    \ row)\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Filter-sterilized\
    \ trace-stock preparation only\",\n    \"existing\": null,\n    \"proposed\":\
    \ \"Represent this exact stock recipe within the 10 ml stock reference. Preserve\
    \ supplied hydrates and unspecified x in manganese sulfate; do not use the whole\
    \ Metallosphaera medium or its 2 ml dose.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm748\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748\"\
    ,\n        \"source_locator\": \"Medium748 Trace element solution (filter-sterilized)\
    \ subsection, exact ingredient/water row\",\n        \"exact_source_quote\": \"\
    MnSO 4 · x H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"b3eaa995112e3091d95865876d73c4f528410e061ee693a6870770f88aa82a52\"\
    ,\n        \"parsed_text_sha256\": \"891051d0214b0859d7067c6c685b9f9d828b0418c4a43d40f367f2de4aea1566\"\
    \n      },\n      {\n        \"source_key\": \"togoM773\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M773\",\n \
    \       \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4・xH2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"56b46b138798e6e9f5869ccfc5348881a5086ee592a1025da18c7cde5bffd7c2\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '4 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 4/4 primary and 2/4 secondary
    instances; all asserted current CHEBI-keyed secondary IDs have exact pinned MIM
    rows. The separate legacy MediaIngredientMech:001072 correspondence remains unresolved
    and is not included in that current-key count. Source forms are assessed separately.'
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi26836
  - chebi31795
  - chebi33403
  details: 'Instance coverage on a 0–100 percent scale, denominator 4: primary 100.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Direct ingredient identity and referenced-stock form boundaries
  outcome: supported
  summary: 'Direct water, magnesium sulfate heptahydrate, elemental sulfur and sulfuric
    acid identities match the named source species at their stated specificity. Sulfur
    powder remains a physical-form qualifier. Referenced stock salts must retain their
    primary hydrate labels: the M773 dependency’s cobalt dichloride term does not
    represent hexahydrate, and MnSO4 xH2O has unspecified hydration that must not
    be replaced by a fixed hydrate or used for mass-to-mole conversion. These dependency
    issues are bounded context for resolving the empty target stock.'
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - primary
  - ubs-primary
  - trace-primary
  - trace-local
  - stock-chebi35696
  - stock-chebi86360
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Source-specific preparation and pH
  outcome: concern
  summary: The primary excludes sulfur during basal autoclaving, states basal pH 1.9,
    gives sulfur-specific treatment and adds sulfur plus filter-sterilized stocks
    after cooling. Both target and owner omit all preparation_steps and ph_value.
    The table and preparation claims are represented separately in the complete quantity
    inventory; unspecified acid dose, measured final volume and stock preparation
    masses remain unresolved.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Physical state and inherited complexity classification
  outcome: concern
  summary: The source is a liquid mineral/sulfur formulation with specified salt stocks;
    it states no complex biological mixture. COMPLEX / UNDEFINED requires reassessment
    after the empty stocks are represented, without promoting a fully defined classification
    while hydration/specification limits remain. Bacterial category and generic cultivation
    application are metadata, not experimental evidence for a named organism or strain.
  target_ids:
  - CultureMech:010315
  evidence_ids:
  - record
  - primary
  - ubs-primary
  - trace-primary
findings:
- finding_id: f1
  issue_key: culturemech.010315.dose-volume-basis
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Source batch doses are misrepresented as per-litre mass concentrations
  description: Water 885 ml and stock additions 50/10/5/10 ml are all stored as G_PER_L.
    Magnesium sulfate 26.64 g and sulfur 1 g are source batch masses, while the source
    gives no 1 L final make-up. The named liquid additions sum to 960 ml before unquantified
    acid, solids and volume effects; that sum is not measured final volume. Reading
    these fields as final concentrations changes the represented formulation.
  target_ids:
  - CultureMech:010315
  field_paths:
  - ingredients[0:3].concentration
  - solutions[0:4].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  issue_key: culturemech.010315.unresolved-stock-compositions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Empty stock nodes omit exact accessible referenced compositions
  description: All four stocks have empty composition and Unknown solution names.
    Modified UBS resolves specifically to JCM860’s stock subsection, and trace solution
    to JCM748’s filtered stock subsection; their exact salts/solvent are available.
    FeSO4 and tetrathionate strengths are present in names but not evidence-linked
    structured stock context. Copying entire local dependency media would import unrelated
    ingredients/conditions and known inherited representation/form errors.
  target_ids:
  - CultureMech:010315
  field_paths:
  - solutions
  - solutions[0].composition
  - solutions[3].composition
  evidence_ids:
  - record
  - owner-0
  - ubs-primary
  - ubs-provider
  - trace-primary
  - trace-provider
  - ubs-local
  - trace-local
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  issue_key: culturemech.010315.preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Distinct sulfur and stock preparation stages and basal pH are absent
  description: 'The entire source preparation is missing from both local layers: basal
    pH 1.9, exclusion of sulfur from autoclaving, sulfur-specific treatment, then
    post-cooling sulfur and filtered-stock additions. The stock name’s pH 2.0 is specific
    to FeSO4 and cannot replace the base pH. The qualified general sterilization instruction
    is distinct from explicitly stated exceptions.'
  target_ids:
  - CultureMech:010315
  field_paths:
  - preparation_steps
  - ph_value
  - solutions[1].preferred_term
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.010315.legacy-sulfur-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The legacy sulfur secondary identifier is unresolved in the pinned index
  description: Elemental sulfur CHEBI:33403 is a supported primary identity, but MediaIngredientMech:001072
    remains an unverified historical secondary link. The complete current pinned index
    has no exact identifier row. The absence is limited to this snapshot and does
    not prove historical nonexistence or justify a guessed replacement.
  target_ids:
  - CultureMech:010315
  field_paths:
  - ingredients[2].mediaingredientmech_term
  evidence_ids:
  - record
  - chebi33403
  - mim
  - legacy-sulfur-index
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.010315.classification-support
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Inherited COMPLEX and UNDEFINED labels lack source-specific support
  description: The exact basal and referenced-stock sources contain named mineral
    compounds and elemental sulfur rather than an identified complex biological ingredient.
    Missing local stock representation does not itself make the scientific recipe
    complex. Unresolved hydrate/specification details remain distinct from classification.
  target_ids:
  - CultureMech:010315
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - primary
  - ubs-primary
  - trace-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  description: Restore exact batch masses, ml doses and preparation-stage basis in
    the normalized owner, then regenerate through maintained code. Do not use solvent
    density, assume 1 L final volume or derive final molarity from the incomplete
    volume specification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010315
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  description: Represent the exact named stock recipes/typed references and explicit
    strength/dose distinction. Preserve CoCl2 hexahydrate and unspecified manganese
    sulfate hydration; leave unspecified FeSO4/tetrathionate preparation masses unguessed.
    Do not flatten dependency media into this target.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010315
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  description: Restore exact source preparation and evidence at each stage, keeping
    basal pH, stock pH, separate sulfur treatment and filtered additions distinct.
    Retain unquantified acid dose and avoid invented operating details.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010315
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  description: Recover an exact historical catalog mapping or retain the secondary
    link as unresolved with provenance; any later migration must use a verified exact
    identity while preserving the supported primary sulfur term.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010315
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
  description: Reassess and evidence the medium/composition enums after resolving
    scoped stocks, preserving LIQUID and avoiding unverified organism/growth claims.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010315
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml
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
- Required exact historical correspondence for the asserted legacy MediaIngredientMech:001072
  could not be verified. This makes completion partial; it does not alter the independently
  supported elemental-sulfur primary identity or the assessed source formulation.
- No final-volume normalization, sulfuric-acid strength/dose, fixed MnSO4 hydration,
  missing stock preparation mass, growth temperature or strain-specific outcome was
  inferred. Exact referenced stock subsections were assessed; the two entire dependency
  media were not promoted to independently reviewed records. Legacy MIM absence is
  bounded to the pinned current index, not all historical releases.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
