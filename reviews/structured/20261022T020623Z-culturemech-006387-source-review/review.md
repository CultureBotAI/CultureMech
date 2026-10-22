# Source and formulation review: bphd_medium (CultureMech:006387)

- Review: 20261022T020623Z-culturemech-006387-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T02:02:37Z
- Finished UTC: 2026-10-22T02:06:23Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BPHD is represented as a flattened mixture of basal and stock ingredients, with a phenol-named contributor still containing cresol. The exact primary supports separate vitamin/mineral stocks and substrate alternatives, while current provider displays differ from stored rates. Restore source stages and variant identity before regeneration; do not infer final volumes or repair the anomalous phosphate formula by guesswork.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 442; batch 045 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-four task batches contain 440 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 443 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006387 | data/merge_yaml/merged/BPHD_Medium.yaml | generated | bphd_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006387 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006387 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/442/strict.tsv |
| validate-terms | passed | True | CultureMech:006387 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006387 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006387 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive738api | unavailable | False | CultureMech:006387 | The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock primaries and exact KOMODO base/variant pages are usable; no unavailable API response is treated as amount authentication. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006387.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:006387.

30 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly. 29/29 asserted current secondary keys have exact pinned index rows. Target primary linkage is 30/31 (96.77%) and current secondary linkage is 29/31 (93.55%) on a 0–100 linkage scale, not a correctness score. Current missing keys do not prove historical invalidity; compatible generic source wording does not establish a stereochemical conflict.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006387.

40 timestamp instances inspected; 6 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Base recipe and distinct phenol branch

identity: concern. Targets: CultureMech:006387.

The three native contributors are exact maintained inputs, but source identity does not make their recipes interchangeable. The phenol replacement accession must retain phenol rather than the copied cresol entry. Source permits either substrate, not both and not a mixture of all cresol isomers. Catalog Is Aerobic=false and Is Complex=false do not override the recipe or establish an anoxic requirement.

### Basal masses, stock batches and doses

quantity: concern. Targets: CultureMech:006387.

All four local layers flatten ten vitamins and mineral-stock ingredients into main G_PER_L fields. Main FeSO4 0.04 g and stock FeSO4 0.10 g are combined as 0.14; target calcium 0.2 combines two 0.1 entries, while current owners collapsed these to 0.1 but still lost the stock boundary. The two 10 ml doses and three distinct listed-water inputs must be preserved; no measured main or stock final volume is established by the PDF tables.

### Supported hydrates, source spelling and nickel form

grounding: concern. Targets: CultureMech:006387.

The primary literally prints Na2H2PO4 x H2O for the second phosphate. The local Na2HPO4 x H2O label and anhydrous CHEBI:34683 do not resolve that source ambiguity. Do not silently replace it with a plausible mono- or dibasic phosphate. The named NiCl2 hexahydrate is mapped to anhydrous CHEBI:34887. Calcium D-pantothenate agrees with the D structure in CHEBI:31345; generic lipoic acid is compatible with DL source wording. Primary thiamine HCl and current KOMODO thiamine-HCl dihydrate remain distinct source formulations.

### Supported preparation versus imported additions

representation: concern. Targets: CultureMech:006387.

Main pH 6.5 and substrate addition after autoclaving are explicit. The source stock subsection has an initial pH 6.5 and final pH 7.0 using KOH; these do not alter main pH. The DSMZ owner additionally says to dissolve phosphates separately and add vitamins after autoclaving, neither stated in the current DSM738 primary. No heating temperature/duration or incubation condition is supplied.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006387.

45 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Basal NH4Cl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'NH4Cl'",
        "exact_source_quote": "NH4Cl                                                       1.00     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary supports this nominal batch mass, not the stored final-litre basis. Current provider displays are separately normalized/rounded and do not establish a measured denominator for the stored recipe. Preserve the exact source mass and unit; the second phosphate identity remains unresolved rather than silently corrected."
  },
  {
    "decision_id": "q2",
    "subject": "Basal Na2HPO4 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.42",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Na2HPO4 x 2'",
        "exact_source_quote": "Na2HPO4 x 2 H2O                                             0.42     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary supports this nominal batch mass, not the stored final-litre basis. Current provider displays are separately normalized/rounded and do not establish a measured denominator for the stored recipe. Preserve the exact source mass and unit; the second phosphate identity remains unresolved rather than silently corrected."
  },
  {
    "decision_id": "q3",
    "subject": "Basal Na2HPO4 x H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Na2H2PO4'",
        "exact_source_quote": "Na2H2PO4 x H2O                                              0.18     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary supports this nominal batch mass, not the stored final-litre basis. Current provider displays are separately normalized/rounded and do not establish a measured denominator for the stored recipe. Preserve the exact source mass and unit; the second phosphate identity remains unresolved rather than silently corrected."
  },
  {
    "decision_id": "q4",
    "subject": "Basal MgCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'MgCl2'",
        "exact_source_quote": "MgCl2 x 6 H2O                                               0.10     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary supports this nominal batch mass, not the stored final-litre basis. Current provider displays are separately normalized/rounded and do not establish a measured denominator for the stored recipe. Preserve the exact source mass and unit; the second phosphate identity remains unresolved rather than silently corrected."
  },
  {
    "decision_id": "q5",
    "subject": "Basal KCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'KCl'",
        "exact_source_quote": "KCl                                                         0.10     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary supports this nominal batch mass, not the stored final-litre basis. Current provider displays are separately normalized/rounded and do not establish a measured denominator for the stored recipe. Preserve the exact source mass and unit; the second phosphate identity remains unresolved rather than silently corrected."
  },
  {
    "decision_id": "q6",
    "subject": "Separate basal and mineral-stock CaCl2 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'CaCl2 x 2'",
        "exact_source_quote": "CaCl2 x 2 H2O                                               0.10     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      },
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing CaCl2 x 2",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "These are two separate source-stage amounts, not additive whole-medium rates. Calcium is 0.10 g in the basal batch and 0.10 g in the stock; iron is 0.04 g basal and 0.10 g stock. The target calcium 0.2 and every layer iron 0.14 combine stages incorrectly. Owners collapsed calcium to 0.1 but still omit its stock input. Reconstruct both stages and the stock dose without inventing final-litre values."
  },
  {
    "decision_id": "q7",
    "subject": "Separate basal and mineral-stock FeSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'FeSO4 x 7'",
        "exact_source_quote": "FeSO4 x 7 H2O                                               0.04     g",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      },
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing FeSO4 x 7",
        "exact_source_quote": "FeSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "These are two separate source-stage amounts, not additive whole-medium rates. Calcium is 0.10 g in the basal batch and 0.10 g in the stock; iron is 0.04 g basal and 0.10 g stock. The target calcium 0.2 and every layer iron 0.14 combine stages incorrectly. Owners collapsed calcium to 0.1 but still omit its stock input. Reconstruct both stages and the stock dose without inventing final-litre values."
  },
  {
    "decision_id": "q8",
    "subject": "Cresol selected base branch",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Cresol or phenol'",
        "exact_source_quote": "Cresol or phenol                                            1.00   mM*",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The primary explicitly states 1.00 mM for either selected substrate. This supports the base cresol branch value/unit, but no matching attached claim is present. Do not turn the provider 0.32 g/L display or three SEED isomers into a different substrate dose."
  },
  {
    "decision_id": "q9",
    "subject": "Phenol owner still stores cresol",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[7].preferred_term",
        "stored": "Cresol"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Cresol or phenol'",
        "exact_source_quote": "Cresol or phenol                                            1.00   mM*",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      },
      {
        "source_key": "komodoDetail738_replace_Cresol_with_Phenol",
        "source_url": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738_replace_Cresol_with_Phenol",
        "source_locator": "Metabolites list, exact Phenol row",
        "exact_source_quote": "Phenol\nphenol-solution\nphenol-solution#\nnull\nnull",
        "snapshot_sha256": "b635e7cb24c4f816fcc36fd99199ea7a68c642ce7e38a856cc351fa5d6cf9642",
        "parsed_text_sha256": "d769d7e1ab8280af6d696a35c4371f6de1400cf927bea2f743fe76705fb8dc56"
      }
    ],
    "rationale": "The named phenol-replacement source has phenol, not cresol. Restore the supported phenol branch after identity reconciliation. The primary offers 1 mM phenol; null provider cells supply no numeric amount and must not be treated as zero or copied cresol."
  },
  {
    "decision_id": "q10",
    "subject": "Vitamin-stock Biotin",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Biotin",
        "exact_source_quote": "Biotin 2.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q11",
    "subject": "Vitamin-stock Folic acid",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Folic acid",
        "exact_source_quote": "Folic acid 2.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q12",
    "subject": "Vitamin-stock Pyridoxine hydrochloride",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Pyridoxine hydrochloride",
        "exact_source_quote": "Pyridoxine hydrochloride 10.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q13",
    "subject": "Vitamin-stock Thiamine HCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Thiamine HCl",
        "exact_source_quote": "Thiamine HCl 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q14",
    "subject": "Vitamin-stock Riboflavin",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Riboflavin",
        "exact_source_quote": "Riboflavin 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q15",
    "subject": "Vitamin-stock Nicotinic acid",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Nicotinic acid",
        "exact_source_quote": "Nicotinic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q16",
    "subject": "Vitamin-stock Calcium D-(+)-pantothenate",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Calcium D-(+)-pantothenate",
        "exact_source_quote": "Calcium D-(+)-pantothenate 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q17",
    "subject": "Vitamin-stock Vitamin B12",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Vitamin B12",
        "exact_source_quote": "Vitamin B12 0.10 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q18",
    "subject": "Vitamin-stock p-Aminobenzoic acid",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing p-Aminobenzoic acid",
        "exact_source_quote": "p-Aminobenzoic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q19",
    "subject": "Vitamin-stock (DL)-alpha-Lipoic acid",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing (DL)-alpha-Lipoic acid",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 5.00 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "This is a mass in the separate Wolin vitamin stock batch, with the displayed mg converted to g only arithmetically. It is not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate 10 ml receiving-batch dose; listed stock water is not a measured final litre."
  },
  {
    "decision_id": "q20",
    "subject": "Mineral-stock Nitrilotriacetic acid",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing Nitrilotriacetic acid",
        "exact_source_quote": "Nitrilotriacetic acid 1.50 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q21",
    "subject": "Mineral-stock MgSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 3.00 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q22",
    "subject": "Mineral-stock MnSO4 x H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing MnSO4 x H2O",
        "exact_source_quote": "MnSO4 x H2O 0.50 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q23",
    "subject": "Mineral-stock NaCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing NaCl",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q24",
    "subject": "Mineral-stock CoSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing CoSO4 x 7 H2O",
        "exact_source_quote": "CoSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q25",
    "subject": "Mineral-stock ZnSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q26",
    "subject": "Mineral-stock CuSO4 x 5 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 0.01 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q27",
    "subject": "Mineral-stock AlK(SO4)2 x 12 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing AlK(SO4)2 x 12 H2O",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.02 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q28",
    "subject": "Mineral-stock H3BO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing H3BO3",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q29",
    "subject": "Mineral-stock Na2MoO4 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.01 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q30",
    "subject": "Mineral-stock NiCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing NiCl2 x 6 H2O",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q31",
    "subject": "Mineral-stock Na2SeO3 x 5 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing Na2SeO3 x 5 H2O",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.30 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q32",
    "subject": "Mineral-stock Na2WO4 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing Na2WO4 x 2 H2O",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary supports a separate mineral-stock batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g and 0.0004 g in that stock batch. No stock or receiving final-volume basis is inferred."
  },
  {
    "decision_id": "q33",
    "subject": "Vitamin stock 10 ml batch dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Vitamin solution'",
        "exact_source_quote": "Vitamin solution (see medium 141)                          10.00    ml",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "Add this exact source batch input at its named stage. The table does not print ml/L for the two stock doses; the listed 1000 ml main water does not establish measured final volume."
  },
  {
    "decision_id": "q34",
    "subject": "Mineral stock 10 ml batch dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Trace element solution'",
        "exact_source_quote": "Trace element solution (see medium 141)                    10.00    ml",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "Add this exact source batch input at its named stage. The table does not print ml/L for the two stock doses; the listed 1000 ml main water does not establish measured final volume."
  },
  {
    "decision_id": "q35",
    "subject": "Main water 1000 ml",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "Na2HPO4 x 2 H2O",
            "term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            },
            "concentration": {
              "value": "0.42",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            }
          },
          {
            "preferred_term": "Na2HPO4 x H2O",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "notes": " [Merged 2 duplicates: 0.1, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.14",
              "unit": "G_PER_L"
            },
            "notes": " [Merged 2 duplicates: 0.04, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Cresol",
            "concentration": {
              "value": "1",
              "unit": "MILLIMOLAR"
            }
          },
          {
            "preferred_term": "Biotin",
            "term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            }
          },
          {
            "preferred_term": "Folic acid",
            "term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            }
          },
          {
            "preferred_term": "Pyridoxine hydrochloride",
            "term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            }
          },
          {
            "preferred_term": "Thiamine HCl",
            "term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            }
          },
          {
            "preferred_term": "Riboflavin",
            "term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            }
          },
          {
            "preferred_term": "Nicotinic acid",
            "term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            }
          },
          {
            "preferred_term": "Calcium D-(+)-pantothenate",
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:31345",
              "label": "Calcium pantothenate"
            }
          },
          {
            "preferred_term": "Vitamin B12",
            "term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            },
            "concentration": {
              "value": "0.0001",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            }
          },
          {
            "preferred_term": "p-Aminobenzoic acid",
            "term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            }
          },
          {
            "preferred_term": "(DL)-alpha-Lipoic acid",
            "term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            }
          },
          {
            "preferred_term": "Nitrilotriacetic acid",
            "term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "CoSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CuSO4 x 5 H2O",
            "term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            }
          },
          {
            "preferred_term": "AlK(SO4)2 x 12 H2O",
            "term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "Na2SeO3 x 5 H2O",
            "term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            },
            "concentration": {
              "value": "0.0003",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            }
          },
          {
            "preferred_term": "Na2WO4 x 2 H2O",
            "term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            },
            "concentration": {
              "value": "0.0004",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "Na2HPO4 x 2 H2O",
            "term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            },
            "concentration": {
              "value": "0.42",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            }
          },
          {
            "preferred_term": "Na2HPO4 x H2O",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "notes": "[Collapsed 2 identical duplicates: 0.1, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.14",
              "unit": "G_PER_L"
            },
            "notes": " [Merged 2 duplicates: 0.04, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Cresol",
            "concentration": {
              "value": "1",
              "unit": "MILLIMOLAR"
            }
          },
          {
            "preferred_term": "Biotin",
            "term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            }
          },
          {
            "preferred_term": "Folic acid",
            "term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            }
          },
          {
            "preferred_term": "Pyridoxine hydrochloride",
            "term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            }
          },
          {
            "preferred_term": "Thiamine HCl",
            "term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            }
          },
          {
            "preferred_term": "Riboflavin",
            "term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            }
          },
          {
            "preferred_term": "Nicotinic acid",
            "term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            }
          },
          {
            "preferred_term": "Calcium D-(+)-pantothenate",
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:31345",
              "label": "Calcium pantothenate"
            }
          },
          {
            "preferred_term": "Vitamin B12",
            "term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            },
            "concentration": {
              "value": "0.0001",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            }
          },
          {
            "preferred_term": "p-Aminobenzoic acid",
            "term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            }
          },
          {
            "preferred_term": "(DL)-alpha-Lipoic acid",
            "term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            }
          },
          {
            "preferred_term": "Nitrilotriacetic acid",
            "term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "CoSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CuSO4 x 5 H2O",
            "term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            }
          },
          {
            "preferred_term": "AlK(SO4)2 x 12 H2O",
            "term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "Na2SeO3 x 5 H2O",
            "term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            },
            "concentration": {
              "value": "0.0003",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            }
          },
          {
            "preferred_term": "Na2WO4 x 2 H2O",
            "term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            },
            "concentration": {
              "value": "0.0004",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "Na2HPO4 x 2 H2O",
            "term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            },
            "concentration": {
              "value": "0.42",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            }
          },
          {
            "preferred_term": "Na2HPO4 x H2O",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "notes": "[Collapsed 2 identical duplicates: 0.1, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.14",
              "unit": "G_PER_L"
            },
            "notes": " [Merged 2 duplicates: 0.04, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Cresol",
            "concentration": {
              "value": "1",
              "unit": "MILLIMOLAR"
            }
          },
          {
            "preferred_term": "Biotin",
            "term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            }
          },
          {
            "preferred_term": "Folic acid",
            "term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            }
          },
          {
            "preferred_term": "Pyridoxine hydrochloride",
            "term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            }
          },
          {
            "preferred_term": "Thiamine HCl",
            "term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            }
          },
          {
            "preferred_term": "Riboflavin",
            "term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            }
          },
          {
            "preferred_term": "Nicotinic acid",
            "term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            }
          },
          {
            "preferred_term": "Calcium D-(+)-pantothenate",
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:31345",
              "label": "Calcium pantothenate"
            }
          },
          {
            "preferred_term": "Vitamin B12",
            "term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            },
            "concentration": {
              "value": "0.0001",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            }
          },
          {
            "preferred_term": "p-Aminobenzoic acid",
            "term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            }
          },
          {
            "preferred_term": "(DL)-alpha-Lipoic acid",
            "term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            }
          },
          {
            "preferred_term": "Nitrilotriacetic acid",
            "term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "CoSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CuSO4 x 5 H2O",
            "term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            }
          },
          {
            "preferred_term": "AlK(SO4)2 x 12 H2O",
            "term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "Na2SeO3 x 5 H2O",
            "term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            },
            "concentration": {
              "value": "0.0003",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            }
          },
          {
            "preferred_term": "Na2WO4 x 2 H2O",
            "term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            },
            "concentration": {
              "value": "0.0004",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "Na2HPO4 x 2 H2O",
            "term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            },
            "concentration": {
              "value": "0.42",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91258",
              "label": "disodium hydrogenphosphate dihydrate"
            }
          },
          {
            "preferred_term": "Na2HPO4 x H2O",
            "term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34683",
              "label": "disodium hydrogenphosphate"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "notes": "[Collapsed 2 identical duplicates: 0.1, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.14",
              "unit": "G_PER_L"
            },
            "notes": " [Merged 2 duplicates: 0.04, 0.1]",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Cresol",
            "concentration": {
              "value": "1",
              "unit": "MILLIMOLAR"
            }
          },
          {
            "preferred_term": "Biotin",
            "term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15956",
              "label": "biotin"
            }
          },
          {
            "preferred_term": "Folic acid",
            "term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:27470",
              "label": "folic acid"
            }
          },
          {
            "preferred_term": "Pyridoxine hydrochloride",
            "term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30961",
              "label": "pyridoxine hydrochloride"
            }
          },
          {
            "preferred_term": "Thiamine HCl",
            "term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:49105",
              "label": "thiamine hydrochloride"
            }
          },
          {
            "preferred_term": "Riboflavin",
            "term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17015",
              "label": "riboflavin"
            }
          },
          {
            "preferred_term": "Nicotinic acid",
            "term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:15940",
              "label": "nicotinic acid"
            }
          },
          {
            "preferred_term": "Calcium D-(+)-pantothenate",
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "term": {
              "id": "CHEBI:31345",
              "label": "Calcium pantothenate"
            }
          },
          {
            "preferred_term": "Vitamin B12",
            "term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            },
            "concentration": {
              "value": "0.0001",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:176843",
              "label": "vitamin B12"
            }
          },
          {
            "preferred_term": "p-Aminobenzoic acid",
            "term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:30753",
              "label": "4-aminobenzoic acid"
            }
          },
          {
            "preferred_term": "(DL)-alpha-Lipoic acid",
            "term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16494",
              "label": "lipoic acid"
            }
          },
          {
            "preferred_term": "Nitrilotriacetic acid",
            "term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            },
            "concentration": {
              "value": "1.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:44557",
              "label": "nitrilotriacetic acid"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "CoSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91244",
              "label": "cobalt(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.18",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CuSO4 x 5 H2O",
            "term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31440",
              "label": "copper(II) sulfate pentahydrate"
            }
          },
          {
            "preferred_term": "AlK(SO4)2 x 12 H2O",
            "term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86465",
              "label": "potassium aluminium sulfate dodecahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "Na2SeO3 x 5 H2O",
            "term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            },
            "concentration": {
              "value": "0.0003",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131361",
              "label": "disodium selenite pentahydrate"
            }
          },
          {
            "preferred_term": "Na2WO4 x 2 H2O",
            "term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            },
            "concentration": {
              "value": "0.0004",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63939",
              "label": "sodium tungstate dihydrate"
            }
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Distilled water'",
        "exact_source_quote": "Distilled water                                          1000.00    ml",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "Add this exact source batch input at its named stage. The table does not print ml/L for the two stock doses; the listed 1000 ml main water does not establish measured final volume."
  },
  {
    "decision_id": "q36",
    "subject": "Vitamin-stock water",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Wolin's vitamin solution (from medium 141); exact row containing Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Preserve 1000 ml as the separate stock water input. Do not import DSM141 main 1013 ml volume or infer stock makeup/final volume."
  },
  {
    "decision_id": "q37",
    "subject": "Mineral-stock water",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "Preserve 1000 ml as the separate stock water input. Do not import DSM141 main 1013 ml volume or infer stock makeup/final volume."
  },
  {
    "decision_id": "q38",
    "subject": "Explicit phenol stock dose per litre",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing '20 ml/l'",
        "exact_source_quote": "  (e.g.: 20 ml/l of a 4.7 g/l phenol-solution)",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The example explicitly states 20 ml/l of 4.7 g/l phenol solution. Preserve both dose and stock strength with that example scope; arithmetic 0.020 L × 4.7 g/L = 0.094 g per litre belongs outside the quote. This does not change the two stock-table 10 ml batch doses into per-litre doses."
  },
  {
    "decision_id": "q39",
    "subject": "Main pH 6.5",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 6.5. Add cresol/phenol after autoclaving.",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "Existing main pH 6.5 matches the explicit primary endpoint. Add exact current claim linkage; no titrant dose is stated."
  },
  {
    "decision_id": "q40",
    "subject": "Missing generated/KOMODO preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 6.5. Add cresol/phenol after autoclaving.",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "Add the exact main preparation sentence, keeping substrate addition after autoclaving and no conventional temperature or duration."
  },
  {
    "decision_id": "q41",
    "subject": "DSMZ owner extra preparation clauses",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve phosphates separately, Adjust pH to 6.5. Add cresol/phenol and vitamin solution after autoclaving."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 6.5. Add cresol/phenol after autoclaving.",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The current primary supports pH and post-autoclave cresol/phenol only. Its text does not support the local separate-phosphate instruction or the additional vitamin timing. Retain provenance of the old text while resolving the unsupported additions; excluded DSM141 parent gas/handling is not borrowed."
  },
  {
    "decision_id": "q42",
    "subject": "DSMZ owner phenol example",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "(e.g.: 20 ml/l of a 4.7 g/l phenol-solution)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing '20 ml/l'",
        "exact_source_quote": "  (e.g.: 20 ml/l of a 4.7 g/l phenol-solution)",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The existing example matches the explicit dose and stock strength; add narrow primary linkage."
  },
  {
    "decision_id": "q43",
    "subject": "Mineral preparation pH stages",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin mineral preparation",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\nfinal to pH 7.0 with KOH.",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The text is supported for the separate mineral stock. Keep its pH 6.5 then 7.0 endpoints and order separate from receiving-medium pH 6.5."
  },
  {
    "decision_id": "q44",
    "subject": "KOH titration amounts",
    "decision": "not_quantified",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing First dissolve nitrilotriacetic acid",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      },
      {
        "source_key": "dsmz141StockContext",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Modified Wolin's mineral solution (from medium 141); exact row containing final to pH",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ],
    "rationale": "The primary specifies pH endpoints using KOH but no fixed titrant dose. Do not invent one."
  },
  {
    "decision_id": "q45",
    "subject": "Incubation and autoclave temperature/duration",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BPHD_Medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz738",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf",
        "source_locator": "Exact extracted source line containing 'Adjust pH'",
        "exact_source_quote": "Adjust pH to 6.5. Add cresol/phenol after autoclaving.",
        "snapshot_sha256": "b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb",
        "parsed_text_sha256": "fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5"
      }
    ],
    "rationale": "The source mentions autoclaving without a cycle and gives no incubation temperature. Neither the parent methane-medium conditions nor customary cycles establish these missing values."
  }
]

## Findings

### f1: Separate the phenol source branch from copied cresol content

blocker / open / confirmed; issue key: bphd-phenol-variant-identity.

The exact phenol-replacement contributor is included in merged_from, but its maintained recipe retains Cresol 1 mM. Its current source names Phenol with null numeric cells, and DSM738 permits alternative cresol or phenol. The generated recipe cannot stand for both distinct choices without explicit variant identity.

### f2: Restore stock boundaries and distinct basal calcium/iron masses

major / open / confirmed; issue key: bphd-stock-stage-flattening.

Vitamin and mineral batches are flattened into main rates. The target calcium 0.2 and all local iron 0.14 collapse independent basal and stock inputs; owner calcium repair removes one duplicate but does not reconstruct the mineral stock. Water and 10 ml stock doses are absent.

### f3: Nickel hexahydrate is grounded to anhydrous nickel chloride

major / open / confirmed; issue key: bphd-nickel-hydrate-grounding.

All four inspected recipe layers name NiCl2 x 6 H2O but use CHEBI:34887 nickel dichloride in primary and secondary slots. Canonical label success does not establish the supplied hydrate.

### f4: Retain supported preparation and qualify unsupported source extensions

major / open / confirmed; issue key: bphd-preparation-source-scope.

The target loses preparation, while the DSMZ owner adds separate-phosphate and post-autoclave vitamin instructions absent from the current main primary. Mineral-stock pH preparation is valid only for that stock.

### f5: Historical date precision remains unresolved

minor / open / confirmed; issue key: bphd-history-timestamp-shape.

Malformed or timezone-absent historical timestamps remain preserved; they are not silently converted to exact UTC chronology.

## Recommended Actions And Acceptance Checks

### a1

Correct the exact phenol owner identity and represent the alternative formulation separately. Reassess source-duplicate relationships before authorized regeneration using the already conservative current grouping gate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent separate basal inputs, both complete stocks and their exact batch doses. Preserve conditional arithmetic only where source final-volume basis is explicit; do not replace unsupported rates with inferred ones.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the exact hexahydrate and current secondary mapping from inspected ontology evidence; retain ambiguity rather than substitute an unverified identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact main and stock preparation evidence at their own stages, resolve added clauses and preserve historical text as provenance rather than validated current instructions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Append verified clarification if available while retaining original history.

- Do not rewrite original timestamps or infer historical execution from current code.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BPHD_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bphd_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BPHD_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BPHD_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch045/442/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/442/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BPHD_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BPHD_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BPHD_Medium.yaml:1:id: CultureMech:006387<br>./data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml:1:id: CultureMech:006387<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch045/source-preflight-bound/442/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 38 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch045/442/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:31206": [{"label": "(NH4)Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "[NH4]Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Chloride", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium chloride", "match_type": "ontology_label", "identifier": "CHEBI:31206", "preferred_term": "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammoniumchlorid", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "azanium chloride", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(CAS: 12125-02-9)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(Fisher A 649-500)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl2", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "disodium hydrogenphosphate dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4 x2 H2O", "match_type": "synonym", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Dibasic sodium phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Disodium hydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Disodium Phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO anydrous", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2H2PO4", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride anhydrous", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl 2", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2  x 76 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "MgCl2 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2.6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS: 10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl (Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS: 7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klor-con", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klotrix", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "muriate of potash", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sylvite", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "Fe SO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous sulfate.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron (II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron(II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biotin (1 μg/μL)", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biotin (Vitamin B7)", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "biotina", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biotine", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "biotinum", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Coenzyme R", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D(+)-Biotin", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D-(+)-biotin", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D-Biotin", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "vitamin B7", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Vitamin H", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Acfol", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acide folique", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acido folico", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acidum folicum", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folate", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folic acid (5 μg/μL)", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folicet", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folinic acid (citrovorum)", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folsaeure", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N-pteroyl-L-glutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "PGA", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "PteGlu", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroyl-L-glutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroyl-L-monoglutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroylglutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroylmonoglutamic acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "vitamin B11", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "vitamin B9", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine . HCl", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine HCl", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine-HCl", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine-HCl (Vitamin B6)", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine-HCl (VitaminB6)", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine-hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine.HCL", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine·HCl", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine・HCl", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pyridoxol hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamin dichloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamin HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamin hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamin-HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine . HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamine chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamine dichloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine Dihydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl (B ) -", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl (Vitamin B )", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl (Vitamin B1)", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamine(2+) dichloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine-HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine·HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine・HCl", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine・HCl (see below)", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiaminium chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6,7-dimethyl-9-D-ribitylisoalloxazine", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "7,8-dimethyl-10-ribitylisoalloxazine", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Aqua-Flave", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Beflavin", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Beflavine", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bisulase", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dermadram", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E101", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Fiboflavin", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Flavaxin", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Flavin Bb", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Flaxain", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Hyflavin", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (0.05 μg/mL)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (0.2 mg/ml)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (see below)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (Vitamin B2)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (Vitamine B2)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavine", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavine (B2)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "3-carboxylpyridine", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-carboxypyridine", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-pyridinecarboxylic acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-Pyridylcarboxylic acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acide nicotinique", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acido nicotinico", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acidum nicotinicum", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "anti-pellagra vitamin", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "beta-pyridinecarboxylic acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "m-pyridinecarboxylic acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Niacin", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Niacor", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Niaspan", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinate", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinic acid (PP)", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinsaure", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nikotinsaeure", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "P.P. factor", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pellagra preventive factor", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "PP factor", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pyridine-3-carboxylic acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "CN-Cbl", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "CO-CYANOCOBALAMIN", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Coalpha-[alpha-(5,6-dimethylbenzimidazolyl)]-Cobeta-cyanocobamide", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocob(III)alamin", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocobalamin (B )", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocobalamin (Vitamin B )", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocobalamine", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocobalamin in", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Dicopac", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "vitamin B-12", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "Vitamin B12 (cyanocobalamin)", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Vitamin B12 complex", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "vitamin B12 vitamer", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "VitaminB12", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Vitamine B12", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Vitamin B12  (4)", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Vitamin B12  (8)", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Vitamin B12  (9)", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}], "CHEBI:30753": [{"label": "1-Amino-4-carboxybenzene", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Amino-benzoic acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Aminobenzoesaeure", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Aminobenzoic Acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-aminobenzoic acid zwitterion", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-ammoniobenzoate", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-azaniumylbenzoate", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Carboxyaniline", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Carboxyphenylamine", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ABEE", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "gamma-Aminobenzoic acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p--Aminobenzoic acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-Amino Benzoic Acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-Aminobenzoesaeure", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-aminobenzoic acid (0.3 μg/μL)", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-carboxyaniline", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-carboxyphenylamine", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "PABA", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Para-aminobenzoic acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "1,2-dithiolane-3-pentanoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "1,2-dithiolane-3-valeric acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-(1,2-dithiolan-3-yl)pentanoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-(1,2-dithiolan-3-yl)valeric acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-(dithiolan-3-yl)valeric acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-[3-(1,2-dithiolanyl)]pentanoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6,8-thioctic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6,8-thiotic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6-thioctic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6-thiotic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Acetate-replacing factor", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "alpha-lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "alpha-Liponsaeure", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biletan", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D,L-6,8-Thioctic Acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D,L-6,8-Thioctic Acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "DL-6,8-thioctic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "DL-alpha-lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Lipoate", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "lipoic acid", "match_type": "ontology_label", "identifier": "CHEBI:16494", "preferred_term": "Thioctic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "lipoic acid", "match_type": "ontology_label", "identifier": "CHEBI:16494", "preferred_term": "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "liponic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioctansaeure", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioctic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "Thioctic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Thioctic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioctsaeure", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioktsaeure", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "α--Lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "α-lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "α-lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Complexon I", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3nta", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Komplexon I", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N(CH2-COOH)3", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N,N-bis(carboxymethyl)glycine", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nitrilo-2,2',2''-triacetic acid", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nitrilotriacetic acid (NTA)", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nitrilotriessigsaeure", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "tri(carboxymethyl)amine", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "triglycine", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Triglycollamic acid", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Trilon A", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "Cobalt sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zinc sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc sulfate heptahydrate (1:1:7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zn2SO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 .7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 × 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4-7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4∙7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4･7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "Copper (II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulphate(5.H2O)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate (1:1) pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cupric sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO .5H O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 .5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 · 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 ⋅ 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4*5 H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4.5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4·5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4・5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2.12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2・12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aluminium potassium sulfate--water (1/12)", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium disulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium sulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 x 12 H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2・12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kalinite", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potash alum dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium alum dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "potassium aluminium sulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium aluminum disulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2 MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "[NiCl2]", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel dichloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(2+) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel(II) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(II) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NiCl 2", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "disodium selenite hydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium selenite pentahydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium selenite pentahydrate", "match_type": "ontology_label", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2Se3 x 5 H2O", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 x 5 H2O (0.01% w/v)", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 x 5 H2O (0.01% w/v)", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2SeO3·5H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2SeO3·5H2O", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3・5H2O", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Selenious acid disodium salt, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium selenite hydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium selenite pentahydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium selenite--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Disodium tetraoxotungstate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na-tungstate x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 × 2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4•2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaWO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)tungsten--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthotungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tetraoxotungstate(VI)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungstate(VI)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tungstate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungsten oxide", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium wolframate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic acid, disodium salt", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic acid, sodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BPHD_Medium.yaml; data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml; data/normalized_yaml/bacterial/bphd_medium.yaml; data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.967726"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.967726"}]}, {"input": "data/normalized_yaml/bacterial/bphd_medium.yaml", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:03.795268"}]}] |
| history-full | /private/tmp/culturemech-review-work-batch045/442/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch045/442/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf; Complete DSMZ 738 recipe, footnote and preparation | supports | Basal masses, 10 ml of each DSM141 stock, 1000 ml water, cresol or phenol 1 mM, pH 6.5 and post-autoclave substrate addition are explicit. The phenol example explicitly gives 20 ml/l of 4.7 g/l stock. |
| stocks | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Modified Wolin mineral and Wolin vitamin subsections only | supports | Only the two named stock recipes transfer. DSM141 basal medium, 1013 ml final volume, parent gases, pressures, strain variants and their quantities are excluded. Stock water is listed as 1000 ml; neither stock subsection says to make up to a final litre. |
| provider-base | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738; Exact accession 738 features and full metabolites table | supports | Current provider labels rates per litre and displays a different normalized set, including NH4Cl 0.98, phosphate dihydrate 0.41, diluted stocks and cresol 0.32 g/L. These are distinct provider claims, not a primary measured denominator or an instruction to combine cresol isomers. |
| provider-phenol | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738_replace_Cresol_with_Phenol; Exact variant accession and metabolites Phenol row | supports | Current phenol variant names phenol-solution with null mass/molar values and no cresol row. The maintained phenol-named owner instead contains Cresol 1 mM. |
| mediadive738api-attempt | https://mediadive.dsmz.de/rest/medium/738; Preserved exact public retrieval result | context_only | The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock primaries and exact KOMODO base/variant pages are usable; no unavailable API response is treated as amount authentication. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current CLI calls conservative formulation grouping with scientific-field equality. Existing flattened/generated content and the phenol-owner identity defect require maintained-input correction followed by regeneration and freshness checks. Old fingerprint grouping is historical context, not proof that the current generator still blindly combines ingredient sets. |
| writer-1 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current CLI calls conservative formulation grouping with scientific-field equality. Existing flattened/generated content and the phenol-owner identity defect require maintained-input correction followed by regeneration and freshness checks. Old fingerprint grouping is historical context, not proof that the current generator still blindly combines ingredient sets. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current CLI calls conservative formulation grouping with scientific-field equality. Existing flattened/generated content and the phenol-owner identity defect require maintained-input correction followed by regeneration and freshness checks. Old fingerprint grouping is historical context, not proof that the current generator still blindly combines ingredient sets. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch045/442/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock primaries and exact KOMODO base/variant pages are usable; no unavailable API response is treated as amount authentication.
- The source second-phosphate spelling remains unresolved; no corrected chemical formula is invented.
- The exact DSM141 parent record is context only. Its main quantities, gases, pressure, strains and final volume do not transfer to BPHD.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T020623Z-culturemech-006387-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bphd_medium (CultureMech:006387)'
started_at: '2026-10-22T02:02:37Z'
finished_at: '2026-10-22T02:06:23Z'
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
summary: BPHD is represented as a flattened mixture of basal and stock ingredients,
  with a phenol-named contributor still containing cresol. The exact primary supports
  separate vitamin/mineral stocks and substrate alternatives, while current provider
  displays differ from stored rates. Restore source stages and variant identity before
  regeneration; do not infer final volumes or repair the anomalous phosphate formula
  by guesswork.
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
  - path: data/merge_yaml/merged/BPHD_Medium.yaml
    sha256: 9ed422c6808c6cd5081180eaebd331fcda113b62f9a7db3fd347a5d57714512e
    role: target
  - path: data/normalized_yaml/archaea/methanogenium_medium_h2_co2.yaml
    sha256: 7d9f3fc0fab5ea985fdca11a2a39449646302a6c01d8479b1c208e708d608e6b
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    sha256: 56a34ecf674a5819eaa950cbbc98a72469d32241ccedc6aecefb023b35124fe3
    role: context
  - path: data/normalized_yaml/bacterial/bphd_medium.yaml
    sha256: c29403b3c528587531a17832955c003654c387a851a2f4ca9f2aa7fee9340df7
    role: context
  - path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
    sha256: 996ab91e4ee3941703d8878179f089eba17c32cc191aa193d8e577bddb9a6573
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_738_BPHD_Medium.yaml.md
    sha256: 40e9e07684dc90a5645a4af259c3653d56c1b4f5d20cc91b897c9495b7c93ef7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/bphd_medium_replace_cresol_with_phenol.yaml.md
    sha256: 510b16ba0d29e9acdc20b0402c1b2934f032734ec2068e99bd00c1001778ba81
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/bphd_medium.yaml.md
    sha256: 4a47fcf5860cd3b2fd6032565119e511eaa15f61717bd2d6ff6ade2fa89de0ba
    role: context
  - path: reports/yaml_record_review/20260921T232424Z-BPHD_Medium.md
    sha256: beceeefd3df01328cccfa272a2a650840b0e6c2cddda05fb9422f52bbe1cda12
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
  selection: Task review 442; batch 045 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:006387
targets:
- target_id: CultureMech:006387
  path: data/merge_yaml/merged/BPHD_Medium.yaml
  label: bphd_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BPHD_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BPHD_Medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch045/442/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/442/strict.tsv"
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BPHD_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BPHD_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006387
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
  - CultureMech:006387
- check_id: mediadive738api-source-access
  name: 'Exact source content access: mediadive738api'
  required: false
  status: unavailable
  summary: The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock
    primaries and exact KOMODO base/variant pages are usable; no unavailable API response
    is treated as amount authentication.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - mediadive738api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BPHD_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bphd_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BPHD_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:04.618527Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BPHD_Medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch045/442/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:06.367117Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/442/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BPHD_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:07.939209Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BPHD_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:09.152137Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T02:06:21Z'
  support: supports
  summary: './data/merge_yaml/merged/BPHD_Medium.yaml:1:id: CultureMech:006387

    ./data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml:1:id: CultureMech:006387

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/source-preflight-bound/442/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T02:06:21Z'
  support: supports
  summary: 38 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e8465fb69d083305d1ac4e66b2b368068912ba9b4dbe6ef2cf2f4beda5b36b2a
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/442/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: 7bb1479f00227374cc991c17852a672a8f6ad635f50e0101c1e702a1989c6c07
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
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
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:24.147433Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:25.002266Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:23.223232Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:24.193584Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
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
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:31206":
    [{"label": "(NH4)Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "[NH4]Cl", "match_type": "synonym", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Ammonium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium chloride",
    "match_type": "ontology_label", "identifier": "CHEBI:31206", "preferred_term":
    "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)",
    "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)",
    "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl",
    "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Ammoniumchlorid", "match_type": "synonym", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "azanium chloride", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(CAS:
    12125-02-9)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NH4Cl(Fisher A 649-500)", "match_type": "synonym", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl2", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label":
    "disodium hydrogenphosphate dihydrate", "match_type": "ontology_label", "identifier":
    "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term":
    "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2HPO4 x 2H2O", "match_type": "synonym", "identifier":
    "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4 x2 H2O",
    "match_type": "synonym", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4
    x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2HPO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:91258",
    "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Dibasic sodium phosphate",
    "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4",
    "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Disodium hydrogen phosphate", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type":
    "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium
    hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683",
    "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Disodium Phosphate", "match_type":
    "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na
    HPO", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term":
    "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na HPO anydrous", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2H2PO4", "match_type": "synonym",
    "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    phosphate dibasic", "match_type": "preferred_term", "identifier": "CHEBI:34683",
    "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type":
    "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium
    chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Magnesium chloride anhydrous", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium
    chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Magnesium chloride hydrate", "match_type": "synonym", "identifier":
    "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride
    hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/2)",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium
    chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl 2", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium
    chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x
    7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "MgCl2  x 76 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier":
    "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "MgCl2 x 7H2O", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"},
    {"label": "MgCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2.6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x
    6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x
    6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x7H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x
    6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x
    6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2
    x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2⋅6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2・6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2
    x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x
    2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50
    g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution
    (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type":
    "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label":
    "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS:
    10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water
    (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type": "synonym", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl (Fisher P 217)",
    "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl",
    "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KCl(CAS: 7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)", "match_type": "synonym",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(Fisher P 217)",
    "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl",
    "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Klor-con", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Klotrix", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Monopotassium chloride", "match_type": "synonym",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "muriate of potash",
    "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl",
    "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Potassium Chloride", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "sylvite", "match_type": "synonym", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "Fe SO4 x 7 H2O",
    "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4
    x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ferrous sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous
    sulfate.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4
    x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4
    x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4
    · 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4
    x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4・7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron
    (II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type":
    "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O",
    "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Iron(II) sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956":
    [{"label": "(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "match_type":
    "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric
    acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic
    acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Biotin (1 μg/μL)", "match_type": "synonym",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Biotin (Vitamin
    B7)", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "biotina", "match_type": "synonym", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Biotine", "match_type": "synonym", "identifier":
    "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "biotinum", "match_type": "synonym",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric
    acid", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid",
    "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin",
    "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "match_type":
    "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Coenzyme
    R", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin",
    "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "D(+)-Biotin", "match_type": "synonym", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "D-(+)-biotin", "match_type": "synonym", "identifier":
    "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "D-Biotin", "match_type": "synonym",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "vitamin B7", "match_type":
    "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Vitamin
    H", "match_type": "synonym", "identifier": "CHEBI:15956", "preferred_term": "Biotin",
    "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:27470": [{"label": "(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic
    acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Acfol", "match_type": "synonym", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "acide folique", "match_type": "synonym",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acido folico",
    "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic
    acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "acidum folicum", "match_type": "synonym", "identifier":
    "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Folate", "match_type": "synonym",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid",
    "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Folic acid (5 μg/μL)", "match_type": "synonym", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Folicet", "match_type": "synonym",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Folinic acid (citrovorum)",
    "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic
    acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Folsaeure", "match_type": "synonym", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic
    acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "N-pteroyl-L-glutamic acid", "match_type": "synonym", "identifier":
    "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "PGA", "match_type": "synonym", "identifier":
    "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "PteGlu", "match_type": "synonym",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroyl-L-glutamic
    acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "pteroyl-L-monoglutamic acid", "match_type": "synonym", "identifier":
    "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "pteroylglutamic acid", "match_type":
    "synonym", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id":
    "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pteroylmonoglutamic
    acid", "match_type": "synonym", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "vitamin B11", "match_type": "synonym", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "vitamin B9", "match_type": "synonym",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label":
    "2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "match_type":
    "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "match_type":
    "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "match_type":
    "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "match_type":
    "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Pyridoxine . HCl", "match_type": "synonym", "identifier": "CHEBI:30961",
    "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine HCl", "match_type": "synonym",
    "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id":
    "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine
    hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Pyridoxine-HCl", "match_type": "synonym", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine-HCl
    (Vitamin B6)", "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Pyridoxine-HCl (VitaminB6)", "match_type":
    "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Pyridoxine-hydrochloride", "match_type": "synonym", "identifier": "CHEBI:30961",
    "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine.HCL", "match_type": "synonym",
    "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id":
    "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Pyridoxine·HCl",
    "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine
    hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Pyridoxine・HCl", "match_type": "synonym", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pyridoxol hydrochloride",
    "match_type": "synonym", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine
    hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49105": [{"label": "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "thiamin dichloride", "match_type": "synonym", "identifier":
    "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamin HCl", "match_type":
    "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamin
    hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Thiamin-HCl", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine . HCl", "match_type": "synonym",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamine
    chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "thiamine dichloride", "match_type":
    "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine
    Dihydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Thiamine HCl", "match_type": "preferred_term", "identifier":
    "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl (B
    ) -", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Thiamine HCl (Vitamin B )", "match_type": "synonym", "identifier":
    "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl (Vitamin
    B1)", "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Thiamine hydrochloride", "match_type": "synonym", "identifier":
    "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiamine(2+) dichloride",
    "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine
    HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Thiamine-HCl", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine HCl", "match_type": "synonym",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine·HCl",
    "match_type": "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine
    HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Thiamine・HCl", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thiamine・HCl (see below)", "match_type":
    "synonym", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "thiaminium
    chloride hydrochloride", "match_type": "synonym", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "6,7-dimethyl-9-D-ribitylisoalloxazine", "match_type": "synonym", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "7,8-dimethyl-10-ribitylisoalloxazine", "match_type": "synonym", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Aqua-Flave", "match_type": "synonym",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Beflavin", "match_type":
    "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id":
    "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Beflavine",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Bisulase", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Dermadram", "match_type": "synonym", "identifier": "CHEBI:17015",
    "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "E101", "match_type": "synonym", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Fiboflavin", "match_type": "synonym",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Flavaxin", "match_type":
    "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id":
    "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Flavin
    Bb", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Flaxain", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Hyflavin", "match_type": "synonym", "identifier": "CHEBI:17015",
    "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin", "match_type": "preferred_term",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (0.05
    μg/mL)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Riboflavin (0.2 mg/ml)", "match_type": "synonym", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin (see below)", "match_type":
    "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id":
    "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavin
    (Vitamin B2)", "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Riboflavin (Vitamine B2)", "match_type": "synonym", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavine", "match_type": "synonym",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Riboflavine (B2)",
    "match_type": "synonym", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15940": [{"label": "3-carboxylpyridine", "match_type": "synonym", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-carboxypyridine",
    "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic
    acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "3-pyridinecarboxylic acid", "match_type": "synonym", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "3-Pyridylcarboxylic
    acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "acide nicotinique", "match_type": "synonym", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acido nicotinico",
    "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic
    acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "acidum nicotinicum", "match_type": "synonym", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "anti-pellagra vitamin",
    "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic
    acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "beta-pyridinecarboxylic acid", "match_type": "synonym",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "m-pyridinecarboxylic
    acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Niacin", "match_type": "synonym", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Niacor", "match_type": "synonym",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Niaspan",
    "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic
    acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Nicotinate", "match_type": "synonym", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nicotinic
    acid (PP)", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Nicotinsaure", "match_type": "synonym", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Nikotinsaeure", "match_type": "synonym",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "P.P.
    factor", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "pellagra preventive factor", "match_type": "synonym", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "PP factor", "match_type":
    "synonym", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "pyridine-3-carboxylic
    acid", "match_type": "synonym", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:176843": [{"label": "CN-Cbl", "match_type": "synonym", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label":
    "CO-CYANOCOBALAMIN", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "Coalpha-[alpha-(5,6-dimethylbenzimidazolyl)]-Cobeta-cyanocobamide",
    "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin
    B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "Cyanocob(III)alamin", "match_type":
    "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"},
    {"label": "Cyanocobalamin (B )", "match_type": "synonym", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Cyanocobalamin
    (Vitamin B )", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "Cyanocobalamine", "match_type": "synonym",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"},
    {"label": "Cyanocobalamin in", "match_type": "synonym", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Dicopac", "match_type":
    "synonym", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"},
    {"label": "vitamin B-12", "match_type": "synonym", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "Vitamin B12",
    "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}, {"label": "Vitamin B12 (cyanocobalamin)", "match_type": "synonym",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "Vitamin B12 complex", "match_type": "synonym", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "vitamin B12
    vitamer", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "VitaminB12", "match_type": "synonym",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "Vitamine B12", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Vitamin B12  (4)", "match_type": "synonym", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}, {"label":
    "Vitamin B12  (8)", "match_type": "synonym", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "Vitamin B12  (9)", "match_type": "synonym",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "unresolved:partial_chemistry"}],
    "CHEBI:30753": [{"label": "1-Amino-4-carboxybenzene", "match_type": "synonym",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Amino-benzoic
    acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "4-Aminobenzoesaeure", "match_type": "synonym",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "4-Aminobenzoic
    Acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "4-aminobenzoic acid zwitterion", "match_type":
    "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid",
    "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "4-ammoniobenzoate", "match_type": "synonym", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "4-azaniumylbenzoate", "match_type":
    "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid",
    "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "4-Carboxyaniline", "match_type": "synonym", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "4-Carboxyphenylamine", "match_type":
    "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid",
    "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "ABEE", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "gamma-Aminobenzoic acid", "match_type": "synonym",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p--Aminobenzoic
    acid", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "p-Amino Benzoic Acid", "match_type": "synonym",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-Aminobenzoesaeure",
    "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-aminobenzoic
    acid (0.3 μg/μL)", "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "p-carboxyaniline", "match_type": "synonym",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "p-carboxyphenylamine",
    "match_type": "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "PABA", "match_type": "synonym", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Para-aminobenzoic acid", "match_type":
    "synonym", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid",
    "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "1,2-dithiolane-3-pentanoic
    acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "1,2-dithiolane-3-valeric acid", "match_type":
    "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid",
    "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "5-(1,2-dithiolan-3-yl)pentanoic acid", "match_type": "synonym", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "5-(1,2-dithiolan-3-yl)valeric
    acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "5-(dithiolan-3-yl)valeric acid", "match_type":
    "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid",
    "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "5-[3-(1,2-dithiolanyl)]pentanoic acid", "match_type": "synonym", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6,8-thioctic acid",
    "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "6,8-thiotic acid", "match_type": "synonym", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "6-thioctic acid",
    "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "6-thiotic acid", "match_type": "synonym", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Acetate-replacing
    factor", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "alpha-lipoic acid", "match_type": "synonym",
    "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "alpha-Liponsaeure",
    "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Biletan", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "D,L-6,8-Thioctic Acid", "match_type":
    "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid",
    "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "D,L-6,8-Thioctic Acid", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "DL-6,8-thioctic acid", "match_type":
    "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid",
    "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "DL-alpha-lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Lipoate", "match_type": "synonym",
    "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Lipoic
    acid", "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "lipoic acid", "match_type": "ontology_label",
    "identifier": "CHEBI:16494", "preferred_term": "Thioctic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "lipoic acid", "match_type": "ontology_label", "identifier": "CHEBI:16494", "preferred_term":
    "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "liponic acid", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thioctansaeure", "match_type": "synonym",
    "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioctic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "Thioctic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Thioctic acid", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thioctsaeure", "match_type": "synonym",
    "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id":
    "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioktsaeure",
    "match_type": "synonym", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "α--Lipoic acid", "match_type": "synonym", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "α-lipoic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "α-lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "α-lipoic acid", "match_type": "synonym", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "alpha,alpha'',alpha''''-trimethylaminetricarboxylic
    acid", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term":
    "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Complexon I", "match_type": "synonym", "identifier":
    "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3nta", "match_type":
    "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid",
    "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Komplexon I", "match_type": "synonym", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "N(CH2-COOH)3", "match_type": "synonym",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "N,N-bis(carboxymethyl)glycine",
    "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "nitrilo-2,2'',2''''-triacetic acid", "match_type": "synonym",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nitrilotriacetic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term":
    "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Nitrilotriacetic acid (NTA)", "match_type":
    "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid",
    "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Nitrilotriessigsaeure", "match_type": "synonym", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "tri(carboxymethyl)amine", "match_type":
    "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid",
    "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "triglycine", "match_type": "synonym", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Triglycollamic acid", "match_type":
    "synonym", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid",
    "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Trilon A", "match_type": "synonym", "identifier": "CHEBI:44557", "preferred_term":
    "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1%
    w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS:
    10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric
    acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese sulfate", "match_type": "synonym", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate
    hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate
    monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4
    ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O",
    "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4
    x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity":
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
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244":
    [{"label": "Cobalt sulfate heptahydrate", "match_type": "synonym", "identifier":
    "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) sulfate
    heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CoSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id":
    "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4
    ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CoSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4·7H2O", "match_type": "synonym",
    "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id":
    "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoSO4・7H2O",
    "match_type": "synonym", "identifier": "CHEBI:91244", "preferred_term": "CoSO4
    x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1) heptahydrate", "match_type":
    "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zinc
    sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "zinc sulfate heptahydrate (1:1:7)", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+)
    sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "zinc(2+) sulfate--water (1/7)", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zn2SO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 .7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4
    x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4
    × 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4-7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4∙7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4･7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "Copper (II) sulfate
    pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper sulfate pentahydrate", "match_type": "synonym", "identifier":
    "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulphate(5.H2O)",
    "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4
    x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(2+) sulfate (1:1) pentahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+)
    sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(2+) sulfate--water (1/5)", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II)
    sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(II) sulfate, pentahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cupric
    sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO .5H O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 . 5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4
    .5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5H2O",
    "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4
    x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4 · 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 ⋅ 5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4*5
    H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4.5H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4·5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4・5H2O",
    "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4
    x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 . 12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2
    12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2
    x 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "AlK(SO4)2.12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2·12H2O",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "AlK(SO4)2・12H2O", "match_type": "synonym", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aluminium potassium
    sulfate--water (1/12)", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium disulfate dodecahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Aluminum potassium sulfate dodecahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KAl(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 x 12 H2O", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KAl(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2・12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kalinite",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potash alum dodecahydrate", "match_type": "synonym", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium alum
    dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "potassium aluminium sulfate dodecahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium aluminum disulfate dodecahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide",
    "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3",
    "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type":
    "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric
    acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2
    MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4
    . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O",
    "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O",
    "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water
    (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI)
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "[NiCl2]", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Nickel chloride", "match_type": "synonym", "identifier":
    "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "nickel chloride", "match_type": "synonym",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel dichloride",
    "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2",
    "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "nickel(2+) chloride", "match_type": "synonym", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Nickel(II) chloride", "match_type": "synonym",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(II) chloride",
    "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2",
    "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NiCl 2", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:131361": [{"label": "disodium selenite hydrate",
    "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3
    x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "disodium selenite pentahydrate", "match_type": "synonym",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "disodium selenite pentahydrate", "match_type": "ontology_label", "identifier":
    "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2Se3 x 5 H2O",
    "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3
    x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2SeO3 . 5H2O", "match_type": "synonym", "identifier":
    "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 . 5H2O",
    "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O",
    "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3 x 5 H2O (0.01% w/v)", "match_type":
    "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O",
    "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na2SeO3 x 5 H2O (0.01% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2SeO3·5H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term":
    "Na2SeO3·5H2O", "ontology_id": "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2SeO3·5H2O", "match_type": "synonym", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3・5H2O", "match_type": "synonym",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3·5H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Selenious acid disodium salt, pentahydrate", "match_type": "synonym", "identifier":
    "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium selenite
    hydrate", "match_type": "synonym", "identifier": "CHEBI:131361", "preferred_term":
    "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium selenite pentahydrate", "match_type":
    "synonym", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O",
    "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sodium selenite--water (1/5)", "match_type": "synonym", "identifier":
    "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label":
    "Disodium tetraoxotungstate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na-tungstate x 2 H2O", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2
    x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO2.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 . 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 × 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4.2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4•2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4・2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaWO4·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium dioxido(dioxo)tungsten--water (1/2)", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    orthotungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium tetraoxotungstate(VI)", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    tungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium tungstate(VI)", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tungstate(VI)
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium tungsten oxide", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium wolframate",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Tungstic acid, disodium salt", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic
    acid, sodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BPHD_Medium.yaml; data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml;
    data/normalized_yaml/bacterial/bphd_medium.yaml; data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:59.967726"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.967726"}]}, {"input": "data/normalized_yaml/bacterial/bphd_medium.yaml",
    "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:03.795268"}]}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/442/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 3d0a47d7c59aa7bc34cbac249f754abc3eead634a9c62d51e0bd7c14e1eb6f9b
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/442/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: 60573cf5d1f4f037c6d7296f3156d72b11e92233d1d8896f7aa8f37aee9047ab
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf
  locator: Complete DSMZ 738 recipe, footnote and preparation
  accessed_at: '2026-10-22T01:49:17.202971Z'
  support: supports
  summary: Basal masses, 10 ml of each DSM141 stock, 1000 ml water, cresol or phenol
    1 mM, pH 6.5 and post-autoclave substrate addition are explicit. The phenol example
    explicitly gives 20 ml/l of 4.7 g/l stock.
  quote: 738. BPHD Medium
  snapshot_sha256: b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb
- evidence_id: stocks
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: Modified Wolin mineral and Wolin vitamin subsections only
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Only the two named stock recipes transfer. DSM141 basal medium, 1013 ml
    final volume, parent gases, pressures, strain variants and their quantities are
    excluded. Stock water is listed as 1000 ml; neither stock subsection says to make
    up to a final litre.
  quote: Modified Wolin's mineral solution (from medium 141)
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: provider-base
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738
  locator: Exact accession 738 features and full metabolites table
  accessed_at: '2026-10-22T01:51:10.822589Z'
  support: supports
  summary: Current provider labels rates per litre and displays a different normalized
    set, including NH4Cl 0.98, phosphate dihydrate 0.41, diluted stocks and cresol
    0.32 g/L. These are distinct provider claims, not a primary measured denominator
    or an instruction to combine cresol isomers.
  snapshot_sha256: 0ceb2324c907dbc3fd947fcc5141bc55eba6fed02d441d4d451c81dccff9698c
- evidence_id: provider-phenol
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738_replace_Cresol_with_Phenol
  locator: Exact variant accession and metabolites Phenol row
  accessed_at: '2026-10-22T01:51:11.332046Z'
  support: supports
  summary: Current phenol variant names phenol-solution with null mass/molar values
    and no cresol row. The maintained phenol-named owner instead contains Cresol 1
    mM.
  snapshot_sha256: b635e7cb24c4f816fcc36fd99199ea7a68c642ce7e38a856cc351fa5d6cf9642
- evidence_id: mediadive738api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/738
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:49:18.773517Z'
  support: context_only
  summary: The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock
    primaries and exact KOMODO base/variant pages are usable; no unavailable API response
    is treated as amount authentication.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: The current CLI calls conservative formulation grouping with scientific-field
    equality. Existing flattened/generated content and the phenol-owner identity defect
    require maintained-input correction followed by regeneration and freshness checks.
    Old fingerprint grouping is historical context, not proof that the current generator
    still blindly combines ingredient sets.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: The current CLI calls conservative formulation grouping with scientific-field
    equality. Existing flattened/generated content and the phenol-owner identity defect
    require maintained-input correction followed by regeneration and freshness checks.
    Old fingerprint grouping is historical context, not proof that the current generator
    still blindly combines ingredient sets.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: The current CLI calls conservative formulation grouping with scientific-field
    equality. Existing flattened/generated content and the phenol-owner identity defect
    require maintained-input correction followed by regeneration and freshness checks.
    Old fingerprint grouping is historical context, not proof that the current generator
    still blindly combines ingredient sets.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/442/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T02:06:21Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a4cde060f5a9a2239c28b1d5232ad783f2bf4744d8c1fa0f9e0180a5088023f0
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: supported
  summary: 30 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label
    mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly.
    29/29 asserted current secondary keys have exact pinned index rows. Target primary
    linkage is 30/31 (96.77%) and current secondary linkage is 29/31 (93.55%) on a
    0–100 linkage scale, not a correctness score. Current missing keys do not prove
    historical invalidity; compatible generic source wording does not establish a
    stereochemical conflict.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - grounding-inventory
  - mim
  - chebi31206
  - chebi91258
  - chebi34683
  - chebi86345
  - chebi86158
  - chebi32588
  - chebi75836
  - chebi15956
  - chebi27470
  - chebi30961
  - chebi49105
  - chebi17015
  - chebi15940
  - chebi31345
  - chebi176843
  - chebi30753
  - chebi16494
  - chebi44557
  - chebi31795
  - chebi86364
  - chebi26710
  - chebi91244
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi34887
  - chebi131361
  - chebi63939
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 40 timestamp instances inspected; 6 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: identity
  area: identity
  topic: Base recipe and distinct phenol branch
  outcome: concern
  summary: The three native contributors are exact maintained inputs, but source identity
    does not make their recipes interchangeable. The phenol replacement accession
    must retain phenol rather than the copied cresol entry. Source permits either
    substrate, not both and not a mixture of all cresol isomers. Catalog Is Aerobic=false
    and Is Complex=false do not override the recipe or establish an anoxic requirement.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - record
  - primary
  - provider-base
  - provider-phenol
- assessment_id: stock-boundaries
  area: quantity
  topic: Basal masses, stock batches and doses
  outcome: concern
  summary: All four local layers flatten ten vitamins and mineral-stock ingredients
    into main G_PER_L fields. Main FeSO4 0.04 g and stock FeSO4 0.10 g are combined
    as 0.14; target calcium 0.2 combines two 0.1 entries, while current owners collapsed
    these to 0.1 but still lost the stock boundary. The two 10 ml doses and three
    distinct listed-water inputs must be preserved; no measured main or stock final
    volume is established by the PDF tables.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - primary
  - stocks
  - record
- assessment_id: chemical-forms
  area: grounding
  topic: Supported hydrates, source spelling and nickel form
  outcome: concern
  summary: The primary literally prints Na2H2PO4 x H2O for the second phosphate. The
    local Na2HPO4 x H2O label and anhydrous CHEBI:34683 do not resolve that source
    ambiguity. Do not silently replace it with a plausible mono- or dibasic phosphate.
    The named NiCl2 hexahydrate is mapped to anhydrous CHEBI:34887. Calcium D-pantothenate
    agrees with the D structure in CHEBI:31345; generic lipoic acid is compatible
    with DL source wording. Primary thiamine HCl and current KOMODO thiamine-HCl dihydrate
    remain distinct source formulations.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - primary
  - stocks
  - grounding-inventory
  - chebi34887
  - chebi34683
  - chebi31345
  - chebi16494
  - provider-base
- assessment_id: preparation
  area: representation
  topic: Supported preparation versus imported additions
  outcome: concern
  summary: Main pH 6.5 and substrate addition after autoclaving are explicit. The
    source stock subsection has an initial pH 6.5 and final pH 7.0 using KOH; these
    do not alter main pH. The DSMZ owner additionally says to dissolve phosphates
    separately and add vitamins after autoclaving, neither stated in the current DSM738
    primary. No heating temperature/duration or incubation condition is supplied.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - primary
  - stocks
  - record
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 45 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006387
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Basal NH4Cl\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'NH4Cl'\"\
    ,\n        \"exact_source_quote\": \"NH4Cl                                   \
    \                    1.00     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this nominal batch\
    \ mass, not the stored final-litre basis. Current provider displays are separately\
    \ normalized/rounded and do not establish a measured denominator for the stored\
    \ recipe. Preserve the exact source mass and unit; the second phosphate identity\
    \ remains unresolved rather than silently corrected.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"subject\": \"Basal Na2HPO4 x 2 H2O\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2HPO4\
    \ x 2'\",\n        \"exact_source_quote\": \"Na2HPO4 x 2 H2O                 \
    \                            0.42     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this nominal batch\
    \ mass, not the stored final-litre basis. Current provider displays are separately\
    \ normalized/rounded and do not establish a measured denominator for the stored\
    \ recipe. Preserve the exact source mass and unit; the second phosphate identity\
    \ remains unresolved rather than silently corrected.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"subject\": \"Basal Na2HPO4 x H2O\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Na2H2PO4'\"\
    ,\n        \"exact_source_quote\": \"Na2H2PO4 x H2O                          \
    \                    0.18     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this nominal batch\
    \ mass, not the stored final-litre basis. Current provider displays are separately\
    \ normalized/rounded and do not establish a measured denominator for the stored\
    \ recipe. Preserve the exact source mass and unit; the second phosphate identity\
    \ remains unresolved rather than silently corrected.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"subject\": \"Basal MgCl2 x 6 H2O\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'MgCl2'\"\
    ,\n        \"exact_source_quote\": \"MgCl2 x 6 H2O                           \
    \                    0.10     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this nominal batch\
    \ mass, not the stored final-litre basis. Current provider displays are separately\
    \ normalized/rounded and do not establish a measured denominator for the stored\
    \ recipe. Preserve the exact source mass and unit; the second phosphate identity\
    \ remains unresolved rather than silently corrected.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"subject\": \"Basal KCl\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'KCl'\"\
    ,\n        \"exact_source_quote\": \"KCl                                     \
    \                    0.10     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports this nominal batch\
    \ mass, not the stored final-litre basis. Current provider displays are separately\
    \ normalized/rounded and do not establish a measured denominator for the stored\
    \ recipe. Preserve the exact source mass and unit; the second phosphate identity\
    \ remains unresolved rather than silently corrected.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"subject\": \"Separate basal and mineral-stock CaCl2 x 2 H2O\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'CaCl2\
    \ x 2'\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O                   \
    \                            0.10     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      },\n      {\n        \"source_key\": \"dsmz141StockContext\",\n      \
    \  \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing CaCl2 x 2\",\n        \"exact_source_quote\": \"\
    CaCl2 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"These are two separate source-stage amounts,\
    \ not additive whole-medium rates. Calcium is 0.10 g in the basal batch and 0.10\
    \ g in the stock; iron is 0.04 g basal and 0.10 g stock. The target calcium 0.2\
    \ and every layer iron 0.14 combine stages incorrectly. Owners collapsed calcium\
    \ to 0.1 but still omit its stock input. Reconstruct both stages and the stock\
    \ dose without inventing final-litre values.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"subject\": \"Separate basal and mineral-stock FeSO4 x 7 H2O\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.14\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.14\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.14\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.14\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'FeSO4\
    \ x 7'\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O                   \
    \                            0.04     g\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      },\n      {\n        \"source_key\": \"dsmz141StockContext\",\n      \
    \  \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing FeSO4 x 7\",\n        \"exact_source_quote\": \"\
    FeSO4 x 7 H2O 0.10 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"These are two separate source-stage amounts,\
    \ not additive whole-medium rates. Calcium is 0.10 g in the basal batch and 0.10\
    \ g in the stock; iron is 0.04 g basal and 0.10 g stock. The target calcium 0.2\
    \ and every layer iron 0.14 combine stages incorrectly. Owners collapsed calcium\
    \ to 0.1 but still omit its stock input. Reconstruct both stages and the stock\
    \ dose without inventing final-litre values.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"subject\": \"Cresol selected base branch\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    MILLIMOLAR\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"MILLIMOLAR\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"MILLIMOLAR\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Cresol\
    \ or phenol'\",\n        \"exact_source_quote\": \"Cresol or phenol          \
    \                                  1.00   mM*\",\n        \"snapshot_sha256\"\
    : \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\",\n    \
    \    \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary explicitly states 1.00 mM\
    \ for either selected substrate. This supports the base cresol branch value/unit,\
    \ but no matching attached claim is present. Do not turn the provider 0.32 g/L\
    \ display or three SEED isomers into a different substrate dose.\"\n  },\n  {\n\
    \    \"decision_id\": \"q9\",\n    \"subject\": \"Phenol owner still stores cresol\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"MILLIMOLAR\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].preferred_term\",\n        \"stored\"\
    : \"Cresol\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Cresol\
    \ or phenol'\",\n        \"exact_source_quote\": \"Cresol or phenol          \
    \                                  1.00   mM*\",\n        \"snapshot_sha256\"\
    : \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\",\n    \
    \    \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      },\n      {\n        \"source_key\": \"komodoDetail738_replace_Cresol_with_Phenol\"\
    ,\n        \"source_url\": \"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=738_replace_Cresol_with_Phenol\"\
    ,\n        \"source_locator\": \"Metabolites list, exact Phenol row\",\n     \
    \   \"exact_source_quote\": \"Phenol\\nphenol-solution\\nphenol-solution#\\nnull\\\
    nnull\",\n        \"snapshot_sha256\": \"b635e7cb24c4f816fcc36fd99199ea7a68c642ce7e38a856cc351fa5d6cf9642\"\
    ,\n        \"parsed_text_sha256\": \"d769d7e1ab8280af6d696a35c4371f6de1400cf927bea2f743fe76705fb8dc56\"\
    \n      }\n    ],\n    \"rationale\": \"The named phenol-replacement source has\
    \ phenol, not cresol. Restore the supported phenol branch after identity reconciliation.\
    \ The primary offers 1 mM phenol; null provider cells supply no numeric amount\
    \ and must not be treated as zero or copied cresol.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"subject\": \"Vitamin-stock Biotin\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Biotin\",\n        \"exact_source_quote\": \"Biotin 2.00 mg\"\
    ,\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Vitamin-stock Folic\
    \ acid\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Folic acid\",\n        \"exact_source_quote\": \"Folic acid 2.00\
    \ mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\": \"Vitamin-stock Pyridoxine\
    \ hydrochloride\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Pyridoxine hydrochloride\",\n        \"exact_source_quote\":\
    \ \"Pyridoxine hydrochloride 10.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Vitamin-stock Thiamine\
    \ HCl\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Thiamine HCl\",\n        \"exact_source_quote\": \"Thiamine HCl\
    \ 5.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\": \"Vitamin-stock Riboflavin\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Riboflavin\",\n        \"exact_source_quote\": \"Riboflavin 5.00\
    \ mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"subject\": \"Vitamin-stock Nicotinic\
    \ acid\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Nicotinic acid\",\n        \"exact_source_quote\": \"Nicotinic\
    \ acid 5.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"subject\": \"Vitamin-stock Calcium\
    \ D-(+)-pantothenate\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Calcium D-(+)-pantothenate\",\n        \"exact_source_quote\"\
    : \"Calcium D-(+)-pantothenate 5.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q17\",\n    \"subject\": \"Vitamin-stock Vitamin\
    \ B12\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0001\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing Vitamin B12\",\n        \"exact_source_quote\": \"Vitamin B12\
    \ 0.10 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"subject\": \"Vitamin-stock p-Aminobenzoic\
    \ acid\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing p-Aminobenzoic acid\",\n        \"exact_source_quote\": \"p-Aminobenzoic\
    \ acid 5.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q19\",\n    \"subject\": \"Vitamin-stock (DL)-alpha-Lipoic\
    \ acid\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact\
    \ row containing (DL)-alpha-Lipoic acid\",\n        \"exact_source_quote\": \"\
    (DL)-alpha-Lipoic acid 5.00 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a mass in the separate Wolin vitamin\
    \ stock batch, with the displayed mg converted to g only arithmetically. It is\
    \ not a direct main-medium G_PER_L amount. Preserve its stock stage and the separate\
    \ 10 ml receiving-batch dose; listed stock water is not a measured final litre.\"\
    \n  },\n  {\n    \"decision_id\": \"q20\",\n    \"subject\": \"Mineral-stock Nitrilotriacetic\
    \ acid\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing Nitrilotriacetic acid\",\n        \"exact_source_quote\"\
    : \"Nitrilotriacetic acid 1.50 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"subject\": \"Mineral-stock\
    \ MgSO4 x 7 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing MgSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 3.00 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"subject\": \"Mineral-stock\
    \ MnSO4 x H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing MnSO4 x H2O\",\n        \"exact_source_quote\": \"\
    MnSO4 x H2O 0.50 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"subject\": \"Mineral-stock\
    \ NaCl\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing NaCl\",\n        \"exact_source_quote\": \"NaCl 1.00\
    \ g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"subject\": \"Mineral-stock\
    \ CoSO4 x 7 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing CoSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"CoSO4 x 7 H2O 0.18 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"subject\": \"Mineral-stock\
    \ ZnSO4 x 7 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing ZnSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 7 H2O 0.18 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"subject\": \"Mineral-stock\
    \ CuSO4 x 5 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing CuSO4 x 5 H2O\",\n        \"exact_source_quote\"\
    : \"CuSO4 x 5 H2O 0.01 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"subject\": \"Mineral-stock\
    \ AlK(SO4)2 x 12 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing AlK(SO4)2 x 12 H2O\",\n        \"exact_source_quote\"\
    : \"AlK(SO4)2 x 12 H2O 0.02 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"subject\": \"Mineral-stock\
    \ H3BO3\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing H3BO3\",\n        \"exact_source_quote\": \"H3BO3\
    \ 0.01 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"subject\": \"Mineral-stock\
    \ Na2MoO4 x 2 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing Na2MoO4 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 0.01 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"subject\": \"Mineral-stock\
    \ NiCl2 x 6 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing NiCl2 x 6 H2O\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.03 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"subject\": \"Mineral-stock\
    \ Na2SeO3 x 5 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing Na2SeO3 x 5 H2O\",\n        \"exact_source_quote\"\
    : \"Na2SeO3 x 5 H2O 0.30 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"subject\": \"Mineral-stock\
    \ Na2WO4 x 2 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing Na2WO4 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"Na2WO4 x 2 H2O 0.40 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary supports a separate mineral-stock\
    \ batch mass, not the flattened main G_PER_L value. Preserve exact hydrate/form\
    \ and original mass unit; 0.30 mg selenite and 0.40 mg tungstate are 0.0003 g\
    \ and 0.0004 g in that stock batch. No stock or receiving final-volume basis is\
    \ inferred.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"subject\": \"Vitamin\
    \ stock 10 ml batch dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz738\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Vitamin\
    \ solution'\",\n        \"exact_source_quote\": \"Vitamin solution (see medium\
    \ 141)                          10.00    ml\",\n        \"snapshot_sha256\": \"\
    b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\",\n        \"\
    parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"Add this exact source batch input at its\
    \ named stage. The table does not print ml/L for the two stock doses; the listed\
    \ 1000 ml main water does not establish measured final volume.\"\n  },\n  {\n\
    \    \"decision_id\": \"q34\",\n    \"subject\": \"Mineral stock 10 ml batch dose\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz738\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Trace\
    \ element solution'\",\n        \"exact_source_quote\": \"Trace element solution\
    \ (see medium 141)                    10.00    ml\",\n        \"snapshot_sha256\"\
    : \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\",\n    \
    \    \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"Add this exact source batch input at its\
    \ named stage. The table does not print ml/L for the two stock doses; the listed\
    \ 1000 ml main water does not establish measured final volume.\"\n  },\n  {\n\
    \    \"decision_id\": \"q35\",\n    \"subject\": \"Main water 1000 ml\",\n   \
    \ \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\": \"ingredients\"\
    ,\n        \"stored\": [\n          {\n            \"preferred_term\": \"NH4Cl\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:31206\",\n         \
    \     \"label\": \"ammonium chloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium chloride\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2HPO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91258\"\
    ,\n              \"label\": \"disodium hydrogenphosphate dihydrate\"\n       \
    \     },\n            \"concentration\": {\n              \"value\": \"0.42\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91258\",\n              \"label\": \"disodium\
    \ hydrogenphosphate dihydrate\"\n            }\n          },\n          {\n  \
    \          \"preferred_term\": \"Na2HPO4 x H2O\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:86345\",\n              \"label\": \"magnesium dichloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.2\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \" [Merged 2 duplicates: 0.1, 0.1]\",\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86158\",\n\
    \              \"label\": \"calcium chloride dihydrate\"\n            }\n    \
    \      },\n          {\n            \"preferred_term\": \"KCl\",\n           \
    \ \"term\": {\n              \"id\": \"CHEBI:32588\",\n              \"label\"\
    : \"potassium chloride\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"FeSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\",\n\
    \              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.14\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \" [Merged\
    \ 2 duplicates: 0.04, 0.1]\",\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"Cresol\",\n            \"concentration\": {\n      \
    \        \"value\": \"1\",\n              \"unit\": \"MILLIMOLAR\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Biotin\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:15956\",\n           \
    \   \"label\": \"biotin\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"Folic acid\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:27470\",\n         \
    \     \"label\": \"folic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:27470\",\n              \"label\": \"folic acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Pyridoxine\
    \ hydrochloride\",\n            \"term\": {\n              \"id\": \"CHEBI:30961\"\
    ,\n              \"label\": \"pyridoxine hydrochloride\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:30961\",\n              \"label\": \"pyridoxine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Thiamine HCl\",\n            \"term\": {\n              \"id\": \"CHEBI:49105\"\
    ,\n              \"label\": \"thiamine hydrochloride\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"0.005\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49105\",\n              \"label\": \"thiamine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Riboflavin\",\n            \"term\": {\n              \"id\": \"CHEBI:17015\"\
    ,\n              \"label\": \"riboflavin\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17015\",\n              \"label\": \"riboflavin\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Nicotinic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:15940\",\n \
    \             \"label\": \"nicotinic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15940\",\n              \"label\": \"nicotinic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calcium D-(+)-pantothenate\",\n            \"concentration\": {\n            \
    \  \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"CHEBI:31345\",\n           \
    \   \"label\": \"Calcium pantothenate\"\n            }\n          },\n       \
    \   {\n            \"preferred_term\": \"Vitamin B12\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:176843\",\n              \"label\": \"vitamin\
    \ B12\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"0.0001\",\n              \"unit\": \"G_PER_L\"\n            },\n         \
    \   \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:176843\"\
    ,\n              \"label\": \"vitamin B12\"\n            }\n          },\n   \
    \       {\n            \"preferred_term\": \"p-Aminobenzoic acid\",\n        \
    \    \"term\": {\n              \"id\": \"CHEBI:30753\",\n              \"label\"\
    : \"4-aminobenzoic acid\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:30753\",\n              \"label\": \"4-aminobenzoic acid\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    (DL)-alpha-Lipoic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:16494\"\
    ,\n              \"label\": \"lipoic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:16494\",\n              \"label\": \"lipoic acid\"\n   \
    \         }\n          },\n          {\n            \"preferred_term\": \"Nitrilotriacetic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:44557\",\n \
    \             \"label\": \"nitrilotriacetic acid\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"1.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:44557\",\n              \"label\": \"nitrilotriacetic\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate\
    \ monohydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.5\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"NaCl\",\n \
    \           \"term\": {\n              \"id\": \"CHEBI:26710\",\n            \
    \  \"label\": \"sodium chloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\n \
    \           }\n          },\n          {\n            \"preferred_term\": \"CoSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91244\",\n\
    \              \"label\": \"cobalt(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.18\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91244\",\n              \"label\": \"cobalt(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"ZnSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CuSO4 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31440\"\
    ,\n              \"label\": \"copper(II) sulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.01\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31440\",\n              \"label\": \"copper(II)\
    \ sulfate pentahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"AlK(SO4)2 x 12 H2O\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium\
    \ sulfate dodecahydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.02\",\n              \"unit\": \"G_PER_L\"\n   \
    \         },\n            \"mediaingredientmech_chebi_term\": {\n            \
    \  \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium sulfate\
    \ dodecahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"H3BO3\",\n            \"term\": {\n              \"id\": \"CHEBI:33118\",\n\
    \              \"label\": \"boric acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.01\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Na2MoO4\
    \ x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\",\n\
    \              \"label\": \"sodium molybdate dihydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n         \
    \     \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.03\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel\
    \ dichloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SeO3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:131361\"\
    ,\n              \"label\": \"disodium selenite pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0003\",\n    \
    \          \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131361\",\n              \"label\": \"disodium\
    \ selenite pentahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"Na2WO4 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:63939\",\n              \"label\": \"sodium tungstate\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.0004\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63939\"\
    ,\n              \"label\": \"sodium tungstate dihydrate\"\n            }\n  \
    \        }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2HPO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91258\"\
    ,\n              \"label\": \"disodium hydrogenphosphate dihydrate\"\n       \
    \     },\n            \"concentration\": {\n              \"value\": \"0.42\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91258\",\n              \"label\": \"disodium\
    \ hydrogenphosphate dihydrate\"\n            }\n          },\n          {\n  \
    \          \"preferred_term\": \"Na2HPO4 x H2O\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:86345\",\n              \"label\": \"magnesium dichloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \"[Collapsed 2 identical duplicates: 0.1, 0.1]\",\n  \
    \          \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            }\n  \
    \        },\n          {\n            \"preferred_term\": \"KCl\",\n         \
    \   \"term\": {\n              \"id\": \"CHEBI:32588\",\n              \"label\"\
    : \"potassium chloride\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"FeSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\",\n\
    \              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.14\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \" [Merged\
    \ 2 duplicates: 0.04, 0.1]\",\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"Cresol\",\n            \"concentration\": {\n      \
    \        \"value\": \"1\",\n              \"unit\": \"MILLIMOLAR\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Biotin\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:15956\",\n           \
    \   \"label\": \"biotin\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"Folic acid\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:27470\",\n         \
    \     \"label\": \"folic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:27470\",\n              \"label\": \"folic acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Pyridoxine\
    \ hydrochloride\",\n            \"term\": {\n              \"id\": \"CHEBI:30961\"\
    ,\n              \"label\": \"pyridoxine hydrochloride\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:30961\",\n              \"label\": \"pyridoxine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Thiamine HCl\",\n            \"term\": {\n              \"id\": \"CHEBI:49105\"\
    ,\n              \"label\": \"thiamine hydrochloride\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"0.005\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49105\",\n              \"label\": \"thiamine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Riboflavin\",\n            \"term\": {\n              \"id\": \"CHEBI:17015\"\
    ,\n              \"label\": \"riboflavin\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17015\",\n              \"label\": \"riboflavin\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Nicotinic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:15940\",\n \
    \             \"label\": \"nicotinic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15940\",\n              \"label\": \"nicotinic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calcium D-(+)-pantothenate\",\n            \"concentration\": {\n            \
    \  \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"CHEBI:31345\",\n           \
    \   \"label\": \"Calcium pantothenate\"\n            }\n          },\n       \
    \   {\n            \"preferred_term\": \"Vitamin B12\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:176843\",\n              \"label\": \"vitamin\
    \ B12\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"0.0001\",\n              \"unit\": \"G_PER_L\"\n            },\n         \
    \   \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:176843\"\
    ,\n              \"label\": \"vitamin B12\"\n            }\n          },\n   \
    \       {\n            \"preferred_term\": \"p-Aminobenzoic acid\",\n        \
    \    \"term\": {\n              \"id\": \"CHEBI:30753\",\n              \"label\"\
    : \"4-aminobenzoic acid\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:30753\",\n              \"label\": \"4-aminobenzoic acid\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    (DL)-alpha-Lipoic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:16494\"\
    ,\n              \"label\": \"lipoic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:16494\",\n              \"label\": \"lipoic acid\"\n   \
    \         }\n          },\n          {\n            \"preferred_term\": \"Nitrilotriacetic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:44557\",\n \
    \             \"label\": \"nitrilotriacetic acid\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"1.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:44557\",\n              \"label\": \"nitrilotriacetic\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate\
    \ monohydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.5\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"NaCl\",\n \
    \           \"term\": {\n              \"id\": \"CHEBI:26710\",\n            \
    \  \"label\": \"sodium chloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\n \
    \           }\n          },\n          {\n            \"preferred_term\": \"CoSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91244\",\n\
    \              \"label\": \"cobalt(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.18\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91244\",\n              \"label\": \"cobalt(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"ZnSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CuSO4 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31440\"\
    ,\n              \"label\": \"copper(II) sulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.01\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31440\",\n              \"label\": \"copper(II)\
    \ sulfate pentahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"AlK(SO4)2 x 12 H2O\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium\
    \ sulfate dodecahydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.02\",\n              \"unit\": \"G_PER_L\"\n   \
    \         },\n            \"mediaingredientmech_chebi_term\": {\n            \
    \  \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium sulfate\
    \ dodecahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"H3BO3\",\n            \"term\": {\n              \"id\": \"CHEBI:33118\",\n\
    \              \"label\": \"boric acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.01\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Na2MoO4\
    \ x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\",\n\
    \              \"label\": \"sodium molybdate dihydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n         \
    \     \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.03\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel\
    \ dichloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SeO3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:131361\"\
    ,\n              \"label\": \"disodium selenite pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0003\",\n    \
    \          \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131361\",\n              \"label\": \"disodium\
    \ selenite pentahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"Na2WO4 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:63939\",\n              \"label\": \"sodium tungstate\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.0004\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63939\"\
    ,\n              \"label\": \"sodium tungstate dihydrate\"\n            }\n  \
    \        }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2HPO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91258\"\
    ,\n              \"label\": \"disodium hydrogenphosphate dihydrate\"\n       \
    \     },\n            \"concentration\": {\n              \"value\": \"0.42\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91258\",\n              \"label\": \"disodium\
    \ hydrogenphosphate dihydrate\"\n            }\n          },\n          {\n  \
    \          \"preferred_term\": \"Na2HPO4 x H2O\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:86345\",\n              \"label\": \"magnesium dichloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \"[Collapsed 2 identical duplicates: 0.1, 0.1]\",\n  \
    \          \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            }\n  \
    \        },\n          {\n            \"preferred_term\": \"KCl\",\n         \
    \   \"term\": {\n              \"id\": \"CHEBI:32588\",\n              \"label\"\
    : \"potassium chloride\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"FeSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\",\n\
    \              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.14\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \" [Merged\
    \ 2 duplicates: 0.04, 0.1]\",\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"Cresol\",\n            \"concentration\": {\n      \
    \        \"value\": \"1\",\n              \"unit\": \"MILLIMOLAR\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Biotin\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:15956\",\n           \
    \   \"label\": \"biotin\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"Folic acid\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:27470\",\n         \
    \     \"label\": \"folic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:27470\",\n              \"label\": \"folic acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Pyridoxine\
    \ hydrochloride\",\n            \"term\": {\n              \"id\": \"CHEBI:30961\"\
    ,\n              \"label\": \"pyridoxine hydrochloride\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:30961\",\n              \"label\": \"pyridoxine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Thiamine HCl\",\n            \"term\": {\n              \"id\": \"CHEBI:49105\"\
    ,\n              \"label\": \"thiamine hydrochloride\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"0.005\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49105\",\n              \"label\": \"thiamine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Riboflavin\",\n            \"term\": {\n              \"id\": \"CHEBI:17015\"\
    ,\n              \"label\": \"riboflavin\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17015\",\n              \"label\": \"riboflavin\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Nicotinic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:15940\",\n \
    \             \"label\": \"nicotinic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15940\",\n              \"label\": \"nicotinic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calcium D-(+)-pantothenate\",\n            \"concentration\": {\n            \
    \  \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"CHEBI:31345\",\n           \
    \   \"label\": \"Calcium pantothenate\"\n            }\n          },\n       \
    \   {\n            \"preferred_term\": \"Vitamin B12\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:176843\",\n              \"label\": \"vitamin\
    \ B12\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"0.0001\",\n              \"unit\": \"G_PER_L\"\n            },\n         \
    \   \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:176843\"\
    ,\n              \"label\": \"vitamin B12\"\n            }\n          },\n   \
    \       {\n            \"preferred_term\": \"p-Aminobenzoic acid\",\n        \
    \    \"term\": {\n              \"id\": \"CHEBI:30753\",\n              \"label\"\
    : \"4-aminobenzoic acid\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:30753\",\n              \"label\": \"4-aminobenzoic acid\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    (DL)-alpha-Lipoic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:16494\"\
    ,\n              \"label\": \"lipoic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:16494\",\n              \"label\": \"lipoic acid\"\n   \
    \         }\n          },\n          {\n            \"preferred_term\": \"Nitrilotriacetic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:44557\",\n \
    \             \"label\": \"nitrilotriacetic acid\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"1.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:44557\",\n              \"label\": \"nitrilotriacetic\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate\
    \ monohydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.5\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"NaCl\",\n \
    \           \"term\": {\n              \"id\": \"CHEBI:26710\",\n            \
    \  \"label\": \"sodium chloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\n \
    \           }\n          },\n          {\n            \"preferred_term\": \"CoSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91244\",\n\
    \              \"label\": \"cobalt(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.18\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91244\",\n              \"label\": \"cobalt(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"ZnSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CuSO4 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31440\"\
    ,\n              \"label\": \"copper(II) sulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.01\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31440\",\n              \"label\": \"copper(II)\
    \ sulfate pentahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"AlK(SO4)2 x 12 H2O\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium\
    \ sulfate dodecahydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.02\",\n              \"unit\": \"G_PER_L\"\n   \
    \         },\n            \"mediaingredientmech_chebi_term\": {\n            \
    \  \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium sulfate\
    \ dodecahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"H3BO3\",\n            \"term\": {\n              \"id\": \"CHEBI:33118\",\n\
    \              \"label\": \"boric acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.01\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Na2MoO4\
    \ x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\",\n\
    \              \"label\": \"sodium molybdate dihydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n         \
    \     \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.03\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel\
    \ dichloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SeO3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:131361\"\
    ,\n              \"label\": \"disodium selenite pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0003\",\n    \
    \          \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131361\",\n              \"label\": \"disodium\
    \ selenite pentahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"Na2WO4 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:63939\",\n              \"label\": \"sodium tungstate\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.0004\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63939\"\
    ,\n              \"label\": \"sodium tungstate dihydrate\"\n            }\n  \
    \        }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2HPO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91258\"\
    ,\n              \"label\": \"disodium hydrogenphosphate dihydrate\"\n       \
    \     },\n            \"concentration\": {\n              \"value\": \"0.42\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91258\",\n              \"label\": \"disodium\
    \ hydrogenphosphate dihydrate\"\n            }\n          },\n          {\n  \
    \          \"preferred_term\": \"Na2HPO4 x H2O\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium hydrogenphosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34683\",\n              \"label\": \"disodium\
    \ hydrogenphosphate\"\n            }\n          },\n          {\n            \"\
    preferred_term\": \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:86345\",\n              \"label\": \"magnesium dichloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"CaCl2 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium chloride\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \"[Collapsed 2 identical duplicates: 0.1, 0.1]\",\n  \
    \          \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            }\n  \
    \        },\n          {\n            \"preferred_term\": \"KCl\",\n         \
    \   \"term\": {\n              \"id\": \"CHEBI:32588\",\n              \"label\"\
    : \"potassium chloride\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.1\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"FeSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\",\n\
    \              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.14\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \" [Merged\
    \ 2 duplicates: 0.04, 0.1]\",\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"Cresol\",\n            \"concentration\": {\n      \
    \        \"value\": \"1\",\n              \"unit\": \"MILLIMOLAR\"\n         \
    \   }\n          },\n          {\n            \"preferred_term\": \"Biotin\",\n\
    \            \"term\": {\n              \"id\": \"CHEBI:15956\",\n           \
    \   \"label\": \"biotin\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:15956\",\n              \"label\": \"biotin\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"Folic acid\"\
    ,\n            \"term\": {\n              \"id\": \"CHEBI:27470\",\n         \
    \     \"label\": \"folic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:27470\",\n              \"label\": \"folic acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Pyridoxine\
    \ hydrochloride\",\n            \"term\": {\n              \"id\": \"CHEBI:30961\"\
    ,\n              \"label\": \"pyridoxine hydrochloride\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:30961\",\n              \"label\": \"pyridoxine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Thiamine HCl\",\n            \"term\": {\n              \"id\": \"CHEBI:49105\"\
    ,\n              \"label\": \"thiamine hydrochloride\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"0.005\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:49105\",\n              \"label\": \"thiamine\
    \ hydrochloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Riboflavin\",\n            \"term\": {\n              \"id\": \"CHEBI:17015\"\
    ,\n              \"label\": \"riboflavin\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17015\",\n              \"label\": \"riboflavin\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Nicotinic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:15940\",\n \
    \             \"label\": \"nicotinic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:15940\",\n              \"label\": \"nicotinic acid\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Calcium D-(+)-pantothenate\",\n            \"concentration\": {\n            \
    \  \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"term\": {\n              \"id\": \"CHEBI:31345\",\n           \
    \   \"label\": \"Calcium pantothenate\"\n            }\n          },\n       \
    \   {\n            \"preferred_term\": \"Vitamin B12\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:176843\",\n              \"label\": \"vitamin\
    \ B12\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"0.0001\",\n              \"unit\": \"G_PER_L\"\n            },\n         \
    \   \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:176843\"\
    ,\n              \"label\": \"vitamin B12\"\n            }\n          },\n   \
    \       {\n            \"preferred_term\": \"p-Aminobenzoic acid\",\n        \
    \    \"term\": {\n              \"id\": \"CHEBI:30753\",\n              \"label\"\
    : \"4-aminobenzoic acid\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:30753\",\n              \"label\": \"4-aminobenzoic acid\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    (DL)-alpha-Lipoic acid\",\n            \"term\": {\n              \"id\": \"CHEBI:16494\"\
    ,\n              \"label\": \"lipoic acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.005\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:16494\",\n              \"label\": \"lipoic acid\"\n   \
    \         }\n          },\n          {\n            \"preferred_term\": \"Nitrilotriacetic\
    \ acid\",\n            \"term\": {\n              \"id\": \"CHEBI:44557\",\n \
    \             \"label\": \"nitrilotriacetic acid\"\n            },\n         \
    \   \"concentration\": {\n              \"value\": \"1.5\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:44557\",\n              \"label\": \"nitrilotriacetic\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate\
    \ monohydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.5\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86364\"\
    ,\n              \"label\": \"manganese(II) sulfate monohydrate\"\n          \
    \  }\n          },\n          {\n            \"preferred_term\": \"NaCl\",\n \
    \           \"term\": {\n              \"id\": \"CHEBI:26710\",\n            \
    \  \"label\": \"sodium chloride\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\n \
    \           }\n          },\n          {\n            \"preferred_term\": \"CoSO4\
    \ x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:91244\",\n\
    \              \"label\": \"cobalt(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.18\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:91244\",\n              \"label\": \"cobalt(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"ZnSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.18\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CuSO4 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31440\"\
    ,\n              \"label\": \"copper(II) sulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.01\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31440\",\n              \"label\": \"copper(II)\
    \ sulfate pentahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"AlK(SO4)2 x 12 H2O\",\n            \"term\": {\n   \
    \           \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium\
    \ sulfate dodecahydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"0.02\",\n              \"unit\": \"G_PER_L\"\n   \
    \         },\n            \"mediaingredientmech_chebi_term\": {\n            \
    \  \"id\": \"CHEBI:86465\",\n              \"label\": \"potassium aluminium sulfate\
    \ dodecahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"H3BO3\",\n            \"term\": {\n              \"id\": \"CHEBI:33118\",\n\
    \              \"label\": \"boric acid\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.01\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n    \
    \        }\n          },\n          {\n            \"preferred_term\": \"Na2MoO4\
    \ x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\",\n\
    \              \"label\": \"sodium molybdate dihydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.01\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n         \
    \     \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.03\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel\
    \ dichloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SeO3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:131361\"\
    ,\n              \"label\": \"disodium selenite pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0003\",\n    \
    \          \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131361\",\n              \"label\": \"disodium\
    \ selenite pentahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"Na2WO4 x 2 H2O\",\n            \"term\": {\n      \
    \        \"id\": \"CHEBI:63939\",\n              \"label\": \"sodium tungstate\
    \ dihydrate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.0004\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63939\"\
    ,\n              \"label\": \"sodium tungstate dihydrate\"\n            }\n  \
    \        }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Distilled\
    \ water'\",\n        \"exact_source_quote\": \"Distilled water               \
    \                           1000.00    ml\",\n        \"snapshot_sha256\": \"\
    b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\",\n        \"\
    parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"Add this exact source batch input at its\
    \ named stage. The table does not print ml/L for the two stock doses; the listed\
    \ 1000 ml main water does not establish measured final volume.\"\n  },\n  {\n\
    \    \"decision_id\": \"q36\",\n    \"subject\": \"Vitamin-stock water\",\n  \
    \  \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz141StockContext\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\",\n    \
    \    \"source_locator\": \"Wolin's vitamin solution (from medium 141); exact row\
    \ containing Distilled water\",\n        \"exact_source_quote\": \"Distilled water\
    \ 1000.00 ml\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve 1000 ml as the separate stock\
    \ water input. Do not import DSM141 main 1013 ml volume or infer stock makeup/final\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"subject\": \"Mineral-stock\
    \ water\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz141StockContext\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin's mineral solution (from medium 141);\
    \ exact row containing Distilled water\",\n        \"exact_source_quote\": \"\
    Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve 1000 ml as the separate stock\
    \ water input. Do not import DSM141 main 1013 ml volume or infer stock makeup/final\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"subject\": \"Explicit\
    \ phenol stock dose per litre\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz738\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing '20 ml/l'\"\
    ,\n        \"exact_source_quote\": \"  (e.g.: 20 ml/l of a 4.7 g/l phenol-solution)\"\
    ,\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The example explicitly states 20 ml/l\
    \ of 4.7 g/l phenol solution. Preserve both dose and stock strength with that\
    \ example scope; arithmetic 0.020 L × 4.7 g/L = 0.094 g per litre belongs outside\
    \ the quote. This does not change the two stock-table 10 ml batch doses into per-litre\
    \ doses.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"subject\": \"Main\
    \ pH 6.5\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n   \
    \     \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz738\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 6.5. Add cresol/phenol\
    \ after autoclaving.\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"Existing main pH 6.5 matches the explicit\
    \ primary endpoint. Add exact current claim linkage; no titrant dose is stated.\"\
    \n  },\n  {\n    \"decision_id\": \"q40\",\n    \"subject\": \"Missing generated/KOMODO\
    \ preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 6.5. Add cresol/phenol\
    \ after autoclaving.\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"Add the exact main preparation sentence,\
    \ keeping substrate addition after autoclaving and no conventional temperature\
    \ or duration.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"subject\": \"\
    DSMZ owner extra preparation clauses\",\n    \"decision\": \"unsupported\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve phosphates separately, Adjust pH to 6.5. Add cresol/phenol and vitamin\
    \ solution after autoclaving.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 6.5. Add cresol/phenol\
    \ after autoclaving.\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The current primary supports pH and post-autoclave\
    \ cresol/phenol only. Its text does not support the local separate-phosphate instruction\
    \ or the additional vitamin timing. Retain provenance of the old text while resolving\
    \ the unsupported additions; excluded DSM141 parent gas/handling is not borrowed.\"\
    \n  },\n  {\n    \"decision_id\": \"q42\",\n    \"subject\": \"DSMZ owner phenol\
    \ example\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"(e.g.: 20 ml/l of a 4.7 g/l phenol-solution)\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz738\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\",\n        \"\
    source_locator\": \"Exact extracted source line containing '20 ml/l'\",\n    \
    \    \"exact_source_quote\": \"  (e.g.: 20 ml/l of a 4.7 g/l phenol-solution)\"\
    ,\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The existing example matches the explicit\
    \ dose and stock strength; add narrow primary linkage.\"\n  },\n  {\n    \"decision_id\"\
    : \"q43\",\n    \"subject\": \"Mineral preparation pH stages\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bphd_medium.yaml\",\n        \"field_path\": \"\
    preparation_steps[2].description\",\n        \"stored\": \"First dissolve nitrilotriacetic\
    \ acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0\
    \ with KOH.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz141StockContext\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin mineral preparation\",\n     \
    \   \"exact_source_quote\": \"First dissolve nitrilotriacetic acid and adjust\
    \ pH to 6.5 with KOH, then add minerals. Adjust\\nfinal to pH 7.0 with KOH.\"\
    ,\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The text is supported for the separate\
    \ mineral stock. Keep its pH 6.5 then 7.0 endpoints and order separate from receiving-medium\
    \ pH 6.5.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"subject\": \"KOH\
    \ titration amounts\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz141StockContext\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing First dissolve nitrilotriacetic acid\",\n       \
    \ \"exact_source_quote\": \"First dissolve nitrilotriacetic acid and adjust pH\
    \ to 6.5 with KOH, then add minerals. Adjust\",\n        \"snapshot_sha256\":\
    \ \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\",\n    \
    \    \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      },\n      {\n        \"source_key\": \"dsmz141StockContext\",\n      \
    \  \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin's mineral solution (from medium\
    \ 141); exact row containing final to pH\",\n        \"exact_source_quote\": \"\
    final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ],\n    \"rationale\": \"The primary specifies pH endpoints using\
    \ KOH but no fixed titrant dose. Do not invent one.\"\n  },\n  {\n    \"decision_id\"\
    : \"q45\",\n    \"subject\": \"Incubation and autoclave temperature/duration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BPHD_Medium.yaml\",\n        \"field_path\"\
    : \"temperature_value\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml\",\n\
    \        \"field_path\": \"temperature_value\",\n        \"stored\": null\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz738\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium738.pdf\"\
    ,\n        \"source_locator\": \"Exact extracted source line containing 'Adjust\
    \ pH'\",\n        \"exact_source_quote\": \"Adjust pH to 6.5. Add cresol/phenol\
    \ after autoclaving.\",\n        \"snapshot_sha256\": \"b4fb6b66c0a9b63cbf962c624342fdab2fa87a1f5da09f286f1586fe5f4519fb\"\
    ,\n        \"parsed_text_sha256\": \"fb371c7acb4bdacafcff8e4da78e8ae67a3fef32ea705036aec11ffcad6e66b5\"\
    \n      }\n    ],\n    \"rationale\": \"The source mentions autoclaving without\
    \ a cycle and gives no incubation temperature. Neither the parent methane-medium\
    \ conditions nor customary cycles establish these missing values.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: bphd-phenol-variant-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Separate the phenol source branch from copied cresol content
  description: The exact phenol-replacement contributor is included in merged_from,
    but its maintained recipe retains Cresol 1 mM. Its current source names Phenol
    with null numeric cells, and DSM738 permits alternative cresol or phenol. The
    generated recipe cannot stand for both distinct choices without explicit variant
    identity.
  target_ids:
  - CultureMech:006387
  field_paths:
  - merged_from
  - ingredients[7]
  evidence_ids:
  - record
  - provider-phenol
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  issue_key: bphd-stock-stage-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore stock boundaries and distinct basal calcium/iron masses
  description: Vitamin and mineral batches are flattened into main rates. The target
    calcium 0.2 and all local iron 0.14 collapse independent basal and stock inputs;
    owner calcium repair removes one duplicate but does not reconstruct the mineral
    stock. Water and 10 ml stock doses are absent.
  target_ids:
  - CultureMech:006387
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - stocks
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  issue_key: bphd-nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel chloride
  description: All four inspected recipe layers name NiCl2 x 6 H2O but use CHEBI:34887
    nickel dichloride in primary and secondary slots. Canonical label success does
    not establish the supplied hydrate.
  target_ids:
  - CultureMech:006387
  field_paths:
  - ingredients[28].term
  - ingredients[28].mediaingredientmech_chebi_term
  evidence_ids:
  - stocks
  - chebi34887
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  issue_key: bphd-preparation-source-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Retain supported preparation and qualify unsupported source extensions
  description: The target loses preparation, while the DSMZ owner adds separate-phosphate
    and post-autoclave vitamin instructions absent from the current main primary.
    Mineral-stock pH preparation is valid only for that stock.
  target_ids:
  - CultureMech:006387
  field_paths:
  - preparation_steps
  evidence_ids:
  - primary
  - stocks
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  issue_key: bphd-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical date precision remains unresolved
  description: Malformed or timezone-absent historical timestamps remain preserved;
    they are not silently converted to exact UTC chronology.
  target_ids:
  - CultureMech:006387
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-full
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  description: Correct the exact phenol owner identity and represent the alternative
    formulation separately. Reassess source-duplicate relationships before authorized
    regeneration using the already conservative current grouping gate.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006387
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  description: Represent separate basal inputs, both complete stocks and their exact
    batch doses. Preserve conditional arithmetic only where source final-volume basis
    is explicit; do not replace unsupported rates with inferred ones.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006387
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  description: Resolve the exact hexahydrate and current secondary mapping from inspected
    ontology evidence; retain ambiguity rather than substitute an unverified identifier.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006387
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  description: Attach exact main and stock preparation evidence at their own stages,
    resolve added clauses and preserve historical text as provenance rather than validated
    current instructions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006387
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
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
  description: Append verified clarification if available while retaining original
    history.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006387
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bphd_medium_replace_cresol_with_phenol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Do not rewrite original timestamps or infer historical execution from current
    code.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The current MediaDive 738 API returned HTTP 503. Current DSMZ main/stock primaries
  and exact KOMODO base/variant pages are usable; no unavailable API response is treated
  as amount authentication.
- The source second-phosphate spelling remains unresolved; no corrected chemical formula
  is invented.
- The exact DSM141 parent record is context only. Its main quantities, gases, pressure,
  strains and final volume do not transfer to BPHD.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-045
- generated-medium
```
