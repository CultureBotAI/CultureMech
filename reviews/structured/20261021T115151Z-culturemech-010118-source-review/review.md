# Source and formulation review: aerobic_sulfolobales_medium (CultureMech:010118)

- Review: 20261021T115151Z-culturemech-010118-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:24Z
- Finished UTC: 2026-10-21T11:51:51Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M711 resolves to JCM 691 and its sulfur-containing formulation, but the target/owner flatten the salt base, inflate seven milligram quantities to g/L, encode water and stock volume as mass, and omit source-specific preparation. Primary chemical metadata resolves, with a borax formula conflict and an unresolved historical sulfur MIM link. The current sulfur-free sibling remains a distinct variant.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 186; batch 019 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010118 | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml | generated | aerobic_sulfolobales_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010118 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010118 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/186/strict.tsv |
| validate-terms | passed | True | CultureMech:010118 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010118 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010118 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Bounded current legacy-ID lookup | passed | False | CultureMech:010118 | Current pinned catalog/tree and ignored-inclusive local lookup completed; no historical identity correspondence established. |
| Historical sulfur MIM numeric-ID correspondence | unavailable | True | CultureMech:010118 | The exact historical mapping for MediaIngredientMech:001072 was not available in the bounded current sources. This is distinct from a failed or unavailable current catalog lookup. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010118.

The four documented recipes completed; interpret the scope of each separately.

### Complete primary and secondary identifier metadata

grounding: concern. Targets: CultureMech:010118.

13 distinct asserted CHEBI keys resolve to nonobsolete terms; 0 canonical-label mismatches. Exact current secondary lookup misses []; legacy IDs are separately bounded. These are identifier/linkage results, not source-form correctness.

{
  "scale": "0\u2013100 percent; each denominator is that layer\u2019s direct+nested ingredient-node count, not a scientific score",
  "counts": {
    "target": {
      "ingredient_nodes": 15,
      "primary_assertions": 13,
      "secondary_chebi_assertions": 4,
      "legacy_assertions": 1,
      "primary_percent": 86.66666666666667,
      "secondary_chebi_percent": 26.666666666666668,
      "verified_current_secondary_instances": 4,
      "verified_current_secondary_percent": 26.666666666666668
    },
    "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml": {
      "ingredient_nodes": 15,
      "primary_assertions": 13,
      "secondary_chebi_assertions": 4,
      "legacy_assertions": 1,
      "primary_percent": 86.66666666666667,
      "secondary_chebi_percent": 26.666666666666668,
      "verified_current_secondary_instances": 4,
      "verified_current_secondary_percent": 26.666666666666668
    }
  }
}

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010118.

36 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "name": "Sulfur (powder)",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; Sulfur (powder)",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Main source batch amount is numerically preserved on the provider nominal 1000 mL basis, but attached evidence and batch context are missing. No independently measured final volume follows from 1 L base plus a separately prepared yeast solution.",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 1 g; provider stock/main declared volume 1000 mL and g_l=1. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "name": "Yeast extract (BD-Difco)",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe; Yeast extract (BD-Difco)",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Main source batch amount is numerically preserved on the provider nominal 1000 mL basis, but attached evidence and batch context are missing. No independently measured final volume follows from 1 L base plus a separately prepared yeast solution.",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.5 g; provider stock/main declared volume 1000 mL and g_l=0.5. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "name": "Distilled water",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; Distilled water",
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
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source specifies 1 L stock water, not 1 g/L water in the final medium. Restore the stock/preparation volume context; do not assume density or final volume.",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 1000 ml; provider stock/main declared volume 1000 mL and g_l=None. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "MgSO4・7H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; MgSO4・7H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Numeric value equals the provider stock g/L convention, but the amount belongs to the salt-base recipe and is flattened as a final-medium claim. Restore stock scope and attach precise evidence without inventing a final volume.",
    "local": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.25 g; provider stock/main declared volume 1000 mL and g_l=0.25. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CaCl2・2H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CaCl2・2H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Numeric value equals the provider stock g/L convention, but the amount belongs to the salt-base recipe and is flattened as a final-medium claim. Restore stock scope and attach precise evidence without inventing a final volume.",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.07 g; provider stock/main declared volume 1000 mL and g_l=0.07. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "KH2PO4",
    "field_path": "ingredients[5].concentration",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Numeric value equals the provider stock g/L convention, but the amount belongs to the salt-base recipe and is flattened as a final-medium claim. Restore stock scope and attach precise evidence without inventing a final volume.",
    "local": {
      "value": "0.28",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.28 g; provider stock/main declared volume 1000 mL and g_l=0.28. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Na2MoO4・2H2O",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; Na2MoO4・2H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.03 mg; provider stock/main declared volume 1000 mL and g_l=3e-05. Mass conversion only: 0.03 mg × 0.001 = 0.00003 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "MnCl2・4H2O",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; MnCl2・4H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 1.8 mg; provider stock/main declared volume 1000 mL and g_l=0.0018. Mass conversion only: 1.8 mg × 0.001 = 0.0018 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "ZnSO4・7H2O",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; ZnSO4・7H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "0.22",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.22 mg; provider stock/main declared volume 1000 mL and g_l=0.00022. Mass conversion only: 0.22 mg × 0.001 = 0.00022 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CuCl2・2H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CuCl2・2H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.05 mg; provider stock/main declared volume 1000 mL and g_l=5e-05. Mass conversion only: 0.05 mg × 0.001 = 0.00005 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "(NH4)2SO4",
    "field_path": "ingredients[10].concentration",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Numeric value equals the provider stock g/L convention, but the amount belongs to the salt-base recipe and is flattened as a final-medium claim. Restore stock scope and attach precise evidence without inventing a final volume.",
    "local": {
      "value": "1.3",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 1.3 g; provider stock/main declared volume 1000 mL and g_l=1.3. Preserve the printed source mass or volume separately from that provider convention.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "CoSO4・7H2O",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; CoSO4・7H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.01 mg; provider stock/main declared volume 1000 mL and g_l=1e-05. Mass conversion only: 0.01 mg × 0.001 = 0.00001 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "VOSO4・xH2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; VOSO4・xH2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 0.03 mg; provider stock/main declared volume 1000 mL and g_l=3e-05. Mass conversion only: 0.03 mg × 0.001 = 0.00003 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Na2B4O7・10H2O",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 Salt base solution table; Na2B4O7・10H2O",
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
        "source_locator": "JCM 691 main recipe, salt base dose",
        "exact_source_quote": "Salt base solution (see below) 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      },
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 salt base table, water amount",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "The source milligram number is copied unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit and restore stock scope; it is 1000 times the provider stock g/L number, not a verified final-medium concentration.",
    "local": {
      "value": "4.5",
      "unit": "G_PER_L"
    },
    "arithmetic": "Source 4.5 mg; provider stock/main declared volume 1000 mL and g_l=0.0045. Mass conversion only: 4.5 mg × 0.001 = 0.0045 g; provider g/L uses its declared stock basis.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "decision": "correct"
      }
    ]
  },
  {
    "name": "Sulfuric acid adjustment dose",
    "field_path": "ingredients[14].concentration",
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
        "source_key": "togoM711",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711",
        "source_locator": "$.components[1].items[12]",
        "exact_source_quote": "\"component_name\": \"H2SO4\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "21e1c43c188e1fd1b950b66e33c5a4f5d698a04261d62fce00a810f953e10b3a"
      }
    ],
    "rationale": "Source acid strength is 10 N, but the addition volume is not quantified. VARIABLE correctly avoids a fixed dose; the stock strength, pH endpoint and titration stage still need evidence and cannot be replaced by 10 N final medium.",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "decision": "not_quantified"
      }
    ]
  },
  {
    "name": "Salt-base receiving addition",
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 main recipe, salt base dose",
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
        "source_key": "togoM711",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Salt base solution (see below)\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "21e1c43c188e1fd1b950b66e33c5a4f5d698a04261d62fce00a810f953e10b3a"
      }
    ],
    "rationale": "The exact source supplies 1 L salt base, not 1 G_PER_L of Unknown solution. Its named composition is given in the source and must be represented once, separately from the final medium.",
    "local": {
      "preferred_term": "Salt base solution (see below)",
      "composition": [],
      "concentration": {
        "value": "1",
        "unit": "G_PER_L"
      },
      "name": "Unknown solution"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0]",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "solutions[0]",
        "decision": "correct"
      }
    ]
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
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.",
    "arithmetic": "Source value: 121°C; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.autoclave.temperature",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
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
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.",
    "arithmetic": "Source value: 15 min; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.autoclave.duration",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
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
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence. The 10% basis and resulting physical addition volume are unspecified; do not infer w/v or calculate a final dilution.",
    "arithmetic": "Source value: 10%; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.yeast_solution.strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "preparation.yeast_solution.strength",
        "decision": "add"
      }
    ]
  },
  {
    "name": "Sulfur steaming duration",
    "field_path": "preparation.sulfur_steam.duration",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 parent sulfur-specific preparation",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.",
    "arithmetic": "Source value: 3 hr; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.sulfur_steam.duration",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "preparation.sulfur_steam.duration",
        "decision": "add"
      }
    ]
  },
  {
    "name": "Sulfur steaming repetitions",
    "field_path": "preparation.sulfur_steam.repetitions",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm691",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691",
        "source_locator": "JCM 691 parent sulfur-specific preparation",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788",
        "parsed_text_sha256": "6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c"
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.",
    "arithmetic": "Source value: 3 successive days; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.sulfur_steam.repetitions",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "preparation.sulfur_steam.repetitions",
        "decision": "add"
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
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.",
    "arithmetic": "Source value: 2.5; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.salt_base.pH",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "preparation.salt_base.pH",
        "decision": "add"
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
      }
    ],
    "rationale": "Source-supported preparation context is absent in both reviewed layers. Preserve its specific stage and attach evidence.10 N is the adjustment reagent strength, not its unquantified dose or a final-medium concentration.",
    "arithmetic": "Source value: 10 N; no conversion.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation.salt_base.acid_strength",
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
        "field_path": "preparation.salt_base.acid_strength",
        "decision": "add"
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

### TOGO M711, JCM 691 and current maintained owner

identity: supported. Targets: CultureMech:010118.

TOGO meta explicitly maps M711 to JCM_M691 and its collection URL. Target and owner denote the sulfur-containing parent; the sulfur-free JCM 693/TOGO M713 sibling is a separate omitted-component variant. Current main source content is available.

### All local amounts and dependency boundaries

quantity: concern. Targets: CultureMech:010118.

Seven trace stock values retain milligram numbers as G_PER_L; water 1 L and salt-base 1 L also become 1 G_PER_L. Eleven stock solutes are flattened while the remaining salt-base descriptor has an empty composition and unknown name. Main yeast/sulfur amounts are nominal provider concentrations, not independently measured final-volume quantities. The complete inventory distinguishes every target/owner value, source-only preparation quantity and standalone dependency row.

### Separate stock preparation and source conditions

completeness: concern. Targets: CultureMech:010118.

Both reviewed layers omit the full source protocol: separately autoclave salt base and 10% yeast solution, combine after cooling, steam powdered sulfur 3 hr on each of 3 successive days, and adjust salt base to pH 2.5 using 10 N sulfuric acid. JCM’s page default 121°C for 15 min applies where not otherwise stated; it must not replace the explicit sulfur-steaming exception. No gas fraction, incubation temperature or yeast-percent basis is supplied.

### Exact source hydrates and bounded ontology conflict

grounding: concern. Targets: CultureMech:010118.

The sulfate/chloride hydrates and variable vanadyl hydrate retain explicit source forms. CHEBI:131366 has the expected canonical borax label but its captured formula 10H2O.H4B4O9.2Na and mass 417.401 differ from source Na2B4O7·10H2O. Label agreement cannot settle that structural/stoichiometric conflict. No alternate ID or molar conversion is inferred.

### Classification, role notes and organism scope

scope: supported. Targets: CultureMech:010118.

COMPLEX/UNDEFINED is consistent with yeast extract and liquid preparation. Archaea/Sulfolobales naming is collection/source context, not a strain-specific growth assertion. The record asserts no taxon, assembly, DOI/PMID or growth optimum. TOGO-derived Role/Properties notes are provider annotations; they do not establish measured nutritional mechanisms, and sulfuric acid is specifically used for pH adjustment.

### Omitted-component sibling and generated freshness

scope: concern. Targets: CultureMech:010118.

The current owner’s reciprocal M713 child path/id resolves under archaea and its sulfur omission is supported. That later owner relationship is absent from the generated target. TOGO M713’s retained sulfur-steaming comment conflicts with its own omission and must not be imported into the child. After maintained corrections, regenerate without collapsing these formulations.

### Current transform versus historical flattened output

provenance: concern. Targets: CultureMech:010118.

Current TOGO methods separate main and local stock sections, retain referenced stocks and treat concentration-only adjustment reagents separately. Their volume anchoring is an importer convention, not measured final volume. Existing history records historical defaults/migration; no importer or merge was rerun, and current code is not blamed automatically for historical output.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010118.

28 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: The represented salt base cannot reproduce the named source formulation

blocker / open / confirmed; issue key: culturemech.010118.salt-base-flattening-units.

The target/owner inflate seven milligram stock quantities to G_PER_L, represent 1 L water as 1 G_PER_L, and keep 1 G_PER_L of an empty Unknown solution while flattening its eleven solutes. This is an invalid formulation representation even though the YAML and term checks pass.

### f2: Source-specific sterilization and pH preparation are missing

major / open / confirmed; issue key: culturemech.010118.source-preparation-omitted.

The full separately sterilized base/yeast process, source autoclave default, sulfur-specific 3 hr × 3 day steaming schedule, salt-base pH 2.5 and 10 N adjustment stock are absent. These omissions materially change reproduction of the source protocol, justifying major severity for native P3.5; the 10% yeast basis and acid addition volume remain unquantified.

### f3: Borax source formula conflicts with the asserted ontology structure

major / open / confirmed; issue key: culturemech.010118.borax-structure-conflict.

CHEBI:131366 resolves with the expected label, but its captured formula 10H2O.H4B4O9.2Na/mass 417.401 is not stoichiometrically identical to source Na2B4O7·10H2O. This is a source-versus-ontology metadata conflict, not proof that the source 4.5 mg amount should change or that a guessed alternative ID is correct.

### f4: Historical sulfur MIM linkage remains unresolved

major / open / confirmed; issue key: culturemech.010118.legacy-sulfur-mim-unresolved.

The asserted MediaIngredientMech:001072 correspondence is not established by the accessible current 2953-row catalog/untruncated tree or ignored-inclusive local lookup. Primary CHEBI:33403 is valid; present CHEBI identity is not a substitute for historical numeric-ID evidence.

### f5: Amount evidence and the current sibling relationship are not retained

minor / open / confirmed; issue key: culturemech.010118.evidence-and-generated-context.

No target/owner ingredient carries attached matching source quantity evidence. The current maintained owner additionally has a valid sulfur-free child relationship that the older generated target omits. The stock helper’s eleven amount evidence objects support only that stock and cannot be transferred as final-medium evidence.

## Recommended Actions And Acceptance Checks

### a1

Restore the explicit main/salt-base hierarchy, source mg/g/L units and 1 L receiving volume with exact evidence. Keep the source stock-water basis and unquantified additions distinct from final volume; do not duplicate expanded solutes or inherit the local stock’s invalid water percentage/placeholder.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add exact source-scoped preparation and quantitative context with evidence. Keep the sulfur exception, stock-stage pH and unquantified reagent doses; never invent a yeast percentage basis or universal autoclave replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the source formula versus ontology structural annotations using authoritative supplied-material/ontology evidence before molar conversion or re-grounding. Preserve the literal source mass and document the conflict while unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover the historical exact MIM identity or explicitly retire/replace the unsupported link using verified current correspondence. Do not guess a numeric successor or treat the bounded current miss as proof that the historical record never existed.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach narrow JCM/TOGO quantity and preparation evidence to maintained claims, retain the current explicit sibling relationship, and regenerate only after the formulation corrections pass follow-up gates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/186/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/186/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml:1:id: CultureMech:010118<br>./data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml:1:id: CultureMech:010118<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/186/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 23 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| source-context | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/186/evidence-context-original.json; Frozen per-record preflight; exact source fields, owner/dependency inventories and source limitations | context_only | The preflight is diagnostic context. Its literal captures and current input bytes are independently read and assessed here; no provisional coverage or source conclusion is automatically promoted. |
| jcm691 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691; Complete main table, Salt base solution table, preparation and page-level default | supports | Exact parent formulation separates 1 L salt base, 0.5 g yeast and 1 g powdered sulfur; salt base has four gram solutes, seven milligram solutes and 1 L water, with unquantified 10 N acid to pH 2.5. The global 121°C/15 min autoclave default is distinct from sulfur steaming 3 hr on each of 3 successive days. |
| jcm693 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=693; Complete modification sentence and page-level default | supports | Exact sulfur-free source says to use Medium 691 without sulfur. It does not authorize adding the parent sulfur or its sulfur-specific steaming procedure. |
| togoM711 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711; meta, both component sections and all comments | supports | Provider preserves main/salt-base hierarchy, raw g/mg/L quantities and the 10 N adjustment reagent; it corroborates source identity, not an independent measured final volume. |
| togoM713 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M713; meta, main component rows and all comments | supports | Provider variant omits sulfur in its ingredient list and explicitly names the omission. Its copied parent sulfur-steaming comment is a source inconsistency, not a valid sulfur-free instruction. |
| mediadiveJ691api | https://mediadive.dsmz.de/rest/medium/J691; data.medium and complete solutions4597/4598 | supports | Provider names 1000 mL receiving base and 1000 mL stock basis; g_l values describe that declared convention, not an independently measured final medium after unquantified additions. |
| mediadiveJ693api | https://mediadive.dsmz.de/rest/medium/J693; data.medium and solution4600 steps | supports | Child is a step-only reference to 691 without sulfur; no direct recipe array is provided. That is not evidence for an empty medium or an unmodified parent. |
| solution4598 | https://mediadive.dsmz.de/rest/solution/4598; data.recipe[0:12], volume and step | supports | Exact standalone salt base, whose numeric source/evidence correspondence is assessed separately from any receiving medium. |
| chebi131366 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131366; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:131366 resolves to disodium tetraborate decahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:15377 resolves to water. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:26836 resolves to sulfuric acid. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:33403 resolves to elemental sulfur. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:62946 resolves to ammonium sulfate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure annotations | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. A matching nonobsolete label is not evidence that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific concerns are assessed separately. |
| mim-grounding | src/culturemech/data/mediaingredientmech/label_index.csv; Complete exact preferred_term/MAPPED lookup for every asserted current secondary key; adjacent source_commit/hash metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "matches": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_keys": [], "legacy_assertions": [{"input": "target", "field_path": "ingredients[0].mediaingredientmech_term", "id": "MediaIngredientMech:001072", "label": "Sulfur (powder)"}, {"input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml", "field_path": "ingredients[0].mediaingredientmech_term", "id": "MediaIngredientMech:001072", "label": "Sulfur (powder)"}]} |
| chemical-metadata | /private/tmp/culturemech-review-work-batch019/186/chemical-metadata-context.json; All asserted ingredient IDs/labels, formula/CAS/mass/structure fields and per-layer linkage denominators | context_only | All source-specific identity decisions are separated from canonical metadata correspondence. |
| stock-local | data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml; Complete standalone stock YAML, twelve composition rows, eleven attached evidence objects, preparation, placeholder and history | context_only | Dependency only: eleven attached amount excerpts match the exact current provider response and limit support to provider-declared stock concentrations. Water 1000 PERCENT_V_V and the separate placeholder are not valid receiving-medium instructions. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/186/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Pinned public commit6643131b0f12ab40b66f98135245fca04027e0e9; exact numeric-ID search | supports | Current source snapshot is accessible and inspected. It does not establish the historical correspondence of MediaIngredientMech:001072. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Pinned public commit6643131b0f12ab40b66f98135245fca04027e0e9; exact numeric-ID search | supports | Current source snapshot is accessible and inspected. It does not establish the historical correspondence of MediaIngredientMech:001072. |
| legacy-search | /private/tmp/culturemech-review-work-batch019/186/legacy-mim-search.json; Exact legacy-ID lookup in current pinned public catalog/tree and owned repository | context_only | The owned source retains usages but no corresponding historical identity mapping was established in the bounded search. Current CHEBI:33403 validity is a separate assertion. |
| sibling | data/normalized_yaml/archaea/TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur.yaml; Complete dependency read; exact stable ID, reciprocal parent, omission and preparation scope | context_only | Maintained M713 child omits sulfur and explicitly points to this M711 parent. It is contextual variant evidence, not a replacement recipe or a full independent review of the sibling. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation signature and merge_formulation_evidence | context_only | Current formulation-aware merge code is pinned; it was not executed or historically replayed. Existing generated targets can predate owner repairs/evidence. |
| writer-context-1 | src/culturemech/ingredients/mim_label_index.py; strong_label_key, weak_label_key, label_hydrate_count and pinned metadata | context_only | Current exact-key correspondence and explicit source hydration are separate checks. Current CHEBI keys cannot establish historical MediaIngredientMech numeric identity. |
| writer-context-2 | src/culturemech/import/togo_importer.py; _ingredient_from_item; _solution_from_item; _local_batch_volume_ml; _extract_primary_components | context_only | Current TOGO code separates primary/local stock layers and can use a water anchor or matching liquid total for a stock basis. This does not establish measured final volume and does not validate historical broad-name solution IDs. No importer executed. |
| history-metadata | data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml", "events": 14, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Historical MediaIngredientMech:001072 correspondence is required but unresolved; current catalog and repository searches completed successfully within stated bounds. This creates partial completion without changing the four canonical diagnostic results.
- No final volume, density, yeast percentage basis, acid dose, specific vanadyl hydration count, strain growth claim or replacement borax identifier was inferred. The sibling and standalone stock were inspected as bounded dependencies; they are not separately reviewed targets.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115151Z-culturemech-010118-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aerobic_sulfolobales_medium (CultureMech:010118)'
started_at: '2026-10-21T11:43:24Z'
finished_at: '2026-10-21T11:51:51Z'
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
summary: TOGO M711 resolves to JCM 691 and its sulfur-containing formulation, but
  the target/owner flatten the salt base, inflate seven milligram quantities to g/L,
  encode water and stock volume as mass, and omit source-specific preparation. Primary
  chemical metadata resolves, with a borax formula conflict and an unresolved historical
  sulfur MIM link. The current sulfur-free sibling remains a distinct variant.
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
  - path: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
    sha256: 8070e6742c358a8b1293236852fe34a903372a469f6397c81b8e810edabe46bb
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
    sha256: fc54d1027bb0f9f7b68ba69aec99a97d26205bdf0eb9708fe6b723ec8d787913
    role: context
  - path: data/normalized_yaml/archaea/TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur.yaml
    sha256: 0125ad0bd909fb0d6213eda0d2e6f63d920093f98fdae5685cb2144468a690b5
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
  selection: Task review 186; batch 019 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010118
targets:
- target_id: CultureMech:010118
  path: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  label: aerobic_sulfolobales_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/186/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/186/strict.tsv"
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010118
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
  - CultureMech:010118
- check_id: current-legacy-lookup
  name: Bounded current legacy-ID lookup
  required: false
  status: passed
  summary: Current pinned catalog/tree and ignored-inclusive local lookup completed;
    no historical identity correspondence established.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - legacy-search
  - mimPinnedCatalog
  - mimPinnedTree
- check_id: historical-legacy-correspondence
  name: Historical sulfur MIM numeric-ID correspondence
  required: true
  status: unavailable
  summary: The exact historical mapping for MediaIngredientMech:001072 was not available
    in the bounded current sources. This is distinct from a failed or unavailable
    current catalog lookup.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - legacy-search
  - mimPinnedCatalog
  - mimPinnedTree
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:15.959890Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/186/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:19.372110Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/186/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:22.830867Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:26.047151Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:51:50Z'
  support: supports
  summary: './data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml:1:id:
    CultureMech:010118

    ./data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml:1:id: CultureMech:010118

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/186/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:51:50Z'
  support: supports
  summary: 23 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5f9992bbdb312c6afbedcf1ebb8f24b9406c9213055939a03f4e97e78ffcd864
- evidence_id: source-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/186/evidence-context-original.json
  locator: Frozen per-record preflight; exact source fields, owner/dependency inventories
    and source limitations
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: The preflight is diagnostic context. Its literal captures and current input
    bytes are independently read and assessed here; no provisional coverage or source
    conclusion is automatically promoted.
  snapshot_sha256: 0d75841989f65cb931729c0979ab5db291fd7c0c68565ab0ca629058dbf374db
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
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. A matching nonobsolete label is not evidence
    that the source supplied this exact salt, hydrate, stereoisomer or material. Source-specific
    concerns are assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. A matching nonobsolete label is
    not evidence that the source supplied this exact salt, hydrate, stereoisomer or
    material. Source-specific concerns are assessed separately.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
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
- evidence_id: chebi33403
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  locator: Exact OLS obo_id, label, obsolete flag, definition, supplied-form formula/CAS/mass/structure
    annotations
  accessed_at: '2026-10-20T07:26:28.748668Z'
  support: supports
  summary: CHEBI:33403 resolves to elemental sulfur. A matching nonobsolete label
    is not evidence that the source supplied this exact salt, hydrate, stereoisomer
    or material. Source-specific concerns are assessed separately.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
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
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "matches":
    {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836":
    [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836",
    "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "missing_keys": [], "legacy_assertions": [{"input":
    "target", "field_path": "ingredients[0].mediaingredientmech_term", "id": "MediaIngredientMech:001072",
    "label": "Sulfur (powder)"}, {"input": "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml",
    "field_path": "ingredients[0].mediaingredientmech_term", "id": "MediaIngredientMech:001072",
    "label": "Sulfur (powder)"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: chemical-metadata
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/186/chemical-metadata-context.json
  locator: All asserted ingredient IDs/labels, formula/CAS/mass/structure fields and
    per-layer linkage denominators
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: All source-specific identity decisions are separated from canonical metadata
    correspondence.
  snapshot_sha256: 6704f8cf1faccf169130572866d8e4faf8521f1054cabdca8be68a7e6ffafd44
- evidence_id: stock-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml
  locator: Complete standalone stock YAML, twelve composition rows, eleven attached
    evidence objects, preparation, placeholder and history
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: 'Dependency only: eleven attached amount excerpts match the exact current
    provider response and limit support to provider-declared stock concentrations.
    Water 1000 PERCENT_V_V and the separate placeholder are not valid receiving-medium
    instructions.'
  snapshot_sha256: ae6f94eced45d7243bebb925fb5449cc385003f8dc0e210c198e6c89305dcf33
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/186/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 2060bbc8174c5ef58306dd4fdc4f8bae1cee2cc6a870de45613d9c3eafe74e91
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Pinned public commit6643131b0f12ab40b66f98135245fca04027e0e9; exact numeric-ID
    search
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Current source snapshot is accessible and inspected. It does not establish
    the historical correspondence of MediaIngredientMech:001072.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Pinned public commit6643131b0f12ab40b66f98135245fca04027e0e9; exact numeric-ID
    search
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Current source snapshot is accessible and inspected. It does not establish
    the historical correspondence of MediaIngredientMech:001072.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-search
  kind: search
  reference: /private/tmp/culturemech-review-work-batch019/186/legacy-mim-search.json
  locator: Exact legacy-ID lookup in current pinned public catalog/tree and owned
    repository
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: The owned source retains usages but no corresponding historical identity
    mapping was established in the bounded search. Current CHEBI:33403 validity is
    a separate assertion.
  snapshot_sha256: 4f9edc3f83810dc5f66da8db6b870f98b2fc97418fa133033261f360be981678
  search_scope: Owned fresh019 data/normalized_yaml and packaged MIM resources, including
    ignored/hidden files via rg --no-ignore --hidden; exact 2953-row pinned public
    catalog plus untruncated tree at 6643131b0f12ab40b66f98135245fca04027e0e9.
- evidence_id: sibling
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur.yaml
  locator: Complete dependency read; exact stable ID, reciprocal parent, omission
    and preparation scope
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Maintained M713 child omits sulfur and explicitly points to this M711 parent.
    It is contextual variant evidence, not a replacement recipe or a full independent
    review of the sibling.
  snapshot_sha256: 0125ad0bd909fb0d6213eda0d2e6f63d920093f98fdae5685cb2144468a690b5
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation signature and merge_formulation_evidence
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Current formulation-aware merge code is pinned; it was not executed or
    historically replayed. Existing generated targets can predate owner repairs/evidence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/ingredients/mim_label_index.py
  locator: strong_label_key, weak_label_key, label_hydrate_count and pinned metadata
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Current exact-key correspondence and explicit source hydration are separate
    checks. Current CHEBI keys cannot establish historical MediaIngredientMech numeric
    identity.
  snapshot_sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
- evidence_id: writer-context-2
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _solution_from_item; _local_batch_volume_ml; _extract_primary_components
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: Current TOGO code separates primary/local stock layers and can use a water
    anchor or matching liquid total for a stock basis. This does not establish measured
    final volume and does not validate historical broad-name solution IDs. No importer
    executed.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AEROBIC_SULFOLOBALES_MEDIUM.yaml; data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:51:50Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml", "events":
    14, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete primary and secondary identifier metadata
  outcome: concern
  summary: 13 distinct asserted CHEBI keys resolve to nonobsolete terms; 0 canonical-label
    mismatches. Exact current secondary lookup misses []; legacy IDs are separately
    bounded. These are identifier/linkage results, not source-form correctness.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - chemical-metadata
  - mim-grounding
  - chebi131366
  - chebi15377
  - chebi26836
  - chebi31795
  - chebi32312
  - chebi33403
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86368
  - chebi91244
  details: "{\n  \"scale\": \"0\\u2013100 percent; each denominator is that layer\\\
    u2019s direct+nested ingredient-node count, not a scientific score\",\n  \"counts\"\
    : {\n    \"target\": {\n      \"ingredient_nodes\": 15,\n      \"primary_assertions\"\
    : 13,\n      \"secondary_chebi_assertions\": 4,\n      \"legacy_assertions\":\
    \ 1,\n      \"primary_percent\": 86.66666666666667,\n      \"secondary_chebi_percent\"\
    : 26.666666666666668,\n      \"verified_current_secondary_instances\": 4,\n  \
    \    \"verified_current_secondary_percent\": 26.666666666666668\n    },\n    \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\": {\n\
    \      \"ingredient_nodes\": 15,\n      \"primary_assertions\": 13,\n      \"\
    secondary_chebi_assertions\": 4,\n      \"legacy_assertions\": 1,\n      \"primary_percent\"\
    : 86.66666666666667,\n      \"secondary_chebi_percent\": 26.666666666666668,\n\
    \      \"verified_current_secondary_instances\": 4,\n      \"verified_current_secondary_percent\"\
    : 26.666666666666668\n    }\n  }\n}"
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 36 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"name\": \"Sulfur (powder)\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; Sulfur (powder)\",\n   \
    \     \"exact_source_quote\": \"Sulfur (powder) 1.0 g\",\n        \"snapshot_sha256\"\
    : \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n    \
    \    \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Main source batch amount is numerically\
    \ preserved on the provider nominal 1000 mL basis, but attached evidence and batch\
    \ context are missing. No independently measured final volume follows from 1 L\
    \ base plus a separately prepared yeast solution.\",\n    \"local\": {\n     \
    \ \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\":\
    \ \"Source 1 g; provider stock/main declared volume 1000 mL and g_l=1. Preserve\
    \ the printed source mass or volume separately from that provider convention.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"decision\": \"\
    evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Yeast extract\
    \ (BD-Difco)\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe; Yeast extract (BD-Difco)\"\
    ,\n        \"exact_source_quote\": \"Yeast extract (BD-Difco) 0.5 g\",\n     \
    \   \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Main source batch amount is numerically\
    \ preserved on the provider nominal 1000 mL basis, but attached evidence and batch\
    \ context are missing. No independently measured final volume follows from 1 L\
    \ base plus a separately prepared yeast solution.\",\n    \"local\": {\n     \
    \ \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\"\
    : \"Source 0.5 g; provider stock/main declared volume 1000 mL and g_l=0.5. Preserve\
    \ the printed source mass or volume separately from that provider convention.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"decision\": \"\
    evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Distilled water\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"\
    correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; Distilled water\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
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
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source specifies 1 L stock water,\
    \ not 1 g/L water in the final medium. Restore the stock/preparation volume context;\
    \ do not assume density or final volume.\",\n    \"local\": {\n      \"value\"\
    : \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source 1000\
    \ ml; provider stock/main declared volume 1000 mL and g_l=None. Preserve the printed\
    \ source mass or volume separately from that provider convention.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[2].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"MgSO4・7H2O\",\n    \"\
    field_path\": \"ingredients[3].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; MgSO4・7H2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Numeric value equals the provider stock\
    \ g/L convention, but the amount belongs to the salt-base recipe and is flattened\
    \ as a final-medium claim. Restore stock scope and attach precise evidence without\
    \ inventing a final volume.\",\n    \"local\": {\n      \"value\": \"0.25\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source 0.25 g; provider\
    \ stock/main declared volume 1000 mL and g_l=0.25. Preserve the printed source\
    \ mass or volume separately from that provider convention.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[3].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CaCl2・2H2O\",\n    \"\
    field_path\": \"ingredients[4].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CaCl2・2H2O\"\
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
    ,\n        \"source_locator\": \"JCM 691 main recipe, salt base dose\",\n    \
    \    \"exact_source_quote\": \"Salt base solution (see below) 1.0 L\",\n     \
    \   \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Numeric value equals the provider stock\
    \ g/L convention, but the amount belongs to the salt-base recipe and is flattened\
    \ as a final-medium claim. Restore stock scope and attach precise evidence without\
    \ inventing a final volume.\",\n    \"local\": {\n      \"value\": \"0.07\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source 0.07 g; provider\
    \ stock/main declared volume 1000 mL and g_l=0.07. Preserve the printed source\
    \ mass or volume separately from that provider convention.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[4].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"KH2PO4\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"decision\": \"correct\",\n    \"source_snippets\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Numeric value equals the provider stock\
    \ g/L convention, but the amount belongs to the salt-base recipe and is flattened\
    \ as a final-medium claim. Restore stock scope and attach precise evidence without\
    \ inventing a final volume.\",\n    \"local\": {\n      \"value\": \"0.28\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source 0.28 g; provider\
    \ stock/main declared volume 1000 mL and g_l=0.28. Preserve the printed source\
    \ mass or volume separately from that provider convention.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[5].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Na2MoO4・2H2O\",\n  \
    \  \"field_path\": \"ingredients[6].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; Na2MoO4・2H2O\"\
    ,\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.03 mg\",\n        \"\
    snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"0.03\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 0.03 mg; provider stock/main declared volume 1000 mL and g_l=3e-05. Mass conversion\
    \ only: 0.03 mg × 0.001 = 0.00003 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[6].concentration\",\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"MnCl2・4H2O\",\n    \"\
    field_path\": \"ingredients[7].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; MnCl2・4H2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"1.8\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 1.8 mg; provider stock/main declared volume 1000 mL and g_l=0.0018. Mass conversion\
    \ only: 1.8 mg × 0.001 = 0.0018 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[7].concentration\",\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"ZnSO4・7H2O\",\n    \"\
    field_path\": \"ingredients[8].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; ZnSO4・7H2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"0.22\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 0.22 mg; provider stock/main declared volume 1000 mL and g_l=0.00022. Mass conversion\
    \ only: 0.22 mg × 0.001 = 0.00022 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[8].concentration\",\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CuCl2・2H2O\",\n    \"\
    field_path\": \"ingredients[9].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CuCl2・2H2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 0.05 mg; provider stock/main declared volume 1000 mL and g_l=5e-05. Mass conversion\
    \ only: 0.05 mg × 0.001 = 0.00005 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[9].concentration\",\n        \"decision\": \"\
    correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"(NH4)2SO4\",\n    \"\
    field_path\": \"ingredients[10].concentration\",\n    \"decision\": \"correct\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Numeric value equals the provider stock\
    \ g/L convention, but the amount belongs to the salt-base recipe and is flattened\
    \ as a final-medium claim. Restore stock scope and attach precise evidence without\
    \ inventing a final volume.\",\n    \"local\": {\n      \"value\": \"1.3\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source 1.3 g; provider\
    \ stock/main declared volume 1000 mL and g_l=1.3. Preserve the printed source\
    \ mass or volume separately from that provider convention.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[10].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"CoSO4・7H2O\",\n    \"\
    field_path\": \"ingredients[11].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; CoSO4・7H2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"0.01\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 0.01 mg; provider stock/main declared volume 1000 mL and g_l=1e-05. Mass conversion\
    \ only: 0.01 mg × 0.001 = 0.00001 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[11].concentration\",\n        \"decision\":\
    \ \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"VOSO4・xH2O\",\n    \"\
    field_path\": \"ingredients[12].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; VOSO4・xH2O\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"0.03\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 0.03 mg; provider stock/main declared volume 1000 mL and g_l=3e-05. Mass conversion\
    \ only: 0.03 mg × 0.001 = 0.00003 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[12].concentration\",\n        \"decision\":\
    \ \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Na2B4O7・10H2O\",\n \
    \   \"field_path\": \"ingredients[13].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution table; Na2B4O7・10H2O\"\
    ,\n        \"exact_source_quote\": \"Na 2 B 4 O 7 ·10H 2 O 4.5 mg\",\n       \
    \ \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
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
    : \"JCM 691 main recipe, salt base dose\",\n        \"exact_source_quote\": \"\
    Salt base solution (see below) 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"jcm691\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\",\n        \"source_locator\"\
    : \"JCM 691 salt base table, water amount\",\n        \"exact_source_quote\":\
    \ \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"The source milligram number is copied\
    \ unchanged as G_PER_L and the salt-base stage is flattened. Correct the unit\
    \ and restore stock scope; it is 1000 times the provider stock g/L number, not\
    \ a verified final-medium concentration.\",\n    \"local\": {\n      \"value\"\
    : \"4.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"arithmetic\": \"Source\
    \ 4.5 mg; provider stock/main declared volume 1000 mL and g_l=0.0045. Mass conversion\
    \ only: 4.5 mg × 0.001 = 0.0045 g; provider g/L uses its declared stock basis.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[13].concentration\",\n        \"decision\":\
    \ \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Sulfuric acid adjustment\
    \ dose\",\n    \"field_path\": \"ingredients[14].concentration\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation\",\n \
    \       \"exact_source_quote\": \"Adjust pH to 2.5 with 10 N H 2 SO 4 .\",\n \
    \       \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      },\n      {\n        \"source_key\": \"togoM711\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711\",\n \
    \       \"source_locator\": \"$.components[1].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\",\\n          \\\"conc_value\\\": 10,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"21e1c43c188e1fd1b950b66e33c5a4f5d698a04261d62fce00a810f953e10b3a\"\
    \n      }\n    ],\n    \"rationale\": \"Source acid strength is 10 N, but the\
    \ addition volume is not quantified. VARIABLE correctly avoids a fixed dose; the\
    \ stock strength, pH endpoint and titration stage still need evidence and cannot\
    \ be replaced by 10 N final medium.\",\n    \"local\": {\n      \"value\": \"\
    variable\",\n      \"unit\": \"VARIABLE\"\n    },\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"decision\"\
    : \"not_quantified\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Salt-base receiving\
    \ addition\",\n    \"field_path\": \"solutions[0].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 main recipe, salt base dose\",\n    \
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
    \n      },\n      {\n        \"source_key\": \"togoM711\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M711\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Salt base solution (see below)\\\",\\n       \
    \   \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"21e1c43c188e1fd1b950b66e33c5a4f5d698a04261d62fce00a810f953e10b3a\"\n     \
    \ }\n    ],\n    \"rationale\": \"The exact source supplies 1 L salt base, not\
    \ 1 G_PER_L of Unknown solution. Its named composition is given in the source\
    \ and must be represented once, separately from the final medium.\",\n    \"local\"\
    : {\n      \"preferred_term\": \"Salt base solution (see below)\",\n      \"composition\"\
    : [],\n      \"concentration\": {\n        \"value\": \"1\",\n        \"unit\"\
    : \"G_PER_L\"\n      },\n      \"name\": \"Unknown solution\"\n    },\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"solutions[0]\",\n        \"decision\": \"correct\"\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0]\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"name\": \"Autoclave temperature\",\n    \"\
    field_path\": \"preparation.autoclave.temperature\",\n    \"decision\": \"add\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 page-level default; salt base and yeast\
    \ separately\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\",\n        \"\
    parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\"\
    ,\n    \"arithmetic\": \"Source value: 121°C; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.autoclave.temperature\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
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
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\"\
    ,\n    \"arithmetic\": \"Source value: 15 min; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.autoclave.duration\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
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
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\
    \ The 10% basis and resulting physical addition volume are unspecified; do not\
    \ infer w/v or calculate a final dilution.\",\n    \"arithmetic\": \"Source value:\
    \ 10%; no conversion.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation.yeast_solution.strength\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation.yeast_solution.strength\",\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Sulfur steaming\
    \ duration\",\n    \"field_path\": \"preparation.sulfur_steam.duration\",\n  \
    \  \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 parent sulfur-specific preparation\"\
    ,\n        \"exact_source_quote\": \"Steam sulfur for 3 hr on each of 3 successive\
    \ days.\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\"\
    ,\n    \"arithmetic\": \"Source value: 3 hr; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.sulfur_steam.duration\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation.sulfur_steam.duration\",\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Sulfur steaming\
    \ repetitions\",\n    \"field_path\": \"preparation.sulfur_steam.repetitions\"\
    ,\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm691\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 parent sulfur-specific preparation\"\
    ,\n        \"exact_source_quote\": \"Steam sulfur for 3 hr on each of 3 successive\
    \ days.\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\"\
    ,\n    \"arithmetic\": \"Source value: 3 successive days; no conversion.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation.sulfur_steam.repetitions\",\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation.sulfur_steam.repetitions\",\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Salt base\
    \ pH endpoint\",\n    \"field_path\": \"preparation.salt_base.pH\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation\",\n \
    \       \"exact_source_quote\": \"Adjust pH to 2.5 with 10 N H 2 SO 4 .\",\n \
    \       \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.\"\
    ,\n    \"arithmetic\": \"Source value: 2.5; no conversion.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation.salt_base.pH\"\
    ,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation.salt_base.pH\",\n        \"decision\"\
    : \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Adjustment acid strength\"\
    ,\n    \"field_path\": \"preparation.salt_base.acid_strength\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm691\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=691\"\
    ,\n        \"source_locator\": \"JCM 691 Salt base solution preparation; dose\
    \ not quantified\",\n        \"exact_source_quote\": \"Adjust pH to 2.5 with 10\
    \ N H 2 SO 4 .\",\n        \"snapshot_sha256\": \"d3293b3a572a899b1971e8da7046252ff521df300921ac067ec906e2cf51e788\"\
    ,\n        \"parsed_text_sha256\": \"6bd2f10e56f1ba9d12cdd1d07eae603e8e6c594ded8c3296ab6e671e513fcb9c\"\
    \n      }\n    ],\n    \"rationale\": \"Source-supported preparation context is\
    \ absent in both reviewed layers. Preserve its specific stage and attach evidence.10\
    \ N is the adjustment reagent strength, not its unquantified dose or a final-medium\
    \ concentration.\",\n    \"arithmetic\": \"Source value: 10 N; no conversion.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation.salt_base.acid_strength\",\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation.salt_base.acid_strength\",\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"name\": \"Dependency stock:\
    \ (NH4)2SO4\",\n    \"field_path\": \"data/normalized_yaml/bacterial/mediadive_4598_Salt_base_solution.yaml::composition[0].concentration\"\
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
  topic: TOGO M711, JCM 691 and current maintained owner
  outcome: supported
  summary: TOGO meta explicitly maps M711 to JCM_M691 and its collection URL. Target
    and owner denote the sulfur-containing parent; the sulfur-free JCM 693/TOGO M713
    sibling is a separate omitted-component variant. Current main source content is
    available.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - togoM711
  - jcm691
  - jcm693
  - togoM713
- assessment_id: stock-scopes
  area: quantity
  topic: All local amounts and dependency boundaries
  outcome: concern
  summary: Seven trace stock values retain milligram numbers as G_PER_L; water 1 L
    and salt-base 1 L also become 1 G_PER_L. Eleven stock solutes are flattened while
    the remaining salt-base descriptor has an empty composition and unknown name.
    Main yeast/sulfur amounts are nominal provider concentrations, not independently
    measured final-volume quantities. The complete inventory distinguishes every target/owner
    value, source-only preparation quantity and standalone dependency row.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - jcm691
  - togoM711
  - mediadiveJ691api
  - solution4598
  - stock-local
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Separate stock preparation and source conditions
  outcome: concern
  summary: 'Both reviewed layers omit the full source protocol: separately autoclave
    salt base and 10% yeast solution, combine after cooling, steam powdered sulfur
    3 hr on each of 3 successive days, and adjust salt base to pH 2.5 using 10 N sulfuric
    acid. JCM’s page default 121°C for 15 min applies where not otherwise stated;
    it must not replace the explicit sulfur-steaming exception. No gas fraction, incubation
    temperature or yeast-percent basis is supplied.'
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - jcm691
  - togoM711
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
  - CultureMech:010118
  evidence_ids:
  - record
  - jcm691
  - solution4598
  - chebi131366
  - chemical-metadata
- assessment_id: classification
  area: scope
  topic: Classification, role notes and organism scope
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with yeast extract and liquid preparation.
    Archaea/Sulfolobales naming is collection/source context, not a strain-specific
    growth assertion. The record asserts no taxon, assembly, DOI/PMID or growth optimum.
    TOGO-derived Role/Properties notes are provider annotations; they do not establish
    measured nutritional mechanisms, and sulfuric acid is specifically used for pH
    adjustment.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - jcm691
  - togoM711
- assessment_id: relationships
  area: scope
  topic: Omitted-component sibling and generated freshness
  outcome: concern
  summary: The current owner’s reciprocal M713 child path/id resolves under archaea
    and its sulfur omission is supported. That later owner relationship is absent
    from the generated target. TOGO M713’s retained sulfur-steaming comment conflicts
    with its own omission and must not be imported into the child. After maintained
    corrections, regenerate without collapsing these formulations.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - sibling
  - jcm693
  - togoM713
- assessment_id: generation
  area: provenance
  topic: Current transform versus historical flattened output
  outcome: concern
  summary: Current TOGO methods separate main and local stock sections, retain referenced
    stocks and treat concentration-only adjustment reagents separately. Their volume
    anchoring is an importer convention, not measured final volume. Existing history
    records historical defaults/migration; no importer or merge was rerun, and current
    code is not blamed automatically for historical output.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - owner-0
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 28 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010118
  evidence_ids:
  - record
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.010118.salt-base-flattening-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: The represented salt base cannot reproduce the named source formulation
  description: The target/owner inflate seven milligram stock quantities to G_PER_L,
    represent 1 L water as 1 G_PER_L, and keep 1 G_PER_L of an empty Unknown solution
    while flattening its eleven solutes. This is an invalid formulation representation
    even though the YAML and term checks pass.
  target_ids:
  - CultureMech:010118
  field_paths:
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - solutions[0]
  evidence_ids:
  - record
  - owner-0
  - jcm691
  - togoM711
  - mediadiveJ691api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  issue_key: culturemech.010118.source-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-specific sterilization and pH preparation are missing
  description: The full separately sterilized base/yeast process, source autoclave
    default, sulfur-specific 3 hr × 3 day steaming schedule, salt-base pH 2.5 and
    10 N adjustment stock are absent. These omissions materially change reproduction
    of the source protocol, justifying major severity for native P3.5; the 10% yeast
    basis and acid addition volume remain unquantified.
  target_ids:
  - CultureMech:010118
  field_paths:
  - preparation_steps
  - ph_value
  - solutions[0]
  - ingredients[14]
  evidence_ids:
  - record
  - owner-0
  - jcm691
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.010118.borax-structure-conflict
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Borax source formula conflicts with the asserted ontology structure
  description: CHEBI:131366 resolves with the expected label, but its captured formula
    10H2O.H4B4O9.2Na/mass 417.401 is not stoichiometrically identical to source Na2B4O7·10H2O.
    This is a source-versus-ontology metadata conflict, not proof that the source
    4.5 mg amount should change or that a guessed alternative ID is correct.
  target_ids:
  - CultureMech:010118
  field_paths:
  - ingredients[13].term
  evidence_ids:
  - record
  - jcm691
  - togoM711
  - chebi131366
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  issue_key: culturemech.010118.legacy-sulfur-mim-unresolved
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Historical sulfur MIM linkage remains unresolved
  description: The asserted MediaIngredientMech:001072 correspondence is not established
    by the accessible current 2953-row catalog/untruncated tree or ignored-inclusive
    local lookup. Primary CHEBI:33403 is valid; present CHEBI identity is not a substitute
    for historical numeric-ID evidence.
  target_ids:
  - CultureMech:010118
  field_paths:
  - ingredients[0].mediaingredientmech_term
  evidence_ids:
  - record
  - owner-0
  - chebi33403
  - legacy-search
  - mimPinnedCatalog
  - mimPinnedTree
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.010118.evidence-and-generated-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Amount evidence and the current sibling relationship are not retained
  description: No target/owner ingredient carries attached matching source quantity
    evidence. The current maintained owner additionally has a valid sulfur-free child
    relationship that the older generated target omits. The stock helper’s eleven
    amount evidence objects support only that stock and cannot be transferred as final-medium
    evidence.
  target_ids:
  - CultureMech:010118
  field_paths:
  - ingredients
  - solutions
  - variant_children
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - sibling
  - stock-local
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  description: Restore the explicit main/salt-base hierarchy, source mg/g/L units
    and 1 L receiving volume with exact evidence. Keep the source stock-water basis
    and unquantified additions distinct from final volume; do not duplicate expanded
    solutes or inherit the local stock’s invalid water percentage/placeholder.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  description: Add exact source-scoped preparation and quantitative context with evidence.
    Keep the sulfur exception, stock-stage pH and unquantified reagent doses; never
    invent a yeast percentage basis or universal autoclave replacement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  description: Resolve the source formula versus ontology structural annotations using
    authoritative supplied-material/ontology evidence before molar conversion or re-grounding.
    Preserve the literal source mass and document the conflict while unresolved.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  description: Recover the historical exact MIM identity or explicitly retire/replace
    the unsupported link using verified current correspondence. Do not guess a numeric
    successor or treat the bounded current miss as proof that the historical record
    never existed.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
  description: Attach narrow JCM/TOGO quantity and preparation evidence to maintained
    claims, retain the current explicit sibling relationship, and regenerate only
    after the formulation corrections pass follow-up gates.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M711_Aerobic_Sulfolobales_Medium.yaml
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
- Historical MediaIngredientMech:001072 correspondence is required but unresolved;
  current catalog and repository searches completed successfully within stated bounds.
  This creates partial completion without changing the four canonical diagnostic results.
- No final volume, density, yeast percentage basis, acid dose, specific vanadyl hydration
  count, strain growth claim or replacement borax identifier was inferred. The sibling
  and standalone stock were inspected as bounded dependencies; they are not separately
  reviewed targets.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
