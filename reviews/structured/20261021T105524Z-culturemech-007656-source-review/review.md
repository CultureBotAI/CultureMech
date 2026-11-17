# Source and formulation review: acidified_mpob_medium (CultureMech:007656)

- Review: 20261021T105524Z-culturemech-007656-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:44Z
- Finished UTC: 2026-10-21T10:55:24Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM1065/TOGO M1134 identity is supported, but both local layers misstate water, resazurin and all six stock doses, omit the referenced stock definitions, and lose the source anaerobic preparation sequence. The recipe is not scientifically usable as represented despite four passing diagnostics.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 165; batch 017 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007656 | data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml | generated | acidified_mpob_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007656 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007656 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/165/strict.tsv |
| validate-terms | passed | True | CultureMech:007656 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007656 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007656 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007656.

The four documented recipes completed; interpret the scope of each separately.

### Exact source and cross-reference identity

identity: supported. Targets: CultureMech:007656.

TOGO M1134 explicitly identifies JCM1065. M180 resolves to JCM187 for FeCl2 and trace elements; M190 resolves to JCM197 for trace vitamins. Their whole parent media are not additions to this recipe. The six local stock names retain useful source qualifiers but name=Unknown solution and empty compositions are not resolved stock definitions.

### Every current amount and source-only stock/preparation quantity

quantity: concern. Targets: CultureMech:007656.

All ten direct ingredient quantities, six stock doses/strengths, twenty-two referenced stock components and three numeric preparation contexts are accounted for in 41 native decisions. Neither reviewed layer attaches claim-level evidence, so none is called verified. Initial listed liquid inputs total 1012 mL (1000+1+1+10); the three later additions are explicitly per liter. These statements do not establish a 1032 mL final working volume.

[
  {
    "field_path": "ingredients[0].concentration",
    "source_name": "Distilled water",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "The source specifies 1.0 L distilled water, not 1 g/L. Restore solvent volume without assigning final working-medium volume.",
    "source_original_amount": 1,
    "source_original_unit": "L"
  },
  {
    "field_path": "ingredients[1].concentration",
    "source_name": "NaCl",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 0.3,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[2].concentration",
    "source_name": "CaCl2・2H2O",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.11,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 0.11,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[3].concentration",
    "source_name": "NH4Cl",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 0.3,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[4].concentration",
    "source_name": "Resazurin",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "The source specifies 0.5 mg resazurin; the local 0.5 G_PER_L changes both unit and batch basis. Preserve the original mg batch amount.",
    "source_original_amount": 0.5,
    "source_original_unit": "mg",
    "arithmetic": "0.5 mg = 0.0005 g. The g-versus-mg numerical unit error is a factor of 1000 on the same batch basis; an exact final concentration is not established."
  },
  {
    "field_path": "ingredients[5].concentration",
    "source_name": "MgCl2・6H2O",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 0.1,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[6].concentration",
    "source_name": "Na2SO4",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Na2SO4\",\n          \"volume\": 1.42,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 1.42,
    "source_original_unit": "g"
  },
  {
    "field_path": "ingredients[7].concentration",
    "source_name": "Yeast extract (BD-Difco)",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial mixture",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Retain the literal source batch amount in the initial mixture made with 1.0 L water; the existing bare g/L statement does not establish a measured final-volume basis. Attach exact claim evidence after restoring the stage.",
    "source_original_amount": 0.2,
    "source_original_unit": "g"
  },
  {
    "field_path": "solutions[0].concentration",
    "source_name": "FeCl2 solution (see Medium [M180])",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial stock addition",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Restore the literal mL stock addition and the named source-specific stock definition. Existing g/L is a mass-concentration claim, not a stock dose; do not treat the dose as a final concentration.",
    "source_original_amount": 1,
    "source_original_unit": "ml"
  },
  {
    "field_path": "solutions[1].concentration",
    "source_name": "Trace element solution (see Medium [M180])",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial stock addition",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Restore the literal mL stock addition and the named source-specific stock definition. Existing g/L is a mass-concentration claim, not a stock dose; do not treat the dose as a final concentration.",
    "source_original_amount": 1,
    "source_original_unit": "ml"
  },
  {
    "field_path": "solutions[2].concentration",
    "source_name": "Trace vitamins (see Medium [M190])",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "initial stock addition",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Restore the literal mL stock addition and the named source-specific stock definition. Existing g/L is a mass-concentration claim, not a stock dose; do not treat the dose as a final concentration.",
    "source_original_amount": 10,
    "source_original_unit": "ml"
  },
  {
    "field_path": "ingredients[8].concentration",
    "source_name": "Carbon dioxide gas",
    "decision": "not_quantified",
    "layer_decisions": {
      "target": "not_quantified",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "not_quantified"
    },
    "source_stage": "initial gas atmosphere",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Gas amounts are not quantified. VARIABLE may retain that absence, but attach the specified N2/CO2 ratio and source preparation context separately; do not invent a gas volume or dissolved concentration."
  },
  {
    "field_path": "ingredients[9].concentration",
    "source_name": "Nitrogen gas",
    "decision": "not_quantified",
    "layer_decisions": {
      "target": "not_quantified",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "not_quantified"
    },
    "source_stage": "initial gas atmosphere",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Gas amounts are not quantified. VARIABLE may retain that absence, but attach the specified N2/CO2 ratio and source preparation context separately; do not invent a gas volume or dissolved concentration."
  },
  {
    "field_path": "solutions[3].concentration and stock strength",
    "source_name": "1 M Glycerin solution",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "after cooling; separately sterilized additions per liter",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"1 M Glycerin solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Preserve the source stock strength, original dose and explicit per-liter receiving-batch instruction. The local g/L dose is dimensionally wrong. The 5% cysteine stock has no separately stated percentage convention; preserve literal 5% without silently deriving w/v, molarity or a final cysteine concentration.",
    "source_original_amount": 5,
    "source_original_unit": "ml",
    "source_strength": 1,
    "source_strength_unit": "M",
    "arithmetic": "For a 1 M stock, 5 mL contains 5 mmol; that is the added amount per source liter, not an independently measured final 5 mM concentration."
  },
  {
    "field_path": "solutions[4].concentration and stock strength",
    "source_name": "1 M K2HPO4 solution",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "after cooling; separately sterilized additions per liter",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"1 M K2HPO4 solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Preserve the source stock strength, original dose and explicit per-liter receiving-batch instruction. The local g/L dose is dimensionally wrong. The 5% cysteine stock has no separately stated percentage convention; preserve literal 5% without silently deriving w/v, molarity or a final cysteine concentration.",
    "source_original_amount": 5,
    "source_original_unit": "ml",
    "source_strength": 1,
    "source_strength_unit": "M",
    "arithmetic": "For a 1 M stock, 5 mL contains 5 mmol; that is the added amount per source liter, not an independently measured final 5 mM concentration."
  },
  {
    "field_path": "solutions[5].concentration and stock strength",
    "source_name": "5% L--Cysteine・HCl・H2O solution",
    "decision": "correct",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "correct"
    },
    "source_stage": "after cooling; separately sterilized additions per liter",
    "primary_source_evidence_id": "jcm1065",
    "source_snippets": [
      {
        "source_key": "togoM1134",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"5% L--Cysteine・HCl・H2O solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764"
      }
    ],
    "explanation": "Preserve the source stock strength, original dose and explicit per-liter receiving-batch instruction. The local g/L dose is dimensionally wrong. The 5% cysteine stock has no separately stated percentage convention; preserve literal 5% without silently deriving w/v, molarity or a final cysteine concentration.",
    "source_original_amount": 10,
    "source_original_unit": "ml",
    "source_strength": 5,
    "source_strength_unit": "%"
  },
  {
    "field_path": "solutions[0].composition[source row 0]",
    "source_name": "25% HCl (7.7 M)",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "FeCl2 stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume. The acid reagent is explicitly 25% HCl (7.7 M), dosed 10 mL; preserve both source strength descriptors without guessing density or a percentage convention.",
    "source_original_amount": 10,
    "source_original_unit": "ml",
    "source_strength": 25,
    "source_strength_unit": "%"
  },
  {
    "field_path": "solutions[0].composition[source row 1]",
    "source_name": "Distilled water",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "FeCl2 stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 990,
    "source_original_unit": "ml"
  },
  {
    "field_path": "solutions[0].composition[source row 2]",
    "source_name": "FeCl2・4H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "FeCl2 stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 1.5,
    "source_original_unit": "g"
  },
  {
    "field_path": "solutions[1].composition[source row 0]",
    "source_name": "Distilled water",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 1,
    "source_original_unit": "L"
  },
  {
    "field_path": "solutions[1].composition[source row 1]",
    "source_name": "Na2MoO4・2H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 36,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 2]",
    "source_name": "H3BO3",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 6,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 3]",
    "source_name": "MnCl2・4H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 100,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 4]",
    "source_name": "CoCl2・6H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 190,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 5]",
    "source_name": "NiCl2・6H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 24,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 6]",
    "source_name": "CuCl2・2H2O",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 2,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[1].composition[source row 7]",
    "source_name": "ZnCl2",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-element stock batch",
    "primary_source_evidence_id": "jcm187",
    "source_snippets": [
      {
        "source_key": "togoM180",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 70,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 0]",
    "source_name": "Distilled water",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 1,
    "source_original_unit": "L"
  },
  {
    "field_path": "solutions[2].composition[source row 1]",
    "source_name": "Biotin",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 2,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 2]",
    "source_name": "p--Aminobenzoic acid",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 3]",
    "source_name": "Thiamine・HCl",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 4]",
    "source_name": "Calcium pantothenate",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 5]",
    "source_name": "Pyridoxine・HCl",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 10,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 6]",
    "source_name": "Folic acid",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 2,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 7]",
    "source_name": "Vitamin B12",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 0.1,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 8]",
    "source_name": "Riboflavin",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 9]",
    "source_name": "Nicotinic acid",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "solutions[2].composition[source row 10]",
    "source_name": "Lipoic acid",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "trace-vitamin stock batch",
    "primary_source_evidence_id": "jcm197",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "explanation": "Add this exact source stock component, original amount/unit and supplied form to the correct stock scope, with claim-level evidence. The stock batch amount is not a direct receiving-medium ingredient concentration; water is a listed solvent volume, not proof of a measured final volume.",
    "source_original_amount": 5,
    "source_original_unit": "mg"
  },
  {
    "field_path": "preparation_steps.initial_gas_ratio",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "initial bubbling and sealed autoclaving",
    "source_snippets": [
      {
        "source_key": "jcm1065",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065",
        "source_locator": "JCM1065 first preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47",
        "parsed_text_sha256": "f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1"
      }
    ],
    "explanation": "Recover 80:20 by volume as a gas-mixture ratio, not concentrations or a total gas dose. Later separately autoclaved stocks use an N2 atmosphere; no purity percentage is asserted."
  },
  {
    "field_path": "preparation_steps.autoclave_temperature",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "source autoclaving operations absent an explicit exception",
    "source_snippets": [
      {
        "source_key": "jcm1065",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065",
        "source_locator": "Collection page general sterilization header",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47",
        "parsed_text_sha256": "f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1"
      }
    ],
    "explanation": "Recover the source default 121°C with its stated conditional scope; it is not an incubation temperature."
  },
  {
    "field_path": "preparation_steps.autoclave_duration",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml": "add"
    },
    "source_stage": "source autoclaving operations absent an explicit exception",
    "source_snippets": [
      {
        "source_key": "jcm1065",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065",
        "source_locator": "Collection page general sterilization header",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47",
        "parsed_text_sha256": "f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1"
      }
    ],
    "explanation": "Recover the source default 15 min with its stated conditional scope; do not transfer unrelated parent-medium procedures."
  }
]

### Referenced stock definitions and source-version boundaries

completeness: concern. Targets: CultureMech:007656.

The FeCl2 stock has 10 mL 25% HCl (7.7 M), 1.5 g FeCl2·4H2O and 990 mL water. The trace stock has seven solutes plus 1 L water; the vitamin stock has ten solutes plus 1 L water. All are absent from the local empty compositions. Preserve the three later reagent strengths (1 M glycerin, 1 M K2HPO4, literal 5% L-cysteine hydrochloride monohydrate). JCM197 describes filter-sterilizing vitamins in its own parent procedure; JCM1065 instead includes vitamins among its initial mixed components. Do not silently transplant the JCM197 parent sequence into JCM1065 or claim the two procedures are identical.

### All supplied forms and unasserted stock identities

grounding: supported. Targets: CultureMech:007656.

The direct hydrated CaCl2 and MgCl2 terms correspond to the explicit dihydrate and hexahydrate. Neutral resazurin matches the unsuffixed source name; no sodium-resazurin substitution is justified. Named stocks retain FeCl2 tetrahydrate and Co/Ni chloride hexahydrates, not anhydrous masses. No stock-composition IDs are asserted in this target: do not import unrelated helper-record mappings, assign stereochemistry to generic calcium pantothenate/lipoic acid, or invent replacements. Yeast extract remains a source-branded mixture.

### Anaerobic sequencing and source default sterilization

completeness: concern. Targets: CultureMech:007656.

Both layers omit the entire preparation procedure: mix and bubble with N2/CO2 80:20 v/v, stopper, autoclave under the same gas, then cool and add the three separately N2-autoclaved stocks aseptically and anaerobically per liter. The exact JCM page gives a conditional 121°C/15 min default. No medium pH, incubation temperature/time or organism growth optimum is supplied by this exact recipe; do not borrow JCM187 or JCM197 parent conditions.

### Mixture and physical-state classifications

scope: supported. Targets: CultureMech:007656.

Yeast extract is a compositionally complex component alongside specified salts and named stocks, supporting COMPLEX/SEMI_DEFINED. LIQUID is consistent with the complete no-agar source. These classifications do not validate erroneous units or source completeness.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:007656.

9 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 9/10 primary and 5/10 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007656.

23 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained-owner and generated correspondence

provenance: supported. Targets: CultureMech:007656.

The entire maintained source and generated target agree on the reviewed formulation, stock references and classifications. The merge event identifies the owner; later generated metadata does not provide independent recipe evidence. Current collection captures corroborate source identity but do not authenticate every historical import/enrichment assertion.

### Growth claims, organism identifiers and literature scope

scope: supported. Targets: CultureMech:007656.

The source title and generic cultivation application do not establish strain-level growth. Neither reviewed layer asserts a target-organism identifier, genome accession, DOI/PMID, incubation optimum or quantitative growth result. No such claim is added. Bacterial placement is consistent with source identity; this is a recipe review, not an exhaustive organism or literature search.

## Findings

### f1: Water, resazurin and every stock dose have wrong dimensions

blocker / open / confirmed; issue key: m1134-amount-units-and-basis.

The source 1 L water and six mL stock additions are represented as g/L, and 0.5 mg resazurin becomes 0.5 g/L. Other source batch masses are presented without a defensible final-volume basis. This is an unusable formulation, not a cosmetic unit-label problem; a blind reimport or unit relabel cannot establish final concentrations.

### f2: Six stock placeholders do not preserve the source formulation

major / open / confirmed; issue key: m1134-stock-definitions.

Three referenced stocks have empty composition despite accessible exact definitions, and three reagent stocks lack structured strength/composition context. Unknown solution names and top-level source notes do not preserve the needed stock quantities or claim-level evidence.

### f3: The source anaerobic and separate sterilization sequence is absent

major / open / confirmed; issue key: m1134-anaerobic-preparation.

Missing gas ratio, sealed initial sterilization, cooling, and separately sterilized later stocks materially prevent reproducible reconstruction. This also omits the collection default autoclave temperature/time. The accessible exact source supplies the sequence; no generic cycle or borrowed parent-medium pH is needed.

## Recommended Actions And Acceptance Checks

### a1

Restore source batch quantities, liquid stock doses, explicit strengths and staged per-liter addition context in the maintained owner. Attach exact evidence to every quantity; calculate any proposed final concentration only on an independently justified basis. Regenerate only after owner correction and verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve only the named FeCl2, trace-element and vitamin sections, restore stock-specific composition/evidence and meaningful names, and represent later reagent strengths without inventing percentage basis. Preserve exact supplied forms and distinguish stock preparation from the receiving recipe; do not copy whole parent media or their pH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add the exact JCM1065 ordered procedure and conditional default with literal excerpts. Retain the source-specific treatment of initial vitamins and later stock additions; do not substitute JCM197 parent-medium filtering/order without an explicitly sourced reconciliation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/165/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/165/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml:1:id: CultureMech:007656<br>./data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml:1:id: CultureMech:007656<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/165/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 44 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| jcm1065 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065; Complete JCM1065 formulation, general sterilization header and ordered procedure | supports | Exact original medium; all initial amounts and three later per-liter stock additions compared. |
| togoM1134 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134; Source identity; components[0:2]; comments | supports | Structured provider corroborates the exact source and preserves original units and stock strengths. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; FeCl2 solution and Trace element solution sections only | supports | Only the two explicitly referenced stock definitions support this medium; the parent medium and its pH/growth/preparation claims are excluded. |
| togoM180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; components[1] FeCl2 solution; components[2] trace elements | supports | Structured representations of the two JCM187 stock definitions, not the whole M180 recipe. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins section only; surrounding preparation retained as distinct context | supports | Ten vitamin components and water support the named stock. Other medium ingredients, mineral stock and pH are excluded. |
| togoM190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; components[1] trace vitamins only | supports | Structured vitamin stock; unrelated main and mineral sections are excluded. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/165/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 12, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml", "events": 11, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code distinguishes primary and local stock sections and retains source comments. Its bare g/mg/ml mappings are concentration-shaped and still require a justified batch basis. The migration helper creates empty cross-reference stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier entries; it copies existing amounts without scientific reconciliation. These current functions explain relevant failure modes but do not establish an exact historical replay. Single-owner merge correspondence does not independently verify science; correct the maintained owner and inspect source-specific writer behavior before regeneration. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code distinguishes primary and local stock sections and retains source comments. Its bare g/mg/ml mappings are concentration-shaped and still require a justified batch basis. The migration helper creates empty cross-reference stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier entries; it copies existing amounts without scientific reconciliation. These current functions explain relevant failure modes but do not establish an exact historical replay. Single-owner merge correspondence does not independently verify science; correct the maintained owner and inspect source-specific writer behavior before regeneration. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code distinguishes primary and local stock sections and retains source comments. Its bare g/mg/ml mappings are concentration-shaped and still require a justified batch basis. The migration helper creates empty cross-reference stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier entries; it copies existing amounts without scientific reconciliation. These current functions explain relevant failure modes but do not establish an exact historical replay. Single-owner merge correspondence does not independently verify science; correct the maintained owner and inspect source-specific writer behavior before regeneration. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code distinguishes primary and local stock sections and retains source comments. Its bare g/mg/ml mappings are concentration-shaped and still require a justified batch basis. The migration helper creates empty cross-reference stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier entries; it copies existing amounts without scientific reconciliation. These current functions explain relevant failure modes but do not establish an exact historical replay. Single-owner merge correspondence does not independently verify science; correct the maintained owner and inspect source-specific writer behavior before regeneration. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Source liquid additions and provider-declared stock volumes are not independently measured final working-medium volumes. No unqualified final g/L or molarity is inferred from sums of listed water/stock inputs.
- Contextual stock/helper records are inspected to resolve this target; their separate defects, provenance and unrelated medium sections are not blanket approvals or additional reviewed targets.
- The schema/term passes and exact pinned MIM label-index correspondence establish bounded metadata support, not experimental validation or proof of historical secondary-mapping methodology.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105524Z-culturemech-007656-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidified_mpob_medium (CultureMech:007656)'
started_at: '2026-10-21T10:48:44Z'
finished_at: '2026-10-21T10:55:24Z'
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
summary: The exact JCM1065/TOGO M1134 identity is supported, but both local layers
  misstate water, resazurin and all six stock doses, omit the referenced stock definitions,
  and lose the source anaerobic preparation sequence. The recipe is not scientifically
  usable as represented despite four passing diagnostics.
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
  - path: data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
    sha256: 51795ba2ff3df0a9328449061e152cb3163a79e53f632e4f9e84f293232cad7e
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
    sha256: 0092f2c05f396df1547be23467867a55f7a6e4e155fedb40abbf429908dfd32c
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_methanogen_stock_boundaries.py
    sha256: 8d4d32c7dc3cb2586242a188f958087482df3aff553d1dbc468c422eddb037ba
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
  selection: Task review 165; batch 017 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007656
targets:
- target_id: CultureMech:007656
  path: data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  label: acidified_mpob_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/165/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/165/strict.tsv"
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007656
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
  - CultureMech:007656
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:24.313881Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/165/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:25.610399Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/165/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:26.928254Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:27.769149Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:55:23Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml:1:id: CultureMech:007656

    ./data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml:1:id: CultureMech:007656

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/165/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:55:23Z'
  support: supports
  summary: 44 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: b46ebe41abb7c1b277b02a54280e7aed2967dadf0773956c45890eeb7cec2b1b
- evidence_id: jcm1065
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065
  locator: Complete JCM1065 formulation, general sterilization header and ordered
    procedure
  accessed_at: '2026-10-21T10:33:40.856863Z'
  support: supports
  summary: Exact original medium; all initial amounts and three later per-liter stock
    additions compared.
  snapshot_sha256: 4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47
- evidence_id: togoM1134
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134
  locator: Source identity; components[0:2]; comments
  accessed_at: '2026-10-21T10:33:39.169302Z'
  support: supports
  summary: Structured provider corroborates the exact source and preserves original
    units and stock strengths.
  snapshot_sha256: 057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: FeCl2 solution and Trace element solution sections only
  accessed_at: '2026-10-21T10:33:40.897866Z'
  support: supports
  summary: Only the two explicitly referenced stock definitions support this medium;
    the parent medium and its pH/growth/preparation claims are excluded.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: togoM180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: components[1] FeCl2 solution; components[2] trace elements
  accessed_at: '2026-10-21T10:33:39.509384Z'
  support: supports
  summary: Structured representations of the two JCM187 stock definitions, not the
    whole M180 recipe.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins section only; surrounding preparation retained as distinct
    context
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Ten vitamin components and water support the named stock. Other medium
    ingredients, mineral stock and pH are excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: togoM190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: components[1] trace vitamins only
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: Structured vitamin stock; unrelated main and mineral sections are excluded.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/165/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4209ff9b366410d3097aab1701bead04656a6489c1444372cbf4fbb7f76ef50c
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
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
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
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T10:55:23Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: '[{"input": "target", "events": 12, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml", "events":
    11, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Current TOGO code distinguishes primary and local stock sections and retains
    source comments. Its bare g/mg/ml mappings are concentration-shaped and still
    require a justified batch basis. The migration helper creates empty cross-reference
    stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier
    entries; it copies existing amounts without scientific reconciliation. These current
    functions explain relevant failure modes but do not establish an exact historical
    replay. Single-owner merge correspondence does not independently verify science;
    correct the maintained owner and inspect source-specific writer behavior before
    regeneration.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Current TOGO code distinguishes primary and local stock sections and retains
    source comments. Its bare g/mg/ml mappings are concentration-shaped and still
    require a justified batch basis. The migration helper creates empty cross-reference
    stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier
    entries; it copies existing amounts without scientific reconciliation. These current
    functions explain relevant failure modes but do not establish an exact historical
    replay. Single-owner merge correspondence does not independently verify science;
    correct the maintained owner and inspect source-specific writer behavior before
    regeneration.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Current TOGO code distinguishes primary and local stock sections and retains
    source comments. Its bare g/mg/ml mappings are concentration-shaped and still
    require a justified batch basis. The migration helper creates empty cross-reference
    stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier
    entries; it copies existing amounts without scientific reconciliation. These current
    functions explain relevant failure modes but do not establish an exact historical
    replay. Single-owner merge correspondence does not independently verify science;
    correct the maintained owner and inspect source-specific writer behavior before
    regeneration.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:55:23Z'
  support: context_only
  summary: Current TOGO code distinguishes primary and local stock sections and retains
    source comments. Its bare g/mg/ml mappings are concentration-shaped and still
    require a justified batch basis. The migration helper creates empty cross-reference
    stubs and a name-to-ID dictionary whose repeated generic names overwrite earlier
    entries; it copies existing amounts without scientific reconciliation. These current
    functions explain relevant failure modes but do not establish an exact historical
    replay. Single-owner merge correspondence does not independently verify science;
    correct the maintained owner and inspect source-specific writer behavior before
    regeneration.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source and cross-reference identity
  outcome: supported
  summary: TOGO M1134 explicitly identifies JCM1065. M180 resolves to JCM187 for FeCl2
    and trace elements; M190 resolves to JCM197 for trace vitamins. Their whole parent
    media are not additions to this recipe. The six local stock names retain useful
    source qualifiers but name=Unknown solution and empty compositions are not resolved
    stock definitions.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - togoM1134
  - jcm187
  - togoM180
  - jcm197
  - togoM190
- assessment_id: quantities
  area: quantity
  topic: Every current amount and source-only stock/preparation quantity
  outcome: concern
  summary: All ten direct ingredient quantities, six stock doses/strengths, twenty-two
    referenced stock components and three numeric preparation contexts are accounted
    for in 41 native decisions. Neither reviewed layer attaches claim-level evidence,
    so none is called verified. Initial listed liquid inputs total 1012 mL (1000+1+1+10);
    the three later additions are explicitly per liter. These statements do not establish
    a 1032 mL final working volume.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - quantity-inventory
  - owner-0
  details: "[\n  {\n    \"field_path\": \"ingredients[0].concentration\",\n    \"\
    source_name\": \"Distilled water\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"The source specifies 1.0 L distilled\
    \ water, not 1 g/L. Restore solvent volume without assigning final working-medium\
    \ volume.\",\n    \"source_original_amount\": 1,\n    \"source_original_unit\"\
    : \"L\"\n  },\n  {\n    \"field_path\": \"ingredients[1].concentration\",\n  \
    \  \"source_name\": \"NaCl\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 0.3,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the literal source batch amount\
    \ in the initial mixture made with 1.0 L water; the existing bare g/L statement\
    \ does not establish a measured final-volume basis. Attach exact claim evidence\
    \ after restoring the stage.\",\n    \"source_original_amount\": 0.3,\n    \"\
    source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"source_name\": \"CaCl2・2H2O\",\n    \"decision\": \"correct\",\n    \"\
    layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.11,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the literal source batch amount\
    \ in the initial mixture made with 1.0 L water; the existing bare g/L statement\
    \ does not establish a measured final-volume basis. Attach exact claim evidence\
    \ after restoring the stage.\",\n    \"source_original_amount\": 0.11,\n    \"\
    source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"source_name\": \"NH4Cl\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the literal source batch amount\
    \ in the initial mixture made with 1.0 L water; the existing bare g/L statement\
    \ does not establish a measured final-volume basis. Attach exact claim evidence\
    \ after restoring the stage.\",\n    \"source_original_amount\": 0.3,\n    \"\
    source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"source_name\": \"Resazurin\",\n    \"decision\": \"correct\",\n    \"\
    layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"The source specifies 0.5 mg resazurin;\
    \ the local 0.5 G_PER_L changes both unit and batch basis. Preserve the original\
    \ mg batch amount.\",\n    \"source_original_amount\": 0.5,\n    \"source_original_unit\"\
    : \"mg\",\n    \"arithmetic\": \"0.5 mg = 0.0005 g. The g-versus-mg numerical\
    \ unit error is a factor of 1000 on the same batch basis; an exact final concentration\
    \ is not established.\"\n  },\n  {\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"source_name\": \"MgCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"\
    layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the literal source batch amount\
    \ in the initial mixture made with 1.0 L water; the existing bare g/L statement\
    \ does not establish a measured final-volume basis. Attach exact claim evidence\
    \ after restoring the stage.\",\n    \"source_original_amount\": 0.1,\n    \"\
    source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"source_name\": \"Na2SO4\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SO4\\\",\\n          \\\"volume\\\": 1.42,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the literal source batch amount\
    \ in the initial mixture made with 1.0 L water; the existing bare g/L statement\
    \ does not establish a measured final-volume basis. Attach exact claim evidence\
    \ after restoring the stage.\",\n    \"source_original_amount\": 1.42,\n    \"\
    source_original_unit\": \"g\"\n  },\n  {\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"source_name\": \"Yeast extract (BD-Difco)\",\n    \"decision\": \"correct\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial mixture\",\n    \"primary_source_evidence_id\"\
    : \"jcm1065\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 0.2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\n     \
    \ }\n    ],\n    \"explanation\": \"Retain the literal source batch amount in\
    \ the initial mixture made with 1.0 L water; the existing bare g/L statement does\
    \ not establish a measured final-volume basis. Attach exact claim evidence after\
    \ restoring the stage.\",\n    \"source_original_amount\": 0.2,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"solutions[0].concentration\",\n    \"\
    source_name\": \"FeCl2 solution (see Medium [M180])\",\n    \"decision\": \"correct\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial stock addition\",\n   \
    \ \"primary_source_evidence_id\": \"jcm1065\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2 solution (see Medium [M180])\\\",\\n   \
    \       \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Restore the literal mL stock addition\
    \ and the named source-specific stock definition. Existing g/L is a mass-concentration\
    \ claim, not a stock dose; do not treat the dose as a final concentration.\",\n\
    \    \"source_original_amount\": 1,\n    \"source_original_unit\": \"ml\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[1].concentration\",\n    \"source_name\"\
    : \"Trace element solution (see Medium [M180])\",\n    \"decision\": \"correct\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial stock addition\",\n   \
    \ \"primary_source_evidence_id\": \"jcm1065\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M180])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Restore the literal mL stock addition\
    \ and the named source-specific stock definition. Existing g/L is a mass-concentration\
    \ claim, not a stock dose; do not treat the dose as a final concentration.\",\n\
    \    \"source_original_amount\": 1,\n    \"source_original_unit\": \"ml\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[2].concentration\",\n    \"source_name\"\
    : \"Trace vitamins (see Medium [M190])\",\n    \"decision\": \"correct\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"initial stock addition\",\n   \
    \ \"primary_source_evidence_id\": \"jcm1065\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"togoM1134\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Restore the literal mL stock addition\
    \ and the named source-specific stock definition. Existing g/L is a mass-concentration\
    \ claim, not a stock dose; do not treat the dose as a final concentration.\",\n\
    \    \"source_original_amount\": 10,\n    \"source_original_unit\": \"ml\"\n \
    \ },\n  {\n    \"field_path\": \"ingredients[8].concentration\",\n    \"source_name\"\
    : \"Carbon dioxide gas\",\n    \"decision\": \"not_quantified\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"not_quantified\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"not_quantified\"\n    },\n    \"source_stage\": \"initial gas atmosphere\"\
    ,\n    \"primary_source_evidence_id\": \"jcm1065\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1134\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\",\n\
    \        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\n     \
    \ }\n    ],\n    \"explanation\": \"Gas amounts are not quantified. VARIABLE may\
    \ retain that absence, but attach the specified N2/CO2 ratio and source preparation\
    \ context separately; do not invent a gas volume or dissolved concentration.\"\
    \n  },\n  {\n    \"field_path\": \"ingredients[9].concentration\",\n    \"source_name\"\
    : \"Nitrogen gas\",\n    \"decision\": \"not_quantified\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"not_quantified\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"not_quantified\"\n    },\n    \"source_stage\": \"initial gas atmosphere\"\
    ,\n    \"primary_source_evidence_id\": \"jcm1065\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1134\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\",\n\
    \        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\n     \
    \ }\n    ],\n    \"explanation\": \"Gas amounts are not quantified. VARIABLE may\
    \ retain that absence, but attach the specified N2/CO2 ratio and source preparation\
    \ context separately; do not invent a gas volume or dissolved concentration.\"\
    \n  },\n  {\n    \"field_path\": \"solutions[3].concentration and stock strength\"\
    ,\n    \"source_name\": \"1 M Glycerin solution\",\n    \"decision\": \"correct\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"after cooling; separately sterilized\
    \ additions per liter\",\n    \"primary_source_evidence_id\": \"jcm1065\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1134\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1 M Glycerin solution\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the source stock strength,\
    \ original dose and explicit per-liter receiving-batch instruction. The local\
    \ g/L dose is dimensionally wrong. The 5% cysteine stock has no separately stated\
    \ percentage convention; preserve literal 5% without silently deriving w/v, molarity\
    \ or a final cysteine concentration.\",\n    \"source_original_amount\": 5,\n\
    \    \"source_original_unit\": \"ml\",\n    \"source_strength\": 1,\n    \"source_strength_unit\"\
    : \"M\",\n    \"arithmetic\": \"For a 1 M stock, 5 mL contains 5 mmol; that is\
    \ the added amount per source liter, not an independently measured final 5 mM\
    \ concentration.\"\n  },\n  {\n    \"field_path\": \"solutions[4].concentration\
    \ and stock strength\",\n    \"source_name\": \"1 M K2HPO4 solution\",\n    \"\
    decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\": \"correct\"\
    ,\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"after cooling; separately sterilized\
    \ additions per liter\",\n    \"primary_source_evidence_id\": \"jcm1065\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1134\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1 M K2HPO4 solution\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\": \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the source stock strength,\
    \ original dose and explicit per-liter receiving-batch instruction. The local\
    \ g/L dose is dimensionally wrong. The 5% cysteine stock has no separately stated\
    \ percentage convention; preserve literal 5% without silently deriving w/v, molarity\
    \ or a final cysteine concentration.\",\n    \"source_original_amount\": 5,\n\
    \    \"source_original_unit\": \"ml\",\n    \"source_strength\": 1,\n    \"source_strength_unit\"\
    : \"M\",\n    \"arithmetic\": \"For a 1 M stock, 5 mL contains 5 mmol; that is\
    \ the added amount per source liter, not an independently measured final 5 mM\
    \ concentration.\"\n  },\n  {\n    \"field_path\": \"solutions[5].concentration\
    \ and stock strength\",\n    \"source_name\": \"5% L--Cysteine・HCl・H2O solution\"\
    ,\n    \"decision\": \"correct\",\n    \"layer_decisions\": {\n      \"target\"\
    : \"correct\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"correct\"\n    },\n    \"source_stage\": \"after cooling; separately sterilized\
    \ additions per liter\",\n    \"primary_source_evidence_id\": \"jcm1065\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1134\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1134\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% L--Cysteine・HCl・H2O solution\\\",\\n      \
    \    \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"\
    conc_value\\\": 5,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"057a63a5dcca5def074e42c8aa5dbcbf6ec86db4729deda20fbea5f137fc5764\"\n     \
    \ }\n    ],\n    \"explanation\": \"Preserve the source stock strength, original\
    \ dose and explicit per-liter receiving-batch instruction. The local g/L dose\
    \ is dimensionally wrong. The 5% cysteine stock has no separately stated percentage\
    \ convention; preserve literal 5% without silently deriving w/v, molarity or a\
    \ final cysteine concentration.\",\n    \"source_original_amount\": 10,\n    \"\
    source_original_unit\": \"ml\",\n    \"source_strength\": 5,\n    \"source_strength_unit\"\
    : \"%\"\n  },\n  {\n    \"field_path\": \"solutions[0].composition[source row\
    \ 0]\",\n    \"source_name\": \"25% HCl (7.7 M)\",\n    \"decision\": \"add\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"FeCl2 stock batch\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl (7.7 M)\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume. The acid reagent is explicitly 25% HCl (7.7 M), dosed 10 mL; preserve\
    \ both source strength descriptors without guessing density or a percentage convention.\"\
    ,\n    \"source_original_amount\": 10,\n    \"source_original_unit\": \"ml\",\n\
    \    \"source_strength\": 25,\n    \"source_strength_unit\": \"%\"\n  },\n  {\n\
    \    \"field_path\": \"solutions[0].composition[source row 1]\",\n    \"source_name\"\
    : \"Distilled water\",\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n\
    \      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"FeCl2 stock batch\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 990,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 990,\n    \"source_original_unit\": \"ml\"\n\
    \  },\n  {\n    \"field_path\": \"solutions[0].composition[source row 2]\",\n\
    \    \"source_name\": \"FeCl2・4H2O\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"FeCl2 stock batch\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2・4H2O\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 1.5,\n    \"source_original_unit\"\
    : \"g\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 0]\",\n    \"source_name\": \"Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 1,\n    \"source_original_unit\"\
    : \"L\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 1]\",\n    \"source_name\": \"Na2MoO4・2H2O\",\n    \"decision\": \"add\",\n\
    \    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 36,\n    \"source_original_unit\": \"mg\"\n \
    \ },\n  {\n    \"field_path\": \"solutions[1].composition[source row 2]\",\n \
    \   \"source_name\": \"H3BO3\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 6,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 3]\",\n    \"source_name\": \"MnCl2・4H2O\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 100,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 4]\",\n    \"source_name\": \"CoCl2・6H2O\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 190,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 5]\",\n    \"source_name\": \"NiCl2・6H2O\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 24,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 6]\",\n    \"source_name\": \"CuCl2・2H2O\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 2,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[1].composition[source row\
    \ 7]\",\n    \"source_name\": \"ZnCl2\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-element stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM180\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 70,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 70,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 0]\",\n    \"source_name\": \"Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 1,\n    \"source_original_unit\"\
    : \"L\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 1]\",\n    \"source_name\": \"Biotin\",\n    \"decision\": \"add\",\n    \"\
    layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 2,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 2]\",\n    \"source_name\": \"p--Aminobenzoic acid\",\n    \"decision\": \"\
    add\",\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 5,\n    \"source_original_unit\": \"mg\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[2].composition[source row 3]\",\n    \"\
    source_name\": \"Thiamine・HCl\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 5,\n    \"source_original_unit\": \"mg\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[2].composition[source row 4]\",\n    \"\
    source_name\": \"Calcium pantothenate\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 5,\n    \"source_original_unit\": \"mg\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[2].composition[source row 5]\",\n    \"\
    source_name\": \"Pyridoxine・HCl\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 10,\n    \"source_original_unit\": \"mg\"\n \
    \ },\n  {\n    \"field_path\": \"solutions[2].composition[source row 6]\",\n \
    \   \"source_name\": \"Folic acid\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 2,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 7]\",\n    \"source_name\": \"Vitamin B12\",\n    \"decision\": \"add\",\n \
    \   \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 0.1,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 8]\",\n    \"source_name\": \"Riboflavin\",\n    \"decision\": \"add\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 5,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"solutions[2].composition[source row\
    \ 9]\",\n    \"source_name\": \"Nicotinic acid\",\n    \"decision\": \"add\",\n\
    \    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"explanation\": \"Add this exact source stock component, original\
    \ amount/unit and supplied form to the correct stock scope, with claim-level evidence.\
    \ The stock batch amount is not a direct receiving-medium ingredient concentration;\
    \ water is a listed solvent volume, not proof of a measured final volume.\",\n\
    \    \"source_original_amount\": 5,\n    \"source_original_unit\": \"mg\"\n  },\n\
    \  {\n    \"field_path\": \"solutions[2].composition[source row 10]\",\n    \"\
    source_name\": \"Lipoic acid\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"trace-vitamin stock batch\",\n    \"\
    primary_source_evidence_id\": \"jcm197\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"explanation\": \"Add this exact source stock component,\
    \ original amount/unit and supplied form to the correct stock scope, with claim-level\
    \ evidence. The stock batch amount is not a direct receiving-medium ingredient\
    \ concentration; water is a listed solvent volume, not proof of a measured final\
    \ volume.\",\n    \"source_original_amount\": 5,\n    \"source_original_unit\"\
    : \"mg\"\n  },\n  {\n    \"field_path\": \"preparation_steps.initial_gas_ratio\"\
    ,\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"\
    add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"initial bubbling and sealed autoclaving\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1065\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065\"\
    ,\n        \"source_locator\": \"JCM1065 first preparation sentence\",\n     \
    \   \"exact_source_quote\": \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\"\
    : \"4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47\",\n    \
    \    \"parsed_text_sha256\": \"f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1\"\
    \n      }\n    ],\n    \"explanation\": \"Recover 80:20 by volume as a gas-mixture\
    \ ratio, not concentrations or a total gas dose. Later separately autoclaved stocks\
    \ use an N2 atmosphere; no purity percentage is asserted.\"\n  },\n  {\n    \"\
    field_path\": \"preparation_steps.autoclave_temperature\",\n    \"decision\":\
    \ \"add\",\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"source autoclaving operations absent\
    \ an explicit exception\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1065\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065\"\
    ,\n        \"source_locator\": \"Collection page general sterilization header\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47\"\
    ,\n        \"parsed_text_sha256\": \"f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1\"\
    \n      }\n    ],\n    \"explanation\": \"Recover the source default 121°C with\
    \ its stated conditional scope; it is not an incubation temperature.\"\n  },\n\
    \  {\n    \"field_path\": \"preparation_steps.autoclave_duration\",\n    \"decision\"\
    : \"add\",\n    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"source autoclaving operations absent\
    \ an explicit exception\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1065\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1065\"\
    ,\n        \"source_locator\": \"Collection page general sterilization header\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"4230b24811840d01043ecd1957ef84021e71f640c807229e4d59292d3e79ea47\"\
    ,\n        \"parsed_text_sha256\": \"f6c5302e0a4b4aebeaf6c268ce400388c4021821a3b4c6f6734ed2c0b8e7f0d1\"\
    \n      }\n    ],\n    \"explanation\": \"Recover the source default 15 min with\
    \ its stated conditional scope; do not transfer unrelated parent-medium procedures.\"\
    \n  }\n]"
- assessment_id: stock-scope
  area: completeness
  topic: Referenced stock definitions and source-version boundaries
  outcome: concern
  summary: The FeCl2 stock has 10 mL 25% HCl (7.7 M), 1.5 g FeCl2·4H2O and 990 mL
    water. The trace stock has seven solutes plus 1 L water; the vitamin stock has
    ten solutes plus 1 L water. All are absent from the local empty compositions.
    Preserve the three later reagent strengths (1 M glycerin, 1 M K2HPO4, literal
    5% L-cysteine hydrochloride monohydrate). JCM197 describes filter-sterilizing
    vitamins in its own parent procedure; JCM1065 instead includes vitamins among
    its initial mixed components. Do not silently transplant the JCM197 parent sequence
    into JCM1065 or claim the two procedures are identical.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - jcm187
  - jcm197
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: All supplied forms and unasserted stock identities
  outcome: supported
  summary: 'The direct hydrated CaCl2 and MgCl2 terms correspond to the explicit dihydrate
    and hexahydrate. Neutral resazurin matches the unsuffixed source name; no sodium-resazurin
    substitution is justified. Named stocks retain FeCl2 tetrahydrate and Co/Ni chloride
    hexahydrates, not anhydrous masses. No stock-composition IDs are asserted in this
    target: do not import unrelated helper-record mappings, assign stereochemistry
    to generic calcium pantothenate/lipoic acid, or invent replacements. Yeast extract
    remains a source-branded mixture.'
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - jcm187
  - jcm197
- assessment_id: preparation
  area: completeness
  topic: Anaerobic sequencing and source default sterilization
  outcome: concern
  summary: 'Both layers omit the entire preparation procedure: mix and bubble with
    N2/CO2 80:20 v/v, stopper, autoclave under the same gas, then cool and add the
    three separately N2-autoclaved stocks aseptically and anaerobically per liter.
    The exact JCM page gives a conditional 121°C/15 min default. No medium pH, incubation
    temperature/time or organism growth optimum is supplied by this exact recipe;
    do not borrow JCM187 or JCM197 parent conditions.'
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Mixture and physical-state classifications
  outcome: supported
  summary: Yeast extract is a compositionally complex component alongside specified
    salts and named stocks, supporting COMPLEX/SEMI_DEFINED. LIQUID is consistent
    with the complete no-agar source. These classifications do not validate erroneous
    units or source completeness.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - jcm1065
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '9 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 9/10 primary and 5/10 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32149
  - chebi86158
  - chebi86345
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 23 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: provenance
  topic: Maintained-owner and generated correspondence
  outcome: supported
  summary: The entire maintained source and generated target agree on the reviewed
    formulation, stock references and classifications. The merge event identifies
    the owner; later generated metadata does not provide independent recipe evidence.
    Current collection captures corroborate source identity but do not authenticate
    every historical import/enrichment assertion.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-0
  - writer-1
  - writer-2
  - writer-3
- assessment_id: biology
  area: scope
  topic: Growth claims, organism identifiers and literature scope
  outcome: supported
  summary: The source title and generic cultivation application do not establish strain-level
    growth. Neither reviewed layer asserts a target-organism identifier, genome accession,
    DOI/PMID, incubation optimum or quantitative growth result. No such claim is added.
    Bacterial placement is consistent with source identity; this is a recipe review,
    not an exhaustive organism or literature search.
  target_ids:
  - CultureMech:007656
  evidence_ids:
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: m1134-amount-units-and-basis
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Water, resazurin and every stock dose have wrong dimensions
  description: The source 1 L water and six mL stock additions are represented as
    g/L, and 0.5 mg resazurin becomes 0.5 g/L. Other source batch masses are presented
    without a defensible final-volume basis. This is an unusable formulation, not
    a cosmetic unit-label problem; a blind reimport or unit relabel cannot establish
    final concentrations.
  target_ids:
  - CultureMech:007656
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - togoM1134
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
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
  issue_key: m1134-stock-definitions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Six stock placeholders do not preserve the source formulation
  description: Three referenced stocks have empty composition despite accessible exact
    definitions, and three reagent stocks lack structured strength/composition context.
    Unknown solution names and top-level source notes do not preserve the needed stock
    quantities or claim-level evidence.
  target_ids:
  - CultureMech:007656
  field_paths:
  - solutions[*].name
  - solutions[*].composition
  - solutions[*].notes
  - references
  - ingredients[*].evidence
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - jcm187
  - jcm197
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
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
  issue_key: m1134-anaerobic-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source anaerobic and separate sterilization sequence is absent
  description: Missing gas ratio, sealed initial sterilization, cooling, and separately
    sterilized later stocks materially prevent reproducible reconstruction. This also
    omits the collection default autoclave temperature/time. The accessible exact
    source supplies the sequence; no generic cycle or borrowed parent-medium pH is
    needed.
  target_ids:
  - CultureMech:007656
  field_paths:
  - preparation_steps
  - solutions[*].preparation_notes
  evidence_ids:
  - record
  - owner-0
  - jcm1065
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because omission of the atmosphere
    and separate sterilization/addition stages materially compromises reproducibility;
    P3.4 missing preparation is a related aspect of the same defect.
actions:
- action_id: a1
  description: Restore source batch quantities, liquid stock doses, explicit strengths
    and staged per-liter addition context in the maintained owner. Attach exact evidence
    to every quantity; calculate any proposed final concentration only on an independently
    justified basis. Regenerate only after owner correction and verification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
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
  description: Resolve only the named FeCl2, trace-element and vitamin sections, restore
    stock-specific composition/evidence and meaningful names, and represent later
    reagent strengths without inventing percentage basis. Preserve exact supplied
    forms and distinguish stock preparation from the receiving recipe; do not copy
    whole parent media or their pH.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
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
  description: Add the exact JCM1065 ordered procedure and conditional default with
    literal excerpts. Retain the source-specific treatment of initial vitamins and
    later stock additions; do not substitute JCM197 parent-medium filtering/order
    without an explicitly sourced reconciliation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007656
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml
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
- Source liquid additions and provider-declared stock volumes are not independently
  measured final working-medium volumes. No unqualified final g/L or molarity is inferred
  from sums of listed water/stock inputs.
- Contextual stock/helper records are inspected to resolve this target; their separate
  defects, provenance and unrelated medium sections are not blanket approvals or additional
  reviewed targets.
- The schema/term passes and exact pinned MIM label-index correspondence establish
  bounded metadata support, not experimental validation or proof of historical secondary-mapping
  methodology.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
