# Source and formulation review: anaerobiospirillum_thomasii_medium (CultureMech:001945)

- Review: 20261021T152650Z-culturemech-001945-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:15:06Z
- Finished UTC: 2026-10-21T15:26:50Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 800 is correctly identified, but the record substitutes aminovaleric acid and hydroxybenzoic acid for source bicarbonate, cysteine and sulfide additions, and represents broth/enrichment volumes as g/L. The generated hydroxybenzoate value also predates an owner duplicate repair. Restore the exact source-specific formulation and retain unavailable historical API correspondence as a separate limit.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 269; batch 027 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-six task batches contain 260 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 263 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001945 | data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml | generated | anaerobiospirillum_thomasii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001945 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001945 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/269/strict.tsv |
| validate-terms | passed | True | CultureMech:001945 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001945 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001945 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive800api | unavailable | True | CultureMech:001945 | mediadive800api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive800api_retry | unavailable | True | CultureMech:001945 | mediadive800api_retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Historical provider recipe correspondence | unavailable | True | CultureMech:001945 | Both current API attempts returned 503. The derivative report records historical source metadata but cannot revalidate its five reported source rows against original response bytes. Exact DSMZ and supplier primaries remain available. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001945.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001945.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 2/4 primary and 2/4 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 4: primary 50.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001945.

14 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Stable source membership and distinct maintained state

identity: supported. Targets: CultureMech:001945.

CultureMech:001945, DSMZ 800, the complete source title/link and sole maintained owner agree. Both local layers retain four direct ingredients. The generated target has 0.2 g/L hydroxybenzoate with a summed-duplicate note, while the owner has 0.1 g/L and a later repair event. Neither the title nor the generic application establishes a strain-specific growth claim.

### Source-specific additions and unsupported chemical substitutions

consistency: concern. Targets: CultureMech:001945.

DSMZ 800 starts with 10 mL prepared Oxoid CM643 broth. It then adds 0.5 mL of 5% w/v NaHCO3, 1 mL Fildes Enrichment BBL20810, 0.1 mL of 3% w/v cysteine-HCl monohydrate and 0.1 mL of 3% w/v sodium sulfide nonahydrate. Local aminovaleric acid and hydroxybenzoic acid are not those chemicals; the two reducing additions must remain separate. The broth 10 and enrichment 1 are volumes, not g/L. The 11.7 mL listed-liquid sum is not a measured final denominator.

### Canonical labels versus the chemical claims actually supplied

grounding: concern. Targets: CultureMech:001945.

CHEBI:15887 correctly labels 5-aminopentanoic acid, and CHEBI:30764 correctly labels 3-hydroxybenzoic acid. Their structures and names do not match bicarbonate or the cysteine/sulfide additions. Correct primary/current CHEBI-based secondary labels do not authenticate these source substitutions. No replacement ontology ID is invented; source-specific identities must be reconciled before new mappings are attached.

### Per-aliquot supplements and separate plate alternative

completeness: concern. Targets: CultureMech:001945.

The existing procedure preserves 80% N2 plus 20% CO2, post-autoclave cooling, per-10 mL additions, completed-medium pH 6.8–7.0 and a separately named Columbia sheep-blood agar alternative under 5–10% CO2. The quantified supplement list and its individual gas conditions are absent from the represented solution hierarchy. The supplier base-product 121°C/15 min cycle applies to preparation of CM0643, not to autoclaving the final supplemented mixture. The scalar pH 6.9 is an in-range summary, not an exact endpoint printed by DSMZ.

### Complex liquid recipe and bounded product evidence

scope: supported. Targets: CultureMech:001945.

The supplier’s peptones/yeast extract support COMPLEX/UNDEFINED, and the represented main recipe is liquid. The mentioned agar plates are an alternative formulation, not evidence that the liquid recipe contains agar. Supplier quality-control organisms, inocula, growth and temperature/time results do not transfer to DSMZ 800. No DOI, PMID, taxon, assembly, internal stock path, legacy MIM identifier or KG match is asserted.

### Historical duplicate correction does not repair source identity

provenance: concern. Targets: CultureMech:001945.

The September 2 owner event collapsed the recorded identical 0.1 values without source lookup. The earlier generated target still sums them to 0.2. Reconcile/regenerate that stale layer after source curation; repeating the owner duplicate repair would not recover the distinct cysteine and sulfide stocks or remove the unsupported hydroxybenzoate identity. The October derivative report changed neither owner nor these unresolved claims.

### Available primary evidence versus missing historical API bytes

evidence: unknown. Targets: CultureMech:001945.

The exact DSMZ PDF and named supplier specification independently establish the current source comparison. Current API 503 responses establish access failure only. The attributed historical report is preserved and fully read, including its unresolved status and source-row attributes, but no newly verified raw API correspondence is claimed. No existing attached concentration evidence is present in either local layer.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001945.

25 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Prepared CM643 broth aliquot",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The local 10 g/L is not the source 10 mL aliquot of already prepared broth. Preserve product identity and base-product reconstitution separately from the supplemented-medium basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unsupported aminovaleric acid row",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 1",
        "exact_source_quote": "5% (w/v) NaHCO3 (flushed with N2 + CO2) 0.5 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The local 0.5 g/L aminovaleric acid has no corresponding primary ingredient. The source instead gives 0.5 mL of 5% w/v sodium bicarbonate; correcting the unit alone does not fix identity.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Fildes enrichment addition",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 2",
        "exact_source_quote": "Fildes Enrichment (BBL 20810) (under N2) 1.0 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The source supplies 1 mL of the named enrichment per 10 mL broth. No density, neat mass or final g/L concentration is given.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unsupported hydroxybenzoate row and stale sum",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 3",
        "exact_source_quote": "3% (w/v) cysteine-HCl x H2O (under N2) 0.1 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 4",
        "exact_source_quote": "3% (w/v) Na2S x 9 H2O (under N2) 0.1 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Neither local hydroxybenzoate value is a primary ingredient amount. Target 0.2 g/L and repaired owner 0.1 g/L are distinct historical states; preserve their exact stored values while restoring two different named stocks, not a combined benzoate amount.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Bicarbonate 5% w/v stock, 0.5 mL",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 1",
        "exact_source_quote": "5% (w/v) NaHCO3 (flushed with N2 + CO2) 0.5 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Represent the explicit strength/dose as its own source-scoped solution addition, preserving the individual gas qualifier and per-aliquot receiving basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "5 g per 100 mL × 0.5 mL = 0.025 g bicarbonate delivered. This is an amount, not a final concentration."
  },
  {
    "ingredient_or_context": "Fildes Enrichment BBL20810, 1 mL",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 2",
        "exact_source_quote": "Fildes Enrichment (BBL 20810) (under N2) 1.0 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Represent the explicit strength/dose as its own source-scoped solution addition, preserving the individual gas qualifier and per-aliquot receiving basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "The 1 mL dose is exact. Its composition, density and delivered component masses are not specified by this primary."
  },
  {
    "ingredient_or_context": "Cysteine-HCl monohydrate 3% w/v stock, 0.1 mL",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 3",
        "exact_source_quote": "3% (w/v) cysteine-HCl x H2O (under N2) 0.1 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Represent the explicit strength/dose as its own source-scoped solution addition, preserving the individual gas qualifier and per-aliquot receiving basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "3 g per 100 mL × 0.1 mL = 0.003 g of the named monohydrate delivered; no final denominator is inferred."
  },
  {
    "ingredient_or_context": "Sodium sulfide nonahydrate 3% w/v stock, 0.1 mL",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 4",
        "exact_source_quote": "3% (w/v) Na2S x 9 H2O (under N2) 0.1 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Represent the explicit strength/dose as its own source-scoped solution addition, preserving the individual gas qualifier and per-aliquot receiving basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "3 g per 100 mL × 0.1 mL = 0.003 g of the named nonahydrate delivered; this is separate from the cysteine addition."
  },
  {
    "ingredient_or_context": "Unquantified Fildes component composition",
    "field_path": "solutions",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, supplement row 2",
        "exact_source_quote": "Fildes Enrichment (BBL 20810) (under N2) 1.0 ml",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The source names BBL20810 and gives a volume but no composition or component mass. Do not invent a recipe or expand the product from a different formulation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Named supplier base-product reconstitution",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Directions, first sentence",
        "exact_source_quote": "Suspend 33g in 1 litre of warm distilled water.",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1, opening paragraph; prepared broth aliquot",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The exact CM0643 direction applies to the prepared base broth only. It is not 33 g/L of final supplemented DSMZ 800 and must not replace the per-10 mL stock-addition representation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "On the supplier’s nominal 33 g per litre preparation basis, a 10 mL aliquot corresponds to 0.33 g powder; this does not establish final supplemented volume or a measured solution density."
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Tryptone",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Tryptone row; grams per litre heading",
        "exact_source_quote": "Tryptone     grams per litre    10.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Gelatin peptone",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Gelatin peptone row; grams per litre heading",
        "exact_source_quote": "Gelatin peptone         10.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Yeast extract",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Yeast extract row; grams per litre heading",
        "exact_source_quote": "Yeast extract            5.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Glucose",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Glucose row; grams per litre heading",
        "exact_source_quote": "Glucose            1.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Sodium chloride",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Sodium chloride row; grams per litre heading",
        "exact_source_quote": "Sodium chloride           5.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: L-Arginine",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, L-Arginine row; grams per litre heading",
        "exact_source_quote": "L-Arginine            1.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Sodium pyruvate",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Sodium pyruvate row; grams per litre heading",
        "exact_source_quote": "Sodium pyruvate           1.0",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Menadione",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Menadione row; grams per litre heading",
        "exact_source_quote": "Menadione            0.0005",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 typical base formula: Haemin",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula, Haemin row; grams per litre heading",
        "exact_source_quote": "Haemin            0.005",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      },
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 Typical Formula qualification",
        "exact_source_quote": "* adjusted as required to meet performance standards",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "This is a supplier typical base-product amount, subject to the printed adjustment qualification. If documenting the base stock composition, retain it at that product stage; do not silently expand these as exact final DSMZ 800 ingredients or assert all commercial lots have an invariant formula.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Prepared-broth aliquot basis",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1 opening paragraph",
        "exact_source_quote": "per 10 ml the following sterile, anaerobic solutions:",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The receiving aliquot is already preserved in prose, with no matching attached source evidence; it is not a 10 mL total final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Main preparation atmosphere",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1 opening paragraph",
        "exact_source_quote": "under 80% N2 + 20% CO2 gas.",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "Both stated gas fractions survive in the local procedure. Preserve this atmosphere without transferring the separate plate CO2 range.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Completed-medium pH range",
    "field_path": "preparation_steps[1].description",
    "decision": "evidence_only",
    "local": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1 final paragraph",
        "exact_source_quote": "The pH of the completed medium should be 6.8 - 7.0.",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The full range is preserved in prose but has no attached source evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Scalar pH precision",
    "field_path": "ph_value",
    "decision": "unsupported",
    "local": 6.9,
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1 final paragraph",
        "exact_source_quote": "The pH of the completed medium should be 6.8 - 7.0.",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "6.9 is within the supported range, but the primary does not select it as an exact endpoint. Preserve the range and label any scalar summary as such rather than treating the midpoint as a literal source value.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 6.9,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.9,
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Separate agar-plate atmosphere",
    "field_path": "preparation_steps[1].description",
    "decision": "evidence_only",
    "local": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
    "source_snippets": [
      {
        "source_key": "dsmz800",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf",
        "source_locator": "Page 1 plate-alternative paragraph",
        "exact_source_quote": "atmosphere containig 5 - 10% CO2.",
        "snapshot_sha256": "de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8",
        "parsed_text_sha256": "4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c"
      }
    ],
    "rationale": "The 5–10% CO2 range belongs only to the explicitly named Columbia sheep-blood agar alternative, not the liquid-medium preparation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "CM0643 base sterilization cycle",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "COOL",
        "description": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:"
      },
      {
        "step_number": 2,
        "action": "MIX",
        "description": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2."
      }
    ],
    "source_snippets": [
      {
        "source_key": "oxoidCM0643",
        "source_url": "https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf",
        "source_locator": "Page 1 supplier Directions",
        "exact_source_quote": "sterilize by autoclaving at 121°C for 15 minutes.",
        "snapshot_sha256": "0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d",
        "parsed_text_sha256": "d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5"
      }
    ],
    "rationale": "Attach the named base-product cycle at the base-preparation stage. It is not evidence to autoclave the final mixture after sterile supplements are added.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "COOL",
            "description": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "COOL",
            "description": "Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the following sterile, anaerobic solutions:"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2."
          }
        ],
        "decision": "add"
      }
    ]
  }
]

## Findings

### f1: Unsupported chemical substitutions and volume-to-mass conversion change the formulation

blocker / open / confirmed; issue key: thomasii-source-formula-substitution.

The primary’s bicarbonate, cysteine-HCl monohydrate and sodium sulfide nonahydrate stocks are replaced by local aminovaleric acid and hydroxybenzoic acid. Broth and Fildes volumes are also represented as g/L. Valid labels for the substituted chemicals do not support their presence in DSMZ 800, and neither summing nor collapsing the two distinct reducing additions repairs the source formula.

### f2: The generated target retains a sum already collapsed in the owner

major / open / confirmed; issue key: thomasii-stale-duplicate-state.

The target still has hydroxybenzoate 0.2 g/L with [Merged 2 duplicates: 0.1, 0.1], whereas the later maintained owner has 0.1 g/L with an explicit duplicate-repair event. The repair is arithmetic/provenance correction only; the primary still requires two different stock additions rather than either benzoate value.

### f3: The preserved preparation is disconnected from its exact supplement list

major / open / confirmed; issue key: thomasii-preparation-stock-linkage.

The local text says to add the following solutions but the source strengths/doses and individual gas handling have become unrelated direct ingredient rows. Supplier base reconstitution/cycle and the separate plate alternative require explicit scope; the scalar pH midpoint must not replace the source range. This is a preparation-representation defect, not a claim that all sterilization instructions are absent.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the maintained owner from the exact primary: named prepared base broth, individually scoped strength/dose additions and their source forms. Replace unsupported ingredient identities only after exact grounding; keep broth-product and final-medium bases separate. Preserve historical attribution and do not invent a final-volume denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the existing owner repair and reconcile its remaining source-identity defects before regenerating the target. Do not repeat that repair or present 0.1 g/L hydroxybenzoate as source-validated.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore the exact per-10 mL supplement sequence and each gas qualifier, associate CM0643 reconstitution/sterilization with the base stage, retain the completed-medium pH range and keep the agar-plate alternative separate. Exclude all supplier QC organisms and performance conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch027/269/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/269/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml:1:id: CultureMech:001945<br>./data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml:1:id: CultureMech:001945<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/269/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 6 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/269/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf; Complete one-page DSMZ 800 PDF; visual page and extracted text | supports | The exact primary specifies additions per 10 mL prepared Oxoid CM643 broth, each solution strength/dose, anaerobic conditions, completed-medium pH range and a separately named plate alternative. No aminoacid/benzoate substitution is printed. |
| base-product | https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf; Page 1: exact CM0643 identity, typical base formula, reconstitution and sterilization directions only | supports | The supplier identifies the base product and directs 33 g in 1 litre warm distilled water, with a typical formula adjusted to performance standards. These are unsupplemented base-product details, not final DSMZ 800 concentrations. Quality-control organisms, growth-performance claims, challenge inocula and test conditions are excluded. |
| mediadive800api-attempt | https://mediadive.dsmz.de/rest/medium/800; Preserved exact public retrieval result | context_only | mediadive800api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive800api_retry-attempt | https://mediadive.dsmz.de/rest/medium/800; Preserved exact public retrieval result | context_only | mediadive800api_retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| chebi15887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15887 resolves to 5-aminopentanoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30764 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30764; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30764 resolves to 3-hydroxybenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15887": [{"label": "5-Aminovaleric acid", "match_type": "preferred_term", "identifier": "CHEBI:15887", "preferred_term": "5-Aminovaleric acid", "ontology_id": "CHEBI:15887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30764": [{"label": "3-Hydroxybenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30764", "preferred_term": "3-Hydroxybenzoic acid", "ontology_id": "CHEBI:30764", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml", "events": 7, "timestamp_issues": []}] |
| historical-report | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobiospirillum_thomasii_medium.yaml.md; Complete record-specific report; all four local rows, five reported API rows and two preparation rows | context_only | The local derivative report preserves an attributed 2026-10-07T12:19:07.498696+00:00 response with SHA256 ef47351a21e0cac0fef82455743e49fb80ef6b265b901422a54fb1c85b0ee71f. Its source attributes describe bicarbonate/cysteine/sulfide while its reported compound labels differ. Original raw API bytes are unavailable; the report is historical context, not a recovered source response. It states the owner was unchanged and claims remained unresolved. |
| duplicate-repair-writer | scripts/repair_merged_duplicates.py; Complete file, especially repair_ingredient and appended history | context_only | The repair restores an identical pre-sum value from a recorded duplicate note; it does not establish chemical identity from a primary source. Current cleanup no longer sums agreeing duplicate values. The owner September 2 repair and target August 6 merge are distinct historical states. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch027/269/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch027/269/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- mediadive800api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive800api_retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- The required historical MediaDive correspondence is unavailable because both current attempts returned 503 and the exact historical raw response was not recovered. The pinned derivative report preserves provenance but is not a recovered primary response.
- Only the named CM0643 base product identity, typical formula and preparation direction are used; supplier quality-control organisms, inocula and growth conditions are explicitly outside scope. No Fildes composition or final supplemented volume is inferred.
- The DSMZ and supplier page 1 images were read alongside their complete extracted text. No replacement chemical identifiers or strain-level growth assertions were introduced.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152650Z-culturemech-001945-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobiospirillum_thomasii_medium (CultureMech:001945)'
started_at: '2026-10-21T15:15:06Z'
finished_at: '2026-10-21T15:26:50Z'
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
summary: DSMZ 800 is correctly identified, but the record substitutes aminovaleric
  acid and hydroxybenzoic acid for source bicarbonate, cysteine and sulfide additions,
  and represents broth/enrichment volumes as g/L. The generated hydroxybenzoate value
  also predates an owner duplicate repair. Restore the exact source-specific formulation
  and retain unavailable historical API correspondence as a separate limit.
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
  - path: data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
    sha256: 1d341fc700fcb0a3ff820c12ee6a6d7ba9f714dd5703f1d233968e9b74aa05d5
    role: target
  - path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
    sha256: 383970a9273aa1095518e336b8beca5d0a93bb787697e14de9aa1af05638f59d
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobiospirillum_thomasii_medium.yaml.md
    sha256: 18c27ccda64997bb5faca29859d2f576a521b38634a61c6996e911bd5156fad2
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 269; batch 027 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-six task batches
    contain 260 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 263 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001945
targets:
- target_id: CultureMech:001945
  path: data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  label: anaerobiospirillum_thomasii_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/269/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/269/strict.tsv"
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001945
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
  - CultureMech:001945
- check_id: mediadive800api-source-access
  name: 'Exact source content access: mediadive800api'
  required: true
  status: unavailable
  summary: 'mediadive800api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - mediadive800api-attempt
- check_id: mediadive800api_retry-source-access
  name: 'Exact source content access: mediadive800api_retry'
  required: true
  status: unavailable
  summary: 'mediadive800api_retry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - mediadive800api_retry-attempt
- check_id: historical-provider-correspondence
  name: Historical provider recipe correspondence
  required: true
  status: unavailable
  summary: Both current API attempts returned 503. The derivative report records historical
    source metadata but cannot revalidate its five reported source rows against original
    response bytes. Exact DSMZ and supplier primaries remain available.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - historical-report
  - mediadive800api-attempt
  - mediadive800api_retry-attempt
  - primary
  - base-product
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:16:03.689262Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/269/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:16:07.054525Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/269/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:16:10.776785Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:16:12.432902Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:26:48Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml:1:id:
    CultureMech:001945

    ./data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml:1:id:
    CultureMech:001945

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/269/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:26:48Z'
  support: supports
  summary: 6 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 273e19c5891d59b5eb3a94e998228d373185098b1dca6e07774e8ced842dc688
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/269/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 29424e1876459dec33a4b5d07955a437ca553ce8a40aa0439af7cc5cb3cb0fac
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf
  locator: Complete one-page DSMZ 800 PDF; visual page and extracted text
  accessed_at: '2026-10-21T14:59:59.203185Z'
  support: supports
  summary: The exact primary specifies additions per 10 mL prepared Oxoid CM643 broth,
    each solution strength/dose, anaerobic conditions, completed-medium pH range and
    a separately named plate alternative. No aminoacid/benzoate substitution is printed.
  snapshot_sha256: de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8
- evidence_id: base-product
  kind: database
  reference: https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf
  locator: 'Page 1: exact CM0643 identity, typical base formula, reconstitution and
    sterilization directions only'
  accessed_at: '2026-10-21T15:02:49.950151Z'
  support: supports
  summary: The supplier identifies the base product and directs 33 g in 1 litre warm
    distilled water, with a typical formula adjusted to performance standards. These
    are unsupplemented base-product details, not final DSMZ 800 concentrations. Quality-control
    organisms, growth-performance claims, challenge inocula and test conditions are
    excluded.
  snapshot_sha256: 0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d
- evidence_id: mediadive800api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/800
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:59:58.500689Z'
  support: context_only
  summary: 'mediadive800api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive800api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/800
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:49.950454Z'
  support: context_only
  summary: 'mediadive800api_retry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: chebi15887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:00:00.511966Z'
  support: supports
  summary: CHEBI:15887 resolves to 5-aminopentanoic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 11287e9a7775cbb5bd48a89d48724cd34136e093ae8f0b25f185cd316c4d20b0
- evidence_id: chebi30764
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30764
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:00:00.516270Z'
  support: supports
  summary: CHEBI:30764 resolves to 3-hydroxybenzoic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 6c0a7e4c3ea852837eb20cf69829ab07696ce0a4f7e4e60781d353400ad9b319
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:26:48Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15887":
    [{"label": "5-Aminovaleric acid", "match_type": "preferred_term", "identifier":
    "CHEBI:15887", "preferred_term": "5-Aminovaleric acid", "ontology_id": "CHEBI:15887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30764": [{"label":
    "3-Hydroxybenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30764",
    "preferred_term": "3-Hydroxybenzoic acid", "ontology_id": "CHEBI:30764", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: historical-report
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerobiospirillum_thomasii_medium.yaml.md
  locator: Complete record-specific report; all four local rows, five reported API
    rows and two preparation rows
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: The local derivative report preserves an attributed 2026-10-07T12:19:07.498696+00:00
    response with SHA256 ef47351a21e0cac0fef82455743e49fb80ef6b265b901422a54fb1c85b0ee71f.
    Its source attributes describe bicarbonate/cysteine/sulfide while its reported
    compound labels differ. Original raw API bytes are unavailable; the report is
    historical context, not a recovered source response. It states the owner was unchanged
    and claims remained unresolved.
  snapshot_sha256: 18c27ccda64997bb5faca29859d2f576a521b38634a61c6996e911bd5156fad2
- evidence_id: duplicate-repair-writer
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: Complete file, especially repair_ingredient and appended history
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: The repair restores an identical pre-sum value from a recorded duplicate
    note; it does not establish chemical identity from a primary source. Current cleanup
    no longer sums agreeing duplicate values. The owner September 2 repair and target
    August 6 merge are distinct historical states.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/269/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 1b024225a4f15f977969b60e16cd502acdf0b3b07536a480c553c3e5a219d179
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/269/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:26:48Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: bf5b6de429a91fc3dc4226e476f3e4ed6fa6825a382f2987c8a8024e09d136b0
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '2 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 2/4 primary
    and 2/4 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15887
  - chebi30764
  details: 'Instance coverage on a 0–100 percent scale, denominator 4: primary 50.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Stable source membership and distinct maintained state
  outcome: supported
  summary: CultureMech:001945, DSMZ 800, the complete source title/link and sole maintained
    owner agree. Both local layers retain four direct ingredients. The generated target
    has 0.2 g/L hydroxybenzoate with a summed-duplicate note, while the owner has
    0.1 g/L and a later repair event. Neither the title nor the generic application
    establishes a strain-specific growth claim.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - primary
  - id-search
- assessment_id: source-formulation
  area: consistency
  topic: Source-specific additions and unsupported chemical substitutions
  outcome: concern
  summary: DSMZ 800 starts with 10 mL prepared Oxoid CM643 broth. It then adds 0.5
    mL of 5% w/v NaHCO3, 1 mL Fildes Enrichment BBL20810, 0.1 mL of 3% w/v cysteine-HCl
    monohydrate and 0.1 mL of 3% w/v sodium sulfide nonahydrate. Local aminovaleric
    acid and hydroxybenzoic acid are not those chemicals; the two reducing additions
    must remain separate. The broth 10 and enrichment 1 are volumes, not g/L. The
    11.7 mL listed-liquid sum is not a measured final denominator.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - primary
  - base-product
- assessment_id: source-grounding
  area: grounding
  topic: Canonical labels versus the chemical claims actually supplied
  outcome: concern
  summary: CHEBI:15887 correctly labels 5-aminopentanoic acid, and CHEBI:30764 correctly
    labels 3-hydroxybenzoic acid. Their structures and names do not match bicarbonate
    or the cysteine/sulfide additions. Correct primary/current CHEBI-based secondary
    labels do not authenticate these source substitutions. No replacement ontology
    ID is invented; source-specific identities must be reconciled before new mappings
    are attached.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi15887
  - chebi30764
  - mim
- assessment_id: preparation
  area: completeness
  topic: Per-aliquot supplements and separate plate alternative
  outcome: concern
  summary: The existing procedure preserves 80% N2 plus 20% CO2, post-autoclave cooling,
    per-10 mL additions, completed-medium pH 6.8–7.0 and a separately named Columbia
    sheep-blood agar alternative under 5–10% CO2. The quantified supplement list and
    its individual gas conditions are absent from the represented solution hierarchy.
    The supplier base-product 121°C/15 min cycle applies to preparation of CM0643,
    not to autoclaving the final supplemented mixture. The scalar pH 6.9 is an in-range
    summary, not an exact endpoint printed by DSMZ.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - primary
  - base-product
- assessment_id: classification
  area: scope
  topic: Complex liquid recipe and bounded product evidence
  outcome: supported
  summary: The supplier’s peptones/yeast extract support COMPLEX/UNDEFINED, and the
    represented main recipe is liquid. The mentioned agar plates are an alternative
    formulation, not evidence that the liquid recipe contains agar. Supplier quality-control
    organisms, inocula, growth and temperature/time results do not transfer to DSMZ
    800. No DOI, PMID, taxon, assembly, internal stock path, legacy MIM identifier
    or KG match is asserted.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - primary
  - base-product
- assessment_id: generated-correspondence
  area: provenance
  topic: Historical duplicate correction does not repair source identity
  outcome: concern
  summary: The September 2 owner event collapsed the recorded identical 0.1 values
    without source lookup. The earlier generated target still sums them to 0.2. Reconcile/regenerate
    that stale layer after source curation; repeating the owner duplicate repair would
    not recover the distinct cysteine and sulfide stocks or remove the unsupported
    hydroxybenzoate identity. The October derivative report changed neither owner
    nor these unresolved claims.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - owner-0
  - duplicate-repair-writer
  - historical-report
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: historical-source
  area: evidence
  topic: Available primary evidence versus missing historical API bytes
  outcome: unknown
  summary: The exact DSMZ PDF and named supplier specification independently establish
    the current source comparison. Current API 503 responses establish access failure
    only. The attributed historical report is preserved and fully read, including
    its unresolved status and source-row attributes, but no newly verified raw API
    correspondence is claimed. No existing attached concentration evidence is present
    in either local layer.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - historical-report
  - primary
  - base-product
  - mediadive800api-attempt
  - mediadive800api_retry-attempt
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 25 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001945
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Prepared CM643 broth aliquot\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz800\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The local 10 g/L is not the source 10\
    \ mL aliquot of already prepared broth. Preserve product identity and base-product\
    \ reconstitution separately from the supplemented-medium basis.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unsupported aminovaleric acid row\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 1\",\n        \"exact_source_quote\"\
    : \"5% (w/v) NaHCO3 (flushed with N2 + CO2) 0.5 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The local 0.5 g/L aminovaleric acid has\
    \ no corresponding primary ingredient. The source instead gives 0.5 mL of 5% w/v\
    \ sodium bicarbonate; correcting the unit alone does not fix identity.\",\n  \
    \  \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Fildes enrichment addition\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 2\",\n        \"exact_source_quote\"\
    : \"Fildes Enrichment (BBL 20810) (under N2) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The source supplies 1 mL of the named\
    \ enrichment per 10 mL broth. No density, neat mass or final g/L concentration\
    \ is given.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Unsupported hydroxybenzoate row and stale sum\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 3\",\n        \"exact_source_quote\"\
    : \"3% (w/v) cysteine-HCl x H2O (under N2) 0.1 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, supplement row 4\",\n        \"exact_source_quote\"\
    : \"3% (w/v) Na2S x 9 H2O (under N2) 0.1 ml\",\n        \"snapshot_sha256\": \"\
    de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n        \"\
    parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Neither local hydroxybenzoate value is\
    \ a primary ingredient amount. Target 0.2 g/L and repaired owner 0.1 g/L are distinct\
    \ historical states; preserve their exact stored values while restoring two different\
    \ named stocks, not a combined benzoate amount.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Bicarbonate 5% w/v stock, 0.5 mL\",\n    \"field_path\": \"solutions\",\n\
    \    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 1\",\n        \"exact_source_quote\"\
    : \"5% (w/v) NaHCO3 (flushed with N2 + CO2) 0.5 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit strength/dose as\
    \ its own source-scoped solution addition, preserving the individual gas qualifier\
    \ and per-aliquot receiving basis.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"5 g per 100 mL\
    \ × 0.5 mL = 0.025 g bicarbonate delivered. This is an amount, not a final concentration.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Fildes Enrichment BBL20810, 1 mL\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz800\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 2\",\n        \"exact_source_quote\"\
    : \"Fildes Enrichment (BBL 20810) (under N2) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit strength/dose as\
    \ its own source-scoped solution addition, preserving the individual gas qualifier\
    \ and per-aliquot receiving basis.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"The 1 mL dose\
    \ is exact. Its composition, density and delivered component masses are not specified\
    \ by this primary.\"\n  },\n  {\n    \"ingredient_or_context\": \"Cysteine-HCl\
    \ monohydrate 3% w/v stock, 0.1 mL\",\n    \"field_path\": \"solutions\",\n  \
    \  \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 3\",\n        \"exact_source_quote\"\
    : \"3% (w/v) cysteine-HCl x H2O (under N2) 0.1 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit strength/dose as\
    \ its own source-scoped solution addition, preserving the individual gas qualifier\
    \ and per-aliquot receiving basis.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"3 g per 100 mL\
    \ × 0.1 mL = 0.003 g of the named monohydrate delivered; no final denominator\
    \ is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Sodium sulfide nonahydrate\
    \ 3% w/v stock, 0.1 mL\",\n    \"field_path\": \"solutions\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1, supplement row 4\",\n        \"exact_source_quote\"\
    : \"3% (w/v) Na2S x 9 H2O (under N2) 0.1 ml\",\n        \"snapshot_sha256\": \"\
    de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n        \"\
    parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit strength/dose as\
    \ its own source-scoped solution addition, preserving the individual gas qualifier\
    \ and per-aliquot receiving basis.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"3 g per 100 mL\
    \ × 0.1 mL = 0.003 g of the named nonahydrate delivered; this is separate from\
    \ the cysteine addition.\"\n  },\n  {\n    \"ingredient_or_context\": \"Unquantified\
    \ Fildes component composition\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n        \"\
    source_locator\": \"Page 1, supplement row 2\",\n        \"exact_source_quote\"\
    : \"Fildes Enrichment (BBL 20810) (under N2) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The source names BBL20810 and gives a\
    \ volume but no composition or component mass. Do not invent a recipe or expand\
    \ the product from a different formulation.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"not_quantified\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Named supplier base-product reconstitution\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Directions, first sentence\",\n      \
    \  \"exact_source_quote\": \"Suspend 33g in 1 litre of warm distilled water.\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"dsmz800\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\",\n    \
    \    \"source_locator\": \"Page 1, opening paragraph; prepared broth aliquot\"\
    ,\n        \"exact_source_quote\": \"per 10 ml the following sterile, anaerobic\
    \ solutions:\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The exact CM0643 direction applies to\
    \ the prepared base broth only. It is not 33 g/L of final supplemented DSMZ 800\
    \ and must not replace the per-10 mL stock-addition representation.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"On the supplier’s\
    \ nominal 33 g per litre preparation basis, a 10 mL aliquot corresponds to 0.33\
    \ g powder; this does not establish final supplemented volume or a measured solution\
    \ density.\"\n  },\n  {\n    \"ingredient_or_context\": \"CM0643 typical base\
    \ formula: Tryptone\",\n    \"field_path\": \"solutions\",\n    \"decision\":\
    \ \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"oxoidCM0643\",\n        \"source_url\": \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Tryptone row; grams per\
    \ litre heading\",\n        \"exact_source_quote\": \"Tryptone     grams per litre\
    \    10.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Gelatin peptone\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Gelatin peptone row;\
    \ grams per litre heading\",\n        \"exact_source_quote\": \"Gelatin peptone\
    \         10.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Yeast extract\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Yeast extract row; grams\
    \ per litre heading\",\n        \"exact_source_quote\": \"Yeast extract      \
    \      5.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Glucose\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Glucose row; grams per\
    \ litre heading\",\n        \"exact_source_quote\": \"Glucose            1.0\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Sodium chloride\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Sodium chloride row;\
    \ grams per litre heading\",\n        \"exact_source_quote\": \"Sodium chloride\
    \           5.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: L-Arginine\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, L-Arginine row; grams\
    \ per litre heading\",\n        \"exact_source_quote\": \"L-Arginine         \
    \   1.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Sodium pyruvate\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Sodium pyruvate row;\
    \ grams per litre heading\",\n        \"exact_source_quote\": \"Sodium pyruvate\
    \           1.0\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Menadione\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Menadione row; grams\
    \ per litre heading\",\n        \"exact_source_quote\": \"Menadione          \
    \  0.0005\",\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"CM0643 typical base formula: Haemin\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula, Haemin row; grams per\
    \ litre heading\",\n        \"exact_source_quote\": \"Haemin            0.005\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      },\n      {\n        \"source_key\": \"oxoidCM0643\",\n        \"source_url\"\
    : \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Typical Formula qualification\",\n   \
    \     \"exact_source_quote\": \"* adjusted as required to meet performance standards\"\
    ,\n        \"snapshot_sha256\": \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\"\
    ,\n        \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"This is a supplier typical base-product\
    \ amount, subject to the printed adjustment qualification. If documenting the\
    \ base stock composition, retain it at that product stage; do not silently expand\
    \ these as exact final DSMZ 800 ingredients or assert all commercial lots have\
    \ an invariant formula.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Prepared-broth aliquot basis\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"Use Wilkins Chalgrene\
    \ Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20%\
    \ CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the\
    \ following sterile, anaerobic solutions:\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1 opening paragraph\",\n        \"exact_source_quote\"\
    : \"per 10 ml the following sterile, anaerobic solutions:\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The receiving aliquot is already preserved\
    \ in prose, with no matching attached source evidence; it is not a 10 mL total\
    \ final volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps[0].description\",\n        \"stored\": \"\
    Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically\
    \ under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature\
    \ add per 10 ml the following sterile, anaerobic solutions:\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically\
    \ under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature\
    \ add per 10 ml the following sterile, anaerobic solutions:\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main preparation atmosphere\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"Use Wilkins Chalgrene\
    \ Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically under 80% N2 + 20%\
    \ CO2 gas. After autoclaving and cooling to room temperature add per 10 ml the\
    \ following sterile, anaerobic solutions:\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1 opening paragraph\",\n        \"exact_source_quote\"\
    : \"under 80% N2 + 20% CO2 gas.\",\n        \"snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"Both stated gas fractions survive in the\
    \ local procedure. Preserve this atmosphere without transferring the separate\
    \ plate CO2 range.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically\
    \ under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature\
    \ add per 10 ml the following sterile, anaerobic solutions:\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM 643) and prepare it anaerobically\
    \ under 80% N2 + 20% CO2 gas. After autoclaving and cooling to room temperature\
    \ add per 10 ml the following sterile, anaerobic solutions:\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Completed-medium pH range\",\n    \"field_path\": \"preparation_steps[1].description\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"The pH of the completed\
    \ medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood\
    \ agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig\
    \ 5 - 10% CO2.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final paragraph\",\n        \"exact_source_quote\"\
    : \"The pH of the completed medium should be 6.8 - 7.0.\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The full range is preserved in prose but\
    \ has no attached source evidence.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps[1].description\",\n   \
    \     \"stored\": \"The pH of the completed medium should be 6.8 - 7.0. For growth\
    \ an agar plates, Columbia sheep blood agar plates (BBL) may be used and incubated\
    \ under an anaerobic atmosphere containig 5 - 10% CO2.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates,\
    \ Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic\
    \ atmosphere containig 5 - 10% CO2.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Scalar pH precision\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"decision\": \"unsupported\",\n   \
    \ \"local\": 6.9,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final paragraph\",\n        \"exact_source_quote\"\
    : \"The pH of the completed medium should be 6.8 - 7.0.\",\n        \"snapshot_sha256\"\
    : \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\",\n    \
    \    \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"6.9 is within the supported range, but\
    \ the primary does not select it as an exact endpoint. Preserve the range and\
    \ label any scalar summary as such rather than treating the midpoint as a literal\
    \ source value.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ph_value\",\n        \"stored\": 6.9,\n        \"decision\"\
    : \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9,\n        \"\
    decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Separate agar-plate atmosphere\",\n    \"field_path\": \"preparation_steps[1].description\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"The pH of the completed\
    \ medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep blood\
    \ agar plates (BBL) may be used and incubated under an anaerobic atmosphere containig\
    \ 5 - 10% CO2.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz800\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium800.pdf\"\
    ,\n        \"source_locator\": \"Page 1 plate-alternative paragraph\",\n     \
    \   \"exact_source_quote\": \"atmosphere containig 5 - 10% CO2.\",\n        \"\
    snapshot_sha256\": \"de064830b6e32039c337f67bba9d4a9dfb976eb5ed181b97debc55aa3cf191f8\"\
    ,\n        \"parsed_text_sha256\": \"4d0359789b645e6d539dd0f6fc4b3baefa127959d4fdb39126c87ae7e228170c\"\
    \n      }\n    ],\n    \"rationale\": \"The 5–10% CO2 range belongs only to the\
    \ explicitly named Columbia sheep-blood agar alternative, not the liquid-medium\
    \ preparation.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps[1].description\",\n        \"stored\": \"\
    The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates,\
    \ Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic\
    \ atmosphere containig 5 - 10% CO2.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"The pH of the completed medium should be 6.8 - 7.0. For growth an agar plates,\
    \ Columbia sheep blood agar plates (BBL) may be used and incubated under an anaerobic\
    \ atmosphere containig 5 - 10% CO2.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"CM0643 base sterilization\
    \ cycle\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\"\
    ,\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"action\"\
    : \"COOL\",\n        \"description\": \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid\
    \ CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving\
    \ and cooling to room temperature add per 10 ml the following sterile, anaerobic\
    \ solutions:\"\n      },\n      {\n        \"step_number\": 2,\n        \"action\"\
    : \"MIX\",\n        \"description\": \"The pH of the completed medium should be\
    \ 6.8 - 7.0. For growth an agar plates, Columbia sheep blood agar plates (BBL)\
    \ may be used and incubated under an anaerobic atmosphere containig 5 - 10% CO2.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"oxoidCM0643\",\n        \"source_url\": \"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0643-V2.pdf\"\
    ,\n        \"source_locator\": \"Page 1 supplier Directions\",\n        \"exact_source_quote\"\
    : \"sterilize by autoclaving at 121°C for 15 minutes.\",\n        \"snapshot_sha256\"\
    : \"0db62fadef77ebec2a11b4d2a85d662f39886e771c8403c834ea3edcb9400d1d\",\n    \
    \    \"parsed_text_sha256\": \"d4da03c3547cbec4508fe9d6959b5fc3bde63494e1179387a36e7e054eb0daf5\"\
    \n      }\n    ],\n    \"rationale\": \"Attach the named base-product cycle at\
    \ the base-preparation stage. It is not evidence to autoclave the final mixture\
    \ after sterile supplements are added.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    COOL\",\n            \"description\": \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid\
    \ CM 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving\
    \ and cooling to room temperature add per 10 ml the following sterile, anaerobic\
    \ solutions:\"\n          },\n          {\n            \"step_number\": 2,\n \
    \           \"action\": \"MIX\",\n            \"description\": \"The pH of the\
    \ completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep\
    \ blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere\
    \ containig 5 - 10% CO2.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"COOL\",\n\
    \            \"description\": \"Use Wilkins Chalgrene Anaerobe Broth (Oxoid CM\
    \ 643) and prepare it anaerobically under 80% N2 + 20% CO2 gas. After autoclaving\
    \ and cooling to room temperature add per 10 ml the following sterile, anaerobic\
    \ solutions:\"\n          },\n          {\n            \"step_number\": 2,\n \
    \           \"action\": \"MIX\",\n            \"description\": \"The pH of the\
    \ completed medium should be 6.8 - 7.0. For growth an agar plates, Columbia sheep\
    \ blood agar plates (BBL) may be used and incubated under an anaerobic atmosphere\
    \ containig 5 - 10% CO2.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: thomasii-source-formula-substitution
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Unsupported chemical substitutions and volume-to-mass conversion change the
    formulation
  description: The primary’s bicarbonate, cysteine-HCl monohydrate and sodium sulfide
    nonahydrate stocks are replaced by local aminovaleric acid and hydroxybenzoic
    acid. Broth and Fildes volumes are also represented as g/L. Valid labels for the
    substituted chemicals do not support their presence in DSMZ 800, and neither summing
    nor collapsing the two distinct reducing additions repairs the source formula.
  target_ids:
  - CultureMech:001945
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - base-product
  - chebi15887
  - chebi30764
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
  issue_key: thomasii-stale-duplicate-state
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: The generated target retains a sum already collapsed in the owner
  description: 'The target still has hydroxybenzoate 0.2 g/L with [Merged 2 duplicates:
    0.1, 0.1], whereas the later maintained owner has 0.1 g/L with an explicit duplicate-repair
    event. The repair is arithmetic/provenance correction only; the primary still
    requires two different stock additions rather than either benzoate value.'
  target_ids:
  - CultureMech:001945
  field_paths:
  - ingredients[3].concentration
  - ingredients[3].notes
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - duplicate-repair-writer
  - primary
  - historical-report
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
  issue_key: thomasii-preparation-stock-linkage
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The preserved preparation is disconnected from its exact supplement list
  description: The local text says to add the following solutions but the source strengths/doses
    and individual gas handling have become unrelated direct ingredient rows. Supplier
    base reconstitution/cycle and the separate plate alternative require explicit
    scope; the scalar pH midpoint must not replace the source range. This is a preparation-representation
    defect, not a claim that all sterilization instructions are absent.
  target_ids:
  - CultureMech:001945
  field_paths:
  - preparation_steps
  - solutions
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - primary
  - base-product
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
  description: 'Reconstruct the maintained owner from the exact primary: named prepared
    base broth, individually scoped strength/dose additions and their source forms.
    Replace unsupported ingredient identities only after exact grounding; keep broth-product
    and final-medium bases separate. Preserve historical attribution and do not invent
    a final-volume denominator.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001945
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
  description: Preserve the existing owner repair and reconcile its remaining source-identity
    defects before regenerating the target. Do not repeat that repair or present 0.1
    g/L hydroxybenzoate as source-validated.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001945
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
  description: Restore the exact per-10 mL supplement sequence and each gas qualifier,
    associate CM0643 reconstitution/sterilization with the base stage, retain the
    completed-medium pH range and keep the agar-plate alternative separate. Exclude
    all supplier QC organisms and performance conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001945
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml
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
- 'mediadive800api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadive800api_retry: exact public request returned HTTP 503; original access
  time, response bytes and any separately recorded retry are retained. Error bytes
  do not establish formulation or historical absence.'
- The required historical MediaDive correspondence is unavailable because both current
  attempts returned 503 and the exact historical raw response was not recovered. The
  pinned derivative report preserves provenance but is not a recovered primary response.
- Only the named CM0643 base product identity, typical formula and preparation direction
  are used; supplier quality-control organisms, inocula and growth conditions are
  explicitly outside scope. No Fildes composition or final supplemented volume is
  inferred.
- The DSMZ and supplier page 1 images were read alongside their complete extracted
  text. No replacement chemical identifiers or strain-level growth assertions were
  introduced.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-027
- generated-medium
```
