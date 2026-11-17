# Source and formulation review: bacillus_acidocaldarius_medium (CultureMech:002203)

- Review: 20261021T211128Z-culturemech-002203-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:59:31Z
- Finished UTC: 2026-10-21T21:11:28Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The merged record combines the distinct DSMZ 1286 formulation and seven unresolved strain-labelled records with the JCM 101/DSMZ 13 base. Its seven direct amounts are nominal stock rates without the A/B boundaries retained by the repaired DSMZ 13 owner. Source-stage pH and preparation, standalone solution A water units, incomplete stock placeholders and historical evidence need bounded follow-up.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 373; batch 038 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-seven task batches contain 370 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 373 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002203 | data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml | generated | bacillus_acidocaldarius_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002203 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002203 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/373/strict.tsv |
| validate-terms | passed | True | CultureMech:002203 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002203 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002203 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm101 | unavailable | False | CultureMech:002203 | Preserved jcm101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadiveJ101 | unavailable | False | CultureMech:002203 | Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: dsmz13 | unavailable | False | CultureMech:002203 | Preserved dsmz13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: dsmz1286 | unavailable | False | CultureMech:002203 | Preserved dsmz1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadive13 | unavailable | False | CultureMech:002203 | Preserved mediadive13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadive1286 | unavailable | False | CultureMech:002203 | Preserved mediadive1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: solution17 | unavailable | False | CultureMech:002203 | Preserved solution17 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: solution18 | unavailable | False | CultureMech:002203 | Preserved solution18 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13 | unavailable | False | CultureMech:002203 | Preserved komodo13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_13609 | unavailable | False | CultureMech:002203 | Preserved komodo13_13609 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17974 | unavailable | False | CultureMech:002203 | Preserved komodo13_17974 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17975 | unavailable | False | CultureMech:002203 | Preserved komodo13_17975 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17978 | unavailable | False | CultureMech:002203 | Preserved komodo13_17978 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17979 | unavailable | False | CultureMech:002203 | Preserved komodo13_17979 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17980 | unavailable | False | CultureMech:002203 | Preserved komodo13_17980 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17981 | unavailable | False | CultureMech:002203 | Preserved komodo13_17981 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadiveJ101_network_retry | unavailable | False | CultureMech:002203 | Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadive13_network_retry | unavailable | False | CultureMech:002203 | Preserved mediadive13_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: mediadive1286_network_retry | unavailable | False | CultureMech:002203 | Preserved mediadive1286_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: solution17_network_retry | unavailable | False | CultureMech:002203 | Preserved solution17_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: solution18_network_retry | unavailable | False | CultureMech:002203 | Preserved solution18_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_13609_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_13609_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17974_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17974_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17975_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17975_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17978_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17978_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17979_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17979_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17980_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17980_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Exact source content access: komodo13_17981_network_retry | unavailable | True | CultureMech:002203 | Preserved komodo13_17981_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| Required historical medium and solution raw correspondence | unavailable | True | CultureMech:002203 | Exact cited historical raw responses for medium 13, medium 1286, solution 17 and solution 18 were not recovered in the documented bounded local searches. All 25 claims remain derivative-only; recovered primary PDFs are different source objects. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002203.

The four documented recipes completed; interpret the scope of each separately.

### Base accession, distinct DSMZ 1286 and seven unresolved variants

identity: concern. Targets: CultureMech:002203.

JCM 101 and DSMZ 13 agree on the A/B formulation. DSMZ 1286 is a distinct formula with pH 5.0–5.8 and optional agar. Seven catalogue-labelled variants have inaccessible exact details; their local equality cannot prove equivalence. All eleven owner identities and the two separate stock dependencies are retained.

### Maintained and generated boundaries

ownership: concern. Targets: CultureMech:002203.

The maintained DSMZ 13 owner already has two 0.5 L nominal stock additions, separate stock compositions and water, and full cycle/cooling prose. The target, JCM owner and KOMODO 13 owner still present seven stock rates as direct amounts. Seven named variants require their own source recovery; the repaired DSMZ owner must not be treated as flattened.

### Complete CHEBI, current secondary and provider identifier inventory

grounding: concern. Targets: CultureMech:002203.

152 CHEBI objects have matching nonobsolete labels; every asserted current mediaingredientmech_chebi_term key has a pinned MIM preferred-term row. Target primary and secondary linkage are each 6/7 (85.71%), not a correctness score. No current legacy MIM slot is asserted. 19 provider-namespace objects are inventoried separately; their exact API correspondence remains unavailable. Hydrates are directly supported; generic glucose is not a stereochemical contradiction.

### Stage-specific pH, separate sterilization and cooling

completeness: concern. Targets: CultureMech:002203.

Existing target/JCM prose already retains separate autoclaving and pH adjustment. The missing A/B representation loses which stock receives pH 3–4; 3.5 is an unmarked midpoint. Preserve JCM 121°C/15 min default and DSMZ-specific 50°C cooling with their source scopes. The DSMZ maintained owner already retains the full procedure. These temperatures are preparation, not growth.

### Composition, physical state and environmental/growth claims

scope: concern. Targets: CultureMech:002203.

Yeast extract supports a complex, chemically undefined base; mandatory base agar supports the selected solid branch. DSMZ 1286 permits optional solidification and is separately scoped. Provider Is Aerobic=false is a catalogue attribute, not experimental evidence of obligate anaerobiosis. No strain-labelled title or synonym establishes growth, taxonomy or a temperature phenotype. No new growth assertion is warranted.

### Historical and current source authentication

evidence: concern. Targets: CultureMech:002203.

All 25 attached API objects are retained as historical derivative claims. Current primary matches can support new claim-level evidence without retroactively authenticating unrecovered old API responses. Catalogue and failed detail responses cannot establish variant formulas.

### Full historical objects and timestamp shape

provenance: concern. Targets: CultureMech:002203.

103 events inspected across all local layers; 20 timestamp instances are malformed or timezone-naive. Preserve original claims and events, append later clarifications, and avoid causal assertions about historical writer behavior from current code.

### Relationship and graph scope

graph: concern. Targets: CultureMech:002203.

The target asserts source-duplicate relationships, not independently established recipe equivalence. All named local paths/IDs resolve; no external graph ingredient match or taxonomic growth assertion was established. The two provider stock IDs are source-specific links whose old exact raw joins remain unavailable.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002203.

34 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Yeast extract",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, Yeast extract row",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "Ammonium sulfate",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "0.4",
      "unit": "G_PER_L"
    },
    "source_amount": 0.2,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, Ammonium sulfate row",
        "exact_source_quote": "(NH4)2SO4 0.20 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Magnesium sulfate heptahydrate",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 0.5,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, Magnesium sulfate heptahydrate row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Calcium chloride dihydrate",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_amount": 0.25,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, Calcium chloride dihydrate row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.25 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Potassium dihydrogen phosphate",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "1.2",
      "unit": "G_PER_L"
    },
    "source_amount": 0.6,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, Potassium dihydrogen phosphate row",
        "exact_source_quote": "KH2PO4 0.60 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "Glucose",
    "field_path": "ingredients[5].concentration",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution B",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B, Glucose row",
        "exact_source_quote": "Glucose 1.00 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Agar",
    "field_path": "ingredients[6].concentration",
    "local": {
      "value": "40",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "g per stated stock batch",
    "source_stage": "Solution B",
    "primary_source_evidence_id": "dsm13",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B, Agar row",
        "exact_source_quote": "Agar 20.00 g",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The primary specifies 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The existing numeric stock rate agrees with the nominal primary batch basis. Its attached historical API object is derivative-only; attach current primary evidence with stock scope, preserving existing value/form and the distinction from measured volume."
      }
    ],
    "arithmetic_and_scope": "The primary specifies 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate or measured final volume. Restore the stock boundary in these flattened layers; do not change the repaired DSMZ owner to a flattened recipe."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Solution A listed water",
    "field_path": "solutions[0].composition[5].concentration",
    "local": null,
    "source_amount": 500,
    "source_unit": "mL listed water",
    "source_stage": "Solution A",
    "primary_source_evidence_id": "dsm13",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "Existing 0.5 L equals 500 mL listed water. Preserve the repaired stock boundary; current primary evidence does not authenticate the old API response."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "PERCENT_V_V"
        },
        "decision": "correct",
        "rationale": "Solution 17 stores 1000 PERCENT_V_V, incompatible with a 500 mL batch water amount; recover the original volume unit without inventing a percentage denominator."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "preparation_notes",
        "stored": "Adjust pH to 3.0 - 4.0.\n\nOriginal volume: 500 mL",
        "decision": "evidence_only",
        "rationale": "The existing Original volume: 500 mL note is nominal stock context; the primary explicitly lists 500 mL water, without a measured make-up volume."
      }
    ],
    "arithmetic_and_scope": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Solution A whole prepared stock combination",
    "field_path": "solutions[0].concentration",
    "local": null,
    "source_amount": null,
    "source_unit": "whole prepared stock; nominal 500 mL water basis",
    "source_stage": "Solution A into base medium",
    "primary_source_evidence_id": "jcm101",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Medium 101 final paragraph",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution A water",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "Existing 0.5 L stock addition is a nominal provider representation of the prepared batch. Retain its stock-only scope and historical limitation; primary wording supports combining the whole preparations rather than a measured aliquot."
      }
    ],
    "arithmetic_and_scope": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
  },
  {
    "quantity_id": "q10",
    "ingredient_or_context": "Solution B listed water",
    "field_path": "solutions[1].composition[2].concentration",
    "local": null,
    "source_amount": 500,
    "source_unit": "mL listed water",
    "source_stage": "Solution B",
    "primary_source_evidence_id": "dsm13",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B, water row",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "Existing 0.5 L equals 500 mL listed water. Preserve the repaired stock boundary; current primary evidence does not authenticate the old API response."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "Solution 18 already stores the correct 0.5 L water addition; attach the direct primary evidence without changing the amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml",
        "field_path": "preparation_notes",
        "stored": "Original volume: 500 mL",
        "decision": "evidence_only",
        "rationale": "The existing Original volume: 500 mL note is nominal stock context; the primary explicitly lists 500 mL water, without a measured make-up volume."
      }
    ],
    "arithmetic_and_scope": "Add the source water within the absent stock representation; 500 mL is a water addition, not an instruction to make up a measured final volume."
  },
  {
    "quantity_id": "q11",
    "ingredient_or_context": "Solution B whole prepared stock combination",
    "field_path": "solutions[1].concentration",
    "local": null,
    "source_amount": null,
    "source_unit": "whole prepared stock; nominal 500 mL water basis",
    "source_stage": "Solution B into base medium",
    "primary_source_evidence_id": "jcm101",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Medium 101 final paragraph",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      },
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, Solution B water",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add",
        "rationale": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "Existing 0.5 L stock addition is a nominal provider representation of the prepared batch. Retain its stock-only scope and historical limitation; primary wording supports combining the whole preparations rather than a measured aliquot."
      }
    ],
    "arithmetic_and_scope": "The sources say to combine the separately prepared stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce an independently measured 500 mL aliquot or final 1 L assertion."
  },
  {
    "quantity_id": "q12",
    "ingredient_or_context": "See source for composition placeholder",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Solution A metadata",
    "primary_source_evidence_id": "dsm13",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, named stock heading",
        "exact_source_quote": "Solution A:",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported",
        "rationale": "VARIABLE is an unquantified placeholder. The actual composition is separately present and reviewed; it does not represent another ingredient or dose. Resolve the incomplete-composition flag and placeholder after preserving provenance."
      }
    ],
    "arithmetic_and_scope": "VARIABLE is an unquantified placeholder. The actual composition is separately present and reviewed; it does not represent another ingredient or dose. Resolve the incomplete-composition flag and placeholder after preserving provenance."
  },
  {
    "quantity_id": "q13",
    "ingredient_or_context": "See source for composition placeholder",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Solution B metadata",
    "primary_source_evidence_id": "dsm13",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1, named stock heading",
        "exact_source_quote": "Solution B:",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported",
        "rationale": "VARIABLE is an unquantified placeholder. The actual composition is separately present and reviewed; it does not represent another ingredient or dose. Resolve the incomplete-composition flag and placeholder after preserving provenance."
      }
    ],
    "arithmetic_and_scope": "VARIABLE is an unquantified placeholder. The actual composition is separately present and reviewed; it does not represent another ingredient or dose. Resolve the incomplete-composition flag and placeholder after preserving provenance."
  },
  {
    "quantity_id": "q14",
    "ingredient_or_context": "Yeast extract in seven named variants",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q15",
    "ingredient_or_context": "Ammonium sulfate in seven named variants",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "0.4",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q16",
    "ingredient_or_context": "Magnesium sulfate heptahydrate in seven named variants",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q17",
    "ingredient_or_context": "Calcium chloride dihydrate in seven named variants",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q18",
    "ingredient_or_context": "Potassium dihydrogen phosphate in seven named variants",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "1.2",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q19",
    "ingredient_or_context": "Glucose in seven named variants",
    "field_path": "ingredients[5].concentration",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q20",
    "ingredient_or_context": "Agar in seven named variants",
    "field_path": "ingredients[6].concentration",
    "local": {
      "value": "40",
      "unit": "G_PER_L"
    },
    "source_amount": null,
    "source_unit": null,
    "source_stage": "Seven independent 13_strain source identities",
    "primary_source_evidence_id": "catalog",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 619; accession 13_13609",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609' &gt;13_13609&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 13609&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 620; accession 13_17974",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974' &gt;13_17974&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17974&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 621; accession 13_17975",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975' &gt;13_17975&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17975&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 622; accession 13_17978",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978' &gt;13_17978&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17978&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 623; accession 13_17979",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979' &gt;13_17979&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17979&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 624; accession 13_17980",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980' &gt;13_17980&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17980&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      },
      {
        "source_key": "komodoList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Raw HTML row 625; accession 13_17981",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981' &gt;13_17981&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;MEDIUM 13 MODIFIED FOR DSM 17981&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;null&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      },
      {
        "input": "data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
      }
    ],
    "arithmetic_and_scope": "Each local value equals the base stock-rate table, but exact variant details are unavailable. The catalogue authenticates accession/name only. Do not project base corrections onto these variants, infer equivalence, or invent their quantities."
  },
  {
    "quantity_id": "q21",
    "ingredient_or_context": "Glucose/fructose",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_amount": 0.5,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Glucose/fructose row",
        "exact_source_quote": "Glucose (or fructose) 0.50 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      },
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "MIX",
          "description": "Use either glucose or fructose."
        },
        "decision": "evidence_only",
        "rationale": "The source explicitly permits glucose or fructose; preserve this alternative within DSMZ 1286 only."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q22",
    "ingredient_or_context": "Yeast extract",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_amount": 0.05,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Yeast extract row",
        "exact_source_quote": "Yeast extract 0.05 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q23",
    "ingredient_or_context": "Magnesium sulfate heptahydrate",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_amount": 0.05,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Magnesium sulfate heptahydrate row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.05 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q24",
    "ingredient_or_context": "Calcium chloride dihydrate",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_amount": 0.02,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Calcium chloride dihydrate row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.02 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q25",
    "ingredient_or_context": "Potassium dihydrogen phosphate",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_amount": 0.1,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Potassium dihydrogen phosphate row",
        "exact_source_quote": "KH2PO4 0.10 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q26",
    "ingredient_or_context": "Ammonium sulfate",
    "field_path": "ingredients[5].concentration",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_amount": 0.1,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Ammonium sulfate row",
        "exact_source_quote": "(NH4)2SO4 0.10 g",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q27",
    "ingredient_or_context": "Optional agar",
    "field_path": "ingredients[6].concentration",
    "local": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "source_amount": 15,
    "source_unit": "g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1, Optional agar row",
        "exact_source_quote": "The medium may be solidified with 15 g/l agar.",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      },
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
      },
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "MIX",
          "description": "The medium may be solidified with 15 g/l agar. Adjust to pH 5.0 - 5.8."
        },
        "decision": "evidence_only",
        "rationale": "The 15 g/L agar is explicitly optional, already retained in owner prose; it does not establish equivalence with mandatory 20 g in base solution B."
      }
    ],
    "arithmetic_and_scope": "The maintained owner agrees numerically with its own primary formulation. Preserve its distinct recipe and optional solid branch. The listed 1000 mL water is not a measured final volume; historical API normalization remains separately unauthenticated."
  },
  {
    "quantity_id": "q28",
    "ingredient_or_context": "DSMZ 1286 water",
    "field_path": "ingredients",
    "local": [
      {
        "preferred_term": "Glucose",
        "term": {
          "id": "CHEBI:17234",
          "label": "glucose"
        },
        "concentration": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:17234",
          "label": "glucose"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"condition\": \"\",\n                        \"attribute\": \"\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.77531,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[0].concentration (Glucose) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "Yeast extract",
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[1].concentration (Yeast extract) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "MgSO4 x 7 H2O",
        "term": {
          "id": "CHEBI:31795",
          "label": "magnesium sulfate heptahydrate"
        },
        "concentration": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:31795",
          "label": "magnesium sulfate heptahydrate"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.20286,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "CaCl2 x 2 H2O",
        "term": {
          "id": "CHEBI:86158",
          "label": "calcium chloride dihydrate"
        },
        "concentration": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:86158",
          "label": "calcium chloride dihydrate"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.136041,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[3].concentration (CaCl2 x 2 H2O) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.02; check: 0.02 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.02 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "KH2PO4",
        "term": {
          "id": "CHEBI:63036",
          "label": "potassium dihydrogen phosphate"
        },
        "concentration": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:63036",
          "label": "potassium dihydrogen phosphate"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.734835,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "(NH4)2SO4",
        "term": {
          "id": "CHEBI:62946",
          "label": "ammonium sulfate"
        },
        "concentration": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:62946",
          "label": "ammonium sulfate"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.756773,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[5].concentration ((NH4)2SO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      },
      {
        "preferred_term": "Agar",
        "term": {
          "id": "CHEBI:2509",
          "label": "agar"
        },
        "concentration": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "notes": " (for solid medium)",
        "mediaingredientmech_chebi_term": {
          "id": "CHEBI:2509",
          "label": "agar"
        },
        "evidence": [
          {
            "reference": "https://mediadive.dsmz.de/rest/medium/1286",
            "supports": "SUPPORT",
            "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
            "explanation": "Concentration evidence for ingredients[6].concentration (Agar) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
          }
        ]
      }
    ],
    "source_amount": 1000,
    "source_unit": "mL listed water",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"condition\": \"\",\n                        \"attribute\": \"\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.77531,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Glucose) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (Yeast extract) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.20286,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.02",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.136041,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (CaCl2 x 2 H2O) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.02; check: 0.02 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.02 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.734835,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "(NH4)2SO4",
            "term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:62946",
              "label": "ammonium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.756773,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration ((NH4)2SO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "notes": " (for solid medium)",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1286",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Agar) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49."
              }
            ]
          }
        ],
        "decision": "add",
        "rationale": "The seven-ingredient owner lacks this explicit water row. Add source batch water without asserting a measured final litre."
      }
    ],
    "arithmetic_and_scope": "The seven-ingredient owner lacks this explicit water row. Add source batch water without asserting a measured final litre."
  },
  {
    "quantity_id": "q29",
    "ingredient_or_context": "DSMZ 1286 pH range",
    "field_path": "ph_range",
    "local": {
      "min": 5.0,
      "max": 5.8
    },
    "source_amount": [
      5.0,
      5.8
    ],
    "source_unit": "pH",
    "source_stage": "DSMZ 1286 only",
    "primary_source_evidence_id": "dsm1286",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "dsmz1286_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf",
        "source_locator": "Page 1 final sentence",
        "exact_source_quote": "Adjust to pH 5.0 – 5.8.",
        "snapshot_sha256": "a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c",
        "parsed_text_sha256": "dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2"
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 5.0,
          "max": 5.8
        },
        "decision": "evidence_only",
        "rationale": "Existing pH range is directly supported by its own primary; it must not become a synonym of base solution A pH 3–4."
      },
      {
        "input": "data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "MIX",
          "description": "The medium may be solidified with 15 g/l agar. Adjust to pH 5.0 - 5.8."
        },
        "decision": "evidence_only",
        "rationale": "Existing conditional agar and pH prose is supported within DSMZ 1286."
      }
    ],
    "arithmetic_and_scope": "Existing pH range is directly supported by its own primary; it must not become a synonym of base solution A pH 3–4."
  },
  {
    "quantity_id": "q30",
    "ingredient_or_context": "Solution A pH range",
    "field_path": "ph_value",
    "local": 3.5,
    "source_amount": [
      3.0,
      4.0
    ],
    "source_unit": "pH",
    "source_stage": "Solution A before separate sterilization",
    "primary_source_evidence_id": "jcm101",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Medium 101, following Solution A table",
        "exact_source_quote": "Adjust pH to 3.0-4.0.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 3.5,
        "decision": "correct",
        "rationale": "The source gives a range for solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed source setpoint or demonstrated final-medium pH."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 3.5,
        "decision": "correct",
        "rationale": "The source gives a range for solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed source setpoint or demonstrated final-medium pH."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 3.0,
          "max": 4.0
        },
        "decision": "correct",
        "rationale": "The values match the source range, but stock-A scope is missing. Restore that scope rather than infer a final-medium pH."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Adjust pH to 3.0 - 4.0.",
        "decision": "evidence_only",
        "rationale": "Existing note correctly retains solution-A range; preserve it within that stock."
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml",
        "field_path": "preparation_notes",
        "stored": "Adjust pH to 3.0 - 4.0.\n\nOriginal volume: 500 mL",
        "decision": "evidence_only",
        "rationale": "Existing note correctly retains solution-A range; preserve it within that stock."
      },
      {
        "input": "target",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "ADJUST_PH",
          "description": "Adjust pH to 3.0-4.0."
        },
        "decision": "correct",
        "rationale": "Existing pH instruction is present but lacks the corresponding represented solution A; attach it to the restored stock."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "ADJUST_PH",
          "description": "Adjust pH to 3.0-4.0."
        },
        "decision": "correct",
        "rationale": "Existing pH instruction is present but lacks the corresponding represented solution A; attach it to the restored stock."
      }
    ],
    "arithmetic_and_scope": "The source gives a range for solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed source setpoint or demonstrated final-medium pH."
  },
  {
    "quantity_id": "q31",
    "ingredient_or_context": "Separate-stock sterilization temperature",
    "field_path": "preparation_steps",
    "local": [
      {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 3.0-4.0."
      },
      {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave Solutions A and B separately, and mix aseptically."
      }
    ],
    "source_amount": 121,
    "source_unit": "°C",
    "source_stage": "A and B separately; cooling precedes their combination",
    "primary_source_evidence_id": "dsm13",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1 final preparation paragraph",
        "exact_source_quote": "Sterilize solution A and B separately at 121C for 15 min.",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Catalogue default applicable to medium 101",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "HEAT",
            "description": "Sterilize solution A and B separately at 121°C for 15 min. Cool to 50°C and then combine."
          }
        ],
        "decision": "evidence_only",
        "rationale": "The maintained DSMZ 13 owner already retains the full temperature, duration and cooling text. Add current primary evidence; do not describe its procedure as absent."
      }
    ],
    "arithmetic_and_scope": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
  },
  {
    "quantity_id": "q32",
    "ingredient_or_context": "Separate-stock sterilization duration",
    "field_path": "preparation_steps",
    "local": [
      {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 3.0-4.0."
      },
      {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave Solutions A and B separately, and mix aseptically."
      }
    ],
    "source_amount": 15,
    "source_unit": "min",
    "source_stage": "A and B separately; cooling precedes their combination",
    "primary_source_evidence_id": "dsm13",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1 final preparation paragraph",
        "exact_source_quote": "Sterilize solution A and B separately at 121C for 15 min.",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Catalogue default applicable to medium 101",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "HEAT",
            "description": "Sterilize solution A and B separately at 121°C for 15 min. Cool to 50°C and then combine."
          }
        ],
        "decision": "evidence_only",
        "rationale": "The maintained DSMZ 13 owner already retains the full temperature, duration and cooling text. Add current primary evidence; do not describe its procedure as absent."
      }
    ],
    "arithmetic_and_scope": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
  },
  {
    "quantity_id": "q33",
    "ingredient_or_context": "DSMZ cooling before combination",
    "field_path": "preparation_steps",
    "local": [
      {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 3.0-4.0."
      },
      {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave Solutions A and B separately, and mix aseptically."
      }
    ],
    "source_amount": 50,
    "source_unit": "°C",
    "source_stage": "A and B separately; cooling precedes their combination",
    "primary_source_evidence_id": "dsm13",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1 final preparation paragraph",
        "exact_source_quote": "Cool to 50C and then",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 3.0-4.0."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions A and B separately, and mix aseptically."
          }
        ],
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "HEAT",
            "description": "Sterilize solution A and B separately at 121°C for 15 min. Cool to 50°C and then combine."
          }
        ],
        "decision": "evidence_only",
        "rationale": "The maintained DSMZ 13 owner already retains the full temperature, duration and cooling text. Add current primary evidence; do not describe its procedure as absent."
      }
    ],
    "arithmetic_and_scope": "Retain this source-specific preparation context, not a growth condition. JCM explicitly supplies the 121°C/15 min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose already mentions separate sterilization but lacks these numeric details."
  },
  {
    "quantity_id": "q34",
    "ingredient_or_context": "Base combined final volume",
    "field_path": "solutions",
    "local": null,
    "source_amount": null,
    "source_unit": null,
    "source_stage": "After combining A and B",
    "primary_source_evidence_id": "jcm101",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "dsmz13_network_retry",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf",
        "source_locator": "Page 1 both water rows",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95",
        "parsed_text_sha256": "27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79"
      },
      {
        "source_key": "jcm101_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101",
        "source_locator": "Medium 101 final paragraph",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a",
        "parsed_text_sha256": "6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "not_quantified",
        "rationale": "The two 500 mL water additions sum nominally to 1000 mL before accounting for dissolved solids. Neither primary declares a measured final volume or make-up instruction. Retain exact batch masses and stock stages; do not invent a measured denominator."
      }
    ],
    "arithmetic_and_scope": "The two 500 mL water additions sum nominally to 1000 mL before accounting for dissolved solids. Neither primary declares a measured final volume or make-up instruction. Retain exact batch masses and stock stages; do not invent a measured denominator."
  }
]

## Findings

### f1: Distinct formulation and unresolved variants share one generated identity

blocker / open / confirmed; issue key: culturemech.002203.distinct-formulations-merged.

DSMZ 1286 differs in its ingredient amounts, pH 5.0–5.8, glucose/fructose option and optional agar. It is merged with base JCM 101/DSMZ 13 and seven strain-labelled records whose exact formulations remain unavailable. Current equal signatures and catalogue labels do not establish synonymy.

### f2: Base stock rates are exposed as whole-medium amounts

blocker / open / confirmed; issue key: culturemech.002203.base-stock-boundaries.

The target, JCM owner and KOMODO 13 owner store 2/.4/1/.5/1.2/2/40 g/L directly. Primaries instead list A masses 1/.2/.5/.25/.6 g and B masses 1/20 g, each with 500 mL water, followed by combination. These stored numbers are nominal stock rates. The maintained DSMZ 13 owner already correctly separates these stocks and must be preserved. Neither primary establishes a measured final volume.

### f3: pH midpoint and numeric preparation lack source-stage scope

major / open / confirmed; issue key: culturemech.002203.ph-and-preparation-stage.

The target/JCM scalar 3.5 is not the source-prescribed setpoint; 3–4 applies to solution A. Existing separate-autoclaving prose is present but incomplete numerically. JCM supplies the 121°C/15 min default; DSMZ 13 additionally specifies 50°C cooling before combining. The maintained DSMZ owner already retains these details.

### f4: Standalone solution A water is encoded as 1000 percent

major / open / confirmed; issue key: culturemech.002203.solution17-water-units.

Solution 17 composition[5] stores 1000 PERCENT_V_V, whereas both primaries list 500 mL water. This is a batch water amount, not a percentage or make-up-volume instruction. Solution 18 already stores 0.5 L and is not the same defect.

### f5: Historical API claims and variant equivalence remain unresolved

major / open / confirmed; issue key: culturemech.002203.historical-evidence-gap.

All 25 attached source objects are derivative-only because their exact old API raw responses remain unrecovered in the bounded search. Current primary PDFs support individual amounts and procedures but cannot authenticate different API payloads or inaccessible strain variants.

### f6: Two complete composition tables still carry variable ingredient placeholders

minor / open / confirmed; issue key: culturemech.002203.stock-placeholders.

Standalone solutions 17 and 18 each retain a VARIABLE See source for composition ingredient and incomplete-composition annotation despite separately represented composition. The placeholder is not another quantified ingredient.

### f7: Historical timestamps contain malformed or unzoned values

minor / open / confirmed; issue key: culturemech.002203.history-timestamps.

The full inventory records 20 malformed or timezone-naive timestamp instances, including KOMODO imports. These metadata defects do not by themselves negate scientific source content.

## Recommended Actions And Acceptance Checks

### a1

Separate the resolved DSMZ 1286 formulation from the base. Retain stable source identities and unresolved variant relationships pending exact variant evidence; do not apply base amount corrections to all seven variants.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore exact A/B batch composition and whole-preparation assembly in the three flattened base layers, retain existing repaired DSMZ stock scope, and attach literal primary evidence without assuming measured final-volume normalization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the source range on solution A and preserve numeric preparation with exact JCM/DSMZ scope, keeping growth conditions distinct and retaining the repaired DSMZ owner procedure.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Correct only the erroneous standalone solution 17 water quantity/unit with exact source support and batch scope; preserve solution 18 water and both maintained DSMZ stock water entries.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Retain historical assertions with explicit provenance limits, add separately dated primary evidence where directly supported, and recover exact variant/formulation sources before completing equivalence review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Reconcile placeholder and completeness metadata after verifying the represented composition, preserving old curation events and all explicit water/solute rows.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a7

Append a documented timestamp clarification only where provenance establishes the intended value; do not silently rewrite old events or invent timezones.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-4 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-5 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-6 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-7 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-8 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-9 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-10 | data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch038/373/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/373/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml:1:id: CultureMech:002203<br>./data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml:1:id: CultureMech:002203<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch038/source-preflight-bound/373/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 40 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dep17 | data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml; Whole composition, placeholder, preparation notes, attached evidence and history | context_only | Separate linked stock inspected in full; it is not an additional receiving-medium ingredient. |
| dep18 | data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml; Whole composition, placeholder, preparation notes, attached evidence and history | context_only | Separate linked stock inspected in full; it is not an additional receiving-medium ingredient. |
| dsm13 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf; Page 1, Solutions A/B and final preparation paragraph | supports | Exact original formulation: separate stocks, listed water additions and stage-specific pH/cycle/cooling; no independently measured final-volume statement. |
| jcm101 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101; Medium 101, complete A/B table, pH sentence and catalogue default sterilization | supports | JCM independently states the same batch amounts and separate autoclaving; its global default is 121°C for 15 min. |
| dsm1286 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf; Page 1, entire formula and optional agar/pH sentence | supports | DSMZ 1286 is a distinct formula with a glucose/fructose choice, substantially different amounts and pH 5.0–5.8. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact header and accession rows 13 and seven 13_strain identifiers | supports | Catalogue rows establish source identity and provider attributes only; no exact variant formulation or demonstrated growth is recovered. |
| jcm101-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101; Preserved exact public retrieval result | context_only | Preserved jcm101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadiveJ101-attempt | https://mediadive.dsmz.de/rest/medium/J101; Preserved exact public retrieval result | context_only | Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| dsmz13-attempt | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf; Preserved exact public retrieval result | context_only | Preserved dsmz13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| dsmz1286-attempt | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf; Preserved exact public retrieval result | context_only | Preserved dsmz1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadive13-attempt | https://mediadive.dsmz.de/rest/medium/13; Preserved exact public retrieval result | context_only | Preserved mediadive13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadive1286-attempt | https://mediadive.dsmz.de/rest/medium/1286; Preserved exact public retrieval result | context_only | Preserved mediadive1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| solution17-attempt | https://mediadive.dsmz.de/rest/solution/17; Preserved exact public retrieval result | context_only | Preserved solution17 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| solution18-attempt | https://mediadive.dsmz.de/rest/solution/18; Preserved exact public retrieval result | context_only | Preserved solution18 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13; Preserved exact public retrieval result | context_only | Preserved komodo13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_13609-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609; Preserved exact public retrieval result | context_only | Preserved komodo13_13609 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17974-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974; Preserved exact public retrieval result | context_only | Preserved komodo13_17974 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17975-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975; Preserved exact public retrieval result | context_only | Preserved komodo13_17975 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17978-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978; Preserved exact public retrieval result | context_only | Preserved komodo13_17978 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17979-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979; Preserved exact public retrieval result | context_only | Preserved komodo13_17979 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17980-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980; Preserved exact public retrieval result | context_only | Preserved komodo13_17980 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17981-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981; Preserved exact public retrieval result | context_only | Preserved komodo13_17981 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadiveJ101_network_retry-attempt | https://mediadive.dsmz.de/rest/medium/J101; Preserved exact public retrieval result | context_only | Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadive13_network_retry-attempt | https://mediadive.dsmz.de/rest/medium/13; Preserved exact public retrieval result | context_only | Preserved mediadive13_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| mediadive1286_network_retry-attempt | https://mediadive.dsmz.de/rest/medium/1286; Preserved exact public retrieval result | context_only | Preserved mediadive1286_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| solution17_network_retry-attempt | https://mediadive.dsmz.de/rest/solution/17; Preserved exact public retrieval result | context_only | Preserved solution17_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| solution18_network_retry-attempt | https://mediadive.dsmz.de/rest/solution/18; Preserved exact public retrieval result | context_only | Preserved solution18_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13; Preserved exact public retrieval result | context_only | Preserved komodo13_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_13609_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609; Preserved exact public retrieval result | context_only | Preserved komodo13_13609_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17974_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974; Preserved exact public retrieval result | context_only | Preserved komodo13_17974_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17975_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975; Preserved exact public retrieval result | context_only | Preserved komodo13_17975_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17978_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978; Preserved exact public retrieval result | context_only | Preserved komodo13_17978_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17979_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979; Preserved exact public retrieval result | context_only | Preserved komodo13_17979_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17980_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980; Preserved exact public retrieval result | context_only | Preserved komodo13_17980_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| komodo13_17981_network_retry-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981; Preserved exact public retrieval result | context_only | Preserved komodo13_17981_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact obo_id, label, definition, annotations and obsolete status | supports | Canonical metadata is checked for every asserted CHEBI object, independently from source-specific hydrate and provider-ID scope. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact preferred-term rows for asserted current mediaingredientmech_chebi_term keys | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| grounding-inventory | /private/tmp/culturemech-review-work-batch038/373/grounding-inventory.json; Complete named layers with exact field paths and original objects | context_only | Deterministic serialization of manually read scientific and historical fields; local metadata is not primary authentication. |
| history-inventory | /private/tmp/culturemech-review-work-batch038/373/history-inventory.json; Complete named layers with exact field paths and original objects | context_only | Deterministic serialization of manually read scientific and historical fields; local metadata is not primary authentication. |
| historical-source-context | /private/tmp/culturemech-review-work-batch038/source-preflight-bound/373/evidence-context-original.json; Historical report/plan comparisons, exact native-input paths, complete local-history objects and bounded raw-search results | context_only | Twenty-five historical API claims match retained local derivative evidence where recorded. Exact old medium 13/1286 and solution 17/18 raw responses remain unrecovered. Current DSMZ/JCM primaries independently support only their specifically stated facts. |
| local-variant_children | data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; variant_children | context_only | Exact current stable IDs and path-qualified owner relationships were read. All eleven owners resolve; equal local signatures do not establish source equivalence. |
| local-merged_from | data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml; merged_from | context_only | Exact current stable IDs and path-qualified owner relationships were read. All eleven owners resolve; equal local signatures do not establish source equivalence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch038/373/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Preserved jcm101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved dsmz13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved dsmz1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadive13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadive1286 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved solution17 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved solution18 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_13609 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17974 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17975 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17978 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17979 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17980 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17981 access attempt: DNS/name-resolution failure before an HTTP response (no HTTP status or response body captured). No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadive13_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved mediadive1286_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved solution17_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved solution18_network_retry access attempt: 503. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_13609_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17974_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17975_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17978_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17979_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17980_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- Preserved komodo13_17981_network_retry access attempt: 403. No usable exact formulation from this response; failed access is not proof of nonexistence. Variant detail is required for equivalence assessment; current base/stock API failures do not negate available primary recipes.
- The required scientific comparison is partial because exact strain-variant formulations and historical medium/solution API raw correspondence remain unavailable. Current primary base and DSMZ 1286 comparisons are completed within their stated scopes.
- No generic M142 transfer statement from the preparatory template applies to record 373. Only the named local stocks and source-specific base/DSMZ 1286 formulations are assessed.
- Canonical reference validation checked zero references. No experimental phenotype, growth temperature, exact final volume, supplier grade or chemical stereochemistry beyond explicit source statements is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T211128Z-culturemech-002203-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_acidocaldarius_medium (CultureMech:002203)'
started_at: '2026-10-21T20:59:31Z'
finished_at: '2026-10-21T21:11:28Z'
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
summary: The merged record combines the distinct DSMZ 1286 formulation and seven unresolved
  strain-labelled records with the JCM 101/DSMZ 13 base. Its seven direct amounts
  are nominal stock rates without the A/B boundaries retained by the repaired DSMZ
  13 owner. Source-stage pH and preparation, standalone solution A water units, incomplete
  stock placeholders and historical evidence need bounded follow-up.
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
  - path: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    sha256: b594afe75190d85f49bb29af81efbd16e4b84f31d332e1f481a8bd9167ea7284
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    sha256: 2630798ce1487eed195268e6d1e62ae26f5f042612d0ade3f74f976c0abb229e
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    sha256: 437ecfb9844ae9c00c65c0f7d1395852e0ce8115cacc86411bb0f1ba42f57545
    role: context
  - path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    sha256: 6302148d39581f7f35afdd342fdf182c5aee72aedbcb856cb7fed9c85d47e67b
    role: context
  - path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    sha256: 9ae7c306a9f44ffdac5954162ec8aaaa295bb696c6ea38ebfb048dff06a97e12
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    sha256: 037f9917d4415e298b16de046850d334bc48c99b2e62d5c0036b2942fe0ca215
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    sha256: 380856270bab12f397cbbd1a13bbf8f45c62a171cedec14ccd53b7695f51c77a
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    sha256: 3c1fa41e54c619ac52b4a2e92d9ec0e5aac332e3e3ff586757a2d75ded5408df
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    sha256: f78f4ba037d712161202709e38518d7e19985f25970d39fe612ac3b93c58ba54
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    sha256: 87e7fb1240318e464ed1fb3bbe1540836d1f21edc43651668933a2ee26ebcba8
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    sha256: 52b92f2c43d77f4410429c4ee48cfb5b069bb0397d93c7bc232a02b49f335017
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    sha256: b6e7ebf92dc65c755e416867a0905b4069418f610cca571d1e791cabc1d25880
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    sha256: f71978980c9e4b98b4bb3a963560fd4a062693f790dacb6e6806ee36417eb3e8
    role: context
  - path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
    sha256: 044d9d6cf29027756b36a541dd4254063216105923d0935608fd8f415d14294a
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
  - path: reports/ingredient_concentration_curation/20261007-dsmz13-stock-only/plan.json
    sha256: 01013f5341f9a51b8e2ea93b148a201f91da976dcd0fc71dce46723768c51013
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json
    sha256: 7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml.md
    sha256: 975a4ea7e828e1dc5b453b54f01286f436ed195a72c9dfba8e738cd6e712f4c6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_13609.yaml.md
    sha256: 5d11766bcff884e4d512e508d9007bf390ddea1cb3bcb23da17fdd703db4d39e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17974.yaml.md
    sha256: 5bb9ff1b1c28cb2c9953178c261d261c8030b8f2c1aaeda5b4ea8dccae92d6e5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17975.yaml.md
    sha256: 75be53f00dcb48b8cf4df22f9d30290e519a6f518305f5c87b7def02152c0633
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17978.yaml.md
    sha256: c78652bfc79d8ebdff5871eea1bb57855fd6aaece5f434fe9e3b69f4c255be9a
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17979.yaml.md
    sha256: a83d8da2ebbed932308c998d8a0e97f889c9ba31bcefbbcd03bf52cb350b3e15
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17980.yaml.md
    sha256: dddd38699e41373b0ea882e6a89cddb7c84f8260ebdcdcc6f67e47f2e1aeeebe
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_13_modified_for_dsm_17981.yaml.md
    sha256: b94e8c4a7efb3d4be8d929ad0ab3df6bb94dabd99363363b8190b98318cb70ee
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacillus_acidocaldarius_medium.yaml.md
    sha256: ff5bc378c8aa7bebcb1f01474eace56074cfb996f420d1beece10a3697c89da8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/bryocella_elongata_medium.yaml.md
    sha256: 90da6ae078a4daa691a343c280488b7f4408a43164fd4bebcdc10af6b73fa4c1
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/plan.json
    sha256: 2a664ea8af07a25caadaa3e00421ae8eaa883ddd3e42c83f5013b3bf303c789b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml.md
    sha256: 2f68fcc1f384f1d4c9c05854c034edc25668cd5bcb60ae40d7a90d2e1e12cbf2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/plan.json
    sha256: c1d7b6e777a4761b79c3781f469e9c0f12bad85d7972e397d35afe228bbf8078
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/records/bacterial/mediadive_17_Solution_A.yaml.md
    sha256: 1702cb5de505f317292527e61a9b3a7b803ee9aba7c773b517e1e6d7bc3e2d75
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/records/bacterial/mediadive_18_Solution_B.yaml.md
    sha256: 84f7cb52c3c34c6f61707d57e196f2672a44d0e7a6127488bd254d2b49982b3f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 373; batch 038 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-seven task batches
    contain 370 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 373 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002203
targets:
- target_id: CultureMech:002203
  path: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  label: bacillus_acidocaldarius_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch038/373/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/373/strict.tsv"
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002203
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
  - CultureMech:002203
- check_id: jcm101-source-access
  name: 'Exact source content access: jcm101'
  required: false
  status: unavailable
  summary: 'Preserved jcm101 access attempt: DNS/name-resolution failure before an
    HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - jcm101-attempt
- check_id: mediadiveJ101-source-access
  name: 'Exact source content access: mediadiveJ101'
  required: false
  status: unavailable
  summary: 'Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadiveJ101-attempt
- check_id: dsmz13-source-access
  name: 'Exact source content access: dsmz13'
  required: false
  status: unavailable
  summary: 'Preserved dsmz13 access attempt: DNS/name-resolution failure before an
    HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - dsmz13-attempt
- check_id: dsmz1286-source-access
  name: 'Exact source content access: dsmz1286'
  required: false
  status: unavailable
  summary: 'Preserved dsmz1286 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - dsmz1286-attempt
- check_id: mediadive13-source-access
  name: 'Exact source content access: mediadive13'
  required: false
  status: unavailable
  summary: 'Preserved mediadive13 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadive13-attempt
- check_id: mediadive1286-source-access
  name: 'Exact source content access: mediadive1286'
  required: false
  status: unavailable
  summary: 'Preserved mediadive1286 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadive1286-attempt
- check_id: solution17-source-access
  name: 'Exact source content access: solution17'
  required: false
  status: unavailable
  summary: 'Preserved solution17 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - solution17-attempt
- check_id: solution18-source-access
  name: 'Exact source content access: solution18'
  required: false
  status: unavailable
  summary: 'Preserved solution18 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - solution18-attempt
- check_id: komodo13-source-access
  name: 'Exact source content access: komodo13'
  required: false
  status: unavailable
  summary: 'Preserved komodo13 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13-attempt
- check_id: komodo13_13609-source-access
  name: 'Exact source content access: komodo13_13609'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_13609 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_13609-attempt
- check_id: komodo13_17974-source-access
  name: 'Exact source content access: komodo13_17974'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17974 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17974-attempt
- check_id: komodo13_17975-source-access
  name: 'Exact source content access: komodo13_17975'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17975 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17975-attempt
- check_id: komodo13_17978-source-access
  name: 'Exact source content access: komodo13_17978'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17978 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17978-attempt
- check_id: komodo13_17979-source-access
  name: 'Exact source content access: komodo13_17979'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17979 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17979-attempt
- check_id: komodo13_17980-source-access
  name: 'Exact source content access: komodo13_17980'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17980 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17980-attempt
- check_id: komodo13_17981-source-access
  name: 'Exact source content access: komodo13_17981'
  required: false
  status: unavailable
  summary: 'Preserved komodo13_17981 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17981-attempt
- check_id: mediadiveJ101_network_retry-source-access
  name: 'Exact source content access: mediadiveJ101_network_retry'
  required: false
  status: unavailable
  summary: 'Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadiveJ101_network_retry-attempt
- check_id: mediadive13_network_retry-source-access
  name: 'Exact source content access: mediadive13_network_retry'
  required: false
  status: unavailable
  summary: 'Preserved mediadive13_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadive13_network_retry-attempt
- check_id: mediadive1286_network_retry-source-access
  name: 'Exact source content access: mediadive1286_network_retry'
  required: false
  status: unavailable
  summary: 'Preserved mediadive1286_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - mediadive1286_network_retry-attempt
- check_id: solution17_network_retry-source-access
  name: 'Exact source content access: solution17_network_retry'
  required: false
  status: unavailable
  summary: 'Preserved solution17_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - solution17_network_retry-attempt
- check_id: solution18_network_retry-source-access
  name: 'Exact source content access: solution18_network_retry'
  required: false
  status: unavailable
  summary: 'Preserved solution18_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - solution18_network_retry-attempt
- check_id: komodo13_network_retry-source-access
  name: 'Exact source content access: komodo13_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_network_retry access attempt: 403. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_network_retry-attempt
- check_id: komodo13_13609_network_retry-source-access
  name: 'Exact source content access: komodo13_13609_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_13609_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_13609_network_retry-attempt
- check_id: komodo13_17974_network_retry-source-access
  name: 'Exact source content access: komodo13_17974_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17974_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17974_network_retry-attempt
- check_id: komodo13_17975_network_retry-source-access
  name: 'Exact source content access: komodo13_17975_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17975_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17975_network_retry-attempt
- check_id: komodo13_17978_network_retry-source-access
  name: 'Exact source content access: komodo13_17978_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17978_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17978_network_retry-attempt
- check_id: komodo13_17979_network_retry-source-access
  name: 'Exact source content access: komodo13_17979_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17979_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17979_network_retry-attempt
- check_id: komodo13_17980_network_retry-source-access
  name: 'Exact source content access: komodo13_17980_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17980_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17980_network_retry-attempt
- check_id: komodo13_17981_network_retry-source-access
  name: 'Exact source content access: komodo13_17981_network_retry'
  required: true
  status: unavailable
  summary: 'Preserved komodo13_17981_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - komodo13_17981_network_retry-attempt
- check_id: historical-api-authentication
  name: Required historical medium and solution raw correspondence
  required: true
  status: unavailable
  summary: Exact cited historical raw responses for medium 13, medium 1286, solution
    17 and solution 18 were not recovered in the documented bounded local searches.
    All 25 claims remain derivative-only; recovered primary PDFs are different source
    objects.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - historical-source-context
  - history-inventory
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-6
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-7
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-8
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-9
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-10
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:03.484498Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch038/373/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:04.783177Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/373/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:06.410043Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:07.883220Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:11:27Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml:1:id: CultureMech:002203

    ./data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml:1:id:
    CultureMech:002203

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/source-preflight-bound/373/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:11:27Z'
  support: supports
  summary: 40 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 6a21b6b0875a585a4c25c2164e9c10f7e05a8966bf4c100d10c3ff84a8764cc1
- evidence_id: dep17
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
  locator: Whole composition, placeholder, preparation notes, attached evidence and
    history
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Separate linked stock inspected in full; it is not an additional receiving-medium
    ingredient.
  snapshot_sha256: 037f9917d4415e298b16de046850d334bc48c99b2e62d5c0036b2942fe0ca215
- evidence_id: dep18
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
  locator: Whole composition, placeholder, preparation notes, attached evidence and
    history
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Separate linked stock inspected in full; it is not an additional receiving-medium
    ingredient.
  snapshot_sha256: 380856270bab12f397cbbd1a13bbf8f45c62a171cedec14ccd53b7695f51c77a
- evidence_id: dsm13
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf
  locator: Page 1, Solutions A/B and final preparation paragraph
  accessed_at: '2026-10-21T20:20:21.157620Z'
  support: supports
  summary: 'Exact original formulation: separate stocks, listed water additions and
    stage-specific pH/cycle/cooling; no independently measured final-volume statement.'
  quote: 'Solution A:'
  snapshot_sha256: 5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95
- evidence_id: jcm101
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101
  locator: Medium 101, complete A/B table, pH sentence and catalogue default sterilization
  accessed_at: '2026-10-21T20:20:20.876143Z'
  support: supports
  summary: JCM independently states the same batch amounts and separate autoclaving;
    its global default is 121°C for 15 min.
  quote: Autoclave Solutions A and B separately, and mix aseptically.
  snapshot_sha256: 1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a
- evidence_id: dsm1286
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf
  locator: Page 1, entire formula and optional agar/pH sentence
  accessed_at: '2026-10-21T20:20:21.438973Z'
  support: supports
  summary: DSMZ 1286 is a distinct formula with a glucose/fructose choice, substantially
    different amounts and pH 5.0–5.8.
  quote: The medium may be solidified with 15 g/l agar. Adjust to pH 5.0 – 5.8.
  snapshot_sha256: a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact header and accession rows 13 and seven 13_strain identifiers
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Catalogue rows establish source identity and provider attributes only;
    no exact variant formulation or demonstrated growth is recovered.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: jcm101-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:55.046665Z'
  support: context_only
  summary: 'Preserved jcm101 access attempt: DNS/name-resolution failure before an
    HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: mediadiveJ101-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J101
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.752089Z'
  support: context_only
  summary: 'Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: dsmz13-attempt
  kind: database
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.986561Z'
  support: context_only
  summary: 'Preserved dsmz13 access attempt: DNS/name-resolution failure before an
    HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: dsmz1286-attempt
  kind: database
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.986444Z'
  support: context_only
  summary: 'Preserved dsmz1286 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: mediadive13-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/13
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.692346Z'
  support: context_only
  summary: 'Preserved mediadive13 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: mediadive1286-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1286
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.692240Z'
  support: context_only
  summary: 'Preserved mediadive1286 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: solution17-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/17
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.809471Z'
  support: context_only
  summary: 'Preserved solution17 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: solution18-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/18
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.810865Z'
  support: context_only
  summary: 'Preserved solution18 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.509065Z'
  support: context_only
  summary: 'Preserved komodo13 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_13609-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.509139Z'
  support: context_only
  summary: 'Preserved komodo13_13609 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17974-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.574375Z'
  support: context_only
  summary: 'Preserved komodo13_17974 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17975-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.574483Z'
  support: context_only
  summary: 'Preserved komodo13_17975 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17978-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.574582Z'
  support: context_only
  summary: 'Preserved komodo13_17978 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17979-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.632116Z'
  support: context_only
  summary: 'Preserved komodo13_17979 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17980-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.632171Z'
  support: context_only
  summary: 'Preserved komodo13_17980 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: komodo13_17981-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:13:54.632232Z'
  support: context_only
  summary: 'Preserved komodo13_17981 access attempt: DNS/name-resolution failure before
    an HTTP response (no HTTP status or response body captured). No usable exact formulation
    from this response; failed access is not proof of nonexistence. Variant detail
    is required for equivalence assessment; current base/stock API failures do not
    negate available primary recipes.'
- evidence_id: mediadiveJ101_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J101
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:21.134426Z'
  support: context_only
  summary: 'Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive13_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/13
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:21.683685Z'
  support: context_only
  summary: 'Preserved mediadive13_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1286_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1286
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.033547Z'
  support: context_only
  summary: 'Preserved mediadive1286_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution17_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/17
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.211597Z'
  support: context_only
  summary: 'Preserved solution17_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution18_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/18
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.315948Z'
  support: context_only
  summary: 'Preserved solution18_network_retry access attempt: 503. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo13_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.598042Z'
  support: context_only
  summary: 'Preserved komodo13_network_retry access attempt: 403. No usable exact
    formulation from this response; failed access is not proof of nonexistence. Variant
    detail is required for equivalence assessment; current base/stock API failures
    do not negate available primary recipes.'
  snapshot_sha256: 4ef508fd8c8ff3e5091bf128f2af5065002ca482d27f0216138d6281fc10d803
- evidence_id: komodo13_13609_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.684907Z'
  support: context_only
  summary: 'Preserved komodo13_13609_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: 335f27adbc41b0bc5768cdab988dc220aa2628fff861146836df067db966f56c
- evidence_id: komodo13_17974_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.732381Z'
  support: context_only
  summary: 'Preserved komodo13_17974_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: c45ed257e2ed85d8d313509897a99912503866d1f50a059ce873ced1cf5fc291
- evidence_id: komodo13_17975_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.813553Z'
  support: context_only
  summary: 'Preserved komodo13_17975_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: 4d85b28b7f6f800a7c71df271f23fcfd14705da1fa9cb17fef13ef68759a2218
- evidence_id: komodo13_17978_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.842367Z'
  support: context_only
  summary: 'Preserved komodo13_17978_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: 6edc7ed3a29071ba0b48f3ec8f605625e473237b52e067f2e6334d93086cdcc9
- evidence_id: komodo13_17979_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.846871Z'
  support: context_only
  summary: 'Preserved komodo13_17979_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: 49a7cf4a413df0ec59bed7f97675d09e8cdb2079515f5e589705ad0122958253
- evidence_id: komodo13_17980_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.894716Z'
  support: context_only
  summary: 'Preserved komodo13_17980_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: 035bc8fb72fbb3bbce9d72914c30bd760fb1371565c39f73cefcf7e633e51b96
- evidence_id: komodo13_17981_network_retry-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:22.968857Z'
  support: context_only
  summary: 'Preserved komodo13_17981_network_retry access attempt: 403. No usable
    exact formulation from this response; failed access is not proof of nonexistence.
    Variant detail is required for equivalence assessment; current base/stock API
    failures do not negate available primary recipes.'
  snapshot_sha256: f24454ad3e6c5666f71092fc180fc9497ad4cb97cd4d940faae698fb812caa21
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact obo_id, label, definition, annotations and obsolete status
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: Canonical metadata is checked for every asserted CHEBI object, independently
    from source-specific hydrate and provider-ID scope.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact preferred-term rows for asserted current mediaingredientmech_chebi_term
    keys
  accessed_at: '2026-10-21T21:11:27Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label":
    "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/373/grounding-inventory.json
  locator: Complete named layers with exact field paths and original objects
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Deterministic serialization of manually read scientific and historical
    fields; local metadata is not primary authentication.
  snapshot_sha256: d7eec3db882787a7c7e5882eced40efa814d4ffab453db99c9ec10e16ab2cbc5
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/373/history-inventory.json
  locator: Complete named layers with exact field paths and original objects
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Deterministic serialization of manually read scientific and historical
    fields; local metadata is not primary authentication.
  snapshot_sha256: ec9b079381d367476016f745e001cadcc71cc47ed016441f924e3af93d4a36b3
- evidence_id: historical-source-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/source-preflight-bound/373/evidence-context-original.json
  locator: Historical report/plan comparisons, exact native-input paths, complete
    local-history objects and bounded raw-search results
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Twenty-five historical API claims match retained local derivative evidence
    where recorded. Exact old medium 13/1286 and solution 17/18 raw responses remain
    unrecovered. Current DSMZ/JCM primaries independently support only their specifically
    stated facts.
  snapshot_sha256: 95202fd9467cc6e058cb5de3ec6d69f146efcc4e47daf0b7c9e0c83d8ce9d264
- evidence_id: local-variant_children
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: variant_children
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Exact current stable IDs and path-qualified owner relationships were read.
    All eleven owners resolve; equal local signatures do not establish source equivalence.
- evidence_id: local-merged_from
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
  locator: merged_from
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Exact current stable IDs and path-qualified owner relationships were read.
    All eleven owners resolve; equal local signatures do not establish source equivalence.
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/373/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:11:27Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ff8686c8a77e1ac8e40960cf2737884694e58dc2d57e5ea99645517a6693e9f4
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Base accession, distinct DSMZ 1286 and seven unresolved variants
  outcome: concern
  summary: JCM 101 and DSMZ 13 agree on the A/B formulation. DSMZ 1286 is a distinct
    formula with pH 5.0–5.8 and optional agar. Seven catalogue-labelled variants have
    inaccessible exact details; their local equality cannot prove equivalence. All
    eleven owner identities and the two separate stock dependencies are retained.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - dsm13
  - jcm101
  - dsm1286
  - catalog
  - local-merged_from
  - local-variant_children
- assessment_id: ownership
  area: ownership
  topic: Maintained and generated boundaries
  outcome: concern
  summary: The maintained DSMZ 13 owner already has two 0.5 L nominal stock additions,
    separate stock compositions and water, and full cycle/cooling prose. The target,
    JCM owner and KOMODO 13 owner still present seven stock rates as direct amounts.
    Seven named variants require their own source recovery; the repaired DSMZ owner
    must not be treated as flattened.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  - owner-9
  - owner-10
  - dep17
  - dep18
- assessment_id: grounding
  area: grounding
  topic: Complete CHEBI, current secondary and provider identifier inventory
  outcome: concern
  summary: 152 CHEBI objects have matching nonobsolete labels; every asserted current
    mediaingredientmech_chebi_term key has a pinned MIM preferred-term row. Target
    primary and secondary linkage are each 6/7 (85.71%), not a correctness score.
    No current legacy MIM slot is asserted. 19 provider-namespace objects are inventoried
    separately; their exact API correspondence remains unavailable. Hydrates are directly
    supported; generic glucose is not a stereochemical contradiction.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - grounding-inventory
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
  - chebi31795
  - chebi62946
  - chebi63036
  - chebi86158
- assessment_id: preparation
  area: completeness
  topic: Stage-specific pH, separate sterilization and cooling
  outcome: concern
  summary: Existing target/JCM prose already retains separate autoclaving and pH adjustment.
    The missing A/B representation loses which stock receives pH 3–4; 3.5 is an unmarked
    midpoint. Preserve JCM 121°C/15 min default and DSMZ-specific 50°C cooling with
    their source scopes. The DSMZ maintained owner already retains the full procedure.
    These temperatures are preparation, not growth.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - jcm101
  - dsm13
- assessment_id: classification
  area: scope
  topic: Composition, physical state and environmental/growth claims
  outcome: concern
  summary: Yeast extract supports a complex, chemically undefined base; mandatory
    base agar supports the selected solid branch. DSMZ 1286 permits optional solidification
    and is separately scoped. Provider Is Aerobic=false is a catalogue attribute,
    not experimental evidence of obligate anaerobiosis. No strain-labelled title or
    synonym establishes growth, taxonomy or a temperature phenotype. No new growth
    assertion is warranted.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - catalog
  - dsm13
  - dsm1286
- assessment_id: evidence
  area: evidence
  topic: Historical and current source authentication
  outcome: concern
  summary: All 25 attached API objects are retained as historical derivative claims.
    Current primary matches can support new claim-level evidence without retroactively
    authenticating unrecovered old API responses. Catalogue and failed detail responses
    cannot establish variant formulas.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - history-inventory
  - historical-source-context
  - bound-source-integrity
- assessment_id: history
  area: provenance
  topic: Full historical objects and timestamp shape
  outcome: concern
  summary: 103 events inspected across all local layers; 20 timestamp instances are
    malformed or timezone-naive. Preserve original claims and events, append later
    clarifications, and avoid causal assertions about historical writer behavior from
    current code.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - history-inventory
- assessment_id: graph
  area: graph
  topic: Relationship and graph scope
  outcome: concern
  summary: The target asserts source-duplicate relationships, not independently established
    recipe equivalence. All named local paths/IDs resolve; no external graph ingredient
    match or taxonomic growth assertion was established. The two provider stock IDs
    are source-specific links whose old exact raw joins remain unavailable.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - local-variant_children
  - local-merged_from
  - grounding-inventory
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 34 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002203
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Yeast extract\",\n    \"field_path\": \"ingredients[0].concentration\",\n    \"\
    local\": {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n    },\n   \
    \ \"source_amount\": 1,\n    \"source_unit\": \"g per stated stock batch\",\n\
    \    \"source_stage\": \"Solution A\",\n    \"primary_source_evidence_id\": \"\
    dsm13\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\",\n        \"\
    source_locator\": \"Page 1, Solution A, Yeast extract row\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[0].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 1 g in Solution A with 500 mL listed water. Dividing by 0.5\
    \ L gives the stored nominal stock rate, not a direct receiving-medium rate or\
    \ measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].composition[0].concentration\",\n        \"\
    stored\": {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    The existing numeric stock rate agrees with the nominal primary batch basis. Its\
    \ attached historical API object is derivative-only; attach current primary evidence\
    \ with stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 1 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q2\"\
    ,\n    \"ingredient_or_context\": \"Ammonium sulfate\",\n    \"field_path\": \"\
    ingredients[1].concentration\",\n    \"local\": {\n      \"value\": \"0.4\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.2,\n    \"source_unit\"\
    : \"g per stated stock batch\",\n    \"source_stage\": \"Solution A\",\n    \"\
    primary_source_evidence_id\": \"dsm13\",\n    \"decision\": \"correct\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, Ammonium sulfate row\",\n\
    \        \"exact_source_quote\": \"(NH4)2SO4 0.20 g\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[1].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 0.2 g in Solution A with 500 mL listed water. Dividing by\
    \ 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate\
    \ or measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].composition[1].concentration\",\n        \"\
    stored\": {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"The existing numeric stock rate agrees with the nominal primary batch basis.\
    \ Its attached historical API object is derivative-only; attach current primary\
    \ evidence with stock scope, preserving existing value/form and the distinction\
    \ from measured volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 0.2 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q3\"\
    ,\n    \"ingredient_or_context\": \"Magnesium sulfate heptahydrate\",\n    \"\
    field_path\": \"ingredients[2].concentration\",\n    \"local\": {\n      \"value\"\
    : \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.5,\n \
    \   \"source_unit\": \"g per stated stock batch\",\n    \"source_stage\": \"Solution\
    \ A\",\n    \"primary_source_evidence_id\": \"dsm13\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, Magnesium sulfate heptahydrate\
    \ row\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"\
    snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 0.5 g in Solution A with 500 mL listed water. Dividing by\
    \ 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate\
    \ or measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].composition[2].concentration\",\n        \"\
    stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    The existing numeric stock rate agrees with the nominal primary batch basis. Its\
    \ attached historical API object is derivative-only; attach current primary evidence\
    \ with stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 0.5 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q4\"\
    ,\n    \"ingredient_or_context\": \"Calcium chloride dihydrate\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.25,\n    \"source_unit\"\
    : \"g per stated stock batch\",\n    \"source_stage\": \"Solution A\",\n    \"\
    primary_source_evidence_id\": \"dsm13\",\n    \"decision\": \"correct\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, Calcium chloride dihydrate\
    \ row\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.25 g\",\n        \"\
    snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[3].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 0.25 g in Solution A with 500 mL listed water. Dividing by\
    \ 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate\
    \ or measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].composition[3].concentration\",\n        \"\
    stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"The existing numeric stock rate agrees with the nominal primary batch basis.\
    \ Its attached historical API object is derivative-only; attach current primary\
    \ evidence with stock scope, preserving existing value/form and the distinction\
    \ from measured volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 0.25 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q5\"\
    ,\n    \"ingredient_or_context\": \"Potassium dihydrogen phosphate\",\n    \"\
    field_path\": \"ingredients[4].concentration\",\n    \"local\": {\n      \"value\"\
    : \"1.2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.6,\n\
    \    \"source_unit\": \"g per stated stock batch\",\n    \"source_stage\": \"\
    Solution A\",\n    \"primary_source_evidence_id\": \"dsm13\",\n    \"decision\"\
    : \"correct\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz13_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, Potassium dihydrogen phosphate\
    \ row\",\n        \"exact_source_quote\": \"KH2PO4 0.60 g\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[4].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 0.6 g in Solution A with 500 mL listed water. Dividing by\
    \ 0.5 L gives the stored nominal stock rate, not a direct receiving-medium rate\
    \ or measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].composition[4].concentration\",\n        \"\
    stored\": {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"The existing numeric stock rate agrees with the nominal primary batch basis.\
    \ Its attached historical API object is derivative-only; attach current primary\
    \ evidence with stock scope, preserving existing value/form and the distinction\
    \ from measured volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 0.6 g in Solution A with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q6\"\
    ,\n    \"ingredient_or_context\": \"Glucose\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": 1,\n    \"source_unit\": \"g per stated stock batch\"\
    ,\n    \"source_stage\": \"Solution B\",\n    \"primary_source_evidence_id\":\
    \ \"dsm13\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\",\n     \
    \   \"source_locator\": \"Page 1, Solution B, Glucose row\",\n        \"exact_source_quote\"\
    : \"Glucose 1.00 g\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution B, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[5].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 1 g in Solution B with 500 mL listed water. Dividing by 0.5\
    \ L gives the stored nominal stock rate, not a direct receiving-medium rate or\
    \ measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[1].composition[0].concentration\",\n        \"\
    stored\": {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    The existing numeric stock rate agrees with the nominal primary batch basis. Its\
    \ attached historical API object is derivative-only; attach current primary evidence\
    \ with stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 1 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q7\"\
    ,\n    \"ingredient_or_context\": \"Agar\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"40\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_amount\": 20,\n    \"source_unit\": \"g per stated stock\
    \ batch\",\n    \"source_stage\": \"Solution B\",\n    \"primary_source_evidence_id\"\
    : \"dsm13\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\",\n     \
    \   \"source_locator\": \"Page 1, Solution B, Agar row\",\n        \"exact_source_quote\"\
    : \"Agar 20.00 g\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution B, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[6].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ primary specifies 20 g in Solution B with 500 mL listed water. Dividing by 0.5\
    \ L gives the stored nominal stock rate, not a direct receiving-medium rate or\
    \ measured final volume. Restore the stock boundary in these flattened layers;\
    \ do not change the repaired DSMZ owner to a flattened recipe.\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The primary specifies\
    \ 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[1].composition[1].concentration\",\n        \"\
    stored\": {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    The existing numeric stock rate agrees with the nominal primary batch basis. Its\
    \ attached historical API object is derivative-only; attach current primary evidence\
    \ with stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The existing\
    \ numeric stock rate agrees with the nominal primary batch basis. Its attached\
    \ historical API object is derivative-only; attach current primary evidence with\
    \ stock scope, preserving existing value/form and the distinction from measured\
    \ volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The primary specifies\
    \ 20 g in Solution B with 500 mL listed water. Dividing by 0.5 L gives the stored\
    \ nominal stock rate, not a direct receiving-medium rate or measured final volume.\
    \ Restore the stock boundary in these flattened layers; do not change the repaired\
    \ DSMZ owner to a flattened recipe.\"\n  },\n  {\n    \"quantity_id\": \"q8\"\
    ,\n    \"ingredient_or_context\": \"Solution A listed water\",\n    \"field_path\"\
    : \"solutions[0].composition[5].concentration\",\n    \"local\": null,\n    \"\
    source_amount\": 500,\n    \"source_unit\": \"mL listed water\",\n    \"source_stage\"\
    : \"Solution A\",\n    \"primary_source_evidence_id\": \"dsm13\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A, water row\",\n        \"\
    exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].composition[5].concentration\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Existing 0.5 L equals 500 mL listed water. Preserve the repaired stock boundary;\
    \ current primary evidence does not authenticate the old API response.\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"PERCENT_V_V\"\n \
    \       },\n        \"decision\": \"correct\",\n        \"rationale\": \"Solution\
    \ 17 stores 1000 PERCENT_V_V, incompatible with a 500 mL batch water amount; recover\
    \ the original volume unit without inventing a percentage denominator.\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Adjust\
    \ pH to 3.0 - 4.0.\\n\\nOriginal volume: 500 mL\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The existing Original volume: 500 mL note is nominal\
    \ stock context; the primary explicitly lists 500 mL water, without a measured\
    \ make-up volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"Add the\
    \ source water within the absent stock representation; 500 mL is a water addition,\
    \ not an instruction to make up a measured final volume.\"\n  },\n  {\n    \"\
    quantity_id\": \"q9\",\n    \"ingredient_or_context\": \"Solution A whole prepared\
    \ stock combination\",\n    \"field_path\": \"solutions[0].concentration\",\n\
    \    \"local\": null,\n    \"source_amount\": null,\n    \"source_unit\": \"whole\
    \ prepared stock; nominal 500 mL water basis\",\n    \"source_stage\": \"Solution\
    \ A into base medium\",\n    \"primary_source_evidence_id\": \"jcm101\",\n   \
    \ \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm101_network_retry\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Medium 101 final paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave Solutions A and B separately, and mix aseptically.\",\n        \"\
    snapshot_sha256\": \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\"\
    ,\n        \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A water\",\n        \"exact_source_quote\"\
    : \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].concentration\",\n        \"\
    stored\": null,\n        \"decision\": \"add\",\n        \"rationale\": \"The\
    \ sources say to combine the separately prepared stocks. Preserve whole-batch\
    \ assembly and the 500 mL water basis; do not introduce an independently measured\
    \ 500 mL aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"The sources\
    \ say to combine the separately prepared stocks. Preserve whole-batch assembly\
    \ and the 500 mL water basis; do not introduce an independently measured 500 mL\
    \ aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"The sources\
    \ say to combine the separately prepared stocks. Preserve whole-batch assembly\
    \ and the 500 mL water basis; do not introduce an independently measured 500 mL\
    \ aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].concentration\",\n        \"stored\": {\n  \
    \        \"value\": \"0.5\",\n          \"unit\": \"L\"\n        },\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing 0.5 L stock\
    \ addition is a nominal provider representation of the prepared batch. Retain\
    \ its stock-only scope and historical limitation; primary wording supports combining\
    \ the whole preparations rather than a measured aliquot.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The sources say to combine the separately prepared\
    \ stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce\
    \ an independently measured 500 mL aliquot or final 1 L assertion.\"\n  },\n \
    \ {\n    \"quantity_id\": \"q10\",\n    \"ingredient_or_context\": \"Solution\
    \ B listed water\",\n    \"field_path\": \"solutions[1].composition[2].concentration\"\
    ,\n    \"local\": null,\n    \"source_amount\": 500,\n    \"source_unit\": \"\
    mL listed water\",\n    \"source_stage\": \"Solution B\",\n    \"primary_source_evidence_id\"\
    : \"dsm13\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\",\n        \"\
    source_locator\": \"Page 1, Solution B, water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition[2].concentration\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Add the source water within the absent stock representation; 500 mL is a water\
    \ addition, not an instruction to make up a measured final volume.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Existing 0.5 L equals 500 mL listed water. Preserve the repaired stock boundary;\
    \ current primary evidence does not authenticate the old API response.\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"Solution 18\
    \ already stores the correct 0.5 L water addition; attach the direct primary evidence\
    \ without changing the amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Original\
    \ volume: 500 mL\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The existing Original volume: 500 mL note is nominal stock context; the primary\
    \ explicitly lists 500 mL water, without a measured make-up volume.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"Add the source water within the absent\
    \ stock representation; 500 mL is a water addition, not an instruction to make\
    \ up a measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n  \
    \  \"ingredient_or_context\": \"Solution B whole prepared stock combination\"\
    ,\n    \"field_path\": \"solutions[1].concentration\",\n    \"local\": null,\n\
    \    \"source_amount\": null,\n    \"source_unit\": \"whole prepared stock; nominal\
    \ 500 mL water basis\",\n    \"source_stage\": \"Solution B into base medium\"\
    ,\n    \"primary_source_evidence_id\": \"jcm101\",\n    \"decision\": \"add\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm101_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Medium 101 final paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave Solutions A and B separately, and mix aseptically.\",\n        \"\
    snapshot_sha256\": \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\"\
    ,\n        \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      },\n      {\n        \"source_key\": \"dsmz13_network_retry\",\n     \
    \   \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution B water\",\n        \"exact_source_quote\"\
    : \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].concentration\",\n        \"\
    stored\": null,\n        \"decision\": \"add\",\n        \"rationale\": \"The\
    \ sources say to combine the separately prepared stocks. Preserve whole-batch\
    \ assembly and the 500 mL water basis; do not introduce an independently measured\
    \ 500 mL aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"The sources\
    \ say to combine the separately prepared stocks. Preserve whole-batch assembly\
    \ and the 500 mL water basis; do not introduce an independently measured 500 mL\
    \ aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"The sources\
    \ say to combine the separately prepared stocks. Preserve whole-batch assembly\
    \ and the 500 mL water basis; do not introduce an independently measured 500 mL\
    \ aliquot or final 1 L assertion.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[1].concentration\",\n        \"stored\": {\n  \
    \        \"value\": \"0.5\",\n          \"unit\": \"L\"\n        },\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing 0.5 L stock\
    \ addition is a nominal provider representation of the prepared batch. Retain\
    \ its stock-only scope and historical limitation; primary wording supports combining\
    \ the whole preparations rather than a measured aliquot.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"The sources say to combine the separately prepared\
    \ stocks. Preserve whole-batch assembly and the 500 mL water basis; do not introduce\
    \ an independently measured 500 mL aliquot or final 1 L assertion.\"\n  },\n \
    \ {\n    \"quantity_id\": \"q12\",\n    \"ingredient_or_context\": \"See source\
    \ for composition placeholder\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Solution A metadata\",\n    \"primary_source_evidence_id\": \"dsm13\",\n \
    \   \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, named stock heading\",\n        \"exact_source_quote\"\
    : \"Solution A:\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n        \"decision\"\
    : \"unsupported\",\n        \"rationale\": \"VARIABLE is an unquantified placeholder.\
    \ The actual composition is separately present and reviewed; it does not represent\
    \ another ingredient or dose. Resolve the incomplete-composition flag and placeholder\
    \ after preserving provenance.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"VARIABLE is an unquantified placeholder. The actual composition is separately\
    \ present and reviewed; it does not represent another ingredient or dose. Resolve\
    \ the incomplete-composition flag and placeholder after preserving provenance.\"\
    \n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"ingredient_or_context\": \"\
    See source for composition placeholder\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Solution B metadata\",\n    \"primary_source_evidence_id\": \"dsm13\",\n \
    \   \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1, named stock heading\",\n        \"exact_source_quote\"\
    : \"Solution B:\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n        \"decision\"\
    : \"unsupported\",\n        \"rationale\": \"VARIABLE is an unquantified placeholder.\
    \ The actual composition is separately present and reviewed; it does not represent\
    \ another ingredient or dose. Resolve the incomplete-composition flag and placeholder\
    \ after preserving provenance.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"VARIABLE is an unquantified placeholder. The actual composition is separately\
    \ present and reviewed; it does not represent another ingredient or dose. Resolve\
    \ the incomplete-composition flag and placeholder after preserving provenance.\"\
    \n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"ingredient_or_context\": \"\
    Yeast extract in seven named variants\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Seven independent 13_strain source identities\",\n    \"primary_source_evidence_id\"\
    : \"catalog\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"komodoList\",\n        \"source_url\": \"\
    https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q15\",\n    \"ingredient_or_context\": \"Ammonium sulfate in seven named variants\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"local\": {\n \
    \     \"value\": \"0.4\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : null,\n    \"source_unit\": null,\n    \"source_stage\": \"Seven independent\
    \ 13_strain source identities\",\n    \"primary_source_evidence_id\": \"catalog\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"komodoList\",\n        \"source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q16\",\n    \"ingredient_or_context\": \"Magnesium sulfate heptahydrate in\
    \ seven named variants\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Seven independent 13_strain source identities\",\n    \"primary_source_evidence_id\"\
    : \"catalog\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"komodoList\",\n        \"source_url\": \"\
    https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q17\",\n    \"ingredient_or_context\": \"Calcium chloride dihydrate in seven\
    \ named variants\",\n    \"field_path\": \"ingredients[3].concentration\",\n \
    \   \"local\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n   \
    \ },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Seven independent 13_strain source identities\",\n    \"primary_source_evidence_id\"\
    : \"catalog\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"komodoList\",\n        \"source_url\": \"\
    https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q18\",\n    \"ingredient_or_context\": \"Potassium dihydrogen phosphate in\
    \ seven named variants\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"1.2\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"Seven independent 13_strain source identities\",\n    \"primary_source_evidence_id\"\
    : \"catalog\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"komodoList\",\n        \"source_url\": \"\
    https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q19\",\n    \"ingredient_or_context\": \"Glucose in seven named variants\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"local\": {\n \
    \     \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : null,\n    \"source_unit\": null,\n    \"source_stage\": \"Seven independent\
    \ 13_strain source identities\",\n    \"primary_source_evidence_id\": \"catalog\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"komodoList\",\n        \"source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q20\",\n    \"ingredient_or_context\": \"Agar in seven named variants\",\n\
    \    \"field_path\": \"ingredients[6].concentration\",\n    \"local\": {\n   \
    \   \"value\": \"40\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : null,\n    \"source_unit\": null,\n    \"source_stage\": \"Seven independent\
    \ 13_strain source identities\",\n    \"primary_source_evidence_id\": \"catalog\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"komodoList\",\n        \"source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 619; accession 13_13609\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_13609'\
    \ >13_13609</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 13609</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 620; accession 13_17974\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17974'\
    \ >13_17974</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17974</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 621; accession 13_17975\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17975'\
    \ >13_17975</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17975</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 622; accession 13_17978\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17978'\
    \ >13_17978</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17978</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 623; accession 13_17979\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17979'\
    \ >13_17979</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17979</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 624; accession 13_17980\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17980'\
    \ >13_17980</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17980</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      },\n      {\n        \"source_key\": \"komodoList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Raw HTML row 625; accession 13_17981\",\n   \
    \     \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a\
    \ href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=13_17981'\
    \ >13_17981</a></TD>\\n\\t\\t\\t\\t\\t<TD>MEDIUM 13 MODIFIED FOR DSM 17981</TD>\\\
    n\\t\\t\\t\\t\\t<TD>null</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\\
    t<TD>false</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf</a></TD>\\n\\\
    t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Each local value\
    \ equals the base stock-rate table, but exact variant details are unavailable.\
    \ The catalogue authenticates accession/name only. Do not project base corrections\
    \ onto these variants, infer equivalence, or invent their quantities.\"\n    \
    \  }\n    ],\n    \"arithmetic_and_scope\": \"Each local value equals the base\
    \ stock-rate table, but exact variant details are unavailable. The catalogue authenticates\
    \ accession/name only. Do not project base corrections onto these variants, infer\
    \ equivalence, or invent their quantities.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q21\",\n    \"ingredient_or_context\": \"Glucose/fructose\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.5,\n    \"source_unit\"\
    : \"g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch\"\
    ,\n    \"source_stage\": \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\"\
    : \"dsm1286\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Glucose/fructose row\",\n        \"exact_source_quote\"\
    : \"Glucose (or fructose) 0.50 g\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"Use either glucose or fructose.\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The source explicitly permits glucose or fructose;\
    \ preserve this alternative within DSMZ 1286 only.\"\n      }\n    ],\n    \"\
    arithmetic_and_scope\": \"The maintained owner agrees numerically with its own\
    \ primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q22\"\
    ,\n    \"ingredient_or_context\": \"Yeast extract\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_amount\": 0.05,\n    \"source_unit\": \"g/L explicitly for\
    \ optional agar; otherwise g per listed 1000 mL water batch\",\n    \"source_stage\"\
    : \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\": \"dsm1286\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1286_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Yeast extract row\",\n        \"exact_source_quote\"\
    : \"Yeast extract 0.05 g\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      }\n    ],\n \
    \   \"arithmetic_and_scope\": \"The maintained owner agrees numerically with its\
    \ own primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q23\"\
    ,\n    \"ingredient_or_context\": \"Magnesium sulfate heptahydrate\",\n    \"\
    field_path\": \"ingredients[2].concentration\",\n    \"local\": {\n      \"value\"\
    : \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.05,\n\
    \    \"source_unit\": \"g/L explicitly for optional agar; otherwise g per listed\
    \ 1000 mL water batch\",\n    \"source_stage\": \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\"\
    : \"dsm1286\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Magnesium sulfate heptahydrate row\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.05 g\",\n        \"snapshot_sha256\"\
    : \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\",\n    \
    \    \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      }\n    ],\n \
    \   \"arithmetic_and_scope\": \"The maintained owner agrees numerically with its\
    \ own primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q24\"\
    ,\n    \"ingredient_or_context\": \"Calcium chloride dihydrate\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.02,\n    \"source_unit\"\
    : \"g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch\"\
    ,\n    \"source_stage\": \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\"\
    : \"dsm1286\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Calcium chloride dihydrate row\",\n \
    \       \"exact_source_quote\": \"CaCl2 x 2 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\",\n    \
    \    \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      }\n    ],\n \
    \   \"arithmetic_and_scope\": \"The maintained owner agrees numerically with its\
    \ own primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q25\"\
    ,\n    \"ingredient_or_context\": \"Potassium dihydrogen phosphate\",\n    \"\
    field_path\": \"ingredients[4].concentration\",\n    \"local\": {\n      \"value\"\
    : \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.1,\n\
    \    \"source_unit\": \"g/L explicitly for optional agar; otherwise g per listed\
    \ 1000 mL water batch\",\n    \"source_stage\": \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\"\
    : \"dsm1286\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Potassium dihydrogen phosphate row\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 0.10 g\",\n        \"snapshot_sha256\"\
    : \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\",\n    \
    \    \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      }\n    ],\n \
    \   \"arithmetic_and_scope\": \"The maintained owner agrees numerically with its\
    \ own primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q26\"\
    ,\n    \"ingredient_or_context\": \"Ammonium sulfate\",\n    \"field_path\": \"\
    ingredients[5].concentration\",\n    \"local\": {\n      \"value\": \"0.1\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 0.1,\n    \"source_unit\"\
    : \"g/L explicitly for optional agar; otherwise g per listed 1000 mL water batch\"\
    ,\n    \"source_stage\": \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\"\
    : \"dsm1286\",\n    \"decision\": \"evidence_only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Ammonium sulfate row\",\n        \"exact_source_quote\"\
    : \"(NH4)2SO4 0.10 g\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      }\n    ],\n \
    \   \"arithmetic_and_scope\": \"The maintained owner agrees numerically with its\
    \ own primary formulation. Preserve its distinct recipe and optional solid branch.\
    \ The listed 1000 mL water is not a measured final volume; historical API normalization\
    \ remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\": \"q27\"\
    ,\n    \"ingredient_or_context\": \"Optional agar\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"15\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_amount\": 15,\n    \"source_unit\": \"g/L explicitly for\
    \ optional agar; otherwise g per listed 1000 mL water batch\",\n    \"source_stage\"\
    : \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\": \"dsm1286\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1286_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Optional agar row\",\n        \"exact_source_quote\"\
    : \"The medium may be solidified with 15 g/l agar.\",\n        \"snapshot_sha256\"\
    : \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\",\n    \
    \    \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1286_network_retry\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n\
    \          \"step_number\": 2,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"The medium may be solidified with 15 g/l agar. Adjust to pH 5.0 - 5.8.\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"The 15 g/L agar is explicitly optional, already retained in owner prose; it\
    \ does not establish equivalence with mandatory 20 g in base solution B.\"\n \
    \     }\n    ],\n    \"arithmetic_and_scope\": \"The maintained owner agrees numerically\
    \ with its own primary formulation. Preserve its distinct recipe and optional\
    \ solid branch. The listed 1000 mL water is not a measured final volume; historical\
    \ API normalization remains separately unauthenticated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q28\",\n    \"ingredient_or_context\": \"DSMZ 1286 water\",\n    \"field_path\"\
    : \"ingredients\",\n    \"local\": [\n      {\n        \"preferred_term\": \"\
    Glucose\",\n        \"term\": {\n          \"id\": \"CHEBI:17234\",\n        \
    \  \"label\": \"glucose\"\n        },\n        \"concentration\": {\n        \
    \  \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"\
    mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:17234\",\n    \
    \      \"label\": \"glucose\"\n        },\n        \"evidence\": [\n         \
    \ {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"condition\\\": \\\"\\\",\\n               \
    \         \\\"attribute\\\": \\\"\\\",\\n                        \\\"amount\\\"\
    : 0.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.77531,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \        \"explanation\": \"Concentration evidence for ingredients[0].concentration\
    \ (Glucose) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[0]. Provider\
    \ explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L)\
    \ = 0.5 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"Yeast\
    \ extract\",\n        \"concentration\": {\n          \"value\": \"0.05\",\n \
    \         \"unit\": \"G_PER_L\"\n        },\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.05,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \        \"explanation\": \"Concentration evidence for ingredients[1].concentration\
    \ (Yeast extract) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"MgSO4\
    \ x 7 H2O\",\n        \"term\": {\n          \"id\": \"CHEBI:31795\",\n      \
    \    \"label\": \"magnesium sulfate heptahydrate\"\n        },\n        \"concentration\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:31795\"\
    ,\n          \"label\": \"magnesium sulfate heptahydrate\"\n        },\n     \
    \   \"evidence\": [\n          {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.05,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.20286,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n            \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive\
    \ medium 1286; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"CaCl2\
    \ x 2 H2O\",\n        \"term\": {\n          \"id\": \"CHEBI:86158\",\n      \
    \    \"label\": \"calcium chloride dihydrate\"\n        },\n        \"concentration\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:86158\"\
    ,\n          \"label\": \"calcium chloride dihydrate\"\n        },\n        \"\
    evidence\": [\n          {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.02,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.136041,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n            \"explanation\": \"\
    Concentration evidence for ingredients[3].concentration (CaCl2 x 2 H2O) in MediaDive\
    \ medium 1286; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports\
    \ g_l=0.02; check: 0.02 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.02 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"KH2PO4\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:63036\",\n          \"label\"\
    : \"potassium dihydrogen phosphate\"\n        },\n        \"concentration\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"mediaingredientmech_chebi_term\": {\n          \"id\": \"CHEBI:63036\"\
    ,\n          \"label\": \"potassium dihydrogen phosphate\"\n        },\n     \
    \   \"evidence\": [\n          {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n                \
    \        \\\"mmol_l\\\": 0.734835,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n            \"explanation\": \"Concentration evidence\
    \ for ingredients[4].concentration (KH2PO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[4].\
    \ Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"(NH4)2SO4\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:62946\",\n          \"label\"\
    : \"ammonium sulfate\"\n        },\n        \"concentration\": {\n          \"\
    value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"mediaingredientmech_chebi_term\"\
    : {\n          \"id\": \"CHEBI:62946\",\n          \"label\": \"ammonium sulfate\"\
    \n        },\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"https://mediadive.dsmz.de/rest/medium/1286\",\n            \"supports\": \"\
    SUPPORT\",\n            \"snippet\": \"{\\n                        \\\"recipe_order\\\
    \": 7,\\n                        \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n     \
    \                   \\\"compound_id\\\": 27,\\n                        \\\"amount\\\
    \": 0.1,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\": 0.756773,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \        \"explanation\": \"Concentration evidence for ingredients[5].concentration\
    \ ((NH4)2SO4) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[5].\
    \ Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      },\n      {\n        \"preferred_term\": \"Agar\"\
    ,\n        \"term\": {\n          \"id\": \"CHEBI:2509\",\n          \"label\"\
    : \"agar\"\n        },\n        \"concentration\": {\n          \"value\": \"\
    15\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"notes\": \" (for\
    \ solid medium)\",\n        \"mediaingredientmech_chebi_term\": {\n          \"\
    id\": \"CHEBI:2509\",\n          \"label\": \"agar\"\n        },\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n            \"supports\": \"SUPPORT\",\n            \"snippet\": \"{\\n   \
    \                     \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"condition\\\": \\\"for solid medium\\\",\\n     \
    \                   \\\"amount\\\": 15,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                   \
    \     \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n            \"explanation\": \"Concentration evidence\
    \ for ingredients[6].concentration (Agar) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[7].\
    \ Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 15 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_amount\": 1000,\n    \"\
    source_unit\": \"mL listed water\",\n    \"source_stage\": \"DSMZ 1286 only\"\
    ,\n    \"primary_source_evidence_id\": \"dsm1286\",\n    \"decision\": \"add\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1286_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ingredients\",\n        \"stored\": [\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.5\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n       \
    \     },\n            \"evidence\": [\n              {\n                \"reference\"\
    : \"https://mediadive.dsmz.de/rest/medium/1286\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 1,\\n                        \\\"compound\\\": \\\"Glucose\\\
    \",\\n                        \\\"compound_id\\\": 5,\\n                     \
    \   \\\"condition\\\": \\\"\\\",\\n                        \\\"attribute\\\":\
    \ \\\"\\\",\\n                        \\\"amount\\\": 0.5,\\n                \
    \        \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\\
    n                        \\\"mmol_l\\\": 2.77531,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[0].concentration (Glucose) in MediaDive\
    \ medium 1286; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports\
    \ g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"0.05\",\n              \"unit\": \"G_PER_L\"\n            },\n           \
    \ \"evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.05,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \            \"explanation\": \"Concentration evidence for ingredients[1].concentration\
    \ (Yeast extract) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:20:01.732437+00:00; response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.05\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.05,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.20286,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in\
    \ MediaDive medium 1286; locator=$.data.solutions[0].recipe[2]. Provider explicitly\
    \ reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.02\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.02,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.136041,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (CaCl2 x 2 H2O) in\
    \ MediaDive medium 1286; locator=$.data.solutions[0].recipe[3]. Provider explicitly\
    \ reports g_l=0.02; check: 0.02 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.02 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.734835,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive\
    \ medium 1286; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"(NH4)2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:62946\"\
    ,\n              \"label\": \"ammonium sulfate\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"0.1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:62946\",\n              \"label\": \"ammonium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 7,\\n                        \\\
    \"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.756773,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[5].concentration ((NH4)2SO4) in MediaDive\
    \ medium 1286; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports\
    \ g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \" (for solid medium)\",\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            },\n            \"evidence\": [\n\
    \              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1286\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 9,\\n                      \
    \  \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n                \"explanation\": \"Concentration evidence\
    \ for ingredients[6].concentration (Agar) in MediaDive medium 1286; locator=$.data.solutions[0].recipe[7].\
    \ Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 15 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:20:01.732437+00:00;\
    \ response SHA256=7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49.\"\
    \n              }\n            ]\n          }\n        ],\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"The seven-ingredient owner lacks this explicit\
    \ water row. Add source batch water without asserting a measured final litre.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"The seven-ingredient owner\
    \ lacks this explicit water row. Add source batch water without asserting a measured\
    \ final litre.\"\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"ingredient_or_context\"\
    : \"DSMZ 1286 pH range\",\n    \"field_path\": \"ph_range\",\n    \"local\": {\n\
    \      \"min\": 5.0,\n      \"max\": 5.8\n    },\n    \"source_amount\": [\n \
    \     5.0,\n      5.8\n    ],\n    \"source_unit\": \"pH\",\n    \"source_stage\"\
    : \"DSMZ 1286 only\",\n    \"primary_source_evidence_id\": \"dsm1286\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1286_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final sentence\",\n        \"exact_source_quote\"\
    : \"Adjust to pH 5.0 – 5.8.\",\n        \"snapshot_sha256\": \"a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c\"\
    ,\n        \"parsed_text_sha256\": \"dee4a747a0f88937d42f656cc560015bc49565aae5d6f7497a96cde7f16be1a2\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n        \"field_path\"\
    : \"ph_range\",\n        \"stored\": {\n          \"min\": 5.0,\n          \"\
    max\": 5.8\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Existing pH range is directly supported by its own primary; it must not become\
    \ a synonym of base solution A pH 3–4.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml\",\n       \
    \ \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n         \
    \ \"step_number\": 2,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"The medium may be solidified with 15 g/l agar. Adjust to pH 5.0 - 5.8.\"\n\
    \        },\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"Existing conditional agar and pH prose is supported within DSMZ 1286.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Existing pH range is directly\
    \ supported by its own primary; it must not become a synonym of base solution\
    \ A pH 3–4.\"\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"ingredient_or_context\"\
    : \"Solution A pH range\",\n    \"field_path\": \"ph_value\",\n    \"local\":\
    \ 3.5,\n    \"source_amount\": [\n      3.0,\n      4.0\n    ],\n    \"source_unit\"\
    : \"pH\",\n    \"source_stage\": \"Solution A before separate sterilization\"\
    ,\n    \"primary_source_evidence_id\": \"jcm101\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm101_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Medium 101, following Solution A table\",\n \
    \       \"exact_source_quote\": \"Adjust pH to 3.0-4.0.\",\n        \"snapshot_sha256\"\
    : \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\",\n    \
    \    \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ph_value\",\n        \"stored\": 3.5,\n \
    \       \"decision\": \"correct\",\n        \"rationale\": \"The source gives\
    \ a range for solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed\
    \ source setpoint or demonstrated final-medium pH.\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 3.5,\n        \"\
    decision\": \"correct\",\n        \"rationale\": \"The source gives a range for\
    \ solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed source setpoint\
    \ or demonstrated final-medium pH.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 3.0,\n          \"max\": 4.0\n        },\n        \"decision\": \"correct\"\
    ,\n        \"rationale\": \"The values match the source range, but stock-A scope\
    \ is missing. Restore that scope rather than infer a final-medium pH.\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Adjust pH to 3.0 - 4.0.\",\n        \"decision\": \"evidence_only\",\n   \
    \     \"rationale\": \"Existing note correctly retains solution-A range; preserve\
    \ it within that stock.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Adjust\
    \ pH to 3.0 - 4.0.\\n\\nOriginal volume: 500 mL\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Existing note correctly retains solution-A range;\
    \ preserve it within that stock.\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"ADJUST_PH\",\n       \
    \   \"description\": \"Adjust pH to 3.0-4.0.\"\n        },\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"Existing pH instruction is present but\
    \ lacks the corresponding represented solution A; attach it to the restored stock.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"ADJUST_PH\",\n       \
    \   \"description\": \"Adjust pH to 3.0-4.0.\"\n        },\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"Existing pH instruction is present but\
    \ lacks the corresponding represented solution A; attach it to the restored stock.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"The source gives a range for\
    \ solution A. Scalar 3.5 is an unmarked midpoint and not a prescribed source setpoint\
    \ or demonstrated final-medium pH.\"\n  },\n  {\n    \"quantity_id\": \"q31\"\
    ,\n    \"ingredient_or_context\": \"Separate-stock sterilization temperature\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"local\": [\n      {\n   \
    \     \"step_number\": 1,\n        \"action\": \"ADJUST_PH\",\n        \"description\"\
    : \"Adjust pH to 3.0-4.0.\"\n      },\n      {\n        \"step_number\": 2,\n\
    \        \"action\": \"AUTOCLAVE\",\n        \"description\": \"Autoclave Solutions\
    \ A and B separately, and mix aseptically.\"\n      }\n    ],\n    \"source_amount\"\
    : 121,\n    \"source_unit\": \"°C\",\n    \"source_stage\": \"A and B separately;\
    \ cooling precedes their combination\",\n    \"primary_source_evidence_id\": \"\
    dsm13\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"Sterilize solution A and B separately at 121C for\
    \ 15 min.\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"jcm101_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Catalogue default applicable to medium 101\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\"\
    ,\n        \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    ADJUST_PH\",\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"AUTOCLAVE\",\n            \"description\": \"Autoclave Solutions A and B separately,\
    \ and mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\"\
    ,\n        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"ADJUST_PH\"\
    ,\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n          },\n    \
    \      {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave Solutions A and B separately, and\
    \ mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Retain this source-specific\
    \ preparation context, not a growth condition. JCM explicitly supplies the 121°C/15\
    \ min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing\
    \ target/JCM prose already mentions separate sterilization but lacks these numeric\
    \ details.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"HEAT\",\n\
    \            \"description\": \"Sterilize solution A and B separately at 121°C\
    \ for 15 min. Cool to 50°C and then combine.\"\n          }\n        ],\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"The maintained\
    \ DSMZ 13 owner already retains the full temperature, duration and cooling text.\
    \ Add current primary evidence; do not describe its procedure as absent.\"\n \
    \     }\n    ],\n    \"arithmetic_and_scope\": \"Retain this source-specific preparation\
    \ context, not a growth condition. JCM explicitly supplies the 121°C/15 min default\
    \ and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM\
    \ prose already mentions separate sterilization but lacks these numeric details.\"\
    \n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"ingredient_or_context\": \"\
    Separate-stock sterilization duration\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"action\"\
    : \"ADJUST_PH\",\n        \"description\": \"Adjust pH to 3.0-4.0.\"\n      },\n\
    \      {\n        \"step_number\": 2,\n        \"action\": \"AUTOCLAVE\",\n  \
    \      \"description\": \"Autoclave Solutions A and B separately, and mix aseptically.\"\
    \n      }\n    ],\n    \"source_amount\": 15,\n    \"source_unit\": \"min\",\n\
    \    \"source_stage\": \"A and B separately; cooling precedes their combination\"\
    ,\n    \"primary_source_evidence_id\": \"dsm13\",\n    \"decision\": \"add\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"Sterilize solution A and B separately at 121C for\
    \ 15 min.\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"jcm101_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Catalogue default applicable to medium 101\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\"\
    ,\n        \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    ADJUST_PH\",\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"AUTOCLAVE\",\n            \"description\": \"Autoclave Solutions A and B separately,\
    \ and mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\"\
    ,\n        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"ADJUST_PH\"\
    ,\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n          },\n    \
    \      {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave Solutions A and B separately, and\
    \ mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Retain this source-specific\
    \ preparation context, not a growth condition. JCM explicitly supplies the 121°C/15\
    \ min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing\
    \ target/JCM prose already mentions separate sterilization but lacks these numeric\
    \ details.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"HEAT\",\n\
    \            \"description\": \"Sterilize solution A and B separately at 121°C\
    \ for 15 min. Cool to 50°C and then combine.\"\n          }\n        ],\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"The maintained\
    \ DSMZ 13 owner already retains the full temperature, duration and cooling text.\
    \ Add current primary evidence; do not describe its procedure as absent.\"\n \
    \     }\n    ],\n    \"arithmetic_and_scope\": \"Retain this source-specific preparation\
    \ context, not a growth condition. JCM explicitly supplies the 121°C/15 min default\
    \ and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM\
    \ prose already mentions separate sterilization but lacks these numeric details.\"\
    \n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"ingredient_or_context\": \"\
    DSMZ cooling before combination\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"action\"\
    : \"ADJUST_PH\",\n        \"description\": \"Adjust pH to 3.0-4.0.\"\n      },\n\
    \      {\n        \"step_number\": 2,\n        \"action\": \"AUTOCLAVE\",\n  \
    \      \"description\": \"Autoclave Solutions A and B separately, and mix aseptically.\"\
    \n      }\n    ],\n    \"source_amount\": 50,\n    \"source_unit\": \"°C\",\n\
    \    \"source_stage\": \"A and B separately; cooling precedes their combination\"\
    ,\n    \"primary_source_evidence_id\": \"dsm13\",\n    \"decision\": \"add\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz13_network_retry\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"Cool to 50C and then\",\n        \"snapshot_sha256\"\
    : \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\",\n    \
    \    \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    ADJUST_PH\",\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"AUTOCLAVE\",\n            \"description\": \"Autoclave Solutions A and B separately,\
    \ and mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\"\
    ,\n        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"ADJUST_PH\"\
    ,\n            \"description\": \"Adjust pH to 3.0-4.0.\"\n          },\n    \
    \      {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave Solutions A and B separately, and\
    \ mix aseptically.\"\n          }\n        ],\n        \"decision\": \"add\",\n\
    \        \"rationale\": \"Retain this source-specific preparation context, not\
    \ a growth condition. JCM explicitly supplies the 121°C/15 min default and separate\
    \ autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM prose\
    \ already mentions separate sterilization but lacks these numeric details.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Retain this source-specific\
    \ preparation context, not a growth condition. JCM explicitly supplies the 121°C/15\
    \ min default and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing\
    \ target/JCM prose already mentions separate sterilization but lacks these numeric\
    \ details.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"HEAT\",\n\
    \            \"description\": \"Sterilize solution A and B separately at 121°C\
    \ for 15 min. Cool to 50°C and then combine.\"\n          }\n        ],\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"The maintained\
    \ DSMZ 13 owner already retains the full temperature, duration and cooling text.\
    \ Add current primary evidence; do not describe its procedure as absent.\"\n \
    \     }\n    ],\n    \"arithmetic_and_scope\": \"Retain this source-specific preparation\
    \ context, not a growth condition. JCM explicitly supplies the 121°C/15 min default\
    \ and separate autoclaving; 50°C cooling is explicit in DSMZ 13. Existing target/JCM\
    \ prose already mentions separate sterilization but lacks these numeric details.\"\
    \n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"ingredient_or_context\": \"\
    Base combined final volume\",\n    \"field_path\": \"solutions\",\n    \"local\"\
    : null,\n    \"source_amount\": null,\n    \"source_unit\": null,\n    \"source_stage\"\
    : \"After combining A and B\",\n    \"primary_source_evidence_id\": \"jcm101\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz13_network_retry\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf\",\n        \"\
    source_locator\": \"Page 1 both water rows\",\n        \"exact_source_quote\"\
    : \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\": \"5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95\"\
    ,\n        \"parsed_text_sha256\": \"27627d070326deadc20fc179755eb39a100c0ae590b410996399ab392f185a79\"\
    \n      },\n      {\n        \"source_key\": \"jcm101_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101\"\
    ,\n        \"source_locator\": \"Medium 101 final paragraph\",\n        \"exact_source_quote\"\
    : \"Autoclave Solutions A and B separately, and mix aseptically.\",\n        \"\
    snapshot_sha256\": \"1e3d96577c32265f3f0573ea5530eb8ec1659ca26d9565a631d1efefbcfb409a\"\
    ,\n        \"parsed_text_sha256\": \"6d71e4391d987e24f9a063b389f2a0042fceaae1a8887ae14ce0377072cc9d88\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"The two 500\
    \ mL water additions sum nominally to 1000 mL before accounting for dissolved\
    \ solids. Neither primary declares a measured final volume or make-up instruction.\
    \ Retain exact batch masses and stock stages; do not invent a measured denominator.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"The two 500 mL water additions\
    \ sum nominally to 1000 mL before accounting for dissolved solids. Neither primary\
    \ declares a measured final volume or make-up instruction. Retain exact batch\
    \ masses and stock stages; do not invent a measured denominator.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.002203.distinct-formulations-merged
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Distinct formulation and unresolved variants share one generated identity
  description: DSMZ 1286 differs in its ingredient amounts, pH 5.0–5.8, glucose/fructose
    option and optional agar. It is merged with base JCM 101/DSMZ 13 and seven strain-labelled
    records whose exact formulations remain unavailable. Current equal signatures
    and catalogue labels do not establish synonymy.
  target_ids:
  - CultureMech:002203
  field_paths:
  - merged_from
  - synonyms
  - variant_children
  evidence_ids:
  - record
  - dsm13
  - dsm1286
  - catalog
  - local-merged_from
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
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
  issue_key: culturemech.002203.base-stock-boundaries
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Base stock rates are exposed as whole-medium amounts
  description: The target, JCM owner and KOMODO 13 owner store 2/.4/1/.5/1.2/2/40
    g/L directly. Primaries instead list A masses 1/.2/.5/.25/.6 g and B masses 1/20
    g, each with 500 mL water, followed by combination. These stored numbers are nominal
    stock rates. The maintained DSMZ 13 owner already correctly separates these stocks
    and must be preserved. Neither primary establishes a measured final volume.
  target_ids:
  - CultureMech:002203
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - jcm101
  - dsm13
  - owner-2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.002203.ph-and-preparation-stage
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: pH midpoint and numeric preparation lack source-stage scope
  description: The target/JCM scalar 3.5 is not the source-prescribed setpoint; 3–4
    applies to solution A. Existing separate-autoclaving prose is present but incomplete
    numerically. JCM supplies the 121°C/15 min default; DSMZ 13 additionally specifies
    50°C cooling before combining. The maintained DSMZ owner already retains these
    details.
  target_ids:
  - CultureMech:002203
  field_paths:
  - ph_value
  - ph_range
  - preparation_steps
  evidence_ids:
  - record
  - jcm101
  - dsm13
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
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
  issue_key: culturemech.002203.solution17-water-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Standalone solution A water is encoded as 1000 percent
  description: Solution 17 composition[5] stores 1000 PERCENT_V_V, whereas both primaries
    list 500 mL water. This is a batch water amount, not a percentage or make-up-volume
    instruction. Solution 18 already stores 0.5 L and is not the same defect.
  target_ids:
  - CultureMech:002203
  field_paths:
  - composition[5].concentration
  evidence_ids:
  - dep17
  - dep18
  - dsm13
  - jcm101
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.002203.historical-evidence-gap
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Historical API claims and variant equivalence remain unresolved
  description: All 25 attached source objects are derivative-only because their exact
    old API raw responses remain unrecovered in the bounded search. Current primary
    PDFs support individual amounts and procedures but cannot authenticate different
    API payloads or inaccessible strain variants.
  target_ids:
  - CultureMech:002203
  field_paths:
  - ingredients
  - solutions
  - variant_children
  evidence_ids:
  - history-inventory
  - historical-source-context
  - catalog
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.002203.stock-placeholders
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Two complete composition tables still carry variable ingredient placeholders
  description: Standalone solutions 17 and 18 each retain a VARIABLE See source for
    composition ingredient and incomplete-composition annotation despite separately
    represented composition. The placeholder is not another quantified ingredient.
  target_ids:
  - CultureMech:002203
  field_paths:
  - ingredients[0]
  - data_quality_flags
  evidence_ids:
  - dep17
  - dep18
  - dsm13
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f7
  issue_key: culturemech.002203.history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamps contain malformed or unzoned values
  description: The full inventory records 20 malformed or timezone-naive timestamp
    instances, including KOMODO imports. These metadata defects do not by themselves
    negate scientific source content.
  target_ids:
  - CultureMech:002203
  field_paths:
  - curation_history
  evidence_ids:
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Separate the resolved DSMZ 1286 formulation from the base. Retain stable
    source identities and unresolved variant relationships pending exact variant evidence;
    do not apply base amount corrections to all seven variants.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
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
  description: Restore exact A/B batch composition and whole-preparation assembly
    in the three flattened base layers, retain existing repaired DSMZ stock scope,
    and attach literal primary evidence without assuming measured final-volume normalization.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
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
  description: Represent the source range on solution A and preserve numeric preparation
    with exact JCM/DSMZ scope, keeping growth conditions distinct and retaining the
    repaired DSMZ owner procedure.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
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
  description: Correct only the erroneous standalone solution 17 water quantity/unit
    with exact source support and batch scope; preserve solution 18 water and both
    maintained DSMZ stock water entries.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
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
  description: Retain historical assertions with explicit provenance limits, add separately
    dated primary evidence where directly supported, and recover exact variant/formulation
    sources before completing equivalence review.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
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
  description: Reconcile placeholder and completeness metadata after verifying the
    represented composition, preserving old curation events and all explicit water/solute
    rows.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
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
  description: Append a documented timestamp clarification only where provenance establishes
    the intended value; do not silently rewrite old events or invent timezones.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:002203
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_17_Solution_A.yaml
    role: maintained stock dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_18_Solution_B.yaml
    role: maintained stock dependency
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
- 'Preserved jcm101 access attempt: DNS/name-resolution failure before an HTTP response
  (no HTTP status or response body captured). No usable exact formulation from this
  response; failed access is not proof of nonexistence. Variant detail is required
  for equivalence assessment; current base/stock API failures do not negate available
  primary recipes.'
- 'Preserved mediadiveJ101 access attempt: DNS/name-resolution failure before an HTTP
  response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved dsmz13 access attempt: DNS/name-resolution failure before an HTTP response
  (no HTTP status or response body captured). No usable exact formulation from this
  response; failed access is not proof of nonexistence. Variant detail is required
  for equivalence assessment; current base/stock API failures do not negate available
  primary recipes.'
- 'Preserved dsmz1286 access attempt: DNS/name-resolution failure before an HTTP response
  (no HTTP status or response body captured). No usable exact formulation from this
  response; failed access is not proof of nonexistence. Variant detail is required
  for equivalence assessment; current base/stock API failures do not negate available
  primary recipes.'
- 'Preserved mediadive13 access attempt: DNS/name-resolution failure before an HTTP
  response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved mediadive1286 access attempt: DNS/name-resolution failure before an HTTP
  response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved solution17 access attempt: DNS/name-resolution failure before an HTTP
  response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved solution18 access attempt: DNS/name-resolution failure before an HTTP
  response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13 access attempt: DNS/name-resolution failure before an HTTP response
  (no HTTP status or response body captured). No usable exact formulation from this
  response; failed access is not proof of nonexistence. Variant detail is required
  for equivalence assessment; current base/stock API failures do not negate available
  primary recipes.'
- 'Preserved komodo13_13609 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17974 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17975 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17978 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17979 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17980 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17981 access attempt: DNS/name-resolution failure before an
  HTTP response (no HTTP status or response body captured). No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved mediadiveJ101_network_retry access attempt: 503. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved mediadive13_network_retry access attempt: 503. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved mediadive1286_network_retry access attempt: 503. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved solution17_network_retry access attempt: 503. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved solution18_network_retry access attempt: 503. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_13609_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17974_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17975_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17978_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17979_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17980_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- 'Preserved komodo13_17981_network_retry access attempt: 403. No usable exact formulation
  from this response; failed access is not proof of nonexistence. Variant detail is
  required for equivalence assessment; current base/stock API failures do not negate
  available primary recipes.'
- The required scientific comparison is partial because exact strain-variant formulations
  and historical medium/solution API raw correspondence remain unavailable. Current
  primary base and DSMZ 1286 comparisons are completed within their stated scopes.
- No generic M142 transfer statement from the preparatory template applies to record
  373. Only the named local stocks and source-specific base/DSMZ 1286 formulations
  are assessed.
- Canonical reference validation checked zero references. No experimental phenotype,
  growth temperature, exact final volume, supplier grade or chemical stereochemistry
  beyond explicit source statements is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-038
- generated-medium
```
