# Source and formulation review: bacteroides_cellulosolvens_medium (CultureMech:005002)

- Review: 20261021T215704Z-culturemech-005002-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T21:51:53Z
- Finished UTC: 2026-10-21T21:57:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated DSMZ/KOMODO 315 record collapses separate trace and vitamin stocks into direct ingredients and merges an intended cellulose variant whose maintained ingredient remains cellobiose. Correct maintained formulations and preserve their distinct identities before regeneration; retain the primary preparation stages and chemical-form limits.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 388; batch 039 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-eight task batches contain 380 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 383 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005002 | data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml | generated | bacteroides_cellulosolvens_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005002 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005002 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/388/strict.tsv |
| validate-terms | passed | True | CultureMech:005002 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005002 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005002 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive315api | unavailable | False | CultureMech:005002 | The exact optional mediadive315api endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| Exact source content access: mediadive315api_retry | unavailable | False | CultureMech:005002 | The exact optional mediadive315api_retry endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| Exact source content access: komodo315detail | unavailable | False | CultureMech:005002 | The exact optional komodo315detail endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| Exact source content access: komodo315Cellulose | unavailable | False | CultureMech:005002 | The exact optional komodo315Cellulose endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005002.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:005002.

33 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 33/33 primary and 33/33 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:005002.

34 timestamp instances inspected; 6 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source identity and variant boundaries

identity: concern. Targets: CultureMech:005002.

All three exact contributors are accounted for. The DSMZ primary explicitly permits cellobiose OR cellulose at 5 g; the named cellulose owner still contains cellobiose and cannot establish an equivalent cellulose formulation. Existing base SOURCE_DUPLICATE links match local assertions but do not certify them.

### Current primary versus historical derivative reports

evidence: concern. Targets: CultureMech:005002.

No attached ingredient amount evidence exists in any of the four layers. The three historical reports withheld claims because stock topology/variant identity was unresolved. Their source-only objects are derivative context; primary DSMZ text is used for the new quantitative assessment. Original raw API unavailability does not require partial completion for unasserted historical claims.

### Supplied forms and ontology specificity

grounding: concern. Targets: CultureMech:005002.

Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in both link slots. CHEBI:131527 has an anhydrous formula and a trihydrate synonym; the literal K2HPO4 does not justify substituting a hydrate. Primary cysteine-HCl monohydrate lacks an explicit L prefix, so the L-specific mapping remains a specificity limitation rather than proof of another isomer. Explicit D-Ca-pantothenate supports the D form; vitamin B12 remains a generic vitamer class. The other listed hydrate/form correspondences are retained.

### Main and stock procedures

completeness: concern. Targets: CultureMech:005002.

The DSMZ owner retains the main pH, gas and separate cellobiose filtration, but places trace-stock pH steps in the main preparation list. Target and KOMODO owners omit those steps. Preserve the two stocks and their 1000 ml water entries; the listed main liquids sum 1020 ml, not a measured final volume. Do not transfer cellobiose filtration automatically to cellulose or invent a temperature/time cycle.

### Recipe category and conditions

consistency: concern. Targets: CultureMech:005002.

Bacterial/liquid are compatible with the collection identity. COMPLEX/UNDEFINED should be reconsidered only after both alternative formulations and stock chemistry are represented; exact formulas do not establish organism-specific growth. Catalog Aerobic: Yes and the primary N2/CO2 preparation remain distinct conflicting source assertions, not interchangeable growth phenotypes.

### Organism and cultivation claims

evidence: not_applicable. Targets: CultureMech:005002.

The medium name and generic microbial-cultivation application are not strain-specific growth evidence. No taxon, incubation temperature or growth duration is added.

### Maintained ownership and current generator

provenance: concern. Targets: CultureMech:005002.

The maintained owners already contain the shared flattening and the cellulose identity error. Repair those verified owner representations, retain appendix history and resolve source-specific conditions, then regenerate under the current guarded merger. Do not blame the present guarded merger for the older sum or loss of preparation.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:005002.

42 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "topic": "NH4Cl",
    "decision": "evidence_only",
    "local": {
      "value": "0.68",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.68",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.68",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.68",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.68",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'NH4Cl 0.68'; occurrence 1",
        "exact_source_quote": "NH4Cl 0.68 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q2",
    "topic": "K2HPO4",
    "decision": "evidence_only",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'K2HPO4 0.30'; occurrence 1",
        "exact_source_quote": "K2HPO4 0.30 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q3",
    "topic": "KH2PO4",
    "decision": "evidence_only",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'KH2PO4 0.18'; occurrence 1",
        "exact_source_quote": "KH2PO4 0.18 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q4",
    "topic": "(NH4)2SO4",
    "decision": "evidence_only",
    "local": {
      "value": "0.15",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing '(NH4)2SO4 0.15'; occurrence 1",
        "exact_source_quote": "(NH4)2SO4 0.15 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q5",
    "topic": "MgSO4 x 7 H2O",
    "decision": "correct",
    "local": {
      "value": "3.12",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3.12",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3.12",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3.12",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3.12",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'MgSO4 x 7 H2O 0.12'; occurrence 1",
        "exact_source_quote": "MgSO4 x 7 H2O 0.12 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      },
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'MgSO4 x 7 H2O 3.000'; occurrence 1",
        "exact_source_quote": "MgSO4 x 7 H2O 3.000 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q6",
    "topic": "CaCl2 x 2 H2O",
    "decision": "correct",
    "local": {
      "value": "0.16",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'CaCl2 x 2 H2O 0.06'; occurrence 1",
        "exact_source_quote": "CaCl2 x 2 H2O 0.06 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      },
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'CaCl2 x 2 H2O 0.100'; occurrence 1",
        "exact_source_quote": "CaCl2 x 2 H2O 0.100 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q7",
    "topic": "FeSO4 x 7 H2O",
    "decision": "correct",
    "local": {
      "value": "0.12000000000000001",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.12000000000000001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.12000000000000001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.12000000000000001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.12000000000000001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'FeSO4 x 7 H2O 0.02'; occurrence 1",
        "exact_source_quote": "FeSO4 x 7 H2O 0.02 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      },
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'FeSO4 x 7 H2O 0.100'; occurrence 1",
        "exact_source_quote": "FeSO4 x 7 H2O 0.100 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Separate the direct main input from the independent trace-stock batch amount; the stored sum is not a valid direct-medium amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q8",
    "topic": "Cellobiose",
    "decision": "conflict",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose alternative, not an assumed identical recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose alternative, not an assumed identical recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose alternative, not an assumed identical recipe."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose alternative, not an assumed identical recipe."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Cellobiose 5.00'; occurrence 1",
        "exact_source_quote": "Cellobiose 5.00 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose alternative, not an assumed identical recipe."
  },
  {
    "quantity_id": "q9",
    "topic": "Resazurin",
    "decision": "evidence_only",
    "local": {
      "value": "0.001",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Resazurin 1.00'; occurrence 1",
        "exact_source_quote": "Resazurin 1.00 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q10",
    "topic": "NaHCO3",
    "decision": "evidence_only",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'NaHCO3 2.00'; occurrence 1",
        "exact_source_quote": "NaHCO3 2.00 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q11",
    "topic": "L-Cysteine HCl x H2O",
    "decision": "evidence_only",
    "local": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Cysteine-HCl x H2O 0.25'; occurrence 1",
        "exact_source_quote": "Cysteine-HCl x H2O 0.25 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q12",
    "topic": "Na2S x 9 H2O",
    "decision": "evidence_only",
    "local": {
      "value": "0.25",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Na2S x 9 H2O 0.25'; occurrence 1",
        "exact_source_quote": "Na2S x 9 H2O 0.25 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "The numerical mass agrees with the main recipe, but no matching attached evidence exists and G_PER_L requires a declared volume convention. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q13",
    "topic": "Nitrilotriacetic acid",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Nitrilotriacetic acid 1.500'; occurrence 1",
        "exact_source_quote": "Nitrilotriacetic acid 1.500 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q14",
    "topic": "MnSO4 x H2O",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'MnSO4 x H2O 0.500'; occurrence 1",
        "exact_source_quote": "MnSO4 x H2O 0.500 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q15",
    "topic": "NaCl",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'NaCl 1.000'; occurrence 1",
        "exact_source_quote": "NaCl 1.000 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q16",
    "topic": "CoSO4 x 7 H2O",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'CoSO4 x 7 H2O 0.180'; occurrence 1",
        "exact_source_quote": "CoSO4 x 7 H2O 0.180 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q17",
    "topic": "ZnSO4 x 7 H2O",
    "decision": "correct",
    "local": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'ZnSO4 x 7 H2O 0.180'; occurrence 1",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.180 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q18",
    "topic": "CuSO4 x 5 H2O",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'CuSO4 x 5 H2O 0.010'; occurrence 1",
        "exact_source_quote": "CuSO4 x 5 H2O 0.010 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q19",
    "topic": "AlK(SO4)2 x 12 H2O",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'KAl(SO4)2 x 12 H2O 0.020'; occurrence 1",
        "exact_source_quote": "KAl(SO4)2 x 12 H2O 0.020 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q20",
    "topic": "H3BO3",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'H3BO3 0.010'; occurrence 1",
        "exact_source_quote": "H3BO3 0.010 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q21",
    "topic": "Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Na2MoO4 x 2 H2O 0.010'; occurrence 1",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.010 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q22",
    "topic": "NiCl2 x 6 H2O",
    "decision": "correct",
    "local": {
      "value": "0.025",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'NiCl2 x 6 H2O 0.025'; occurrence 1",
        "exact_source_quote": "NiCl2 x 6 H2O 0.025 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q23",
    "topic": "Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local": {
      "value": "0.0003",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300 mg."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300 mg."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300 mg."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300 mg."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Na2SeO3 x 5 H2O 0.300'; occurrence 1",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.300 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300 mg."
  },
  {
    "quantity_id": "q24",
    "topic": "Biotin",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Biotin 2.000'; occurrence 1",
        "exact_source_quote": "Biotin 2.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q25",
    "topic": "Folic acid",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Folic acid 2.000'; occurrence 1",
        "exact_source_quote": "Folic acid 2.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q26",
    "topic": "Pyridoxine hydrochloride",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Pyridoxine-HCl 10.000'; occurrence 1",
        "exact_source_quote": "Pyridoxine-HCl 10.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q27",
    "topic": "Thiamine-HCl x 2 H2O",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Thiamine-HCl x 2 H2O 5.000'; occurrence 1",
        "exact_source_quote": "Thiamine-HCl x 2 H2O 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q28",
    "topic": "Riboflavin",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Riboflavin 5.000'; occurrence 1",
        "exact_source_quote": "Riboflavin 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q29",
    "topic": "Nicotinic acid",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Nicotinic acid 5.000'; occurrence 1",
        "exact_source_quote": "Nicotinic acid 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q30",
    "topic": "D-Calcium pantothenate",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'D-Ca-pantothenate 5.000'; occurrence 1",
        "exact_source_quote": "D-Ca-pantothenate 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q31",
    "topic": "Vitamin B12",
    "decision": "correct",
    "local": {
      "value": "0.0001",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Vitamin B12 0.100'; occurrence 1",
        "exact_source_quote": "Vitamin B12 0.100 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q32",
    "topic": "p-Aminobenzoic acid",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'p-Aminobenzoic acid 5.000'; occurrence 1",
        "exact_source_quote": "p-Aminobenzoic acid 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q33",
    "topic": "Lipoic acid",
    "decision": "correct",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Lipoic acid 5.000'; occurrence 1",
        "exact_source_quote": "Lipoic acid 5.000 mg",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Move the stock batch amount to its own trace or vitamin recipe and represent the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not declare a measured final volume; preserve recipe amounts rather than derive final rates."
  },
  {
    "quantity_id": "q34",
    "topic": "Main water",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Distilled water 1000.00 ml'; occurrence 1",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the exact source stage and its literal volume; this is not a standalone direct solute concentration or proof of measured final volume."
  },
  {
    "quantity_id": "q35",
    "topic": "Trace dose",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Trace element solution (see below) 10.00'; occurrence 1",
        "exact_source_quote": "Trace element solution (see below) 10.00 ml",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the exact source stage and its literal volume; this is not a standalone direct solute concentration or proof of measured final volume."
  },
  {
    "quantity_id": "q36",
    "topic": "Vitamin dose",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Vitamin solution (see below) 10.00'; occurrence 1",
        "exact_source_quote": "Vitamin solution (see below) 10.00 ml",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the exact source stage and its literal volume; this is not a standalone direct solute concentration or proof of measured final volume."
  },
  {
    "quantity_id": "q37",
    "topic": "Trace water",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Distilled water 1000.000'; occurrence 1",
        "exact_source_quote": "Distilled water 1000.000 ml",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the exact source stage and its literal volume; this is not a standalone direct solute concentration or proof of measured final volume."
  },
  {
    "quantity_id": "q38",
    "topic": "Vitamin water",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Distilled water 1000.000'; occurrence 2",
        "exact_source_quote": "Distilled water 1000.000 ml",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the exact source stage and its literal volume; this is not a standalone direct solute concentration or proof of measured final volume."
  },
  {
    "quantity_id": "q39",
    "topic": "Cellulose alternative",
    "decision": "add",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'or Cellulose'; occurrence 1",
        "exact_source_quote": "or Cellulose (i.e. MN 300) 5.00 g",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Represent the explicit alternative and repair the intended cellulose owner after checking its identity; do not add both carbon sources simultaneously.",
    "proposed_source_scoped_value": {
      "amount": "5.00",
      "unit": "g",
      "branch": "cellulose"
    }
  },
  {
    "quantity_id": "q40",
    "topic": "Main pH and gas",
    "decision": "evidence_only",
    "local": 7.0,
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "Existing pH 7.0 agrees; attach scoped primary evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "Existing pH 7.0 agrees; attach scoped primary evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "Existing pH 7.0 agrees; attach scoped primary evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only",
        "rationale": "Existing pH 7.0 agrees; attach scoped primary evidence."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Adjust pH'; occurrence 1",
        "exact_source_quote": "Adjust pH to 7.0. Gas atmosphere: 80% N2 + 20% CO2.",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Keep scalar pH 7.0. Main atmosphere 80% N2 + 20% CO2 has unspecified percentage basis and no supplied pressure; do not infer a growth temperature or aerobic phenotype."
  },
  {
    "quantity_id": "q41",
    "topic": "Main preparation and cellobiose filtration",
    "decision": "add",
    "local": null,
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve existing DSMZ main steps; relocate its trace-stock step and add missing main preparation in the other applicable base layers."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve existing DSMZ main steps; relocate its trace-stock step and add missing main preparation in the other applicable base layers."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.0. Gas atmosphere: 80% N2 + 20% CO2."
          },
          {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": "Filter sterilize cellobiose separately."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Final pH 7.0 (with KOH)."
          }
        ],
        "decision": "correct",
        "rationale": "Preserve existing DSMZ main steps; relocate its trace-stock step and add missing main preparation in the other applicable base layers."
      },
      {
        "input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve existing DSMZ main steps; relocate its trace-stock step and add missing main preparation in the other applicable base layers."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Adjust pH'; occurrence 1",
        "exact_source_quote": "Adjust pH to 7.0. Gas atmosphere: 80% N2 + 20% CO2.",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      },
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'Filter sterilize'; occurrence 1",
        "exact_source_quote": "Filter sterilize cellobiose separately.",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "Main pH/gas and cellobiose-specific filtration must survive regeneration. The cellulose alternative has no separately stated sterilization instruction; leave that limit explicit."
  },
  {
    "quantity_id": "q42",
    "topic": "Trace pH sequence and KOH amount",
    "decision": "not_quantified",
    "local": null,
    "layer_decisions": [],
    "source_snippets": [
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'First dissolve'; occurrence 1",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Final",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      },
      {
        "source_key": "dsmz315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf",
        "source_locator": "Extracted primary text, literal line containing 'pH 7.0 (with KOH).'; occurrence 1",
        "exact_source_quote": "pH 7.0 (with KOH).",
        "snapshot_sha256": "371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d",
        "parsed_text_sha256": "2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2"
      }
    ],
    "rationale": "NTA dissolution precedes KOH adjustment to pH 6.5; add minerals, then adjust the stock to pH 7.0. KOH dose, concentration and physical volume are not supplied; no amount or final denominator is inferred."
  }
]

## Findings

### f1: The cellulose variant still contains cellobiose

blocker / open / confirmed; issue key: culturemech.005002.cellulose-identity.

All four layers share the same cellobiose ingredient despite a distinct cellulose-replacement accession and the primary 5 g cellulose alternative. Generated synonymization currently hides an unresolved formulation identity.

### f2: Trace and vitamin batches are exposed as main-medium quantities

major / open / confirmed; issue key: culturemech.005002.stock-flattening.

Magnesium 3.12, calcium 0.16 and iron 0.12000000000000001 g/L sum main and stock batch masses; the remaining stock-only values are also unscaled. Neither 10 ml stock dose nor its separate solvent stage survives.

### f3: Preparation is missing or attached to the wrong stage

major / open / confirmed; issue key: culturemech.005002.preparation-scope.

The target and KOMODO owners omit the primary steps; the DSMZ owner retains the trace-stock KOH sequence as a main-medium step. Its retained main preparation is not absent.

### f4: Nickel hexahydrate uses an anhydrous identifier

major / open / confirmed; issue key: culturemech.005002.nickel-hydrate.

The primary trace stock names NiCl2 x 6 H2O; CHEBI:34887 describes Cl2Ni. Both local identifier lanes reproduce the supplied-form mismatch.

### f5: Historical import timestamps are malformed or timezone-naive

minor / open / confirmed; issue key: culturemech.005002.history-timestamps.

The target and two KOMODO owners retain .fZ timestamps and timezone-naive enrichment times. Historical source hashes and import notes do not authenticate ingredient quantities.

## Recommended Actions And Acceptance Checks

### a1

Resolve the cellulose owner as its intended alternative, retain source-specific identity, and regenerate only compatible formulations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Reconstruct main recipe amounts and both stock recipes with exact doses, supplied forms and evidence; do not replace the missing measured final-volume basis with an inferred denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve source-specific main pH, gas and cellobiose filtration, attach NTA/KOH steps to the trace stock, and retain unknown KOH amount and cellulose sterilization scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the exact hexahydrate identifier and current secondary correspondence while preserving the 0.025 g stock batch mass; retain other source specificity limitations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Append a dated clarification with recoverable original provenance; do not invent missing timestamp precision or silently rewrite historical events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch039/388/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/388/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml:1:id: CultureMech:005002<br>./data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml:1:id: CultureMech:005002<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch039/source-preflight-bound/388/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 39 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch039/388/grounding-inventory.json; Exact current local objects and bound snapshot joins | context_only | Mechanical inventory preserves per-layer values and source hashes; narrative judgments are separately authored. |
| history-inventory | /private/tmp/culturemech-review-work-batch039/388/history-inventory.json; Exact current local objects and bound snapshot joins | context_only | Mechanical inventory preserves per-layer values and source hashes; narrative judgments are separately authored. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf; Pages 1–2, complete main recipe, trace and vitamin subsections | supports | The primary specifies two alternative 5 g carbon sources, two separate 10 ml stock doses, and distinct main/stock preparation stages. |
| gas | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf; Page 1 main preparation | supports | The gas percentages have no explicit basis; pH is 7.0. No growth temperature/time is supplied. |
| trace-prep | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf; Page 1 trace preparation | supports | KOH adjusts the NTA solution to pH 6.5 before the minerals, then the final stock to pH 7.0; KOH amount is unspecified. |
| catalog-0 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact raw catalog row 1603; seven-column header retained in source audit | supports | Base and cellulose-replacement accessions are distinct identity records. Catalog aerobic flag is source metadata, not a cultivation claim. |
| catalog-1 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact raw catalog row 1606; seven-column header retained in source audit | supports | Base and cellulose-replacement accessions are distinct identity records. Catalog aerobic flag is source metadata, not a cultivation claim. |
| mediadive315api-attempt | https://mediadive.dsmz.de/rest/medium/315; Preserved exact public retrieval result | context_only | The exact optional mediadive315api endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| mediadive315api_retry-attempt | https://mediadive.dsmz.de/rest/medium/315; Preserved exact public retrieval result | context_only | The exact optional mediadive315api_retry endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| komodo315detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315; Preserved exact public retrieval result | context_only | The exact optional komodo315detail endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| komodo315Cellulose-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315_replace_Cellobiose_with_Cellulose; Preserved exact public retrieval result | context_only | The exact optional komodo315Cellulose endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:132751 resolves to thiamine hydrochloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term": "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml; data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:09.982036"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:09.982036"}]}, {"input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.397619"}]}] |
| writer-0 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merger requires exact scientific formulation compatibility; current cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive ingredient extraction restricts composition to the primary solution, while its preparation extraction collects steps from all solutions. These present functions are not proof of the historical execution that produced this stale flattened record. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merger requires exact scientific formulation compatibility; current cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive ingredient extraction restricts composition to the primary solution, while its preparation extraction collects steps from all solutions. These present functions are not proof of the historical execution that produced this stale flattened record. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merger requires exact scientific formulation compatibility; current cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive ingredient extraction restricts composition to the primary solution, while its preparation extraction collects steps from all solutions. These present functions are not proof of the historical execution that produced this stale flattened record. |
| writer-3 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merger requires exact scientific formulation compatibility; current cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive ingredient extraction restricts composition to the primary solution, while its preparation extraction collects steps from all solutions. These present functions are not proof of the historical execution that produced this stale flattened record. |
| report-0 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml.md; Complete report header and scoped claim table; source-only rows remain derivative | context_only | The October 7 review withheld the flattened quantities and variants, leaving the record unchanged. Its reported API hash is a historical reference, not an available authenticated response. No current local layer attaches amount evidence. |
| report-1 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml.md; Complete report header and scoped claim table; source-only rows remain derivative | context_only | The October 7 review withheld the flattened quantities and variants, leaving the record unchanged. Its reported API hash is a historical reference, not an available authenticated response. No current local layer attaches amount evidence. |
| report-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacteroides_cellulosolvens_medium.yaml.md; Complete report header and scoped claim table; source-only rows remain derivative | context_only | The October 7 review withheld the flattened quantities and variants, leaving the record unchanged. Its reported API hash is a historical reference, not an available authenticated response. No current local layer attaches amount evidence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch039/388/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact optional mediadive315api endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request.
- The exact optional mediadive315api_retry endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request.
- The exact optional komodo315detail endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request.
- The exact optional komodo315Cellulose endpoint was unavailable in the preserved attempt. The current primary DSMZ recipe and exact catalog mapping support this bounded review; no historical API payload or detailed variant page is authenticated by the failed request.
- CHEBI:131527 synonym metadata includes a trihydrate wording despite its anhydrous formula; no hydrate replacement or molarity is inferred.
- Current unavailable optional detail/API responses do not authenticate historical derivative payloads. No local amount claim depends on those unavailable bytes.
- This scientific assessment precedes formal review validation and saving; their outcomes are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T215704Z-culturemech-005002-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacteroides_cellulosolvens_medium (CultureMech:005002)'
started_at: '2026-10-21T21:51:53Z'
finished_at: '2026-10-21T21:57:04Z'
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
summary: The generated DSMZ/KOMODO 315 record collapses separate trace and vitamin
  stocks into direct ingredients and merges an intended cellulose variant whose maintained
  ingredient remains cellobiose. Correct maintained formulations and preserve their
  distinct identities before regeneration; retain the primary preparation stages and
  chemical-form limits.
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
  - path: data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    sha256: 550f048d8a57c6e4f457d44150717b2d78db4de381cda2ae062b48636f8b31b4
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    sha256: 2c048fdf9d872d1e5f3dd00f20aa4970c41bb71af61d8083ab7c6d6702c01aef
    role: context
  - path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    sha256: 34aca281911299f824e8e3e8eb9f9ba24b73b810d3680d05c3bc228af16c62da
    role: context
  - path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
    sha256: 24aa54dad7a6c8350442e9927155ff2ef369c0b8c5def3b5f1f817a6b6a89bd5
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml.md
    sha256: 325a08dfeadb1002f267cb7aac67914d9b1158c8315d17805cbad03e5ca9fded
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml.md
    sha256: 3fa84e1cafd28c80728e6897646bdd5577816ed7c39a5c614d130d890c33a9a2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacteroides_cellulosolvens_medium.yaml.md
    sha256: 70fe6339a347b2e8c253afbc40809247f186624a0abcf3e139f0cf68f3c226ef
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  selection: Task review 388; batch 039 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-eight task batches
    contain 380 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 383 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005002
targets:
- target_id: CultureMech:005002
  path: data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  label: bacteroides_cellulosolvens_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/388/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/388/strict.tsv"
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005002
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
  - CultureMech:005002
- check_id: mediadive315api-source-access
  name: 'Exact source content access: mediadive315api'
  required: false
  status: unavailable
  summary: The exact optional mediadive315api endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - mediadive315api-attempt
- check_id: mediadive315api_retry-source-access
  name: 'Exact source content access: mediadive315api_retry'
  required: false
  status: unavailable
  summary: The exact optional mediadive315api_retry endpoint was unavailable in the
    preserved attempt. The current primary DSMZ recipe and exact catalog mapping support
    this bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - mediadive315api_retry-attempt
- check_id: komodo315detail-source-access
  name: 'Exact source content access: komodo315detail'
  required: false
  status: unavailable
  summary: The exact optional komodo315detail endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - komodo315detail-attempt
- check_id: komodo315Cellulose-source-access
  name: 'Exact source content access: komodo315Cellulose'
  required: false
  status: unavailable
  summary: The exact optional komodo315Cellulose endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - komodo315Cellulose-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:35.599413Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/388/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:36.612495Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/388/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:37.742235Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:38.552643Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:57:03Z'
  support: supports
  summary: './data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml:1:id:
    CultureMech:005002

    ./data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml:1:id:
    CultureMech:005002

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/source-preflight-bound/388/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:57:03Z'
  support: supports
  summary: 39 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: cf7d8d5bb044cd5dc9a0f762863afd7935c4b895e87124ca092ade6bf878a817
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/388/grounding-inventory.json
  locator: Exact current local objects and bound snapshot joins
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Mechanical inventory preserves per-layer values and source hashes; narrative
    judgments are separately authored.
  snapshot_sha256: 818a806a32228bb63b10e94b153fe0f845914b0e31da182ae67ca18b5f9561c7
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/388/history-inventory.json
  locator: Exact current local objects and bound snapshot joins
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Mechanical inventory preserves per-layer values and source hashes; narrative
    judgments are separately authored.
  snapshot_sha256: 257200855228b6c11bbcb03d41c9a7671aa2b0a2aaeaeec403c3ec2c1528f28f
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf
  locator: Pages 1–2, complete main recipe, trace and vitamin subsections
  accessed_at: '2026-10-21T21:13:30.409016Z'
  support: supports
  summary: The primary specifies two alternative 5 g carbon sources, two separate
    10 ml stock doses, and distinct main/stock preparation stages.
  quote: or Cellulose (i.e. MN 300) 5.00 g
  snapshot_sha256: 371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d
- evidence_id: gas
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf
  locator: Page 1 main preparation
  accessed_at: '2026-10-21T21:13:30.409016Z'
  support: supports
  summary: The gas percentages have no explicit basis; pH is 7.0. No growth temperature/time
    is supplied.
  quote: 'Adjust pH to 7.0. Gas atmosphere: 80% N2 + 20% CO2.'
  snapshot_sha256: 371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d
- evidence_id: trace-prep
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf
  locator: Page 1 trace preparation
  accessed_at: '2026-10-21T21:13:30.409016Z'
  support: supports
  summary: KOH adjusts the NTA solution to pH 6.5 before the minerals, then the final
    stock to pH 7.0; KOH amount is unspecified.
  quote: pH 7.0 (with KOH).
  snapshot_sha256: 371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d
- evidence_id: catalog-0
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact raw catalog row 1603; seven-column header retained in source audit
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Base and cellulose-replacement accessions are distinct identity records.
    Catalog aerobic flag is source metadata, not a cultivation claim.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315'\
    \ >315</a></TD>\n\t\t\t\t\t<TD>BACTEROIDES CELLULOSOLVENS MEDIUM</TD>\n\t\t\t\t\
    \t<TD> 7.0</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t\
    <TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-1
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact raw catalog row 1606; seven-column header retained in source audit
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Base and cellulose-replacement accessions are distinct identity records.
    Catalog aerobic flag is source metadata, not a cultivation claim.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315_replace_Cellobiose_with_Cellulose'\
    \ >315_replace_Cellobiose_with_Cellulose</a></TD>\n\t\t\t\t\t<TD>BACTEROIDES CELLULOSOLVENS\
    \ MEDIUM_replace_Cellobiose_with_Cellulose</TD>\n\t\t\t\t\t<TD> 7.0</TD>\n\t\t\
    \t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive315api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:13:29.828370Z'
  support: context_only
  summary: The exact optional mediadive315api endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive315api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:14:38.789239Z'
  support: context_only
  summary: The exact optional mediadive315api_retry endpoint was unavailable in the
    preserved attempt. The current primary DSMZ recipe and exact catalog mapping support
    this bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo315detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:13:29.548081Z'
  support: context_only
  summary: The exact optional komodo315detail endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  snapshot_sha256: fcf74e3344f96067b2373829282972be54649eb5acb1a7d87a7c64592d91c9c1
- evidence_id: komodo315Cellulose-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=315_replace_Cellobiose_with_Cellulose
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:13:29.548155Z'
  support: context_only
  summary: The exact optional komodo315Cellulose endpoint was unavailable in the preserved
    attempt. The current primary DSMZ recipe and exact catalog mapping support this
    bounded review; no historical API payload or detailed variant page is authenticated
    by the failed request.
  snapshot_sha256: f9e6fa5cc052fab6a085fbe83baeaf25a57821b54d0fac22227dfddfa2d90bc3
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi132751
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:54.818359Z'
  support: supports
  summary: CHEBI:132751 resolves to thiamine hydrochloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
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
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
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
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
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
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
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
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
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
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
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
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
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
  accessed_at: '2026-10-21T21:57:03Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132751":
    [{"label": "Thiamine-HCl x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:132751", "preferred_term": "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label":
    "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label":
    "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term",
    "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id":
    "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312":
    [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label":
    "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806":
    [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml;
    data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml; data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:09.982036"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:09.982036"}]}, {"input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml",
    "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.397619"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Current merger requires exact scientific formulation compatibility; current
    cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive
    ingredient extraction restricts composition to the primary solution, while its
    preparation extraction collects steps from all solutions. These present functions
    are not proof of the historical execution that produced this stale flattened record.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Current merger requires exact scientific formulation compatibility; current
    cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive
    ingredient extraction restricts composition to the primary solution, while its
    preparation extraction collects steps from all solutions. These present functions
    are not proof of the historical execution that produced this stale flattened record.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Current merger requires exact scientific formulation compatibility; current
    cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive
    ingredient extraction restricts composition to the primary solution, while its
    preparation extraction collects steps from all solutions. These present functions
    are not proof of the historical execution that produced this stale flattened record.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Current merger requires exact scientific formulation compatibility; current
    cleanup refuses to sum disagreeing duplicate concentrations. Current MediaDive
    ingredient extraction restricts composition to the primary solution, while its
    preparation extraction collects steps from all solutions. These present functions
    are not proof of the historical execution that produced this stale flattened record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: report-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml.md
  locator: Complete report header and scoped claim table; source-only rows remain
    derivative
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: The October 7 review withheld the flattened quantities and variants, leaving
    the record unchanged. Its reported API hash is a historical reference, not an
    available authenticated response. No current local layer attaches amount evidence.
  snapshot_sha256: 325a08dfeadb1002f267cb7aac67914d9b1158c8315d17805cbad03e5ca9fded
- evidence_id: report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml.md
  locator: Complete report header and scoped claim table; source-only rows remain
    derivative
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: The October 7 review withheld the flattened quantities and variants, leaving
    the record unchanged. Its reported API hash is a historical reference, not an
    available authenticated response. No current local layer attaches amount evidence.
  snapshot_sha256: 3fa84e1cafd28c80728e6897646bdd5577816ed7c39a5c614d130d890c33a9a2
- evidence_id: report-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacteroides_cellulosolvens_medium.yaml.md
  locator: Complete report header and scoped claim table; source-only rows remain
    derivative
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: The October 7 review withheld the flattened quantities and variants, leaving
    the record unchanged. Its reported API hash is a historical reference, not an
    available authenticated response. No current local layer attaches amount evidence.
  snapshot_sha256: 70fe6339a347b2e8c253afbc40809247f186624a0abcf3e139f0cf68f3c226ef
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/388/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:57:03Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: d3f137ecb09311563d5d3d7725d53468383bd9f407fa6840b7d8a2143727e696
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '33 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 33/33
    primary and 33/33 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi131361
  - chebi131527
  - chebi132751
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17057
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32312
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86364
  - chebi86465
  - chebi8806
  - chebi91244
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 34 timestamp instances inspected; 6 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: identity
  area: identity
  topic: Source identity and variant boundaries
  outcome: concern
  summary: All three exact contributors are accounted for. The DSMZ primary explicitly
    permits cellobiose OR cellulose at 5 g; the named cellulose owner still contains
    cellobiose and cannot establish an equivalent cellulose formulation. Existing
    base SOURCE_DUPLICATE links match local assertions but do not certify them.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - primary
  - catalog-0
  - catalog-1
  - owner-0
  - owner-1
  - owner-2
- assessment_id: evidence-scope
  area: evidence
  topic: Current primary versus historical derivative reports
  outcome: concern
  summary: No attached ingredient amount evidence exists in any of the four layers.
    The three historical reports withheld claims because stock topology/variant identity
    was unresolved. Their source-only objects are derivative context; primary DSMZ
    text is used for the new quantitative assessment. Original raw API unavailability
    does not require partial completion for unasserted historical claims.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - primary
  - history-inventory
  - report-0
  - report-1
  - report-2
- assessment_id: forms
  area: grounding
  topic: Supplied forms and ontology specificity
  outcome: concern
  summary: Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in both link slots.
    CHEBI:131527 has an anhydrous formula and a trihydrate synonym; the literal K2HPO4
    does not justify substituting a hydrate. Primary cysteine-HCl monohydrate lacks
    an explicit L prefix, so the L-specific mapping remains a specificity limitation
    rather than proof of another isomer. Explicit D-Ca-pantothenate supports the D
    form; vitamin B12 remains a generic vitamer class. The other listed hydrate/form
    correspondences are retained.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - primary
  - chebi34887
  - chebi131527
  - chebi91248
  - chebi31345
  - grounding-inventory
- assessment_id: prep
  area: completeness
  topic: Main and stock procedures
  outcome: concern
  summary: The DSMZ owner retains the main pH, gas and separate cellobiose filtration,
    but places trace-stock pH steps in the main preparation list. Target and KOMODO
    owners omit those steps. Preserve the two stocks and their 1000 ml water entries;
    the listed main liquids sum 1020 ml, not a measured final volume. Do not transfer
    cellobiose filtration automatically to cellulose or invent a temperature/time
    cycle.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - primary
  - gas
  - trace-prep
  - owner-1
- assessment_id: classification
  area: consistency
  topic: Recipe category and conditions
  outcome: concern
  summary: 'Bacterial/liquid are compatible with the collection identity. COMPLEX/UNDEFINED
    should be reconsidered only after both alternative formulations and stock chemistry
    are represented; exact formulas do not establish organism-specific growth. Catalog
    Aerobic: Yes and the primary N2/CO2 preparation remain distinct conflicting source
    assertions, not interchangeable growth phenotypes.'
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - primary
  - catalog-0
- assessment_id: biology
  area: evidence
  topic: Organism and cultivation claims
  outcome: not_applicable
  summary: The medium name and generic microbial-cultivation application are not strain-specific
    growth evidence. No taxon, incubation temperature or growth duration is added.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - primary
- assessment_id: writer
  area: provenance
  topic: Maintained ownership and current generator
  outcome: concern
  summary: The maintained owners already contain the shared flattening and the cellulose
    identity error. Repair those verified owner representations, retain appendix history
    and resolve source-specific conditions, then regenerate under the current guarded
    merger. Do not blame the present guarded merger for the older sum or loss of preparation.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - history-inventory
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 42 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:005002
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"topic\": \"NH4Cl\",\n    \"\
    decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"0.68\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.68\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'NH4Cl 0.68';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"NH4Cl 0.68 g\",\n       \
    \ \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"topic\"\
    : \"K2HPO4\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"\
    value\": \"0.3\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'K2HPO4 0.30';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"K2HPO4 0.30 g\",\n      \
    \  \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"topic\"\
    : \"KH2PO4\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"\
    value\": \"0.18\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'KH2PO4 0.18';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"KH2PO4 0.18 g\",\n      \
    \  \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"topic\"\
    : \"(NH4)2SO4\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n   \
    \   \"value\": \"0.15\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.15\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing '(NH4)2SO4\
    \ 0.15'; occurrence 1\",\n        \"exact_source_quote\": \"(NH4)2SO4 0.15 g\"\
    ,\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"topic\"\
    : \"MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local\": {\n     \
    \ \"value\": \"3.12\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3.12\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Separate the direct main input from the independent trace-stock batch amount;\
    \ the stored sum is not a valid direct-medium amount. The primary lists 1000 ml\
    \ water plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.12\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.12\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.12\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'MgSO4 x 7\
    \ H2O 0.12'; occurrence 1\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O\
    \ 0.12 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n    \
    \    \"source_locator\": \"Extracted primary text, literal line containing 'MgSO4\
    \ x 7 H2O 3.000'; occurrence 1\",\n        \"exact_source_quote\": \"MgSO4 x 7\
    \ H2O 3.000 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Separate the direct main input from the\
    \ independent trace-stock batch amount; the stored sum is not a valid direct-medium\
    \ amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare\
    \ a measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"topic\": \"CaCl2 x 2 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.16\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.16\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Separate the direct main input from the independent trace-stock batch amount;\
    \ the stored sum is not a valid direct-medium amount. The primary lists 1000 ml\
    \ water plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate the\
    \ direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'CaCl2 x 2\
    \ H2O 0.06'; occurrence 1\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O\
    \ 0.06 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n    \
    \    \"source_locator\": \"Extracted primary text, literal line containing 'CaCl2\
    \ x 2 H2O 0.100'; occurrence 1\",\n        \"exact_source_quote\": \"CaCl2 x 2\
    \ H2O 0.100 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Separate the direct main input from the\
    \ independent trace-stock batch amount; the stored sum is not a valid direct-medium\
    \ amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare\
    \ a measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"topic\": \"FeSO4 x 7 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.12000000000000001\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n\
    \        \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.12000000000000001\",\n    \
    \      \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n\
    \        \"rationale\": \"Separate the direct main input from the independent\
    \ trace-stock batch amount; the stored sum is not a valid direct-medium amount.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.12000000000000001\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate\
    \ the direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.12000000000000001\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate\
    \ the direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.12000000000000001\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Separate\
    \ the direct main input from the independent trace-stock batch amount; the stored\
    \ sum is not a valid direct-medium amount. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'FeSO4 x 7\
    \ H2O 0.02'; occurrence 1\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O\
    \ 0.02 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n    \
    \    \"source_locator\": \"Extracted primary text, literal line containing 'FeSO4\
    \ x 7 H2O 0.100'; occurrence 1\",\n        \"exact_source_quote\": \"FeSO4 x 7\
    \ H2O 0.100 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Separate the direct main input from the\
    \ independent trace-stock batch amount; the stored sum is not a valid direct-medium\
    \ amount. The primary lists 1000 ml water plus two 10 ml stocks and does not declare\
    \ a measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"topic\": \"Cellobiose\",\n  \
    \  \"decision\": \"conflict\",\n    \"local\": {\n      \"value\": \"5\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\",\n        \"rationale\"\
    : \"The numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates. Retain 5 g cellobiose\
    \ for the base branch; the cellulose owner needs its explicitly intended 5 g cellulose\
    \ alternative, not an assumed identical recipe.\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates. Retain 5 g cellobiose for the\
    \ base branch; the cellulose owner needs its explicitly intended 5 g cellulose\
    \ alternative, not an assumed identical recipe.\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates. Retain 5 g cellobiose for the\
    \ base branch; the cellulose owner needs its explicitly intended 5 g cellulose\
    \ alternative, not an assumed identical recipe.\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\",\n        \"rationale\": \"The numerical mass\
    \ agrees with the main recipe, but no matching attached evidence exists and G_PER_L\
    \ requires a declared volume convention. The primary lists 1000 ml water plus\
    \ two 10 ml stocks and does not declare a measured final volume; preserve recipe\
    \ amounts rather than derive final rates. Retain 5 g cellobiose for the base branch;\
    \ the cellulose owner needs its explicitly intended 5 g cellulose alternative,\
    \ not an assumed identical recipe.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Cellobiose\
    \ 5.00'; occurrence 1\",\n        \"exact_source_quote\": \"Cellobiose 5.00 g\"\
    ,\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates. Retain 5 g cellobiose for the base branch; the cellulose\
    \ owner needs its explicitly intended 5 g cellulose alternative, not an assumed\
    \ identical recipe.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"topic\"\
    : \"Resazurin\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n   \
    \   \"value\": \"0.001\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The\
    \ numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz315\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Resazurin 1.00'; occurrence 1\",\n        \"exact_source_quote\": \"Resazurin\
    \ 1.00 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"topic\"\
    : \"NaHCO3\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"\
    value\": \"2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The numerical mass agrees with the main recipe, but no matching attached evidence\
    \ exists and G_PER_L requires a declared volume convention. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'NaHCO3 2.00';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"NaHCO3 2.00 g\",\n      \
    \  \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"topic\"\
    : \"L-Cysteine HCl x H2O\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"0.25\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.25\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Cysteine-HCl\
    \ x H2O 0.25'; occurrence 1\",\n        \"exact_source_quote\": \"Cysteine-HCl\
    \ x H2O 0.25 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"topic\"\
    : \"Na2S x 9 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n\
    \      \"value\": \"0.25\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.25\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The numerical mass agrees with the main recipe, but no matching\
    \ attached evidence exists and G_PER_L requires a declared volume convention.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The numerical\
    \ mass agrees with the main recipe, but no matching attached evidence exists and\
    \ G_PER_L requires a declared volume convention. The primary lists 1000 ml water\
    \ plus two 10 ml stocks and does not declare a measured final volume; preserve\
    \ recipe amounts rather than derive final rates.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Na2S x 9\
    \ H2O 0.25'; occurrence 1\",\n        \"exact_source_quote\": \"Na2S x 9 H2O 0.25\
    \ g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"The numerical mass agrees with the main\
    \ recipe, but no matching attached evidence exists and G_PER_L requires a declared\
    \ volume convention. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"topic\"\
    : \"Nitrilotriacetic acid\",\n    \"decision\": \"correct\",\n    \"local\": {\n\
    \      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Nitrilotriacetic acid 1.500'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"Nitrilotriacetic acid 1.500 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q14\",\n    \"topic\": \"MnSO4 x H2O\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'MnSO4 x H2O 0.500'; occurrence 1\",\n        \"exact_source_quote\": \"MnSO4\
    \ x H2O 0.500 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q15\",\n    \"topic\": \"NaCl\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n \
    \       \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'NaCl 1.000'; occurrence 1\",\n        \"exact_source_quote\": \"NaCl 1.000\
    \ g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q16\",\n    \"topic\": \"CoSO4 x 7 H2O\",\n    \"decision\":\
    \ \"correct\",\n    \"local\": {\n      \"value\": \"0.18\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[15].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'CoSO4 x 7 H2O 0.180'; occurrence 1\",\n        \"exact_source_quote\": \"CoSO4\
    \ x 7 H2O 0.180 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q17\",\n    \"topic\": \"ZnSO4 x 7 H2O\",\n    \"decision\":\
    \ \"correct\",\n    \"local\": {\n      \"value\": \"0.18\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[16].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'ZnSO4 x 7 H2O 0.180'; occurrence 1\",\n        \"exact_source_quote\": \"ZnSO4\
    \ x 7 H2O 0.180 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q18\",\n    \"topic\": \"CuSO4 x 5 H2O\",\n    \"decision\":\
    \ \"correct\",\n    \"local\": {\n      \"value\": \"0.01\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[17].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'CuSO4 x 5 H2O 0.010'; occurrence 1\",\n        \"exact_source_quote\": \"CuSO4\
    \ x 5 H2O 0.010 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q19\",\n    \"topic\": \"AlK(SO4)2 x 12 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.02\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[18].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'KAl(SO4)2 x 12 H2O 0.020'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"KAl(SO4)2 x 12 H2O 0.020 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q20\",\n    \"topic\": \"H3BO3\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"0.01\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'H3BO3 0.010'; occurrence 1\",\n        \"exact_source_quote\": \"H3BO3 0.010\
    \ g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q21\",\n    \"topic\": \"Na2MoO4 x 2 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.01\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[20].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Na2MoO4 x 2 H2O 0.010'; occurrence 1\",\n        \"exact_source_quote\": \"\
    Na2MoO4 x 2 H2O 0.010 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q22\",\n    \"topic\": \"NiCl2 x 6 H2O\",\n    \"decision\":\
    \ \"correct\",\n    \"local\": {\n      \"value\": \"0.025\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[21].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.025\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'NiCl2 x 6 H2O 0.025'; occurrence 1\",\n        \"exact_source_quote\": \"NiCl2\
    \ x 6 H2O 0.025 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q23\",\n    \"topic\": \"Na2SeO3 x 5 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.0003\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[22].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.0003\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates. The printed amount is 0.300 mg = 0.0003 g in the trace\
    \ batch, not 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003\
    \ mg, not 0.300 mg.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not\
    \ 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300\
    \ mg.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not\
    \ 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300\
    \ mg.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates. The printed amount is 0.300 mg = 0.0003 g in the trace batch, not\
    \ 3 mg. On a nominal 1 L stock basis, a 10 ml dose would carry 0.003 mg, not 0.300\
    \ mg.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Na2SeO3 x 5 H2O 0.300'; occurrence 1\",\n        \"exact_source_quote\": \"\
    Na2SeO3 x 5 H2O 0.300 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates. The printed amount is\
    \ 0.300 mg = 0.0003 g in the trace batch, not 3 mg. On a nominal 1 L stock basis,\
    \ a 10 ml dose would carry 0.003 mg, not 0.300 mg.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q24\",\n    \"topic\": \"Biotin\",\n    \"decision\": \"correct\",\n    \"\
    local\": {\n      \"value\": \"0.002\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock batch\
    \ amount to its own trace or vitamin recipe and represent the separate 10 ml dose.\
    \ The primary lists 1000 ml water plus two 10 ml stocks and does not declare a\
    \ measured final volume; preserve recipe amounts rather than derive final rates.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Biotin 2.000'; occurrence 1\",\n        \"exact_source_quote\": \"Biotin 2.000\
    \ mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q25\",\n    \"topic\": \"Folic acid\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.002\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[24].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Folic acid 2.000'; occurrence 1\",\n        \"exact_source_quote\": \"Folic\
    \ acid 2.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q26\",\n    \"topic\": \"Pyridoxine hydrochloride\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n       \
    \ \"input\": \"target\",\n        \"field_path\": \"ingredients[25].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Pyridoxine-HCl 10.000'; occurrence 1\",\n        \"exact_source_quote\": \"\
    Pyridoxine-HCl 10.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q27\",\n    \"topic\": \"Thiamine-HCl x 2 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[26].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Thiamine-HCl x 2 H2O 5.000'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"Thiamine-HCl x 2 H2O 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q28\",\n    \"topic\": \"Riboflavin\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[27].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Riboflavin 5.000'; occurrence 1\",\n        \"exact_source_quote\": \"Riboflavin\
    \ 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q29\",\n    \"topic\": \"Nicotinic acid\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[28].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Nicotinic acid 5.000'; occurrence 1\",\n        \"exact_source_quote\": \"\
    Nicotinic acid 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q30\",\n    \"topic\": \"D-Calcium pantothenate\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[29].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'D-Ca-pantothenate 5.000'; occurrence 1\",\n        \"exact_source_quote\":\
    \ \"D-Ca-pantothenate 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q31\",\n    \"topic\": \"Vitamin B12\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.0001\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[30].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the\
    \ stock batch amount to its own trace or vitamin recipe and represent the separate\
    \ 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Vitamin B12 0.100'; occurrence 1\",\n        \"exact_source_quote\": \"Vitamin\
    \ B12 0.100 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q32\",\n    \"topic\": \"p-Aminobenzoic acid\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[31].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"Move the stock batch amount to its own trace or vitamin recipe and represent\
    \ the separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks\
    \ and does not declare a measured final volume; preserve recipe amounts rather\
    \ than derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'p-Aminobenzoic acid 5.000'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"p-Aminobenzoic acid 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q33\",\n    \"topic\": \"Lipoic acid\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.005\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[32].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move\
    \ the stock batch amount to its own trace or vitamin recipe and represent the\
    \ separate 10 ml dose. The primary lists 1000 ml water plus two 10 ml stocks and\
    \ does not declare a measured final volume; preserve recipe amounts rather than\
    \ derive final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"Move the stock\
    \ batch amount to its own trace or vitamin recipe and represent the separate 10\
    \ ml dose. The primary lists 1000 ml water plus two 10 ml stocks and does not\
    \ declare a measured final volume; preserve recipe amounts rather than derive\
    \ final rates.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Lipoic acid 5.000'; occurrence 1\",\n        \"exact_source_quote\": \"Lipoic\
    \ acid 5.000 mg\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Move the stock batch amount to its own\
    \ trace or vitamin recipe and represent the separate 10 ml dose. The primary lists\
    \ 1000 ml water plus two 10 ml stocks and does not declare a measured final volume;\
    \ preserve recipe amounts rather than derive final rates.\"\n  },\n  {\n    \"\
    quantity_id\": \"q34\",\n    \"topic\": \"Main water\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"layer_decisions\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Distilled\
    \ water 1000.00 ml'; occurrence 1\",\n        \"exact_source_quote\": \"Distilled\
    \ water 1000.00 ml\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact source stage and its\
    \ literal volume; this is not a standalone direct solute concentration or proof\
    \ of measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"\
    topic\": \"Trace dose\",\n    \"decision\": \"add\",\n    \"local\": null,\n \
    \   \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Trace element solution (see below) 10.00'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"Trace element solution (see below) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\",\n    \
    \    \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact source stage and its\
    \ literal volume; this is not a standalone direct solute concentration or proof\
    \ of measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"\
    topic\": \"Vitamin dose\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Vitamin solution (see below) 10.00'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"Vitamin solution (see below) 10.00 ml\",\n        \"snapshot_sha256\": \"\
    371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\",\n        \"\
    parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact source stage and its\
    \ literal volume; this is not a standalone direct solute concentration or proof\
    \ of measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"\
    topic\": \"Trace water\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Distilled water 1000.000'; occurrence 1\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.000 ml\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact source stage and its\
    \ literal volume; this is not a standalone direct solute concentration or proof\
    \ of measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"\
    topic\": \"Vitamin water\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'Distilled water 1000.000'; occurrence 2\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.000 ml\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the exact source stage and its\
    \ literal volume; this is not a standalone direct solute concentration or proof\
    \ of measured final volume.\"\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"\
    topic\": \"Cellulose alternative\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"layer_decisions\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'or Cellulose'; occurrence 1\",\n        \"exact_source_quote\": \"or Cellulose\
    \ (i.e. MN 300) 5.00 g\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Represent the explicit alternative and\
    \ repair the intended cellulose owner after checking its identity; do not add\
    \ both carbon sources simultaneously.\",\n    \"proposed_source_scoped_value\"\
    : {\n      \"amount\": \"5.00\",\n      \"unit\": \"g\",\n      \"branch\": \"\
    cellulose\"\n    }\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"topic\": \"\
    Main pH and gas\",\n    \"decision\": \"evidence_only\",\n    \"local\": 7.0,\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"Existing pH 7.0 agrees; attach\
    \ scoped primary evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing pH 7.0 agrees;\
    \ attach scoped primary evidence.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\",\n   \
    \     \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"Existing pH 7.0 agrees; attach\
    \ scoped primary evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\",\n        \"rationale\": \"Existing pH 7.0 agrees;\
    \ attach scoped primary evidence.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Adjust pH';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"Adjust pH to 7.0. Gas atmosphere:\
    \ 80% N2 + 20% CO2.\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Keep scalar pH 7.0. Main atmosphere 80%\
    \ N2 + 20% CO2 has unspecified percentage basis and no supplied pressure; do not\
    \ infer a growth temperature or aerobic phenotype.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q41\",\n    \"topic\": \"Main preparation and cellobiose filtration\",\n \
    \   \"decision\": \"add\",\n    \"local\": null,\n    \"layer_decisions\": [\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"Preserve existing DSMZ main steps; relocate its trace-stock step and add missing\
    \ main preparation in the other applicable base layers.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Preserve existing DSMZ\
    \ main steps; relocate its trace-stock step and add missing main preparation in\
    \ the other applicable base layers.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps\",\n        \"stored\": [\n        \
    \  {\n            \"step_number\": 1,\n            \"action\": \"ADJUST_PH\",\n\
    \            \"description\": \"Adjust pH to 7.0. Gas atmosphere: 80% N2 + 20%\
    \ CO2.\"\n          },\n          {\n            \"step_number\": 2,\n       \
    \     \"action\": \"FILTER_STERILIZE\",\n            \"description\": \"Filter\
    \ sterilize cellobiose separately.\"\n          },\n          {\n            \"\
    step_number\": 3,\n            \"action\": \"ADJUST_PH\",\n            \"description\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Final pH 7.0 (with KOH).\"\n          }\n        ],\n        \"decision\"\
    : \"correct\",\n        \"rationale\": \"Preserve existing DSMZ main steps; relocate\
    \ its trace-stock step and add missing main preparation in the other applicable\
    \ base layers.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Preserve existing DSMZ\
    \ main steps; relocate its trace-stock step and add missing main preparation in\
    \ the other applicable base layers.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n        \"\
    source_locator\": \"Extracted primary text, literal line containing 'Adjust pH';\
    \ occurrence 1\",\n        \"exact_source_quote\": \"Adjust pH to 7.0. Gas atmosphere:\
    \ 80% N2 + 20% CO2.\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n    \
    \    \"source_locator\": \"Extracted primary text, literal line containing 'Filter\
    \ sterilize'; occurrence 1\",\n        \"exact_source_quote\": \"Filter sterilize\
    \ cellobiose separately.\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"Main pH/gas and cellobiose-specific filtration\
    \ must survive regeneration. The cellulose alternative has no separately stated\
    \ sterilization instruction; leave that limit explicit.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q42\",\n    \"topic\": \"Trace pH sequence and KOH amount\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local\": null,\n    \"layer_decisions\": [],\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz315\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\"\
    ,\n        \"source_locator\": \"Extracted primary text, literal line containing\
    \ 'First dissolve'; occurrence 1\",\n        \"exact_source_quote\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Final\"\
    ,\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium315.pdf\",\n    \
    \    \"source_locator\": \"Extracted primary text, literal line containing 'pH\
    \ 7.0 (with KOH).'; occurrence 1\",\n        \"exact_source_quote\": \"pH 7.0\
    \ (with KOH).\",\n        \"snapshot_sha256\": \"371312525ed47d009988959be455952c9c23a4a5513864c88e31c6941b317f1d\"\
    ,\n        \"parsed_text_sha256\": \"2b1d498646c9ea4966f8f717b8d6ec5ecffb7da6364c9d1caca4d612bdead5e2\"\
    \n      }\n    ],\n    \"rationale\": \"NTA dissolution precedes KOH adjustment\
    \ to pH 6.5; add minerals, then adjust the stock to pH 7.0. KOH dose, concentration\
    \ and physical volume are not supplied; no amount or final denominator is inferred.\"\
    \n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.005002.cellulose-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The cellulose variant still contains cellobiose
  description: All four layers share the same cellobiose ingredient despite a distinct
    cellulose-replacement accession and the primary 5 g cellulose alternative. Generated
    synonymization currently hides an unresolved formulation identity.
  target_ids:
  - CultureMech:005002
  field_paths:
  - ingredients[7]
  - synonyms
  - merged_from
  evidence_ids:
  - primary
  - catalog-1
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  issue_key: culturemech.005002.stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Trace and vitamin batches are exposed as main-medium quantities
  description: Magnesium 3.12, calcium 0.16 and iron 0.12000000000000001 g/L sum main
    and stock batch masses; the remaining stock-only values are also unscaled. Neither
    10 ml stock dose nor its separate solvent stage survives.
  target_ids:
  - CultureMech:005002
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.005002.preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation is missing or attached to the wrong stage
  description: The target and KOMODO owners omit the primary steps; the DSMZ owner
    retains the trace-stock KOH sequence as a main-medium step. Its retained main
    preparation is not absent.
  target_ids:
  - CultureMech:005002
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - primary
  - gas
  - trace-prep
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  issue_key: culturemech.005002.nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate uses an anhydrous identifier
  description: The primary trace stock names NiCl2 x 6 H2O; CHEBI:34887 describes
    Cl2Ni. Both local identifier lanes reproduce the supplied-form mismatch.
  target_ids:
  - CultureMech:005002
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  issue_key: culturemech.005002.history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical import timestamps are malformed or timezone-naive
  description: The target and two KOMODO owners retain .fZ timestamps and timezone-naive
    enrichment times. Historical source hashes and import notes do not authenticate
    ingredient quantities.
  target_ids:
  - CultureMech:005002
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  description: Resolve the cellulose owner as its intended alternative, retain source-specific
    identity, and regenerate only compatible formulations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005002
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  description: Reconstruct main recipe amounts and both stock recipes with exact doses,
    supplied forms and evidence; do not replace the missing measured final-volume
    basis with an inferred denominator.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005002
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  description: Preserve source-specific main pH, gas and cellobiose filtration, attach
    NTA/KOH steps to the trace stock, and retain unknown KOH amount and cellulose
    sterilization scope.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005002
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  description: Resolve the exact hexahydrate identifier and current secondary correspondence
    while preserving the 0.025 g stock batch mass; retain other source specificity
    limitations.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005002
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
  description: Append a dated clarification with recoverable original provenance;
    do not invent missing timestamp precision or silently rewrite historical events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005002
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml
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
- The exact optional mediadive315api endpoint was unavailable in the preserved attempt.
  The current primary DSMZ recipe and exact catalog mapping support this bounded review;
  no historical API payload or detailed variant page is authenticated by the failed
  request.
- The exact optional mediadive315api_retry endpoint was unavailable in the preserved
  attempt. The current primary DSMZ recipe and exact catalog mapping support this
  bounded review; no historical API payload or detailed variant page is authenticated
  by the failed request.
- The exact optional komodo315detail endpoint was unavailable in the preserved attempt.
  The current primary DSMZ recipe and exact catalog mapping support this bounded review;
  no historical API payload or detailed variant page is authenticated by the failed
  request.
- The exact optional komodo315Cellulose endpoint was unavailable in the preserved
  attempt. The current primary DSMZ recipe and exact catalog mapping support this
  bounded review; no historical API payload or detailed variant page is authenticated
  by the failed request.
- CHEBI:131527 synonym metadata includes a trihydrate wording despite its anhydrous
  formula; no hydrate replacement or molarity is inferred.
- Current unavailable optional detail/API responses do not authenticate historical
  derivative payloads. No local amount claim depends on those unavailable bytes.
- This scientific assessment precedes formal review validation and saving; their outcomes
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-039
- generated-medium
```
