# Source and formulation review: anaerobic_brain_heart_infusion_broth (CultureMech:010151)

- Review: 20261021T195019Z-culturemech-010151-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:39:58Z
- Finished UTC: 2026-10-21T19:50:19Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 723 and TOGO M746 specify 37 g of commercial brain heart infusion broth, 1 L water and two separate 5 ml/L reducing-stock additions. The maintained input and generated target replace the premix with an unauthenticated constituent breakdown, retain wrong liquid units and omit preparation. Required manufacturer-specific formulation evidence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 356; batch 036 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-five task batches contain 350 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 353 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010151 | data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml | generated | anaerobic_brain_heart_infusion_broth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010151 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010151 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/356/strict.tsv |
| validate-terms | passed | True | CultureMech:010151 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010151 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010151 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: bd237500bio | unavailable | True | CultureMech:010151 | Exact manufacturer-specific quantitative composition of BD 237500 remains unavailable: raw product/IFU attempts returned 403, the legacy IFU host failed DNS and the manual URL returned 404. The separately preserved parsed page supports limited product identity only. This required formulation uncertainty makes the review partial; it does not negate the available JCM recipe. |
| Exact source content access: mediadiveJ723 | unavailable | False | CultureMech:010151 | Both optional current MediaDive J723 requests returned 503; original failures and retry remain preserved. Exact JCM 723 and TOGO M746 content independently support the main recipe and its reducing-stock instructions. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010151.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010151.

22 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "JCM 723 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 1; Distilled water / 1.0 / L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      }
    ],
    "interpretation": "The source adds 1.0 L of water. Both local layers instead store 1 G_PER_L; preserve the volume without claiming a measured final medium volume."
  },
  {
    "decision_id": "q2",
    "ingredient": "Commercial brain heart infusion broth premix",
    "decision": "add",
    "stage": "JCM 723 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Brain heart infusion broth (BD-Difco)\",\n          \"volume\": 37,\n          \"unit\": \"g\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      }
    ],
    "interpretation": "Restore an explicitly identified 37 g BD-Difco premix at source batch scope, replacing the unsupported decomposition rather than double-counting premix and presumed constituents. The primary does not give a catalog number or constituent amounts."
  },
  {
    "decision_id": "q3",
    "ingredient": "Calf brain infusion",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "infusion from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table; distinct powder names and amounts",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The local VARIABLE amount and 200 g/L tissue-equivalent note are not authenticated for this product. The inspected article does not state that tissue equivalence. Do not interpret it as tissue weighed into the broth or replace it with an assumed powder conversion."
  },
  {
    "decision_id": "q4",
    "ingredient": "Beef heart infusion",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "infusion from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent of Brain Heart Infusion commercial product"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table; distinct powder names and amounts",
        "exact_source_quote": "HM infusion powder 12.500 BHI powder 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The local VARIABLE amount and 250 g/L tissue-equivalent note are not authenticated for this product. The inspected article does not state that tissue equivalence. Do not interpret it as tissue weighed into the broth or replace it with an assumed powder conversion."
  },
  {
    "decision_id": "q5",
    "ingredient": "Proteose peptone",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table under Ingredients Gms/liter",
        "exact_source_quote": "Proteose peptone 10.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The number matches the cited secondary agar formulation, but neither that article nor JCM 723 establishes this constituent concentration in the asserted BD 237500 broth. Preserve the uncertainty rather than marking the local claim verified or silently substituting another formulation."
  },
  {
    "decision_id": "q6",
    "ingredient": "Dextrose",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table under Ingredients Gms/liter",
        "exact_source_quote": "Dextrose (Glucose) 2.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The number matches the cited secondary agar formulation, but neither that article nor JCM 723 establishes this constituent concentration in the asserted BD 237500 broth. Preserve the uncertainty rather than marking the local claim verified or silently substituting another formulation."
  },
  {
    "decision_id": "q7",
    "ingredient": "Sodium chloride",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table under Ingredients Gms/liter",
        "exact_source_quote": "Sodium chloride 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The number matches the cited secondary agar formulation, but neither that article nor JCM 723 establishes this constituent concentration in the asserted BD 237500 broth. Preserve the uncertainty rather than marking the local claim verified or silently substituting another formulation."
  },
  {
    "decision_id": "q8",
    "ingredient": "Disodium phosphate",
    "decision": "unsupported",
    "stage": "Local commercial-product decomposition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table under Ingredients Gms/liter",
        "exact_source_quote": "Disodium phosphate 2.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The number matches the cited secondary agar formulation, but neither that article nor JCM 723 establishes this constituent concentration in the asserted BD 237500 broth. Preserve the uncertainty rather than marking the local claim verified or silently substituting another formulation."
  },
  {
    "decision_id": "q9",
    "ingredient": "N2 atmosphere quantity",
    "decision": "not_quantified",
    "stage": "Main preparation and reducing-stock storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Preparation sentence before reducer additions",
        "exact_source_quote": "Prepare the medium anaerobically under a N 2 atmosphere.",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"N2\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      }
    ],
    "interpretation": "The source names N2 but gives no fraction, volume, flow or pressure. VARIABLE is an honest unquantified amount; do not turn the gas name into 100%. Attach the preparation stage separately."
  },
  {
    "decision_id": "q10",
    "ingredient": "Sodium sulfide nonahydrate stock dose",
    "decision": "correct",
    "stage": "Aseptic anaerobic addition before inoculation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Receiving-medium denominator and timing sentence",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "The source dose is 5.0 ml per liter of receiving medium, not 5 G_PER_L. Represent the stock addition separately from its strength and named hydrate; do not infer a solute mass or final concentration."
  },
  {
    "decision_id": "q11",
    "ingredient": "Sodium sulfide nonahydrate stock strength",
    "decision": "add",
    "stage": "Separate reducing stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[8].preferred_term",
        "stored": "5% Na2S・9H2O"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[8].preferred_term",
        "stored": "5% Na2S・9H2O"
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Receiving-medium denominator and timing sentence",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "The name retains 5%, but a separate stock representation is absent. Preserve 5% without assigning w/v, v/v or density: neither primary nor provider qualifies the percentage basis. Do not infer a stock batch volume."
  },
  {
    "decision_id": "q12",
    "ingredient": "L-cysteine hydrochloride monohydrate stock dose",
    "decision": "correct",
    "stage": "Aseptic anaerobic addition before inoculation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"5% L--Cysteine・HCl・H2O\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Receiving-medium denominator and timing sentence",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "The source dose is 5.0 ml per liter of receiving medium, not 5 G_PER_L. Represent the stock addition separately from its strength and named hydrate; do not infer a solute mass or final concentration."
  },
  {
    "decision_id": "q13",
    "ingredient": "L-cysteine hydrochloride monohydrate stock strength",
    "decision": "add",
    "stage": "Separate reducing stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[9].preferred_term",
        "stored": "5% L--Cysteine・HCl・H2O"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[9].preferred_term",
        "stored": "5% L--Cysteine・HCl・H2O"
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "togoM746original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"5% L--Cysteine・HCl・H2O\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Receiving-medium denominator and timing sentence",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "The name retains 5%, but a separate stock representation is absent. Preserve 5% without assigning w/v, v/v or density: neither primary nor provider qualifies the percentage basis. Do not infer a stock batch volume."
  },
  {
    "decision_id": "q14",
    "ingredient": "Stock preparation volumes and final solute concentrations",
    "decision": "not_quantified",
    "stage": "Two separate reducing stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      }
    ],
    "interpretation": "The source supplies stock strengths and doses only. Stock solvent amounts, batch volumes and mass-based final concentrations are unspecified; the hydrate names do not supply the missing percentage basis."
  },
  {
    "decision_id": "q15",
    "ingredient": "Final pH 7.4 ± 0.2 claim",
    "decision": "unsupported",
    "stage": "Local phosphate note versus secondary agar pH",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "pH buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial product"
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar composition table; temperature-qualified pH",
        "exact_source_quote": "Final pH (at 25°C): 7.4±0.2",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      }
    ],
    "interpretation": "The current local note transfers the agar article pH to the broth without product-specific evidence and omits its 25°C measurement qualifier. JCM 723 states no pH. Do not promote this note to an authenticated final pH or infer a culture temperature."
  },
  {
    "decision_id": "q16",
    "ingredient": "Autoclave temperature and duration",
    "decision": "add",
    "stage": "JCM 723 displayed default and expressly autoclaved stages",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Exact-page default sterilization statement",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "Record the exact-page 121°C for 15 min default with the appropriate autoclaved stages. Pressure is not specified by JCM 723; do not import the secondary agar article pressure or cooling conditions."
  },
  {
    "decision_id": "q17",
    "ingredient": "Reducer timing and storage atmosphere",
    "decision": "add",
    "stage": "Before inoculation; separate autoclaved reducing stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Complete pre-inoculation reducer instruction",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions (autoclaved and stored under a N 2 atmosphere) aseptically and anaerobically:",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "Retain the receiving-liter denominator, separate autoclaving, N2 storage and aseptic anaerobic addition. Storage duration and temperature are unquantified; package-storage metadata must not become stock-storage or culture conditions."
  },
  {
    "decision_id": "q18",
    "ingredient": "Measured final medium volume",
    "decision": "not_quantified",
    "stage": "Basal medium followed by per-liter reducing-stock additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 1; Distilled water / 1.0 / L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "Receiving-liter instruction",
        "exact_source_quote": "Prior to inoculation, add per liter the following solutions",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7",
        "parsed_text_sha256": "ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8"
      }
    ],
    "interpretation": "One liter of water plus commercial solids is a preparation amount, not a measured final volume. Both 5 ml/L additions retain their explicit receiving basis; do not assert that a measured final 1010 ml or a final premix g/L was provided."
  },
  {
    "decision_id": "q19",
    "ingredient": "HM infusion powder in secondary article",
    "decision": "unsupported",
    "stage": "Secondary BHI agar formula only; excluded from JCM 723 transfer",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Composition table headed Ingredients Gms/liter",
        "exact_source_quote": "HM infusion powder 12.500",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      }
    ],
    "interpretation": "This is an explicit amount in a different agar formulation. It neither supplies a manufacturer-verified broth constituent nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact product evidence before any decomposition."
  },
  {
    "decision_id": "q20",
    "ingredient": "BHI powder in secondary article",
    "decision": "unsupported",
    "stage": "Secondary BHI agar formula only; excluded from JCM 723 transfer",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Composition table headed Ingredients Gms/liter",
        "exact_source_quote": "BHI powder 5.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      }
    ],
    "interpretation": "This is an explicit amount in a different agar formulation. It neither supplies a manufacturer-verified broth constituent nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact product evidence before any decomposition."
  },
  {
    "decision_id": "q21",
    "ingredient": "Agar in secondary article",
    "decision": "unsupported",
    "stage": "Secondary BHI agar formula only; excluded from JCM 723 transfer",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Distilled water",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "notes": "Role: Solvating media; Properties: Defined component, Inorganic compound, Simple component",
            "term": {
              "id": "CHEBI:15377",
              "label": "water"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15377",
              "label": "water"
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
          },
          {
            "preferred_term": "N2",
            "notes": "Properties: Gas",
            "concentration": {
              "value": "variable",
              "unit": "VARIABLE"
            },
            "term": {
              "id": "CHEBI:17997",
              "label": "dinitrogen"
            }
          },
          {
            "preferred_term": "5% Na2S・9H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution"
          },
          {
            "preferred_term": "5% L--Cysteine・HCl・H2O",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Defined component, Organic compound, Solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "Composition table headed Ingredients Gms/liter",
        "exact_source_quote": "Agar 15.000",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      },
      {
        "source_key": "jcm723",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723",
        "source_locator": "JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Brain heart infusion broth (BD-Difco)                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7"
      }
    ],
    "interpretation": "This is an explicit amount in a different agar formulation. It neither supplies a manufacturer-verified broth constituent nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact product evidence before any decomposition."
  },
  {
    "decision_id": "q22",
    "ingredient": "Secondary article total and preparation conditions",
    "decision": "unsupported",
    "stage": "Secondary agar preparation only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "microbenotesBHI",
        "source_url": "https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "source_locator": "BHI agar preparation paragraph",
        "exact_source_quote": "Suspend 52.0 grams in 1000 ml distilled water. Heat to boiling to dissolve the medium completely. Sterilize by autoclaving at 15 lbs pressure (121°C) for 15 minutes. Cool to 45-50°C.",
        "snapshot_sha256": "b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01",
        "parsed_text_sha256": "051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59"
      }
    ],
    "interpretation": "The article total 52 g includes its 15 g agar; subtracting it is not authentication of BD 237500 constituent composition. Its 1000 ml, 15 lbs pressure and 45–50°C cooling belong to agar preparation and do not transfer to this broth. JCM default temperature/time has its own independent support."
  }
]

### Mixed-ontology labels and supplied material scope

grounding: concern. Targets: CultureMech:010151.

All eight distinct asserted primary IDs and the water secondary key have matching nonobsolete metadata. Target linkage is 8/10 primary (80%) and 1/10 secondary (10%), not a correctness score. UBERON brain and heart denote anatomy rather than a manufactured infusion; they do not establish species, tissue-equivalent mass or product formulation. MICRO proteose peptone and CHEBI dextrose/D-glucose, sodium chloride and disodium phosphate are valid name correspondences within the qualified article only; phosphate hydration and the exact broth composition remain unverified. The two stock names retain source hydrate identity but have no primary or secondary links in these layers.

### Exact culture-medium and commercial-source identity

identity: concern. Targets: CultureMech:010151.

The target and sole bacterial owner are CultureMech:010151, TOGO M746 and JCM 723. The specialized namesake CultureMech:015416 is excluded by exact stable ID and import provenance. JCM calls for a BD-Difco commercial broth; it does not identify catalog 237500 or a constituent formula. The parsed manufacturer page supports the catalog product as an agar-free BHI bottle, while the supplied product_url is a secondary agar article. Full catalog formulation/version correspondence remains unresolved.

### Commercial product and reducing stocks

representation: concern. Targets: CultureMech:010151.

The six inferred commercial constituents replace the source 37 g premix. Current article table values are not exact broth-product evidence, and neither inspected article nor primary contains the local 200/250 g/L tissue-equivalence claims. Water and reducer units are wrong. Reducing-stock names retain strengths and hydrate names, but the record lacks distinct stock composition, receiving dose and unqualified percentage-basis handling.

### Anaerobic preparation, sterilization and pH

completeness: concern. Targets: CultureMech:010151.

Both layers omit the exact JCM anaerobic preparation, displayed 121°C/15 min default, separate stock autoclaving/N2 storage and aseptic addition before inoculation. JCM gives no final pH; the phosphate note borrows the secondary agar pH. No source-specific gas fraction, pressure, measured final volume or incubation condition is inferred.

### Mixture state and biological assertions

scope: supported. Targets: CultureMech:010151.

COMPLEX/UNDEFINED and LIQUID are consistent with the exact commercial-broth source. Bacterial category and generic cultivation application are not organism-specific growth evidence. The agar article organisms, incubation temperatures, supplements and clinical uses do not transfer to this anaerobic broth.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010151.

17 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained correction surface

ownership: supported. Targets: CultureMech:010151.

The sole maintained bacterial owner is the correction surface, followed by authorized merge regeneration. Its full import history matches this target; the specialized same-basename record is not a contributor or substitute. Preserve old history, append any later source-backed curation, and do not edit the generated target directly.

### Claim attachment and historical product provenance

evidence: concern. Targets: CultureMech:010151.

Neither reviewed layer has attached amount/preparation evidence. JCM and TOGO support the premix and reducer stages, while the local product-specification note and secondary URL cannot authenticate its constituent claims. Required exact manufacturer quantitative formulation remains unavailable after preserved attempts; the limited parsed identity response is not promoted to a raw formulation capture.

## Findings

### f1: Unauthenticated constituents replace the commercial premix

blocker / open / confirmed; issue key: culturemech.010151.commercial-premix-decomposition.

Both layers omit the source 37 g BD-Difco premix and replace it with six presumed constituents. The secondary agar article does not authenticate BD 237500 broth composition, and it contains neither local tissue-equivalence amount. Anatomy terms and a catalog number do not supply that missing formulation evidence.

### f2: Water and reducing-stock doses have mass units

major / open / confirmed; issue key: culturemech.010151.liquid-units-stock-scope.

The source 1 L water is stored as 1 G_PER_L; both 5 ml/L reducing-stock doses are stored as 5 G_PER_L. Their 5% strengths lack an explicit percentage basis and must remain separate from dose and solute identity.

### f3: Preparation is absent and the pH note comes from an agar source

major / open / confirmed; issue key: culturemech.010151.preparation-and-ph-scope.

Anaerobic handling, default sterilization and pre-inoculation reducer stages are missing. The phosphate note asserts final pH 7.4 ± 0.2 from a different agar formulation, without exact broth support.

### f4: Historical product claims lack claim-level evidence

minor / open / confirmed; issue key: culturemech.010151.claim-evidence-provenance.

Source URLs, a March 28 access note and import history do not attach exact amounts, preparation or product-version support. Current source reads cannot reconstruct the absent historical specification.

## Recommended Actions And Acceptance Checks

### a1

Restore the source-identified premix and its 37 g batch amount, or obtain exact manufacturer formulation/version evidence before retaining any decomposition. Keep organ-source descriptions distinct from manufactured infusion identity and do not double-count constituents with the premix.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct water and stock-dose units, structure the two reducing stocks with exact source hydrate names, and retain the explicit per-liter receiving basis without invented percentage basis, stock recipe or final concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add exact JCM preparation and stock-handling evidence; qualify or remove the unsupported broth pH claim until product-specific evidence is obtained. Do not transfer agar cooling, pressure, incubation or growth conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow source snippets with exact capture hashes, dates and stage locators after curation. Preserve inaccessible manufacturer attempts and append a transparent provenance clarification without rewriting historical events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch036/356/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/356/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml:1:id: CultureMech:010151<br>./data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml:1:id: CultureMech:010151<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch036/source-preflight-bound/356/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 22 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| jcm723 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723; Complete exact recipe, both reducer rows and displayed default sterilization | supports | The exact primary specifies a commercial premix rather than its constituent formula; both reducer doses are explicitly per liter. |
| togo746 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746; $.meta.original_media_id and complete components/comments | supports | Exact M746 to JCM 723 identity and original commercial-product representation. |
| agar-article | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Composition of Brain Heart Infusion (BHI) Agar; table and pH statement | refutes | This is a secondary agar formulation. It does not authenticate the BD 237500 broth formula or the locally asserted tissue-equivalent amounts. |
| bound-scope-correction | /private/tmp/culturemech-review-work-batch036/source-preflight-bound/356/batch036-tail-356-source-scope-addendum.json; $.source_context[2].observation | context_only | The current article has no 200 g or 250 g tissue-equivalence statements. Those amounts are local assertions only, unsupported by the inspected article; the original cache interpretation is superseded at this exact locator. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch036/356/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, definition and structural annotations | supports | CHEBI:15377 resolves to water. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955; Exact OLS obo_id, canonical label, definition and structural annotations | supports | UBERON:0000955 resolves to brain. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; Exact OLS obo_id, canonical label, definition and structural annotations | supports | UBERON:0000948 resolves to heart. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; Exact OLS obo_id, canonical label, definition and structural annotations | supports | MICRO:0000180 resolves to proteose peptone. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, definition and structural annotations | supports | CHEBI:17634 resolves to D-glucose. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, definition and structural annotations | supports | CHEBI:26710 resolves to sodium chloride. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, definition and structural annotations | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, definition and structural annotations | supports | CHEBI:17997 resolves to dinitrogen. Identifier validity does not authenticate commercial constituent quantities or make an anatomy class equivalent to an infusion product. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch036/356/grounding-inventory.json; Every primary and secondary slot in the target and exact bacterial owner | context_only | Eight primary links and one secondary link per ten ingredient instances; all labels match their exact nonobsolete ontology responses. No excluded specialized-owner grounding is inherited. |
| mim-water | src/culturemech/data/mediaingredientmech/label_index.csv; Exact current CHEBI:15377 preferred-term MAPPED rows; all other secondary slots absent in both reviewed layers | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| manufacturer-parsed-identity | /private/tmp/culturemech-review-source-preflight-batch036-tail/356/bd-product-web-tool-scoped-response.json; $.tool_response, lines 712 and 765–771; separately captured parsed public response | context_only | The preserved parsed manufacturer response identifies BD Bacto BHI, bottle 500 g, and Contains Agar &#124; No. It supplies limited product identity, not numerical constituent formulation, original raw HTTP authentication or the March 2026 product version. Package size, shelf life and package storage are not medium quantities or growth conditions. |
| history-metadata | data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml", "events": 8, "timestamp_issues": []}] |
| commercial-writer-search | /private/tmp/culturemech-review-source-preflight-batch036-tail/356/commercial-writer-search.json; Ignored-inclusive owned-checkout Python/shell search for catalog 237500, exact composition statement and commercial-product marker | context_only | The bounded search did not identify the original March 28 BHI decomposition writer. Related current repairs do not authenticate this product or establish historical causation. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current static implementation only: import supports explicit solution sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup require source-stage review. These paths do not prove the historical execution that produced the commercial breakdown or authorize a guessed percentage basis. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current static implementation only: import supports explicit solution sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup require source-stage review. These paths do not prove the historical execution that produced the commercial breakdown or authorize a guessed percentage basis. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current static implementation only: import supports explicit solution sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup require source-stage review. These paths do not prove the historical execution that produced the commercial breakdown or authorize a guessed percentage basis. |
| writer-3 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current static implementation only: import supports explicit solution sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup require source-stage review. These paths do not prove the historical execution that produced the commercial breakdown or authorize a guessed percentage basis. |
| bd237500bio-attempt | https://www.bdbiosciences.com/en-ca/products/reagents/dehydrated-culture-media/animal-based-culture-media/brain-heart-infusion-bhi-bottle-500g.237500; Preserved exact public retrieval result | context_only | Exact manufacturer-specific quantitative composition of BD 237500 remains unavailable: raw product/IFU attempts returned 403, the legacy IFU host failed DNS and the manual URL returned 404. The separately preserved parsed page supports limited product identity only. This required formulation uncertainty makes the review partial; it does not negate the available JCM recipe. |
| mediadiveJ723-attempt | https://mediadive.dsmz.de/rest/medium/J723; Preserved exact public retrieval result | context_only | Both optional current MediaDive J723 requests returned 503; original failures and retry remain preserved. Exact JCM 723 and TOGO M746 content independently support the main recipe and its reducing-stock instructions. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact manufacturer-specific quantitative composition of BD 237500 remains unavailable: raw product/IFU attempts returned 403, the legacy IFU host failed DNS and the manual URL returned 404. The separately preserved parsed page supports limited product identity only. This required formulation uncertainty makes the review partial; it does not negate the available JCM recipe.
- Both optional current MediaDive J723 requests returned 503; original failures and retry remain preserved. Exact JCM 723 and TOGO M746 content independently support the main recipe and its reducing-stock instructions.
- The current MicrobeNotes article is an agar source and contains no 200 g/250 g tissue equivalences. No product lot/version equivalence, tissue-to-powder conversion, broth final pH, gas pressure/fraction, percentage basis, measured final volume or organism growth is inferred. The excluded specialized namesake is comparison context only.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195019Z-culturemech-010151-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_brain_heart_infusion_broth (CultureMech:010151)'
started_at: '2026-10-21T19:39:58Z'
finished_at: '2026-10-21T19:50:19Z'
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
summary: JCM 723 and TOGO M746 specify 37 g of commercial brain heart infusion broth,
  1 L water and two separate 5 ml/L reducing-stock additions. The maintained input
  and generated target replace the premix with an unauthenticated constituent breakdown,
  retain wrong liquid units and omit preparation. Required manufacturer-specific formulation
  evidence remains unavailable.
source:
  git_revision: 033ef56966c19f8948d84a579b3f280e3e94e9e3
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
  - path: data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
    sha256: e9dade0860e13573cd5ff7f08ce20cc3effc1ef3b470c7b19729f6645eeb091d
    role: target
  - path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
    sha256: 444de41ba8755c75ac20b1368ceed5ea1a476f6fa976035da5ce1d0dee4701b7
    role: context
  - path: data/normalized_yaml/specialized/anaerobic_brain_heart_infusion_broth.yaml
    sha256: fbcd441259f5a074e198561a646f23d7adb5475642878166c3f79eff265ce3e9
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
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 356; batch 036 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-five task batches
    contain 350 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 353 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010151
targets:
- target_id: CultureMech:010151
  path: data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  label: anaerobic_brain_heart_infusion_broth
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/356/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/356/strict.tsv"
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010151
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
  - CultureMech:010151
- check_id: bd237500bio-source-access
  name: 'Exact source content access: bd237500bio'
  required: true
  status: unavailable
  summary: 'Exact manufacturer-specific quantitative composition of BD 237500 remains
    unavailable: raw product/IFU attempts returned 403, the legacy IFU host failed
    DNS and the manual URL returned 404. The separately preserved parsed page supports
    limited product identity only. This required formulation uncertainty makes the
    review partial; it does not negate the available JCM recipe.'
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - bd237500bio-attempt
- check_id: mediadiveJ723-source-access
  name: 'Exact source content access: mediadiveJ723'
  required: false
  status: unavailable
  summary: Both optional current MediaDive J723 requests returned 503; original failures
    and retry remain preserved. Exact JCM 723 and TOGO M746 content independently
    support the main recipe and its reducing-stock instructions.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - mediadiveJ723-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:09.005217Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/356/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:10.414089Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/356/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:12.340814Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:13.181678Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:50:18Z'
  support: supports
  summary: './data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml:1:id:
    CultureMech:010151

    ./data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml:1:id:
    CultureMech:010151

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/source-preflight-bound/356/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:50:18Z'
  support: supports
  summary: 22 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 1523649dbbe6c11a63f59f954f06a700d3c7356086a9ada18119f09e34f47d68
- evidence_id: jcm723
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723
  locator: Complete exact recipe, both reducer rows and displayed default sterilization
  accessed_at: '2026-10-21T19:24:05.493716Z'
  support: supports
  summary: The exact primary specifies a commercial premix rather than its constituent
    formula; both reducer doses are explicitly per liter.
  quote: 'Brain heart infusion broth (BD-Difco) 37.0 g Distilled water 1.0 L Prepare
    the medium anaerobically under a N 2 atmosphere.  Prior to inoculation, add per
    liter the following solutions (autoclaved and stored under a N 2 atmosphere) aseptically
    and anaerobically: 5% L-Cysteine·HCl·H 2 O 5.0 ml 5% Na 2 S·9H 2 O 5.0 ml'
  snapshot_sha256: 73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7
- evidence_id: togo746
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746
  locator: $.meta.original_media_id and complete components/comments
  accessed_at: '2026-10-21T19:24:04.044784Z'
  support: supports
  summary: Exact M746 to JCM 723 identity and original commercial-product representation.
  quote: '"original_media_id": "JCM_M723"'
  snapshot_sha256: 98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483
- evidence_id: agar-article
  kind: database
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Composition of Brain Heart Infusion (BHI) Agar; table and pH statement
  accessed_at: '2026-10-21T08:42:28.042848Z'
  support: refutes
  summary: This is a secondary agar formulation. It does not authenticate the BD 237500
    broth formula or the locally asserted tissue-equivalent amounts.
  quote: 'Ingredients Gms/liter HM infusion powder 12.500 BHI powder 5.000 Proteose
    peptone 10.000 Dextrose (Glucose) 2.000 Sodium chloride 5.000 Disodium phosphate
    2.500 Agar 15.000 Final pH (at 25°C): 7.4±0.2'
  snapshot_sha256: b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01
- evidence_id: bound-scope-correction
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/source-preflight-bound/356/batch036-tail-356-source-scope-addendum.json
  locator: $.source_context[2].observation
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: The current article has no 200 g or 250 g tissue-equivalence statements.
    Those amounts are local assertions only, unsupported by the inspected article;
    the original cache interpretation is superseded at this exact locator.
  snapshot_sha256: e8a6fb9bff7678a853e1b71da0655fb1bdb7e1d0f5322dedf1144c0d7c52e333
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/356/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 583eca5233fb4999aba9220df66ba08efab1125825940f91520ae0058f4f0845
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: uberon0000955
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000955
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:43:25.122940Z'
  support: supports
  summary: UBERON:0000955 resolves to brain. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: ce200fe58b82652d0f04310c92d23633919fa6ad6aee2a17c6b25c2e490a8877
- evidence_id: uberon0000948
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:43:24.915343Z'
  support: supports
  summary: UBERON:0000948 resolves to heart. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: c658bbcacd89befa47e3bd4859f176db247b3ce67483b6590c91d0865d41aed4
- evidence_id: micro0000180
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:43:24.290496Z'
  support: supports
  summary: MICRO:0000180 resolves to proteose peptone. Identifier validity does not
    authenticate commercial constituent quantities or make an anatomy class equivalent
    to an infusion product.
  snapshot_sha256: b3a39a531c5ab5508a297228d13ba81c99899b041d5292a9d668eded939bfe73
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier validity
    does not authenticate commercial constituent quantities or make an anatomy class
    equivalent to an infusion product.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, definition and structural annotations
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier validity does not authenticate
    commercial constituent quantities or make an anatomy class equivalent to an infusion
    product.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/356/grounding-inventory.json
  locator: Every primary and secondary slot in the target and exact bacterial owner
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: Eight primary links and one secondary link per ten ingredient instances;
    all labels match their exact nonobsolete ontology responses. No excluded specialized-owner
    grounding is inherited.
  snapshot_sha256: 54c5da3eabd87a04ae2269e1f4cdb0a9f6134bf4900a807db9207c5672ff29de
- evidence_id: mim-water
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact current CHEBI:15377 preferred-term MAPPED rows; all other secondary
    slots absent in both reviewed layers
  accessed_at: '2026-10-21T19:50:18Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: manufacturer-parsed-identity
  kind: record_content
  reference: /private/tmp/culturemech-review-source-preflight-batch036-tail/356/bd-product-web-tool-scoped-response.json
  locator: $.tool_response, lines 712 and 765–771; separately captured parsed public
    response
  accessed_at: '2026-10-21T19:25:38Z'
  support: context_only
  summary: The preserved parsed manufacturer response identifies BD Bacto BHI, bottle
    500 g, and Contains Agar | No. It supplies limited product identity, not numerical
    constituent formulation, original raw HTTP authentication or the March 2026 product
    version. Package size, shelf life and package storage are not medium quantities
    or growth conditions.
  quote: BD Bacto™ Brain Heart Infusion (BHI), Bottle, 500g
  snapshot_sha256: 6130321f196a2810aa25b5f8818befc0ba8dc944f19dc12c166ae5be994c2cbd
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml; data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: commercial-writer-search
  kind: record_content
  reference: /private/tmp/culturemech-review-source-preflight-batch036-tail/356/commercial-writer-search.json
  locator: Ignored-inclusive owned-checkout Python/shell search for catalog 237500,
    exact composition statement and commercial-product marker
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: The bounded search did not identify the original March 28 BHI decomposition
    writer. Related current repairs do not authenticate this product or establish
    historical causation.
  snapshot_sha256: e28aa5e63b47e6d72269996b8c0764ec7dff9a3a6c5d06538729ddfe6c3f2e6a
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: 'Current static implementation only: import supports explicit solution
    sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup
    require source-stage review. These paths do not prove the historical execution
    that produced the commercial breakdown or authorize a guessed percentage basis.'
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: 'Current static implementation only: import supports explicit solution
    sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup
    require source-stage review. These paths do not prove the historical execution
    that produced the commercial breakdown or authorize a guessed percentage basis.'
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: 'Current static implementation only: import supports explicit solution
    sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup
    require source-stage review. These paths do not prove the historical execution
    that produced the commercial breakdown or authorize a guessed percentage basis.'
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:50:18Z'
  support: context_only
  summary: 'Current static implementation only: import supports explicit solution
    sections and preparation, bare percent defaults to w/v, and migration/merge/cleanup
    require source-stage review. These paths do not prove the historical execution
    that produced the commercial breakdown or authorize a guessed percentage basis.'
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: bd237500bio-attempt
  kind: database
  reference: https://www.bdbiosciences.com/en-ca/products/reagents/dehydrated-culture-media/animal-based-culture-media/brain-heart-infusion-bhi-bottle-500g.237500
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:04.145147Z'
  support: context_only
  summary: 'Exact manufacturer-specific quantitative composition of BD 237500 remains
    unavailable: raw product/IFU attempts returned 403, the legacy IFU host failed
    DNS and the manual URL returned 404. The separately preserved parsed page supports
    limited product identity only. This required formulation uncertainty makes the
    review partial; it does not negate the available JCM recipe.'
  snapshot_sha256: 820f0991d997705f9921056612c0053aeeee5721a5a6fe2eed1750cad2c18989
- evidence_id: mediadiveJ723-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J723
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:24:01.474186Z'
  support: context_only
  summary: Both optional current MediaDive J723 requests returned 503; original failures
    and retry remain preserved. Exact JCM 723 and TOGO M746 content independently
    support the main recipe and its reducing-stock instructions.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 22 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM 723 basal batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 1; Distilled water / 1.0\
    \ / L\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"togoM746original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1.0 L of water. Both\
    \ local layers instead store 1 G_PER_L; preserve the volume without claiming a\
    \ measured final medium volume.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n \
    \   \"ingredient\": \"Commercial brain heart infusion broth premix\",\n    \"\
    decision\": \"add\",\n    \"stage\": \"JCM 723 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"togoM746original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Brain heart infusion broth (BD-Difco)\\\",\\n\
    \          \\\"volume\\\": 37,\\n          \\\"unit\\\": \\\"g\\\"\",\n      \
    \  \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore an explicitly identified\
    \ 37 g BD-Difco premix at source batch scope, replacing the unsupported decomposition\
    \ rather than double-counting premix and presumed constituents. The primary does\
    \ not give a catalog number or constituent amounts.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"ingredient\": \"Calf brain infusion\",\n    \"decision\": \"\
    unsupported\",\n    \"stage\": \"Local commercial-product decomposition\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"infusion\
    \ from 200 g/L; Tissue infusion - source material is calf brain tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table; distinct powder names\
    \ and amounts\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The local VARIABLE amount and 200\
    \ g/L tissue-equivalent note are not authenticated for this product. The inspected\
    \ article does not state that tissue equivalence. Do not interpret it as tissue\
    \ weighed into the broth or replace it with an assumed powder conversion.\"\n\
    \  },\n  {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"Beef heart infusion\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Local commercial-product\
    \ decomposition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"infusion\
    \ from 250 g/L; Tissue infusion - source material is beef/ox heart tissue; Constituent\
    \ of Brain Heart Infusion commercial product\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table; distinct powder names\
    \ and amounts\",\n        \"exact_source_quote\": \"HM infusion powder 12.500\
    \ BHI powder 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The local VARIABLE amount and 250\
    \ g/L tissue-equivalent note are not authenticated for this product. The inspected\
    \ article does not state that tissue equivalence. Do not interpret it as tissue\
    \ weighed into the broth or replace it with an assumed powder conversion.\"\n\
    \  },\n  {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"Proteose peptone\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Local commercial-product\
    \ decomposition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 0; Brain heart infusion\
    \ broth (BD-Difco) / 37.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Brain heart infusion broth (BD-Difco)                     </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table under Ingredients Gms/liter\"\
    ,\n        \"exact_source_quote\": \"Proteose peptone 10.000\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The number matches the cited secondary\
    \ agar formulation, but neither that article nor JCM 723 establishes this constituent\
    \ concentration in the asserted BD 237500 broth. Preserve the uncertainty rather\
    \ than marking the local claim verified or silently substituting another formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"ingredient\": \"Dextrose\",\n\
    \    \"decision\": \"unsupported\",\n    \"stage\": \"Local commercial-product\
    \ decomposition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 0; Brain heart infusion\
    \ broth (BD-Difco) / 37.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Brain heart infusion broth (BD-Difco)                     </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table under Ingredients Gms/liter\"\
    ,\n        \"exact_source_quote\": \"Dextrose (Glucose) 2.000\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The number matches the cited secondary\
    \ agar formulation, but neither that article nor JCM 723 establishes this constituent\
    \ concentration in the asserted BD 237500 broth. Preserve the uncertainty rather\
    \ than marking the local claim verified or silently substituting another formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q7\",\n    \"ingredient\": \"Sodium chloride\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Local commercial-product\
    \ decomposition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 0; Brain heart infusion\
    \ broth (BD-Difco) / 37.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Brain heart infusion broth (BD-Difco)                     </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table under Ingredients Gms/liter\"\
    ,\n        \"exact_source_quote\": \"Sodium chloride 5.000\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The number matches the cited secondary\
    \ agar formulation, but neither that article nor JCM 723 establishes this constituent\
    \ concentration in the asserted BD 237500 broth. Preserve the uncertainty rather\
    \ than marking the local claim verified or silently substituting another formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"ingredient\": \"Disodium phosphate\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Local commercial-product\
    \ decomposition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 0; Brain heart infusion\
    \ broth (BD-Difco) / 37.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Brain heart infusion broth (BD-Difco)                     </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"\
    source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n \
    \       \"source_locator\": \"BHI agar composition table under Ingredients Gms/liter\"\
    ,\n        \"exact_source_quote\": \"Disodium phosphate 2.500\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The number matches the cited secondary\
    \ agar formulation, but neither that article nor JCM 723 establishes this constituent\
    \ concentration in the asserted BD 237500 broth. Preserve the uncertainty rather\
    \ than marking the local claim verified or silently substituting another formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"ingredient\": \"N2 atmosphere\
    \ quantity\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"Main preparation\
    \ and reducing-stock storage\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"Preparation sentence before reducer additions\"\
    ,\n        \"exact_source_quote\": \"Prepare the medium anaerobically under a\
    \ N 2 atmosphere.\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      },\n      {\n        \"source_key\": \"togoM746original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      }\n    ],\n    \"interpretation\": \"The source names N2 but gives no\
    \ fraction, volume, flow or pressure. VARIABLE is an honest unquantified amount;\
    \ do not turn the gas name into 100%. Attach the preparation stage separately.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"ingredient\": \"Sodium sulfide\
    \ nonahydrate stock dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Aseptic anaerobic addition before inoculation\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0\
    \ / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O\
    \                               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM746original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"Receiving-medium denominator and timing sentence\",\n        \"exact_source_quote\"\
    : \"Prior to inoculation, add per liter the following solutions\",\n        \"\
    snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"The source dose is 5.0 ml per liter\
    \ of receiving medium, not 5 G_PER_L. Represent the stock addition separately\
    \ from its strength and named hydrate; do not infer a solute mass or final concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"ingredient\": \"Sodium sulfide\
    \ nonahydrate stock strength\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Separate reducing stock preparation\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].preferred_term\",\n        \"stored\"\
    : \"5% Na2S・9H2O\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].preferred_term\",\n        \"stored\"\
    : \"5% Na2S・9H2O\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm723\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0\
    \ / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O\
    \                               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM746original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"Receiving-medium denominator and timing sentence\",\n        \"exact_source_quote\"\
    : \"Prior to inoculation, add per liter the following solutions\",\n        \"\
    snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"The name retains 5%, but a separate\
    \ stock representation is absent. Preserve 5% without assigning w/v, v/v or density:\
    \ neither primary nor provider qualifies the percentage basis. Do not infer a\
    \ stock batch volume.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"ingredient\"\
    : \"L-cysteine hydrochloride monohydrate stock dose\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Aseptic anaerobic addition before inoculation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2\
    \ O / 5.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% L-Cysteine&#183;HCl&#183;H<sub>2</sub>O\
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"togoM746original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% L--Cysteine・HCl・H2O\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"Receiving-medium denominator and timing sentence\",\n        \"exact_source_quote\"\
    : \"Prior to inoculation, add per liter the following solutions\",\n        \"\
    snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"The source dose is 5.0 ml per liter\
    \ of receiving medium, not 5 G_PER_L. Represent the stock addition separately\
    \ from its strength and named hydrate; do not infer a solute mass or final concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"ingredient\": \"L-cysteine hydrochloride\
    \ monohydrate stock strength\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Separate reducing stock preparation\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].preferred_term\",\n        \"stored\"\
    : \"5% L--Cysteine・HCl・H2O\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].preferred_term\",\n        \"stored\"\
    : \"5% L--Cysteine・HCl・H2O\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm723\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2\
    \ O / 5.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% L-Cysteine&#183;HCl&#183;H<sub>2</sub>O\
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"togoM746original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M746\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% L--Cysteine・HCl・H2O\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"98cfb6edc91469dc59ce4b6fa4ac4dcd442cc18cb59cf16892f58f9a60d1d483\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"Receiving-medium denominator and timing sentence\",\n        \"exact_source_quote\"\
    : \"Prior to inoculation, add per liter the following solutions\",\n        \"\
    snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"The name retains 5%, but a separate\
    \ stock representation is absent. Preserve 5% without assigning w/v, v/v or density:\
    \ neither primary nor provider qualifies the percentage basis. Do not infer a\
    \ stock batch volume.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"ingredient\"\
    : \"Stock preparation volumes and final solute concentrations\",\n    \"decision\"\
    : \"not_quantified\",\n    \"stage\": \"Two separate reducing stocks\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm723\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 2; 5% L-Cysteine·HCl·H 2\
    \ O / 5.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% L-Cysteine&#183;HCl&#183;H<sub>2</sub>O\
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 3; 5% Na 2 S·9H 2 O / 5.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O               \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The source supplies stock strengths and\
    \ doses only. Stock solvent amounts, batch volumes and mass-based final concentrations\
    \ are unspecified; the hydrate names do not supply the missing percentage basis.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"ingredient\": \"Final pH 7.4\
    \ ± 0.2 claim\",\n    \"decision\": \"unsupported\",\n    \"stage\": \"Local phosphate\
    \ note versus secondary agar pH\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"pH\
    \ buffer (final pH 7.4 ± 0.2); Constituent of Brain Heart Infusion commercial\
    \ product\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"microbenotesBHI\"\
    ,\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"BHI agar composition table; temperature-qualified\
    \ pH\",\n        \"exact_source_quote\": \"Final pH (at 25°C): 7.4±0.2\",\n  \
    \      \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      }\n    ],\n    \"interpretation\": \"The current local note transfers\
    \ the agar article pH to the broth without product-specific evidence and omits\
    \ its 25°C measurement qualifier. JCM 723 states no pH. Do not promote this note\
    \ to an authenticated final pH or infer a culture temperature.\"\n  },\n  {\n\
    \    \"decision_id\": \"q16\",\n    \"ingredient\": \"Autoclave temperature and\
    \ duration\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM 723 displayed\
    \ default and expressly autoclaved stages\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"Exact-page default sterilization statement\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"Record the exact-page 121°C for 15\
    \ min default with the appropriate autoclaved stages. Pressure is not specified\
    \ by JCM 723; do not import the secondary agar article pressure or cooling conditions.\"\
    \n  },\n  {\n    \"decision_id\": \"q17\",\n    \"ingredient\": \"Reducer timing\
    \ and storage atmosphere\",\n    \"decision\": \"add\",\n    \"stage\": \"Before\
    \ inoculation; separate autoclaved reducing stocks\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"Complete pre-inoculation reducer instruction\"\
    ,\n        \"exact_source_quote\": \"Prior to inoculation, add per liter the following\
    \ solutions (autoclaved and stored under a N 2 atmosphere) aseptically and anaerobically:\"\
    ,\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    ,\n        \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the receiving-liter denominator,\
    \ separate autoclaving, N2 storage and aseptic anaerobic addition. Storage duration\
    \ and temperature are unquantified; package-storage metadata must not become stock-storage\
    \ or culture conditions.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"ingredient\"\
    : \"Measured final medium volume\",\n    \"decision\": \"not_quantified\",\n \
    \   \"stage\": \"Basal medium followed by per-liter reducing-stock additions\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm723\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\"\
    ,\n        \"source_locator\": \"JCM 723 raw HTML row 1; Distilled water / 1.0\
    \ / L\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"Receiving-liter instruction\",\n        \"exact_source_quote\": \"Prior to\
    \ inoculation, add per liter the following solutions\",\n        \"snapshot_sha256\"\
    : \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\",\n    \
    \    \"parsed_text_sha256\": \"ff838ccd308ca9331a0ba3f75700c595ac0dbb8f4e49ceedc1bc2bd56a44eff8\"\
    \n      }\n    ],\n    \"interpretation\": \"One liter of water plus commercial\
    \ solids is a preparation amount, not a measured final volume. Both 5 ml/L additions\
    \ retain their explicit receiving basis; do not assert that a measured final 1010\
    \ ml or a final premix g/L was provided.\"\n  },\n  {\n    \"decision_id\": \"\
    q19\",\n    \"ingredient\": \"HM infusion powder in secondary article\",\n   \
    \ \"decision\": \"unsupported\",\n    \"stage\": \"Secondary BHI agar formula\
    \ only; excluded from JCM 723 transfer\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\"\
    : \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Composition table headed Ingredients Gms/liter\",\n        \"exact_source_quote\"\
    : \"HM infusion powder 12.500\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an explicit amount in a different\
    \ agar formulation. It neither supplies a manufacturer-verified broth constituent\
    \ nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact\
    \ product evidence before any decomposition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"ingredient\": \"BHI powder in secondary article\",\n    \"decision\"\
    : \"unsupported\",\n    \"stage\": \"Secondary BHI agar formula only; excluded\
    \ from JCM 723 transfer\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\",\n    \
    \    \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n  \
    \          \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\"\
    : \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Composition table headed Ingredients Gms/liter\",\n        \"exact_source_quote\"\
    : \"BHI powder 5.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an explicit amount in a different\
    \ agar formulation. It neither supplies a manufacturer-verified broth constituent\
    \ nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact\
    \ product evidence before any decomposition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"ingredient\": \"Agar in secondary article\",\n    \"decision\"\
    : \"unsupported\",\n    \"stage\": \"Secondary BHI agar formula only; excluded\
    \ from JCM 723 transfer\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\",\n    \
    \    \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n  \
    \          \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Distilled water\",\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Solvating media; Properties: Defined\
    \ component, Inorganic compound, Simple component\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15377\",\n              \"label\": \"water\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Calf brains\"\
    ,\n            \"term\": {\n              \"id\": \"UBERON:0000955\",\n      \
    \        \"label\": \"brain\"\n            },\n            \"concentration\":\
    \ {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
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
    \      }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"N2\",\n            \"notes\": \"Properties: Gas\",\n            \"concentration\"\
    : {\n              \"value\": \"variable\",\n              \"unit\": \"VARIABLE\"\
    \n            },\n            \"term\": {\n              \"id\": \"CHEBI:17997\"\
    ,\n              \"label\": \"dinitrogen\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"5% Na2S・9H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Role: Reducing agent; Properties: Defined\
    \ component, Inorganic compound, Solution\"\n          },\n          {\n     \
    \       \"preferred_term\": \"5% L--Cysteine・HCl・H2O\",\n            \"concentration\"\
    : {\n              \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"Properties: Defined component, Organic\
    \ compound, Solution\"\n          }\n        ]\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"microbenotesBHI\",\n        \"source_url\"\
    : \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\",\n        \"source_locator\"\
    : \"Composition table headed Ingredients Gms/liter\",\n        \"exact_source_quote\"\
    : \"Agar 15.000\",\n        \"snapshot_sha256\": \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\"\
    ,\n        \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      },\n      {\n        \"source_key\": \"jcm723\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=723\",\n        \"source_locator\"\
    : \"JCM 723 raw HTML row 0; Brain heart infusion broth (BD-Difco) / 37.0 / g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Brain heart infusion broth\
    \ (BD-Difco)                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"73c72b04683318715c98c35adc61514989890fe94f6201acb5260542113c67c7\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an explicit amount in a different\
    \ agar formulation. It neither supplies a manufacturer-verified broth constituent\
    \ nor authorizes adding it to JCM 723. Preserve the discrepancy and require exact\
    \ product evidence before any decomposition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q22\",\n    \"ingredient\": \"Secondary article total and preparation conditions\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Secondary agar preparation\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Brain_Heart_Infusion_Broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"microbenotesBHI\",\n        \"source_url\": \"https://microbenotes.com/brain-heart-infusion-bhi-agar/\"\
    ,\n        \"source_locator\": \"BHI agar preparation paragraph\",\n        \"\
    exact_source_quote\": \"Suspend 52.0 grams in 1000 ml distilled water. Heat to\
    \ boiling to dissolve the medium completely. Sterilize by autoclaving at 15 lbs\
    \ pressure (121°C) for 15 minutes. Cool to 45-50°C.\",\n        \"snapshot_sha256\"\
    : \"b3cc10040924962852a01d9d3341fa2d14616b8c845f83d5d187d03c08db0a01\",\n    \
    \    \"parsed_text_sha256\": \"051d1ff8fb532e65c6625950fa89778cf51ade5fd9ca069882e67dcf9e960c59\"\
    \n      }\n    ],\n    \"interpretation\": \"The article total 52 g includes its\
    \ 15 g agar; subtracting it is not authentication of BD 237500 constituent composition.\
    \ Its 1000 ml, 15 lbs pressure and 45–50°C cooling belong to agar preparation\
    \ and do not transfer to this broth. JCM default temperature/time has its own\
    \ independent support.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Mixed-ontology labels and supplied material scope
  outcome: concern
  summary: All eight distinct asserted primary IDs and the water secondary key have
    matching nonobsolete metadata. Target linkage is 8/10 primary (80%) and 1/10 secondary
    (10%), not a correctness score. UBERON brain and heart denote anatomy rather than
    a manufactured infusion; they do not establish species, tissue-equivalent mass
    or product formulation. MICRO proteose peptone and CHEBI dextrose/D-glucose, sodium
    chloride and disodium phosphate are valid name correspondences within the qualified
    article only; phosphate hydration and the exact broth composition remain unverified.
    The two stock names retain source hydrate identity but have no primary or secondary
    links in these layers.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - grounding-inventory
  - mim-water
  - agar-article
  - jcm723
  - chebi15377
  - uberon0000955
  - uberon0000948
  - micro0000180
  - chebi17634
  - chebi26710
  - chebi34683
  - chebi17997
- assessment_id: identity
  area: identity
  topic: Exact culture-medium and commercial-source identity
  outcome: concern
  summary: The target and sole bacterial owner are CultureMech:010151, TOGO M746 and
    JCM 723. The specialized namesake CultureMech:015416 is excluded by exact stable
    ID and import provenance. JCM calls for a BD-Difco commercial broth; it does not
    identify catalog 237500 or a constituent formula. The parsed manufacturer page
    supports the catalog product as an agar-free BHI bottle, while the supplied product_url
    is a secondary agar article. Full catalog formulation/version correspondence remains
    unresolved.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - togo746
  - jcm723
  - agar-article
  - manufacturer-parsed-identity
- assessment_id: quantitative-scope
  area: representation
  topic: Commercial product and reducing stocks
  outcome: concern
  summary: The six inferred commercial constituents replace the source 37 g premix.
    Current article table values are not exact broth-product evidence, and neither
    inspected article nor primary contains the local 200/250 g/L tissue-equivalence
    claims. Water and reducer units are wrong. Reducing-stock names retain strengths
    and hydrate names, but the record lacks distinct stock composition, receiving
    dose and unqualified percentage-basis handling.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - jcm723
  - agar-article
  - bound-scope-correction
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Anaerobic preparation, sterilization and pH
  outcome: concern
  summary: Both layers omit the exact JCM anaerobic preparation, displayed 121°C/15
    min default, separate stock autoclaving/N2 storage and aseptic addition before
    inoculation. JCM gives no final pH; the phosphate note borrows the secondary agar
    pH. No source-specific gas fraction, pressure, measured final volume or incubation
    condition is inferred.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - jcm723
  - agar-article
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Mixture state and biological assertions
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are consistent with the exact commercial-broth
    source. Bacterial category and generic cultivation application are not organism-specific
    growth evidence. The agar article organisms, incubation temperatures, supplements
    and clinical uses do not transfer to this anaerobic broth.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - jcm723
  - agar-article
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 17 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface
  outcome: supported
  summary: The sole maintained bacterial owner is the correction surface, followed
    by authorized merge regeneration. Its full import history matches this target;
    the specialized same-basename record is not a contributor or substitute. Preserve
    old history, append any later source-backed curation, and do not edit the generated
    target directly.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - commercial-writer-search
  - writer-0
  - writer-2
- assessment_id: evidence
  area: evidence
  topic: Claim attachment and historical product provenance
  outcome: concern
  summary: Neither reviewed layer has attached amount/preparation evidence. JCM and
    TOGO support the premix and reducer stages, while the local product-specification
    note and secondary URL cannot authenticate its constituent claims. Required exact
    manufacturer quantitative formulation remains unavailable after preserved attempts;
    the limited parsed identity response is not promoted to a raw formulation capture.
  target_ids:
  - CultureMech:010151
  evidence_ids:
  - record
  - owner-0
  - jcm723
  - togo746
  - agar-article
  - manufacturer-parsed-identity
  - bound-scope-correction
findings:
- finding_id: f1
  issue_key: culturemech.010151.commercial-premix-decomposition
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Unauthenticated constituents replace the commercial premix
  description: Both layers omit the source 37 g BD-Difco premix and replace it with
    six presumed constituents. The secondary agar article does not authenticate BD
    237500 broth composition, and it contains neither local tissue-equivalence amount.
    Anatomy terms and a catalog number do not supply that missing formulation evidence.
  target_ids:
  - CultureMech:010151
  field_paths:
  - ingredients[1]
  - ingredients[2]
  - ingredients[3]
  - ingredients[4]
  - ingredients[5]
  - ingredients[6]
  - notes
  evidence_ids:
  - jcm723
  - togo746
  - agar-article
  - manufacturer-parsed-identity
  - bound-scope-correction
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  issue_key: culturemech.010151.liquid-units-stock-scope
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and reducing-stock doses have mass units
  description: The source 1 L water is stored as 1 G_PER_L; both 5 ml/L reducing-stock
    doses are stored as 5 G_PER_L. Their 5% strengths lack an explicit percentage
    basis and must remain separate from dose and solute identity.
  target_ids:
  - CultureMech:010151
  field_paths:
  - ingredients[0].concentration
  - ingredients[8]
  - ingredients[9]
  evidence_ids:
  - jcm723
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  issue_key: culturemech.010151.preparation-and-ph-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation is absent and the pH note comes from an agar source
  description: Anaerobic handling, default sterilization and pre-inoculation reducer
    stages are missing. The phosphate note asserts final pH 7.4 ± 0.2 from a different
    agar formulation, without exact broth support.
  target_ids:
  - CultureMech:010151
  field_paths:
  - preparation_steps
  - sterilization
  - ingredients[6].notes
  - ph_value
  evidence_ids:
  - jcm723
  - agar-article
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  issue_key: culturemech.010151.claim-evidence-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical product claims lack claim-level evidence
  description: Source URLs, a March 28 access note and import history do not attach
    exact amounts, preparation or product-version support. Current source reads cannot
    reconstruct the absent historical specification.
  target_ids:
  - CultureMech:010151
  field_paths:
  - ingredients
  - notes
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - jcm723
  - agar-article
  - commercial-writer-search
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  description: Restore the source-identified premix and its 37 g batch amount, or
    obtain exact manufacturer formulation/version evidence before retaining any decomposition.
    Keep organ-source descriptions distinct from manufactured infusion identity and
    do not double-count constituents with the premix.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010151
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  description: Correct water and stock-dose units, structure the two reducing stocks
    with exact source hydrate names, and retain the explicit per-liter receiving basis
    without invented percentage basis, stock recipe or final concentration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010151
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  description: Add exact JCM preparation and stock-handling evidence; qualify or remove
    the unsupported broth pH claim until product-specific evidence is obtained. Do
    not transfer agar cooling, pressure, incubation or growth conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010151
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
  description: Attach narrow source snippets with exact capture hashes, dates and
    stage locators after curation. Preserve inaccessible manufacturer attempts and
    append a transparent provenance clarification without rewriting historical events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010151
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_brain_heart_infusion_broth.yaml
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
- 'Exact manufacturer-specific quantitative composition of BD 237500 remains unavailable:
  raw product/IFU attempts returned 403, the legacy IFU host failed DNS and the manual
  URL returned 404. The separately preserved parsed page supports limited product
  identity only. This required formulation uncertainty makes the review partial; it
  does not negate the available JCM recipe.'
- Both optional current MediaDive J723 requests returned 503; original failures and
  retry remain preserved. Exact JCM 723 and TOGO M746 content independently support
  the main recipe and its reducing-stock instructions.
- The current MicrobeNotes article is an agar source and contains no 200 g/250 g tissue
  equivalences. No product lot/version equivalence, tissue-to-powder conversion, broth
  final pH, gas pressure/fraction, percentage basis, measured final volume or organism
  growth is inferred. The excluded specialized namesake is comparison context only.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-036
- generated-medium
```
