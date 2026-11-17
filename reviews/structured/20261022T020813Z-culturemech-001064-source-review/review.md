# Source and formulation review: bradymonas_sediminis_medium (CultureMech:001064)

- Review: 20261022T020813Z-culturemech-001064-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T02:02:38Z
- Finished UTC: 2026-10-22T02:08:13Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1588 supports a basal solution with a later seawater addition and a choice of aged natural or separately prepared artificial seawater. Both local layers collapse the alternative stock into main ingredients, sum sodium chloride across stages, label water volumes as mass rates, and expose the initial pH as the sole endpoint.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 443; batch 045 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-four task batches contain 440 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 443 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001064 | data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml | generated | bradymonas_sediminis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001064 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001064 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/443/strict.tsv |
| validate-terms | passed | True | CultureMech:001064 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001064 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001064 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1588api | unavailable | False | CultureMech:001064 | The current exact MediaDive 1588 request returned HTTP 503. The complete DSMZ primary is available; no failed provider response is treated as quantity or denominator evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001064.

The four documented recipes completed; interpret the scope of each separately.

### Complete current ontology and secondary linkage inventory

grounding: supported. Targets: CultureMech:001064.

9 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly. 9/9 asserted current secondary keys have exact pinned index rows. Target primary linkage is 9/12 (75.00%) and current secondary linkage is 9/12 (75.00%) on a 0–100 linkage scale, not a correctness score. Current missing keys do not prove historical invalidity; compatible generic source wording does not establish a stereochemical conflict.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001064.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact collection identity and alternative formulation

identity: supported. Targets: CultureMech:001064.

The generated record and its single maintained owner identify DSMZ 1588 and the source title matches. The selected solid-agar state is a supported branch, but the same source permits a liquid branch without agar. The title is collection scope, not a strain-resolved experiment or growth temperature.

### Natural/artificial seawater boundaries

quantity: concern. Targets: CultureMech:001064.

Solution A contains 5 g NaCl, 250 ml tap water and other basal inputs. A later 750 ml seawater addition uses aged natural seawater, or the separately described artificial-seawater preparation when natural water is unavailable. The local 33.129999999999995 g/L NaCl sums the basal 5 g and the full stock 28.13 g; other artificial-stock masses are also promoted directly into main rates while natural seawater remains present.

### Preserved procedure and structured pH ambiguity

representation: concern. Targets: CultureMech:001064.

The two local preparation descriptions preserve most source instructions: pH 7.8 before a 10-minute boil, readjustment to 7.3, 121°C for 20 minutes, then 55°C sterile seawater for the agar branch; liquid medium is mixed after cooling to room temperature. Natural seawater ages in darkness for at least three weeks. The isolated ph_value 7.8 does not convey the later adjustment; neither endpoint is claimed as a measured final pH after seawater addition.

### Asserted forms versus complex materials

grounding: supported. Targets: CultureMech:001064.

Named inorganic hydrate identities are compatible with the primary, and the D(+)-trehalose name is not a supported ontology mismatch. Peptone, meat/beef extract and natural seawater remain complex materials. Water CHEBI:15377 identifies the solvent, not the mineral composition of tap or natural seawater. No supplier formulation or sea-water chemistry is inferred.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001064.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Peptone basal input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Solution A exact row Peptone",
        "exact_source_quote": " Peptone                                                           10.0        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The primary gives the matching nominal batch mass, not a measured final-litre concentration. Agar 19 g is conditional on the solid branch. Preserve the mass and stage without inferring a final medium volume."
  },
  {
    "decision_id": "q2",
    "subject": "Meat extract basal input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Solution A exact row Meat extract",
        "exact_source_quote": " Meat extract                                                       3.0        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The primary gives the matching nominal batch mass, not a measured final-litre concentration. Agar 19 g is conditional on the solid branch. Preserve the mass and stage without inferring a final medium volume."
  },
  {
    "decision_id": "q3",
    "subject": "D(+)-Trehalose basal input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Solution A exact row D(+)-Trehalose",
        "exact_source_quote": " D(+)-Trehalose                                                     1.0        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The primary gives the matching nominal batch mass, not a measured final-litre concentration. Agar 19 g is conditional on the solid branch. Preserve the mass and stage without inferring a final medium volume."
  },
  {
    "decision_id": "q4",
    "subject": "Agar basal input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "19",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "19",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Solution A exact row Agar if appropriate",
        "exact_source_quote": " Agar if appropriate                                               19.0        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The primary gives the matching nominal batch mass, not a measured final-litre concentration. Agar 19 g is conditional on the solid branch. Preserve the mass and stage without inferring a final medium volume."
  },
  {
    "decision_id": "q5",
    "subject": "Sodium chloride across two stages",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "33.129999999999995",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "33.129999999999995",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Solution A exact row NaCl",
        "exact_source_quote": " NaCl                                                               5.0        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      },
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row NaCl",
        "exact_source_quote": " NaCl                                                             28.13        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The main 5 g and separate stock 28.13 g must not be added directly as 33.13 g/L. The artificial stock supplies the 750 ml alternative dose, not its full listed batch. Even nominal 0.75 scaling is conditional on a stock volume basis; the listed stock water alone is not a measured final-volume statement."
  },
  {
    "decision_id": "q6",
    "subject": "Tap water batch volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "250",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "250",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Main input exact row Tap water",
        "exact_source_quote": " Tap water                                                        250.0       ml",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The source unit is ml: 250 ml tap water or the separate later 750 ml seawater addition, not G_PER_L. Preserve the exact volume and stage. A sum of these liquid inputs is not a measured final-volume declaration."
  },
  {
    "decision_id": "q7",
    "subject": "Natural sea water batch volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "750",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "750",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Main input exact row Sea water*",
        "exact_source_quote": "Sea water*                                                        750.0       ml",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The source unit is ml: 250 ml tap water or the separate later 750 ml seawater addition, not G_PER_L. Preserve the exact volume and stage. A sum of these liquid inputs is not a measured final-volume declaration."
  },
  {
    "decision_id": "q8",
    "subject": "Artificial-seawater stock KCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.77",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.77",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row KCl",
        "exact_source_quote": " KCl                                                               0.77        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "This mass belongs to the separately prepared artificial-seawater stock, only used as the natural-seawater alternative. It is neither a direct receiving-medium mass nor an independently supported final G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without assuming stock final volume."
  },
  {
    "decision_id": "q9",
    "subject": "Artificial-seawater stock CaCl2 x 2 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row CaCl2",
        "exact_source_quote": " CaCl2 x 2 H2O                                                     1.60        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "This mass belongs to the separately prepared artificial-seawater stock, only used as the natural-seawater alternative. It is neither a direct receiving-medium mass nor an independently supported final G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without assuming stock final volume."
  },
  {
    "decision_id": "q10",
    "subject": "Artificial-seawater stock MgCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row MgCl2",
        "exact_source_quote": " MgCl2 x 6 H2O                                                     4.80        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "This mass belongs to the separately prepared artificial-seawater stock, only used as the natural-seawater alternative. It is neither a direct receiving-medium mass nor an independently supported final G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without assuming stock final volume."
  },
  {
    "decision_id": "q11",
    "subject": "Artificial-seawater stock NaHCO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.11",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.11",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row NaHCO3",
        "exact_source_quote": " NaHCO3                                                            0.11        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "This mass belongs to the separately prepared artificial-seawater stock, only used as the natural-seawater alternative. It is neither a direct receiving-medium mass nor an independently supported final G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without assuming stock final volume."
  },
  {
    "decision_id": "q12",
    "subject": "Artificial-seawater stock MgSO4 x 7 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "3.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "3.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row MgSO4",
        "exact_source_quote": " MgSO4 x 7 H2O                                                     3.50        g",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "This mass belongs to the separately prepared artificial-seawater stock, only used as the natural-seawater alternative. It is neither a direct receiving-medium mass nor an independently supported final G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without assuming stock final volume."
  },
  {
    "decision_id": "q13",
    "subject": "Artificial stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Artificial seawater exact row Distilled water",
        "exact_source_quote": " Distilled water                                                 1000.0       ml",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "Add the separate 1000 ml distilled-water stock input. Do not mix it with the 250 ml basal water or promote it to the receiving denominator."
  },
  {
    "decision_id": "q14",
    "subject": "Initial and later pH endpoints",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.8
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.8
      },
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Main preparation pH and boil sequence",
        "exact_source_quote": "adjust pH to 7.8 and boil for\n10 min. Readjust pH to 7.3.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "Keep 7.8 explicitly as the initial pre-boil endpoint and 7.3 as the subsequent adjustment. Correct the unqualified single pH representation or associate it with its stage; the source does not measure final pH after seawater addition."
  },
  {
    "decision_id": "q15",
    "subject": "Ten-minute boil",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Main basal boiling duration",
        "exact_source_quote": "adjust pH to 7.8 and boil for\n10 min.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The existing preparation contains the source ten-minute boil at this stage. Attach exact support; this is not the autoclave duration."
  },
  {
    "decision_id": "q16",
    "subject": "Autoclave 121 degrees C for 20 minutes",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Primary PDF extracted cycle, exact glyph retained",
        "exact_source_quote": "Add agar and autoclave at 121C for 20 min.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The local normalized Celsius glyph represents the explicitly printed 121°C, 20-minute cycle. It applies to the basal agar preparation, not the sterile seawater or an organism incubation."
  },
  {
    "decision_id": "q17",
    "subject": "Warm sterile seawater at 55 degrees C",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Post-autoclave agar branch addition",
        "exact_source_quote": "autoclaving, add warm (55C) sterile sea water.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The existing 55°C addition is explicit for the agar branch. Preserve that addition stage and do not label it growth temperature."
  },
  {
    "decision_id": "q18",
    "subject": "Liquid branch room-temperature mixing",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8 and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid medium without agar should be combined when cooled to room temperature."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Liquid alternative after cooling",
        "exact_source_quote": "Liquid medium without agar should be\ncombined when cooled to room temperature.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The qualitative room-temperature condition is explicit. Do not assign an invented numeric temperature or make agar mandatory."
  },
  {
    "decision_id": "q19",
    "subject": "Natural seawater aging",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Natural sea water is stored in the dark for at least three weeks to \"age\". If natural sea water is not available use artificial sea water:"
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Natural sea water is stored in the dark for at least three weeks to \"age\". If natural sea water is not available use artificial sea water:"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Natural-seawater preparation, minimum duration",
        "exact_source_quote": "Natural sea water is stored in the dark for at least three weeks to \"age\".",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The existing instruction correctly retains darkness and a minimum three-week aging duration. It applies to natural seawater; artificial seawater is the stated alternative."
  },
  {
    "decision_id": "q20",
    "subject": "Titrant amount",
    "decision": "not_quantified",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Main pH readjustment",
        "exact_source_quote": "Readjust pH to 7.3.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "The source supplies endpoints but no titrant identity or fixed dose. No amount is invented."
  },
  {
    "decision_id": "q21",
    "subject": "Incubation temperature",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1588",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf",
        "source_locator": "Preparation temperature scope",
        "exact_source_quote": "Liquid medium without agar should be\ncombined when cooled to room temperature.",
        "snapshot_sha256": "fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2",
        "parsed_text_sha256": "39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009"
      }
    ],
    "rationale": "No growth/incubation temperature is supplied; preparation temperatures do not support a generic incubation value."
  }
]

## Findings

### f1: Restore seawater alternatives and separate stock quantities

major / open / confirmed; issue key: bradymonas-seawater-alternative-stages.

The record simultaneously retains natural seawater and all artificial-stock salts, sums basal and full-stock sodium chloride, and loses the 750 ml stock-dose stage. This changes the formulation regardless of any disputed final-volume interpretation.

### f2: Water volumes are stored as mass concentrations

major / open / confirmed; issue key: bradymonas-water-units-and-batch-basis.

Tap water 250 and natural seawater 750 are source millilitres but local G_PER_L values. The remaining listed masses also lack an independently established final-volume denominator.

### f3: Expose the later pH adjustment with its stage

major / open / confirmed; issue key: bradymonas-ph-stage.

The standalone pH field is 7.8 although the preserved procedure next readjusts to 7.3. The initial value cannot serve as an unqualified complete-medium endpoint.

## Recommended Actions And Acceptance Checks

### a1

Rebuild Solution A and a separately scoped seawater choice in the maintained owner. Preserve 5 g basal NaCl, the complete artificial stock and the 750 ml addition without summing the entire stock into the main recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the liquid inputs as batch volumes and retain other source masses at their stages; preserve uncertainty in final volume instead of substituting a guessed litre denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent both source pH stages explicitly and qualify any scalar field according to its documented stage; do not claim a measured final pH after seawater addition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch045/443/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch045/443/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml:1:id: CultureMech:001064<br>./data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml:1:id: CultureMech:001064<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch045/source-preflight-bound/443/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch045/443/grounding-inventory.json; Complete path-qualified sidecar | context_only | Every asserted ingredient primary/secondary/legacy slot in target and exact owners, full OLS scientific properties, current exact index rows and any unverified provider identifiers. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi27082 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27082; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact asserted OLS ID, label, obsolete state and full scientific properties | supports | Current identifier resolves; exact canonical-label differences and scientific properties are retained in the grounding inventory. Source chemical forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact asserted current secondary identifiers in pinned 9077-row label index | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27082": [{"label": "D(+)-Trehalose", "match_type": "synonym", "identifier": "CHEBI:27082", "preferred_term": "Trehalose", "ontology_id": "CHEBI:27082", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "D-Trehalose", "match_type": "synonym", "identifier": "CHEBI:27082", "preferred_term": "Trehalose", "ontology_id": "CHEBI:27082", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Trehalose", "match_type": "preferred_term", "identifier": "CHEBI:27082", "preferred_term": "Trehalose", "ontology_id": "CHEBI:27082", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "[OH2]", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dH2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydridooxygen", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydrogen oxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distiled water", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for liquid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for solid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "eau", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H(2)O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "HOH", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen hydroxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "oxidane", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Wasser", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "WATER", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl (Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS: 7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klor-con", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klotrix", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "muriate of potash", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sylvite", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS: 10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride anhydrous", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl 2", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2  x 76 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "MgCl2 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2.6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "baking soda", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bicarbonate of soda", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "carbonic acid monosodium salt", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E 500", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E-500", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E500", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (1 M)", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (10% (w/v))", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (10%, w/v)", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (3% (w/v))", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (5%, w/v)", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (7.5% w/v in water)", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3(Fisher S 233)", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumhydrogenkarbonat", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium acid carbonate", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Bicarbonate", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium hydrogen carbonate", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium hydrogencarbonate", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "legacy": []} |
| history-metadata | data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml", "events": 6, "timestamp_issues": []}] |
| history-full | /private/tmp/culturemech-review-work-batch045/443/history-inventory.json; Complete path-qualified sidecar | context_only | Full target and maintained-owner history events retained without rewriting malformed or timezone-absent values. |
| historical-inventory | /private/tmp/culturemech-review-work-batch045/443/historical-evidence-inventory.json; Complete path-qualified sidecar | context_only | Exact attached claim objects and decoded historical report joins; a decoded match is not original API-response authentication. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf; Complete DSMZ 1588 formulation, preparation and artificial-seawater subsection | supports | Exact main/stock alternatives and processing stages read. Natural seawater and its artificial substitute are alternatives, not simultaneous inputs. |
| mediadive1588api-attempt | https://mediadive.dsmz.de/rest/medium/1588; Preserved exact public retrieval result | context_only | The current exact MediaDive 1588 request returned HTTP 503. The complete DSMZ primary is available; no failed provider response is treated as quantity or denominator evidence. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current conservative merge gate is distinct from the historical flattened recipe. Correct the exact maintained recipe stages and alternatives before authorized regeneration; do not attribute these bytes to an unproved current merge execution. |
| writer-1 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current conservative merge gate is distinct from the historical flattened recipe. Correct the exact maintained recipe stages and alternatives before authorized regeneration; do not attribute these bytes to an unproved current merge execution. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current conservative merge gate is distinct from the historical flattened recipe. Correct the exact maintained recipe stages and alternatives before authorized regeneration; do not attribute these bytes to an unproved current merge execution. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch045/443/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current exact MediaDive 1588 request returned HTTP 503. The complete DSMZ primary is available; no failed provider response is treated as quantity or denominator evidence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T020813Z-culturemech-001064-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bradymonas_sediminis_medium (CultureMech:001064)'
started_at: '2026-10-22T02:02:38Z'
finished_at: '2026-10-22T02:08:13Z'
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
summary: DSMZ 1588 supports a basal solution with a later seawater addition and a
  choice of aged natural or separately prepared artificial seawater. Both local layers
  collapse the alternative stock into main ingredients, sum sodium chloride across
  stages, label water volumes as mass rates, and expose the initial pH as the sole
  endpoint.
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
  - path: data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
    sha256: ae4878e3deaf95917fd4c74c6220bd31985cd138d230fcf530a5230a3c3d91af
    role: target
  - path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
    sha256: ac40183a0ff98ffe4d07054b8c40db24e8c8b72885aa89aaa6294aa14f0a1a73
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/bradymonas_sediminis_medium.yaml.md
    sha256: 3b6c2a63b8e1cdb0a314369b6263254814effa5454964b16be5d90d03fd4d270
    role: context
  - path: reports/yaml_record_review/20260921T232745Z-BRADYMONAS_SEDIMINIS_MEDIUM.md
    sha256: 9e2697d3188d890290c144e56b394b8008f5490e56168e58372f73be0bf3f963
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
  selection: Task review 443; batch 045 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:001064
targets:
- target_id: CultureMech:001064
  path: data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  label: bradymonas_sediminis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/443/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/443/strict.tsv"
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001064
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
  - CultureMech:001064
- check_id: mediadive1588api-source-access
  name: 'Exact source content access: mediadive1588api'
  required: false
  status: unavailable
  summary: The current exact MediaDive 1588 request returned HTTP 503. The complete
    DSMZ primary is available; no failed provider response is treated as quantity
    or denominator evidence.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - mediadive1588api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:10.524669Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch045/443/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:13.743858Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-045/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch045/443/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:15.675875Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T02:03:16.923947Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T02:08:12Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml:1:id:
    CultureMech:001064

    ./data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml:1:id: CultureMech:001064

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/source-preflight-bound/443/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T02:08:12Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7ceb3159021f7961b1f0befa12f21c646796b663fd9fc493e2a6f6e16f5cd40e
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/443/grounding-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Every asserted ingredient primary/secondary/legacy slot in target and exact
    owners, full OLS scientific properties, current exact index rows and any unverified
    provider identifiers.
  snapshot_sha256: 9706aef88a37ac0e3554b3caf7086f9107ebdf39f763d55f95e9b9ddba8d381a
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
- evidence_id: chebi27082
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27082
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-22T01:49:22.196359Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 8116c1cb0cd1f08abce72007c7e6150d979d0cb5b789e5b417faad9209052b24
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
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
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
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact asserted OLS ID, label, obsolete state and full scientific properties
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: Current identifier resolves; exact canonical-label differences and scientific
    properties are retained in the grounding inventory. Source chemical forms are
    assessed separately.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact asserted current secondary identifiers in pinned 9077-row label index
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710":
    [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid",
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
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27082":
    [{"label": "D(+)-Trehalose", "match_type": "synonym", "identifier": "CHEBI:27082",
    "preferred_term": "Trehalose", "ontology_id": "CHEBI:27082", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "D-Trehalose", "match_type": "synonym",
    "identifier": "CHEBI:27082", "preferred_term": "Trehalose", "ontology_id": "CHEBI:27082",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Trehalose", "match_type":
    "preferred_term", "identifier": "CHEBI:27082", "preferred_term": "Trehalose",
    "ontology_id": "CHEBI:27082", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type":
    "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar
    (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label":
    "[OH2]", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "acqua", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "agua", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aqua", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dH2O",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "dihydridooxygen", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydrogen oxide",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distiled water", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water",
    "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distilled water (for liquid medium)", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled
    water (for solid medium)", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "eau", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H(2)O", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H2O",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "HOH", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen hydroxide", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "oxidane",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Wasser", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "WATER", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term":
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
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
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
    "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86345": [{"label":
    "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type":
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
    "unique"}], "CHEBI:32139": [{"label": "baking soda", "match_type": "synonym",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bicarbonate of
    soda", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "carbonic acid monosodium salt", "match_type": "synonym",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E 500", "match_type":
    "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E-500",
    "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3",
    "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "E500", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaHCO", "match_type": "synonym", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (1 M)", "match_type": "synonym",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (10% (w/v))",
    "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3",
    "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NaHCO3 (10%, w/v)", "match_type": "synonym", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "NaHCO3 (3% (w/v))", "match_type": "synonym",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3 (5%, w/v)",
    "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3",
    "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NaHCO3 (7.5% w/v in water)", "match_type": "synonym", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaHCO3(Fisher S 233)", "match_type":
    "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumhydrogenkarbonat",
    "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3",
    "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sodium acid carbonate", "match_type": "synonym", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium Bicarbonate", "match_type": "synonym",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium hydrogen
    carbonate", "match_type": "synonym", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium hydrogencarbonate", "match_type": "synonym", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
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
    "MAPPED", "ambiguity": "unique"}]}, "legacy": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml; data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: history-full
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/443/history-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Full target and maintained-owner history events retained without rewriting
    malformed or timezone-absent values.
  snapshot_sha256: 9133552ea5524a28af69c7685d083d186b261fd2aa8d3cfe1d47119e2dbf5b88
- evidence_id: historical-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/443/historical-evidence-inventory.json
  locator: Complete path-qualified sidecar
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Exact attached claim objects and decoded historical report joins; a decoded
    match is not original API-response authentication.
  snapshot_sha256: 7fb869508e8c8f7d21d1f259558ed28c98fe03be590c47659c1f217f65b157e0
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf
  locator: Complete DSMZ 1588 formulation, preparation and artificial-seawater subsection
  accessed_at: '2026-10-22T01:49:19.327240Z'
  support: supports
  summary: Exact main/stock alternatives and processing stages read. Natural seawater
    and its artificial substitute are alternatives, not simultaneous inputs.
  quote: 1588. BRADYMONAS SEDIMINIS MEDIUM
  snapshot_sha256: fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2
- evidence_id: mediadive1588api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1588
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T01:49:19.460847Z'
  support: context_only
  summary: The current exact MediaDive 1588 request returned HTTP 503. The complete
    DSMZ primary is available; no failed provider response is treated as quantity
    or denominator evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: The current conservative merge gate is distinct from the historical flattened
    recipe. Correct the exact maintained recipe stages and alternatives before authorized
    regeneration; do not attribute these bytes to an unproved current merge execution.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: The current conservative merge gate is distinct from the historical flattened
    recipe. Correct the exact maintained recipe stages and alternatives before authorized
    regeneration; do not attribute these bytes to an unproved current merge execution.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: The current conservative merge gate is distinct from the historical flattened
    recipe. Correct the exact maintained recipe stages and alternatives before authorized
    regeneration; do not attribute these bytes to an unproved current merge execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch045/443/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T02:08:12Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ff51e859caeadd3c5d688d4081035a326204266f479590e0ea2c731e3226c37f
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete current ontology and secondary linkage inventory
  outcome: supported
  summary: 9 distinct bound ontology IDs resolve and are nonobsolete. 0 literal canonical-label
    mismatches, 0 unverified provider slots and 0 legacy slots are retained explicitly.
    9/9 asserted current secondary keys have exact pinned index rows. Target primary
    linkage is 9/12 (75.00%) and current secondary linkage is 9/12 (75.00%) on a 0–100
    linkage scale, not a correctness score. Current missing keys do not prove historical
    invalidity; compatible generic source wording does not establish a stereochemical
    conflict.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - grounding-inventory
  - mim
  - chebi26710
  - chebi27082
  - chebi2509
  - chebi15377
  - chebi32588
  - chebi86158
  - chebi86345
  - chebi32139
  - chebi31795
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact collection identity and alternative formulation
  outcome: supported
  summary: The generated record and its single maintained owner identify DSMZ 1588
    and the source title matches. The selected solid-agar state is a supported branch,
    but the same source permits a liquid branch without agar. The title is collection
    scope, not a strain-resolved experiment or growth temperature.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - primary
  - record
  - owner-0
- assessment_id: formulation
  area: quantity
  topic: Natural/artificial seawater boundaries
  outcome: concern
  summary: Solution A contains 5 g NaCl, 250 ml tap water and other basal inputs.
    A later 750 ml seawater addition uses aged natural seawater, or the separately
    described artificial-seawater preparation when natural water is unavailable. The
    local 33.129999999999995 g/L NaCl sums the basal 5 g and the full stock 28.13
    g; other artificial-stock masses are also promoted directly into main rates while
    natural seawater remains present.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - primary
  - record
- assessment_id: preparation
  area: representation
  topic: Preserved procedure and structured pH ambiguity
  outcome: concern
  summary: 'The two local preparation descriptions preserve most source instructions:
    pH 7.8 before a 10-minute boil, readjustment to 7.3, 121°C for 20 minutes, then
    55°C sterile seawater for the agar branch; liquid medium is mixed after cooling
    to room temperature. Natural seawater ages in darkness for at least three weeks.
    The isolated ph_value 7.8 does not convey the later adjustment; neither endpoint
    is claimed as a measured final pH after seawater addition.'
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - primary
  - record
  - owner-0
- assessment_id: forms
  area: grounding
  topic: Asserted forms versus complex materials
  outcome: supported
  summary: Named inorganic hydrate identities are compatible with the primary, and
    the D(+)-trehalose name is not a supported ontology mismatch. Peptone, meat/beef
    extract and natural seawater remain complex materials. Water CHEBI:15377 identifies
    the solvent, not the mineral composition of tap or natural seawater. No supplier
    formulation or sea-water chemistry is inferred.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - primary
  - grounding-inventory
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 21 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001064
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Peptone basal\
    \ input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Solution A exact row Peptone\",\n        \"exact_source_quote\"\
    : \" Peptone                                                           10.0  \
    \      g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The primary gives the matching nominal\
    \ batch mass, not a measured final-litre concentration. Agar 19 g is conditional\
    \ on the solid branch. Preserve the mass and stage without inferring a final medium\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\": \"Meat\
    \ extract basal input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Solution A exact row Meat extract\",\n      \
    \  \"exact_source_quote\": \" Meat extract                                   \
    \                    3.0        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The primary gives the matching nominal\
    \ batch mass, not a measured final-litre concentration. Agar 19 g is conditional\
    \ on the solid branch. Preserve the mass and stage without inferring a final medium\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"D(+)-Trehalose\
    \ basal input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Solution A exact row D(+)-Trehalose\",\n    \
    \    \"exact_source_quote\": \" D(+)-Trehalose                               \
    \                      1.0        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The primary gives the matching nominal\
    \ batch mass, not a measured final-litre concentration. Agar 19 g is conditional\
    \ on the solid branch. Preserve the mass and stage without inferring a final medium\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"subject\": \"Agar\
    \ basal input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Solution A exact row Agar if appropriate\",\n\
    \        \"exact_source_quote\": \" Agar if appropriate                      \
    \                         19.0        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The primary gives the matching nominal\
    \ batch mass, not a measured final-litre concentration. Agar 19 g is conditional\
    \ on the solid branch. Preserve the mass and stage without inferring a final medium\
    \ volume.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"subject\": \"Sodium\
    \ chloride across two stages\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"33.129999999999995\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"33.129999999999995\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Solution A exact row NaCl\",\n        \"exact_source_quote\"\
    : \" NaCl                                                               5.0  \
    \      g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1588\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\",\n   \
    \     \"source_locator\": \"Artificial seawater exact row NaCl\",\n        \"\
    exact_source_quote\": \" NaCl                                                \
    \             28.13        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The main 5 g and separate stock 28.13\
    \ g must not be added directly as 33.13 g/L. The artificial stock supplies the\
    \ 750 ml alternative dose, not its full listed batch. Even nominal 0.75 scaling\
    \ is conditional on a stock volume basis; the listed stock water alone is not\
    \ a measured final-volume statement.\"\n  },\n  {\n    \"decision_id\": \"q6\"\
    ,\n    \"subject\": \"Tap water batch volume\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"250\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"250\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Main input exact row Tap water\",\n        \"\
    exact_source_quote\": \" Tap water                                           \
    \             250.0       ml\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The source unit is ml: 250 ml tap water\
    \ or the separate later 750 ml seawater addition, not G_PER_L. Preserve the exact\
    \ volume and stage. A sum of these liquid inputs is not a measured final-volume\
    \ declaration.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"subject\": \"\
    Natural sea water batch volume\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"750\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"750\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Main input exact row Sea water*\",\n        \"\
    exact_source_quote\": \"Sea water*                                           \
    \             750.0       ml\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The source unit is ml: 250 ml tap water\
    \ or the separate later 750 ml seawater addition, not G_PER_L. Preserve the exact\
    \ volume and stage. A sum of these liquid inputs is not a measured final-volume\
    \ declaration.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\": \"\
    Artificial-seawater stock KCl\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.77\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.77\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row KCl\",\n      \
    \  \"exact_source_quote\": \" KCl                                            \
    \                   0.77        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"This mass belongs to the separately prepared\
    \ artificial-seawater stock, only used as the natural-seawater alternative. It\
    \ is neither a direct receiving-medium mass nor an independently supported final\
    \ G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without\
    \ assuming stock final volume.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n  \
    \  \"subject\": \"Artificial-seawater stock CaCl2 x 2 H2O\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row CaCl2\",\n    \
    \    \"exact_source_quote\": \" CaCl2 x 2 H2O                                \
    \                     1.60        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"This mass belongs to the separately prepared\
    \ artificial-seawater stock, only used as the natural-seawater alternative. It\
    \ is neither a direct receiving-medium mass nor an independently supported final\
    \ G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without\
    \ assuming stock final volume.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n \
    \   \"subject\": \"Artificial-seawater stock MgCl2 x 6 H2O\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row MgCl2\",\n    \
    \    \"exact_source_quote\": \" MgCl2 x 6 H2O                                \
    \                     4.80        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"This mass belongs to the separately prepared\
    \ artificial-seawater stock, only used as the natural-seawater alternative. It\
    \ is neither a direct receiving-medium mass nor an independently supported final\
    \ G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without\
    \ assuming stock final volume.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n \
    \   \"subject\": \"Artificial-seawater stock NaHCO3\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row NaHCO3\",\n   \
    \     \"exact_source_quote\": \" NaHCO3                                      \
    \                      0.11        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"This mass belongs to the separately prepared\
    \ artificial-seawater stock, only used as the natural-seawater alternative. It\
    \ is neither a direct receiving-medium mass nor an independently supported final\
    \ G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without\
    \ assuming stock final volume.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n \
    \   \"subject\": \"Artificial-seawater stock MgSO4 x 7 H2O\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row MgSO4\",\n    \
    \    \"exact_source_quote\": \" MgSO4 x 7 H2O                                \
    \                     3.50        g\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"This mass belongs to the separately prepared\
    \ artificial-seawater stock, only used as the natural-seawater alternative. It\
    \ is neither a direct receiving-medium mass nor an independently supported final\
    \ G_PER_L rate. Preserve the source stock batch and 750 ml receiving dose without\
    \ assuming stock final volume.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n \
    \   \"subject\": \"Artificial stock water\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1588\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Artificial seawater exact row Distilled water\"\
    ,\n        \"exact_source_quote\": \" Distilled water                        \
    \                         1000.0       ml\",\n        \"snapshot_sha256\": \"\
    fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\",\n        \"\
    parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"Add the separate 1000 ml distilled-water\
    \ stock input. Do not mix it with the 250 ml basal water or promote it to the\
    \ receiving denominator.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"subject\"\
    : \"Initial and later pH endpoints\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.8\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.8\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Main preparation pH and boil sequence\",\n  \
    \      \"exact_source_quote\": \"adjust pH to 7.8 and boil for\\n10 min. Readjust\
    \ pH to 7.3.\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"Keep 7.8 explicitly as the initial pre-boil\
    \ endpoint and 7.3 as the subsequent adjustment. Correct the unqualified single\
    \ pH representation or associate it with its stage; the source does not measure\
    \ final pH after seawater addition.\"\n  },\n  {\n    \"decision_id\": \"q15\"\
    ,\n    \"subject\": \"Ten-minute boil\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Main basal boiling duration\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7.8 and boil for\\n10 min.\",\n        \"snapshot_sha256\": \"\
    fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\",\n        \"\
    parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The existing preparation contains the\
    \ source ten-minute boil at this stage. Attach exact support; this is not the\
    \ autoclave duration.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"subject\"\
    : \"Autoclave 121 degrees C for 20 minutes\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Primary PDF extracted cycle, exact glyph retained\"\
    ,\n        \"exact_source_quote\": \"Add agar and autoclave at 121C for 20 min.\"\
    ,\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The local normalized Celsius glyph represents\
    \ the explicitly printed 121°C, 20-minute cycle. It applies to the basal agar\
    \ preparation, not the sterile seawater or an organism incubation.\"\n  },\n \
    \ {\n    \"decision_id\": \"q17\",\n    \"subject\": \"Warm sterile seawater at\
    \ 55 degrees C\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Post-autoclave agar branch addition\",\n    \
    \    \"exact_source_quote\": \"autoclaving, add warm (55C) sterile sea water.\"\
    ,\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The existing 55°C addition is explicit\
    \ for the agar branch. Preserve that addition stage and do not label it growth\
    \ temperature.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"subject\": \"\
    Liquid branch room-temperature mixing\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve beef extract and peptone by heating in tap water, adjust pH to 7.8\
    \ and boil for 10 min. Readjust pH to 7.3. Add agar and autoclave at 121°C for\
    \ 20 min. Directly after autoclaving, add warm (55°C) sterile sea water. Liquid\
    \ medium without agar should be combined when cooled to room temperature.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Liquid alternative after cooling\",\n       \
    \ \"exact_source_quote\": \"Liquid medium without agar should be\\ncombined when\
    \ cooled to room temperature.\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The qualitative room-temperature condition\
    \ is explicit. Do not assign an invented numeric temperature or make agar mandatory.\"\
    \n  },\n  {\n    \"decision_id\": \"q19\",\n    \"subject\": \"Natural seawater\
    \ aging\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Natural sea water is stored in the dark for at least three weeks to \\\"age\\\
    \". If natural sea water is not available use artificial sea water:\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Natural sea water is stored in the dark for at least three weeks to \\\"age\\\
    \". If natural sea water is not available use artificial sea water:\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1588\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Natural-seawater preparation, minimum duration\"\
    ,\n        \"exact_source_quote\": \"Natural sea water is stored in the dark for\
    \ at least three weeks to \\\"age\\\".\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The existing instruction correctly retains\
    \ darkness and a minimum three-week aging duration. It applies to natural seawater;\
    \ artificial seawater is the stated alternative.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"subject\": \"Titrant amount\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Main pH readjustment\",\n        \"exact_source_quote\"\
    : \"Readjust pH to 7.3.\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"The source supplies endpoints but no titrant\
    \ identity or fixed dose. No amount is invented.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"subject\": \"Incubation temperature\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1588\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf\"\
    ,\n        \"source_locator\": \"Preparation temperature scope\",\n        \"\
    exact_source_quote\": \"Liquid medium without agar should be\\ncombined when cooled\
    \ to room temperature.\",\n        \"snapshot_sha256\": \"fdf9aa12ee9bb1661f0fe5f5e4cff5dc2a4d124f8a7273f49825232c15d3a0a2\"\
    ,\n        \"parsed_text_sha256\": \"39093e1c45c75132ce5db90c46a22922ebdfaad2a1ef925b19735ba240a08009\"\
    \n      }\n    ],\n    \"rationale\": \"No growth/incubation temperature is supplied;\
    \ preparation temperatures do not support a generic incubation value.\"\n  }\n\
    ]"
findings:
- finding_id: f1
  issue_key: bradymonas-seawater-alternative-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore seawater alternatives and separate stock quantities
  description: The record simultaneously retains natural seawater and all artificial-stock
    salts, sums basal and full-stock sodium chloride, and loses the 750 ml stock-dose
    stage. This changes the formulation regardless of any disputed final-volume interpretation.
  target_ids:
  - CultureMech:001064
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: bradymonas-water-units-and-batch-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volumes are stored as mass concentrations
  description: Tap water 250 and natural seawater 750 are source millilitres but local
    G_PER_L values. The remaining listed masses also lack an independently established
    final-volume denominator.
  target_ids:
  - CultureMech:001064
  field_paths:
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients
  evidence_ids:
  - primary
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
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
  issue_key: bradymonas-ph-stage
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Expose the later pH adjustment with its stage
  description: The standalone pH field is 7.8 although the preserved procedure next
    readjusts to 7.3. The initial value cannot serve as an unqualified complete-medium
    endpoint.
  target_ids:
  - CultureMech:001064
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - primary
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Rebuild Solution A and a separately scoped seawater choice in the maintained
    owner. Preserve 5 g basal NaCl, the complete artificial stock and the 750 ml addition
    without summing the entire stock into the main recipe.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001064
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
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
  description: Represent the liquid inputs as batch volumes and retain other source
    masses at their stages; preserve uncertainty in final volume instead of substituting
    a guessed litre denominator.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001064
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
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
  description: Represent both source pH stages explicitly and qualify any scalar field
    according to its documented stage; do not claim a measured final pH after seawater
    addition.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001064
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml
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
- The current exact MediaDive 1588 request returned HTTP 503. The complete DSMZ primary
  is available; no failed provider response is treated as quantity or denominator
  evidence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-045
- generated-medium
```
