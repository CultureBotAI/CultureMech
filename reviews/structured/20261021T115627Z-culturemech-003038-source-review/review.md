# Source and formulation review: aerobic_sulfolobales_medium_without_sulfur (CultureMech:003038)

- Review: 20261021T115627Z-culturemech-003038-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:25Z
- Finished UTC: 2026-10-21T11:56:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The sulfur-free JCM 693 record contains the parent sulfur dose and was merged with the sulfur-containing JCM 691 formulation. The collection explicitly requires omission. All other listed amounts match the provider’s nominal stock convention, but stock hierarchy, preparation scope, chemical metadata and duplicate/path claims need curation. Required current sources and checks are available.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 187; batch 019 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003038 | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml | generated | aerobic_sulfolobales_medium_without_sulfur |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003038 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003038 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/187/strict.tsv |
| validate-terms | passed | True | CultureMech:003038 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003038 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003038 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003038.

The four documented recipes completed; interpret the scope of each separately.

### Complete primary and secondary identifier metadata

grounding: concern. Targets: CultureMech:003038.

12 distinct asserted CHEBI keys resolve to nonobsolete terms; 0 canonical-label mismatches. Exact current secondary lookup misses ['CHEBI:26833']; legacy IDs are separately bounded. These are identifier/linkage results, not source-form correctness.

{
  "scale": "0\u2013100 percent; each denominator is that layer\u2019s direct+nested ingredient-node count, not a scientific score",
  "counts": {
    "target": {
      "ingredient_nodes": 13,
      "primary_assertions": 12,
      "secondary_chebi_assertions": 11,
      "legacy_assertions": 0,
      "primary_percent": 92.3076923076923,
      "secondary_chebi_percent": 84.61538461538461,
      "verified_current_secondary_instances": 10,
      "verified_current_secondary_percent": 76.92307692307692
    },
    "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml": {
      "ingredient_nodes": 13,
      "primary_assertions": 12,
      "secondary_chebi_assertions": 11,
      "legacy_assertions": 0,
      "primary_percent": 92.3076923076923,
      "secondary_chebi_percent": 84.61538461538461,
      "verified_current_secondary_instances": 10,
      "verified_current_secondary_percent": 76.92307692307692
    },
    "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml": {
      "ingredient_nodes": 13,
      "primary_assertions": 12,
      "secondary_chebi_assertions": 11,
      "legacy_assertions": 0,
      "primary_percent": 92.3076923076923,
      "secondary_chebi_percent": 84.61538461538461,
      "verified_current_secondary_instances": 10,
      "verified_current_secondary_percent": 76.92307692307692
    }
  }
}

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003038.

37 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "name": "Yeast extract",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; Yeast extract",
        "exact_source_quote": "Yeast extract (BD-Difco) 0.5 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "Yeast 0.5 g is retained from the parent under the explicit omission-only modification. Its G_PER_L value follows the provider nominal 1000 mL basis; attach that convention and preserve the separate yeast-solution preparation. No measured final volume is inferred.",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.5 g with g_l=0.5 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[0].concentration",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "name": "Sulfur",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; Sulfur",
        "exact_source_quote": "Sulfur (powder) 1.0 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"attribute\": \"powder\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 31.1818,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "JCM 693 explicitly omits this parent ingredient. Remove the sulfur assertion from the child formulation; do not turn omission into a measured zero. The JCM 691 owner legitimately retains its source 1 g sulfur batch amount, with evidence still needed.",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 1 g with g_l=1 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[1].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "name": "(NH4)2SO4",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; (NH4)2SO4",
        "exact_source_quote": "(NH 4 ) 2 SO 4 1.3 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.3,\n                        \"mmol_l\": 9.83805,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "1.3",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 1.3 g with g_l=1.3 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[2].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "KH2PO4",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; KH2PO4",
        "exact_source_quote": "KH 2 PO 4 0.28 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.28,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.28,\n                        \"mmol_l\": 2.05752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.28",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.28 g with g_l=0.28 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[3].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "MgSO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.25 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.0143,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.25 g with g_l=0.25 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[4].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CaCl2 x 2 H2O",
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.07 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.07,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.476142,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.07 g with g_l=0.07 on declared 1000 mL basis. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[5].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "MnCl2 x 4 H2O",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl 2 ·4H 2 O 1.8 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 1.8,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0018,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.0018",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 1.8 mg with g_l=0.0018 on declared 1000 mL basis. Unit conversion: 1.8 mg × 0.001 = 0.0018 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[6].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Na2B4O7 x 10 H2O",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; Na2B4O7 x 10 H2O",
        "exact_source_quote": "Na 2 B 4 O 7 ·10H 2 O 4.5 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2B4O7 x 10 H2O\",\n                        \"compound_id\": 196,\n                        \"amount\": 4.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.0045",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 4.5 mg with g_l=0.0045 on declared 1000 mL basis. Unit conversion: 4.5 mg × 0.001 = 0.0045 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[7].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "ZnSO4 x 7 H2O",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.22 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.22,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00022,\n                        \"mmol_l\": 0.000765055,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "0.00022",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.22 mg with g_l=0.00022 on declared 1000 mL basis. Unit conversion: 0.22 mg × 0.001 = 0.00022 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[8].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CuCl2 x 2 H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CuCl2 x 2 H2O",
        "exact_source_quote": "CuCl 2 ·2H 2 O 0.05 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.05,\n                        \"unit\": \"mg\",\n                        \"g_l\": 5.0e-5,\n                        \"mmol_l\": 0.000293284,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "5e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.05 mg with g_l=5e-05 on declared 1000 mL basis. Unit conversion: 0.05 mg × 0.001 = 0.00005 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[9].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Na2MoO4 x 2 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.03 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"mg\",\n                        \"g_l\": 3.0e-5,\n                        \"mmol_l\": 0.000123993,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "3e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.03 mg with g_l=3e-05 on declared 1000 mL basis. Unit conversion: 0.03 mg × 0.001 = 0.00003 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[10].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "VOSO4 x n H2O",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; VOSO4 x n H2O",
        "exact_source_quote": "VOSO 4 · x H 2 O 0.03 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"VOSO4 x n H2O\",\n                        \"compound_id\": 1062,\n                        \"amount\": 0.03,\n                        \"unit\": \"mg\",\n                        \"g_l\": 3.0e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "3e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.03 mg with g_l=3e-05 on declared 1000 mL basis. Unit conversion: 0.03 mg × 0.001 = 0.00003 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[11].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CoSO4 x 7 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CoSO4 x 7 H2O",
        "exact_source_quote": "CoSO 4 ·7H 2 O 0.01 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.01,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1.0e-5,\n                        \"mmol_l\": 6.45178e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The numerical G_PER_L value agrees with the provider-declared salt-base concentration. Both target and owners flatten it into final ingredients without stock-dose/batch context or attached evidence. Restore source stock scope; do not change the supported stock number or silently assert a measured final-medium concentration.",
    "local": {
      "value": "1e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "Provider 0.01 mg with g_l=1e-05 on declared 1000 mL basis. Unit conversion: 0.01 mg × 0.001 = 0.00001 g. Receiving volume, stock-water amount and unquantified preparation additions remain separate.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "ingredients[12].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Receiving salt-base dose",
    "field_path": "source.salt_base.receiving_volume",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; salt-base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Salt base solution\",\n                        \"solution_id\": 4598,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The inherited source main formulation uses 1 L salt base; the dose is missing as a distinct claim in all three layers. Add this source-stage information without double-counting the eleven expanded solutes or inferring final volume."
  },
  {
    "name": "Salt-base water amount",
    "field_path": "source.salt_base.water",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt-base table; water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "Source water is 1 L within salt-base preparation. Preserve the volume, not a mass concentration, an inferred final volume or the local dependency’s 1000 PERCENT_V_V artifact."
  },
  {
    "name": "Autoclave temperature",
    "field_path": "preparation.autoclave.temperature",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 page-level default; salt base and yeast separately",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The JCM page gives the 121°C/15 min default where not otherwise stated. It supports separate salt-base/yeast autoclaving, not replacement of the parent’s sulfur-steaming exception.",
    "arithmetic": "Source literal: 121°C; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.autoclave.temperature",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.autoclave.temperature",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation.autoclave.temperature",
        "decision": "add"
      }
    ]
  },
  {
    "name": "Autoclave duration",
    "field_path": "preparation.autoclave.duration",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 page-level default; salt base and yeast separately",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The JCM page gives the 121°C/15 min default where not otherwise stated. It supports separate salt-base/yeast autoclaving, not replacement of the parent’s sulfur-steaming exception.",
    "arithmetic": "Source literal: 15 min; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.autoclave.duration",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.autoclave.duration",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation.autoclave.duration",
        "decision": "add"
      }
    ]
  },
  {
    "name": "Yeast preparation strength",
    "field_path": "preparation.yeast_solution.strength",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main preparation; percent basis not specified",
        "exact_source_quote": "Autoclave Salt base solution and yeast extract (as a 10% solution) separately and combine after cooling.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The parent explicitly retains the 10% yeast preparation. Its percentage basis and physical dose are unspecified, so do not assume w/v or calculate final dilution. The child inherits the non-sulfur procedure.",
    "arithmetic": "Source literal: 10%; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.yeast_solution.strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.yeast_solution.strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "decision": "evidence_only",
        "stored": "Autoclave Salt base solution and yeast extract (as a 10% solution) separately and combine after cooling. Steam sulfur for 3 hr on each of 3 successive days."
      }
    ]
  },
  {
    "name": "Sulfur steaming duration",
    "field_path": "preparation.sulfur_steam.duration",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 parent sulfur-specific preparation",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "This quantitative procedure belongs only to the sulfur-containing parent. Its current parent text is numerically supported but lacks attached evidence; it is not an instruction to add or steam sulfur for JCM 693.",
    "arithmetic": "Source literal: 3 hr; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.sulfur_steam.duration",
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.sulfur_steam.duration",
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "decision": "evidence_only",
        "stored": "Autoclave Salt base solution and yeast extract (as a 10% solution) separately and combine after cooling. Steam sulfur for 3 hr on each of 3 successive days."
      }
    ]
  },
  {
    "name": "Sulfur steaming repetitions",
    "field_path": "preparation.sulfur_steam.repetitions",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 parent sulfur-specific preparation",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "This quantitative procedure belongs only to the sulfur-containing parent. Its current parent text is numerically supported but lacks attached evidence; it is not an instruction to add or steam sulfur for JCM 693.",
    "arithmetic": "Source literal: 3 successive days; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.sulfur_steam.repetitions",
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.sulfur_steam.repetitions",
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "decision": "evidence_only",
        "stored": "Autoclave Salt base solution and yeast extract (as a 10% solution) separately and combine after cooling. Steam sulfur for 3 hr on each of 3 successive days."
      }
    ]
  },
  {
    "name": "Salt base pH endpoint",
    "field_path": "preparation.salt_base.pH",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution preparation",
        "exact_source_quote": "Adjust pH to 2.5 with 10 N H 2 SO 4 .",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The literal pH endpoint/acid strength appears in parent preparation but is presented without a distinct salt-base object. Restore stock scope and attach evidence; add that scoped context to the child. The endpoint is not a measured growth optimum and 10 N is not a dose.",
    "arithmetic": "Source literal: 2.5; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.salt_base.pH",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.salt_base.pH",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "decision": "correct",
        "stored": "Adjust pH to 2.5 with 10 N H2SO4."
      }
    ]
  },
  {
    "name": "Adjustment acid strength",
    "field_path": "preparation.salt_base.acid_strength",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution preparation; dose not quantified",
        "exact_source_quote": "Adjust pH to 2.5 with 10 N H 2 SO 4 .",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The literal pH endpoint/acid strength appears in parent preparation but is presented without a distinct salt-base object. Restore stock scope and attach evidence; add that scoped context to the child. The endpoint is not a measured growth optimum and 10 N is not a dose.",
    "arithmetic": "Source literal: 10 N; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.salt_base.acid_strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
        "field_path": "preparation.salt_base.acid_strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "decision": "correct",
        "stored": "Adjust pH to 2.5 with 10 N H2SO4."
      }
    ]
  },
  {
    "name": "Acid adjustment amount",
    "field_path": "source.salt_base.acid_dose",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution preparation",
        "exact_source_quote": "Adjust pH to 2.5 with 10 N H 2 SO 4 .",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm693",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693",
        "source_locator": "JCM 693 complete modification sentence",
        "exact_source_quote": "Use Medium No. 691 without sulfur.",
        "snapshot_sha256": "18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65",
        "parsed_text_sha256": "e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace"
      }
    ],
    "rationale": "The source fixes a 10 N adjustment reagent and pH endpoint but gives no addition volume. Absence of a fixed local acid number must not be replaced with an invented dose or final concentration."
  },
  {
    "name": "Parent provider pH scalar",
    "field_path": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml::ph_value",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.medium.min_pH",
        "exact_source_quote": "\"min_pH\": 2.5",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "mediadiveJ691api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J691",
        "source_locator": "$.data.medium.max_pH",
        "exact_source_quote": "\"max_pH\": 2.5",
        "snapshot_sha256": "5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution preparation",
        "exact_source_quote": "Adjust pH to 2.5 with 10 N H 2 SO 4 .",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The parent scalar 2.5 matches provider metadata. Preserve it as provider/source context with evidence, distinct from an experimentally measured final pH or growth optimum.",
    "local": 2.5,
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
        "field_path": "ph_value",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "name": "Dependency stock: (NH4)2SO4",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[0].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; (NH4)2SO4",
        "exact_source_quote": "(NH 4 ) 2 SO 4 1.3 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"(NH4)2SO4\",\n                \"compound_id\": 27,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.3,\n                \"unit\": \"g\",\n                \"g_l\": 1.3,\n                \"mmol_l\": 9.83805,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "1.3",
      "unit": "G_PER_L"
    },
    "arithmetic": "1.3 g on provider-declared 1000 mL stock basis; g_l=1.3. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[0].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: KH2PO4",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[1].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; KH2PO4",
        "exact_source_quote": "KH 2 PO 4 0.28 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"KH2PO4\",\n                \"compound_id\": 11,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.28,\n                \"unit\": \"g\",\n                \"g_l\": 0.28,\n                \"mmol_l\": 2.05752,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.28",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.28 g on provider-declared 1000 mL stock basis; g_l=0.28. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[1].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: MgSO4 x 7 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[2].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.25 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"MgSO4 x 7 H2O\",\n                \"compound_id\": 8,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.25,\n                \"unit\": \"g\",\n                \"g_l\": 0.25,\n                \"mmol_l\": 1.0143,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.25 g on provider-declared 1000 mL stock basis; g_l=0.25. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[2].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: CaCl2 x 2 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[3].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.07 g",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"CaCl2 x 2 H2O\",\n                \"compound_id\": 7,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.07,\n                \"unit\": \"g\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.476142,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.07 g on provider-declared 1000 mL stock basis; g_l=0.07. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[3].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: MnCl2 x 4 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[4].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl 2 ·4H 2 O 1.8 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.8,\n                \"unit\": \"mg\",\n                \"g_l\": 0.0018,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.0018",
      "unit": "G_PER_L"
    },
    "arithmetic": "1.8 mg on provider-declared 1000 mL stock basis; g_l=0.0018. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[4].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: Na2B4O7 x 10 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[5].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; Na2B4O7 x 10 H2O",
        "exact_source_quote": "Na 2 B 4 O 7 ·10H 2 O 4.5 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Na2B4O7 x 10 H2O\",\n                \"compound_id\": 196,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4.5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.0045,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.0045",
      "unit": "G_PER_L"
    },
    "arithmetic": "4.5 mg on provider-declared 1000 mL stock basis; g_l=0.0045. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[5].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: ZnSO4 x 7 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[6].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.22 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.22,\n                \"unit\": \"mg\",\n                \"g_l\": 0.00022,\n                \"mmol_l\": 0.000765055,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "0.00022",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.22 mg on provider-declared 1000 mL stock basis; g_l=0.00022. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[6].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: CuCl2 x 2 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[7].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; CuCl2 x 2 H2O",
        "exact_source_quote": "CuCl 2 ·2H 2 O 0.05 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.05,\n                \"unit\": \"mg\",\n                \"g_l\": 5.0e-5,\n                \"mmol_l\": 0.000293284,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "5e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.05 mg on provider-declared 1000 mL stock basis; g_l=5e-05. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[7].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: Na2MoO4 x 2 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[8].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.03 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"mg\",\n                \"g_l\": 3.0e-5,\n                \"mmol_l\": 0.000123993,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "3e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.03 mg on provider-declared 1000 mL stock basis; g_l=3e-05. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[8].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: VOSO4 x n H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[9].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; VOSO4 x n H2O",
        "exact_source_quote": "VOSO 4 · x H 2 O 0.03 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"VOSO4 x n H2O\",\n                \"compound_id\": 1062,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"mg\",\n                \"g_l\": 3.0e-5,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "3e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.03 mg on provider-declared 1000 mL stock basis; g_l=3e-05. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[9].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: CoSO4 x 7 H2O",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[10].concentration",
    "decision": "verified",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; CoSO4 x 7 H2O",
        "exact_source_quote": "CoSO 4 ·7H 2 O 0.01 mg",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[10]",
        "exact_source_quote": "{\n                \"recipe_order\": 11,\n                \"compound\": \"CoSO4 x 7 H2O\",\n                \"compound_id\": 198,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"mg\",\n                \"g_l\": 1.0e-5,\n                \"mmol_l\": 6.45178e-5,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Existing stock value/unit and attached exact evidence agree with the provider-declared stock basis. This does not verify a receiving-medium final concentration or resolve a separate chemical-form metadata conflict.",
    "local": {
      "value": "1e-05",
      "unit": "G_PER_L"
    },
    "arithmetic": "0.01 mg on provider-declared 1000 mL stock basis; g_l=1e-05. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[10].concentration",
        "decision": "verified"
      }
    ]
  },
  {
    "name": "Dependency stock: Distilled water",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[11].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "Salt base solution table; Distilled water",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[11]",
        "exact_source_quote": "{\n                \"recipe_order\": 12,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "Provider and collection give 1000 mL/1 L water for the salt-base batch. Local 1000 PERCENT_V_V is not that volume; do not inherit or use it as a measured final-volume claim.",
    "local": {
      "value": "1000",
      "unit": "PERCENT_V_V"
    },
    "arithmetic": "1000 ml on provider-declared 1000 mL stock basis; g_l=None. No receiving-medium dilution inferred.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml",
        "field_path": "composition[11].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Dependency placeholder",
    "field_path": "data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::ingredients[0]",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "solution4598",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4598",
        "source_locator": "$.data.recipe[11]",
        "exact_source_quote": "{\n                \"recipe_order\": 12,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501"
      }
    ],
    "rationale": "The file separately carries See source for composition with a VARIABLE amount despite a populated composition. This is not an additional ingredient or dose and must not be imported into the target.",
    "local": {
      "preferred_term": "See source for composition",
      "concentration": {
        "value": "variable",
        "unit": "VARIABLE"
      }
    }
  }
]

### Sulfur-free JCM 693 versus sulfur-containing JCM 691

identity: concern. Targets: CultureMech:003038.

JCM 693 explicitly requires the parent without sulfur. The target and its JCM 693 owner instead include sulfur 1 G_PER_L copied from the parent; the generated merge also treats the JCM 691 owner as a synonym/source duplicate. That changes the named formulation. Source M713’s contradictory copied sulfur-steaming comment does not override its ingredient omission or the collection instruction.

### Numerical agreement does not establish formulation identity

consistency: concern. Targets: CultureMech:003038.

The thirteen local numbers match the provider-normalized parent formula, including the sulfur that must be absent from the child. Four gram and seven milligram source salts are numerically converted consistently with the provider-declared stock basis, but stock composition, receiving dose and water/preparation scope are not represented distinctly. The inventory retains source rows, explicit omission, all owner-layer decisions and the eleven independently evidenced stock quantities.

### Inherited procedure, exceptions and missing stage detail

completeness: concern. Targets: CultureMech:003038.

The child’s single instruction accurately says without sulfur but contradicts its ingredient list and omits the inherited non-sulfur protocol. The parent retains separate autoclaving/cooling, yeast 10%, sulfur 3 hr on each of 3 days, and acid/pH text; its stock boundary remains flattened and the page-default autoclave temperature/duration are absent. Do not copy sulfur-specific preparation into the child. No yeast percentage basis, acid volume, incubation temperature or gas mixture is supplied.

### Exact source hydrates and bounded ontology conflict

grounding: concern. Targets: CultureMech:003038.

The sulfate/chloride hydrates and variable vanadyl hydrate retain explicit source forms. CHEBI:131366 has the expected canonical borax label but its captured formula 10H2O.H4B4O9.2Na and mass 417.401 differ from source Na2B4O7·10H2O. Label agreement cannot settle that structural/stoichiometric conflict. No alternate ID or molar conversion is inferred.

### Primary sulfur identity versus current secondary mapping

grounding: concern. Targets: CultureMech:003038.

CHEBI:26833 is a valid nonobsolete sulfur term and has an Elemental sulfur synonym; powder context alone does not prove a wrong primary ID or justify an allotrope replacement. Its asserted current secondary CHEBI key has no preferred_term/MAPPED row in the pinned MIM index. This completed current lookup is distinct from the unresolved historical numeric ID assessed in record186; no unavailable historical check is introduced here.

### Duplicate labels, broken paths and merged-source boundaries

scope: concern. Targets: CultureMech:003038.

The three bacterial path instances are absent from the ignored-inclusive normalized listing; their stable IDs resolve under archaea. The underlying SOURCE_DUPLICATE designation is also wrong for the collection’s explicit omission variant. Current formulation-aware merging cannot be replaced by an ingredient-set fingerprint as evidence of equality; retain source-specific stable IDs and formulation boundaries.

### Medium class, roles and biological limits

scope: supported. Targets: CultureMech:003038.

COMPLEX/UNDEFINED and LIQUID are consistent with the inherited yeast-containing liquid source. Archaea and Sulfolobales are source/title context, not claims that every taxon or strain grows in either variant. There are no asserted organisms, genome accessions, DOI/PMID, optimum or experimental growth result to verify. No new growth or pathway assertion is inferred from the name or source recipe.

### Maintained owners and current import/merge semantics

provenance: concern. Targets: CultureMech:003038.

The child history explicitly records copying thirteen parent ingredients, and the target records merging these two owners. Those historical statements explain provenance but do not justify copying an omitted ingredient. Current MediaDive code distinguishes the primary solution from referenced stock sections; current formulation merging requires compatible payloads. Neither was executed and no historical code behavior is inferred solely from current implementation.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003038.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: The sulfur-free recipe contains sulfur and is conflated with its parent

blocker / open / confirmed; issue key: culturemech.003038.sulfur-omission-lost.

The exact JCM 693 instruction and local preparation say without sulfur, yet the target and JCM 693 owner include sulfur 1 G_PER_L and the generated record merges JCM 691 as a synonym. A parent-derived numerical match is insufficient: this child must omit sulfur. The resolved_reference flag and historical copy/merge events do not validate the formulation.

### f2: Reciprocal source links use absent bacterial paths

major / open / confirmed; issue key: culturemech.003038.relationship-paths.

The target and JCM 693 owner point to bacterial/aerobic_sulfolobales_medium.yaml, while the JCM 691 owner points to bacterial/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml. All three are absent in the ignored-inclusive search; the exact stable-ID records are under archaea. The successful reference recipe reported zero checked references.

### f3: Inherited salt-base and non-sulfur preparation are incompletely represented

major / open / confirmed; issue key: culturemech.003038.stock-preparation-scope.

The eleven salt-base concentrations are flattened, the separate 1 L base dose and water basis are absent, and the child has only a parent-reference sentence. Source default autoclaving at 121°C for 15 min, separate yeast preparation/cooling, stock pH 2.5 and 10 N adjustment reagent need scoped evidence; the parent sulfur-steaming procedure must remain parent-only. This protocol impact warrants major severity for native P3.5.

### f4: Borax label agreement hides a formula conflict

major / open / confirmed; issue key: culturemech.003038.borax-structure-conflict.

The asserted CHEBI:131366 label matches the named decahydrate, but its captured structural formula 10H2O.H4B4O9.2Na and mass 417.401 differ from the collection’s Na2B4O7·10H2O. This is an unresolved source/ontology metadata conflict; the source mass and provider g/L correspondence are separate.

### f5: The current sulfur secondary key has no pinned MIM mapping

major / open / confirmed; issue key: culturemech.003038.current-mim-sulfur-gap.

CHEBI:26833 is valid as a primary term, but the asserted mediaingredientmech_chebi_term has no exact preferred_term/MAPPED entry in the complete pinned MIM index. The other ten asserted current secondary keys resolve. The current negative result is a completed lookup, not an unavailable ontology or historical numeric-ID search.

### f6: Source quantities lack attached evidence and four history instances lack timezones

minor / open / confirmed; issue key: culturemech.003038.evidence-and-history.

Target and both owners have source URLs and historical copied-from notes but no attached matching ingredient quantity excerpts. Two timezone-naive events occur in the target and are repeated in the JCM 693 owner, totaling four instances; the six JCM 691 owner timestamps are timezone-aware. History is provenance, not scientific validation.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained JCM 693 formulation to retain the explicit omission, preserve the distinct sulfur-containing JCM 691 owner and stable IDs, and replace duplicate/equivalence treatment with the supported omitted-component relationship before separately authorized regeneration. Do not encode omission as a measured zero.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Repair exact canonical owner paths and reciprocal IDs together with the scientific variant relationship. Verify all three occurrences and regenerate; do not treat a path-only fix as confirmation of SOURCE_DUPLICATE.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the exact inherited stock/dose and non-sulfur preparation context, with literal evidence and explicit unknown yeast-percent basis, acid dose and final volume. Preserve supported provider stock numbers; do not import the dependency water percentage or placeholder.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the exact supplied borax form and ontology structural discrepancy before molar use or re-grounding. Retain the source mass and avoid inventing a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Remove the sulfur row from the sulfur-free child as required by its source, and separately reconcile the sulfur-containing owner’s current secondary link using verified exact correspondence. Do not replace a valid primary term solely to increase linkage coverage.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Attach claim-level primary/provider evidence with stock/variant scope. Preserve historical event bytes and append a bounded provenance clarification when authorized; do not invent timezone offsets or rewrite old events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/187/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/187/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml:1:id: CultureMech:003038<br>./data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml:1:id: CultureMech:003038<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/187/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 20 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| source-context | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/187/evidence-context-original.json; Frozen per-record preflight; exact source fields, owner/dependency inventories and source limitations | context_only | The preflight is diagnostic context. Its literal captures and current input bytes are independently read and assessed here; no provisional coverage or source conclusion is automatically promoted. |
| jcm691 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691; Complete main table, Salt base solution table, preparation and page-level default | supports | Exact parent formulation separates 1 L salt base, 0.5 g yeast and 1 g powdered sulfur; salt base has four gram solutes, seven milligram solutes and 1 L water, with unquantified 10 N acid to pH 2.5. The global 121°C/15 min autoclave default is distinct from sulfur steaming 3 hr on each of 3 successive days. |
| jcm693 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693; Complete modification sentence and page-level default | supports | Exact sulfur-free source says to use Medium 691 without sulfur. It does not authorize adding the parent sulfur or its sulfur-specific steaming procedure. |
| togoM711 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711; meta, both component sections and all comments | supports | Provider preserves main/salt-base hierarchy, raw g/mg/L quantities and the 10 N adjustment reagent; it corroborates source identity, not an independent measured final volume. |
| togoM713 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M713; meta, main component rows and all comments | supports | Provider variant omits sulfur in its ingredient list and explicitly names the omission. Its copied parent sulfur-steaming comment is a source inconsistency, not a valid sulfur-free instruction. |
| mediadiveJ691api | https://mediadive.dsmz.de/rest/medium/J691; data.medium and complete solutions4597/4598 | supports | Provider names 1000 mL receiving base and 1000 mL stock basis; g_l values describe that declared convention, not an independently measured final medium after unquantified additions. |
| mediadiveJ693api | https://mediadive.dsmz.de/rest/medium/J693; data.medium and solution4600 steps | supports | Child is a step-only reference to 691 without sulfur; no direct recipe array is provided. That is not evidence for an empty medium or an unmodified parent. |
| solution4598 | https://mediadive.dsmz.de/rest/solution/4598; data.recipe[0:12], volume and step | supports | Exact standalone salt base, whose numeric source/evidence correspondence is assessed separately from any receiving medium. |
| chebi131366 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131366; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:131366 resolves to disodium tetraborate decahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:26833 resolves to sulfur atom. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:62946 resolves to ammonium sulfate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi87020 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_87020; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:87020 resolves to vanadyl sulfate hydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| mim-grounding | src/culturemech/data/mediaingredientmech/label_index.csv; Complete exact preferred_term/MAPPED lookup for every asserted current secondary key; adjacent source_commit/hash metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "matches": {"CHEBI:26833": [], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:87020": [{"label": "VOSO4 x n H2O", "match_type": "preferred_term", "identifier": "CHEBI:87020", "preferred_term": "VOSO4 x n H2O", "ontology_id": "CHEBI:87020", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_keys": ["CHEBI:26833"], "legacy_assertions": []} |
| chemical-metadata | /private/tmp/culturemech-review-work-batch019/187/chemical-metadata-context.json; All asserted ingredient IDs/labels, formula/CAS/mass/structure fields and per-layer linkage denominators | context_only | All source-specific identity decisions are separated from canonical metadata correspondence. |
| stock-local | data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml; Complete standalone stock YAML, twelve composition rows, eleven attached evidence objects, preparation, placeholder and history | context_only | Dependency only: eleven attached amount excerpts match the exact current provider response and limit support to provider-declared stock concentrations. Water 1000 PERCENT_V_V and the separate placeholder are not valid receiving-medium instructions. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/187/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| relationship-paths | /private/tmp/culturemech-review-work-batch019/187/relationship-path-check.json; Three declared bacterial paths versus exact stable-ID owners under archaea | refutes | Both owner directions and the generated child link point to absent bacterial paths. Actual stable IDs resolve to the inspected archaeal owners. Path repair alone would not make the SOURCE_DUPLICATE relationship scientifically correct. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation signature and merge_formulation_evidence | context_only | Current formulation-aware merge code is pinned; it was not executed or historically replayed. Existing generated targets can predate owner repairs/evidence. |
| writer-context-1 | src/culturemech/ingredients/mim_label_index.py; strong_label_key, weak_label_key, label_hydrate_count and pinned metadata | context_only | Current exact-key correspondence and explicit source hydration are separate checks. Current CHEBI keys cannot establish historical MediaIngredientMech numeric identity. |
| writer-context-2 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit | context_only | Current code reads the first/main solution, recognizes referenced solution IDs and percentage-attributed liquid rows as stocks, and skips direct water. Molarity-labelled liquid rows without solution IDs are not covered by that percent predicate. Unit mapping may label bare amounts per liter; current code was not executed and is not evidence of the historical writer. |
| history-metadata | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml; data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:26:55.749760"}, {"index": 4, "issue": "timezone absent", "value": "2026-04-04T18:49:19.929413"}]}, {"input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml", "events": 8, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:26:55.749760"}, {"index": 4, "issue": "timezone absent", "value": "2026-04-04T18:49:19.929413"}]}, {"input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml", "events": 6, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current primary/provider formulation sources are accessible and all four canonical checks passed. The current sulfur secondary-key miss was fully assessed, so it does not itself force partial completion.
- No final-medium volume, yeast percentage basis, sulfur allotrope, borax replacement identifier, unquantified acid dose, gas mixture or growth claim was inferred. The standalone solution was inspected only as a bounded dependency; its evidence is not automatically transferred to a receiving medium.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115627Z-culturemech-003038-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aerobic_sulfolobales_medium_without_sulfur
  (CultureMech:003038)'
started_at: '2026-10-21T11:43:25Z'
finished_at: '2026-10-21T11:56:27Z'
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
summary: The sulfur-free JCM 693 record contains the parent sulfur dose and was merged
  with the sulfur-containing JCM 691 formulation. The collection explicitly requires
  omission. All other listed amounts match the provider’s nominal stock convention,
  but stock hierarchy, preparation scope, chemical metadata and duplicate/path claims
  need curation. Required current sources and checks are available.
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
  - path: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    sha256: a910f6a6796152958a080efa7dd986ed22f28adb228f1b3a5b5a4ead3bb05ad9
    role: target
  - path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    sha256: ccaf0d18ff84387bd59106448e19c56d23a6ade35731c132ee3b5441649655c1
    role: context
  - path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
    sha256: 37d8c5ba42662c9a7b4364f6e271c3041053151370377da2d7cdbbc8fc85e56d
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml
    sha256: ae6f94eced45d7243bebb925fb5449cc385003f8dc0e210c198e6c89305dcf33
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
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
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
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
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 187; batch 019 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003038
targets:
- target_id: CultureMech:003038
  path: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  label: aerobic_sulfolobales_medium_without_sulfur
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/187/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/187/strict.tsv"
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003038
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
  - CultureMech:003038
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:27.256627Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/187/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:28.841930Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/187/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:31.127537Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:32.295288Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:56:24Z'
  support: supports
  summary: './data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml:1:id:
    CultureMech:003038

    ./data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml:1:id:
    CultureMech:003038

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/187/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:56:24Z'
  support: supports
  summary: 20 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: f0c583f5cbd23eb05f7c0d2f91299f95bab45133198a86cad0fcd0cbbe65da4a
- evidence_id: source-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/187/evidence-context-original.json
  locator: Frozen per-record preflight; exact source fields, owner/dependency inventories
    and source limitations
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: The preflight is diagnostic context. Its literal captures and current input
    bytes are independently read and assessed here; no provisional coverage or source
    conclusion is automatically promoted.
  snapshot_sha256: d4414b96a821306822ae1d38339e8f36e7731354845be9fc98ba40eac0b8dd84
- evidence_id: jcm691
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691
  locator: Complete main table, Salt base solution table, preparation and page-level
    default
  accessed_at: '2026-10-21T11:30:40.417983Z'
  support: supports
  summary: Exact parent formulation separates 1 L salt base, 0.5 g yeast and 1 g powdered
    sulfur; salt base has four gram solutes, seven milligram solutes and 1 L water,
    with unquantified 10 N acid to pH 2.5. The global 121°C/15 min autoclave default
    is distinct from sulfur steaming 3 hr on each of 3 successive days.
  snapshot_sha256: d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788
- evidence_id: jcm693
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693
  locator: Complete modification sentence and page-level default
  accessed_at: '2026-10-21T11:30:40.600535Z'
  support: supports
  summary: Exact sulfur-free source says to use Medium 691 without sulfur. It does
    not authorize adding the parent sulfur or its sulfur-specific steaming procedure.
  snapshot_sha256: 18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65
- evidence_id: togoM711
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711
  locator: meta, both component sections and all comments
  accessed_at: '2026-10-21T11:30:39.095461Z'
  support: supports
  summary: Provider preserves main/salt-base hierarchy, raw g/mg/L quantities and
    the 10 N adjustment reagent; it corroborates source identity, not an independent
    measured final volume.
  snapshot_sha256: 21e1c43c188e1fd1b950b66e33c5a4f5d698a04261d62fce00a810f953e10b3a
- evidence_id: togoM713
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M713
  locator: meta, main component rows and all comments
  accessed_at: '2026-10-21T11:30:39.417305Z'
  support: supports
  summary: Provider variant omits sulfur in its ingredient list and explicitly names
    the omission. Its copied parent sulfur-steaming comment is a source inconsistency,
    not a valid sulfur-free instruction.
  snapshot_sha256: 24f8e06854e575f53ad0baa58f3b458498415bfc6889ba3e035c7bcaf3212670
- evidence_id: mediadiveJ691api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J691
  locator: data.medium and complete solutions4597/4598
  accessed_at: '2026-10-21T11:30:38.449852Z'
  support: supports
  summary: Provider names 1000 mL receiving base and 1000 mL stock basis; g_l values
    describe that declared convention, not an independently measured final medium
    after unquantified additions.
  snapshot_sha256: 5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4
- evidence_id: mediadiveJ693api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J693
  locator: data.medium and solution4600 steps
  accessed_at: '2026-10-21T11:30:38.882656Z'
  support: supports
  summary: Child is a step-only reference to 691 without sulfur; no direct recipe
    array is provided. That is not evidence for an empty medium or an unmodified parent.
  snapshot_sha256: dfb9383c6779c83392cfdaa88b1f86a64484b14f8254de8098a21c3540d4a8f2
- evidence_id: solution4598
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4598
  locator: data.recipe[0:12], volume and step
  accessed_at: '2026-10-21T11:31:25.171773Z'
  support: supports
  summary: Exact standalone salt base, whose numeric source/evidence correspondence
    is assessed separately from any receiving medium.
  snapshot_sha256: 84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501
- evidence_id: chebi131366
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131366
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T11:30:39.793244Z'
  support: supports
  summary: CHEBI:131366 resolves to disodium tetraborate decahydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 1ea4119e009b41d70522d7bdea7b79b0d2a0c8d774d32606f281ade14be31d5d
- evidence_id: chebi26833
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-20T06:55:04.114839Z'
  support: supports
  summary: CHEBI:26833 resolves to sulfur atom. A matching nonobsolete label is not
    evidence that the source supplied this exact salt, hydrate, stereoisomer or material.
    Source-specific concerns are assessed separately.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. A matching nonobsolete label
    is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. A matching
    nonobsolete label is not evidence that the source supplied this exact salt, hydrate,
    stereoisomer or material. Source-specific concerns are assessed separately.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi87020
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_87020
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T11:30:39.996688Z'
  support: supports
  summary: CHEBI:87020 resolves to vanadyl sulfate hydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: f95552b25b2f452d828c90399dc0d24f7f2be2015694c824fac408e0ea353660
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. A matching nonobsolete
    label is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim-grounding
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete exact preferred_term/MAPPED lookup for every asserted current
    secondary key; adjacent source_commit/hash metadata
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "matches":
    {"CHEBI:26833": [], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:87020": [{"label": "VOSO4 x n H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:87020", "preferred_term":
    "VOSO4 x n H2O", "ontology_id": "CHEBI:87020", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id":
    "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_keys":
    ["CHEBI:26833"], "legacy_assertions": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: chemical-metadata
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/187/chemical-metadata-context.json
  locator: All asserted ingredient IDs/labels, formula/CAS/mass/structure fields and
    per-layer linkage denominators
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: All source-specific identity decisions are separated from canonical metadata
    correspondence.
  snapshot_sha256: 18b74b5e685796ccb9bf3b18a90d4e063f279fc5091598712576c6da455fb30b
- evidence_id: stock-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml
  locator: Complete standalone stock YAML, twelve composition rows, eleven attached
    evidence objects, preparation, placeholder and history
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: 'Dependency only: eleven attached amount excerpts match the exact current
    provider response and limit support to provider-declared stock concentrations.
    Water 1000 PERCENT_V_V and the separate placeholder are not valid receiving-medium
    instructions.'
  snapshot_sha256: ae6f94eced45d7243bebb925fb5449cc385003f8dc0e210c198e6c89305dcf33
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/187/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: af48d83a061c0ee06c2b676df1e2db574e60d68beb190378f334cba312508b89
- evidence_id: relationship-paths
  kind: search
  reference: /private/tmp/culturemech-review-work-batch019/187/relationship-path-check.json
  locator: Three declared bacterial paths versus exact stable-ID owners under archaea
  accessed_at: '2026-10-21T11:56:24Z'
  support: refutes
  summary: Both owner directions and the generated child link point to absent bacterial
    paths. Actual stable IDs resolve to the inspected archaeal owners. Path repair
    alone would not make the SOURCE_DUPLICATE relationship scientifically correct.
  snapshot_sha256: 6634cf77ca7a76d5b183b31425d21e76ab8d2f59a96abed3a94d2d03eb97d82e
  search_scope: Complete fresh019 normalized corpus filename listing using rg --files
    --no-ignore --hidden; each declared path checked literally and exact stable IDs/hash-bound
    owners checked under archaea.
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation signature and merge_formulation_evidence
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Current formulation-aware merge code is pinned; it was not executed or
    historically replayed. Existing generated targets can predate owner repairs/evidence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/ingredients/mim_label_index.py
  locator: strong_label_key, weak_label_key, label_hydrate_count and pinned metadata
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Current exact-key correspondence and explicit source hydration are separate
    checks. Current CHEBI keys cannot establish historical MediaIngredientMech numeric
    identity.
  snapshot_sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
- evidence_id: writer-context-2
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: Current code reads the first/main solution, recognizes referenced solution
    IDs and percentage-attributed liquid rows as stocks, and skips direct water. Molarity-labelled
    liquid rows without solution IDs are not covered by that percent predicate. Unit
    mapping may label bare amounts per liter; current code was not executed and is
    not evidence of the historical writer.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml;
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml;
    data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:56:24Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:26:55.749760"}, {"index": 4, "issue":
    "timezone absent", "value": "2026-04-04T18:49:19.929413"}]}, {"input": "data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml",
    "events": 8, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:26:55.749760"}, {"index": 4, "issue": "timezone absent", "value":
    "2026-04-04T18:49:19.929413"}]}, {"input": "data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete primary and secondary identifier metadata
  outcome: concern
  summary: 12 distinct asserted CHEBI keys resolve to nonobsolete terms; 0 canonical-label
    mismatches. Exact current secondary lookup misses ['CHEBI:26833']; legacy IDs
    are separately bounded. These are identifier/linkage results, not source-form
    correctness.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - chemical-metadata
  - mim-grounding
  - chebi131366
  - chebi26833
  - chebi31795
  - chebi32312
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86368
  - chebi87020
  - chebi91244
  details: "{\n  \"scale\": \"0\\u2013100 percent; each denominator is that layer\\\
    u2019s direct+nested ingredient-node count, not a scientific score\",\n  \"counts\"\
    : {\n    \"target\": {\n      \"ingredient_nodes\": 13,\n      \"primary_assertions\"\
    : 12,\n      \"secondary_chebi_assertions\": 11,\n      \"legacy_assertions\"\
    : 0,\n      \"primary_percent\": 92.3076923076923,\n      \"secondary_chebi_percent\"\
    : 84.61538461538461,\n      \"verified_current_secondary_instances\": 10,\n  \
    \    \"verified_current_secondary_percent\": 76.92307692307692\n    },\n    \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    : {\n      \"ingredient_nodes\": 13,\n      \"primary_assertions\": 12,\n    \
    \  \"secondary_chebi_assertions\": 11,\n      \"legacy_assertions\": 0,\n    \
    \  \"primary_percent\": 92.3076923076923,\n      \"secondary_chebi_percent\":\
    \ 84.61538461538461,\n      \"verified_current_secondary_instances\": 10,\n  \
    \    \"verified_current_secondary_percent\": 76.92307692307692\n    },\n    \"\
    data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\": {\n      \"ingredient_nodes\"\
    : 13,\n      \"primary_assertions\": 12,\n      \"secondary_chebi_assertions\"\
    : 11,\n      \"legacy_assertions\": 0,\n      \"primary_percent\": 92.3076923076923,\n\
    \      \"secondary_chebi_percent\": 84.61538461538461,\n      \"verified_current_secondary_instances\"\
    : 10,\n      \"verified_current_secondary_percent\": 76.92307692307692\n    }\n\
    \  }\n}"
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 37 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"name\": \"Yeast extract\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; Yeast extract\",\n     \
    \   \"exact_source_quote\": \"Yeast extract (BD-Difco) 0.5 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n    \
    \                    \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"Yeast 0.5 g is retained from the parent\
    \ under the explicit omission-only modification. Its G_PER_L value follows the\
    \ provider nominal 1000 mL basis; attach that convention and preserve the separate\
    \ yeast-solution preparation. No measured final volume is inferred.\",\n    \"\
    local\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n \
    \   \"arithmetic\": \"Provider 0.5 g with g_l=0.5 on declared 1000 mL basis. Receiving\
    \ volume, stock-water amount and unquantified preparation additions remain separate.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"decision\": \"\
    evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Sulfur\",\n  \
    \  \"field_path\": \"ingredients[1].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; Sulfur\",\n        \"exact_source_quote\"\
    : \"Sulfur (powder) 1.0 g\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"attribute\\\": \\\"powder\\\",\\n               \
    \         \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"g\\\"\
    ,\\n                        \\\"g_l\\\": 1,\\n                        \\\"mmol_l\\\
    \": 31.1818,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"JCM 693 explicitly omits this parent ingredient.\
    \ Remove the sulfur assertion from the child formulation; do not turn omission\
    \ into a measured zero. The JCM 691 owner legitimately retains its source 1 g\
    \ sulfur batch amount, with evidence still needed.\",\n    \"local\": {\n    \
    \  \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\"\
    : \"Provider 1 g with g_l=1 on declared 1000 mL basis. Receiving volume, stock-water\
    \ amount and unquantified preparation additions remain separate.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"name\": \"(NH4)2SO4\",\n\
    \    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; (NH4)2SO4\"\
    ,\n        \"exact_source_quote\": \"(NH 4 ) 2 SO 4 1.3 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 1.3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.3,\\n   \
    \                     \\\"mmol_l\\\": 9.83805,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"1.3\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"\
    Provider 1.3 g with g_l=1.3 on declared 1000 mL basis. Receiving volume, stock-water\
    \ amount and unquantified preparation additions remain separate.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"KH2PO4\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"decision\": \"correct\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 Salt base solution table; KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH 2 PO 4 0.28 g\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.28,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.28,\\n         \
    \               \\\"mmol_l\\\": 2.05752,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.28\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"\
    Provider 0.28 g with g_l=0.28 on declared 1000 mL basis. Receiving volume, stock-water\
    \ amount and unquantified preparation additions remain separate.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"MgSO4 x 7 H2O\",\n \
    \   \"field_path\": \"ingredients[4].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; MgSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.25 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.25,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.25,\\n\
    \                        \\\"mmol_l\\\": 1.0143,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.25\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"\
    Provider 0.25 g with g_l=0.25 on declared 1000 mL basis. Receiving volume, stock-water\
    \ amount and unquantified preparation additions remain separate.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CaCl2 x 2 H2O\",\n \
    \   \"field_path\": \"ingredients[5].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CaCl2 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.07 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.07,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.07,\\n\
    \                        \\\"mmol_l\\\": 0.476142,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n      },\n\
    \      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; salt-base dose\",\n    \
    \    \"exact_source_quote\": \"Salt base solution (see below) 1.0 L\",\n     \
    \   \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.07\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"\
    Provider 0.07 g with g_l=0.07 on declared 1000 mL basis. Receiving volume, stock-water\
    \ amount and unquantified preparation additions remain separate.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"MnCl2 x 4 H2O\",\n \
    \   \"field_path\": \"ingredients[6].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; MnCl2 x 4 H2O\"\
    ,\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 1.8 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0018,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.0018\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\"\
    : \"Provider 1.8 mg with g_l=0.0018 on declared 1000 mL basis. Unit conversion:\
    \ 1.8 mg × 0.001 = 0.0018 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Na2B4O7 x 10 H2O\",\n\
    \    \"field_path\": \"ingredients[7].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; Na2B4O7 x 10\
    \ H2O\",\n        \"exact_source_quote\": \"Na 2 B 4 O 7 ·10H 2 O 4.5 mg\",\n\
    \        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Na2B4O7 x 10 H2O\\\",\\n                        \\\"compound_id\\\
    \": 196,\\n                        \\\"amount\\\": 4.5,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0045,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.0045\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\"\
    : \"Provider 4.5 mg with g_l=0.0045 on declared 1000 mL basis. Unit conversion:\
    \ 4.5 mg × 0.001 = 0.0045 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"ZnSO4 x 7 H2O\",\n \
    \   \"field_path\": \"ingredients[8].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; ZnSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 0.22 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.22,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.00022,\\\
    n                        \\\"mmol_l\\\": 0.000765055,\\n                     \
    \   \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"0.00022\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\"\
    : \"Provider 0.22 mg with g_l=0.00022 on declared 1000 mL basis. Unit conversion:\
    \ 0.22 mg × 0.001 = 0.00022 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CuCl2 x 2 H2O\",\n \
    \   \"field_path\": \"ingredients[9].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CuCl2 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"CuCl 2 ·2H 2 O 0.05 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 0.05,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 5.0e-5,\\\
    n                        \\\"mmol_l\\\": 0.000293284,\\n                     \
    \   \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"5e-05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\":\
    \ \"Provider 0.05 mg with g_l=5e-05 on declared 1000 mL basis. Unit conversion:\
    \ 0.05 mg × 0.001 = 0.00005 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Na2MoO4 x 2 H2O\",\n\
    \    \"field_path\": \"ingredients[10].concentration\",\n    \"decision\": \"\
    correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; Na2MoO4 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.03 mg\",\n  \
    \      \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.03,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 3.0e-5,\\\
    n                        \\\"mmol_l\\\": 0.000123993,\\n                     \
    \   \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"3e-05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\":\
    \ \"Provider 0.03 mg with g_l=3e-05 on declared 1000 mL basis. Unit conversion:\
    \ 0.03 mg × 0.001 = 0.00003 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"VOSO4 x n H2O\",\n \
    \   \"field_path\": \"ingredients[11].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; VOSO4 x n H2O\"\
    ,\n        \"exact_source_quote\": \"VOSO 4 · x H 2 O 0.03 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"VOSO4 x n H2O\\\",\\n                        \\\"compound_id\\\
    \": 1062,\\n                        \\\"amount\\\": 0.03,\\n                 \
    \       \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 3.0e-5,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"3e-05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\":\
    \ \"Provider 0.03 mg with g_l=3e-05 on declared 1000 mL basis. Unit conversion:\
    \ 0.03 mg × 0.001 = 0.00003 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CoSO4 x 7 H2O\",\n \
    \   \"field_path\": \"ingredients[12].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CoSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"CoSO 4 ·7H 2 O 0.01 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 198,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 1.0e-5,\\\
    n                        \\\"mmol_l\\\": 6.45178e-5,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe; salt-base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt-base table; water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical G_PER_L value agrees with\
    \ the provider-declared salt-base concentration. Both target and owners flatten\
    \ it into final ingredients without stock-dose/batch context or attached evidence.\
    \ Restore source stock scope; do not change the supported stock number or silently\
    \ assert a measured final-medium concentration.\",\n    \"local\": {\n      \"\
    value\": \"1e-05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\":\
    \ \"Provider 0.01 mg with g_l=1e-05 on declared 1000 mL basis. Unit conversion:\
    \ 0.01 mg × 0.001 = 0.00001 g. Receiving volume, stock-water amount and unquantified\
    \ preparation additions remain separate.\",\n    \"layer_decisions\": [\n    \
    \  {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Receiving salt-base\
    \ dose\",\n    \"field_path\": \"source.salt_base.receiving_volume\",\n    \"\
    decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; salt-base dose\",\n    \
    \    \"exact_source_quote\": \"Salt base solution (see below) 1.0 L\",\n     \
    \   \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    solution\\\": \\\"Salt base solution\\\",\\n                        \\\"solution_id\\\
    \": 4598,\\n                        \\\"amount\\\": 1000,\\n                 \
    \       \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The inherited source main formulation\
    \ uses 1 L salt base; the dose is missing as a distinct claim in all three layers.\
    \ Add this source-stage information without double-counting the eleven expanded\
    \ solutes or inferring final volume.\"\n  },\n  {\n    \"name\": \"Salt-base water\
    \ amount\",\n    \"field_path\": \"source.salt_base.water\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 salt-base table; water amount\",\n  \
    \      \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"Source water is 1 L within salt-base preparation.\
    \ Preserve the volume, not a mass concentration, an inferred final volume or the\
    \ local dependency’s 1000 PERCENT_V_V artifact.\"\n  },\n  {\n    \"name\": \"\
    Autoclave temperature\",\n    \"field_path\": \"preparation.autoclave.temperature\"\
    ,\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 page-level default; salt base and yeast\
    \ separately\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n        \"\
    parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The JCM page gives the 121°C/15 min default\
    \ where not otherwise stated. It supports separate salt-base/yeast autoclaving,\
    \ not replacement of the parent’s sulfur-steaming exception.\",\n    \"arithmetic\"\
    : \"Source literal: 121°C; no conversion.\",\n    \"layer_decisions\": [\n   \
    \   {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.autoclave.temperature\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.autoclave.temperature\",\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation.autoclave.temperature\",\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Autoclave duration\"\
    ,\n    \"field_path\": \"preparation.autoclave.duration\",\n    \"decision\":\
    \ \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 page-level default; salt base and yeast\
    \ separately\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n        \"\
    parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The JCM page gives the 121°C/15 min default\
    \ where not otherwise stated. It supports separate salt-base/yeast autoclaving,\
    \ not replacement of the parent’s sulfur-steaming exception.\",\n    \"arithmetic\"\
    : \"Source literal: 15 min; no conversion.\",\n    \"layer_decisions\": [\n  \
    \    {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.autoclave.duration\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.autoclave.duration\",\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation.autoclave.duration\",\n        \"decision\"\
    : \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Yeast preparation strength\"\
    ,\n    \"field_path\": \"preparation.yeast_solution.strength\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main preparation; percent basis not specified\"\
    ,\n        \"exact_source_quote\": \"Autoclave Salt base solution and yeast extract\
    \ (as a 10% solution) separately and combine after cooling.\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The parent explicitly retains the 10%\
    \ yeast preparation. Its percentage basis and physical dose are unspecified, so\
    \ do not assume w/v or calculate final dilution. The child inherits the non-sulfur\
    \ procedure.\",\n    \"arithmetic\": \"Source literal: 10%; no conversion.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation.yeast_solution.strength\",\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.yeast_solution.strength\",\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"decision\"\
    : \"evidence_only\",\n        \"stored\": \"Autoclave Salt base solution and yeast\
    \ extract (as a 10% solution) separately and combine after cooling. Steam sulfur\
    \ for 3 hr on each of 3 successive days.\"\n      }\n    ]\n  },\n  {\n    \"\
    name\": \"Sulfur steaming duration\",\n    \"field_path\": \"preparation.sulfur_steam.duration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 parent sulfur-specific preparation\"\
    ,\n        \"exact_source_quote\": \"Steam sulfur for 3 hr on each of 3 successive\
    \ days.\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"This quantitative procedure belongs only\
    \ to the sulfur-containing parent. Its current parent text is numerically supported\
    \ but lacks attached evidence; it is not an instruction to add or steam sulfur\
    \ for JCM 693.\",\n    \"arithmetic\": \"Source literal: 3 hr; no conversion.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation.sulfur_steam.duration\",\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.sulfur_steam.duration\",\n        \"\
    decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"decision\"\
    : \"evidence_only\",\n        \"stored\": \"Autoclave Salt base solution and yeast\
    \ extract (as a 10% solution) separately and combine after cooling. Steam sulfur\
    \ for 3 hr on each of 3 successive days.\"\n      }\n    ]\n  },\n  {\n    \"\
    name\": \"Sulfur steaming repetitions\",\n    \"field_path\": \"preparation.sulfur_steam.repetitions\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 parent sulfur-specific preparation\"\
    ,\n        \"exact_source_quote\": \"Steam sulfur for 3 hr on each of 3 successive\
    \ days.\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"This quantitative procedure belongs only\
    \ to the sulfur-containing parent. Its current parent text is numerically supported\
    \ but lacks attached evidence; it is not an instruction to add or steam sulfur\
    \ for JCM 693.\",\n    \"arithmetic\": \"Source literal: 3 successive days; no\
    \ conversion.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation.sulfur_steam.repetitions\",\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.sulfur_steam.repetitions\",\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"decision\"\
    : \"evidence_only\",\n        \"stored\": \"Autoclave Salt base solution and yeast\
    \ extract (as a 10% solution) separately and combine after cooling. Steam sulfur\
    \ for 3 hr on each of 3 successive days.\"\n      }\n    ]\n  },\n  {\n    \"\
    name\": \"Salt base pH endpoint\",\n    \"field_path\": \"preparation.salt_base.pH\"\
    ,\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation\",\n \
    \       \"exact_source_quote\": \"Adjust pH to 2.5 with 10 N H 2 SO 4 .\",\n \
    \       \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The literal pH endpoint/acid strength\
    \ appears in parent preparation but is presented without a distinct salt-base\
    \ object. Restore stock scope and attach evidence; add that scoped context to\
    \ the child. The endpoint is not a measured growth optimum and 10 N is not a dose.\"\
    ,\n    \"arithmetic\": \"Source literal: 2.5; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.salt_base.pH\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.salt_base.pH\",\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": \"Adjust pH to 2.5 with 10 N H2SO4.\"\n  \
    \    }\n    ]\n  },\n  {\n    \"name\": \"Adjustment acid strength\",\n    \"\
    field_path\": \"preparation.salt_base.acid_strength\",\n    \"decision\": \"add\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation; dose\
    \ not quantified\",\n        \"exact_source_quote\": \"Adjust pH to 2.5 with 10\
    \ N H 2 SO 4 .\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The literal pH endpoint/acid strength\
    \ appears in parent preparation but is presented without a distinct salt-base\
    \ object. Restore stock scope and attach evidence; add that scoped context to\
    \ the child. The endpoint is not a measured growth optimum and 10 N is not a dose.\"\
    ,\n    \"arithmetic\": \"Source literal: 10 N; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.salt_base.acid_strength\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml\"\
    ,\n        \"field_path\": \"preparation.salt_base.acid_strength\",\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": \"Adjust pH to 2.5 with 10 N H2SO4.\"\n  \
    \    }\n    ]\n  },\n  {\n    \"name\": \"Acid adjustment amount\",\n    \"field_path\"\
    : \"source.salt_base.acid_dose\",\n    \"decision\": \"not_quantified\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation\",\n \
    \       \"exact_source_quote\": \"Adjust pH to 2.5 with 10 N H 2 SO 4 .\",\n \
    \       \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm693\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693\",\n        \"source_locator\"\
    : \"JCM 693 complete modification sentence\",\n        \"exact_source_quote\"\
    : \"Use Medium No. 691 without sulfur.\",\n        \"snapshot_sha256\": \"18000e2ce518b24bd5585e7db2a3a01eda7f6b76d1f17995de096ec244c74b65\"\
    ,\n        \"parsed_text_sha256\": \"e6ce7b8dff860e7f118c6b46e5aab17c2c50cf04998bdd9f792288ec40155ace\"\
    \n      }\n    ],\n    \"rationale\": \"The source fixes a 10 N adjustment reagent\
    \ and pH endpoint but gives no addition volume. Absence of a fixed local acid\
    \ number must not be replaced with an invented dose or final concentration.\"\n\
    \  },\n  {\n    \"name\": \"Parent provider pH scalar\",\n    \"field_path\":\
    \ \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml::ph_value\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadiveJ691api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\"\
    ,\n        \"source_locator\": \"$.data.medium.min_pH\",\n        \"exact_source_quote\"\
    : \"\\\"min_pH\\\": 2.5\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ691api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J691\",\n        \"source_locator\"\
    : \"$.data.medium.max_pH\",\n        \"exact_source_quote\": \"\\\"max_pH\\\"\
    : 2.5\",\n        \"snapshot_sha256\": \"5f6378c959d887cec011fd6204fa034ce35bda88b611b3cae83fdd36f66bd2f4\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 Salt base solution preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 2.5 with 10 N H 2 SO 4 .\",\n        \"snapshot_sha256\": \"\
    d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n        \"\
    parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The parent scalar 2.5 matches provider\
    \ metadata. Preserve it as provider/source context with evidence, distinct from\
    \ an experimentally measured final pH or growth optimum.\",\n    \"local\": 2.5,\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: (NH4)2SO4\",\n\
    \    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[0].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; (NH4)2SO4\",\n    \
    \    \"exact_source_quote\": \"(NH 4 ) 2 SO 4 1.3 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"(NH4)2SO4\\\
    \",\\n                \\\"compound_id\\\": 27,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 1.3,\\n                \\\"unit\\\": \\\"g\\\",\\n     \
    \           \\\"g_l\\\": 1.3,\\n                \\\"mmol_l\\\": 9.83805,\\n  \
    \              \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"1.3\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"arithmetic\": \"1.3 g on provider-declared 1000 mL stock\
    \ basis; g_l=1.3. No receiving-medium dilution inferred.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: KH2PO4\"\
    ,\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[1].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; KH2PO4\",\n       \
    \ \"exact_source_quote\": \"KH 2 PO 4 0.28 g\",\n        \"snapshot_sha256\":\
    \ \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"KH2PO4\\\"\
    ,\\n                \\\"compound_id\\\": 11,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 0.28,\\n                \\\"unit\\\": \\\"g\\\",\\n                \\\"g_l\\\
    \": 0.28,\\n                \\\"mmol_l\\\": 2.05752,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\
    \n      }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached\
    \ exact evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.28\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.28 g on provider-declared 1000\
    \ mL stock basis; g_l=0.28. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: MgSO4\
    \ x 7 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[2].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; MgSO4 x 7 H2O\",\n\
    \        \"exact_source_quote\": \"MgSO 4 ·7H 2 O 0.25 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"MgSO4 x 7\
    \ H2O\\\",\\n                \\\"compound_id\\\": 8,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.25,\\n                \\\"unit\\\": \\\"g\\\",\\n    \
    \            \\\"g_l\\\": 0.25,\\n                \\\"mmol_l\\\": 1.0143,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.25\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.25 g on provider-declared 1000\
    \ mL stock basis; g_l=0.25. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: CaCl2\
    \ x 2 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[3].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; CaCl2 x 2 H2O\",\n\
    \        \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.07 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"CaCl2 x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 7,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.07,\\n                \\\"unit\\\": \\\"g\\\",\\n    \
    \            \\\"g_l\\\": 0.07,\\n                \\\"mmol_l\\\": 0.476142,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.07\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.07 g on provider-declared 1000\
    \ mL stock basis; g_l=0.07. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: MnCl2\
    \ x 4 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[4].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; MnCl2 x 4 H2O\",\n\
    \        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 1.8 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[4]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 5,\\n                \\\"compound\\\": \\\"MnCl2 x 4\
    \ H2O\\\",\\n                \\\"compound_id\\\": 36,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 1.8,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.0018,\\n                \\\"mmol_l\\\": null,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.0018\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"1.8 mg on provider-declared 1000\
    \ mL stock basis; g_l=0.0018. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: Na2B4O7\
    \ x 10 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[5].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; Na2B4O7 x 10 H2O\"\
    ,\n        \"exact_source_quote\": \"Na 2 B 4 O 7 ·10H 2 O 4.5 mg\",\n       \
    \ \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"Na2B4O7 x\
    \ 10 H2O\\\",\\n                \\\"compound_id\\\": 196,\\n                \\\
    \"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n        \
    \        \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 4.5,\\n                \\\"unit\\\": \\\"mg\\\
    \",\\n                \\\"g_l\\\": 0.0045,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.0045\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"4.5 mg on provider-declared 1000\
    \ mL stock basis; g_l=0.0045. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: ZnSO4\
    \ x 7 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[6].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; ZnSO4 x 7 H2O\",\n\
    \        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 0.22 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[6]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 7,\\n                \\\"compound\\\": \\\"ZnSO4 x 7\
    \ H2O\\\",\\n                \\\"compound_id\\\": 35,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.22,\\n                \\\"unit\\\": \\\"mg\\\",\\n   \
    \             \\\"g_l\\\": 0.00022,\\n                \\\"mmol_l\\\": 0.000765055,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"0.00022\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.22 mg on provider-declared 1000\
    \ mL stock basis; g_l=0.00022. No receiving-medium dilution inferred.\",\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: CuCl2\
    \ x 2 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[7].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; CuCl2 x 2 H2O\",\n\
    \        \"exact_source_quote\": \"CuCl 2 ·2H 2 O 0.05 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[7]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 8,\\n                \\\"compound\\\": \\\"CuCl2 x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 39,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.05,\\n                \\\"unit\\\": \\\"mg\\\",\\n   \
    \             \\\"g_l\\\": 5.0e-5,\\n                \\\"mmol_l\\\": 0.000293284,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"5e-05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.05 mg on provider-declared 1000\
    \ mL stock basis; g_l=5e-05. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: Na2MoO4\
    \ x 2 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[8].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; Na2MoO4 x 2 H2O\",\n\
    \        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.03 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[8]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 9,\\n                \\\"compound\\\": \\\"Na2MoO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 0.03,\\n                \\\"unit\\\": \\\"mg\\\
    \",\\n                \\\"g_l\\\": 3.0e-5,\\n                \\\"mmol_l\\\": 0.000123993,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"3e-05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.03 mg on provider-declared 1000\
    \ mL stock basis; g_l=3e-05. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: VOSO4\
    \ x n H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[9].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; VOSO4 x n H2O\",\n\
    \        \"exact_source_quote\": \"VOSO 4 · x H 2 O 0.03 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[9]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 10,\\n                \\\"compound\\\": \\\"VOSO4 x n\
    \ H2O\\\",\\n                \\\"compound_id\\\": 1062,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 0.03,\\n                \\\"unit\\\": \\\"mg\\\
    \",\\n                \\\"g_l\\\": 3.0e-5,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"3e-05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.03 mg on provider-declared 1000\
    \ mL stock basis; g_l=3e-05. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: CoSO4\
    \ x 7 H2O\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[10].concentration\"\
    ,\n    \"decision\": \"verified\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; CoSO4 x 7 H2O\",\n\
    \        \"exact_source_quote\": \"CoSO 4 ·7H 2 O 0.01 mg\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[10]\",\n        \"exact_source_quote\": \"{\\n             \
    \   \\\"recipe_order\\\": 11,\\n                \\\"compound\\\": \\\"CoSO4 x\
    \ 7 H2O\\\",\\n                \\\"compound_id\\\": 198,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 0.01,\\n                \\\"unit\\\": \\\"mg\\\
    \",\\n                \\\"g_l\\\": 1.0e-5,\\n                \\\"mmol_l\\\": 6.45178e-5,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Existing stock value/unit and attached exact\
    \ evidence agree with the provider-declared stock basis. This does not verify\
    \ a receiving-medium final concentration or resolve a separate chemical-form metadata\
    \ conflict.\",\n    \"local\": {\n      \"value\": \"1e-05\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"arithmetic\": \"0.01 mg on provider-declared 1000\
    \ mL stock basis; g_l=1e-05. No receiving-medium dilution inferred.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[10].concentration\",\n        \"decision\"\
    : \"verified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock: Distilled\
    \ water\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"Salt base solution table; Distilled water\",\n\
    \        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"solution4598\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4598\",\n        \"source_locator\"\
    : \"$.data.recipe[11]\",\n        \"exact_source_quote\": \"{\\n             \
    \   \\\"recipe_order\\\": 12,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1000,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\n     \
    \ }\n    ],\n    \"rationale\": \"Provider and collection give 1000 mL/1 L water\
    \ for the salt-base batch. Local 1000 PERCENT_V_V is not that volume; do not inherit\
    \ or use it as a measured final-volume claim.\",\n    \"local\": {\n      \"value\"\
    : \"1000\",\n      \"unit\": \"PERCENT_V_V\"\n    },\n    \"arithmetic\": \"1000\
    \ ml on provider-declared 1000 mL stock basis; g_l=None. No receiving-medium dilution\
    \ inferred.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml\"\
    ,\n        \"field_path\": \"composition[11].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency placeholder\"\
    ,\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::ingredients[0]\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"solution4598\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4598\"\
    ,\n        \"source_locator\": \"$.data.recipe[11]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 12,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"84e25b78e4a5935ff4ae986c498ba64b97190e590344a62c2471ce6dc9d11501\"\
    \n      }\n    ],\n    \"rationale\": \"The file separately carries See source\
    \ for composition with a VARIABLE amount despite a populated composition. This\
    \ is not an additional ingredient or dose and must not be imported into the target.\"\
    ,\n    \"local\": {\n      \"preferred_term\": \"See source for composition\"\
    ,\n      \"concentration\": {\n        \"value\": \"variable\",\n        \"unit\"\
    : \"VARIABLE\"\n      }\n    }\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Sulfur-free JCM 693 versus sulfur-containing JCM 691
  outcome: concern
  summary: JCM 693 explicitly requires the parent without sulfur. The target and its
    JCM 693 owner instead include sulfur 1 G_PER_L copied from the parent; the generated
    merge also treats the JCM 691 owner as a synonym/source duplicate. That changes
    the named formulation. Source M713’s contradictory copied sulfur-steaming comment
    does not override its ingredient omission or the collection instruction.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm693
  - jcm691
  - togoM713
  - mediadiveJ693api
- assessment_id: source-stage-consistency
  area: consistency
  topic: Numerical agreement does not establish formulation identity
  outcome: concern
  summary: The thirteen local numbers match the provider-normalized parent formula,
    including the sulfur that must be absent from the child. Four gram and seven milligram
    source salts are numerically converted consistently with the provider-declared
    stock basis, but stock composition, receiving dose and water/preparation scope
    are not represented distinctly. The inventory retains source rows, explicit omission,
    all owner-layer decisions and the eleven independently evidenced stock quantities.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm691
  - jcm693
  - mediadiveJ691api
  - quantity-inventory
  - stock-local
- assessment_id: preparation
  area: completeness
  topic: Inherited procedure, exceptions and missing stage detail
  outcome: concern
  summary: The child’s single instruction accurately says without sulfur but contradicts
    its ingredient list and omits the inherited non-sulfur protocol. The parent retains
    separate autoclaving/cooling, yeast 10%, sulfur 3 hr on each of 3 days, and acid/pH
    text; its stock boundary remains flattened and the page-default autoclave temperature/duration
    are absent. Do not copy sulfur-specific preparation into the child. No yeast percentage
    basis, acid volume, incubation temperature or gas mixture is supplied.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm691
  - jcm693
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Exact source hydrates and bounded ontology conflict
  outcome: concern
  summary: The sulfate/chloride hydrates and variable vanadyl hydrate retain explicit
    source forms. CHEBI:131366 has the expected canonical borax label but its captured
    formula 10H2O.H4B4O9.2Na and mass 417.401 differ from source Na2B4O7·10H2O. Label
    agreement cannot settle that structural/stoichiometric conflict. No alternate
    ID or molar conversion is inferred.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - jcm691
  - solution4598
  - chebi131366
  - chemical-metadata
- assessment_id: sulfur-identity
  area: grounding
  topic: Primary sulfur identity versus current secondary mapping
  outcome: concern
  summary: CHEBI:26833 is a valid nonobsolete sulfur term and has an Elemental sulfur
    synonym; powder context alone does not prove a wrong primary ID or justify an
    allotrope replacement. Its asserted current secondary CHEBI key has no preferred_term/MAPPED
    row in the pinned MIM index. This completed current lookup is distinct from the
    unresolved historical numeric ID assessed in record186; no unavailable historical
    check is introduced here.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - chebi26833
  - mim-grounding
  - chemical-metadata
- assessment_id: relationships
  area: scope
  topic: Duplicate labels, broken paths and merged-source boundaries
  outcome: concern
  summary: The three bacterial path instances are absent from the ignored-inclusive
    normalized listing; their stable IDs resolve under archaea. The underlying SOURCE_DUPLICATE
    designation is also wrong for the collection’s explicit omission variant. Current
    formulation-aware merging cannot be replaced by an ingredient-set fingerprint
    as evidence of equality; retain source-specific stable IDs and formulation boundaries.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - relationship-paths
  - jcm691
  - jcm693
- assessment_id: classification
  area: scope
  topic: Medium class, roles and biological limits
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are consistent with the inherited yeast-containing
    liquid source. Archaea and Sulfolobales are source/title context, not claims that
    every taxon or strain grows in either variant. There are no asserted organisms,
    genome accessions, DOI/PMID, optimum or experimental growth result to verify.
    No new growth or pathway assertion is inferred from the name or source recipe.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm691
  - jcm693
- assessment_id: generation
  area: provenance
  topic: Maintained owners and current import/merge semantics
  outcome: concern
  summary: The child history explicitly records copying thirteen parent ingredients,
    and the target records merging these two owners. Those historical statements explain
    provenance but do not justify copying an omitted ingredient. Current MediaDive
    code distinguishes the primary solution from referenced stock sections; current
    formulation merging requires compatible payloads. Neither was executed and no
    historical code behavior is inferred solely from current implementation.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 24 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003038
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: culturemech.003038.sulfur-omission-lost
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The sulfur-free recipe contains sulfur and is conflated with its parent
  description: 'The exact JCM 693 instruction and local preparation say without sulfur,
    yet the target and JCM 693 owner include sulfur 1 G_PER_L and the generated record
    merges JCM 691 as a synonym. A parent-derived numerical match is insufficient:
    this child must omit sulfur. The resolved_reference flag and historical copy/merge
    events do not validate the formulation.'
  target_ids:
  - CultureMech:003038
  field_paths:
  - ingredients[1]
  - preparation_steps[0]
  - synonyms
  - merged_from
  - variant_children
  - data_quality_flags
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm693
  - jcm691
  - togoM713
  - mediadiveJ693api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  issue_key: culturemech.003038.relationship-paths
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Reciprocal source links use absent bacterial paths
  description: The target and JCM 693 owner point to bacterial/aerobic_sulfolobales_medium.yaml,
    while the JCM 691 owner points to bacterial/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml.
    All three are absent in the ignored-inclusive search; the exact stable-ID records
    are under archaea. The successful reference recipe reported zero checked references.
  target_ids:
  - CultureMech:003038
  field_paths:
  - variant_children[0].path
  - parent_media.path
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - relationship-paths
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  issue_key: culturemech.003038.stock-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Inherited salt-base and non-sulfur preparation are incompletely represented
  description: The eleven salt-base concentrations are flattened, the separate 1 L
    base dose and water basis are absent, and the child has only a parent-reference
    sentence. Source default autoclaving at 121°C for 15 min, separate yeast preparation/cooling,
    stock pH 2.5 and 10 N adjustment reagent need scoped evidence; the parent sulfur-steaming
    procedure must remain parent-only. This protocol impact warrants major severity
    for native P3.5.
  target_ids:
  - CultureMech:003038
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm691
  - jcm693
  - mediadiveJ691api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.003038.borax-structure-conflict
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Borax label agreement hides a formula conflict
  description: The asserted CHEBI:131366 label matches the named decahydrate, but
    its captured structural formula 10H2O.H4B4O9.2Na and mass 417.401 differ from
    the collection’s Na2B4O7·10H2O. This is an unresolved source/ontology metadata
    conflict; the source mass and provider g/L correspondence are separate.
  target_ids:
  - CultureMech:003038
  field_paths:
  - ingredients[7].term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm691
  - chebi131366
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  issue_key: culturemech.003038.current-mim-sulfur-gap
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The current sulfur secondary key has no pinned MIM mapping
  description: CHEBI:26833 is valid as a primary term, but the asserted mediaingredientmech_chebi_term
    has no exact preferred_term/MAPPED entry in the complete pinned MIM index. The
    other ten asserted current secondary keys resolve. The current negative result
    is a completed lookup, not an unavailable ontology or historical numeric-ID search.
  target_ids:
  - CultureMech:003038
  field_paths:
  - ingredients[1].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - chebi26833
  - mim-grounding
  - chemical-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  issue_key: culturemech.003038.evidence-and-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source quantities lack attached evidence and four history instances lack
    timezones
  description: Target and both owners have source URLs and historical copied-from
    notes but no attached matching ingredient quantity excerpts. Two timezone-naive
    events occur in the target and are repeated in the JCM 693 owner, totaling four
    instances; the six JCM 691 owner timestamps are timezone-aware. History is provenance,
    not scientific validation.
  target_ids:
  - CultureMech:003038
  field_paths:
  - ingredients
  - evidence
  - references
  - curation_history[1].timestamp
  - curation_history[4].timestamp
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantity-inventory
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Correct the maintained JCM 693 formulation to retain the explicit omission,
    preserve the distinct sulfur-containing JCM 691 owner and stable IDs, and replace
    duplicate/equivalence treatment with the supported omitted-component relationship
    before separately authorized regeneration. Do not encode omission as a measured
    zero.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  description: Repair exact canonical owner paths and reciprocal IDs together with
    the scientific variant relationship. Verify all three occurrences and regenerate;
    do not treat a path-only fix as confirmation of SOURCE_DUPLICATE.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  description: Represent the exact inherited stock/dose and non-sulfur preparation
    context, with literal evidence and explicit unknown yeast-percent basis, acid
    dose and final volume. Preserve supported provider stock numbers; do not import
    the dependency water percentage or placeholder.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  description: Resolve the exact supplied borax form and ontology structural discrepancy
    before molar use or re-grounding. Retain the source mass and avoid inventing a
    replacement ID.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  description: Remove the sulfur row from the sulfur-free child as required by its
    source, and separately reconcile the sulfur-containing owner’s current secondary
    link using verified exact correspondence. Do not replace a valid primary term
    solely to increase linkage coverage.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
  description: Attach claim-level primary/provider evidence with stock/variant scope.
    Preserve historical event bytes and append a bounded provenance clarification
    when authorized; do not invent timezone offsets or rewrite old events.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:003038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J693_AEROBIC_SULFOLOBALES_MEDIUM_WITHOUT_SULFUR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aerobic_sulfolobales_medium.yaml
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
- The current primary/provider formulation sources are accessible and all four canonical
  checks passed. The current sulfur secondary-key miss was fully assessed, so it does
  not itself force partial completion.
- No final-medium volume, yeast percentage basis, sulfur allotrope, borax replacement
  identifier, unquantified acid dose, gas mixture or growth claim was inferred. The
  standalone solution was inspected only as a bounded dependency; its evidence is
  not automatically transferred to a receiving medium.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
