# Source and formulation review: bl_agar (CultureMech:008201)

- Review: 20261022T012237Z-culturemech-008201-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T01:04:18Z
- Finished UTC: 2026-10-22T01:22:37Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

BL Agar is the NBRC 848 formulation using an opaque Nissui product, 50 ml defibrinated horse blood and 950 ml water. The maintained owner has already corrected liquid units, product representation and preparation; the generated target retains older mass-unit and empty-stock defects. Current source wording specifies 5% final without an explicit percentage basis or measured final volume.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 433; batch 044 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-three task batches contain 430 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 433 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008201 | data/merge_yaml/merged/BL_Agar.yaml | generated | bl_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008201 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008201 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/433/strict.tsv |
| validate-terms | passed | True | CultureMech:008201 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008201 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008201 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008201.

The four documented recipes completed; interpret the scope of each separately.

### Current identifiers, canonical labels and exact source forms

grounding: supported. Targets: CultureMech:008201.

5 asserted primary/secondary slots and 2 distinct captured IDs checked; 0 literal label differences. All 2 current secondary assertions join exact preferred-term MIM rows; no selected legacy ID slots. Target direct ingredient linkage is 1/2 primary (50.00%) and 1/2 secondary (50.00%) on a 0–100 linkage scale, not an accuracy score. Water resolves exactly to CHEBI:15377 and its current MIM preferred row. The repaired owner’s UBERON:0000178 is generic blood; the source and preferred term must separately retain horse species, sterile and defibrinated preparation. No generic ontology label proves those attributes. The Nissui BL Agar product remains an opaque commercial mixture; absence of a molecular ID does not make its source identity invalid.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008201.

20 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Attached evidence, historical derivatives and source versions

evidence: concern. Targets: CultureMech:008201.

All target and maintained-owner history, references and evidence arrays inspected. There is no attached concentration evidence. The September repair added liquid units, an opaque product ingredient, generic blood grounding, references and source preparation; the generated target predates these changes. Its newer per-litre/v/v assertions still require qualification against the captured source. Historical review/report material is context only, not authentication of an original historical response or proof that current import/merge code caused the old target.

### NBRC 848 / TOGO M1645 and Nissui product

identity: supported. Targets: CultureMech:008201.

Exact source accessions and product supplier agree. BL Agar is a proprietary product identity; no equivalence to a generic blood-agar base or inferred ingredient formulation is established.

### Preparation, phenotype and growth scope

completeness: concern. Targets: CultureMech:008201.

The owner contains supported autoclave/cooling/dispensing instructions while the target lacks them. The source specifies neither pH nor autoclave cycle nor strain-specific growth experiment. Final 5% is unqualified; no incubation claim follows from cooling to about 50 C.

### Complex undefined solid agar

scope: supported. Targets: CultureMech:008201.

The opaque BL Agar product and blood support the existing complex, undefined solid-agar classification. The supplier label does not establish the product’s complete formulation.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008201.

8 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "topic": "Nissui BL Agar product: 58 g batch amount",
    "decision": "unsupported",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "58",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The source gives 58 g of an opaque commercial product. Neither original source explicitly gives 58 g/L or measured final volume. Preserve the batch amount and supplier, credit the owner for moving it out of an empty solution wrapper, and do not invent the product composition."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "58.0",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The source gives 58 g of an opaque commercial product. Neither original source explicitly gives 58 g/L or measured final volume. Preserve the batch amount and supplier, credit the owner for moving it out of an empty solution wrapper, and do not invent the product composition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, BL Agar product row",
        "exact_source_quote": "BL Agar*\n58\ng",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "togoM1645original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"BL Agar*\",\n          \"volume\": 58,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465"
      },
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Extracted text line 36",
        "exact_source_quote": "*Nissui Pharmaceutical Co. Ltd., Tokyo, Japan.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "The source gives 58 g of an opaque commercial product. Neither original source explicitly gives 58 g/L or measured final volume. Preserve the batch amount and supplier, credit the owner for moving it out of an empty solution wrapper, and do not invent the product composition."
  },
  {
    "quantity_id": "q2",
    "topic": "Blood: 50 ml batch addition",
    "decision": "correct",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the liquid batch amount of 50 ml rather than a mass rate; no density conversion is supported. The owner correctly changed the liquid dimension, but ML_PER_L remains a nominal interpretation rather than an explicitly measured final-volume rate."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "50.0",
          "unit": "ML_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Credit the corrected liquid dimension and supported 50 ml batch dose. Its stored per-litre denominator is not explicitly established; attach the literal dose and qualify any nominal rate instead of claiming a measured final volume."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, blood row",
        "exact_source_quote": "Defibrinated horse blood\n50\nml",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "togoM1645original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Defibrinated horse blood\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465"
      },
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "Restore the liquid batch amount of 50 ml rather than a mass rate; no density conversion is supported. The owner correctly changed the liquid dimension, but ML_PER_L remains a nominal interpretation rather than an explicitly measured final-volume rate."
  },
  {
    "quantity_id": "q3",
    "topic": "Water: 950 ml batch input",
    "decision": "correct",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "950",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the 950 ml water input instead of G_PER_L. The sum of listed blood and water inputs is 1000 ml, but that sum is not an explicit measurement or makeup instruction for the completed medium."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "950.0",
          "unit": "ML_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The owner correctly uses a liquid unit, but the literal source gives a 950 ml input, not an independently measured ML_PER_L final-medium rate. Retain that batch scope."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, water row",
        "exact_source_quote": "Distilled water\n950\nml",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "togoM1645original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 950,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465"
      }
    ],
    "rationale": "Restore the 950 ml water input instead of G_PER_L. The sum of listed blood and water inputs is 1000 ml, but that sum is not an explicit measurement or makeup instruction for the completed medium."
  },
  {
    "quantity_id": "q4",
    "topic": "Owner product and liquid notes: unsupported per-litre wording",
    "decision": "correct",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "NBRC Medium 848 lists 58 g/L BL Agar and notes that the asterisk marks Nissui Pharmaceutical Co. Ltd.; this commercial BL Agar product is retained as an opaque base/solidifying component.",
        "decision": "correct",
        "rationale": "The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC. The captured page instead gives g, ml and 5% (final). Retain the valid amounts and repair credit while distinguishing normalization assumptions from literal source statements."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "NBRC Medium 848 lists 50 ml/L sterile defibrinated horse blood added aseptically to a final 5% v/v.",
        "decision": "correct",
        "rationale": "The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC. The captured page instead gives g, ml and 5% (final). Retain the valid amounts and repair credit while distinguishing normalization assumptions from literal source statements."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "NBRC Medium 848 lists 950 ml/L distilled water.",
        "decision": "correct",
        "rationale": "The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC. The captured page instead gives g, ml and 5% (final). Retain the valid amounts and repair credit while distinguishing normalization assumptions from literal source statements."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, BL Agar product row",
        "exact_source_quote": "BL Agar*\n58\ng",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, blood row",
        "exact_source_quote": "Defibrinated horse blood\n50\nml",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Composition, water row",
        "exact_source_quote": "Distilled water\n950\nml",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      },
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC. The captured page instead gives g, ml and 5% (final). Retain the valid amounts and repair credit while distinguishing normalization assumptions from literal source statements."
  },
  {
    "quantity_id": "q5",
    "topic": "Blood percentage basis: final 5%, not explicitly v/v",
    "decision": "correct",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Aseptically add sterile defibrinated horse blood to 5% v/v final and mix.",
        "decision": "correct",
        "rationale": "Preserve final 5% as the literal source wording and leave its basis unspecified. The listed 50 ml dose plus 950 ml water motivates a nominal volume interpretation, but does not make v/v an exact quotation or prove measured final volume."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "Preserve final 5% as the literal source wording and leave its basis unspecified. The listed 50 ml dose plus 950 ml water motivates a nominal volume interpretation, but does not make v/v an exact quotation or prove measured final volume."
  },
  {
    "quantity_id": "q6",
    "topic": "Cooling to about 50 C and staged blood addition",
    "decision": "add",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Add the missing target preparation while retaining the owner’s supported approximate cooling temperature. Blood is excluded from autoclaving and added aseptically after cooling. This is preparation temperature, not a growth temperature."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Cool to about 50 C.",
        "decision": "evidence_only",
        "rationale": "The existing cooling description agrees with the source approximate 50 C instruction. Add exact claim linkage; do not convert it into an incubation condition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "Add the missing target preparation while retaining the owner’s supported approximate cooling temperature. Blood is excluded from autoclaving and added aseptically after cooling. This is preparation temperature, not a growth temperature."
  },
  {
    "quantity_id": "q7",
    "topic": "Autoclaving without blood; no explicit cycle",
    "decision": "add",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "The source requires autoclaving the base without blood but supplies no temperature or duration. Add the scoped step to the target without inventing a cycle."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Autoclave the BL Agar base without horse blood.",
        "decision": "evidence_only",
        "rationale": "The owner already has the supported autoclave-without-blood step. Attach the exact source; no cycle is specified."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "The source requires autoclaving the base without blood but supplies no temperature or duration. Add the scoped step to the target without inventing a cycle."
  },
  {
    "quantity_id": "q8",
    "topic": "Rapid dispensing into tubes or Petri dishes",
    "decision": "add",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain both stated vessel choices after mixing; no dispensing volume is given. Carry the owner’s supported preparation to the regenerated target."
      },
      {
        "input": "data/normalized_yaml/bacterial/bl_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Quickly dispense into sterile test tubes or Petri dishes.",
        "decision": "evidence_only",
        "rationale": "The owner already retains the source dispensing instruction. Add its exact source claim without a guessed volume."
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc848",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes.",
        "snapshot_sha256": "92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594",
        "parsed_text_sha256": "6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48"
      }
    ],
    "rationale": "Retain both stated vessel choices after mixing; no dispensing volume is given. Carry the owner’s supported preparation to the regenerated target."
  }
]

## Findings

### f1: Restore literal liquid amounts and qualify final-volume rates

major / open / confirmed; issue key: culturemech.008201.liquid-and-volume-basis.

The target stores 950 ml water and 50 ml blood as G_PER_L. The repaired owner fixes the liquid dimension but its per-litre notes and explicit v/v wording are stronger than the source.

### f2: Carry forward the existing opaque-product repair

minor / open / confirmed; issue key: culturemech.008201.empty-commercial-stock.

The target wraps BL Agar in an empty Unknown solution. The maintained owner already represents the Nissui product as an opaque ingredient and retains its supplier.

### f3: Carry forward supported preparation with exact source linkage

minor / open / confirmed; issue key: culturemech.008201.preparation-and-evidence.

The target omits the owner’s staged preparation and references. Literal batch amounts and preparation lack attached claim evidence; the owner’s 5% v/v description needs qualification.

## Recommended Actions And Acceptance Checks

### a1

Use exact batch amounts and source stages, retain final 5% with an unspecified basis, and distinguish any nominal normalization from a measured final-volume concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the owner’s commercial-product representation and supplier during authorized regeneration; do not fabricate a stock recipe or replace the product with another blood-agar formulation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the existing source-supported steps and references, correct only unsupported basis wording, and attach exact scoped claims when curating the authoritative owner.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BL_Agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/bl_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BL_Agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BL_Agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch044/433/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/433/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BL_Agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BL_Agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BL_Agar.yaml:1:id: CultureMech:008201<br>./data/normalized_yaml/bacterial/bl_agar.yaml:1:id: CultureMech:008201<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch044/source-preflight-bound/433/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| main | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848; Full source identity, formulation and scoped preparation | supports | Exact NBRC 848 composition, supplier and complete preparation read. Batch amounts and final-percentage wording are retained literally. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645; Full source identity, formulation and scoped preparation | supports | Exact M1645/NBRC_M848 identity, original units, comments and supplier agree with the collection page; no per-litre concentration fields are supplied. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Full source identity, formulation and scoped preparation | supports | CHEBI:15377 resolves to water. Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| uberon0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000178; Full source identity, formulation and scoped preparation | supports | UBERON:0000178 resolves to blood. Full captured scientific properties, annotations and synonyms inspected; identifier validity is separate from exact supplied-form support. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch044/433/grounding-inventory.json; Every asserted primary/secondary slot; exact captured OLS objects and pinned current MIM rows | context_only | Complete local slot correspondence, canonical labels and supplied-form distinctions. No invented IDs for unresolved complex products. |
| history-metadata | data/merge_yaml/merged/BL_Agar.yaml; data/normalized_yaml/bacterial/bl_agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bl_agar.yaml", "events": 10, "timestamp_issues": []}] |
| history-evidence | /private/tmp/culturemech-review-work-batch044/433/history-evidence-inventory.json; Full current history/evidence arrays and exact relevant historical report joins | context_only | All target and maintained-owner history, references and evidence arrays inspected. There is no attached concentration evidence. The September repair added liquid units, an opaque product ingredient, generic blood grounding, references and source preparation; the generated target predates these changes. Its newer per-litre/v/v assertions still require qualification against the captured source. Historical review/report material is context only, not authentication of an original historical response or proof that current import/merge code caused the old target. |
| writer-0 | scripts/repair_togo_m1645_bl_agar_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The exact BL Agar repair function and current formulation guards were read. The repair intentionally moves the product out of an empty solution, changes liquid units and adds preparation; its per-litre/v/v prose exceeds literal source wording. Current guarded merger behavior is separate from the historical target state. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The exact BL Agar repair function and current formulation guards were read. The repair intentionally moves the product out of an empty solution, changes liquid units and adds preparation; its per-litre/v/v prose exceeds literal source wording. Current guarded merger behavior is separate from the historical target state. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The exact BL Agar repair function and current formulation guards were read. The repair intentionally moves the product out of an empty solution, changes liquid units and adds preparation; its per-litre/v/v prose exceeds literal source wording. Current guarded merger behavior is separate from the historical target state. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch044/433/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The captured sources do not establish the proprietary Nissui product composition, an explicit percentage basis or a measured final medium volume.
- No pH, autoclave cycle or observed organism-growth claim is supplied by these recipe sources.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012237Z-culturemech-008201-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bl_agar (CultureMech:008201)'
started_at: '2026-10-22T01:04:18Z'
finished_at: '2026-10-22T01:22:37Z'
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
summary: BL Agar is the NBRC 848 formulation using an opaque Nissui product, 50 ml
  defibrinated horse blood and 950 ml water. The maintained owner has already corrected
  liquid units, product representation and preparation; the generated target retains
  older mass-unit and empty-stock defects. Current source wording specifies 5% final
  without an explicit percentage basis or measured final volume.
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
  - path: data/merge_yaml/merged/BL_Agar.yaml
    sha256: ac02d9dc936682c7360f6c41a0ef379327f08be8a1c3ed8033580345070d7821
    role: target
  - path: data/normalized_yaml/bacterial/bl_agar.yaml
    sha256: de76e9b7060c4ca8aab0e05281d82597ea6949605c21991e2b50e0330f76f05b
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
  - path: reports/yaml_record_review/20260921T215808Z-BL_Agar.md
    sha256: e37a46e3b326db0bcea63dfbadf632af7a92ae126587ebb80fd25aaf52a51185
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_togo_m1645_bl_agar_score15.py
    sha256: 09eaa829195a65100e1ffe5d07511a9903abf133da415678f90d35dd4901bc6f
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
  selection: Task review 433; batch 044 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:008201
targets:
- target_id: CultureMech:008201
  path: data/merge_yaml/merged/BL_Agar.yaml
  label: bl_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BL_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BL_Agar.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch044/433/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/433/strict.tsv"
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BL_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BL_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008201
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
  - CultureMech:008201
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BL_Agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/bl_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BL_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:47.433980Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BL_Agar.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch044/433/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:48.879110Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/433/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BL_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:50.537409Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BL_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:07:51.511266Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T01:22:36Z'
  support: supports
  summary: './data/merge_yaml/merged/BL_Agar.yaml:1:id: CultureMech:008201

    ./data/normalized_yaml/bacterial/bl_agar.yaml:1:id: CultureMech:008201

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/source-preflight-bound/433/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T01:22:36Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: d5053faa3fb8e4a3f4c5f3622a5415205c086625223fc41862b8893d63a5dddc
- evidence_id: main
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:54.499785Z'
  support: supports
  summary: Exact NBRC 848 composition, supplier and complete preparation read. Batch
    amounts and final-percentage wording are retained literally.
  snapshot_sha256: 92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:53.934859Z'
  support: supports
  summary: Exact M1645/NBRC_M848 identity, original units, comments and supplier agree
    with the collection page; no per-litre concentration fields are supplied.
  snapshot_sha256: b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Full captured scientific properties, annotations
    and synonyms inspected; identifier validity is separate from exact supplied-form
    support.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: uberon0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000178
  locator: Full source identity, formulation and scoped preparation
  accessed_at: '2026-10-22T00:53:55.858182Z'
  support: supports
  summary: UBERON:0000178 resolves to blood. Full captured scientific properties,
    annotations and synonyms inspected; identifier validity is separate from exact
    supplied-form support.
  snapshot_sha256: 1922fcc7dd50d09155ecaa4a2fcc417b4f069ebda526a493f4b5ef840b7076da
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/433/grounding-inventory.json
  locator: Every asserted primary/secondary slot; exact captured OLS objects and pinned
    current MIM rows
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: Complete local slot correspondence, canonical labels and supplied-form
    distinctions. No invented IDs for unresolved complex products.
  snapshot_sha256: 91a8cb34893446296a4444ce95e8aa9e261aa627efa953633ef36a02b751fec1
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BL_Agar.yaml; data/normalized_yaml/bacterial/bl_agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/bl_agar.yaml", "events": 10, "timestamp_issues":
    []}]'
- evidence_id: history-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/433/history-evidence-inventory.json
  locator: Full current history/evidence arrays and exact relevant historical report
    joins
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: All target and maintained-owner history, references and evidence arrays
    inspected. There is no attached concentration evidence. The September repair added
    liquid units, an opaque product ingredient, generic blood grounding, references
    and source preparation; the generated target predates these changes. Its newer
    per-litre/v/v assertions still require qualification against the captured source.
    Historical review/report material is context only, not authentication of an original
    historical response or proof that current import/merge code caused the old target.
  snapshot_sha256: cfd4fa120f56fdf74d58e91107526e71d98f0a20a8953f9b3bc0e450eefbcdf3
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_togo_m1645_bl_agar_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: The exact BL Agar repair function and current formulation guards were read.
    The repair intentionally moves the product out of an empty solution, changes liquid
    units and adds preparation; its per-litre/v/v prose exceeds literal source wording.
    Current guarded merger behavior is separate from the historical target state.
  snapshot_sha256: 09eaa829195a65100e1ffe5d07511a9903abf133da415678f90d35dd4901bc6f
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: The exact BL Agar repair function and current formulation guards were read.
    The repair intentionally moves the product out of an empty solution, changes liquid
    units and adds preparation; its per-litre/v/v prose exceeds literal source wording.
    Current guarded merger behavior is separate from the historical target state.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: The exact BL Agar repair function and current formulation guards were read.
    The repair intentionally moves the product out of an empty solution, changes liquid
    units and adds preparation; its per-litre/v/v prose exceeds literal source wording.
    Current guarded merger behavior is separate from the historical target state.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/433/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T01:22:36Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c8c75575db1373884daf72fd9420df2f3cae910a01da4f3314cd8ff43a37cbd3
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Current identifiers, canonical labels and exact source forms
  outcome: supported
  summary: 5 asserted primary/secondary slots and 2 distinct captured IDs checked;
    0 literal label differences. All 2 current secondary assertions join exact preferred-term
    MIM rows; no selected legacy ID slots. Target direct ingredient linkage is 1/2
    primary (50.00%) and 1/2 secondary (50.00%) on a 0–100 linkage scale, not an accuracy
    score. Water resolves exactly to CHEBI:15377 and its current MIM preferred row.
    The repaired owner’s UBERON:0000178 is generic blood; the source and preferred
    term must separately retain horse species, sterile and defibrinated preparation.
    No generic ontology label proves those attributes. The Nissui BL Agar product
    remains an opaque commercial mixture; absence of a molecular ID does not make
    its source identity invalid.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - record
  - grounding-inventory
  - chebi15377
  - uberon0000178
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 20 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: evidence-placement
  area: evidence
  topic: Attached evidence, historical derivatives and source versions
  outcome: concern
  summary: All target and maintained-owner history, references and evidence arrays
    inspected. There is no attached concentration evidence. The September repair added
    liquid units, an opaque product ingredient, generic blood grounding, references
    and source preparation; the generated target predates these changes. Its newer
    per-litre/v/v assertions still require qualification against the captured source.
    Historical review/report material is context only, not authentication of an original
    historical response or proof that current import/merge code caused the old target.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - record
  - history-evidence
  - bound-source-integrity
- assessment_id: identity
  area: identity
  topic: NBRC 848 / TOGO M1645 and Nissui product
  outcome: supported
  summary: Exact source accessions and product supplier agree. BL Agar is a proprietary
    product identity; no equivalence to a generic blood-agar base or inferred ingredient
    formulation is established.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - main
  - provider
  - record
- assessment_id: conditions
  area: completeness
  topic: Preparation, phenotype and growth scope
  outcome: concern
  summary: The owner contains supported autoclave/cooling/dispensing instructions
    while the target lacks them. The source specifies neither pH nor autoclave cycle
    nor strain-specific growth experiment. Final 5% is unqualified; no incubation
    claim follows from cooling to about 50 C.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - main
  - provider
  - record
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex undefined solid agar
  outcome: supported
  summary: The opaque BL Agar product and blood support the existing complex, undefined
    solid-agar classification. The supplier label does not establish the product’s
    complete formulation.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - main
  - provider
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 8 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008201
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"topic\": \"Nissui BL Agar\
    \ product: 58 g batch amount\",\n    \"decision\": \"unsupported\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"58\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"unsupported\",\n        \"rationale\"\
    : \"The source gives 58 g of an opaque commercial product. Neither original source\
    \ explicitly gives 58 g/L or measured final volume. Preserve the batch amount\
    \ and supplier, credit the owner for moving it out of an empty solution wrapper,\
    \ and do not invent the product composition.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"58.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\",\n        \"rationale\": \"The source gives 58 g of an opaque\
    \ commercial product. Neither original source explicitly gives 58 g/L or measured\
    \ final volume. Preserve the batch amount and supplier, credit the owner for moving\
    \ it out of an empty solution wrapper, and do not invent the product composition.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Composition, BL Agar product row\",\n       \
    \ \"exact_source_quote\": \"BL Agar*\\n58\\ng\",\n        \"snapshot_sha256\"\
    : \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\",\n    \
    \    \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"togoM1645original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"BL Agar*\\\",\\n          \\\"volume\\\": 58,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465\"\
    \n      },\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n\
    \        \"source_locator\": \"Extracted text line 36\",\n        \"exact_source_quote\"\
    : \"*Nissui Pharmaceutical Co. Ltd., Tokyo, Japan.\",\n        \"snapshot_sha256\"\
    : \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\",\n    \
    \    \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"The source gives 58 g of an opaque commercial\
    \ product. Neither original source explicitly gives 58 g/L or measured final volume.\
    \ Preserve the batch amount and supplier, credit the owner for moving it out of\
    \ an empty solution wrapper, and do not invent the product composition.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q2\",\n    \"topic\": \"Blood: 50 ml batch addition\"\
    ,\n    \"decision\": \"correct\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"50\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Restore the liquid batch amount of 50 ml rather than a mass rate; no density\
    \ conversion is supported. The owner correctly changed the liquid dimension, but\
    \ ML_PER_L remains a nominal interpretation rather than an explicitly measured\
    \ final-volume rate.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50.0\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"Credit\
    \ the corrected liquid dimension and supported 50 ml batch dose. Its stored per-litre\
    \ denominator is not explicitly established; attach the literal dose and qualify\
    \ any nominal rate instead of claiming a measured final volume.\"\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc848\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Composition, blood row\",\n        \"exact_source_quote\"\
    : \"Defibrinated horse blood\\n50\\nml\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"togoM1645original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Defibrinated horse blood\\\",\\n          \\\"\
    volume\\\": 50,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465\"\n     \
    \ },\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n    \
    \    \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the liquid batch amount of 50\
    \ ml rather than a mass rate; no density conversion is supported. The owner correctly\
    \ changed the liquid dimension, but ML_PER_L remains a nominal interpretation\
    \ rather than an explicitly measured final-volume rate.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q3\",\n    \"topic\": \"Water: 950 ml batch input\",\n    \"decision\": \"\
    correct\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"950\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore the 950\
    \ ml water input instead of G_PER_L. The sum of listed blood and water inputs\
    \ is 1000 ml, but that sum is not an explicit measurement or makeup instruction\
    \ for the completed medium.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"950.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"The owner\
    \ correctly uses a liquid unit, but the literal source gives a 950 ml input, not\
    \ an independently measured ML_PER_L final-medium rate. Retain that batch scope.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Composition, water row\",\n        \"exact_source_quote\"\
    : \"Distilled water\\n950\\nml\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"togoM1645original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1645\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 950,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    b6a2b990af7905250874c1687dcbd44bc3cee5bec95e531093a59f07111b2465\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore the 950 ml water input instead of G_PER_L.\
    \ The sum of listed blood and water inputs is 1000 ml, but that sum is not an\
    \ explicit measurement or makeup instruction for the completed medium.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q4\",\n    \"topic\": \"Owner product and liquid\
    \ notes: unsupported per-litre wording\",\n    \"decision\": \"correct\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"NBRC\
    \ Medium 848 lists 58 g/L BL Agar and notes that the asterisk marks Nissui Pharmaceutical\
    \ Co. Ltd.; this commercial BL Agar product is retained as an opaque base/solidifying\
    \ component.\",\n        \"decision\": \"correct\",\n        \"rationale\": \"\
    The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC. The\
    \ captured page instead gives g, ml and 5% (final). Retain the valid amounts and\
    \ repair credit while distinguishing normalization assumptions from literal source\
    \ statements.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"NBRC\
    \ Medium 848 lists 50 ml/L sterile defibrinated horse blood added aseptically\
    \ to a final 5% v/v.\",\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"The owner notes attribute explicit g/L, ml/L and 5% v/v language to NBRC.\
    \ The captured page instead gives g, ml and 5% (final). Retain the valid amounts\
    \ and repair credit while distinguishing normalization assumptions from literal\
    \ source statements.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"NBRC\
    \ Medium 848 lists 950 ml/L distilled water.\",\n        \"decision\": \"correct\"\
    ,\n        \"rationale\": \"The owner notes attribute explicit g/L, ml/L and 5%\
    \ v/v language to NBRC. The captured page instead gives g, ml and 5% (final).\
    \ Retain the valid amounts and repair credit while distinguishing normalization\
    \ assumptions from literal source statements.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n    \
    \    \"source_locator\": \"Composition, BL Agar product row\",\n        \"exact_source_quote\"\
    : \"BL Agar*\\n58\\ng\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n\
    \        \"source_locator\": \"Composition, blood row\",\n        \"exact_source_quote\"\
    : \"Defibrinated horse blood\\n50\\nml\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n\
    \        \"source_locator\": \"Composition, water row\",\n        \"exact_source_quote\"\
    : \"Distilled water\\n950\\nml\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      },\n      {\n        \"source_key\": \"nbrc848\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\",\n\
    \        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"The owner notes attribute explicit g/L,\
    \ ml/L and 5% v/v language to NBRC. The captured page instead gives g, ml and\
    \ 5% (final). Retain the valid amounts and repair credit while distinguishing\
    \ normalization assumptions from literal source statements.\"\n  },\n  {\n   \
    \ \"quantity_id\": \"q5\",\n    \"topic\": \"Blood percentage basis: final 5%,\
    \ not explicitly v/v\",\n    \"decision\": \"correct\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Aseptically add sterile defibrinated horse blood to 5% v/v final and mix.\"\
    ,\n        \"decision\": \"correct\",\n        \"rationale\": \"Preserve final\
    \ 5% as the literal source wording and leave its basis unspecified. The listed\
    \ 50 ml dose plus 950 ml water motivates a nominal volume interpretation, but\
    \ does not make v/v an exact quotation or prove measured final volume.\"\n   \
    \   }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve final 5% as the literal source\
    \ wording and leave its basis unspecified. The listed 50 ml dose plus 950 ml water\
    \ motivates a nominal volume interpretation, but does not make v/v an exact quotation\
    \ or prove measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n\
    \    \"topic\": \"Cooling to about 50 C and staged blood addition\",\n    \"decision\"\
    : \"add\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Add the missing target\
    \ preparation while retaining the owner’s supported approximate cooling temperature.\
    \ Blood is excluded from autoclaving and added aseptically after cooling. This\
    \ is preparation temperature, not a growth temperature.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\",\n       \
    \ \"field_path\": \"preparation_steps[1].description\",\n        \"stored\": \"\
    Cool to about 50 C.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The existing cooling description agrees with the source approximate 50 C instruction.\
    \ Add exact claim linkage; do not convert it into an incubation condition.\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"Add the missing target preparation while\
    \ retaining the owner’s supported approximate cooling temperature. Blood is excluded\
    \ from autoclaving and added aseptically after cooling. This is preparation temperature,\
    \ not a growth temperature.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"\
    topic\": \"Autoclaving without blood; no explicit cycle\",\n    \"decision\":\
    \ \"add\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The source requires\
    \ autoclaving the base without blood but supplies no temperature or duration.\
    \ Add the scoped step to the target without inventing a cycle.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Autoclave the BL Agar base without horse blood.\",\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"The owner already has the supported\
    \ autoclave-without-blood step. Attach the exact source; no cycle is specified.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"The source requires autoclaving the base\
    \ without blood but supplies no temperature or duration. Add the scoped step to\
    \ the target without inventing a cycle.\"\n  },\n  {\n    \"quantity_id\": \"\
    q8\",\n    \"topic\": \"Rapid dispensing into tubes or Petri dishes\",\n    \"\
    decision\": \"add\",\n    \"layer_decisions\": [\n      {\n        \"input\":\
    \ \"target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Retain both\
    \ stated vessel choices after mixing; no dispensing volume is given. Carry the\
    \ owner’s supported preparation to the regenerated target.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bl_agar.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Quickly dispense into sterile test tubes or Petri dishes.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The owner already retains the source\
    \ dispensing instruction. Add its exact source claim without a guessed volume.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc848\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848\"\
    ,\n        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave except horse blood and cool to about 50℃. Aseptically add 5 % (final)\
    \ sterile defibrinated horse blood. Mix and quickly dispense into sterile test\
    \ tubes or petri dishes.\",\n        \"snapshot_sha256\": \"92a634068d6d1042e905a59c14688b57af69ac58ae962bfd93586dd9d9d5a594\"\
    ,\n        \"parsed_text_sha256\": \"6492bc2fe5b4741a60269e94f62b809c9260606fc31e361027cb77eb4b57ab48\"\
    \n      }\n    ],\n    \"rationale\": \"Retain both stated vessel choices after\
    \ mixing; no dispensing volume is given. Carry the owner’s supported preparation\
    \ to the regenerated target.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.008201.liquid-and-volume-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore literal liquid amounts and qualify final-volume rates
  description: The target stores 950 ml water and 50 ml blood as G_PER_L. The repaired
    owner fixes the liquid dimension but its per-litre notes and explicit v/v wording
    are stronger than the source.
  target_ids:
  - CultureMech:008201
  field_paths:
  - ingredients
  - solutions[0].concentration
  - preparation_steps
  evidence_ids:
  - main
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.008201.empty-commercial-stock
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Carry forward the existing opaque-product repair
  description: The target wraps BL Agar in an empty Unknown solution. The maintained
    owner already represents the Nissui product as an opaque ingredient and retains
    its supplier.
  target_ids:
  - CultureMech:008201
  field_paths:
  - solutions[0]
  evidence_ids:
  - record
  - owner-0
  - main
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.008201.preparation-and-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Carry forward supported preparation with exact source linkage
  description: The target omits the owner’s staged preparation and references. Literal
    batch amounts and preparation lack attached claim evidence; the owner’s 5% v/v
    description needs qualification.
  target_ids:
  - CultureMech:008201
  field_paths:
  - preparation_steps
  - references
  - ingredients
  evidence_ids:
  - main
  - provider
  - history-evidence
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Use exact batch amounts and source stages, retain final 5% with an
    unspecified basis, and distinguish any nominal normalization from a measured final-volume
    concentration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008201
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
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
  description: Preserve the owner’s commercial-product representation and supplier
    during authorized regeneration; do not fabricate a stock recipe or replace the
    product with another blood-agar formulation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008201
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
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
  description: Retain the existing source-supported steps and references, correct
    only unsupported basis wording, and attach exact scoped claims when curating the
    authoritative owner.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008201
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_agar.yaml
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
- The captured sources do not establish the proprietary Nissui product composition,
  an explicit percentage basis or a measured final medium volume.
- No pH, autoclave cycle or observed organism-growth claim is supplied by these recipe
  sources.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-044
- generated-medium
```
