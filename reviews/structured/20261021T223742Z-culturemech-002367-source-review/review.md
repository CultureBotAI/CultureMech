# Source and formulation review: bcye_agar (CultureMech:002367)

- Review: 20261021T223742Z-culturemech-002367-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T22:32:18Z
- Finished UTC: 2026-10-21T22:37:42Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated BCYE record combines fifteen distinct maintained formulations and retains a dilute R2A recipe under JCM119 identity. Most maintained contributors already preserve their commercial products and preparation; reconcile their remaining source limits and regenerate only compatible formulations. The false R2A-to-agar link, unsupported percentage bases and unrelated soil-extract graph accession need separate correction.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 395; batch 040 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-nine task batches contain 390 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 393 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002367 | data/merge_yaml/merged/BCYE_AGAR.yaml | generated | bcye_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002367 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002367 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/395/strict.tsv |
| validate-terms | passed | True | CultureMech:002367 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002367 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002367 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm258 | unavailable | True | CultureMech:002367 | Current JCM258 returned HTTP200 with Nothing found, not a formulation. TOGO M250 is usable as its explicitly attributed source snapshot; present primary correspondence remains unavailable. |
| Exact source content access: compound1844Identity | unavailable | False | CultureMech:002367 | Preserved optional source attempt compound 1844Identity did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: komodo604detail | unavailable | False | CultureMech:002367 | Preserved optional source attempt komodo604detail did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ119api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ119api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1329api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1329api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ150api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ150api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ455api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ455api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ258api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ258api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ655api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ655api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1202api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1202api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ118api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ118api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1001api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1001api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1016api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1016api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadive604api | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadive604api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ119api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ119api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1329api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1329api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ150api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ150api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ455api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ455api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ258api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ258api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ655api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ655api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1202api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1202api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ118api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ118api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1001api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1001api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadiveJ1016api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadiveJ1016api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Exact source content access: mediadive604api_retry | unavailable | False | CultureMech:002367 | Preserved optional source attempt mediadive604api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| Original source and exact BCYE formulation for M2859 | unavailable | True | CultureMech:002367 | TOGO M2859 has an empty original-source URL and only an unspecified one-litre BCYE component. Its exact formulation, supplier and original experiment remain unresolved. |
| Source-specific DSM604 product dose and preparation | unavailable | True | CultureMech:002367 | The exact DSM604 page names Difco 0979 but supplies neither amount nor preparation. Both maintained VARIABLE values are appropriate; borrowing the J118 dose would require evidence of equivalence. |
| Historical R2A parent-paper correspondence | unavailable | True | CultureMech:002367 | The scoped R2A parent contains a PMID:3883894 excerpt without a captured paper response. Its original quotation is not independently authenticated here; current JCM346 supports a separate formulation comparison. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002367.

The four documented recipes completed; interpret the scope of each separately.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:002367.

116 timestamp instances inspected; 8 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Fifteen contributor identities and stale generated content

identity: concern. Targets: CultureMech:002367.

JCM119 BCYE has 37 g commercial BCYE base, 100 ml Legionella enrichment and 900 ml water. The target instead contains the J804 dilute R2A product and added agar. Current owners separately preserve R2A dilution, corn-meal suppliers, M2859 unspecified BCYE, alkali RCA, DSM604 commercial identity, ME, modified GAM, oatmeal and marine/pH formulations. Their coincident historical fingerprint does not prove equivalence.

### Provider mixture identity and exact ontology metadata

grounding: concern. Targets: CultureMech:002367.

The two target primary slots are populated, but one is a provider complex-medium identifier rather than CHEBI. Primary CHEBI coverage is 1/2 (50%); all primary identifiers have source metadata 2/2 (100%). Both secondary slots resolve in the pinned MIM index 2/2 (100%), yet the first agar link falsely treats the whole R2A mixture as agar. All asserted CHEBI labels in the target and fifteen owners are exact; commercial products correctly left ungrounded are not missing pure-molecule identities. These percentages measure linkage, not scientific accuracy.

### Recipe water, nominal rates and percentage bases

quantity: concern. Targets: CultureMech:002367.

Treat printed g/ml/L as recipe inputs. J119 lists 900 ml water plus 100 ml enrichment, and J455 lists 900 ml water before 100 ml carbonate solution; neither states a measured final volume. Retained nominal per-litre values require that convention to be explicit. J455/J1001/J1016 say 10% carbonate without a w/v basis. The pH wrappers leave its dose VARIABLE; do not calculate carbonate grams or final pH-mixture volume.

### Contributor-specific preparation survives in owners

completeness: concern. Targets: CultureMech:002367.

The target omits preparation. Most maintained owners already retain the appropriate default 121 C/15 min or TOGO M250 115 C/10 min procedure. Preserve post-autoclave carbonate additions and pH 8.5, 9.0 or about 10 only in their own formulations. DSM604 supplies no cycle, and M2859 supplies no preparation; do not invent either. J119 currently overstates its listed liquids as bringing the medium to 1 L.

### Asserted graph accession12

identity: concern. Targets: CultureMech:002367.

The target and several contributors assert mediadive.medium:12, whose exact DSMZ/API identity is SOIL EXTRACT MEDIUM. Its soil extraction and agar recipe do not support BCYE, R2A or the other contributor products. This is an independently confirmed accession-identity conflict; no local KG ingredient graph was recomputed and no replacement graph match is proposed.

### Cultivation statements and classification

evidence: concern. Targets: CultureMech:002367.

COMPLEX/UNDEFINED/SOLID_AGAR is compatible with the commercial agar formulations, but does not make them identical. The generic microbial-cultivation application does not establish a target strain. TOGO M2859 alone states L. pneumophila Paris/Lens at 37 C for 3 d; the original experiment and taxonomy were not independently recovered, so those conditions are not generalized to BCYE or the other contributors. Sterilization temperatures are not growth temperatures.

### Exact maintained ownership and scoped relationships

provenance: concern. Targets: CultureMech:002367.

Fifteen exact maintained paths are resolved with repeated bacto_marine basename multiplicity across categories. J119/M111, J1329/M3004 and J150/M141 are exact source-duplicate contexts; R2A parent applies only to J804/J845; marine pH wrappers delegate only to J118. Additional marine children are linked context, not extra base ingredients. Exact local ID resolution does not verify every child formulation or DSM604 dose. Excluded bacterial namesakes do not become owners or review obligations.

### Current claims versus parent and historical evidence

evidence: concern. Targets: CultureMech:002367.

No target or maintained contributor has attached evidence objects. Their current source/notes/references and repaired values do not equal claim-level excerpts. The only separately scoped existing evidence object is the R2A parent-paper claim; its source response is unavailable, and it must not transfer to the entire merged target. Historical report/plan prose is read as derivative context with exact record/ID scope, not authenticated original API evidence.

### Already repaired owners and present writer limits

provenance: concern. Targets: CultureMech:002367.

The current BCYE, corn-meal, sparse-product, DSM604, GAM/oatmeal and marine repair constructors explain the present repaired owner fields. Preserve that work. Narrow remaining corrections include unsupported percentage basis and volume wording; then reconcile the false merged identity under current guarded generation. The existing full source constructors are not evidence that current code produced the older false merge.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002367.

78 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "topic": "Generated target R2A agar",
    "decision": "correct",
    "local": {
      "value": "1.82",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.82",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The numbers describe J804, not the declared J119 identity. Reconstruct only after identity reconciliation."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Exact primary raw table row 0; cells ['R2A agar (BD-Difco)', '1.82', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; R2A agar (BD-Difco)                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.82&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09"
      },
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; BCYE agar (BD-Difco)                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "Preserve this historical stored value for audit, but do not keep the J804 formulation under J119 BCYE. Do not add BCYE ingredients to this R2A recipe as one combined medium."
  },
  {
    "quantity_id": "q2",
    "topic": "Generated target Agar",
    "decision": "correct",
    "local": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The numbers describe J804, not the declared J119 identity. Reconstruct only after identity reconciliation."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Exact primary raw table row 1; cells ['Agar', '15.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Agar                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;15.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09"
      },
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; BCYE agar (BD-Difco)                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "Preserve this historical stored value for audit, but do not keep the J804 formulation under J119 BCYE. Do not add BCYE ingredients to this R2A recipe as one combined medium."
  },
  {
    "quantity_id": "q3",
    "topic": "J119 source component 1 missing from generated identity",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; BCYE agar (BD-Difco)                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "After separating unrelated contributors, regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment and 900 ml recipe water. The maintained J119 owner already contains these components; no duplicate owner repair is requested."
  },
  {
    "quantity_id": "q4",
    "topic": "J119 source component 2 missing from generated identity",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 1; cells ['Legionella agar enrichment (BD-Difco)', '100.0', 'ml']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Legionella agar enrichment (BD-Difco)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "After separating unrelated contributors, regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment and 900 ml recipe water. The maintained J119 owner already contains these components; no duplicate owner repair is requested."
  },
  {
    "quantity_id": "q5",
    "topic": "J119 source component 3 missing from generated identity",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 2; cells ['Distilled water', '900.0', 'ml']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "After separating unrelated contributors, regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment and 900 ml recipe water. The maintained J119 owner already contains these components; no duplicate owner repair is requested."
  },
  {
    "quantity_id": "q6",
    "topic": "JCM Medium J804 — R2A agar (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "1.82",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.82",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 804 lists 1.82 g/L R2A agar (BD-Difco).",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Exact primary raw table row 0; cells ['R2A agar (BD-Difco)', '1.82', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; R2A agar (BD-Difco)                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.82&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q7",
    "topic": "JCM Medium J804 — Agar",
    "decision": "evidence_only",
    "local": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 804 adds 15 g/L agar.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Exact primary raw table row 1; cells ['Agar', '15.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Agar                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;15.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q8",
    "topic": "JCM Medium J804 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "JCM Medium 804 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Exact primary raw table row 2; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q9",
    "topic": "JCM Medium J845 — R2A agar (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "9.1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "9.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 845 lists 9.1 g/L R2A agar (BD-Difco).",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm845",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845",
        "source_locator": "Exact primary raw table row 0; cells ['R2A agar (BD-Difco)', '9.1', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; R2A agar (BD-Difco)                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;9.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q10",
    "topic": "JCM Medium J845 — Agar",
    "decision": "evidence_only",
    "local": {
      "value": "7.5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 845 adds 7.5 g/L agar.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm845",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845",
        "source_locator": "Exact primary raw table row 1; cells ['Agar', '7.5', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Agar                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;7.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q11",
    "topic": "JCM Medium J845 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "JCM Medium 845 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm845",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845",
        "source_locator": "Exact primary raw table row 2; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q12",
    "topic": "JCM Medium J119 — BCYE agar (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "37",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "37",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 119 lists this commercial BD-Difco medium base as supplied.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; BCYE agar (BD-Difco)                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;37.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q13",
    "topic": "JCM Medium J119 — Legionella agar enrichment (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "100",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "100",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 119 lists this commercial BD-Difco enrichment as supplied.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 1; cells ['Legionella agar enrichment (BD-Difco)', '100.0', 'ml']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Legionella agar enrichment (BD-Difco)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q14",
    "topic": "JCM Medium J119 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "900",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "900",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. Correct the existing note claiming a final 1 L makeup: the primary lists 900 ml water and 100 ml enrichment, not a measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "JCM Medium 119 brings the base plus enrichment to 1 L.",
        "decision": "correct",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. Correct the existing note claiming a final 1 L makeup: the primary lists 900 ml water and 100 ml enrichment, not a measured final volume."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Exact primary raw table row 2; cells ['Distilled water', '900.0', 'ml']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. Correct the existing note claiming a final 1 L makeup: the primary lists 900 ml water and 100 ml enrichment, not a measured final volume."
  },
  {
    "quantity_id": "q15",
    "topic": "JCM Medium J1329 — Corn meal agar (Nissui)",
    "decision": "evidence_only",
    "local": {
      "value": "17.0",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "17.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 1329 lists 17.0 g/L Corn meal agar (Nissui); this is a commercial dehydrated medium and is intentionally left ungrounded.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1329",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329",
        "source_locator": "Exact primary raw table row 0; cells ['Corn meal agar (Nissui)', '17.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Corn meal agar (Nissui)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;17.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q16",
    "topic": "JCM Medium J1329 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 1329 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1329",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q17",
    "topic": "JCM Medium J150 — Corn meal agar (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "17.0",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "17.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 150 lists 17.0 g/L Corn meal agar (BD-Difco); this is a commercial dehydrated medium and is intentionally left ungrounded.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm150",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150",
        "source_locator": "Exact primary raw table row 0; cells ['Corn meal agar (BD-Difco)', '17.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Corn meal agar (BD-Difco)                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;17.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q18",
    "topic": "JCM Medium J150 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 150 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm150",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q19",
    "topic": "TOGO Medium M2859 — BCYE agar",
    "decision": "not_quantified",
    "local": {
      "value": "1000",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000",
          "unit": "ML_PER_L"
        },
        "decision": "not_quantified",
        "rationale": "The source lists 1 L of unspecified BCYE. 1000 ml is an exact unit conversion, but ML_PER_L adds a denominator not independently supplied for this opaque medium. Preserve the volume-only amount and unresolved product/formulation; no dry mass or J119 equivalence is inferred."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "TOGO M2859 lists one liter of BCYE agar without spelling out the commercial product or formulation.",
        "decision": "not_quantified",
        "rationale": "The source lists 1 L of unspecified BCYE. 1000 ml is an exact unit conversion, but ML_PER_L adds a denominator not independently supplied for this opaque medium. Preserve the volume-only amount and unresolved product/formulation; no dry mass or J119 equivalence is inferred."
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2859original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"BCYE agar\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "ede4a337bb29494b8e3ba5121c94fcfd933e1b19d98916349209f5a56ff133b4"
      }
    ],
    "rationale": "The source lists 1 L of unspecified BCYE. 1000 ml is an exact unit conversion, but ML_PER_L adds a denominator not independently supplied for this opaque medium. Preserve the volume-only amount and unresolved product/formulation; no dry mass or J119 equivalence is inferred."
  },
  {
    "quantity_id": "q20",
    "topic": "JCM Medium J455 — Reinforced clostridial agar (Sigma)",
    "decision": "evidence_only",
    "local": {
      "value": "51.0",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "51.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "MediaDive J455 / JCM Medium 455 lists 51.0 g/L Reinforced clostridial agar (Sigma); this dehydrated commercial mixture is retained as an opaque complex component.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Exact primary raw table row 0; cells ['Reinforced clostridial agar (Sigma)', '51.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Reinforced clostridial agar (Sigma)                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;51.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q21",
    "topic": "JCM Medium J455 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "900.0",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "900.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "MediaDive J455 / JCM Medium 455 lists 900.0 ml/L Distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '900.0', 'ml']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q22",
    "topic": "JCM Medium J455 carbonate stock dose",
    "decision": "evidence_only",
    "local": {
      "value": "100.0",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "100.0",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "Keep the explicit 100 ml dose separate from 900 ml basal water; no measured final volume is declared."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to the medium.",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      }
    ],
    "rationale": "Keep the explicit 100 ml dose separate from 900 ml basal water; no measured final volume is declared."
  },
  {
    "quantity_id": "q23",
    "topic": "JCM Medium J455 carbonate stock percentage",
    "decision": "correct",
    "local": {
      "value": "10.0",
      "unit": "PERCENT_W_V"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        },
        "decision": "correct",
        "rationale": "10% is printed without a mass/volume basis; current PERCENT_W_V is unsupported."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to the medium.",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      }
    ],
    "rationale": "Preserve 10% as an explicitly unspecified basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium concentration. Retain source sodium carbonate without inventing hydrate specificity."
  },
  {
    "quantity_id": "q24",
    "topic": "JCM Medium J455 stock sterilization",
    "decision": "evidence_only",
    "local": "Sterilize the 10% Na2CO3 solution before aseptic addition.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Sterilize the 10% Na2CO3 solution before aseptic addition.",
        "decision": "evidence_only",
        "rationale": "Sterilized stock is explicit; its separate cycle is not supplied."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to the medium.",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      }
    ],
    "rationale": "Keep sterile stock preparation separate from the default main-medium autoclave cycle; no stock temperature/time is inferred."
  },
  {
    "quantity_id": "q25",
    "topic": "KOMODO Medium 604 — Marine agar 2216 (Difco 0979)",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "DSMZ Medium 604 names Marine Agar 2216 (Difco 0979) as the only component but does not state an amount.",
        "decision": "not_quantified",
        "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz604",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf",
        "source_locator": "Complete primary formulation",
        "exact_source_quote": "MARINE AGAR 2216 (Difco 0979).",
        "snapshot_sha256": "9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24",
        "parsed_text_sha256": "f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e"
      }
    ],
    "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
  },
  {
    "quantity_id": "q26",
    "topic": "JCM Medium J258 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1000",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
      },
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "TOGO M250 snapshots JCM_M258 and lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM250original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a"
      }
    ],
    "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
  },
  {
    "quantity_id": "q27",
    "topic": "JCM Medium J258 — Malt extract agar (Oxoid)",
    "decision": "evidence_only",
    "local": {
      "value": "50",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
      },
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "TOGO M250 snapshots JCM_M258 and lists 50 g/L Malt extract agar from Oxoid.",
        "decision": "evidence_only",
        "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM250original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Malt extract agar (Oxoid)\",\n          \"volume\": 50,\n          \"unit\": \"g\"",
        "snapshot_sha256": "0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a"
      }
    ],
    "rationale": "TOGO M250 explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific attribution while current JCM258 is unavailable. One litre water is a recipe input; final volume is not measured."
  },
  {
    "quantity_id": "q28",
    "topic": "JCM Medium J655 — GAM agar, modified (Nissui)",
    "decision": "evidence_only",
    "local": {
      "value": "56.7",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "56.7",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 655 lists 56.7 g GAM agar, modified (Nissui).",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm655",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655",
        "source_locator": "Exact primary raw table row 0; cells ['GAM agar, modified (Nissui)', '56.7', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; GAM agar, modified (Nissui) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;56.7&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q29",
    "topic": "JCM Medium J655 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1000",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1000",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 655 lists 1000 ml distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm655",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q30",
    "topic": "JCM Medium J1202 — Oatmeal agar (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "15.0",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "15.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 1202 lists 15.0 g oatmeal agar (BD-Difco).",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1202",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202",
        "source_locator": "Exact primary raw table row 0; cells ['Oatmeal agar (BD-Difco)', '15.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Oatmeal agar (BD-Difco)      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;15.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q31",
    "topic": "JCM Medium J1202 — Agar",
    "decision": "evidence_only",
    "local": {
      "value": "12.0",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "12.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 1202 lists 12.0 g agar.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1202",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202",
        "source_locator": "Exact primary raw table row 1; cells ['Agar', '12.0', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Agar                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;12.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q32",
    "topic": "JCM Medium J1202 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1000",
      "unit": "ML_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000",
          "unit": "ML_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "JCM Medium 1202 lists 1000 ml distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1202",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202",
        "source_locator": "Exact primary raw table row 2; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q33",
    "topic": "DSMZ Medium 604 — Marine agar 2216 (Difco 0979)",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
      },
      {
        "input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "DSMZ Medium 604 names Marine Agar 2216 (Difco 0979) as the only component but does not state an amount.",
        "decision": "not_quantified",
        "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz604",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf",
        "source_locator": "Complete primary formulation",
        "exact_source_quote": "MARINE AGAR 2216 (Difco 0979).",
        "snapshot_sha256": "9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24",
        "parsed_text_sha256": "f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e"
      }
    ],
    "rationale": "VARIABLE accurately preserves the absent source dose. Product identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization cycle."
  },
  {
    "quantity_id": "q34",
    "topic": "JCM Medium J118 — Marine agar 2216 (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "55.1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "55.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 118 prints this commercial component.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 0; cells ['Marine agar 2216 (BD-Difco)', '55.1', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Marine agar 2216 (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;55.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q35",
    "topic": "JCM Medium J118 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 118 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount."
  },
  {
    "quantity_id": "q36",
    "topic": "JCM Medium J1001 — Marine agar 2216 (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "55.1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "55.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 118 lists 55.1 g/L Marine agar 2216 with the BD-Difco attribute; left ungrounded as an undefined commercial agar.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 0; cells ['Marine agar 2216 (BD-Difco)', '55.1', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Marine agar 2216 (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;55.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      },
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Exact primary delegation to J118",
        "exact_source_quote": "Prepare Marine agar 2216 (see Medium No. 118 ).",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
  },
  {
    "quantity_id": "q37",
    "topic": "JCM Medium J1001 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 118 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      },
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Exact primary delegation to J118",
        "exact_source_quote": "Prepare Marine agar 2216 (see Medium No. 118 ).",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
  },
  {
    "quantity_id": "q38",
    "topic": "JCM Medium J1001 carbonate stock dose",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution."
  },
  {
    "quantity_id": "q39",
    "topic": "JCM Medium J1001 carbonate stock percentage",
    "decision": "correct",
    "local": {
      "value": "10.0",
      "unit": "PERCENT_W_V"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        },
        "decision": "correct",
        "rationale": "10% is printed without a mass/volume basis; current PERCENT_W_V is unsupported."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "Preserve 10% as an explicitly unspecified basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium concentration. Retain source sodium carbonate without inventing hydrate specificity."
  },
  {
    "quantity_id": "q40",
    "topic": "JCM Medium J1001 stock sterilization",
    "decision": "evidence_only",
    "local": "Sterilize the 10% Na2CO3 solution before addition.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Sterilize the 10% Na2CO3 solution before addition.",
        "decision": "evidence_only",
        "rationale": "Sterilized stock is explicit; its separate cycle is not supplied."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "Keep sterile stock preparation separate from the default main-medium autoclave cycle; no stock temperature/time is inferred."
  },
  {
    "quantity_id": "q41",
    "topic": "JCM Medium J1016 — Marine agar 2216 (BD-Difco)",
    "decision": "evidence_only",
    "local": {
      "value": "55.1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "55.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "JCM Medium 118 lists 55.1 g/L Marine agar 2216 with the BD-Difco attribute; left ungrounded as an undefined commercial agar.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 0; cells ['Marine agar 2216 (BD-Difco)', '55.1', 'g']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Marine agar 2216 (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;55.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      },
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Exact primary delegation to J118",
        "exact_source_quote": "Prepare Marine agar 2216 (see Medium No. 118 ).",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
  },
  {
    "quantity_id": "q42",
    "topic": "JCM Medium J1016 — Distilled water",
    "decision": "evidence_only",
    "local": {
      "value": "1.0",
      "unit": "L"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.0",
          "unit": "L"
        },
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "JCM Medium 118 lists 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129"
      },
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Exact primary delegation to J118",
        "exact_source_quote": "Prepare Marine agar 2216 (see Medium No. 118 ).",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "The literal amount belongs to this contributor only. A per-litre field is a nominal recipe convention relative to listed water or liquids, not proof of measured final volume. No attached quantity evidence exists; add an exact scoped excerpt without changing a supported amount. The pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose addition."
  },
  {
    "quantity_id": "q43",
    "topic": "JCM Medium J1016 carbonate stock dose",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution."
  },
  {
    "quantity_id": "q44",
    "topic": "JCM Medium J1016 carbonate stock percentage",
    "decision": "correct",
    "local": {
      "value": "10.0",
      "unit": "PERCENT_W_V"
    },
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "10.0",
          "unit": "PERCENT_W_V"
        },
        "decision": "correct",
        "rationale": "10% is printed without a mass/volume basis; current PERCENT_W_V is unsupported."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "Preserve 10% as an explicitly unspecified basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium concentration. Retain source sodium carbonate without inventing hydrate specificity."
  },
  {
    "quantity_id": "q45",
    "topic": "JCM Medium J1016 stock sterilization",
    "decision": "evidence_only",
    "local": "Sterilize the 10% Na2CO3 solution before addition.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Sterilize the 10% Na2CO3 solution before addition.",
        "decision": "evidence_only",
        "rationale": "Sterilized stock is explicit; its separate cycle is not supplied."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Post-autoclave stock addition",
        "exact_source_quote": "After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "Keep sterile stock preparation separate from the default main-medium autoclave cycle; no stock temperature/time is inferred."
  },
  {
    "quantity_id": "q46",
    "topic": "JCM Medium J804 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 804 lists 1.82 g/L R2A agar (BD-Difco), 15 g/L agar, and 1.0 L distilled water.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 804 lists 1.82 g/L R2A agar (BD-Difco), 15 g/L agar, and 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Dissolve 1.82 g R2A agar (BD-Difco) and 15 g agar in 1.0 L distilled water."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
        "field_path": "variant_modifications",
        "stored": [
          "Uses 1.82 g/L R2A agar (BD-Difco) with 15 g/L added agar."
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm804",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09",
        "parsed_text_sha256": "dff149bc5d15c946bb19a85a30d32a6950618fcfc5279bf5007993f2af839c05"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q47",
    "topic": "JCM Medium J845 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 845 lists 9.1 g/L R2A agar (BD-Difco), 7.5 g/L agar, and 1.0 L distilled water.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 845 lists 9.1 g/L R2A agar (BD-Difco), 7.5 g/L agar, and 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Dissolve 9.1 g R2A agar (BD-Difco) and 7.5 g agar in 1.0 L distilled water."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
        "field_path": "variant_modifications",
        "stored": [
          "Uses 9.1 g/L R2A agar (BD-Difco) with 7.5 g/L added agar."
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm845",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7",
        "parsed_text_sha256": "cfef3065aec7802fb0fd6c802d44cd89c6bc1beecfb8b081e00f8c993ca5804a"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q48",
    "topic": "JCM Medium J119 preparation and conditions",
    "decision": "evidence_only",
    "local": "Source: JCM Medium 119 &#124; Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\n\nThe JCM BCYE Agar table lists BCYE agar, Legionella agar enrichment, and distilled water as supplied BD-Difco products.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "notes",
        "stored": "Source: JCM Medium 119 &#124; Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\n\nThe JCM BCYE Agar table lists BCYE agar, Legionella agar enrichment, and distilled water as supplied BD-Difco products.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows. The water-note claim of final 1 L makeup is separately marked for correction."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows. The water-note claim of final 1 L makeup is separately marked for correction."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c",
        "parsed_text_sha256": "8e902ea14398f3deff72743b4efb5e8d370875df49359881483cfbef8e159bb9"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows. The water-note claim of final 1 L makeup is separately marked for correction."
  },
  {
    "quantity_id": "q49",
    "topic": "JCM Medium J1329 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 1329 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar (Nissui) in 1.0 L distilled water, with default JCM autoclaving at 121 C for 15 minutes.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 1329 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar (Nissui) in 1.0 L distilled water, with default JCM autoclaving at 121 C for 15 minutes.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 minutes."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1329",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723",
        "parsed_text_sha256": "d873785344db095d73c2b7704f723a249e10e405693e8702d9621785ef08fa68"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q50",
    "topic": "JCM Medium J150 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 150 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar (BD-Difco) in 1.0 L distilled water, with default JCM autoclaving at 121 C for 15 minutes.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 150 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar (BD-Difco) in 1.0 L distilled water, with default JCM autoclaving at 121 C for 15 minutes.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 minutes."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm150",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478",
        "parsed_text_sha256": "166ae9f69dd4786d18d7dd2f638dda1799b2a3965e3c3c1c748d28803498d374"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q51",
    "topic": "TOGO Medium M2859 preparation and conditions",
    "decision": "evidence_only",
    "local": "TOGO M2859 records L. pneumophila strains Paris and Lens grown on one liter of BCYE agar at 37 C for 3 d; the source does not disclose the BCYE agar formulation.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml",
        "field_path": "notes",
        "stored": "TOGO M2859 records L. pneumophila strains Paris and Lens grown on one liter of BCYE agar at 37 C for 3 d; the source does not disclose the BCYE agar formulation.",
        "decision": "evidence_only",
        "rationale": "The provider alone states Paris/Lens 37 C and 3 d. Preserve the narrow attribution, and do not treat this as original-paper verification or a general BCYE growth condition."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml",
        "field_path": "temperature_value",
        "stored": 37.0,
        "decision": "evidence_only",
        "rationale": "The provider alone states Paris/Lens 37 C and 3 d. Preserve the narrow attribution, and do not treat this as original-paper verification or a general BCYE growth condition."
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2859original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "L. pneumophila strains Paris and Lens were grown on BCYE agar at 37 °C for 3 d and chromosomal DNA was isolated by standard protocols.",
        "snapshot_sha256": "ede4a337bb29494b8e3ba5121c94fcfd933e1b19d98916349209f5a56ff133b4"
      }
    ],
    "rationale": "The provider alone states Paris/Lens 37 C and 3 d. Preserve the narrow attribution, and do not treat this as original-paper verification or a general BCYE growth condition."
  },
  {
    "quantity_id": "q52",
    "topic": "JCM Medium J455 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 455 Alkali-Reinforced Clostridial Agar lists 51 g Reinforced clostridial agar (Sigma) in 900 ml distilled water per liter. After autoclaving at 121 C for 15 min, 100 ml of sterile 10% Na2CO3 solution is added aseptically and the final pH is checked to be about 10.0.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 455 Alkali-Reinforced Clostridial Agar lists 51 g Reinforced clostridial agar (Sigma) in 900 ml distilled water per liter. After autoclaving at 121 C for 15 min, 100 ml of sterile 10% Na2CO3 solution is added aseptically and the final pH is checked to be about 10.0.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave the reinforced clostridial agar base at 121 C for 15 min."
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "Aseptically add 100 ml/L sterile 10% Na2CO3 solution after autoclaving."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "Check final pH to be about 10.0."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "temperature": {
            "value": 121.0,
            "unit": "CELSIUS"
          },
          "duration": "15 min",
          "notes": "Sterilize the 10% Na2CO3 solution separately before aseptic addition."
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ph_value",
        "stored": 10.0,
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      },
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Complete short primary including separate carbonate/pH instruction",
        "exact_source_quote": "Medium data Medium data Search for medium no. = [455]. Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min. 455   ALKALI-REINFORCED CLOSTRIDIAL AGAR Reinforced clostridial agar (Sigma) 51.0 g Distilled water 900.0 ml After autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to the medium. Check final pH to be about 10.0. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q53",
    "topic": "KOMODO Medium 604 preparation and conditions",
    "decision": "not_quantified",
    "local": "DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216 (Difco 0979).",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml",
        "field_path": "notes",
        "stored": "DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216 (Difco 0979).",
        "decision": "not_quantified",
        "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare the Marine Agar 2216 (Difco 0979) product."
          }
        ],
        "decision": "not_quantified",
        "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz604",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf",
        "source_locator": "Complete primary",
        "exact_source_quote": "MARINE AGAR 2216 (Difco 0979).",
        "snapshot_sha256": "9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24",
        "parsed_text_sha256": "f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e"
      }
    ],
    "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
  },
  {
    "quantity_id": "q54",
    "topic": "JCM Medium J258 preparation and conditions",
    "decision": "evidence_only",
    "local": "TOGO M250 is a snapshot of JCM_M258 and records 50 g/L Malt extract agar from Oxoid in distilled water with autoclaving at 115 C for 10 min.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "notes",
        "stored": "TOGO M250 is a snapshot of JCM_M258 and records 50 g/L Malt extract agar from Oxoid in distilled water with autoclaving at 115 C for 10 min.",
        "decision": "evidence_only",
        "rationale": "Retain the provider-specific 115 C/10 min procedure already present; it is sterilization, not growth. Current primary correspondence remains unavailable."
      },
      {
        "input": "data/normalized_yaml/bacterial/me_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 115 C for 10 min."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the provider-specific 115 C/10 min procedure already present; it is sterilization, not growth. Current primary correspondence remains unavailable."
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM250original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Autoclave at 115C for 10 min.",
        "snapshot_sha256": "0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a"
      }
    ],
    "rationale": "Retain the provider-specific 115 C/10 min procedure already present; it is sterilization, not growth. Current primary correspondence remains unavailable."
  },
  {
    "quantity_id": "q55",
    "topic": "JCM Medium J655 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 655 contains 56.7 g GAM agar, modified (Nissui), and 1.0 L distilled water.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 655 contains 56.7 g GAM agar, modified (Nissui), and 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Suspend 56.7 g GAM agar, modified (Nissui), in 1.0 L distilled water."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min unless otherwise stated."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm655",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53",
        "parsed_text_sha256": "21e3cba1d661434dfeb90bcdf4851663be58e10bfa56a518026c9f1d3c477d2f"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q56",
    "topic": "JCM Medium J1202 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 1202 contains 15.0 g oatmeal agar (BD-Difco), 12.0 g agar, and 1.0 L distilled water.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 1202 contains 15.0 g oatmeal agar (BD-Difco), 12.0 g agar, and 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Suspend 15.0 g oatmeal agar (BD-Difco) and 12.0 g agar in 1.0 L distilled water."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min unless otherwise stated."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1202",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc",
        "parsed_text_sha256": "b5ef6f65af41099fcb4759563ae2cd0402b0efa6e1fb47d824b7d1715e00002a"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q57",
    "topic": "DSMZ Medium 604 preparation and conditions",
    "decision": "not_quantified",
    "local": "DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216 (Difco 0979).",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml",
        "field_path": "notes",
        "stored": "DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216 (Difco 0979).",
        "decision": "not_quantified",
        "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
      },
      {
        "input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare the Marine Agar 2216 (Difco 0979) product."
          }
        ],
        "decision": "not_quantified",
        "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz604",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf",
        "source_locator": "Complete primary",
        "exact_source_quote": "MARINE AGAR 2216 (Difco 0979).",
        "snapshot_sha256": "9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24",
        "parsed_text_sha256": "f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e"
      }
    ],
    "rationale": "The source supplies product identity only. Existing generic MIX instruction does not establish dose, water or sterilization; those details remain unresolved."
  },
  {
    "quantity_id": "q58",
    "topic": "JCM Medium J118 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 118 defines Marine Agar 2216 with 55.1 g Marine agar 2216 (BD-Difco) and 1.0 L distilled water.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 118 defines Marine Agar 2216 with 55.1 g Marine agar 2216 (BD-Difco) and 1.0 L distilled water.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare Marine Agar 2216."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129",
        "parsed_text_sha256": "d58c7e0426fdb2e9321ac2226356dec0dc90eb4f6fea91000167bea3a69ca966"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q59",
    "topic": "JCM Medium J1001 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 1001 defines Marine Agar 2216 at pH 8.5 as JCM Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3 solution.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 1001 defines Marine Agar 2216 at pH 8.5 as JCM Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3 solution.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare Marine agar 2216 from JCM Medium 118."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the Marine Agar 2216 base at 121 C for 15 min."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "After autoclaving, adjust pH to 8.5 with sterilized 10% Na2CO3 solution."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ph_value",
        "stored": 8.5,
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "variant_modifications",
        "stored": [
          "Adjusted JCM Medium 118 Marine Agar 2216 to pH 8.5 with 10% Na2CO3."
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      },
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Complete short primary including separate carbonate/pH instruction",
        "exact_source_quote": "Medium data Medium data Search for medium no. = [1001]. Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min. 1001   MARINE AGAR 2216 (pH 8.5) Prepare Marine agar 2216 (see Medium No. 118 ). After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q60",
    "topic": "JCM Medium J1016 preparation and conditions",
    "decision": "evidence_only",
    "local": "JCM Medium 1016 defines Marine Agar 2216 at pH 9.0 as JCM Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3 solution.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "notes",
        "stored": "JCM Medium 1016 defines Marine Agar 2216 at pH 9.0 as JCM Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3 solution.",
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare Marine agar 2216 from JCM Medium 118."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the Marine Agar 2216 base at 121 C for 15 min."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "After autoclaving, adjust pH to 9.0 with sterilized 10% Na2CO3 solution."
          }
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE"
        },
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      },
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "variant_modifications",
        "stored": [
          "Adjusted JCM Medium 118 Marine Agar 2216 to pH 9.0 with 10% Na2CO3."
        ],
        "decision": "evidence_only",
        "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Page-wide default sterilization",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      },
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Complete short primary including separate carbonate/pH instruction",
        "exact_source_quote": "Medium data Medium data Search for medium no. = [1016]. Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min. 1016   MARINE AGAR 2216 (pH 9.0) Prepare Marine agar 2216 (see Medium No. 118 ). After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "Retain the existing contributor-specific procedure and default 121 C/15 min sterilization; preserve its source-specific formulation and any late carbonate/pH step. No incubation condition or measured final volume follows."
  },
  {
    "quantity_id": "q61",
    "topic": "Generated J119 preparation missing",
    "decision": "add",
    "local": null,
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Regenerate the exact J119 default procedure after separating the contributors."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm119",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119",
        "source_locator": "Page-wide default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c",
        "parsed_text_sha256": "8e902ea14398f3deff72743b4efb5e8d370875df49359881483cfbef8e159bb9"
      }
    ],
    "rationale": "The generated target lacks preparation; the J119 maintained owner already has it. Do not pool the other contributors’ different cycles or pH steps."
  },
  {
    "quantity_id": "q62",
    "topic": "JCM Medium J455 scalar pH",
    "decision": "evidence_only",
    "local": 10.0,
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
        "field_path": "ph_value",
        "stored": 10.0,
        "decision": "evidence_only",
        "rationale": "Existing scalar matches its own source; about 10 remains approximate."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm455",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455",
        "source_locator": "Exact pH instruction",
        "exact_source_quote": "Check final pH to be about 10.0.",
        "snapshot_sha256": "14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53",
        "parsed_text_sha256": "380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe"
      }
    ],
    "rationale": "Retain this scalar only within the source-specific formulation; do not copy a contributor pH to the BCYE target."
  },
  {
    "quantity_id": "q63",
    "topic": "JCM Medium J1001 scalar pH",
    "decision": "evidence_only",
    "local": 8.5,
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "field_path": "ph_value",
        "stored": 8.5,
        "decision": "evidence_only",
        "rationale": "Existing scalar matches its own source; about 10 remains approximate."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1001",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
        "source_locator": "Exact pH instruction",
        "exact_source_quote": "After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084",
        "parsed_text_sha256": "f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7"
      }
    ],
    "rationale": "Retain this scalar only within the source-specific formulation; do not copy a contributor pH to the BCYE target."
  },
  {
    "quantity_id": "q64",
    "topic": "JCM Medium J1016 scalar pH",
    "decision": "evidence_only",
    "local": 9.0,
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only",
        "rationale": "Existing scalar matches its own source; about 10 remains approximate."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1016",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
        "source_locator": "Exact pH instruction",
        "exact_source_quote": "After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.",
        "snapshot_sha256": "026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d",
        "parsed_text_sha256": "ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c"
      }
    ],
    "rationale": "Retain this scalar only within the source-specific formulation; do not copy a contributor pH to the BCYE target."
  },
  {
    "quantity_id": "q65",
    "topic": "J346 parent only — Yeast extract (BD-Difco) 0.5 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Yeast extract (BD-Difco) 0.5 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q66",
    "topic": "J346 parent only — Proteose peptone No. 3 (BD-Difco) 0.5 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Proteose peptone No. 3 (BD-Difco) 0.5 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q67",
    "topic": "J346 parent only — Casamino acids (BD-Difco) 0.5 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Casamino acids (BD-Difco) 0.5 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q68",
    "topic": "J346 parent only — Glucose 0.5 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Glucose 0.5 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q69",
    "topic": "J346 parent only — Soluble starch 0.5 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Soluble starch 0.5 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q70",
    "topic": "J346 parent only — Sodium pyruvate 0.3 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Sodium pyruvate 0.3 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q71",
    "topic": "J346 parent only — K 2 HPO 4 0.3 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "K 2 HPO 4 0.3 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q72",
    "topic": "J346 parent only — MgSO 4 ·7H 2 O 0.05 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.05 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q73",
    "topic": "J346 parent only — Agar 15.0 g",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q74",
    "topic": "J346 parent only — Distilled water 1.0 L",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q75",
    "topic": "J346 parent only — Adjust pH to 7.2.",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Exact R2A parent recipe/condition",
        "exact_source_quote": "Adjust pH to 7.2.",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "This is the standalone R2A parent, scoped only to J804/J845 relationship assessment. Do not add these undiluted values to the target or replace premix quantities; supplier/hydrate details remain exactly as printed."
  },
  {
    "quantity_id": "q76",
    "topic": "J346 parent sterilization",
    "decision": "evidence_only",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "jcm346",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346",
        "source_locator": "Page-wide parent procedure",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
        "parsed_text_sha256": "839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15"
      }
    ],
    "rationale": "The parent default cycle stays with J346; the two child pages independently supply their own default instruction."
  },
  {
    "quantity_id": "q77",
    "topic": "Marine child relationship quantities are not base additions",
    "decision": "unsupported",
    "local": [
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
        "relationship": "PH_VARIANT",
        "id": "CultureMech:015371",
        "name": "marine_agar_2216_ph_8_5",
        "notes": "JCM Medium 1001 adjusts JCM Medium 118 Marine Agar 2216 to pH 8.5."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
        "relationship": "PH_VARIANT",
        "id": "CultureMech:015373",
        "name": "marine_agar_2216_ph_9_0",
        "notes": "JCM Medium 1016 adjusts JCM Medium 118 Marine Agar 2216 to pH 9.0."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015418",
        "name": "marine_agar_2216_with_10_nacl",
        "notes": "Adds 100 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015426",
        "name": "marine_agar_2216_with_1_nacl",
        "notes": "Adds 10 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:015387",
        "name": "marine_agar_2216_with_1_starch",
        "notes": "Adds 10 g/L soluble starch to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015400",
        "name": "marine_agar_2216_with_3_1_nacl",
        "notes": "Adds 31 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015417",
        "name": "marine_agar_2216_with_5_nacl",
        "notes": "Adds 50 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015372",
        "name": "marine_agar_2216_with_8_0_nacl",
        "notes": "Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:015410",
        "name": "marine_agar_2216_with_8_nacl",
        "notes": "Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216."
      },
      {
        "path": "data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:015421",
        "name": "marine_agar_with_1_tween_20",
        "notes": "Adds 10 g/L Tween 20 to JCM Medium 118 Marine Agar 2216."
      }
    ],
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:015371",
            "name": "marine_agar_2216_ph_8_5",
            "notes": "JCM Medium 1001 adjusts JCM Medium 118 Marine Agar 2216 to pH 8.5."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:015373",
            "name": "marine_agar_2216_ph_9_0",
            "notes": "JCM Medium 1016 adjusts JCM Medium 118 Marine Agar 2216 to pH 9.0."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015418",
            "name": "marine_agar_2216_with_10_nacl",
            "notes": "Adds 100 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015426",
            "name": "marine_agar_2216_with_1_nacl",
            "notes": "Adds 10 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": "CultureMech:015387",
            "name": "marine_agar_2216_with_1_starch",
            "notes": "Adds 10 g/L soluble starch to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015400",
            "name": "marine_agar_2216_with_3_1_nacl",
            "notes": "Adds 31 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015417",
            "name": "marine_agar_2216_with_5_nacl",
            "notes": "Adds 50 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015372",
            "name": "marine_agar_2216_with_8_0_nacl",
            "notes": "Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:015410",
            "name": "marine_agar_2216_with_8_nacl",
            "notes": "Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216."
          },
          {
            "path": "data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": "CultureMech:015421",
            "name": "marine_agar_with_1_tween_20",
            "notes": "Adds 10 g/L Tween 20 to JCM Medium 118 Marine Agar 2216."
          }
        ],
        "decision": "unsupported",
        "rationale": "Exact local child links are resolved, but added-salt/starch/Tween quantities in their relationship notes are outside the inspected J118 main formulation."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm118",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118",
        "source_locator": "Main formulation only",
        "exact_source_quote": "Marine agar 2216 (BD-Difco) 55.1 g Distilled water 1.0 L",
        "snapshot_sha256": "e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129",
        "parsed_text_sha256": "d58c7e0426fdb2e9321ac2226356dec0dc90eb4f6fea91000167bea3a69ca966"
      }
    ],
    "rationale": "Keep reciprocal topology separate from ingredient curation. The named child records are not contributors here, and their supplemental quantities require their own source review; none transfers to J118 or BCYE."
  },
  {
    "quantity_id": "q78",
    "topic": "No DSM12 soil-extract quantities transfer",
    "decision": "unsupported",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz12GraphIdentity",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf",
        "source_locator": "Complete independent identity-check recipe",
        "exact_source_quote": "© 2007 DSMZ GmbH - All rights reserved \n12. SOIL EXTRACT MEDIUM \n \n \nSterilize 400.0 g of air-dried garden soil (with high content of organic matter) in 1000 ml \ntap water for one hour at 121C. Allow it to sediment for a few hours at room \ntemperature. Centrifuge the supernatant. Add 15.0 g agar per 1000 ml to the clear \nsupernatant solution thus obtained. Adjust pH to 6.8 - 7.0 and sterilize.",
        "snapshot_sha256": "1b4394336f7ace4e09c66fc67ed2e745e3c633b725e436d94335b99289243580",
        "parsed_text_sha256": "de5da40c03d985f04f682aaf3ccbf31585a595dabef4f3753b977c6396cc0e17"
      }
    ],
    "rationale": "The 400 g soil/1000 ml tap water extraction, 121 C for 1 hour, 15 g agar per 1000 ml supernatant and pH 6.8–7.0 belong to the conflicting graph accession only. They are explicitly excluded from every contributor formulation."
  }
]

## Findings

### f1: The BCYE identity carries an unrelated dilute R2A formulation

blocker / open / confirmed; issue key: culturemech.002367.merged-formulation-identity.

The target retains 1.82 g/L R2A agar and 15 g/L added agar under JCM119 identity and treats fifteen distinct formulations as synonyms. Current maintained owners already distinguish most of these products and stages; the generated record is stale and scientifically overmerged.

### f2: R2A agar is falsely linked to the pure agar ingredient

major / open / confirmed; issue key: culturemech.002367.complex-product-as-agar.

The provider explicitly identifies compound 1844 as complex R2A agar (BD-Difco), separately from compound 3 agar. The target’s first secondary CHEBI:2509 link collapses that whole mixture to agar, while maintained R2A owners already link to the local R2A recipe.

### f3: Stock percentage bases and final-volume wording exceed the sources

major / open / confirmed; issue key: culturemech.002367.percentage-and-volume-basis.

J455 and the two marine pH owners encode 10% carbonate as PERCENT_W_V although their primary pages omit the basis. J119’s water note claims a final 1 L makeup rather than the printed 900 ml water and 100 ml enrichment. Retain the existing stage reconstruction and unknown pH-adjustment dose.

### f4: The asserted graph accession denotes soil-extract medium

major / open / confirmed; issue key: culturemech.002367.graph12-identity.

Exact DSMZ/API medium 12 denotes SOIL EXTRACT MEDIUM rather than any of the merged commercial products. The target and several maintained contributors retain this unrelated kg_microbe_match. Current carbonate/pH repairs already removed it from some owners.

### f5: The target omits preparation already present in its maintained owners

major / open / confirmed; issue key: culturemech.002367.generated-preparation-loss.

The true J119 owner retains its default autoclave procedure, while the target has no preparation. Other contributors have distinct 115 C/10 min or 121 C/15 min cycles and separate pH/stock stages that must survive independently. Missing details for DSM604/M2859 cannot be filled by borrowing a cycle.

### f6: Some historical event timestamps are malformed or lack a timezone

minor / open / confirmed; issue key: culturemech.002367.historical-timestamp-shape.

The complete target/owner history inspection identifies eight malformed or timezone-naive timestamp instances. Their original wording is retained; neither a repair event nor its timestamp authenticates the original source response.

## Recommended Actions And Acceptance Checks

### a1

Retain exact contributor identities and existing owner repairs, resolve bounded remaining owner issues, then regenerate only scientifically compatible formulas. Do not combine every source ingredient into BCYE.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the complex-product identity during regeneration, use verified source-specific recipe/product links, and retain CHEBI:2509 only for actual added agar. Avoid invented pure-molecule mappings for commercial premixes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct only unsupported percentage/final-volume specificity in the exact maintained owners and corresponding current constructors; preserve supported amounts, separate stock doses and recipe-water inputs. Do not derive carbonate mass or measured final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Remove or reconcile the unsupported graph assertion only after checking each exact maintained source. Recompute graph matching against the corrected formulation; do not guess a replacement accession.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Regenerate the J119 preparation from its verified maintained owner after identity reconciliation, retain other contributor protocols in their own records, and leave source-undisclosed procedures explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve append-only history and append a bounded clarification if original timing can be recovered; do not invent missing precision or silently rewrite old events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BCYE_AGAR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_10_r2a_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/1_2_r2a_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-4 | data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-5 | data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-6 | data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-7 | data/normalized_yaml/bacterial/bacto_marine_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-8 | data/normalized_yaml/bacterial/me_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-9 | data/normalized_yaml/bacterial/modified_gam_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-10 | data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-11 | data/normalized_yaml/specialized/bacto_marine_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-12 | data/normalized_yaml/specialized/marine_agar_2216.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-13 | data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-14 | data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BCYE_AGAR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BCYE_AGAR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/395/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/395/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BCYE_AGAR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BCYE_AGAR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BCYE_AGAR.yaml:1:id: CultureMech:002367<br>./data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml:1:id: CultureMech:002367<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch040/source-preflight-bound/395/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 66 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| history-inventory | /private/tmp/culturemech-review-work-batch040/395/history-inventory.json; Exact local field objects and pinned source joins | context_only | Complete current histories and empty receiving-layer evidence arrays; the single R2A parent-paper claim remains separately scoped and unauthenticated. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch040/395/grounding-inventory.json; Exact local field objects and pinned source joins | context_only | Every asserted ingredient ontology, provider or local record link is retained with exact metadata; source-specific identity is assessed independently. |
| jcm119 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119; Complete primary formulation and relevant preparation; exact quoted text | supports | JCM119 specifies BCYE base, Legionella enrichment and water; the target R2A ingredients are a different formulation. |
| jcm804 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804; Complete primary formulation and relevant preparation; exact quoted text | supports | J804 is the separate dilute R2A contributor. |
| jcm845 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845; Complete primary formulation and relevant preparation; exact quoted text | supports | J845 is a different R2A dilution and added-agar amount. |
| jcm346 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346; Complete primary formulation and relevant preparation; exact quoted text | supports | R2A parent formulation applies only to its exact R2A children. |
| jcm1329 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329; Complete primary formulation and relevant preparation; exact quoted text | supports | The Nissui corn-meal product is not silently equated to BD-Difco. |
| jcm150 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150; Complete primary formulation and relevant preparation; exact quoted text | supports | The BD-Difco corn-meal product remains a distinct source identity. |
| jcm455 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455; Complete primary formulation and relevant preparation; exact quoted text | supports | The carbonate is a separate late addition; percentage basis is unspecified. |
| jcm655 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655; Complete primary formulation and relevant preparation; exact quoted text | supports | Modified GAM is a Nissui product, not BCYE or agar alone. |
| jcm1202 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202; Complete primary formulation and relevant preparation; exact quoted text | supports | Oatmeal product and additional agar remain separate. |
| jcm118 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118; Complete primary formulation and relevant preparation; exact quoted text | supports | The J118 marine product has an explicit mass and water entry. |
| jcm1001 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001; Complete primary formulation and relevant preparation; exact quoted text | supports | The pH 8.5 wrapper changes the J118 base after autoclaving; carbonate dose and percentage basis are not given. |
| jcm1016 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016; Complete primary formulation and relevant preparation; exact quoted text | supports | The pH 9 wrapper is distinct from the pH 8.5 wrapper. |
| dsmz604 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf; Complete primary formulation and relevant preparation; exact quoted text | supports | DSM604 supplies product identity but no product mass or water dose. |
| dsmz12GraphIdentity | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf; Complete primary formulation and relevant preparation; exact quoted text | supports | The asserted graph accession resolves to soil-extract medium, an identity cross-check only. |
| default-autoclave | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119; Page-wide instruction, applying unless the recipe states otherwise | supports | The default is sterilization, not an incubation condition. |
| r2a-provider | https://mediadive.dsmz.de/rest/medium/J804; $.data.solutions[0].recipe[0] versus recipe[1] | supports | The provider explicitly distinguishes compound 1844 R2A agar (BD-Difco) from compound 3 agar. |
| graph-identity | https://mediadive.dsmz.de/rest/medium/12; $.data.medium and $.data.solutions[0] | supports | Accession12 denotes SOIL EXTRACT MEDIUM. The response is not a KG ingredient-match proof. |
| togo-bcye | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859; $.meta.src_url, $.components[0].items[0], $.comments[0] | supports | One litre of unspecified BCYE and the Paris/Lens 37 C for 3 d statement are provider-scoped, with no original source URL. |
| togo-me | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250; $.meta.original_media_id, $.components[0].items, $.comments[0] | supports | TOGO explicitly snapshots JCM_M258 with 50 g Oxoid product, 1 L water and 115 C/10 min. Current JCM258 has no recipe. |
| togoM111relationship | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M111; $.meta original source identity and component rows | supports | The exact TOGO source duplicate is a relationship check only; it is not an additional contributor. |
| togoM3004relationship | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3004; $.meta original source identity and component rows | supports | The exact TOGO source duplicate is a relationship check only; it is not an additional contributor. |
| togoM141relationship | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M141; $.meta original source identity and component rows | supports | The exact TOGO source duplicate is a relationship check only; it is not an additional contributor. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS identifier, full label/definition/form metadata | supports | The current term label is exact. Valid agar, water and sodium-carbonate identities do not establish complex commercial-product equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, full label/definition/form metadata | supports | The current term label is exact. Valid agar, water and sodium-carbonate identities do not establish complex commercial-product equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS identifier, full label/definition/form metadata | supports | The current term label is exact. Valid agar, water and sodium-carbonate identities do not establish complex commercial-product equivalence. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact current secondary keys and metadata-pinned preferred rows | context_only | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| jcm258-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=258; Preserved exact public retrieval result | context_only | Current JCM258 returned HTTP200 with Nothing found, not a formulation. TOGO M250 is usable as its explicitly attributed source snapshot; present primary correspondence remains unavailable. |
| compound1844Identity-attempt | https://mediadive.dsmz.de/rest/compound/1844; Preserved exact public retrieval result | context_only | Preserved optional source attempt compound 1844Identity did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| komodo604detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=604; Preserved exact public retrieval result | context_only | Preserved optional source attempt komodo604detail did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ119api-attempt | https://mediadive.dsmz.de/rest/medium/J119; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ119api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1329api-attempt | https://mediadive.dsmz.de/rest/medium/J1329; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1329api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ150api-attempt | https://mediadive.dsmz.de/rest/medium/J150; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ150api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ455api-attempt | https://mediadive.dsmz.de/rest/medium/J455; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ455api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ258api-attempt | https://mediadive.dsmz.de/rest/medium/J258; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ258api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ655api-attempt | https://mediadive.dsmz.de/rest/medium/J655; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ655api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1202api-attempt | https://mediadive.dsmz.de/rest/medium/J1202; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1202api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ118api-attempt | https://mediadive.dsmz.de/rest/medium/J118; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ118api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1001api-attempt | https://mediadive.dsmz.de/rest/medium/J1001; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1001api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1016api-attempt | https://mediadive.dsmz.de/rest/medium/J1016; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1016api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadive604api-attempt | https://mediadive.dsmz.de/rest/medium/604; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadive604api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ119api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J119; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ119api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1329api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J1329; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1329api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ150api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J150; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ150api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ455api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J455; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ455api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ258api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J258; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ258api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ655api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J655; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ655api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1202api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J1202; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1202api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ118api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J118; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ118api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1001api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J1001; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1001api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadiveJ1016api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J1016; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadiveJ1016api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| mediadive604api_retry-attempt | https://mediadive.dsmz.de/rest/medium/604; Preserved exact public retrieval result | context_only | Preserved optional source attempt mediadive604api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads. |
| history-metadata | data/merge_yaml/merged/BCYE_AGAR.yaml; data/normalized_yaml/bacterial/1_10_r2a_agar.yaml; data/normalized_yaml/bacterial/1_2_r2a_agar.yaml; data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml; data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml; data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml; data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml; data/normalized_yaml/bacterial/bacto_marine_agar.yaml; data/normalized_yaml/bacterial/me_agar.yaml; data/normalized_yaml/bacterial/modified_gam_agar.yaml; data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml; data/normalized_yaml/specialized/bacto_marine_agar.yaml; data/normalized_yaml/specialized/marine_agar_2216.yaml; data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml; data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:00.929316"}]}, {"input": "data/normalized_yaml/bacterial/me_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/marine_agar_2216.yaml", "events": 15, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml", "events": 9, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:27:23.692601"}, {"index": 4, "issue": "timezone absent", "value": "2026-04-04T21:48:41.239097"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T21:56:22.581264"}]}, {"input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml", "events": 9, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:27:23.695740"}, {"index": 4, "issue": "timezone absent", "value": "2026-04-04T21:48:41.244258"}, {"index": 5, "issue": "timezone absent", "value": "2026-04-04T21:57:43.660477"}]}] |
| writer-0 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-3 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-4 | scripts/repair_jcm_bcye_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-5 | scripts/repair_jcm_corn_meal_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-6 | scripts/repair_togo_sparse_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-7 | scripts/repair_togo_m455_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-8 | scripts/repair_dsmz_604_bacto_marine_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-9 | scripts/repair_jcm_sparse_siblings_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-10 | scripts/repair_official_simple_score20.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| writer-11 | scripts/repair_jcm_specialized_marine_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current relevant guards, formulation constructors and application functions were inspected. Specific repairs already restore opaque products, water, stages and variant links. The carbonate constructors explicitly encode PERCENT_W_V although inspected collection sources print only 10%. Current guarded merger/cleanup code is not proof of the historical execution causing the stale false merge; broad unrelated recipes in repair_official_simple_score20.py were not reviewed. |
| report-scope | /private/tmp/culturemech-review-work-batch040/395/report-scope-inventory.json; Exact local field objects and pinned source joins | context_only | Exact record-path/ID joins distinguish maintained-owner historical reports from dependency/namesake reports; historical decisions are derivative context, not current response authentication. |
| relationships | /private/tmp/culturemech-review-work-batch040/395/relationship-scope-inventory.json; Exact local field objects and pinned source joins | context_only | Exact local path/ID joins are preserved. Thirteen relationship records and three 395 namesakes are context, not additional maintained contributors; the fourth global exclusion belongs to 393. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch040/395/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current JCM258 returned HTTP200 with Nothing found, not a formulation. TOGO M250 is usable as its explicitly attributed source snapshot; present primary correspondence remains unavailable.
- Preserved optional source attempt compound 1844Identity did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt komodo604detail did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ119api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1329api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ150api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ455api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ258api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ655api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1202api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ118api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1001api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1016api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadive604api did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ119api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1329api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ150api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ455api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ258api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ655api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1202api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ118api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1001api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1016api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadive604api_retry did not provide usable response content. Available exact primary/provider captures supply the bounded comparisons; failed attempts do not authenticate older payloads.
- TOGO M2859 has an empty original-source URL and only an unspecified one-litre BCYE component. Its exact formulation, supplier and original experiment remain unresolved.
- The exact DSM604 page names Difco 0979 but supplies neither amount nor preparation. Both maintained VARIABLE values are appropriate; borrowing the J118 dose would require evidence of equivalence.
- The scoped R2A parent contains a PMID:3883894 excerpt without a captured paper response. Its original quotation is not independently authenticated here; current JCM346 supports a separate formulation comparison.
- The source pages and provider captures support recipe comparisons, not measured final volumes, vendor-lot equivalence, fresh experimental growth or complete commercial-product compositions.
- The full KG ingredient graph was not recomputed; the separately confirmed medium 12 identity conflict does not supply a replacement match.
- Relationship-only descendants and excluded namesakes are not extra contributor reviews. In particular no DSM585a source or independent formulation is borrowed for M2859.
- This scientific assessment precedes formal review validation and saving; those outcomes are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T223742Z-culturemech-002367-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bcye_agar (CultureMech:002367)'
started_at: '2026-10-21T22:32:18Z'
finished_at: '2026-10-21T22:37:42Z'
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
summary: The generated BCYE record combines fifteen distinct maintained formulations
  and retains a dilute R2A recipe under JCM119 identity. Most maintained contributors
  already preserve their commercial products and preparation; reconcile their remaining
  source limits and regenerate only compatible formulations. The false R2A-to-agar
  link, unsupported percentage bases and unrelated soil-extract graph accession need
  separate correction.
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
  - path: data/merge_yaml/merged/BCYE_AGAR.yaml
    sha256: c97935ded0e4038da8fc740939038d67a62ed91bbab1f9459beb024614cfec80
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    sha256: 071e5fd27ac097af23cab67768be3bfbd45117d65a2fd06fbf3044c799238585
    role: context
  - path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    sha256: d1d078b1576bf5e3a3552ce3c24ad265936d4f3a6abc834fae5a5822dda9fc05
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    sha256: 0ac79b672e2fc24abd97d23ad1cd1c0b6473f8cf636804312f2eb3c6376923ab
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    sha256: 7b1ac9847f91ca75443301c9996b7380f3ee0132c569b783caa0e05aafe0ad50
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    sha256: 676a1399ad6951cf4b56a95b7afde75a9c3e7e4015275e276fae3eb78616116e
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M111_BCYE_Agar.yaml
    sha256: f25e03c74243c4b2770281054b505113f43ea1c3dc8a972dbc6887ef1cc83b8a
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M141_Corn_Meal_Agar.yaml
    sha256: 1e3aca5d503d621313d56e8355d176f264dbb30d198e9bd03ece6d5aba7221ff
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    sha256: 098956157992d01f3bbeabd20f4b5853a036dea4eab56e49ae7af0b99dd24a59
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M3004_Corn_Meal_Agar.yaml
    sha256: 7d79ba3f71eb7d1cac40b2dd0bd77541fb8fc7c7996fd2e88f4cdc66be8689ff
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M455_Alkali-Reinforced_Clostridial_Agar.yaml
    sha256: 42ea3ad0c8e46a9e4842df153d37e3aac44148fff251eb9e26a962beff7ca8ae
    role: context
  - path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    sha256: 64e497cd9800e914b41d9f8d20dc66efd06cdaa35d22ede0eaab586595c30b3d
    role: context
  - path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    sha256: b1415b4cbb30bedbc2b26bdd1b03096af51369b55f660fa4ec1c3706b37786f2
    role: context
  - path: data/normalized_yaml/bacterial/marine_agar_2216.yaml
    sha256: c0cdde18441518ff2fa685ee0c367fd82257714fd969f9f92ce8cf1ba4797c3d
    role: context
  - path: data/normalized_yaml/bacterial/marine_agar_2216_ph_8_5.yaml
    sha256: 759dac80baebf7fd43e05f0101ca3f3b368c6c225fa7268ba31aa23d9b090e77
    role: context
  - path: data/normalized_yaml/bacterial/marine_agar_2216_ph_9_0.yaml
    sha256: eb0cf6d6dc086d833d8ab50d522bc0bb99b0413b9f0458f3ef8fbf0c342e8505
    role: context
  - path: data/normalized_yaml/bacterial/me_agar.yaml
    sha256: 84ef2fa07201d1bf46cc5e9ba73ec57aaa337e0501851c7084ef53753c6b2aab
    role: context
  - path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    sha256: 94fc34d2cfc860f413b89658c99daf97676848c45de08559771f30876a26ccbc
    role: context
  - path: data/normalized_yaml/bacterial/r2a_agar.yaml
    sha256: 9fb62888e57c7e55e01e04b49ac366b47ca1d2485e4932e1b1fab9eb0fdd14ab
    role: context
  - path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    sha256: be0f5b70c75d7ea796f86cb7f65c83f4d7a2eb4a7d7bd4f4d4c6f8424ab8316f
    role: context
  - path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    sha256: eefc9fb9382bedcd2509d964a301b39331e5ce36e976b414cf061e09ed37d4ab
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    sha256: cf8f1c2646ecf4f35e69c87cc44f703a212e715eecab168a1f3a96663c33f02d
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    sha256: 56bf60211962148cff86ad17de7f92cb9b70f78301e52163d5ef022f0c4af12b
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    sha256: e4a25a0016b76efb3eba713e5f2c0919cd0a0c1e31da2c5c3e2de8136334805f
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml
    sha256: 5f1687b204c399a022ea71dc3d34ba0bb0fa950431e87b87871a014cb4785550
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml
    sha256: c7cfe9017a933dde67753d6199a9b56f8d01dd305e85c082d434de915e84ea32
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml
    sha256: d7c6b00f81f3c49dfa037aa1dbc63e3be98da9c914d98c065032c2d80c1353db
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml
    sha256: d9ad962cf75037a1549ce33ed9d2eb6d055912704a1822009d9756e543f157b3
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml
    sha256: fec31e7fc913651cb497b66a47da34bd2cf24411891de2443a2f545704577a3f
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml
    sha256: b1fbfbfed0303b1625908eb48f5715c047e540df674a6173ca666e2a4c472fbe
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml
    sha256: 922b0636f28904f792fe7c9dc6ba102810bb4fd9a126e64493b7aa9ad60df9ae
    role: context
  - path: data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml
    sha256: 90c6d5c207dd20ffd8293c68fb3d628720c442988d8545df1e4789513d329335
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_585_BCYE_AGAR.yaml.md
    sha256: c52d4aa07e176deb9c0d3e027ebd9fdae84e5f6e86b490185392231a5039f46b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/bacto_marine_agar.yaml.md
    sha256: f409b9842313b1b170f6e732388e0da377aae6d206cb83ed47992191d878a7bb
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/specialized/bacto_marine_agar.yaml.md
    sha256: db4788c2cd6ca36e388fa7f4e3dd60fcb25b10a87e48bafb44d19500f2023e18
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J119_BCYE_AGAR.yaml.md
    sha256: 2b3579babfde5d4ea1d743bc05b346b205851b625a9603c8f79a28f7014e6172
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml.md
    sha256: 766c76d071af9373296b68d5533640ce527648d1d75700535483570d14e8d875
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/alkali_reinforced_clostridial_agar.yaml.md
    sha256: 71949eee7de509eb0ab14d67e5c0d4a55be1f15bea84cbf8c5d22e4073448b06
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/me_agar.yaml.md
    sha256: 8f443f7b26b32cd3d9f07fd269e0821698fe83ffc6fb77aa0406b5abb0e1acb8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/specialized/marine_agar_2216.yaml.md
    sha256: 818addf6e0b9fae966aa96a6e075763d05eb4d9e79fc014cc715a06a78fb0665
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/specialized/marine_agar_2216_with_3_1_nacl.yaml.md
    sha256: 81cabd00aa4eeab9fa59d5c24a89ae17f9a50ecfdd04370a91a0ee7e3b745e5f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/1_10_r2a_agar.yaml.md
    sha256: 6db85c31096a0e1796012ca595a066b0be08e6f9a60f40f2e10e030019f62966
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/1_2_r2a_agar.yaml.md
    sha256: 35d9f960395ba4fc59ddc7abdefa79c959a215bc7aa3d4a698ccdf22b770ba95
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/modified_gam_agar.yaml.md
    sha256: b1da4974633fb9167b5c6f3f69c6238765bc8c83e07bfbeeed66e65c9356c170
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/marine_agar_2216_ph_8_5.yaml.md
    sha256: a983d3d6fae6bf2a976205ec1d4d2a14969964918238e8011849ee4cedb702db
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/marine_agar_2216_with_10_nacl.yaml.md
    sha256: 48a9578ed637f2dd163832a34c8eebbcc00234e494ee13347fff82eb9c2636d7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/marine_agar_2216_with_1_nacl.yaml.md
    sha256: cd4f1af9e57d6061e994470fb1791061df6a94911cc3e422a3b912454cf65559
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/marine_agar_2216_with_5_nacl.yaml.md
    sha256: 1a8313dba042141ca0825ca75300180ec72364cb3591218eca913a9f73edbfef
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/marine_agar_2216_with_8_nacl.yaml.md
    sha256: 5c33d331f15f1e45eaf83ecc1a5a9d8f63dc6ef750dbb24ff97d5d24d053d7f1
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml.md
    sha256: ed1eee15e2a2b0601b480e1f63f7904fa638e52889c69d94368d883f24d7c23d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/weak_oatmeal_agar.yaml.md
    sha256: 51926fdea1c5682cdc7fed320d9235b3f4e22c4d3775e4848783f46eb1e7b106
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/specialized/marine_agar_2216_ph_9_0.yaml.md
    sha256: 2526f36a8761f56695a324be57c4d18124f9efcfa84683d8c7da754eb8812395
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/specialized/marine_agar_2216_with_1_starch.yaml.md
    sha256: 07e3976adf42256d2e20cf5dc66e13a303bc47029a201efb62f2825bbd53540b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/specialized/marine_agar_2216_with_8_0_nacl.yaml.md
    sha256: bfb5f8d6fed16bccbd1809be60194ed55e49ccb17305046f1d1a276362cfa155
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/specialized/modified_marine_agar_2216.yaml.md
    sha256: f330e56dc6471f29263e134b543508cc2ad542b8c3ab2109db927cb97811b123
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BCYE_AGAR.md
    sha256: 2f4f76a2aada213b2d2944beb0b963ca698f81ebdd267882464c42243221d15f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/alkali_reinforced_clostridial_agar.md
    sha256: ea9efe349ec5b1d0e79be09b0df0fbbb0325efcabb4c8a04bf64b9c702e5af36
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/marine_agar_2216__5672d6e3.md
    sha256: 904e43fc2c4336763511be26b40c5f62401b403d10db47cc31e85d33eb559ef1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.md
    sha256: ab55cf35aed20a97633bd64b755d3b8169d5992175aa28bbfc0b445511fd2020
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/modified_marine_agar_2216__e26e71e7.md
    sha256: 5338b894afda0dad80152611259bc72e0640c86dd18fa20db7f85cd15be14473
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/1_10_r2a_agar.md
    sha256: 790d2c6971f18732047abd10739b2cb609f5ba8b9a69bf5d8c06f13d8be31a77
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/1_2_r2a_agar.md
    sha256: 2af1f07432655047c7448260cc88086c87dbd4f9fa4091caedeccb8f61c4a6b3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.md
    sha256: 6074a0c174b39d6689a7bd913a80a547f10619f0670170c314cbb9be0e4d8071
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.md
    sha256: b34f58703f86b0aa22ec1df67e9902863e0e03b68ec64573b4db84b1cb302d7e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.md
    sha256: 0b5bddc1e343e7f188607d1e42856d25030f0667b9ad9a6eeb4442b923ed019c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_585_BCYE_AGAR.md
    sha256: be1e002db4869c65503e51fe9d27dc013d6c656b5615f265d880fc38bd8042d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.md
    sha256: e432f7ea23b643eb348f25f5e81bd7d3eb2fa3228d6d46e96a7e9db35b5298a3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.md
    sha256: a67bf314a307407cdb21c3157a8aaa3628d947bbb5ea1ba4aadef96c0fc7e6e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/bacto_marine_agar.md
    sha256: c373cb04412d6c9b1b52511465ea3fac10a922c2a022b89b806e991c38ea00de
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/marine_agar_2216.md
    sha256: 95755a5ae4839bf81e43a3c7be7a4f59e9d83a2795ade1d98e2cbee89b87b1e7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/marine_agar_2216_ph_8_5.md
    sha256: ffc8b71a4e20aef2d1192948f6eab0a52642c67dc0485ea5a135f9c0b7802c07
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/marine_agar_2216_ph_9_0.md
    sha256: 81fe7f7a5c0bd2967be9d2c807a2452a484d8530302518be6636adf392730ab9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/me_agar.md
    sha256: 54e34fa5a19aca9b055a7c5647bbd7b9b8da748565db7be133410ffba20a1ddc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/modified_gam_agar.md
    sha256: bff1fb9eb8b870dc4e54d26197799175b0d69b76682f4af651bb6ec00d36e340
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/modified_marine_agar_2216.md
    sha256: 2a899e9c08b20a8ddd4d4226aa9c031ac5727b255fcf9f7e573cce08c31426d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/weak_oatmeal_agar.md
    sha256: 17474e45cdbad3b2913209e527fb87bf711d13416b088a8b4c3b88e3c323ec68
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bacto_marine_agar.md
    sha256: 4f4a12278c5eef11d958fdfcf3e7ccd31d4a61e184d247e30fe46e446f443549
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/marine_agar_2216.md
    sha256: 61eb642c30c5af0346ed6109c8b0f0dd27e6ddbc28dd8ea7f6ae777ad3afb0e5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/marine_agar_2216_ph_8_5.md
    sha256: 1339274a8cb042681097f8155c091e766743dd3590683dd42cbeee5fd194f314
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/marine_agar_2216_ph_9_0.md
    sha256: 94238c25621dfe6b8bc4774080f41e5ca2fe507f003b7e9a8eae675e956c4a3d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/modified_marine_agar_2216.md
    sha256: 19fe58bc7556a26bab4f1f05562265c87094ca19370b78513e9ef894740c17ef
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
  - path: scripts/migrate_data_quality_flags.py
    sha256: 592c531870ab22cbdeeed5fc8fc8d9d0b42d3a6a75c2c54acc3d0c77b566b693
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_dsmz_604_bacto_marine_score20.py
    sha256: 831add00fbabb792f82d2ce76441456e97186189d90f5a2eda668c8147633978
    role: context
  - path: scripts/repair_jcm_bcye_score20.py
    sha256: a2f81fc22fbcef086eea686cdc37829ec9318bdfd54a3fa751d5219d5c732625
    role: context
  - path: scripts/repair_jcm_corn_meal_score20.py
    sha256: b67c2b421df5c561900e05582f0cf016e57d1da4abf458f9f9d4cce0dd92c752
    role: context
  - path: scripts/repair_jcm_sparse_siblings_score20.py
    sha256: ce83fdb9564a6647addbc1fdbcae80bdf9ab450c0bac55bdcae31f8509b05cde
    role: context
  - path: scripts/repair_jcm_specialized_marine_score15.py
    sha256: d705b2335c832feec4ffe29e9776c2c0c718236dc79a1181fd03814fa26964ba
    role: context
  - path: scripts/repair_mixed_score10_exact_terms_batch8.py
    sha256: 6ca89181525efe625a9a64834bb11abbb7510567bd8f5c76e87d637bd0adbb45
    role: context
  - path: scripts/repair_official_simple_score20.py
    sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
    role: context
  - path: scripts/repair_togo_m455_score15.py
    sha256: 3ed1dfe6c76be35bef5dfa4f0bdebca0d5d04cc8ecf9cee320f89499320f4587
    role: context
  - path: scripts/repair_togo_m958_modified_marine_score15.py
    sha256: 883c249aba5e93fc6fc649835588eabc66a4aaff928041483ad97fe2dc4758a6
    role: context
  - path: scripts/repair_togo_sparse_score20.py
    sha256: f037c69b09b6a5a8c1f17127ae2a2160477e73a6a6d172bfbc0fffd7fc2d263d
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 395; batch 040 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-nine task batches
    contain 390 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 393 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002367
targets:
- target_id: CultureMech:002367
  path: data/merge_yaml/merged/BCYE_AGAR.yaml
  label: bcye_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BCYE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BCYE_AGAR.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch040/395/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/395/strict.tsv"
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BCYE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BCYE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002367
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
  - CultureMech:002367
- check_id: jcm258-source-access
  name: 'Exact source content access: jcm258'
  required: true
  status: unavailable
  summary: Current JCM258 returned HTTP200 with Nothing found, not a formulation.
    TOGO M250 is usable as its explicitly attributed source snapshot; present primary
    correspondence remains unavailable.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - jcm258-attempt
- check_id: compound1844Identity-source-access
  name: 'Exact source content access: compound1844Identity'
  required: false
  status: unavailable
  summary: Preserved optional source attempt compound 1844Identity did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - compound1844Identity-attempt
- check_id: komodo604detail-source-access
  name: 'Exact source content access: komodo604detail'
  required: false
  status: unavailable
  summary: Preserved optional source attempt komodo604detail did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - komodo604detail-attempt
- check_id: mediadiveJ119api-source-access
  name: 'Exact source content access: mediadiveJ119api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ119api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ119api-attempt
- check_id: mediadiveJ1329api-source-access
  name: 'Exact source content access: mediadiveJ1329api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1329api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1329api-attempt
- check_id: mediadiveJ150api-source-access
  name: 'Exact source content access: mediadiveJ150api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ150api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ150api-attempt
- check_id: mediadiveJ455api-source-access
  name: 'Exact source content access: mediadiveJ455api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ455api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ455api-attempt
- check_id: mediadiveJ258api-source-access
  name: 'Exact source content access: mediadiveJ258api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ258api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ258api-attempt
- check_id: mediadiveJ655api-source-access
  name: 'Exact source content access: mediadiveJ655api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ655api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ655api-attempt
- check_id: mediadiveJ1202api-source-access
  name: 'Exact source content access: mediadiveJ1202api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1202api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1202api-attempt
- check_id: mediadiveJ118api-source-access
  name: 'Exact source content access: mediadiveJ118api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ118api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ118api-attempt
- check_id: mediadiveJ1001api-source-access
  name: 'Exact source content access: mediadiveJ1001api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1001api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1001api-attempt
- check_id: mediadiveJ1016api-source-access
  name: 'Exact source content access: mediadiveJ1016api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1016api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1016api-attempt
- check_id: mediadive604api-source-access
  name: 'Exact source content access: mediadive604api'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadive604api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadive604api-attempt
- check_id: mediadiveJ119api_retry-source-access
  name: 'Exact source content access: mediadiveJ119api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ119api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ119api_retry-attempt
- check_id: mediadiveJ1329api_retry-source-access
  name: 'Exact source content access: mediadiveJ1329api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1329api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1329api_retry-attempt
- check_id: mediadiveJ150api_retry-source-access
  name: 'Exact source content access: mediadiveJ150api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ150api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ150api_retry-attempt
- check_id: mediadiveJ455api_retry-source-access
  name: 'Exact source content access: mediadiveJ455api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ455api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ455api_retry-attempt
- check_id: mediadiveJ258api_retry-source-access
  name: 'Exact source content access: mediadiveJ258api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ258api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ258api_retry-attempt
- check_id: mediadiveJ655api_retry-source-access
  name: 'Exact source content access: mediadiveJ655api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ655api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ655api_retry-attempt
- check_id: mediadiveJ1202api_retry-source-access
  name: 'Exact source content access: mediadiveJ1202api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1202api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1202api_retry-attempt
- check_id: mediadiveJ118api_retry-source-access
  name: 'Exact source content access: mediadiveJ118api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ118api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ118api_retry-attempt
- check_id: mediadiveJ1001api_retry-source-access
  name: 'Exact source content access: mediadiveJ1001api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1001api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1001api_retry-attempt
- check_id: mediadiveJ1016api_retry-source-access
  name: 'Exact source content access: mediadiveJ1016api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadiveJ1016api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadiveJ1016api_retry-attempt
- check_id: mediadive604api_retry-source-access
  name: 'Exact source content access: mediadive604api_retry'
  required: false
  status: unavailable
  summary: Preserved optional source attempt mediadive604api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - mediadive604api_retry-attempt
- check_id: m2859-original-formulation
  name: Original source and exact BCYE formulation for M2859
  required: true
  status: unavailable
  summary: TOGO M2859 has an empty original-source URL and only an unspecified one-litre
    BCYE component. Its exact formulation, supplier and original experiment remain
    unresolved.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - togo-bcye
- check_id: dsm604-dose
  name: Source-specific DSM604 product dose and preparation
  required: true
  status: unavailable
  summary: The exact DSM604 page names Difco 0979 but supplies neither amount nor
    preparation. Both maintained VARIABLE values are appropriate; borrowing the J118
    dose would require evidence of equivalence.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - dsmz604
- check_id: r2a-paper-history
  name: Historical R2A parent-paper correspondence
  required: true
  status: unavailable
  summary: The scoped R2A parent contains a PMID:3883894 excerpt without a captured
    paper response. Its original quotation is not independently authenticated here;
    current JCM346 supports a separate formulation comparison.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - jcm346
  - history-inventory
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BCYE_AGAR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-6
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-7
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-8
  kind: record_content
  reference: data/normalized_yaml/bacterial/me_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-9
  kind: record_content
  reference: data/normalized_yaml/bacterial/modified_gam_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-10
  kind: record_content
  reference: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-11
  kind: record_content
  reference: data/normalized_yaml/specialized/bacto_marine_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-12
  kind: record_content
  reference: data/normalized_yaml/specialized/marine_agar_2216.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-13
  kind: record_content
  reference: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-14
  kind: record_content
  reference: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BCYE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:37.848581Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BCYE_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch040/395/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:38.869367Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/395/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BCYE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:40.019991Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BCYE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:40.737394Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:37:40Z'
  support: supports
  summary: './data/merge_yaml/merged/BCYE_AGAR.yaml:1:id: CultureMech:002367

    ./data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml:1:id: CultureMech:002367

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/source-preflight-bound/395/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:37:40Z'
  support: supports
  summary: 66 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 780273c88107754244e9f97e1457f40a7d359a7d36ccba2295d26418b556b8a4
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/395/history-inventory.json
  locator: Exact local field objects and pinned source joins
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Complete current histories and empty receiving-layer evidence arrays; the
    single R2A parent-paper claim remains separately scoped and unauthenticated.
  snapshot_sha256: 0d497c839a42dc0cae115478066460947399cbaa8b54b26c53daba66ee7f68fa
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/395/grounding-inventory.json
  locator: Exact local field objects and pinned source joins
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Every asserted ingredient ontology, provider or local record link is retained
    with exact metadata; source-specific identity is assessed independently.
  snapshot_sha256: 5431dd7401dc24c4ed0f520c61995019041c646a9a5a98494ae5da14b4ea746a
- evidence_id: jcm119
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:01.792530Z'
  support: supports
  summary: JCM119 specifies BCYE base, Legionella enrichment and water; the target
    R2A ingredients are a different formulation.
  quote: BCYE agar (BD-Difco) 37.0 g Legionella agar enrichment (BD-Difco) 100.0 ml
    Distilled water 900.0 ml
  snapshot_sha256: d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c
- evidence_id: jcm804
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-20T06:52:54.978426Z'
  support: supports
  summary: J804 is the separate dilute R2A contributor.
  quote: R2A agar (BD-Difco) 1.82 g Agar 15.0 g Distilled water 1.0 L
  snapshot_sha256: 3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09
- evidence_id: jcm845
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-20T06:52:49.130948Z'
  support: supports
  summary: J845 is a different R2A dilution and added-agar amount.
  quote: R2A agar (BD-Difco) 9.1 g Agar 7.5 g Distilled water 1.0 L
  snapshot_sha256: 5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7
- evidence_id: jcm346
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T08:23:35.784072Z'
  support: supports
  summary: R2A parent formulation applies only to its exact R2A children.
  quote: 'Comment: The premixed powder is available from Becton Dickinson & Co. as
    Difco R2A Agar.'
  snapshot_sha256: 63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb
- evidence_id: jcm1329
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:02.160475Z'
  support: supports
  summary: The Nissui corn-meal product is not silently equated to BD-Difco.
  quote: Corn meal agar (Nissui) 17.0 g Distilled water 1.0 L
  snapshot_sha256: ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723
- evidence_id: jcm150
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:02.305352Z'
  support: supports
  summary: The BD-Difco corn-meal product remains a distinct source identity.
  quote: Corn meal agar (BD-Difco) 17.0 g Distilled water 1.0 L
  snapshot_sha256: 1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478
- evidence_id: jcm455
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:02.786345Z'
  support: supports
  summary: The carbonate is a separate late addition; percentage basis is unspecified.
  quote: After autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to
    the medium. Check final pH to be about 10.0.
  snapshot_sha256: 14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53
- evidence_id: jcm655
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:02.786470Z'
  support: supports
  summary: Modified GAM is a Nissui product, not BCYE or agar alone.
  quote: GAM agar, modified (Nissui) 56.7 g Distilled water 1.0 L
  snapshot_sha256: 78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53
- evidence_id: jcm1202
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:02.160415Z'
  support: supports
  summary: Oatmeal product and additional agar remain separate.
  quote: Oatmeal agar (BD-Difco) 15.0 g Agar 12.0 g Distilled water 1.0 L
  snapshot_sha256: 11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc
- evidence_id: jcm118
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:01.720158Z'
  support: supports
  summary: The J118 marine product has an explicit mass and water entry.
  quote: Marine agar 2216 (BD-Difco) 55.1 g Distilled water 1.0 L
  snapshot_sha256: e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129
- evidence_id: jcm1001
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:01.213429Z'
  support: supports
  summary: The pH 8.5 wrapper changes the J118 base after autoclaving; carbonate dose
    and percentage basis are not given.
  quote: After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.
  snapshot_sha256: b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084
- evidence_id: jcm1016
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:01.384290Z'
  support: supports
  summary: The pH 9 wrapper is distinct from the pH 8.5 wrapper.
  quote: After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.
  snapshot_sha256: 026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d
- evidence_id: dsmz604
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:15:00.516090Z'
  support: supports
  summary: DSM604 supplies product identity but no product mass or water dose.
  quote: MARINE AGAR 2216 (Difco 0979).
  snapshot_sha256: 9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24
- evidence_id: dsmz12GraphIdentity
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf
  locator: Complete primary formulation and relevant preparation; exact quoted text
  accessed_at: '2026-10-21T22:20:35.501603Z'
  support: supports
  summary: The asserted graph accession resolves to soil-extract medium, an identity
    cross-check only.
  quote: 12. SOIL EXTRACT MEDIUM
  snapshot_sha256: 1b4394336f7ace4e09c66fc67ed2e745e3c633b725e436d94335b99289243580
- evidence_id: default-autoclave
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119
  locator: Page-wide instruction, applying unless the recipe states otherwise
  accessed_at: '2026-10-21T22:15:01.792530Z'
  support: supports
  summary: The default is sterilization, not an incubation condition.
  quote: Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.
  snapshot_sha256: d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c
- evidence_id: r2a-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J804
  locator: $.data.solutions[0].recipe[0] versus recipe[1]
  accessed_at: '2026-10-20T06:52:56.572648Z'
  support: supports
  summary: The provider explicitly distinguishes compound 1844 R2A agar (BD-Difco)
    from compound 3 agar.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"R2A agar\",\n                        \"compound_id\": 1844,\n\
    \                        \"attribute\": \"BD-Difco\",\n                      \
    \  \"amount\": 1.82,\n                        \"unit\": \"g\",\n             \
    \           \"g_l\": 1.82,\n                        \"optional\": 0\n        \
    \            }"
  snapshot_sha256: 87014fc2e2dfa41bd8598b3acb07e8f9127962e310c79f46a3870d80c95427a6
- evidence_id: graph-identity
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/12
  locator: $.data.medium and $.data.solutions[0]
  accessed_at: '2026-10-21T06:55:22.017167Z'
  support: supports
  summary: Accession12 denotes SOIL EXTRACT MEDIUM. The response is not a KG ingredient-match
    proof.
  quote: '"name": "SOIL EXTRACT MEDIUM"'
  snapshot_sha256: aae1357e31d914ca483bea213eafb7d4a462aa252fc9008b483e42791202bd8b
- evidence_id: togo-bcye
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859
  locator: $.meta.src_url, $.components[0].items[0], $.comments[0]
  accessed_at: '2026-10-21T22:14:58.932072Z'
  support: supports
  summary: One litre of unspecified BCYE and the Paris/Lens 37 C for 3 d statement
    are provider-scoped, with no original source URL.
  quote: '"src_url": ""'
  snapshot_sha256: ede4a337bb29494b8e3ba5121c94fcfd933e1b19d98916349209f5a56ff133b4
- evidence_id: togo-me
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250
  locator: $.meta.original_media_id, $.components[0].items, $.comments[0]
  accessed_at: '2026-10-21T22:14:58.404282Z'
  support: supports
  summary: TOGO explicitly snapshots JCM_M258 with 50 g Oxoid product, 1 L water and
    115 C/10 min. Current JCM258 has no recipe.
  quote: '"original_media_id": "JCM_M258"'
  snapshot_sha256: 0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a
- evidence_id: togoM111relationship
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M111
  locator: $.meta original source identity and component rows
  accessed_at: '2026-10-21T22:16:28.925468Z'
  support: supports
  summary: The exact TOGO source duplicate is a relationship check only; it is not
    an additional contributor.
  snapshot_sha256: e745fa5360d1c561400ac4adfffd9b340bbb3f7536d3aec1288e803495ae9586
- evidence_id: togoM3004relationship
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3004
  locator: $.meta original source identity and component rows
  accessed_at: '2026-10-21T22:16:29.388761Z'
  support: supports
  summary: The exact TOGO source duplicate is a relationship check only; it is not
    an additional contributor.
  snapshot_sha256: bc5da0a3d18dad0b17ce2e3f4adc0891c5d1a242ac26cdc4e12905d7868534b3
- evidence_id: togoM141relationship
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M141
  locator: $.meta original source identity and component rows
  accessed_at: '2026-10-21T22:16:29.350387Z'
  support: supports
  summary: The exact TOGO source duplicate is a relationship check only; it is not
    an additional contributor.
  snapshot_sha256: 7b863d88be9bcf8e155dd87e26b734c3abbd51dc96629877098471803b66ebd3
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS identifier, full label/definition/form metadata
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: The current term label is exact. Valid agar, water and sodium-carbonate
    identities do not establish complex commercial-product equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, full label/definition/form metadata
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: The current term label is exact. Valid agar, water and sodium-carbonate
    identities do not establish complex commercial-product equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact OLS identifier, full label/definition/form metadata
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: The current term label is exact. Valid agar, water and sodium-carbonate
    identities do not establish complex commercial-product equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact current secondary keys and metadata-pinned preferred rows
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: jcm258-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=258
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:15:02.363859Z'
  support: context_only
  summary: Current JCM258 returned HTTP200 with Nothing found, not a formulation.
    TOGO M250 is usable as its explicitly attributed source snapshot; present primary
    correspondence remains unavailable.
  snapshot_sha256: c56a4eee2e914ee349b511c21f47a14b1deeb1baaaf0b623928077183a6ebad3
- evidence_id: compound1844Identity-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/compound/1844
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:20:35.501253Z'
  support: context_only
  summary: Preserved optional source attempt compound 1844Identity did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo604detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=604
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:55.641665Z'
  support: context_only
  summary: Preserved optional source attempt komodo604detail did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 14d5ecbb432efdf725daf052a79d0935b6c34770a61edf9fa130ef930bb7a26e
- evidence_id: mediadiveJ119api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J119
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:56.800083Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ119api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1329api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1329
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.346523Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1329api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ150api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J150
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.348701Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ150api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ455api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J455
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.850147Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ455api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ258api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J258
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.357134Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ258api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ655api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J655
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.891367Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ655api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1202api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1202
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:57.327652Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1202api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ118api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J118
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:56.776420Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ118api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1001api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1001
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:56.771900Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1001api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1016api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1016
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:56.776363Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1016api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive604api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/604
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:14:56.015362Z'
  support: context_only
  summary: Preserved optional source attempt mediadive604api did not provide usable
    response content. Available exact primary/provider captures supply the bounded
    comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ119api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J119
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:27.807473Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ119api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1329api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1329
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.353398Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1329api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ150api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J150
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.383865Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ150api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ455api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J455
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.831223Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ455api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ258api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J258
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.386040Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ258api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ655api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J655
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.870697Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ655api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1202api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1202
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:28.310740Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1202api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ118api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J118
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:27.791168Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ118api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1001api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1001
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:27.785072Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1001api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ1016api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1016
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:27.790936Z'
  support: context_only
  summary: Preserved optional source attempt mediadiveJ1016api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive604api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/604
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:16:27.168689Z'
  support: context_only
  summary: Preserved optional source attempt mediadive604api_retry did not provide
    usable response content. Available exact primary/provider captures supply the
    bounded comparisons; failed attempts do not authenticate older payloads.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BCYE_AGAR.yaml; data/normalized_yaml/bacterial/1_10_r2a_agar.yaml;
    data/normalized_yaml/bacterial/1_2_r2a_agar.yaml; data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml;
    data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml; data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml;
    data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml; data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml;
    data/normalized_yaml/bacterial/bacto_marine_agar.yaml; data/normalized_yaml/bacterial/me_agar.yaml;
    data/normalized_yaml/bacterial/modified_gam_agar.yaml; data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml;
    data/normalized_yaml/specialized/bacto_marine_agar.yaml; data/normalized_yaml/specialized/marine_agar_2216.yaml;
    data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml; data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/1_10_r2a_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/1_2_r2a_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bacto_marine_agar.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:00.929316"}]}, {"input": "data/normalized_yaml/bacterial/me_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/modified_gam_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bacto_marine_agar.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/marine_agar_2216.yaml",
    "events": 15, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml",
    "events": 9, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:27:23.692601"}, {"index": 4, "issue": "timezone absent", "value":
    "2026-04-04T21:48:41.239097"}, {"index": 5, "issue": "timezone absent", "value":
    "2026-04-04T21:56:22.581264"}]}, {"input": "data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml",
    "events": 9, "timestamp_issues": [{"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:27:23.695740"}, {"index": 4, "issue": "timezone absent", "value":
    "2026-04-04T21:48:41.244258"}, {"index": 5, "issue": "timezone absent", "value":
    "2026-04-04T21:57:43.660477"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-4
  kind: record_content
  reference: scripts/repair_jcm_bcye_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: a2f81fc22fbcef086eea686cdc37829ec9318bdfd54a3fa751d5219d5c732625
- evidence_id: writer-5
  kind: record_content
  reference: scripts/repair_jcm_corn_meal_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: b67c2b421df5c561900e05582f0cf016e57d1da4abf458f9f9d4cce0dd92c752
- evidence_id: writer-6
  kind: record_content
  reference: scripts/repair_togo_sparse_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: f037c69b09b6a5a8c1f17127ae2a2160477e73a6a6d172bfbc0fffd7fc2d263d
- evidence_id: writer-7
  kind: record_content
  reference: scripts/repair_togo_m455_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: 3ed1dfe6c76be35bef5dfa4f0bdebca0d5d04cc8ecf9cee320f89499320f4587
- evidence_id: writer-8
  kind: record_content
  reference: scripts/repair_dsmz_604_bacto_marine_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: 831add00fbabb792f82d2ce76441456e97186189d90f5a2eda668c8147633978
- evidence_id: writer-9
  kind: record_content
  reference: scripts/repair_jcm_sparse_siblings_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: ce83fdb9564a6647addbc1fdbcae80bdf9ab450c0bac55bdcae31f8509b05cde
- evidence_id: writer-10
  kind: record_content
  reference: scripts/repair_official_simple_score20.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
- evidence_id: writer-11
  kind: record_content
  reference: scripts/repair_jcm_specialized_marine_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Current relevant guards, formulation constructors and application functions
    were inspected. Specific repairs already restore opaque products, water, stages
    and variant links. The carbonate constructors explicitly encode PERCENT_W_V although
    inspected collection sources print only 10%. Current guarded merger/cleanup code
    is not proof of the historical execution causing the stale false merge; broad
    unrelated recipes in repair_official_simple_score20.py were not reviewed.
  snapshot_sha256: d705b2335c832feec4ffe29e9776c2c0c718236dc79a1181fd03814fa26964ba
- evidence_id: report-scope
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/395/report-scope-inventory.json
  locator: Exact local field objects and pinned source joins
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Exact record-path/ID joins distinguish maintained-owner historical reports
    from dependency/namesake reports; historical decisions are derivative context,
    not current response authentication.
  snapshot_sha256: 3253041fb56d5217855e848a558c95e0ff92b0566bf8e1d3e5ede3eff1c1c826
- evidence_id: relationships
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/395/relationship-scope-inventory.json
  locator: Exact local field objects and pinned source joins
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Exact local path/ID joins are preserved. Thirteen relationship records
    and three 395 namesakes are context, not additional maintained contributors; the
    fourth global exclusion belongs to 393.
  snapshot_sha256: 35cc4cbafd5177c77493b3025ace6834cdaf3fbc9ace7aa30e37a104c85f2c25
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/395/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:37:40Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ff69c91d65720cf6ba06f59c324b7359d949f80d8a3e31774c63954705efec40
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 116 timestamp instances inspected; 8 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - history-metadata
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
  - owner-11
  - owner-12
  - owner-13
  - owner-14
- assessment_id: identity
  area: identity
  topic: Fifteen contributor identities and stale generated content
  outcome: concern
  summary: JCM119 BCYE has 37 g commercial BCYE base, 100 ml Legionella enrichment
    and 900 ml water. The target instead contains the J804 dilute R2A product and
    added agar. Current owners separately preserve R2A dilution, corn-meal suppliers,
    M2859 unspecified BCYE, alkali RCA, DSM604 commercial identity, ME, modified GAM,
    oatmeal and marine/pH formulations. Their coincident historical fingerprint does
    not prove equivalence.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - jcm119
  - jcm804
  - jcm845
  - jcm1329
  - jcm150
  - togo-bcye
  - jcm455
  - dsmz604
  - togo-me
  - jcm655
  - jcm1202
  - jcm118
  - jcm1001
  - jcm1016
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
  - owner-11
  - owner-12
  - owner-13
  - owner-14
- assessment_id: grounding
  area: grounding
  topic: Provider mixture identity and exact ontology metadata
  outcome: concern
  summary: The two target primary slots are populated, but one is a provider complex-medium
    identifier rather than CHEBI. Primary CHEBI coverage is 1/2 (50%); all primary
    identifiers have source metadata 2/2 (100%). Both secondary slots resolve in the
    pinned MIM index 2/2 (100%), yet the first agar link falsely treats the whole
    R2A mixture as agar. All asserted CHEBI labels in the target and fifteen owners
    are exact; commercial products correctly left ungrounded are not missing pure-molecule
    identities. These percentages measure linkage, not scientific accuracy.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - r2a-provider
  - chebi2509
  - chebi15377
  - chebi29377
  - mim
  - grounding-inventory
- assessment_id: volume
  area: quantity
  topic: Recipe water, nominal rates and percentage bases
  outcome: concern
  summary: Treat printed g/ml/L as recipe inputs. J119 lists 900 ml water plus 100
    ml enrichment, and J455 lists 900 ml water before 100 ml carbonate solution; neither
    states a measured final volume. Retained nominal per-litre values require that
    convention to be explicit. J455/J1001/J1016 say 10% carbonate without a w/v basis.
    The pH wrappers leave its dose VARIABLE; do not calculate carbonate grams or final
    pH-mixture volume.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - jcm119
  - jcm455
  - jcm1001
  - jcm1016
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Contributor-specific preparation survives in owners
  outcome: concern
  summary: The target omits preparation. Most maintained owners already retain the
    appropriate default 121 C/15 min or TOGO M250 115 C/10 min procedure. Preserve
    post-autoclave carbonate additions and pH 8.5, 9.0 or about 10 only in their own
    formulations. DSM604 supplies no cycle, and M2859 supplies no preparation; do
    not invent either. J119 currently overstates its listed liquids as bringing the
    medium to 1 L.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - default-autoclave
  - jcm455
  - jcm1001
  - jcm1016
  - togo-me
  - dsmz604
  - togo-bcye
  - owner-2
- assessment_id: graph
  area: identity
  topic: Asserted graph accession12
  outcome: concern
  summary: The target and several contributors assert mediadive.medium:12, whose exact
    DSMZ/API identity is SOIL EXTRACT MEDIUM. Its soil extraction and agar recipe
    do not support BCYE, R2A or the other contributor products. This is an independently
    confirmed accession-identity conflict; no local KG ingredient graph was recomputed
    and no replacement graph match is proposed.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - dsmz12GraphIdentity
  - graph-identity
- assessment_id: biology
  area: evidence
  topic: Cultivation statements and classification
  outcome: concern
  summary: COMPLEX/UNDEFINED/SOLID_AGAR is compatible with the commercial agar formulations,
    but does not make them identical. The generic microbial-cultivation application
    does not establish a target strain. TOGO M2859 alone states L. pneumophila Paris/Lens
    at 37 C for 3 d; the original experiment and taxonomy were not independently recovered,
    so those conditions are not generalized to BCYE or the other contributors. Sterilization
    temperatures are not growth temperatures.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - togo-bcye
  - default-autoclave
  - togo-me
- assessment_id: relationships
  area: provenance
  topic: Exact maintained ownership and scoped relationships
  outcome: concern
  summary: Fifteen exact maintained paths are resolved with repeated bacto_marine
    basename multiplicity across categories. J119/M111, J1329/M3004 and J150/M141
    are exact source-duplicate contexts; R2A parent applies only to J804/J845; marine
    pH wrappers delegate only to J118. Additional marine children are linked context,
    not extra base ingredients. Exact local ID resolution does not verify every child
    formulation or DSM604 dose. Excluded bacterial namesakes do not become owners
    or review obligations.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - relationships
  - jcm346
  - jcm118
  - togoM111relationship
  - togoM3004relationship
  - togoM141relationship
  - dsmz604
- assessment_id: evidence
  area: evidence
  topic: Current claims versus parent and historical evidence
  outcome: concern
  summary: No target or maintained contributor has attached evidence objects. Their
    current source/notes/references and repaired values do not equal claim-level excerpts.
    The only separately scoped existing evidence object is the R2A parent-paper claim;
    its source response is unavailable, and it must not transfer to the entire merged
    target. Historical report/plan prose is read as derivative context with exact
    record/ID scope, not authenticated original API evidence.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - history-inventory
  - report-scope
  - jcm346
  - r2a-provider
- assessment_id: writers
  area: provenance
  topic: Already repaired owners and present writer limits
  outcome: concern
  summary: The current BCYE, corn-meal, sparse-product, DSM604, GAM/oatmeal and marine
    repair constructors explain the present repaired owner fields. Preserve that work.
    Narrow remaining corrections include unsupported percentage basis and volume wording;
    then reconcile the false merged identity under current guarded generation. The
    existing full source constructors are not evidence that current code produced
    the older false merge.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - history-inventory
  - writer-4
  - writer-5
  - writer-6
  - writer-7
  - writer-8
  - writer-9
  - writer-10
  - writer-11
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 78 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002367
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"topic\": \"Generated target\
    \ R2A agar\",\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\"\
    : \"1.82\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.82\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"The numbers describe J804, not the declared J119 identity. Reconstruct only\
    \ after identity reconciliation.\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm804\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\",\n        \"source_locator\"\
    : \"Exact primary raw table row 0; cells ['R2A agar (BD-Difco)', '1.82', 'g']\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> R2A agar (BD-Difco)  \
    \                                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.82&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    \n      },\n      {\n        \"source_key\": \"jcm119\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\",\n        \"source_locator\"\
    : \"Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> BCYE agar (BD-Difco) \
    \                                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this historical stored value\
    \ for audit, but do not keep the J804 formulation under J119 BCYE. Do not add\
    \ BCYE ingredients to this R2A recipe as one combined medium.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q2\",\n    \"topic\": \"Generated target Agar\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"15\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[1].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ numbers describe J804, not the declared J119 identity. Reconstruct only after\
    \ identity reconciliation.\"\n      }\n    ],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm804\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Agar',\
    \ '15.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Agar \
    \                                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;15.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    \n      },\n      {\n        \"source_key\": \"jcm119\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\",\n        \"source_locator\"\
    : \"Exact primary raw table row 0; cells ['BCYE agar (BD-Difco)', '37.0', 'g']\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> BCYE agar (BD-Difco) \
    \                                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this historical stored value\
    \ for audit, but do not keep the J804 formulation under J119 BCYE. Do not add\
    \ BCYE ingredients to this R2A recipe as one combined medium.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q3\",\n    \"topic\": \"J119 source component 1 missing\
    \ from generated identity\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm119\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['BCYE agar\
    \ (BD-Difco)', '37.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ BCYE agar (BD-Difco)                                      </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"After separating unrelated contributors,\
    \ regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment\
    \ and 900 ml recipe water. The maintained J119 owner already contains these components;\
    \ no duplicate owner repair is requested.\"\n  },\n  {\n    \"quantity_id\": \"\
    q4\",\n    \"topic\": \"J119 source component 2 missing from generated identity\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"layer_decisions\":\
    \ [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm119\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Legionella\
    \ agar enrichment (BD-Difco)', '100.0', 'ml']\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Legionella agar enrichment (BD-Difco)                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"After separating unrelated contributors,\
    \ regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment\
    \ and 900 ml recipe water. The maintained J119 owner already contains these components;\
    \ no duplicate owner repair is requested.\"\n  },\n  {\n    \"quantity_id\": \"\
    q5\",\n    \"topic\": \"J119 source component 3 missing from generated identity\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"layer_decisions\":\
    \ [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm119\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 2; cells ['Distilled\
    \ water', '900.0', 'ml']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"After separating unrelated contributors,\
    \ regenerate the J119 formulation with its exact 37 g BCYE product, 100 ml enrichment\
    \ and 900 ml recipe water. The maintained J119 owner already contains these components;\
    \ no duplicate owner repair is requested.\"\n  },\n  {\n    \"quantity_id\": \"\
    q6\",\n    \"topic\": \"JCM Medium J804 — R2A agar (BD-Difco)\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": {\n      \"value\": \"1.82\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.82\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 804 lists 1.82 g/L R2A agar (BD-Difco).\",\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm804\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['R2A agar\
    \ (BD-Difco)', '1.82', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ R2A agar (BD-Difco)                                        </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;1.82&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q7\",\n    \"topic\": \"JCM Medium J804 — Agar\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"\
    15\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 804 adds 15 g/L agar.\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm804\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Agar',\
    \ '15.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Agar \
    \                                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;15.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q8\",\n    \"topic\": \"JCM Medium J804 — Distilled\
    \ water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\"\
    : \"1.0\",\n      \"unit\": \"L\"\n    },\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\",\n \
    \       \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"JCM\
    \ Medium 804 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm804\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 2; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q9\",\n    \"topic\": \"JCM Medium J845 — R2A\
    \ agar (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"9.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 845 lists 9.1 g/L R2A agar (BD-Difco).\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm845\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['R2A agar\
    \ (BD-Difco)', '9.1', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ R2A agar (BD-Difco)                                        </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;9.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q10\",\n    \"topic\": \"JCM Medium J845 —\
    \ Agar\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\"\
    : \"7.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 845 adds 7.5 g/L agar.\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm845\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Agar',\
    \ '7.5', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Agar  \
    \                                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;7.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"topic\": \"JCM Medium J845 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"JCM\
    \ Medium 845 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm845\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 2; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q12\",\n    \"topic\": \"JCM Medium J119 —\
    \ BCYE agar (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"37\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 119 lists this commercial BD-Difco medium base as supplied.\",\n    \
    \    \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal amount\
    \ belongs to this contributor only. A per-litre field is a nominal recipe convention\
    \ relative to listed water or liquids, not proof of measured final volume. No\
    \ attached quantity evidence exists; add an exact scoped excerpt without changing\
    \ a supported amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm119\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['BCYE agar\
    \ (BD-Difco)', '37.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ BCYE agar (BD-Difco)                                      </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;37.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q13\",\n    \"topic\": \"JCM Medium J119 —\
    \ Legionella agar enrichment (BD-Difco)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"100\",\n      \"unit\": \"ML_PER_L\"\n\
    \    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 119 lists this commercial BD-Difco enrichment as supplied.\",\n     \
    \   \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal amount\
    \ belongs to this contributor only. A per-litre field is a nominal recipe convention\
    \ relative to listed water or liquids, not proof of measured final volume. No\
    \ attached quantity evidence exists; add an exact scoped excerpt without changing\
    \ a supported amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm119\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Legionella\
    \ agar enrichment (BD-Difco)', '100.0', 'ml']\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Legionella agar enrichment (BD-Difco)                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q14\",\n    \"topic\": \"JCM Medium J119 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"900\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"ML_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount. Correct the existing note claiming a final 1 L\
    \ makeup: the primary lists 900 ml water and 100 ml enrichment, not a measured\
    \ final volume.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"JCM\
    \ Medium 119 brings the base plus enrichment to 1 L.\",\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. Correct\
    \ the existing note claiming a final 1 L makeup: the primary lists 900 ml water\
    \ and 100 ml enrichment, not a measured final volume.\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm119\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 2; cells ['Distilled\
    \ water', '900.0', 'ml']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. Correct\
    \ the existing note claiming a final 1 L makeup: the primary lists 900 ml water\
    \ and 100 ml enrichment, not a measured final volume.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q15\",\n    \"topic\": \"JCM Medium J1329 — Corn meal agar (Nissui)\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"17.0\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"17.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 1329 lists 17.0 g/L Corn meal agar (Nissui); this is a commercial dehydrated\
    \ medium and is intentionally left ungrounded.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1329\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Corn meal\
    \ agar (Nissui)', '17.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Corn meal agar (Nissui)                </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;17.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q16\",\n    \"topic\": \"JCM Medium J1329 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 1329 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1329\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\":\
    \ \"ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723\"\n     \
    \ }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q17\",\n    \"topic\": \"JCM Medium J150 —\
    \ Corn meal agar (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"17.0\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"17.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 150 lists 17.0 g/L Corn meal agar (BD-Difco); this is a commercial dehydrated\
    \ medium and is intentionally left ungrounded.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm150\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Corn meal\
    \ agar (BD-Difco)', '17.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Corn meal agar (BD-Difco)                                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;17.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q18\",\n    \"topic\": \"JCM Medium J150 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 150 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm150\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"topic\": \"TOGO Medium M2859\
    \ — BCYE agar\",\n    \"decision\": \"not_quantified\",\n    \"local\": {\n  \
    \    \"value\": \"1000\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"The\
    \ source lists 1 L of unspecified BCYE. 1000 ml is an exact unit conversion, but\
    \ ML_PER_L adds a denominator not independently supplied for this opaque medium.\
    \ Preserve the volume-only amount and unresolved product/formulation; no dry mass\
    \ or J119 equivalence is inferred.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[0].notes\",\n        \"stored\": \"TOGO M2859 lists one liter\
    \ of BCYE agar without spelling out the commercial product or formulation.\",\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"The source\
    \ lists 1 L of unspecified BCYE. 1000 ml is an exact unit conversion, but ML_PER_L\
    \ adds a denominator not independently supplied for this opaque medium. Preserve\
    \ the volume-only amount and unresolved product/formulation; no dry mass or J119\
    \ equivalence is inferred.\"\n      }\n    ],\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"togoM2859original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859\",\n\
    \        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"BCYE agar\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"ede4a337bb29494b8e3ba5121c94fcfd933e1b19d98916349209f5a56ff133b4\"\
    \n      }\n    ],\n    \"rationale\": \"The source lists 1 L of unspecified BCYE.\
    \ 1000 ml is an exact unit conversion, but ML_PER_L adds a denominator not independently\
    \ supplied for this opaque medium. Preserve the volume-only amount and unresolved\
    \ product/formulation; no dry mass or J119 equivalence is inferred.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q20\",\n    \"topic\": \"JCM Medium J455 — Reinforced\
    \ clostridial agar (Sigma)\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"51.0\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"51.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"MediaDive\
    \ J455 / JCM Medium 455 lists 51.0 g/L Reinforced clostridial agar (Sigma); this\
    \ dehydrated commercial mixture is retained as an opaque complex component.\"\
    ,\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm455\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Reinforced\
    \ clostridial agar (Sigma)', '51.0', 'g']\",\n        \"exact_source_quote\":\
    \ \"<TR><TD WIDTH=75%> Reinforced clostridial agar (Sigma)                   \
    \ </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;51.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q21\",\n    \"topic\": \"JCM Medium J455 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"900.0\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ literal amount belongs to this contributor only. A per-litre field is a nominal\
    \ recipe convention relative to listed water or liquids, not proof of measured\
    \ final volume. No attached quantity evidence exists; add an exact scoped excerpt\
    \ without changing a supported amount.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\",\n\
    \        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"MediaDive\
    \ J455 / JCM Medium 455 lists 900.0 ml/L Distilled water.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm455\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '900.0', 'ml']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q22\",\n    \"topic\": \"JCM Medium J455 carbonate\
    \ stock dose\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n    \
    \  \"value\": \"100.0\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100.0\",\n          \"unit\": \"ML_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"Keep\
    \ the explicit 100 ml dose separate from 900 ml basal water; no measured final\
    \ volume is declared.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm455\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\"\
    ,\n        \"source_locator\": \"Post-autoclave stock addition\",\n        \"\
    exact_source_quote\": \"After autoclaving, aseptically add 100 ml of a 10% Na\
    \ 2 CO 3 solution to the medium.\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      }\n    ],\n    \"rationale\": \"Keep the explicit 100 ml dose separate\
    \ from 900 ml basal water; no measured final volume is declared.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q23\",\n    \"topic\": \"JCM Medium J455 carbonate stock\
    \ percentage\",\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\"\
    : \"10.0\",\n      \"unit\": \"PERCENT_W_V\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"10%\
    \ is printed without a mass/volume basis; current PERCENT_W_V is unsupported.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm455\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\"\
    ,\n        \"source_locator\": \"Post-autoclave stock addition\",\n        \"\
    exact_source_quote\": \"After autoclaving, aseptically add 100 ml of a 10% Na\
    \ 2 CO 3 solution to the medium.\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve 10% as an explicitly unspecified\
    \ basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium\
    \ concentration. Retain source sodium carbonate without inventing hydrate specificity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"topic\": \"JCM Medium J455 stock\
    \ sterilization\",\n    \"decision\": \"evidence_only\",\n    \"local\": \"Sterilize\
    \ the 10% Na2CO3 solution before aseptic addition.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Sterilize the 10% Na2CO3 solution before aseptic addition.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Sterilized stock is explicit;\
    \ its separate cycle is not supplied.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm455\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\",\n        \"source_locator\"\
    : \"Post-autoclave stock addition\",\n        \"exact_source_quote\": \"After\
    \ autoclaving, aseptically add 100 ml of a 10% Na 2 CO 3 solution to the medium.\"\
    ,\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      }\n    ],\n    \"rationale\": \"Keep sterile stock preparation separate\
    \ from the default main-medium autoclave cycle; no stock temperature/time is inferred.\"\
    \n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"topic\": \"KOMODO Medium 604\
    \ — Marine agar 2216 (Difco 0979)\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    VARIABLE accurately preserves the absent source dose. Product identity alone cannot\
    \ transfer 55.1 g from J118, a water amount, or a sterilization cycle.\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 604 names Marine Agar 2216 (Difco 0979) as the only component but does\
    \ not state an amount.\",\n        \"decision\": \"not_quantified\",\n       \
    \ \"rationale\": \"VARIABLE accurately preserves the absent source dose. Product\
    \ identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization\
    \ cycle.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz604\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf\"\
    ,\n        \"source_locator\": \"Complete primary formulation\",\n        \"exact_source_quote\"\
    : \"MARINE AGAR 2216 (Difco 0979).\",\n        \"snapshot_sha256\": \"9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24\"\
    ,\n        \"parsed_text_sha256\": \"f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e\"\
    \n      }\n    ],\n    \"rationale\": \"VARIABLE accurately preserves the absent\
    \ source dose. Product identity alone cannot transfer 55.1 g from J118, a water\
    \ amount, or a sterilization cycle.\"\n  },\n  {\n    \"quantity_id\": \"q26\"\
    ,\n    \"topic\": \"JCM Medium J258 — Distilled water\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": {\n      \"value\": \"1000\",\n      \"unit\"\
    : \"ML_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/me_agar.yaml\",\n        \"field_path\": \"\
    ingredients[0].concentration\",\n        \"stored\": {\n          \"value\": \"\
    1000\",\n          \"unit\": \"ML_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"TOGO M250 explicitly snapshots JCM_M258\
    \ and gives this recipe amount. Retain its provider-specific attribution while\
    \ current JCM258 is unavailable. One litre water is a recipe input; final volume\
    \ is not measured.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/me_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"TOGO\
    \ M250 snapshots JCM_M258 and lists 1.0 L distilled water.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"TOGO M250 explicitly snapshots\
    \ JCM_M258 and gives this recipe amount. Retain its provider-specific attribution\
    \ while current JCM258 is unavailable. One litre water is a recipe input; final\
    \ volume is not measured.\"\n      }\n    ],\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"togoM250original\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a\"\
    \n      }\n    ],\n    \"rationale\": \"TOGO M250 explicitly snapshots JCM_M258\
    \ and gives this recipe amount. Retain its provider-specific attribution while\
    \ current JCM258 is unavailable. One litre water is a recipe input; final volume\
    \ is not measured.\"\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"topic\"\
    : \"JCM Medium J258 — Malt extract agar (Oxoid)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"50\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/me_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"TOGO M250\
    \ explicitly snapshots JCM_M258 and gives this recipe amount. Retain its provider-specific\
    \ attribution while current JCM258 is unavailable. One litre water is a recipe\
    \ input; final volume is not measured.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/me_agar.yaml\",\n        \"field_path\": \"\
    ingredients[1].notes\",\n        \"stored\": \"TOGO M250 snapshots JCM_M258 and\
    \ lists 50 g/L Malt extract agar from Oxoid.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"TOGO M250 explicitly snapshots JCM_M258 and gives\
    \ this recipe amount. Retain its provider-specific attribution while current JCM258\
    \ is unavailable. One litre water is a recipe input; final volume is not measured.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM250original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Malt extract agar (Oxoid)\\\",\\n          \\\"\
    volume\\\": 50,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a\"\n     \
    \ }\n    ],\n    \"rationale\": \"TOGO M250 explicitly snapshots JCM_M258 and\
    \ gives this recipe amount. Retain its provider-specific attribution while current\
    \ JCM258 is unavailable. One litre water is a recipe input; final volume is not\
    \ measured.\"\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"topic\": \"JCM\
    \ Medium J655 — GAM agar, modified (Nissui)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"56.7\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"56.7\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 655 lists 56.7 g GAM agar, modified (Nissui).\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm655\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['GAM agar,\
    \ modified (Nissui)', '56.7', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> GAM agar, modified (Nissui) </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;56.7&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q29\",\n    \"topic\": \"JCM Medium J655 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1000\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ literal amount belongs to this contributor only. A per-litre field is a nominal\
    \ recipe convention relative to listed water or liquids, not proof of measured\
    \ final volume. No attached quantity evidence exists; add an exact scoped excerpt\
    \ without changing a supported amount.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[1].notes\",\n        \"stored\": \"JCM Medium 655 lists 1000 ml\
    \ distilled water.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The literal amount belongs to this contributor only. A per-litre field is\
    \ a nominal recipe convention relative to listed water or liquids, not proof of\
    \ measured final volume. No attached quantity evidence exists; add an exact scoped\
    \ excerpt without changing a supported amount.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm655\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655\",\n        \"source_locator\"\
    : \"Exact primary raw table row 1; cells ['Distilled water', '1.0', 'L']\",\n\
    \        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\":\
    \ \"78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53\"\n     \
    \ }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q30\",\n    \"topic\": \"JCM Medium J1202 —\
    \ Oatmeal agar (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"15.0\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 1202 lists 15.0 g oatmeal agar (BD-Difco).\",\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm1202\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Oatmeal\
    \ agar (BD-Difco)', '15.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Oatmeal agar (BD-Difco)      </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;15.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q31\",\n    \"topic\": \"JCM Medium J1202 —\
    \ Agar\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\"\
    : \"12.0\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 1202 lists 12.0 g agar.\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1202\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Agar',\
    \ '12.0', 'g']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Agar \
    \                        </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;12.0\
    \ &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\"\
    ,\n        \"snapshot_sha256\": \"11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q32\",\n    \"topic\": \"JCM Medium J1202 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1000\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"ML_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ literal amount belongs to this contributor only. A per-litre field is a nominal\
    \ recipe convention relative to listed water or liquids, not proof of measured\
    \ final volume. No attached quantity evidence exists; add an exact scoped excerpt\
    \ without changing a supported amount.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[2].notes\",\n        \"stored\": \"JCM Medium 1202 lists 1000\
    \ ml distilled water.\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The literal amount belongs to this contributor only. A per-litre\
    \ field is a nominal recipe convention relative to listed water or liquids, not\
    \ proof of measured final volume. No attached quantity evidence exists; add an\
    \ exact scoped excerpt without changing a supported amount.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1202\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 2; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0\
    \ &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT> L      \
    \  </TD></TR>\",\n        \"snapshot_sha256\": \"11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q33\",\n    \"topic\": \"DSMZ Medium 604 —\
    \ Marine agar 2216 (Difco 0979)\",\n    \"decision\": \"not_quantified\",\n  \
    \  \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\n\
    \    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    VARIABLE accurately preserves the absent source dose. Product identity alone cannot\
    \ transfer 55.1 g from J118, a water amount, or a sterilization cycle.\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"DSMZ\
    \ Medium 604 names Marine Agar 2216 (Difco 0979) as the only component but does\
    \ not state an amount.\",\n        \"decision\": \"not_quantified\",\n       \
    \ \"rationale\": \"VARIABLE accurately preserves the absent source dose. Product\
    \ identity alone cannot transfer 55.1 g from J118, a water amount, or a sterilization\
    \ cycle.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz604\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf\"\
    ,\n        \"source_locator\": \"Complete primary formulation\",\n        \"exact_source_quote\"\
    : \"MARINE AGAR 2216 (Difco 0979).\",\n        \"snapshot_sha256\": \"9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24\"\
    ,\n        \"parsed_text_sha256\": \"f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e\"\
    \n      }\n    ],\n    \"rationale\": \"VARIABLE accurately preserves the absent\
    \ source dose. Product identity alone cannot transfer 55.1 g from J118, a water\
    \ amount, or a sterilization cycle.\"\n  },\n  {\n    \"quantity_id\": \"q34\"\
    ,\n    \"topic\": \"JCM Medium J118 — Marine agar 2216 (BD-Difco)\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": {\n      \"value\": \"55.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/marine_agar_2216.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"55.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The literal amount belongs to this\
    \ contributor only. A per-litre field is a nominal recipe convention relative\
    \ to listed water or liquids, not proof of measured final volume. No attached\
    \ quantity evidence exists; add an exact scoped excerpt without changing a supported\
    \ amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 prints this commercial component.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm118\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Marine\
    \ agar 2216 (BD-Difco)', '55.1', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Marine agar 2216 (BD-Difco)                               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;55.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q35\",\n    \"topic\": \"JCM Medium J118 —\
    \ Distilled water\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm118\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q36\",\n    \"topic\": \"JCM Medium J1001 —\
    \ Marine agar 2216 (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": {\n      \"value\": \"55.1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"55.1\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount. The pH wrapper explicitly delegates its base to\
    \ J118; carbonate is a separate unspecified-dose addition.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 lists 55.1 g/L Marine agar 2216 with the BD-Difco attribute; left\
    \ ungrounded as an undefined commercial agar.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount. The pH wrapper\
    \ explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Marine\
    \ agar 2216 (BD-Difco)', '55.1', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Marine agar 2216 (BD-Difco)                               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;55.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      },\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Exact primary delegation to J118\",\n        \"exact_source_quote\": \"Prepare\
    \ Marine agar 2216 (see Medium No. 118 ).\",\n        \"snapshot_sha256\": \"\
    b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\",\n        \"\
    parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. The\
    \ pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"topic\": \"JCM\
    \ Medium J1001 — Distilled water\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount. The pH wrapper explicitly delegates its base to\
    \ J118; carbonate is a separate unspecified-dose addition.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount. The pH wrapper\
    \ explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      },\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Exact primary delegation to J118\",\n        \"exact_source_quote\": \"Prepare\
    \ Marine agar 2216 (see Medium No. 118 ).\",\n        \"snapshot_sha256\": \"\
    b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\",\n        \"\
    parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. The\
    \ pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"topic\": \"JCM\
    \ Medium J1001 carbonate stock dose\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume.\
    \ Do not infer carbonate mass or dilution.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Post-autoclave stock addition\",\n        \"exact_source_quote\": \"After\
    \ autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.\",\n \
    \       \"snapshot_sha256\": \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\"\
    ,\n        \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"Retain VARIABLE dose: the primary states\
    \ a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution.\"\
    \n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"topic\": \"JCM Medium J1001\
    \ carbonate stock percentage\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"10.0\",\n      \"unit\": \"PERCENT_W_V\"\n    },\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"10%\
    \ is printed without a mass/volume basis; current PERCENT_W_V is unsupported.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1001\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\"\
    ,\n        \"source_locator\": \"Post-autoclave stock addition\",\n        \"\
    exact_source_quote\": \"After autoclaving, adjust pH to 8.5 with sterilized 10%\
    \ Na 2 CO 3 solution.\",\n        \"snapshot_sha256\": \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\"\
    ,\n        \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve 10% as an explicitly unspecified\
    \ basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium\
    \ concentration. Retain source sodium carbonate without inventing hydrate specificity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"topic\": \"JCM Medium J1001\
    \ stock sterilization\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : \"Sterilize the 10% Na2CO3 solution before addition.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Sterilize the 10% Na2CO3 solution before addition.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"Sterilized stock is explicit; its\
    \ separate cycle is not supplied.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Post-autoclave stock addition\",\n        \"exact_source_quote\": \"After\
    \ autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.\",\n \
    \       \"snapshot_sha256\": \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\"\
    ,\n        \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"Keep sterile stock preparation separate\
    \ from the default main-medium autoclave cycle; no stock temperature/time is inferred.\"\
    \n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"topic\": \"JCM Medium J1016\
    \ — Marine agar 2216 (BD-Difco)\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local\": {\n      \"value\": \"55.1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"55.1\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount. The pH wrapper explicitly delegates its base to\
    \ J118; carbonate is a separate unspecified-dose addition.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 lists 55.1 g/L Marine agar 2216 with the BD-Difco attribute; left\
    \ ungrounded as an undefined commercial agar.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount. The pH wrapper\
    \ explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 0; cells ['Marine\
    \ agar 2216 (BD-Difco)', '55.1', 'g']\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Marine agar 2216 (BD-Difco)                               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;55.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      },\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Exact primary delegation to J118\",\n        \"exact_source_quote\": \"Prepare\
    \ Marine agar 2216 (see Medium No. 118 ).\",\n        \"snapshot_sha256\": \"\
    026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\",\n        \"\
    parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. The\
    \ pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"topic\": \"JCM\
    \ Medium J1016 — Distilled water\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"1.0\",\n      \"unit\": \"L\"\n    },\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"evidence_only\",\n        \"rationale\": \"The literal\
    \ amount belongs to this contributor only. A per-litre field is a nominal recipe\
    \ convention relative to listed water or liquids, not proof of measured final\
    \ volume. No attached quantity evidence exists; add an exact scoped excerpt without\
    \ changing a supported amount. The pH wrapper explicitly delegates its base to\
    \ J118; carbonate is a separate unspecified-dose addition.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"JCM\
    \ Medium 118 lists 1.0 L distilled water.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The literal amount belongs to this contributor only.\
    \ A per-litre field is a nominal recipe convention relative to listed water or\
    \ liquids, not proof of measured final volume. No attached quantity evidence exists;\
    \ add an exact scoped excerpt without changing a supported amount. The pH wrapper\
    \ explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Exact primary raw table row 1; cells ['Distilled\
    \ water', '1.0', 'L']\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    \n      },\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Exact primary delegation to J118\",\n        \"exact_source_quote\": \"Prepare\
    \ Marine agar 2216 (see Medium No. 118 ).\",\n        \"snapshot_sha256\": \"\
    026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\",\n        \"\
    parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"The literal amount belongs to this contributor\
    \ only. A per-litre field is a nominal recipe convention relative to listed water\
    \ or liquids, not proof of measured final volume. No attached quantity evidence\
    \ exists; add an exact scoped excerpt without changing a supported amount. The\
    \ pH wrapper explicitly delegates its base to J118; carbonate is a separate unspecified-dose\
    \ addition.\"\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"topic\": \"JCM\
    \ Medium J1016 carbonate stock dose\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    Retain VARIABLE dose: the primary states a pH adjustment but gives no added volume.\
    \ Do not infer carbonate mass or dilution.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Post-autoclave stock addition\",\n        \"exact_source_quote\": \"After\
    \ autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.\",\n \
    \       \"snapshot_sha256\": \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\"\
    ,\n        \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain VARIABLE dose: the primary states\
    \ a pH adjustment but gives no added volume. Do not infer carbonate mass or dilution.\"\
    \n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"topic\": \"JCM Medium J1016\
    \ carbonate stock percentage\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"10.0\",\n      \"unit\": \"PERCENT_W_V\"\n    },\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"10.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"10%\
    \ is printed without a mass/volume basis; current PERCENT_W_V is unsupported.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1016\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\"\
    ,\n        \"source_locator\": \"Post-autoclave stock addition\",\n        \"\
    exact_source_quote\": \"After autoclaving, adjust pH to 9.0 with sterilized 10%\
    \ Na 2 CO 3 solution.\",\n        \"snapshot_sha256\": \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\"\
    ,\n        \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve 10% as an explicitly unspecified\
    \ basis; do not calculate 100 g/L, 10 g delivered, molarity, or a final-medium\
    \ concentration. Retain source sodium carbonate without inventing hydrate specificity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"topic\": \"JCM Medium J1016\
    \ stock sterilization\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : \"Sterilize the 10% Na2CO3 solution before addition.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Sterilize the 10% Na2CO3 solution before addition.\",\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"Sterilized stock is explicit; its\
    \ separate cycle is not supplied.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Post-autoclave stock addition\",\n        \"exact_source_quote\": \"After\
    \ autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.\",\n \
    \       \"snapshot_sha256\": \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\"\
    ,\n        \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"Keep sterile stock preparation separate\
    \ from the default main-medium autoclave cycle; no stock temperature/time is inferred.\"\
    \n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"topic\": \"JCM Medium J804 preparation\
    \ and conditions\",\n    \"decision\": \"evidence_only\",\n    \"local\": \"JCM\
    \ Medium 804 lists 1.82 g/L R2A agar (BD-Difco), 15 g/L agar, and 1.0 L distilled\
    \ water.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 804 lists\
    \ 1.82 g/L R2A agar (BD-Difco), 15 g/L agar, and 1.0 L distilled water.\",\n \
    \       \"decision\": \"evidence_only\",\n        \"rationale\": \"Retain the\
    \ existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\",\n \
    \       \"field_path\": \"preparation_steps\",\n        \"stored\": [\n      \
    \    {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n  \
    \          \"description\": \"Dissolve 1.82 g R2A agar (BD-Difco) and 15 g agar\
    \ in 1.0 L distilled water.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Autoclave at 121 C for 15 min.\"\n          }\n        ],\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_10_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"variant_modifications\",\n        \"stored\": [\n\
    \          \"Uses 1.82 g/L R2A agar (BD-Difco) with 15 g/L added agar.\"\n   \
    \     ],\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    Retain the existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm804\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=804\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"3c0828e0f7f390ea13539e20340d86c497c6554da0cea0ea6927eb0dfa3cfa09\"\
    ,\n        \"parsed_text_sha256\": \"dff149bc5d15c946bb19a85a30d32a6950618fcfc5279bf5007993f2af839c05\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"topic\"\
    : \"JCM Medium J845 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 845 lists 9.1 g/L R2A agar (BD-Difco), 7.5 g/L\
    \ agar, and 1.0 L distilled water.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\",\n   \
    \     \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 845 lists 9.1\
    \ g/L R2A agar (BD-Difco), 7.5 g/L agar, and 1.0 L distilled water.\",\n     \
    \   \"decision\": \"evidence_only\",\n        \"rationale\": \"Retain the existing\
    \ contributor-specific procedure and default 121 C/15 min sterilization; preserve\
    \ its source-specific formulation and any late carbonate/pH step. No incubation\
    \ condition or measured final volume follows.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": [\n          {\n            \"step_number\"\
    : 1,\n            \"action\": \"MIX\",\n            \"description\": \"Dissolve\
    \ 9.1 g R2A agar (BD-Difco) and 7.5 g agar in 1.0 L distilled water.\"\n     \
    \     },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"AUTOCLAVE\",\n            \"description\": \"Autoclave at 121 C for 15 min.\"\
    \n          }\n        ],\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"Retain the existing contributor-specific procedure and default\
    \ 121 C/15 min sterilization; preserve its source-specific formulation and any\
    \ late carbonate/pH step. No incubation condition or measured final volume follows.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/1_2_r2a_agar.yaml\"\
    ,\n        \"field_path\": \"variant_modifications\",\n        \"stored\": [\n\
    \          \"Uses 9.1 g/L R2A agar (BD-Difco) with 7.5 g/L added agar.\"\n   \
    \     ],\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    Retain the existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm845\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=845\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"5e2c53029b662cc76b3b17ae2d910557a8c682f41271d0605ad5d65d0dcfa7f7\"\
    ,\n        \"parsed_text_sha256\": \"cfef3065aec7802fb0fd6c802d44cd89c6bc1beecfb8b081e00f8c993ca5804a\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q48\",\n    \"topic\"\
    : \"JCM Medium J119 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"Source: JCM Medium 119 | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\\\
    n\\nThe JCM BCYE Agar table lists BCYE agar, Legionella agar enrichment, and distilled\
    \ water as supplied BD-Difco products.\",\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: JCM Medium\
    \ 119 | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\\n\\nThe\
    \ JCM BCYE Agar table lists BCYE agar, Legionella agar enrichment, and distilled\
    \ water as supplied BD-Difco products.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows. The water-note claim of final 1 L makeup is separately marked for correction.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave at 121 C for 15 min.\"\n         \
    \ }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows. The water-note\
    \ claim of final 1 L makeup is separately marked for correction.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm119\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    ,\n        \"parsed_text_sha256\": \"8e902ea14398f3deff72743b4efb5e8d370875df49359881483cfbef8e159bb9\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows. The water-note claim of final 1 L makeup is separately\
    \ marked for correction.\"\n  },\n  {\n    \"quantity_id\": \"q49\",\n    \"topic\"\
    : \"JCM Medium J1329 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 1329 defines CORN MEAL AGAR as 17.0 g/L Corn meal\
    \ agar (Nissui) in 1.0 L distilled water, with default JCM autoclaving at 121\
    \ C for 15 minutes.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\",\n        \"\
    field_path\": \"notes\",\n        \"stored\": \"JCM Medium 1329 defines CORN MEAL\
    \ AGAR as 17.0 g/L Corn meal agar (Nissui) in 1.0 L distilled water, with default\
    \ JCM autoclaving at 121 C for 15 minutes.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave at 121 C for 15 minutes.\"\n     \
    \     }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm1329\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"ac38682e00db60a4c5d486a3965d920e674de80872e65fc3e66b9741d19ee723\"\
    ,\n        \"parsed_text_sha256\": \"d873785344db095d73c2b7704f723a249e10e405693e8702d9621785ef08fa68\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"topic\"\
    : \"JCM Medium J150 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 150 defines CORN MEAL AGAR as 17.0 g/L Corn meal\
    \ agar (BD-Difco) in 1.0 L distilled water, with default JCM autoclaving at 121\
    \ C for 15 minutes.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\",\n        \"\
    field_path\": \"notes\",\n        \"stored\": \"JCM Medium 150 defines CORN MEAL\
    \ AGAR as 17.0 g/L Corn meal agar (BD-Difco) in 1.0 L distilled water, with default\
    \ JCM autoclaving at 121 C for 15 minutes.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave at 121 C for 15 minutes.\"\n     \
    \     }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm150\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"1e65389196978c201229c7abe3d410b5577c10d8f3a4c31f2ac3735622ff7478\"\
    ,\n        \"parsed_text_sha256\": \"166ae9f69dd4786d18d7dd2f638dda1799b2a3965e3c3c1c748d28803498d374\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q51\",\n    \"topic\"\
    : \"TOGO Medium M2859 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"TOGO M2859 records L. pneumophila strains Paris and Lens grown\
    \ on one liter of BCYE agar at 37 C for 3 d; the source does not disclose the\
    \ BCYE agar formulation.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml\",\n        \"field_path\"\
    : \"notes\",\n        \"stored\": \"TOGO M2859 records L. pneumophila strains\
    \ Paris and Lens grown on one liter of BCYE agar at 37 C for 3 d; the source does\
    \ not disclose the BCYE agar formulation.\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"The provider alone states Paris/Lens 37 C and 3 d.\
    \ Preserve the narrow attribution, and do not treat this as original-paper verification\
    \ or a general BCYE growth condition.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml\",\n        \"field_path\"\
    : \"temperature_value\",\n        \"stored\": 37.0,\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"The provider alone states Paris/Lens\
    \ 37 C and 3 d. Preserve the narrow attribution, and do not treat this as original-paper\
    \ verification or a general BCYE growth condition.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"togoM2859original\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2859\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"L. pneumophila strains Paris and Lens were grown on BCYE agar at 37 °C for\
    \ 3 d and chromosomal DNA was isolated by standard protocols.\",\n        \"snapshot_sha256\"\
    : \"ede4a337bb29494b8e3ba5121c94fcfd933e1b19d98916349209f5a56ff133b4\"\n     \
    \ }\n    ],\n    \"rationale\": \"The provider alone states Paris/Lens 37 C and\
    \ 3 d. Preserve the narrow attribution, and do not treat this as original-paper\
    \ verification or a general BCYE growth condition.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q52\",\n    \"topic\": \"JCM Medium J455 preparation and conditions\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local\": \"JCM Medium 455 Alkali-Reinforced\
    \ Clostridial Agar lists 51 g Reinforced clostridial agar (Sigma) in 900 ml distilled\
    \ water per liter. After autoclaving at 121 C for 15 min, 100 ml of sterile 10%\
    \ Na2CO3 solution is added aseptically and the final pH is checked to be about\
    \ 10.0.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 455 Alkali-Reinforced\
    \ Clostridial Agar lists 51 g Reinforced clostridial agar (Sigma) in 900 ml distilled\
    \ water per liter. After autoclaving at 121 C for 15 min, 100 ml of sterile 10%\
    \ Na2CO3 solution is added aseptically and the final pH is checked to be about\
    \ 10.0.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    Retain the existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave the reinforced clostridial agar base\
    \ at 121 C for 15 min.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"MIX\",\n            \"description\": \"Aseptically\
    \ add 100 ml/L sterile 10% Na2CO3 solution after autoclaving.\"\n          },\n\
    \          {\n            \"step_number\": 3,\n            \"action\": \"ADJUST_PH\"\
    ,\n            \"description\": \"Check final pH to be about 10.0.\"\n       \
    \   }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"temperature\": {\n            \"value\"\
    : 121.0,\n            \"unit\": \"CELSIUS\"\n          },\n          \"duration\"\
    : \"15 min\",\n          \"notes\": \"Sterilize the 10% Na2CO3 solution separately\
    \ before aseptic addition.\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 10.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      }\n    ],\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm455\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      },\n      {\n        \"source_key\": \"jcm455\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\",\n        \"source_locator\"\
    : \"Complete short primary including separate carbonate/pH instruction\",\n  \
    \      \"exact_source_quote\": \"Medium data Medium data Search for medium no.\
    \ = [455]. Unless otherwise stated, sterilize media by autoclaving at 121°C for\
    \ 15 min. 455   ALKALI-REINFORCED CLOSTRIDIAL AGAR Reinforced clostridial agar\
    \ (Sigma) 51.0 g Distilled water 900.0 ml After autoclaving, aseptically add 100\
    \ ml of a 10% Na 2 CO 3 solution to the medium. Check final pH to be about 10.0.\
    \ Copyright © 2026 Microbe Division (JCM) - All Rights Reserved\",\n        \"\
    snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q53\",\n    \"topic\"\
    : \"KOMODO Medium 604 preparation and conditions\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local\": \"DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216\
    \ (Difco 0979).\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacto_marine_agar.yaml\",\n        \"field_path\"\
    : \"notes\",\n        \"stored\": \"DSMZ Medium 604 records BACTO MARINE AGAR\
    \ as Marine Agar 2216 (Difco 0979).\",\n        \"decision\": \"not_quantified\"\
    ,\n        \"rationale\": \"The source supplies product identity only. Existing\
    \ generic MIX instruction does not establish dose, water or sterilization; those\
    \ details remain unresolved.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Prepare the Marine Agar 2216 (Difco 0979) product.\"\
    \n          }\n        ],\n        \"decision\": \"not_quantified\",\n       \
    \ \"rationale\": \"The source supplies product identity only. Existing generic\
    \ MIX instruction does not establish dose, water or sterilization; those details\
    \ remain unresolved.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz604\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf\"\
    ,\n        \"source_locator\": \"Complete primary\",\n        \"exact_source_quote\"\
    : \"MARINE AGAR 2216 (Difco 0979).\",\n        \"snapshot_sha256\": \"9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24\"\
    ,\n        \"parsed_text_sha256\": \"f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e\"\
    \n      }\n    ],\n    \"rationale\": \"The source supplies product identity only.\
    \ Existing generic MIX instruction does not establish dose, water or sterilization;\
    \ those details remain unresolved.\"\n  },\n  {\n    \"quantity_id\": \"q54\"\
    ,\n    \"topic\": \"JCM Medium J258 preparation and conditions\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": \"TOGO M250 is a snapshot of JCM_M258 and\
    \ records 50 g/L Malt extract agar from Oxoid in distilled water with autoclaving\
    \ at 115 C for 10 min.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/me_agar.yaml\",\n        \"field_path\": \"\
    notes\",\n        \"stored\": \"TOGO M250 is a snapshot of JCM_M258 and records\
    \ 50 g/L Malt extract agar from Oxoid in distilled water with autoclaving at 115\
    \ C for 10 min.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the provider-specific 115 C/10 min procedure already present; it is\
    \ sterilization, not growth. Current primary correspondence remains unavailable.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/me_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave at 115 C for 10 min.\"\n         \
    \ }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the provider-specific 115 C/10 min procedure already present; it is\
    \ sterilization, not growth. Current primary correspondence remains unavailable.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM250original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M250\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Autoclave at 115C for 10 min.\",\n        \"snapshot_sha256\": \"0e07b578c3a890503f2de586023f4a8f835ad26b0331e7f12bac677fcbf58f3a\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the provider-specific 115 C/10\
    \ min procedure already present; it is sterilization, not growth. Current primary\
    \ correspondence remains unavailable.\"\n  },\n  {\n    \"quantity_id\": \"q55\"\
    ,\n    \"topic\": \"JCM Medium J655 preparation and conditions\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": \"JCM Medium 655 contains 56.7 g GAM agar,\
    \ modified (Nissui), and 1.0 L distilled water.\",\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 655 contains\
    \ 56.7 g GAM agar, modified (Nissui), and 1.0 L distilled water.\",\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Suspend 56.7 g GAM agar, modified (Nissui), in\
    \ 1.0 L distilled water.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Autoclave at 121 C for 15 min unless otherwise stated.\"\n          }\n      \
    \  ],\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"Retain\
    \ the existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/modified_gam_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm655\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"78aff0d2ae285f7ad1b30372ee187dc97374b54567af891939b0dcbf4fc73b53\"\
    ,\n        \"parsed_text_sha256\": \"21e3cba1d661434dfeb90bcdf4851663be58e10bfa56a518026c9f1d3c477d2f\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q56\",\n    \"topic\"\
    : \"JCM Medium J1202 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 1202 contains 15.0 g oatmeal agar (BD-Difco), 12.0\
    \ g agar, and 1.0 L distilled water.\",\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 1202 contains\
    \ 15.0 g oatmeal agar (BD-Difco), 12.0 g agar, and 1.0 L distilled water.\",\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"Retain the\
    \ existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Suspend 15.0 g oatmeal agar (BD-Difco) and 12.0\
    \ g agar in 1.0 L distilled water.\"\n          },\n          {\n            \"\
    step_number\": 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\"\
    : \"Autoclave at 121 C for 15 min unless otherwise stated.\"\n          }\n  \
    \      ],\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\
    Retain the existing contributor-specific procedure and default 121 C/15 min sterilization;\
    \ preserve its source-specific formulation and any late carbonate/pH step. No\
    \ incubation condition or measured final volume follows.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm1202\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"11a1ef61fa32f8489832dc5f9ca62c9ee1a24ac19f0ab9229ca198bc3f10bcfc\"\
    ,\n        \"parsed_text_sha256\": \"b5ef6f65af41099fcb4759563ae2cd0402b0efa6e1fb47d824b7d1715e00002a\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q57\",\n    \"topic\"\
    : \"DSMZ Medium 604 preparation and conditions\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local\": \"DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216\
    \ (Difco 0979).\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bacto_marine_agar.yaml\",\n        \"field_path\"\
    : \"notes\",\n        \"stored\": \"DSMZ Medium 604 records BACTO MARINE AGAR\
    \ as Marine Agar 2216 (Difco 0979).\",\n        \"decision\": \"not_quantified\"\
    ,\n        \"rationale\": \"The source supplies product identity only. Existing\
    \ generic MIX instruction does not establish dose, water or sterilization; those\
    \ details remain unresolved.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bacto_marine_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Prepare the Marine Agar 2216 (Difco 0979) product.\"\
    \n          }\n        ],\n        \"decision\": \"not_quantified\",\n       \
    \ \"rationale\": \"The source supplies product identity only. Existing generic\
    \ MIX instruction does not establish dose, water or sterilization; those details\
    \ remain unresolved.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz604\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf\"\
    ,\n        \"source_locator\": \"Complete primary\",\n        \"exact_source_quote\"\
    : \"MARINE AGAR 2216 (Difco 0979).\",\n        \"snapshot_sha256\": \"9ebc39cf6780c73b02ed0bdb09b3d83d89d3d2813c2853b99b7a7974c64d8a24\"\
    ,\n        \"parsed_text_sha256\": \"f26ff3027a67b627923f68e41b464fba8511997812d43c75a0e6108e34af146e\"\
    \n      }\n    ],\n    \"rationale\": \"The source supplies product identity only.\
    \ Existing generic MIX instruction does not establish dose, water or sterilization;\
    \ those details remain unresolved.\"\n  },\n  {\n    \"quantity_id\": \"q58\"\
    ,\n    \"topic\": \"JCM Medium J118 preparation and conditions\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": \"JCM Medium 118 defines Marine Agar 2216\
    \ with 55.1 g Marine agar 2216 (BD-Difco) and 1.0 L distilled water.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 118 defines\
    \ Marine Agar 2216 with 55.1 g Marine agar 2216 (BD-Difco) and 1.0 L distilled\
    \ water.\",\n        \"decision\": \"evidence_only\",\n        \"rationale\":\
    \ \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Prepare Marine Agar 2216.\"\n          },\n  \
    \        {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Autoclave at 121 C for 15 min.\"\n         \
    \ }\n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\"\
    ,\n        \"parsed_text_sha256\": \"d58c7e0426fdb2e9321ac2226356dec0dc90eb4f6fea91000167bea3a69ca966\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q59\",\n    \"topic\"\
    : \"JCM Medium J1001 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 1001 defines Marine Agar 2216 at pH 8.5 as JCM\
    \ Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3\
    \ solution.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 1001 defines\
    \ Marine Agar 2216 at pH 8.5 as JCM Medium 118 Marine Agar 2216 adjusted after\
    \ autoclaving with sterilized 10% Na2CO3 solution.\",\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Prepare Marine agar 2216 from JCM Medium 118.\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"AUTOCLAVE\",\n            \"description\": \"Autoclave the Marine Agar 2216\
    \ base at 121 C for 15 min.\"\n          },\n          {\n            \"step_number\"\
    : 3,\n            \"action\": \"ADJUST_PH\",\n            \"description\": \"\
    After autoclaving, adjust pH to 8.5 with sterilized 10% Na2CO3 solution.\"\n \
    \         }\n        ],\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"Retain the existing contributor-specific procedure and default\
    \ 121 C/15 min sterilization; preserve its source-specific formulation and any\
    \ late carbonate/pH step. No incubation condition or measured final volume follows.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.5,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"variant_modifications\",\n        \"stored\": [\n\
    \          \"Adjusted JCM Medium 118 Marine Agar 2216 to pH 8.5 with 10% Na2CO3.\"\
    \n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1001\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\"\
    ,\n        \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      },\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Complete short primary including separate carbonate/pH instruction\",\n  \
    \      \"exact_source_quote\": \"Medium data Medium data Search for medium no.\
    \ = [1001]. Unless otherwise stated, sterilize media by autoclaving at 121°C for\
    \ 15 min. 1001   MARINE AGAR 2216 (pH 8.5) Prepare Marine agar 2216 (see Medium\
    \ No. 118 ). After autoclaving, adjust pH to 8.5 with sterilized 10% Na 2 CO 3\
    \ solution. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved\",\n\
    \        \"snapshot_sha256\": \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\"\
    ,\n        \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q60\",\n    \"topic\"\
    : \"JCM Medium J1016 preparation and conditions\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"JCM Medium 1016 defines Marine Agar 2216 at pH 9.0 as JCM\
    \ Medium 118 Marine Agar 2216 adjusted after autoclaving with sterilized 10% Na2CO3\
    \ solution.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"JCM Medium 1016 defines\
    \ Marine Agar 2216 at pH 9.0 as JCM Medium 118 Marine Agar 2216 adjusted after\
    \ autoclaving with sterilized 10% Na2CO3 solution.\",\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Prepare Marine agar 2216 from JCM Medium 118.\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"AUTOCLAVE\",\n            \"description\": \"Autoclave the Marine Agar 2216\
    \ base at 121 C for 15 min.\"\n          },\n          {\n            \"step_number\"\
    : 3,\n            \"action\": \"ADJUST_PH\",\n            \"description\": \"\
    After autoclaving, adjust pH to 9.0 with sterilized 10% Na2CO3 solution.\"\n \
    \         }\n        ],\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"Retain the existing contributor-specific procedure and default\
    \ 121 C/15 min sterilization; preserve its source-specific formulation and any\
    \ late carbonate/pH step. No incubation condition or measured final volume follows.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\"\n        },\n        \"decision\": \"evidence_only\"\
    ,\n        \"rationale\": \"Retain the existing contributor-specific procedure\
    \ and default 121 C/15 min sterilization; preserve its source-specific formulation\
    \ and any late carbonate/pH step. No incubation condition or measured final volume\
    \ follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"variant_modifications\",\n        \"stored\": [\n\
    \          \"Adjusted JCM Medium 118 Marine Agar 2216 to pH 9.0 with 10% Na2CO3.\"\
    \n        ],\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"Retain the existing contributor-specific procedure and default 121 C/15 min\
    \ sterilization; preserve its source-specific formulation and any late carbonate/pH\
    \ step. No incubation condition or measured final volume follows.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1016\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\"\
    ,\n        \"source_locator\": \"Page-wide default sterilization\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\"\
    ,\n        \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      },\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Complete short primary including separate carbonate/pH instruction\",\n  \
    \      \"exact_source_quote\": \"Medium data Medium data Search for medium no.\
    \ = [1016]. Unless otherwise stated, sterilize media by autoclaving at 121°C for\
    \ 15 min. 1016   MARINE AGAR 2216 (pH 9.0) Prepare Marine agar 2216 (see Medium\
    \ No. 118 ). After autoclaving, adjust pH to 9.0 with sterilized 10% Na 2 CO 3\
    \ solution. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved\",\n\
    \        \"snapshot_sha256\": \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\"\
    ,\n        \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the existing contributor-specific\
    \ procedure and default 121 C/15 min sterilization; preserve its source-specific\
    \ formulation and any late carbonate/pH step. No incubation condition or measured\
    \ final volume follows.\"\n  },\n  {\n    \"quantity_id\": \"q61\",\n    \"topic\"\
    : \"Generated J119 preparation missing\",\n    \"decision\": \"add\",\n    \"\
    local\": null,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Regenerate the exact\
    \ J119 default procedure after separating the contributors.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm119\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119\"\
    ,\n        \"source_locator\": \"Page-wide default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"d56c41430e65aef256ffb73a3131342275e310d0db99a8e6893d4c08e14b5b5c\"\
    ,\n        \"parsed_text_sha256\": \"8e902ea14398f3deff72743b4efb5e8d370875df49359881483cfbef8e159bb9\"\
    \n      }\n    ],\n    \"rationale\": \"The generated target lacks preparation;\
    \ the J119 maintained owner already has it. Do not pool the other contributors’\
    \ different cycles or pH steps.\"\n  },\n  {\n    \"quantity_id\": \"q62\",\n\
    \    \"topic\": \"JCM Medium J455 scalar pH\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": 10.0,\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": 10.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing scalar matches\
    \ its own source; about 10 remains approximate.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm455\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455\",\n        \"source_locator\"\
    : \"Exact pH instruction\",\n        \"exact_source_quote\": \"Check final pH\
    \ to be about 10.0.\",\n        \"snapshot_sha256\": \"14c9bea7427a16693dba1e20a7ec695cc595ef89157d5cf84c23e000680c4e53\"\
    ,\n        \"parsed_text_sha256\": \"380236b119ed75237fd3182723664d627f21a59e25173909e1c4575b5ed6acfe\"\
    \n      }\n    ],\n    \"rationale\": \"Retain this scalar only within the source-specific\
    \ formulation; do not copy a contributor pH to the BCYE target.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q63\",\n    \"topic\": \"JCM Medium J1001 scalar pH\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": 8.5,\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.5,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing scalar matches\
    \ its own source; about 10 remains approximate.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1001\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001\",\n        \"source_locator\"\
    : \"Exact pH instruction\",\n        \"exact_source_quote\": \"After autoclaving,\
    \ adjust pH to 8.5 with sterilized 10% Na 2 CO 3 solution.\",\n        \"snapshot_sha256\"\
    : \"b41aa3040f5d3925d1a1bdc8a2280e3f24c3cd5027afc129922474ddb9a3b084\",\n    \
    \    \"parsed_text_sha256\": \"f652ac4dc6f253b30ac28be01a2171d01c4a021d77eecdd23b5dab9fcbabefb7\"\
    \n      }\n    ],\n    \"rationale\": \"Retain this scalar only within the source-specific\
    \ formulation; do not copy a contributor pH to the BCYE target.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q64\",\n    \"topic\": \"JCM Medium J1016 scalar pH\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": 9.0,\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing scalar matches\
    \ its own source; about 10 remains approximate.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1016\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016\",\n        \"source_locator\"\
    : \"Exact pH instruction\",\n        \"exact_source_quote\": \"After autoclaving,\
    \ adjust pH to 9.0 with sterilized 10% Na 2 CO 3 solution.\",\n        \"snapshot_sha256\"\
    : \"026bd069f38991d67e7db4f0eeb0d1659931520791f0c8d0a3e102566614262d\",\n    \
    \    \"parsed_text_sha256\": \"ab9aab85ede67032e7d4b23b334fd8bbf29eccd3645ccf875cebb6c989767c4c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain this scalar only within the source-specific\
    \ formulation; do not copy a contributor pH to the BCYE target.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q65\",\n    \"topic\": \"J346 parent only — Yeast extract\
    \ (BD-Difco) 0.5 g\",\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n\
    \    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm346\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\"\
    ,\n        \"source_locator\": \"Exact R2A parent recipe/condition\",\n      \
    \  \"exact_source_quote\": \"Yeast extract (BD-Difco) 0.5 g\",\n        \"snapshot_sha256\"\
    : \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\",\n    \
    \    \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q66\",\n    \"topic\"\
    : \"J346 parent only — Proteose peptone No. 3 (BD-Difco) 0.5 g\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": null,\n    \"layer_decisions\": [],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm346\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\"\
    ,\n        \"source_locator\": \"Exact R2A parent recipe/condition\",\n      \
    \  \"exact_source_quote\": \"Proteose peptone No. 3 (BD-Difco) 0.5 g\",\n    \
    \    \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q67\",\n    \"topic\"\
    : \"J346 parent only — Casamino acids (BD-Difco) 0.5 g\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Casamino\
    \ acids (BD-Difco) 0.5 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q68\",\n    \"topic\"\
    : \"J346 parent only — Glucose 0.5 g\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Glucose\
    \ 0.5 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q69\",\n    \"topic\"\
    : \"J346 parent only — Soluble starch 0.5 g\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Soluble\
    \ starch 0.5 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q70\",\n    \"topic\"\
    : \"J346 parent only — Sodium pyruvate 0.3 g\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Sodium\
    \ pyruvate 0.3 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q71\",\n    \"topic\"\
    : \"J346 parent only — K 2 HPO 4 0.3 g\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"K\
    \ 2 HPO 4 0.3 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q72\",\n    \"topic\"\
    : \"J346 parent only — MgSO 4 ·7H 2 O 0.05 g\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"MgSO\
    \ 4 ·7H 2 O 0.05 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q73\",\n    \"topic\"\
    : \"J346 parent only — Agar 15.0 g\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Agar\
    \ 15.0 g\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q74\",\n    \"topic\"\
    : \"J346 parent only — Distilled water 1.0 L\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Distilled\
    \ water 1.0 L\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q75\",\n    \"topic\"\
    : \"J346 parent only — Adjust pH to 7.2.\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\",\n        \"source_locator\"\
    : \"Exact R2A parent recipe/condition\",\n        \"exact_source_quote\": \"Adjust\
    \ pH to 7.2.\",\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"This is the standalone R2A parent, scoped\
    \ only to J804/J845 relationship assessment. Do not add these undiluted values\
    \ to the target or replace premix quantities; supplier/hydrate details remain\
    \ exactly as printed.\"\n  },\n  {\n    \"quantity_id\": \"q76\",\n    \"topic\"\
    : \"J346 parent sterilization\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm346\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346\"\
    ,\n        \"source_locator\": \"Page-wide parent procedure\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb\"\
    ,\n        \"parsed_text_sha256\": \"839fafe0868d94c929ee8f4325d03194a91bec4ad895d5557ffa0ceeb2eadb15\"\
    \n      }\n    ],\n    \"rationale\": \"The parent default cycle stays with J346;\
    \ the two child pages independently supply their own default instruction.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q77\",\n    \"topic\": \"Marine child relationship\
    \ quantities are not base additions\",\n    \"decision\": \"unsupported\",\n \
    \   \"local\": [\n      {\n        \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n        \"relationship\": \"PH_VARIANT\",\n        \"id\": \"CultureMech:015371\"\
    ,\n        \"name\": \"marine_agar_2216_ph_8_5\",\n        \"notes\": \"JCM Medium\
    \ 1001 adjusts JCM Medium 118 Marine Agar 2216 to pH 8.5.\"\n      },\n      {\n\
    \        \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n        \"relationship\": \"PH_VARIANT\",\n        \"id\": \"CultureMech:015373\"\
    ,\n        \"name\": \"marine_agar_2216_ph_9_0\",\n        \"notes\": \"JCM Medium\
    \ 1016 adjusts JCM Medium 118 Marine Agar 2216 to pH 9.0.\"\n      },\n      {\n\
    \        \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015418\"\
    ,\n        \"name\": \"marine_agar_2216_with_10_nacl\",\n        \"notes\": \"\
    Adds 100 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n \
    \       \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015426\"\
    ,\n        \"name\": \"marine_agar_2216_with_1_nacl\",\n        \"notes\": \"\
    Adds 10 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n  \
    \      \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml\"\
    ,\n        \"relationship\": \"SUPPLEMENTED_VARIANT\",\n        \"id\": \"CultureMech:015387\"\
    ,\n        \"name\": \"marine_agar_2216_with_1_starch\",\n        \"notes\": \"\
    Adds 10 g/L soluble starch to JCM Medium 118 Marine Agar 2216.\"\n      },\n \
    \     {\n        \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015400\"\
    ,\n        \"name\": \"marine_agar_2216_with_3_1_nacl\",\n        \"notes\": \"\
    Adds 31 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n  \
    \      \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015417\"\
    ,\n        \"name\": \"marine_agar_2216_with_5_nacl\",\n        \"notes\": \"\
    Adds 50 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n  \
    \      \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015372\"\
    ,\n        \"name\": \"marine_agar_2216_with_8_0_nacl\",\n        \"notes\": \"\
    Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n  \
    \      \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml\"\
    ,\n        \"relationship\": \"SALINITY_VARIANT\",\n        \"id\": \"CultureMech:015410\"\
    ,\n        \"name\": \"marine_agar_2216_with_8_nacl\",\n        \"notes\": \"\
    Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\n      },\n      {\n  \
    \      \"path\": \"data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml\"\
    ,\n        \"relationship\": \"SUPPLEMENTED_VARIANT\",\n        \"id\": \"CultureMech:015421\"\
    ,\n        \"name\": \"marine_agar_with_1_tween_20\",\n        \"notes\": \"Adds\
    \ 10 g/L Tween 20 to JCM Medium 118 Marine Agar 2216.\"\n      }\n    ],\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/marine_agar_2216.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml\"\
    ,\n            \"relationship\": \"PH_VARIANT\",\n            \"id\": \"CultureMech:015371\"\
    ,\n            \"name\": \"marine_agar_2216_ph_8_5\",\n            \"notes\":\
    \ \"JCM Medium 1001 adjusts JCM Medium 118 Marine Agar 2216 to pH 8.5.\"\n   \
    \       },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml\"\
    ,\n            \"relationship\": \"PH_VARIANT\",\n            \"id\": \"CultureMech:015373\"\
    ,\n            \"name\": \"marine_agar_2216_ph_9_0\",\n            \"notes\":\
    \ \"JCM Medium 1016 adjusts JCM Medium 118 Marine Agar 2216 to pH 9.0.\"\n   \
    \       },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015418\",\n            \"name\": \"marine_agar_2216_with_10_nacl\"\
    ,\n            \"notes\": \"Adds 100 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015426\",\n            \"name\": \"marine_agar_2216_with_1_nacl\"\
    ,\n            \"notes\": \"Adds 10 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml\"\
    ,\n            \"relationship\": \"SUPPLEMENTED_VARIANT\",\n            \"id\"\
    : \"CultureMech:015387\",\n            \"name\": \"marine_agar_2216_with_1_starch\"\
    ,\n            \"notes\": \"Adds 10 g/L soluble starch to JCM Medium 118 Marine\
    \ Agar 2216.\"\n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015400\",\n            \"name\": \"marine_agar_2216_with_3_1_nacl\"\
    ,\n            \"notes\": \"Adds 31 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015417\",\n            \"name\": \"marine_agar_2216_with_5_nacl\"\
    ,\n            \"notes\": \"Adds 50 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015372\",\n            \"name\": \"marine_agar_2216_with_8_0_nacl\"\
    ,\n            \"notes\": \"Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:015410\",\n            \"name\": \"marine_agar_2216_with_8_nacl\"\
    ,\n            \"notes\": \"Adds 80 g/L NaCl to JCM Medium 118 Marine Agar 2216.\"\
    \n          },\n          {\n            \"path\": \"data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml\"\
    ,\n            \"relationship\": \"SUPPLEMENTED_VARIANT\",\n            \"id\"\
    : \"CultureMech:015421\",\n            \"name\": \"marine_agar_with_1_tween_20\"\
    ,\n            \"notes\": \"Adds 10 g/L Tween 20 to JCM Medium 118 Marine Agar\
    \ 2216.\"\n          }\n        ],\n        \"decision\": \"unsupported\",\n \
    \       \"rationale\": \"Exact local child links are resolved, but added-salt/starch/Tween\
    \ quantities in their relationship notes are outside the inspected J118 main formulation.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm118\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118\"\
    ,\n        \"source_locator\": \"Main formulation only\",\n        \"exact_source_quote\"\
    : \"Marine agar 2216 (BD-Difco) 55.1 g Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"e8402dbf59eade77978c11f54a2c6f8233064b34639feb9b2780dfc66c78a129\",\n    \
    \    \"parsed_text_sha256\": \"d58c7e0426fdb2e9321ac2226356dec0dc90eb4f6fea91000167bea3a69ca966\"\
    \n      }\n    ],\n    \"rationale\": \"Keep reciprocal topology separate from\
    \ ingredient curation. The named child records are not contributors here, and\
    \ their supplemental quantities require their own source review; none transfers\
    \ to J118 or BCYE.\"\n  },\n  {\n    \"quantity_id\": \"q78\",\n    \"topic\"\
    : \"No DSM12 soil-extract quantities transfer\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz12GraphIdentity\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf\",\n     \
    \   \"source_locator\": \"Complete independent identity-check recipe\",\n    \
    \    \"exact_source_quote\": \"© 2007 DSMZ GmbH - All rights reserved \\n12. SOIL\
    \ EXTRACT MEDIUM \\n \\n \\nSterilize 400.0 g of air-dried garden soil (with high\
    \ content of organic matter) in 1000 ml \\ntap water for one hour at 121C. Allow\
    \ it to sediment for a few hours at room \\ntemperature. Centrifuge the supernatant.\
    \ Add 15.0 g agar per 1000 ml to the clear \\nsupernatant solution thus obtained.\
    \ Adjust pH to 6.8 - 7.0 and sterilize.\",\n        \"snapshot_sha256\": \"1b4394336f7ace4e09c66fc67ed2e745e3c633b725e436d94335b99289243580\"\
    ,\n        \"parsed_text_sha256\": \"de5da40c03d985f04f682aaf3ccbf31585a595dabef4f3753b977c6396cc0e17\"\
    \n      }\n    ],\n    \"rationale\": \"The 400 g soil/1000 ml tap water extraction,\
    \ 121 C for 1 hour, 15 g agar per 1000 ml supernatant and pH 6.8–7.0 belong to\
    \ the conflicting graph accession only. They are explicitly excluded from every\
    \ contributor formulation.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.002367.merged-formulation-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The BCYE identity carries an unrelated dilute R2A formulation
  description: The target retains 1.82 g/L R2A agar and 15 g/L added agar under JCM119
    identity and treats fifteen distinct formulations as synonyms. Current maintained
    owners already distinguish most of these products and stages; the generated record
    is stale and scientifically overmerged.
  target_ids:
  - CultureMech:002367
  field_paths:
  - media_term
  - ingredients
  - synonyms
  - merged_from
  - merge_fingerprint
  evidence_ids:
  - record
  - jcm119
  - jcm804
  - jcm845
  - jcm1329
  - jcm150
  - togo-bcye
  - jcm455
  - dsmz604
  - togo-me
  - jcm655
  - jcm1202
  - jcm118
  - jcm1001
  - jcm1016
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.5
  native_severity: P2
  normalization_reason: P2 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.002367.complex-product-as-agar
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: R2A agar is falsely linked to the pure agar ingredient
  description: The provider explicitly identifies compound 1844 as complex R2A agar
    (BD-Difco), separately from compound 3 agar. The target’s first secondary CHEBI:2509
    link collapses that whole mixture to agar, while maintained R2A owners already
    link to the local R2A recipe.
  target_ids:
  - CultureMech:002367
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  evidence_ids:
  - r2a-provider
  - chebi2509
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
  issue_key: culturemech.002367.percentage-and-volume-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock percentage bases and final-volume wording exceed the sources
  description: J455 and the two marine pH owners encode 10% carbonate as PERCENT_W_V
    although their primary pages omit the basis. J119’s water note claims a final
    1 L makeup rather than the printed 900 ml water and 100 ml enrichment. Retain
    the existing stage reconstruction and unknown pH-adjustment dose.
  target_ids:
  - CultureMech:002367
  field_paths:
  - ingredients
  - solutions
  - notes
  evidence_ids:
  - jcm119
  - jcm455
  - jcm1001
  - jcm1016
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_jcm_bcye_score20.py
    role: source-specific maintained repair writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_togo_m455_score15.py
    role: source-specific maintained repair writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_jcm_specialized_marine_score15.py
    role: source-specific maintained repair writer
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.002367.graph12-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The asserted graph accession denotes soil-extract medium
  description: Exact DSMZ/API medium 12 denotes SOIL EXTRACT MEDIUM rather than any
    of the merged commercial products. The target and several maintained contributors
    retain this unrelated kg_microbe_match. Current carbonate/pH repairs already removed
    it from some owners.
  target_ids:
  - CultureMech:002367
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - record
  - dsmz12GraphIdentity
  - graph-identity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
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
  issue_key: culturemech.002367.generated-preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The target omits preparation already present in its maintained owners
  description: The true J119 owner retains its default autoclave procedure, while
    the target has no preparation. Other contributors have distinct 115 C/10 min or
    121 C/15 min cycles and separate pH/stock stages that must survive independently.
    Missing details for DSM604/M2859 cannot be filled by borrowing a cycle.
  target_ids:
  - CultureMech:002367
  field_paths:
  - preparation_steps
  - sterilization
  evidence_ids:
  - default-autoclave
  - togo-me
  - jcm455
  - jcm1001
  - jcm1016
  - owner-2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.002367.historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Some historical event timestamps are malformed or lack a timezone
  description: The complete target/owner history inspection identifies eight malformed
    or timezone-naive timestamp instances. Their original wording is retained; neither
    a repair event nor its timestamp authenticates the original source response.
  target_ids:
  - CultureMech:002367
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
  description: Retain exact contributor identities and existing owner repairs, resolve
    bounded remaining owner issues, then regenerate only scientifically compatible
    formulas. Do not combine every source ingredient into BCYE.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
  description: Preserve the complex-product identity during regeneration, use verified
    source-specific recipe/product links, and retain CHEBI:2509 only for actual added
    agar. Avoid invented pure-molecule mappings for commercial premixes.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
  description: Correct only unsupported percentage/final-volume specificity in the
    exact maintained owners and corresponding current constructors; preserve supported
    amounts, separate stock doses and recipe-water inputs. Do not derive carbonate
    mass or measured final concentrations.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_jcm_bcye_score20.py
    role: source-specific maintained repair writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_togo_m455_score15.py
    role: source-specific maintained repair writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_jcm_specialized_marine_score15.py
    role: source-specific maintained repair writer
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
  description: Remove or reconcile the unsupported graph assertion only after checking
    each exact maintained source. Recompute graph matching against the corrected formulation;
    do not guess a replacement accession.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
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
  description: Regenerate the J119 preparation from its verified maintained owner
    after identity reconciliation, retain other contributor protocols in their own
    records, and leave source-undisclosed procedures explicit.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
  description: Preserve append-only history and append a bounded clarification if
    original timing can be recovered; do not invent missing precision or silently
    rewrite old events.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:002367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2859_BCYE_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/me_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_gam_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bacto_marine_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
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
- Current JCM258 returned HTTP200 with Nothing found, not a formulation. TOGO M250
  is usable as its explicitly attributed source snapshot; present primary correspondence
  remains unavailable.
- Preserved optional source attempt compound 1844Identity did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt komodo604detail did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ119api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1329api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ150api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ455api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ258api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ655api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1202api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ118api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1001api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1016api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadive604api did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ119api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1329api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ150api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ455api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ258api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ655api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1202api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ118api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1001api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadiveJ1016api_retry did not provide usable
  response content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- Preserved optional source attempt mediadive604api_retry did not provide usable response
  content. Available exact primary/provider captures supply the bounded comparisons;
  failed attempts do not authenticate older payloads.
- TOGO M2859 has an empty original-source URL and only an unspecified one-litre BCYE
  component. Its exact formulation, supplier and original experiment remain unresolved.
- The exact DSM604 page names Difco 0979 but supplies neither amount nor preparation.
  Both maintained VARIABLE values are appropriate; borrowing the J118 dose would require
  evidence of equivalence.
- The scoped R2A parent contains a PMID:3883894 excerpt without a captured paper response.
  Its original quotation is not independently authenticated here; current JCM346 supports
  a separate formulation comparison.
- The source pages and provider captures support recipe comparisons, not measured
  final volumes, vendor-lot equivalence, fresh experimental growth or complete commercial-product
  compositions.
- The full KG ingredient graph was not recomputed; the separately confirmed medium
  12 identity conflict does not supply a replacement match.
- Relationship-only descendants and excluded namesakes are not extra contributor reviews.
  In particular no DSM585a source or independent formulation is borrowed for M2859.
- This scientific assessment precedes formal review validation and saving; those outcomes
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-040
- generated-medium
```
