# Source and formulation review: anaerobacter_medium (CultureMech:002265)

- Review: 20261021T151935Z-culturemech-002265-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:15:02Z
- Finished UTC: 2026-10-21T15:19:35Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated ANAEROBACTER record conflates the JCM 1085 formulation with two DSMZ 482-derived contributors. Its 20 concentrations flatten distinct stocks and misread added solution volumes as g/L. Reconcile each source-specific owner before regeneration; exact provider access remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 261; batch 027 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-six task batches contain 260 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 263 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002265 | data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml | generated | anaerobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002265 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002265 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/261/strict.tsv |
| validate-terms | passed | True | CultureMech:002265 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002265 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002265 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ1085api | unavailable | True | CultureMech:002265 | mediadiveJ1085api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive482api | unavailable | True | CultureMech:002265 | mediadive482api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo482 | unavailable | False | CultureMech:002265 | komodo482: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodoMediaList | unavailable | False | CultureMech:002265 | komodoMediaList: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: komodo482canonical | unavailable | False | CultureMech:002265 | komodo482canonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadiveJ1085apiRetry | unavailable | True | CultureMech:002265 | mediadiveJ1085apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadive482apiRetry | unavailable | True | CultureMech:002265 | mediadive482apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002265.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:002265.

19 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 19/20 primary and 19/20 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 20: primary 95.00%; secondary 95.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:002265.

27 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Three maintained contributors and two distinct primary recipes

identity: concern. Targets: CultureMech:002265.

The target has CultureMech:002265 and JCM 1085 provenance. Its JCM owner is distinct from KOMODO 482 CultureMech:005604 and DSMZ 482 CultureMech:001611. Both DSMZ-derived owners share their ingredient amounts and preserve reciprocal SOURCE_DUPLICATE links; their identity is not interchangeable with JCM 1085. JCM specifies resazurin 1 mg and two separate 1 mL stocks, whereas DSMZ specifies sodium resazurin 0.1% w/v, 0.50 mL, and one 1 mL SL10 stock. Bicarbonate source amounts also differ. A matching ingredient fingerprint does not justify this merge.

### Main quantities, stock composition and aliquots

consistency: concern. Targets: CultureMech:002265.

All four local layers flatten iron/trace composition into direct ingredients. The JCM layer additionally turns 10, 18.3, 6 and 6 mL additions into 10, 18.3, 6 and 6 g/L. Only sucrose explicitly states w/v: 20% w/v × 10 mL supplies 2 g, not 10 g. Other printed percentage bases and the final volume remain unresolved. The JCM main normalization is numerically compatible with the 1042.3 mL sum of listed liquid inputs, but current API errors cannot verify a provider volume declaration, and that sum is not measured final volume. DSMZ values are source amounts per recipe with 1000 mL water, not an independently established final denominator.

### Source-specific sterilization and stock preparation scope

completeness: concern. Targets: CultureMech:002265.

JCM main anaerobic preparation survives, including bicarbonate filtration under 80% N2/20% CO2, but the source default 121°C/15 min cycle is absent and later doses are disconnected. DSMZ preparation survives in its owner, while KOMODO lacks it. DSMZ SL10 dissolution/makeup appears as a main-medium step rather than a stock procedure. Preserve separate source protocols; the JCM parent187 sulfur treatment and other basal steps do not transfer.

### Classification, applications and organism scope

scope: supported. Targets: CultureMech:002265.

COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract and liquid collection formulations. Bacterial filing and generic microbial-cultivation application are catalog descriptors; no organism, strain, growth result, incubation optimum, DOI or PMID is asserted. The anaerobic source procedures do not validate the KOMODO Aerobic: Yes note as physiology.

### Exact nickel hydrate and resazurin salt

grounding: concern. Targets: CultureMech:002265.

All sources specify NiCl2 hexahydrate in trace stocks, but CHEBI:34887 is Cl2Ni without hydration in both asserted CHEBI slots. DSMZ and KOMODO preferred names specify sodium resazurin while primary CHEBI:8806 is the unsalted resazurin species; JCM’s unqualified Resazurin is a separate source assertion. Do not copy a sodium-specific replacement into the JCM source or invent replacement CURIEs. Other explicit hydrate forms and canonical labels were compared; HCl 25% lacks a printed mass/volume basis.

### Current correction route and historical limitations

provenance: concern. Targets: CultureMech:002265.

Current MediaDive code retains primary stock references instead of flattening all solution recipes, but collects preparation from all solution objects. Unit normalization alone cannot establish a batch denominator or percent basis. Current formulation merging requires compatible full formulations; it does not justify the historical three-way merge. Reconcile normalized source owners and preserve their distinctions before regenerating.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002265.

55 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "JCM main row 0",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.316699",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[0] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 1",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.316699",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[1] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 2",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.316699",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[2] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 3",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.316699",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[3] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 4",
    "field_path": "ingredients[4].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.316699",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[4] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.316699",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 5",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[5] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Preserve this explicit source-only stock dose or water amount in its intended local container; it is not represented as a quantified stock addition.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 6",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[6] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Preserve this explicit source-only stock dose or water amount in its intended local container; it is not represented as a quantified stock addition.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 7",
    "field_path": "ingredients[5].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.959693",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[7] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.959693",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.959693",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 8",
    "field_path": "ingredients[6].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.000959693",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[8] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Primary gives the original batch amount, but not a measured final-volume denominator for the stored g/L; current provider content is unavailable. Preserve source mass and stage without endorsing the rounded normalization.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000959693",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000959693",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main row 9",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
      },
      {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[0] row[9] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "Preserve this explicit source-only stock dose or water amount in its intended local container; it is not represented as a quantified stock addition.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Sucrose 20% w/v, 10 mL",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[1] row[0] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 20% (w/v) sucrose solution                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "An added stock volume is stored as a direct mass concentration. Restore the stock strength, dose and preparation stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "20 g/100 mL × 10 mL = 2 g sucrose delivered; final g/L requires a final-volume basis."
  },
  {
    "ingredient_or_context": "Bicarbonate 8%, 18.3 mL",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "18.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[1] row[1] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;18.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "An added stock volume is stored as a direct mass concentration. Restore the stock strength, dose and preparation stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "18.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "18.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The printed percentage lacks a basis; retain stock label and mL dose without a mass conversion."
  },
  {
    "ingredient_or_context": "Cysteine 5%, 6 mL",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "6",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[2] row[0] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O solution         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "An added stock volume is stored as a direct mass concentration. Restore the stock strength, dose and preparation stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The printed percentage lacks a basis; retain stock label and mL dose without a mass conversion."
  },
  {
    "ingredient_or_context": "Sulfide 5%, 6 mL",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "6",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "HTML table[2] row[1] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0"
      }
    ],
    "rationale": "An added stock volume is stored as a direct mass concentration. Restore the stock strength, dose and preparation stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The printed percentage lacks a basis; retain stock label and mL dose without a mass conversion."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 1 row 0",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1] row[0] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 1 row 1",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1] row[1] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 1 row 2",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[1] row[2] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 0",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[0] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 1",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[1] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 2",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[2] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 3",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[3] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 4",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[4] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 5",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[5] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 6",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[6] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "JCM 187 stock table 2 row 7",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "HTML table[2] row[7] (zero-based raw tables)",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "rationale": "This is composition or water of the separately named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted direct-medium concentration. HCl 25% has no printed basis; its separately stated 7.7 M is molarity, not mass percent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L is inferred without stock/final-volume support."
  },
  {
    "ingredient_or_context": "DSMZ 482 KH2PO4 0.33 g",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.33",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "KH2PO4 0.33 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 NH4Cl 0.33 g",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.33",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "NH4Cl 0.33 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 MgCl2 x 6 H2O 0.33 g",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.33",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "MgCl2 x 6 H2O 0.33 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 CaCl2 x 2 H2O 0.33 g",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.33",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.33 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 KCl 0.33 g",
    "field_path": "ingredients[4].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.33",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Yeast extract 1.00 g",
    "field_path": "ingredients[5].concentration",
    "decision": "unsupported",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Sodium resazurin (0.1% w/v) 0.50 ml",
    "field_path": "ingredients[6].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.0005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "arithmetic": "0.1 g/100 mL × 0.50 mL = 0.0005 g sodium resazurin delivered; the final g/L denominator is still unresolved."
  },
  {
    "ingredient_or_context": "DSMZ 482 NaHCO3 1.50 g",
    "field_path": "ingredients[7].concentration",
    "decision": "unsupported",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "NaHCO3 1.50 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Sucrose 2.00 g",
    "field_path": "ingredients[8].concentration",
    "decision": "unsupported",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "Sucrose 2.00 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 L-Cysteine HCl x H2O 0.30 g",
    "field_path": "ingredients[9].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.30 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Na2S x 9 H2O 0.30 g",
    "field_path": "ingredients[10].concentration",
    "decision": "unsupported",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main table",
        "exact_source_quote": "Na2S x 9 H2O 0.30 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "The primary source amount is supported, but the stored g/L denominator is not established by 1000 mL water alone. Preserve source batch/stock dose and attach evidence without claiming measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 HCl (25%) 10.00 ml",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 FeCl2 x 4 H2O 1.50 g",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 ZnCl2 70.00 mg",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 MnCl2 x 4 H2O 100.00 mg",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 H3BO3 6.00 mg",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 CoCl2 x 6 H2O 190.00 mg",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 CuCl2 x 2 H2O 2.00 mg",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 NiCl2 x 6 H2O 24.00 mg",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Na2MoO4 x 2 H2O 36.00 mg",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 SL10 table",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Restore SL10 stock scope and the explicit 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Trace element solution SL-10 1.00 ml",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main/SL10 named row",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Preserve the explicit dose or solvent amount at its main/stock stage; no extra final denominator is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Distilled water 1000.00 ml",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main/SL10 named row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Preserve the explicit dose or solvent amount at its main/stock stage; no extra final denominator is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except bicarbonate, sucrose, cysteine and sulfide), adjust pH to 7.0, and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add sucrose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of complete medium to pH 7.0, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ 482 Distilled water 990.00 ml",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main/SL10 named row",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Preserve the explicit dose or solvent amount at its main/stock stage; no extra final denominator is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM main pH",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": 7.0,
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "Main preparation",
        "exact_source_quote": "adjust pH to 7.0",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0",
        "parsed_text_sha256": "b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983"
      }
    ],
    "rationale": "The literal pH agrees but has no matching attached claim evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM default cycle",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
      },
      {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "Collection default header",
        "exact_source_quote": "autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0",
        "parsed_text_sha256": "b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983"
      }
    ],
    "rationale": "The applicable stated cycle is missing locally; preserve source qualification Unless otherwise stated.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):"
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved and stored under a N2 atmosphere):"
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "JCM bicarbonate gas mixture",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):",
    "source_snippets": [
      {
        "source_key": "jcm1085",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085",
        "source_locator": "Post-cooling stock instructions",
        "exact_source_quote": "80% N 2 and 20% CO2 gas mixture",
        "snapshot_sha256": "41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0",
        "parsed_text_sha256": "b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983"
      }
    ],
    "rationale": "The gas ratio survives in prose; attach source evidence and keep bicarbonate stock scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add per liter the following sterile solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ main pH",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": 7.0,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "Main preparation",
        "exact_source_quote": "adjust pH to 7.0",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "Both owners retain the pH without attached claim evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ N2 fraction and sparging duration",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main preparation or SL10 final makeup",
        "exact_source_quote": "100% N2 gas for 30 - 45 min",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "DSMZ owner retains the literal endpoints; KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach evidence; retain source-specific gas handling.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sucrose, cysteine and sulfide), adjust pH to 7.0, and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add sucrose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of complete medium to pH 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ bicarbonate gas ratio",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main preparation or SL10 final makeup",
        "exact_source_quote": "80% N2 and 20% CO2 gas mixture",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "DSMZ owner retains the literal endpoints; KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach evidence; retain source-specific gas handling.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sucrose, cysteine and sulfide), adjust pH to 7.0, and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization add sucrose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of complete medium to pH 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "DSMZ stock final makeup",
    "field_path": "preparation_steps",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz482",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf",
        "source_locator": "PDF page1 main preparation or SL10 final makeup",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236",
        "parsed_text_sha256": "f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502"
      }
    ],
    "rationale": "DSMZ owner retains the literal endpoints; KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach evidence; retain source-specific gas handling.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ]
  }
]

## Findings

### f1: Distinct source formulations and stock additions are conflated

blocker / open / confirmed; issue key: anaerobacter-distinct-sources-and-stock-flattening.

JCM 1085 and DSMZ 482 differ in resazurin amount/form, bicarbonate and stock architecture. The generated JCM recipe includes20 direct concentrations, including undiluted trace-stock amounts and four added solution volumes mislabeled as g/L. The DSMZ-derived owners also flatten SL10. This changes the denoted medium; neither a fingerprint nor conditional volume arithmetic supplies a valid combined formula.

### f2: Nickel hexahydrate uses an anhydrous identifier

major / open / confirmed; issue key: anaerobacter-nickel-hydrate.

All four layers name NiCl2 x 6 H2O but assert CHEBI:34887, whose captured formula is Cl2Ni. The 24 mg source stock amount must retain its hydrate identity and stock stage.

### f3: DSMZ-derived sodium resazurin is grounded to unsalted resazurin

major / open / confirmed; issue key: anaerobacter-dsmz-resazurin-salt.

The DSMZ and KOMODO owners explicitly name sodium resazurin but use CHEBI:8806. JCM’s unqualified Resazurin is a distinct source assertion; its target mapping is not shown wrong by the DSMZ salt evidence.

### f4: Preparation is incomplete or attached to the wrong source stage

major / open / confirmed; issue key: anaerobacter-preparation-source-scope.

The JCM default 121°C/15 min cycle is absent; KOMODO lacks the DSMZ protocol, while the DSMZ owner stores SL10 dissolution/makeup at the medium level. These source-specific procedures must accompany reconstructed stocks without transferring unrelated JCM 187 instructions.

### f5: KOMODO catalog metadata and malformed history need explicit qualification

minor / open / confirmed; issue key: anaerobacter-komodo-provenance-limits.

The KOMODO owner retains Aerobic: Yes from a table whose primary recipe is anaerobic, plus one malformed and one timezone-naive historical timestamp. Retain the catalog value only with attribution and preserve old history rather than rewriting it.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the JCM and DSMZ formulations separately in their maintained owners, preserving the exact source stock architecture/units and unresolved denominators. Retain only source-supported duplicate relationships; regenerate a compatible source-specific target after review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve an exact supported nickel hexahydrate identity without guessing a CURIE or changing the source mass; correct both current CHEBI slots where asserted.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the sodium-resazurin form only in the DSMZ-derived owners; preserve JCM wording and the separate 1 mg versus 0.5 mg source quantities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore the applicable source cycle, gas handling and stock-specific preparation in each maintained source owner, then regenerate. Use broad P2 for this combined representation defect; existing sterilization wording is not described as entirely absent.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Append a source-specific clarification of the catalog flag and timestamp limitations without fabricating times or modifying prior events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/anaerobacter_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch027/261/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/261/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml:1:id: CultureMech:002265<br>./data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml:1:id: CultureMech:002265<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/261/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 31 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/261/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085; Complete JCM 1085 main table, two later-addition tables and preparation | supports | Exact JCM source uses 1 mg resazurin, separate iron and trace stocks, and four later stock additions. |
| jcm-stocks | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; FeCl2 solution and Trace element solution subsections only | supports | Only the two named stock recipes transfer; parent basal medium, vitamins, sulfur treatment and pH do not. |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf; DSMZ 482 PDF page1, full main recipe, SL10 and preparation | supports | Distinct DSMZ source uses 0.5 mg sodium resazurin, combined SL10 and 1.50 g bicarbonate; source stock masses and final medium are not interchangeable. |
| sl10 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; SL10 subsection across PDF pages1–2 only | supports | Only SL10 composition and its 1000 mL makeup transfer; unrelated parent basal formulation and fluids are excluded. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact href MediaInfo=482 and exact column header | context_only | KOMODO 482 links to DSMZ 482 and marks Is Aerobic true. This is catalog metadata, in tension with the anaerobic primary; it does not prove growth physiology. |
| mediadiveJ1085api-attempt | https://mediadive.dsmz.de/rest/medium/J1085; Preserved exact public retrieval result | context_only | mediadiveJ1085api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive482api-attempt | https://mediadive.dsmz.de/rest/medium/482; Preserved exact public retrieval result | context_only | mediadive482api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo482-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=482; Preserved exact public retrieval result | context_only | komodo482: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodoMediaList-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaList; Preserved exact public retrieval result | context_only | komodoMediaList: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| komodo482canonical-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=482; Preserved exact public retrieval result | context_only | komodo482canonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadiveJ1085apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/J1085; Preserved exact public retrieval result | context_only | mediadiveJ1085apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadive482apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/482; Preserved exact public retrieval result | context_only | mediadive482apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17992 resolves to sucrose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term", "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml; data/normalized_yaml/bacterial/anaerobacter_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:17.625410"}]}, {"input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml", "events": 6, "timestamp_issues": []}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch027/261/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch027/261/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- mediadiveJ1085api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive482api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo482: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodoMediaList: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- komodo482canonical: exact public request returned HTTP 403; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadiveJ1085apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadive482apiRetry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- The unavailable exact MediaDive J1085/482 endpoints prevent independent confirmation of the historical normalized g/L values; primary collection recipes remain available and are the basis of the stage/identity findings.
- No measured final-medium volume, density, or unprinted percentage basis is invented. JCM 187 and DSMZ 320 are used only for explicitly referenced stocks.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151935Z-culturemech-002265-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobacter_medium (CultureMech:002265)'
started_at: '2026-10-21T15:15:02Z'
finished_at: '2026-10-21T15:19:35Z'
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
summary: The generated ANAEROBACTER record conflates the JCM 1085 formulation with
  two DSMZ 482-derived contributors. Its 20 concentrations flatten distinct stocks
  and misread added solution volumes as g/L. Reconcile each source-specific owner
  before regeneration; exact provider access remains unavailable.
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
  - path: data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
    sha256: 05b9880152660f056da25595ece107cb3c665b46aab1474ab72965c03c8bae96
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    sha256: bba06dceccd039587514c9a952083385f684ed4b4a7109f5f54ce7f9e82987e5
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    sha256: 596cefadcb01bce6fe6a1a68b6ccac26cb81db4bcb291db883a6a0cfc5bb0553
    role: context
  - path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
    sha256: f24763f675310368af2b0c0b492c493403920696ad7031f7b5afe712f56b582d
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
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 261; batch 027 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:002265
targets:
- target_id: CultureMech:002265
  path: data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  label: anaerobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch027/261/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/261/strict.tsv"
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002265
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
  - CultureMech:002265
- check_id: mediadiveJ1085api-source-access
  name: 'Exact source content access: mediadiveJ1085api'
  required: true
  status: unavailable
  summary: 'mediadiveJ1085api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - mediadiveJ1085api-attempt
- check_id: mediadive482api-source-access
  name: 'Exact source content access: mediadive482api'
  required: true
  status: unavailable
  summary: 'mediadive482api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - mediadive482api-attempt
- check_id: komodo482-source-access
  name: 'Exact source content access: komodo482'
  required: false
  status: unavailable
  summary: 'komodo482: exact public request returned HTTP 403; original access time,
    response bytes and any separately recorded retry are retained. Error bytes do
    not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - komodo482-attempt
- check_id: komodoMediaList-source-access
  name: 'Exact source content access: komodoMediaList'
  required: false
  status: unavailable
  summary: 'komodoMediaList: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - komodoMediaList-attempt
- check_id: komodo482canonical-source-access
  name: 'Exact source content access: komodo482canonical'
  required: false
  status: unavailable
  summary: 'komodo482canonical: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - komodo482canonical-attempt
- check_id: mediadiveJ1085apiRetry-source-access
  name: 'Exact source content access: mediadiveJ1085apiRetry'
  required: true
  status: unavailable
  summary: 'mediadiveJ1085apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - mediadiveJ1085apiRetry-attempt
- check_id: mediadive482apiRetry-source-access
  name: 'Exact source content access: mediadive482apiRetry'
  required: true
  status: unavailable
  summary: 'mediadive482apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - mediadive482apiRetry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:15.060699Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/261/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:16.065213Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/261/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:17.693148Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:18.571760Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:19:34Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml:1:id:
    CultureMech:002265

    ./data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml:1:id: CultureMech:002265

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/261/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:19:34Z'
  support: supports
  summary: 31 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 27e931a772c9649a4ec315531be13d9530671c1f3be412b30ea5c86ccddda620
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/261/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: c722c5de895261665d754c76439589e8c9745b25478a00bf31df4fa08f98e057
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:19:34Z'
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
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085
  locator: Complete JCM 1085 main table, two later-addition tables and preparation
  accessed_at: '2026-10-21T15:02:34.819304Z'
  support: supports
  summary: Exact JCM source uses 1 mg resazurin, separate iron and trace stocks, and
    four later stock additions.
  snapshot_sha256: 41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0
- evidence_id: jcm-stocks
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: FeCl2 solution and Trace element solution subsections only
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Only the two named stock recipes transfer; parent basal medium, vitamins,
    sulfur treatment and pH do not.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf
  locator: DSMZ 482 PDF page1, full main recipe, SL10 and preparation
  accessed_at: '2026-10-21T15:02:34.281321Z'
  support: supports
  summary: Distinct DSMZ source uses 0.5 mg sodium resazurin, combined SL10 and 1.50
    g bicarbonate; source stock masses and final medium are not interchangeable.
  snapshot_sha256: 13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236
- evidence_id: sl10
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: SL10 subsection across PDF pages1–2 only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: Only SL10 composition and its 1000 mL makeup transfer; unrelated parent
    basal formulation and fluids are excluded.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact href MediaInfo=482 and exact column header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: KOMODO 482 links to DSMZ 482 and marks Is Aerobic true. This is catalog
    metadata, in tension with the anaerobic primary; it does not prove growth physiology.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=482'\
    \ >482</a></TD>\n\t\t\t\t\t<TD>ANAEROBACTER medium</TD>\n\t\t\t\t\t<TD> 7.0</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadiveJ1085api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1085
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:33.658317Z'
  support: context_only
  summary: 'mediadiveJ1085api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive482api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/482
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:33.652928Z'
  support: context_only
  summary: 'mediadive482api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo482-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=482
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:33.449748Z'
  support: context_only
  summary: 'komodo482: exact public request returned HTTP 403; original access time,
    response bytes and any separately recorded retry are retained. Error bytes do
    not establish formulation or historical absence.'
  snapshot_sha256: d9696c8a47fe1b2b7878d61bbd6c9c3a2b62648ce5c867e628a3860439805d62
- evidence_id: komodoMediaList-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaList
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:33.449219Z'
  support: context_only
  summary: 'komodoMediaList: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: bd4daf9caafd1ca06f800e3f7ede0c921fd43c4c01e9cc31ed88068e12f94251
- evidence_id: komodo482canonical-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=482
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:03:39.698432Z'
  support: context_only
  summary: 'komodo482canonical: exact public request returned HTTP 403; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 6a8340f14eb99067a5de38929a5dcc622456305e239164f164540450eac1f7b5
- evidence_id: mediadiveJ1085apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1085
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:03:39.913167Z'
  support: context_only
  summary: 'mediadiveJ1085apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive482apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/482
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:03:39.703235Z'
  support: context_only
  summary: 'mediadive482apiRetry: exact public request returned HTTP 503; original
    access time, response bytes and any separately recorded retry are retained. Error
    bytes do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17992
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:31.913996Z'
  support: supports
  summary: CHEBI:17992 resolves to sucrose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa
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
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
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
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
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
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
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
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:19:34Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term",
    "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id":
    "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type":
    "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml;
    data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml; data/normalized_yaml/bacterial/anaerobacter_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:17.625410"}]}, {"input": "data/normalized_yaml/bacterial/anaerobacter_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/261/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c666b13a797e84a77b953d196c37867a9270461f6912cbd7bd308b48b4a9ffb3
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/261/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:19:34Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 9fcf46a459e498ac9875dbcf26fa5ccbde6e4f154dcbb721e008b16d432a2c8c
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '19 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 19/20
    primary and 19/20 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi17883
  - chebi17992
  - chebi31206
  - chebi32139
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 20: primary 95.00%;
    secondary 95.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 27 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: identity
  area: identity
  topic: Three maintained contributors and two distinct primary recipes
  outcome: concern
  summary: The target has CultureMech:002265 and JCM 1085 provenance. Its JCM owner
    is distinct from KOMODO 482 CultureMech:005604 and DSMZ 482 CultureMech:001611.
    Both DSMZ-derived owners share their ingredient amounts and preserve reciprocal
    SOURCE_DUPLICATE links; their identity is not interchangeable with JCM 1085. JCM
    specifies resazurin 1 mg and two separate 1 mL stocks, whereas DSMZ specifies
    sodium resazurin 0.1% w/v, 0.50 mL, and one 1 mL SL10 stock. Bicarbonate source
    amounts also differ. A matching ingredient fingerprint does not justify this merge.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - jcm
  - dsmz
  - komodo-catalog
  - id-search
- assessment_id: formulation
  area: consistency
  topic: Main quantities, stock composition and aliquots
  outcome: concern
  summary: 'All four local layers flatten iron/trace composition into direct ingredients.
    The JCM layer additionally turns 10, 18.3, 6 and 6 mL additions into 10, 18.3,
    6 and 6 g/L. Only sucrose explicitly states w/v: 20% w/v × 10 mL supplies 2 g,
    not 10 g. Other printed percentage bases and the final volume remain unresolved.
    The JCM main normalization is numerically compatible with the 1042.3 mL sum of
    listed liquid inputs, but current API errors cannot verify a provider volume declaration,
    and that sum is not measured final volume. DSMZ values are source amounts per
    recipe with 1000 mL water, not an independently established final denominator.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - jcm
  - jcm-stocks
  - dsmz
  - sl10
- assessment_id: preparation
  area: completeness
  topic: Source-specific sterilization and stock preparation scope
  outcome: concern
  summary: JCM main anaerobic preparation survives, including bicarbonate filtration
    under 80% N2/20% CO2, but the source default 121°C/15 min cycle is absent and
    later doses are disconnected. DSMZ preparation survives in its owner, while KOMODO
    lacks it. DSMZ SL10 dissolution/makeup appears as a main-medium step rather than
    a stock procedure. Preserve separate source protocols; the JCM parent187 sulfur
    treatment and other basal steps do not transfer.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - jcm
  - dsmz
  - jcm-stocks
- assessment_id: classification
  area: scope
  topic: Classification, applications and organism scope
  outcome: supported
  summary: 'COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract and liquid
    collection formulations. Bacterial filing and generic microbial-cultivation application
    are catalog descriptors; no organism, strain, growth result, incubation optimum,
    DOI or PMID is asserted. The anaerobic source procedures do not validate the KOMODO
    Aerobic: Yes note as physiology.'
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - jcm
  - dsmz
  - komodo-catalog
- assessment_id: forms
  area: grounding
  topic: Exact nickel hydrate and resazurin salt
  outcome: concern
  summary: All sources specify NiCl2 hexahydrate in trace stocks, but CHEBI:34887
    is Cl2Ni without hydration in both asserted CHEBI slots. DSMZ and KOMODO preferred
    names specify sodium resazurin while primary CHEBI:8806 is the unsalted resazurin
    species; JCM’s unqualified Resazurin is a separate source assertion. Do not copy
    a sodium-specific replacement into the JCM source or invent replacement CURIEs.
    Other explicit hydrate forms and canonical labels were compared; HCl 25% lacks
    a printed mass/volume basis.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - jcm
  - jcm-stocks
  - dsmz
  - chebi34887
  - chebi8806
- assessment_id: writers
  area: provenance
  topic: Current correction route and historical limitations
  outcome: concern
  summary: Current MediaDive code retains primary stock references instead of flattening
    all solution recipes, but collects preparation from all solution objects. Unit
    normalization alone cannot establish a batch denominator or percent basis. Current
    formulation merging requires compatible full formulations; it does not justify
    the historical three-way merge. Reconcile normalized source owners and preserve
    their distinctions before regenerating.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 55 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002265
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"JCM main row 0\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"unsupported\",\n    \"\
    local\": {\n      \"value\": \"0.316699\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1085\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[0] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl     \
    \                                           </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 1\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.316699\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[1] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 2\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.316699\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[2] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KCl                  \
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 3\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.316699\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[3] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 4\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.316699\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[4] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.316699\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 5\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1085\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\",\n        \"source_locator\"\
    : \"HTML table[0] row[5] (zero-based raw tables)\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution (see Medium No. <a href=\\\"\
    /cgi-bin/jcm/jcm_grmd?GRMD=187\\\">187</a>)                </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit source-only stock\
    \ dose or water amount in its intended local container; it is not represented\
    \ as a quantified stock addition.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM main row 6\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[6] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Trace element solution\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=187\\\">187</a>)    \
    \       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit source-only stock\
    \ dose or water amount in its intended local container; it is not represented\
    \ as a quantified stock addition.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM main row 7\",\n    \"field_path\": \"ingredients[5].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.959693\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[7] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Yeast extract        \
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.959693\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.959693\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"JCM main row 8\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.000959693\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[0] row[8] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Resazurin            \
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Primary gives the original batch amount,\
    \ but not a measured final-volume denominator for the stored g/L; current provider\
    \ content is unavailable. Preserve source mass and stage without endorsing the\
    \ rounded normalization.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.000959693\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000959693\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"JCM main row 9\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": [\n      {\n        \"step_number\"\
    : 1,\n        \"action\": \"AUTOCLAVE\",\n        \"description\": \"Mix components\
    \ thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling,\
    \ aseptically and anaerobically add per liter the following sterile solutions\
    \ from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized\
    \ and stored under 80% N2 and 20% CO2 gas mixture):\"\n      },\n      {\n   \
    \     \"step_number\": 2,\n        \"action\": \"AUTOCLAVE\",\n        \"description\"\
    : \"Dispense the medium into culture vessels under a N2 atmosphere and seal with\
    \ butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved\
    \ and stored under a N2 atmosphere):\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1085\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\",\n        \"source_locator\"\
    : \"HTML table[0] row[9] (zero-based raw tables)\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this explicit source-only stock\
    \ dose or water amount in its intended local container; it is not represented\
    \ as a quantified stock addition.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : [\n          {\n            \"step_number\": 1,\n            \"action\": \"\
    AUTOCLAVE\",\n            \"description\": \"Mix components thoroughly, adjust\
    \ pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically and\
    \ anaerobically add per liter the following sterile solutions from anaerobic stocks\
    \ (autoclaved and stored under a N2 atmosphere or *filter-sterilized and stored\
    \ under 80% N2 and 20% CO2 gas mixture):\"\n          },\n          {\n      \
    \      \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\",\n         \
    \   \"description\": \"Dispense the medium into culture vessels under a N2 atmosphere\
    \ and seal with butyl rubber stoppers. Finally, add per litter the following solutions\
    \ (autoclaved and stored under a N2 atmosphere):\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 7.0\
    \ and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically\
    \ add per liter the following sterile solutions from anaerobic stocks (autoclaved\
    \ and stored under a N2 atmosphere or *filter-sterilized and stored under 80%\
    \ N2 and 20% CO2 gas mixture):\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl\
    \ rubber stoppers. Finally, add per litter the following solutions (autoclaved\
    \ and stored under a N2 atmosphere):\"\n          }\n        ],\n        \"decision\"\
    : \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Sucrose\
    \ 20% w/v, 10 mL\",\n    \"field_path\": \"ingredients[7].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"10\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[1] row[0] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 20% (w/v) sucrose solution\
    \                            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"An added stock volume is stored as a direct\
    \ mass concentration. Restore the stock strength, dose and preparation stage.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"20\
    \ g/100 mL × 10 mL = 2 g sucrose delivered; final g/L requires a final-volume\
    \ basis.\"\n  },\n  {\n    \"ingredient_or_context\": \"Bicarbonate 8%, 18.3 mL\"\
    ,\n    \"field_path\": \"ingredients[8].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"18.3\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1085\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[1] row[1] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*\
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;18.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"An added stock volume is stored as a direct\
    \ mass concentration. Restore the stock strength, dose and preparation stage.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"18.3\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.3\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"The printed percentage lacks a basis; retain stock label and mL dose without\
    \ a mass conversion.\"\n  },\n  {\n    \"ingredient_or_context\": \"Cysteine 5%,\
    \ 6 mL\",\n    \"field_path\": \"ingredients[9].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"6\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[2] row[0] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% L-Cysteine&#183;HCl&#183;H<sub>2</sub>O\
    \ solution         </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    \n      }\n    ],\n    \"rationale\": \"An added stock volume is stored as a direct\
    \ mass concentration. Restore the stock strength, dose and preparation stage.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"6\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ printed percentage lacks a basis; retain stock label and mL dose without a mass\
    \ conversion.\"\n  },\n  {\n    \"ingredient_or_context\": \"Sulfide 5%, 6 mL\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"6\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1085\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"HTML table[2] row[1] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O\
    \ solution                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\n     \
    \ }\n    ],\n    \"rationale\": \"An added stock volume is stored as a direct\
    \ mass concentration. Restore the stock strength, dose and preparation stage.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"6\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"The\
    \ printed percentage lacks a basis; retain stock label and mL dose without a mass\
    \ conversion.\"\n  },\n  {\n    \"ingredient_or_context\": \"JCM 187 stock table\
    \ 1 row 0\",\n    \"field_path\": \"ingredients[11].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"2.5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1] row[0] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 25% HCl (7.7 M)      \
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[11].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Preserve\
    \ g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 1 row 1\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1] row[1] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[12].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Preserve\
    \ g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 1 row 2\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[1] row[2] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water      \
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"Preserve g or\
    \ mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L\
    \ is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 0\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.07\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[0] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>     \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[13].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 1\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[1] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O\
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[14].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Preserve\
    \ g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 2\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.006\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[2] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[15].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.006\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 3\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.19\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[3] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[16].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 4\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[4] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[17].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.002\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 5\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.024\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[5] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[18].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.024\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 6\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.036\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[6] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O\
    \                            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[19].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.036\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Preserve g or mg per stock recipe and the 1 mL receiving-medium dose. No final-medium\
    \ g/L is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM 187 stock table 2 row 7\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"HTML table[2] row[7] (zero-based raw tables)\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water      \
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\":\
    \ \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\n     \
    \ }\n    ],\n    \"rationale\": \"This is composition or water of the separately\
    \ named iron/trace stock, added at 1 mL each by JCM 1085. It cannot be an undiluted\
    \ direct-medium concentration. HCl 25% has no printed basis; its separately stated\
    \ 7.7 M is molarity, not mass percent.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"Preserve g or\
    \ mg per stock recipe and the 1 mL receiving-medium dose. No final-medium g/L\
    \ is inferred without stock/final-volume support.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ 482 KH2PO4 0.33 g\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.33\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.33 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.33\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 NH4Cl 0.33 g\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.33\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.33 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.33\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 MgCl2 x 6 H2O 0.33 g\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.33\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.33 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.33\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 CaCl2 x 2 H2O 0.33 g\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.33\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.33 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.33\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 KCl 0.33 g\",\n    \"field_path\": \"ingredients[4].concentration\",\n\
    \    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.33\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"KCl 0.33 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.33\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 Yeast extract 1.00 g\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 Sodium resazurin (0.1% w/v) 0.50 ml\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.0005\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ],\n    \"arithmetic\": \"0.1 g/100 mL × 0.50\
    \ mL = 0.0005 g sodium resazurin delivered; the final g/L denominator is still\
    \ unresolved.\"\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ 482 NaHCO3 1.50\
    \ g\",\n    \"field_path\": \"ingredients[7].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"1.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 1.50 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 Sucrose 2.00 g\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"Sucrose 2.00 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 L-Cysteine HCl x H2O 0.30 g\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"L-Cysteine HCl x H2O 0.30 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 Na2S x 9 H2O 0.30 g\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main table\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.30 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"The primary source amount is supported,\
    \ but the stored g/L denominator is not established by 1000 mL water alone. Preserve\
    \ source batch/stock dose and attach evidence without claiming measured final\
    \ volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"\
    DSMZ 482 HCl (25%) 10.00 ml\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ 482 FeCl2 x 4 H2O 1.50 g\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ 482 ZnCl2 70.00 mg\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.07\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 MnCl2 x 4 H2O 100.00 mg\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ 482 H3BO3 6.00 mg\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.006\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 CoCl2 x 6 H2O 190.00 mg\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.19\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 CuCl2 x 2 H2O 2.00 mg\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 NiCl2 x 6 H2O 24.00 mg\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.024\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 Na2MoO4 x 2 H2O 36.00 mg\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.036\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 SL10 table\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Restore SL10 stock scope and the explicit\
    \ 1 mL receiving dose; HCl 25% cannot be converted to 2.5 g/L without an established\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ\
    \ 482 Trace element solution SL-10 1.00 ml\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz482\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\",\n        \"\
    source_locator\": \"PDF page1 main/SL10 named row\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the explicit dose or solvent\
    \ amount at its main/stock stage; no extra final denominator is inferred.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ 482 Distilled water 1000.00 ml\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz482\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\",\n        \"\
    source_locator\": \"PDF page1 main/SL10 named row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the explicit dose or solvent\
    \ amount at its main/stock stage; no extra final denominator is inferred.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients (except bicarbonate, sucrose,\
    \ cysteine and sulfide), adjust pH to 7.0, and sparge medium with 100% N2 gas\
    \ for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. After sterilization\
    \ add sucrose, cysteine and sulfide from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared\
    \ under 80% N2 and 20% CO2 gas mixture. Adjust pH of complete medium to pH 7.0,\
    \ if necessary.\"\n          },\n          {\n            \"step_number\": 2,\n\
    \            \"action\": \"DISSOLVE\",\n            \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"DSMZ 482 Distilled\
    \ water 990.00 ml\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main/SL10 named row\",\n        \"\
    exact_source_quote\": \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\"\
    : \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\",\n    \
    \    \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the explicit dose or solvent\
    \ amount at its main/stock stage; no extra final denominator is inferred.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM main pH\",\n    \"field_path\": \"ph_value\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": 7.0,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"Main preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7.0\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    ,\n        \"parsed_text_sha256\": \"b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983\"\
    \n      }\n    ],\n    \"rationale\": \"The literal pH agrees but has no matching\
    \ attached claim evidence.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"JCM default cycle\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"\
    action\": \"AUTOCLAVE\",\n        \"description\": \"Mix components thoroughly,\
    \ adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically\
    \ and anaerobically add per liter the following sterile solutions from anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and\
    \ stored under 80% N2 and 20% CO2 gas mixture):\"\n      },\n      {\n       \
    \ \"step_number\": 2,\n        \"action\": \"AUTOCLAVE\",\n        \"description\"\
    : \"Dispense the medium into culture vessels under a N2 atmosphere and seal with\
    \ butyl rubber stoppers. Finally, add per litter the following solutions (autoclaved\
    \ and stored under a N2 atmosphere):\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1085\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\",\n        \"source_locator\"\
    : \"Collection default header\",\n        \"exact_source_quote\": \"autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\"\
    ,\n        \"parsed_text_sha256\": \"b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983\"\
    \n      }\n    ],\n    \"rationale\": \"The applicable stated cycle is missing\
    \ locally; preserve source qualification Unless otherwise stated.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Mix components\
    \ thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling,\
    \ aseptically and anaerobically add per liter the following sterile solutions\
    \ from anaerobic stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized\
    \ and stored under 80% N2 and 20% CO2 gas mixture):\"\n          },\n        \
    \  {\n            \"step_number\": 2,\n            \"action\": \"AUTOCLAVE\",\n\
    \            \"description\": \"Dispense the medium into culture vessels under\
    \ a N2 atmosphere and seal with butyl rubber stoppers. Finally, add per litter\
    \ the following solutions (autoclaved and stored under a N2 atmosphere):\"\n \
    \         }\n        ],\n        \"decision\": \"add\"\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 7.0\
    \ and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically\
    \ add per liter the following sterile solutions from anaerobic stocks (autoclaved\
    \ and stored under a N2 atmosphere or *filter-sterilized and stored under 80%\
    \ N2 and 20% CO2 gas mixture):\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Dispense the medium into culture vessels under a N2 atmosphere and seal with butyl\
    \ rubber stoppers. Finally, add per litter the following solutions (autoclaved\
    \ and stored under a N2 atmosphere):\"\n          }\n        ],\n        \"decision\"\
    : \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"JCM bicarbonate\
    \ gas mixture\",\n    \"field_path\": \"preparation_steps[0].description\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local\": \"Mix components thoroughly,\
    \ adjust pH to 7.0 and autoclave under a N2 atmosphere. After cooling, aseptically\
    \ and anaerobically add per liter the following sterile solutions from anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere or *filter-sterilized and\
    \ stored under 80% N2 and 20% CO2 gas mixture):\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1085\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1085\"\
    ,\n        \"source_locator\": \"Post-cooling stock instructions\",\n        \"\
    exact_source_quote\": \"80% N 2 and 20% CO2 gas mixture\",\n        \"snapshot_sha256\"\
    : \"41eeefe0b0cdc3285f2d8fcc95d5cb6a3a68025d8ad29a3c644912965716f8e0\",\n    \
    \    \"parsed_text_sha256\": \"b8b7e7341124cedc92e2a5dfe9b54ceb13297dd6e8d5578690ac60e4e01ff983\"\
    \n      }\n    ],\n    \"rationale\": \"The gas ratio survives in prose; attach\
    \ source evidence and keep bicarbonate stock scope.\",\n    \"action_taken\":\
    \ \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Mix components thoroughly, adjust pH to 7.0 and autoclave\
    \ under a N2 atmosphere. After cooling, aseptically and anaerobically add per\
    \ liter the following sterile solutions from anaerobic stocks (autoclaved and\
    \ stored under a N2 atmosphere or *filter-sterilized and stored under 80% N2 and\
    \ 20% CO2 gas mixture):\",\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix components thoroughly, adjust pH to 7.0 and autoclave under a N2 atmosphere.\
    \ After cooling, aseptically and anaerobically add per liter the following sterile\
    \ solutions from anaerobic stocks (autoclaved and stored under a N2 atmosphere\
    \ or *filter-sterilized and stored under 80% N2 and 20% CO2 gas mixture):\",\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ main pH\",\n    \"field_path\": \"ph_value\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": 7.0,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"Main preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7.0\",\n        \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"Both owners retain the pH without attached\
    \ claim evidence.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ N2 fraction and sparging duration\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz482\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\",\n        \"\
    source_locator\": \"PDF page1 main preparation or SL10 final makeup\",\n     \
    \   \"exact_source_quote\": \"100% N2 gas for 30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\",\n    \
    \    \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ owner retains the literal endpoints;\
    \ KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach\
    \ evidence; retain source-specific gas handling.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sucrose, cysteine and sulfide),\
    \ adjust pH to 7.0, and sparge medium with 100% N2 gas for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. After sterilization add sucrose, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Adjust pH of complete medium to pH 7.0, if necessary.\",\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ bicarbonate gas ratio\",\n    \"field_path\": \"preparation_steps\",\n\
    \    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz482\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\"\
    ,\n        \"source_locator\": \"PDF page1 main preparation or SL10 final makeup\"\
    ,\n        \"exact_source_quote\": \"80% N2 and 20% CO2 gas mixture\",\n     \
    \   \"snapshot_sha256\": \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\"\
    ,\n        \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ owner retains the literal endpoints;\
    \ KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach\
    \ evidence; retain source-specific gas handling.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sucrose, cysteine and sulfide),\
    \ adjust pH to 7.0, and sparge medium with 100% N2 gas for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. After sterilization add sucrose, cysteine\
    \ and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and\
    \ bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%\
    \ CO2 gas mixture. Adjust pH of complete medium to pH 7.0, if necessary.\",\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"DSMZ stock final makeup\",\n    \"field_path\": \"preparation_steps\",\n \
    \   \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz482\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium482.pdf\",\n        \"\
    source_locator\": \"PDF page1 main preparation or SL10 final makeup\",\n     \
    \   \"exact_source_quote\": \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\"\
    : \"13c2d94fbd160780f86c1152a6a8d6ec99e8eb80f3c83d768a93b39b5f2d9236\",\n    \
    \    \"parsed_text_sha256\": \"f302db0f341e3dc59d257d57990c9b1d1b4e527236f9a4c02ba4600269d06502\"\
    \n      }\n    ],\n    \"rationale\": \"DSMZ owner retains the literal endpoints;\
    \ KOMODO does not. Restore SL10 stock scope for the 1000 mL endpoint and attach\
    \ evidence; retain source-specific gas handling.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacter_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: anaerobacter-distinct-sources-and-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Distinct source formulations and stock additions are conflated
  description: JCM 1085 and DSMZ 482 differ in resazurin amount/form, bicarbonate
    and stock architecture. The generated JCM recipe includes20 direct concentrations,
    including undiluted trace-stock amounts and four added solution volumes mislabeled
    as g/L. The DSMZ-derived owners also flatten SL10. This changes the denoted medium;
    neither a fingerprint nor conditional volume arithmetic supplies a valid combined
    formula.
  target_ids:
  - CultureMech:002265
  field_paths:
  - ingredients
  - solutions
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - jcm
  - jcm-stocks
  - dsmz
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  issue_key: anaerobacter-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate uses an anhydrous identifier
  description: All four layers name NiCl2 x 6 H2O but assert CHEBI:34887, whose captured
    formula is Cl2Ni. The 24 mg source stock amount must retain its hydrate identity
    and stock stage.
  target_ids:
  - CultureMech:002265
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - jcm-stocks
  - dsmz
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  issue_key: anaerobacter-dsmz-resazurin-salt
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: DSMZ-derived sodium resazurin is grounded to unsalted resazurin
  description: The DSMZ and KOMODO owners explicitly name sodium resazurin but use
    CHEBI:8806. JCM’s unqualified Resazurin is a distinct source assertion; its target
    mapping is not shown wrong by the DSMZ salt evidence.
  target_ids:
  - CultureMech:002265
  field_paths:
  - ingredients[6].term
  evidence_ids:
  - owner-1
  - owner-2
  - dsmz
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  issue_key: anaerobacter-preparation-source-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation is incomplete or attached to the wrong source stage
  description: The JCM default 121°C/15 min cycle is absent; KOMODO lacks the DSMZ
    protocol, while the DSMZ owner stores SL10 dissolution/makeup at the medium level.
    These source-specific procedures must accompany reconstructed stocks without transferring
    unrelated JCM 187 instructions.
  target_ids:
  - CultureMech:002265
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - jcm
  - dsmz
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  issue_key: anaerobacter-komodo-provenance-limits
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO catalog metadata and malformed history need explicit qualification
  description: 'The KOMODO owner retains Aerobic: Yes from a table whose primary recipe
    is anaerobic, plus one malformed and one timezone-naive historical timestamp.
    Retain the catalog value only with attribution and preserve old history rather
    than rewriting it.'
  target_ids:
  - CultureMech:002265
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - owner-1
  - komodo-catalog
  - dsmz
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  description: Reconcile the JCM and DSMZ formulations separately in their maintained
    owners, preserving the exact source stock architecture/units and unresolved denominators.
    Retain only source-supported duplicate relationships; regenerate a compatible
    source-specific target after review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  description: Resolve an exact supported nickel hexahydrate identity without guessing
    a CURIE or changing the source mass; correct both current CHEBI slots where asserted.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  description: Resolve the sodium-resazurin form only in the DSMZ-derived owners;
    preserve JCM wording and the separate 1 mg versus 0.5 mg source quantities.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  description: Restore the applicable source cycle, gas handling and stock-specific
    preparation in each maintained source owner, then regenerate. Use broad P2 for
    this combined representation defect; existing sterilization wording is not described
    as entirely absent.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
  description: Append a source-specific clarification of the catalog flag and timestamp
    limitations without fabricating times or modifying prior events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1085_ANAEROBACTER_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacter_medium.yaml
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
- 'mediadiveJ1085api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadive482api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo482: exact public request returned HTTP 403; original access time, response
  bytes and any separately recorded retry are retained. Error bytes do not establish
  formulation or historical absence.'
- 'komodoMediaList: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'komodo482canonical: exact public request returned HTTP 403; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadiveJ1085apiRetry: exact public request returned HTTP 503; original access
  time, response bytes and any separately recorded retry are retained. Error bytes
  do not establish formulation or historical absence.'
- 'mediadive482apiRetry: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- The unavailable exact MediaDive J1085/482 endpoints prevent independent confirmation
  of the historical normalized g/L values; primary collection recipes remain available
  and are the basis of the stage/identity findings.
- No measured final-medium volume, density, or unprinted percentage basis is invented.
  JCM 187 and DSMZ 320 are used only for explicitly referenced stocks.
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
