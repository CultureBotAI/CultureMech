# Source and formulation review: BHIS (CultureMech:015493)

- Review: 20261021T235946Z-culturemech-015493-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:44:42Z
- Finished UTC: 2026-10-21T23:59:46Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The eight current FEBA BHIS ingredient rates agree in the target and its sole specialized owner but lack attached concentration evidence. PMID:8573497 authenticates the quoted P43/6/78T growth ranges, not the stored exact 60 min/37 C pair, an anaerobic method or equivalence to this FEBA formula. Taxonomy and paired assemblies support the strain identity. Credit the owner’s September source repair, which the older generated target lacks. Original DNS failure and successful two-snippet recheck are both retained.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 420; batch 042 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-one task batches contain 410 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 413 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015493 | data/merge_yaml/merged/BHIS__8d771a65.yaml | generated | BHIS |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015493 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015493 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/420/strict.tsv |
| validate-terms | passed | True | CultureMech:015493 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | failed | True | CultureMech:015493 | Validating evidence references (MediaRecipe)...<br>  [ERROR] Could not fetch reference: PMID:8573497<br>    Location: variants[0].evidence[0].snippet<br>  [ERROR] Could not fetch reference: PMID:8573497<br>    Location: target_organisms[0].growth_metrics[0].evidence[0].snippet<br>Reference checks: 2; issues: 2<br><br>WARNING:linkml_reference_validator.etl.sources.pmid:Failed to fetch PMID:8573497 from NCBI: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;<br>WARNING:linkml_reference_validator.etl.sources.pmid:Failed to fetch PMID:8573497 from NCBI: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;<br>error: recipe &#96;validate-references&#96; failed with exit code 1 |
| iModulonDB applicability | not_applicable | False | CultureMech:015493 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Reference validation after documented DNS recovery | passed | True | CultureMech:015493 | Validating evidence references (MediaRecipe)...<br>Reference checks: 2; issues: 0<br>✓ Reference validation passed |
| Exact source content access: culturebothtRepository | unavailable | True | CultureMech:015493 | Original CultureBotHT source authentication remains unavailable: exact https://api.github.com/repos/CultureBotAI/CultureBotHT returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |
| Exact source content access: culturebothtExactBHIS | unavailable | True | CultureMech:015493 | Original CultureBotHT source authentication remains unavailable: exact https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |
| Exact source content access: paper8573497DOI | unavailable | True | CultureMech:015493 | Full 1996 article methods needed for exact formula and oxygen protocol remains unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned HTTP 403 at 2026-10-21T23:27:14.556019+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: concern. Targets: CultureMech:015493.

Original schema, strict and term checks passed. Original reference validation attempted two PMID:8573497 snippets and failed twice because DNS retrieval failed; this original failed required check is retained. One separately recorded exact-command network-enabled recheck passed two checks with zero issues. These snippet checks do not establish the exact scalar growth value, oxygen condition, formulation identity or strain/assembly interpretation; those are separately assessed against bound sources.

### Exact maintained owner and excluded BHIS namesake

identity: supported. Targets: CultureMech:015493.

CultureMech:015493, the explicit CultureBotHT import event, source_data and merged_from identify specialized/bhis.yaml. The bacterial/bhis.yaml namesake is CultureMech:009362, TOGO M2814 solid agar, and is excluded. Its product amounts, secondary identifiers and preparation do not transfer. Target and owner agree in ingredients and growth assertions; structured provenance differs.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015493.

44 decisions cover all 16 ingredient concentration fields, all 12 numeric/material-note fields, both layers’ growth scalars, preparation/variant scope and source-only maximum density. All 16 concentration matches are evidence_only. The attached growth sentence is genuine, while its exact endpoint and recipe-scope interpretations need correction.

[
  {
    "decision_id": "q1",
    "name": "Calf brains",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "7.7",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1400 in exact BHIS block",
        "exact_source_quote": "Calf brains\t7.7\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q2",
    "name": "Beef heart",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "9.8",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1401 in exact BHIS block",
        "exact_source_quote": "Beef heart\t9.8\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q3",
    "name": "Proteose Peptone",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1402 in exact BHIS block",
        "exact_source_quote": "Proteose Peptone\t10\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q4",
    "name": "Sodium Chloride",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1403 in exact BHIS block",
        "exact_source_quote": "Sodium Chloride\t5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q5",
    "name": "Disodium phosphate",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1404 in exact BHIS block",
        "exact_source_quote": "Disodium phosphate\t2.5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q6",
    "name": "L-Cysteine",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1405 in exact BHIS block",
        "exact_source_quote": "L-Cysteine\t1\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q7",
    "name": "Sodium bicarbonate",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1406 in exact BHIS block",
        "exact_source_quote": "Sodium bicarbonate\t2\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q8",
    "name": "Hemin",
    "stage": "Named FEBA BHIS direct formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1407 in exact BHIS block",
        "exact_source_quote": "Hemin\t0.005\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q9",
    "name": "Calf brains",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "7.7",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1400 in exact BHIS block",
        "exact_source_quote": "Calf brains\t7.7\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q10",
    "name": "Beef heart",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "9.8",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1401 in exact BHIS block",
        "exact_source_quote": "Beef heart\t9.8\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q11",
    "name": "Proteose Peptone",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1402 in exact BHIS block",
        "exact_source_quote": "Proteose Peptone\t10\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q12",
    "name": "Sodium Chloride",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1403 in exact BHIS block",
        "exact_source_quote": "Sodium Chloride\t5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q13",
    "name": "Disodium phosphate",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1404 in exact BHIS block",
        "exact_source_quote": "Disodium phosphate\t2.5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q14",
    "name": "L-Cysteine",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1405 in exact BHIS block",
        "exact_source_quote": "L-Cysteine\t1\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q15",
    "name": "Sodium bicarbonate",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1406 in exact BHIS block",
        "exact_source_quote": "Sodium bicarbonate\t2\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q16",
    "name": "Hemin",
    "stage": "Named FEBA BHIS direct formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1407 in exact BHIS block",
        "exact_source_quote": "Hemin\t0.005\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Printed amount and g/L basis match, but no matching concentration evidence is attached. Add exact current version/row linkage without changing the amount or claiming the March import or 1996 paper used these exact ingredients."
  },
  {
    "decision_id": "q17",
    "name": "Proteose Peptone material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 91079-38-8"
      }
    ],
    "desired": "CAS: 91079-38-8",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 568",
        "exact_source_quote": "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q18",
    "name": "Proteose Peptone material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 91079-38-8"
      }
    ],
    "desired": "CAS: 91079-38-8",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 568",
        "exact_source_quote": "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q19",
    "name": "Sodium Chloride material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44"
      }
    ],
    "desired": "CAS: 7647-14-5; MW: 58.44",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 375",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q20",
    "name": "Sodium Chloride material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44"
      }
    ],
    "desired": "CAS: 7647-14-5; MW: 58.44",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 375",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q21",
    "name": "Disodium phosphate material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 171",
        "exact_source_quote": "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q22",
    "name": "Disodium phosphate material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 171",
        "exact_source_quote": "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q23",
    "name": "L-Cysteine material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 519",
        "exact_source_quote": "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q24",
    "name": "L-Cysteine material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 519",
        "exact_source_quote": "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q25",
    "name": "Sodium bicarbonate material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 369",
        "exact_source_quote": "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q26",
    "name": "Sodium bicarbonate material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 369",
        "exact_source_quote": "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q27",
    "name": "Hemin material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 520",
        "exact_source_quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q28",
    "name": "Hemin material notes",
    "stage": "Identity metadata, not dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 520",
        "exact_source_quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source supports the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method notes are algorithm provenance, not experimental measurements or upstream authentication."
  },
  {
    "decision_id": "q29",
    "name": "Water, volume and preparation",
    "stage": "FEBA formula completeness",
    "decision": "unsupported",
    "local_fields": [],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Complete media lines 1396–1408",
        "exact_source_quote": "Media\tBHIS\t\nDescription\tBrain heart infusion salt broth\t\nMinimal\tFALSE\t\nControlled vocabulary\tConcentration\tUnits\nCalf brains\t7.7\tg/L\nBeef heart\t9.8\tg/L\nProteose Peptone\t10\tg/L\nSodium Chloride\t5\tg/L\nDisodium phosphate\t2.5\tg/L\nL-Cysteine\t1\tg/L\nSodium bicarbonate\t2\tg/L\nHemin\t0.005\tg/L\n\t\t\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "No water, final batch volume, stock addition, pH, temperature or sterilization cycle is supplied by this FEBA block. Do not default to a measured 1 L batch or infer anaerobic preparation from ingredient names."
  },
  {
    "decision_id": "q30",
    "name": "Doubling time",
    "stage": "P43/6/78T in the paper’s BHIS broth",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].doubling_time_minutes",
        "stored": 60.0
      }
    ],
    "desired": {
      "range_minutes": [
        60,
        120
      ],
      "exact_point": null
    },
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The cited 1–2 h range converts arithmetically to 60–120 min. Stored 60.0 is its lower endpoint, not an authenticated exact doubling-time observation. Preserve the source range in supported text; do not populate invented numeric range slots or substitute an average."
  },
  {
    "decision_id": "q31",
    "name": "Growth temperature",
    "stage": "P43/6/78T paper context",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].temperature_celsius",
        "stored": 37.0
      }
    ],
    "desired": {
      "source_range_degrees_C": [
        37,
        42
      ],
      "exact_point": null
    },
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source gives 37–42 degrees C, not a specific measurement temperature paired with a 60 min doubling time. Remove or qualify the unsupported exact scalar while retaining the literal range."
  },
  {
    "decision_id": "q32",
    "name": "Measurement range and maximum-density text",
    "stage": "Paper-specific growth context",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].measurement_conditions",
        "stored": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C."
      }
    ],
    "desired": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.",
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The range and maximum-density numbers are accurately repeated and have attached matching text. Their assignment to this particular FEBA formula remains unverified; preserve the literal paper observation under explicit unresolved recipe scope."
  },
  {
    "decision_id": "q33",
    "name": "Variant temperature range",
    "stage": "Paper-specific variant text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "variants[0].modifications[1]",
        "stored": "Source reports growth at 37 to 42 degrees C."
      }
    ],
    "desired": "Source reports growth at 37 to 42 degrees C.",
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The literal 37–42 degrees C range matches attached evidence. The exact FEBA-to-paper recipe identity remains unresolved, so this is not unqualified verification of growth on the parent formulation."
  },
  {
    "decision_id": "q34",
    "name": "Anaerobic method",
    "stage": "Asserted incubation instruction",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "variants[0].modifications[0]",
        "stored": "Incubate BHIS broth anaerobically for Brachyspira growth."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Complete accessible AbstractText; full methods unavailable",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "No explicit anaerobic cultivation protocol appears in the full accessible abstract. Consumption of substrate amounts of oxygen is not an anaerobic-method instruction. The failed DOI full text leaves this required protocol check unresolved; do not infer aerobic conditions either."
  },
  {
    "decision_id": "q35",
    "name": "Maximum-attainment classification",
    "stage": "Growth-metric interpretation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].is_max_attainment",
        "stored": false
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The optional false value asserts a conditional/non-default growth context under the schema, but no corresponding perturbation or nutrient override is established by this sentence. Its maximum cell density does not imply that a doubling-time metric should be marked true. Retain unknown rather than infer either Boolean."
  },
  {
    "decision_id": "q36",
    "name": "Paper BHIS versus FEBA BHIS",
    "stage": "Variant-to-parent formula correspondence",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "variants[0].description",
        "stored": "BHIS broth condition supporting growth of the Brachyspira pilosicoli type strain P43/6/78T."
      },
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "variants[0].purpose",
        "stored": "Capture strain-specific BHIS growth evidence under the parent BHIS broth record."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Complete FEBA BHIS lines 1396–1408",
        "exact_source_quote": "Media\tBHIS\t\nDescription\tBrain heart infusion salt broth\t\nMinimal\tFALSE\t\nControlled vocabulary\tConcentration\tUnits\nCalf brains\t7.7\tg/L\nBeef heart\t9.8\tg/L\nProteose Peptone\t10\tg/L\nSodium Chloride\t5\tg/L\nDisodium phosphate\t2.5\tg/L\nL-Cysteine\t1\tg/L\nSodium bicarbonate\t2\tg/L\nHemin\t0.005\tg/L\n\t\t\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The matching medium abbreviation supports a research lead, not compositional equality. The abstract does not enumerate the paper’s BHIS formula; keep the growth claim and organism identity qualified until a complete methods formulation can be matched."
  },
  {
    "decision_id": "q37",
    "name": "Doubling time",
    "stage": "P43/6/78T in the paper’s BHIS broth",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].doubling_time_minutes",
        "stored": 60.0
      }
    ],
    "desired": {
      "range_minutes": [
        60,
        120
      ],
      "exact_point": null
    },
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The cited 1–2 h range converts arithmetically to 60–120 min. Stored 60.0 is its lower endpoint, not an authenticated exact doubling-time observation. Preserve the source range in supported text; do not populate invented numeric range slots or substitute an average."
  },
  {
    "decision_id": "q38",
    "name": "Growth temperature",
    "stage": "P43/6/78T paper context",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].temperature_celsius",
        "stored": 37.0
      }
    ],
    "desired": {
      "source_range_degrees_C": [
        37,
        42
      ],
      "exact_point": null
    },
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The source gives 37–42 degrees C, not a specific measurement temperature paired with a 60 min doubling time. Remove or qualify the unsupported exact scalar while retaining the literal range."
  },
  {
    "decision_id": "q39",
    "name": "Measurement range and maximum-density text",
    "stage": "Paper-specific growth context",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].measurement_conditions",
        "stored": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C."
      }
    ],
    "desired": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.",
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The range and maximum-density numbers are accurately repeated and have attached matching text. Their assignment to this particular FEBA formula remains unverified; preserve the literal paper observation under explicit unresolved recipe scope."
  },
  {
    "decision_id": "q40",
    "name": "Variant temperature range",
    "stage": "Paper-specific variant text",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "variants[0].modifications[1]",
        "stored": "Source reports growth at 37 to 42 degrees C."
      }
    ],
    "desired": "Source reports growth at 37 to 42 degrees C.",
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The literal 37–42 degrees C range matches attached evidence. The exact FEBA-to-paper recipe identity remains unresolved, so this is not unqualified verification of growth on the parent formulation."
  },
  {
    "decision_id": "q41",
    "name": "Anaerobic method",
    "stage": "Asserted incubation instruction",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "variants[0].modifications[0]",
        "stored": "Incubate BHIS broth anaerobically for Brachyspira growth."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Complete accessible AbstractText; full methods unavailable",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "No explicit anaerobic cultivation protocol appears in the full accessible abstract. Consumption of substrate amounts of oxygen is not an anaerobic-method instruction. The failed DOI full text leaves this required protocol check unresolved; do not infer aerobic conditions either."
  },
  {
    "decision_id": "q42",
    "name": "Maximum-attainment classification",
    "stage": "Growth-metric interpretation",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].is_max_attainment",
        "stored": false
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The optional false value asserts a conditional/non-default growth context under the schema, but no corresponding perturbation or nutrient override is established by this sentence. Its maximum cell density does not imply that a doubling-time metric should be marked true. Retain unknown rather than infer either Boolean."
  },
  {
    "decision_id": "q43",
    "name": "Paper BHIS versus FEBA BHIS",
    "stage": "Variant-to-parent formula correspondence",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "variants[0].description",
        "stored": "BHIS broth condition supporting growth of the Brachyspira pilosicoli type strain P43/6/78T."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "variants[0].purpose",
        "stored": "Capture strain-specific BHIS growth evidence under the parent BHIS broth record."
      }
    ],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Article/Abstract/AbstractText, exact BHIS growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Complete FEBA BHIS lines 1396–1408",
        "exact_source_quote": "Media\tBHIS\t\nDescription\tBrain heart infusion salt broth\t\nMinimal\tFALSE\t\nControlled vocabulary\tConcentration\tUnits\nCalf brains\t7.7\tg/L\nBeef heart\t9.8\tg/L\nProteose Peptone\t10\tg/L\nSodium Chloride\t5\tg/L\nDisodium phosphate\t2.5\tg/L\nL-Cysteine\t1\tg/L\nSodium bicarbonate\t2\tg/L\nHemin\t0.005\tg/L\n\t\t\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "The matching medium abbreviation supports a research lead, not compositional equality. The abstract does not enumerate the paper’s BHIS formula; keep the growth claim and organism identity qualified until a complete methods formulation can be matched."
  },
  {
    "decision_id": "q44",
    "name": "Maximum cell density",
    "stage": "Paper-only observation already retained in free text",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS__8d771a65.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].measurement_conditions",
        "stored": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis.yaml",
        "field_path": "target_organisms[0].growth_metrics[0].measurement_conditions",
        "stored": "BHIS broth; source reports 1 to 2 h doubling time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C."
      }
    ],
    "desired": {
      "maximum_cells_per_ml": 2000000000
    },
    "source_snippets": [
      {
        "source_key": "pubmed8573497",
        "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml",
        "source_locator": "Exact growth sentence",
        "exact_source_quote": "In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.",
        "snapshot_sha256": "71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3",
        "quote_representation": "Exact source text with line endings normalized to LF; tabs retained."
      }
    ],
    "interpretation": "Verified only as narrow source-text correspondence: the authentic cited maximum-density text agrees with the existing measurement_conditions in both layers. The source reports maximum 2 x 10(9) cells per ml for its BHIS condition. This does not verify FEBA formulation equivalence or an exact paired scalar observation. It is cell count density, not OD600; no optical-density conversion is made."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:015493.

5 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 5/8 primary and 0/8 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 8: primary 62.50%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact supplied forms and optional ingredient linkages

grounding: supported. Targets: CultureMech:015493.

Five primary chemical IDs agree with their canonical labels and source name/CAS: sodium chloride, disodium hydrogenphosphate, L-cysteine, sodium hydrogencarbonate and hemin. The three complex materials remain unmapped. Neither actual target nor maintained owner asserts a secondary or legacy MediaIngredientMech link; identifiers in excluded bacterial/bhis.yaml do not transfer.

### Claim-level growth support and method/formula boundaries

evidence: concern. Targets: CultureMech:015493.

All four attached evidence instances exactly match the current primary abstract. They support P43/6/78T growth in the paper’s BHIS, range 1–2 h, temperature range 37–42 degrees C and maximum density 2 x 10(9) cells/ml. Exact scalar 60 min/37 C, anaerobic instruction, conditional Boolean and equivalence to FEBA BHIS are not thereby established. The primary’s broader substrate and taxonomic observations are excluded from the recipe.

### Strain, taxon and paired genome identities

identity: supported. Targets: CultureMech:015493.

NCBITaxon:1042417 is the strain Brachyspira pilosicoli P43/6/78 with synonym ATCC 51139. Reciprocal current GCA_000325665.1 and GCF_000325665.1 identify that strain and CP002873. PMID:23469345/PMC3587939 supports its complete genome, not this medium formula. These identities remain valid despite unresolved growth-condition interpretation.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015493.

8 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Completed maintained-owner repair and stale generated metadata

provenance: concern. Targets: CultureMech:015493.

The specialized owner already contains structured CultureBotHT sources, two references and the 2026-09-13 repair event. The August generated target lacks them. Credit this completed owner repair and reconcile the projection after any scientific corrections; do not propose repeating it or blame the current guarded merger for historical losses. Neither layer has a dedicated event recording addition of the two Brachyspira evidence blocks; append a truthful current verification/qualification event without inventing its historical date.

### Prior derivative reports and import chronology

provenance: supported. Targets: CultureMech:015493.

The three exact target/owner reports were read. Their concentration triage was not a source check. The broad corpus growth report is retained as a search lead only and was not fully reread or treated as primary evidence. Four attached quote instances have current raw support without a claimed historical response digest. FEBA’s September revision postdates the March import.

### Unknown formulation protocol and missing quantitative representation

completeness: unknown. Targets: CultureMech:015493.

The accessible FEBA formula has no water, volume, stocks or protocol. GrowthMetrics supplies scalar fields but no numeric doubling-time or temperature range slots; retain exact ranges in measurement_conditions and omit unsupported point estimates. Do not map cell density to OD600. Missing full methods and original CultureBotHT bytes make required scientific source coverage partial.

## Findings

### f1: Source growth ranges are stored as exact lower endpoints

major / open / confirmed; issue key: culturemech.015493.growth-range-collapse.

Both layers retain a genuine 1–2 h and 37–42 degrees C excerpt but store 60.0 minutes and 37.0 degrees C as exact measurement fields. Arithmetic establishes 60–120 minutes, not an observed 60 minute doubling time paired with 37 degrees C.

### f2: Paper growth is asserted for an unreconciled formula and protocol

major / open / confirmed; issue key: culturemech.015493.unverified-paper-formula-scope.

The growth variant and target organism are attached to this FEBA BHIS formula, but the accessible 1996 source names BHIS without its composition or an anaerobic method. The current genome article closes neither gap. The optional is_max_attainment false also lacks a demonstrated perturbation/non-default context; maximum density is a separate observation and does not justify either Boolean.

### f3: Current supported ingredient rates lack attached evidence

minor / open / confirmed; issue key: culturemech.015493.amount-evidence.

All eight direct FEBA rates agree numerically in both layers, but none has claim-level concentration evidence. Generic source identifiers and a provenance repair do not supply the exact version/row/material basis.

### f4: Generated target omits completed owner source repair

minor / open / confirmed; issue key: culturemech.015493.stale-generated-provenance.

The maintained owner already has structured sources, two references and the September provenance repair event. The older target lacks this information. The repair did not change or validate growth values.

### f5: Growth-evidence addition lacks a dedicated audit event

minor / open / confirmed; issue key: culturemech.015493.growth-curation-event-gap.

Both layers contain Brachyspira variant and growth evidence, but their complete histories record import, ID assignment, organism culture classification and either merge or provenance repair, without an event documenting the evidence addition or its interpretation. No historical creation time is inferred.

## Recommended Actions And Acceptance Checks

### a1

In the maintained owner, remove or explicitly qualify unsupported exact scalars and preserve the original ranges in supported text. Use numeric ranges only after a separately authorized schema change; do not insert an average or claim a paired endpoint.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the supported strain and paper observation, but qualify its relationship to the FEBA formula until the original full recipe and cultivation method are verified. Remove unsupported anaerobic/conditional assertions or attach exact method evidence. Do not infer the opposite oxygen condition or a true maximum-attainment flag.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact current FEBA concentration evidence to the maintained owner, retaining original units and later source date. Do not claim the current revision authenticates the original import or the 1996 BHIS recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the completed owner repair and regenerate its corrected projection after scientific follow-up. Confirm sources, references, histories and scoped evidence survive; do not repeat the owner repair or rewrite past dates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

When qualifying the existing evidence, append an accurately dated verification/curation event naming the supported ranges and unresolved recipe/protocol limits. Preserve earlier events and do not fabricate an original evidence-insertion date.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHIS__8d771a65.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/bhis.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHIS__8d771a65.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHIS__8d771a65.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch042/420/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/420/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHIS__8d771a65.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml; Actual command output | refutes | Validating evidence references (MediaRecipe)...<br>  [ERROR] Could not fetch reference: PMID:8573497<br>    Location: variants[0].evidence[0].snippet<br>  [ERROR] Could not fetch reference: PMID:8573497<br>    Location: target_organisms[0].growth_metrics[0].evidence[0].snippet<br>Reference checks: 2; issues: 2<br><br>WARNING:linkml_reference_validator.etl.sources.pmid:Failed to fetch PMID:8573497 from NCBI: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;<br>WARNING:linkml_reference_validator.etl.sources.pmid:Failed to fetch PMID:8573497 from NCBI: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;<br>error: recipe &#96;validate-references&#96; failed with exit code 1 |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/bhis.yaml:1:id: CultureMech:015493<br>./data/merge_yaml/merged/BHIS__8d771a65.yaml:1:id: CultureMech:015493<br> |
| validate-references-network-recheck | just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml; Separate exact-command network-enabled recheck; original failure retained | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 2; issues: 0<br>✓ Reference validation passed<br><br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch042/source-preflight-bound/420/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 21 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| feba-main | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Exact BHIS accession block, media lines 1396–1408 | supports | Complete current eight-ingredient formula. Printed g/L rates do not establish a batch volume, product decomposition, paper recipe or preparation protocol. |
| feba-version | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b; Exact commit hash/date | supports | Revision 803273865ea9e83fab770ec4f13670db80e1180b dates to 2026-09-10, later than the March 2026 CultureBotHT import. Current row agreement is not authenticated import-time equivalence. |
| culturebothtRepository-attempt | https://api.github.com/repos/CultureBotAI/CultureBotHT; Preserved exact public retrieval result | context_only | Original CultureBotHT source authentication remains unavailable: exact https://api.github.com/repos/CultureBotAI/CultureBotHT returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |
| culturebothtExactBHIS-attempt | https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml; Preserved exact public retrieval result | context_only | Original CultureBotHT source authentication remains unavailable: exact https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |
| paper8573497DOI-attempt | https://doi.org/10.1099/00207713-46-1-206; Preserved exact public retrieval result | context_only | Full 1996 article methods needed for exact formula and oxygen protocol remains unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned HTTP 403 at 2026-10-21T23:27:14.556019+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed. |
| excluded-owner | data/normalized_yaml/bacterial/bhis.yaml; Full distinct namesake read; exact ID/source/import-event comparison | context_only | Explicit non-owner boundary only: no scientific or quantity transfer from TOGO M2814. |
| compound-0 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 569 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-1 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 570 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-2 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 568 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-3 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 375 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-4 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 171 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-5 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 519 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-6 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 369 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| compound-7 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 520 | supports | Exact supplied-material metadata; CAS/FW are not a medium dose or measured growth result. |
| growth-abstract | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml; PMID 8573497 Article/Abstract/AbstractText, exact BHIS growth sentence | supports | Current primary abstract directly supports the strain-specific ranges and maximum density. It does not establish a paired exact lower endpoint, the eight-row FEBA formulation, or an anaerobic protocol. |
| growth-full-abstract | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=8573497&amp;retmode=xml; Complete PMID 8573497 abstract | supports | Full accessible primary abstract read. Oxygen consumption, substrate-utilization and taxonomic comparisons are not a recipe or an anaerobic incubation instruction. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch042/420/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| forms | /private/tmp/culturemech-review-work-batch042/420/chemical-form-inventory.json; Eight source-material comparisons and five full OLS scientific projections | context_only | Separate source form assessment; unmapped complex materials are retained honestly. |
| chebi17561 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17561 resolves to L-cysteine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50385 resolves to hemin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}} |
| attached-claims | /private/tmp/culturemech-review-work-batch042/420/historical-evidence-inventory.json; All four evidence-object instances: two per local layer | supports | Exact current raw-substring matches, original explanations and unsupported interpretation limits. No historical raw identity is invented. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1042417&amp;retmode=xml; TaxaSet/Taxon with TaxId 1042417; full current object and lineage | supports | Canonical strain label, rank and ATCC 51139 synonym support the asserted organism identity. Historical Serpulina naming in the 1996 paper is distinguished from the current Brachyspira label. |
| assemblyGCA0003256651 | https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000325665.1/dataset_report; $.reports[0], full organism/assembly/BioSample and ANI qualification | supports | Reciprocal current complete-genome accession identifies the same P43/6/78 / ATCC 51139 strain. The below_threshold_mismatch field is accompanied by taxonomy_check_status OK and a type-strain no-match-expected comment; it is not evidence of a taxon conflict. |
| assemblyGCF0003256651 | https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000325665.1/dataset_report; $.reports[0], full organism/assembly/BioSample and ANI qualification | supports | Reciprocal current complete-genome accession identifies the same P43/6/78 / ATCC 51139 strain. The below_threshold_mismatch field is accompanied by taxonomy_check_status OK and a type-strain no-match-expected comment; it is not evidence of a taxon conflict. |
| genome-paper | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=23469345&amp;retmode=xml; Full PubMed23469345 citation/abstract and linked PMC3587939 | supports | Complete genome identity statement for the same P43/6/78T strain, distinct from growth formulation evidence. |
| genome-fulltext | https://pmc.ncbi.nlm.nih.gov/articles/PMC3587939/; Complete article element, including GENOME ANNOUNCEMENT and Nucleotide sequence accession number | supports | Full article reports complete genome CP002873 and sequencing/identity context. It provides no BHIS formula or cultivation protocol, so it does not close the 1996 methods gap. |
| history-metadata | data/merge_yaml/merged/BHIS__8d771a65.yaml; data/normalized_yaml/specialized/bhis.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis.yaml", "events": 4, "timestamp_issues": []}] |
| writer-0 | scripts/import_from_culturebotht.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-1 | scripts/migrate_legacy_fields.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-4 | scripts/propose_growth_evidence.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-5 | scripts/curate_organism_culture_type.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| writer-6 | scripts/repair_culturebotht_bhis_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current import/migration, range-extraction proposal, organism classification, provenance repair and formulation-preserving merge code was read. Current functions do not authenticate historical execution. The September repair only restores structured sources/references/history and does not authenticate amounts, oxygen conditions or growth scalars. |
| prior-report-0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis.md; Complete exact-identity prior report | context_only | Earlier local derivative report read in full. It records source limits, range and provenance concerns; current sources and local bytes establish this review’s findings independently. |
| prior-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS__8d771a65.md; Complete exact-identity prior report | context_only | Earlier local derivative report read in full. It records source limits, range and provenance concerns; current sources and local bytes establish this review’s findings independently. |
| prior-report-2 | reports/yaml_record_review/20260921T212501Z-BHIS__8d771a65.md; Complete exact-identity prior report | context_only | Earlier local derivative report read in full. It records source limits, range and provenance concerns; current sources and local bytes establish this review’s findings independently. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The original reference check failed on two DNS fetch errors; the separate exact-command recheck passed two snippet checks. Both attempts and actual timestamps are retained. This recovery is not evidence that every scientific interpretation of those snippets is correct.
- Original CultureBotHT source authentication remains unavailable: exact https://api.github.com/repos/CultureBotAI/CultureBotHT returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed.
- Original CultureBotHT source authentication remains unavailable: exact https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed.
- Full 1996 article methods needed for exact formula and oxygen protocol remains unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned HTTP 403 at 2026-10-21T23:27:14.556019+00:00. Preserved response is not usable recipe/method content; no absence from the wider literature is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T235946Z-culturemech-015493-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: BHIS (CultureMech:015493)'
started_at: '2026-10-21T23:44:42Z'
finished_at: '2026-10-21T23:59:46Z'
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
summary: The eight current FEBA BHIS ingredient rates agree in the target and its
  sole specialized owner but lack attached concentration evidence. PMID:8573497 authenticates
  the quoted P43/6/78T growth ranges, not the stored exact 60 min/37 C pair, an anaerobic
  method or equivalence to this FEBA formula. Taxonomy and paired assemblies support
  the strain identity. Credit the owner’s September source repair, which the older
  generated target lacks. Original DNS failure and successful two-snippet recheck
  are both retained.
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
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 2bd19d90afa3d37315c69a45cccad8b4a8e30b6bca8e992a45d7ea0c9cadfb84
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
  - path: data/merge_yaml/merged/BHIS__8d771a65.yaml
    sha256: 8beb1c54982b78c1f4757f5450dc6e033fde967017b74ef7ef1c244f2e618abe
    role: target
  - path: data/normalized_yaml/bacterial/bhis.yaml
    sha256: 0acacc8bfd30711e2df753d5485e08cbfb7b85a060760b00f315a70f6d73bda3
    role: context
  - path: data/normalized_yaml/specialized/bhis.yaml
    sha256: 99440736e3f52ced80b9d46e474b71c74111e8a6f6a272b75b13a8842788ed6f
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS__8d771a65.md
    sha256: dbce0b4695b5bae2378b5b28909c0c64ae5756a7926d7664080bc22705766d29
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis.md
    sha256: 166fc42dd691bc17e677c30b21aae60ebb9244102122550dfc1a9bb3962adfee
    role: context
  - path: reports/media_growth_review_corpus_scope.md
    sha256: ca4ff4c194d04b4f165e59c03d60ad18ef9a85e4afc0de2e9544a1ce6b83f2d1
    role: context
  - path: reports/yaml_record_review/20260921T212501Z-BHIS__8d771a65.md
    sha256: b8bc7ce1eb079bf9cb5ee2a91051435432b3694726e79ef301e80e5d7c5a6763
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curate_organism_culture_type.py
    sha256: 8686de3d3736eaaf3702e2009a299a53819a5ba321966ab2ea01104538ca6a65
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/propose_growth_evidence.py
    sha256: 2d5a5b388c2e63bf1cc395645af1972800618bbe5ec1caef3d7aa60fd7a2d0db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_culturebotht_bhis_score15.py
    sha256: a600d3cf5286268fc003f713557588bab018e95fdac24bbbcdcea558753677e6
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
  selection: Task review 420; batch 042 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-one task batches
    contain 410 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 413 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015493
targets:
- target_id: CultureMech:015493
  path: data/merge_yaml/merged/BHIS__8d771a65.yaml
  label: BHIS
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHIS__8d771a65.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHIS__8d771a65.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch042/420/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/420/strict.tsv"
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHIS__8d771a65.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml
  exit_code: 1
  required: true
  status: failed
  summary: "Validating evidence references (MediaRecipe)...\n  [ERROR] Could not fetch\
    \ reference: PMID:8573497\n    Location: variants[0].evidence[0].snippet\n  [ERROR]\
    \ Could not fetch reference: PMID:8573497\n    Location: target_organisms[0].growth_metrics[0].evidence[0].snippet\n\
    Reference checks: 2; issues: 2\n\nWARNING:linkml_reference_validator.etl.sources.pmid:Failed\
    \ to fetch PMID:8573497 from NCBI: <urlopen error [Errno 8] nodename nor servname\
    \ provided, or not known>\nWARNING:linkml_reference_validator.etl.sources.pmid:Failed\
    \ to fetch PMID:8573497 from NCBI: <urlopen error [Errno 8] nodename nor servname\
    \ provided, or not known>\nerror: recipe `validate-references` failed with exit\
    \ code 1"
  target_ids:
  - CultureMech:015493
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
  - CultureMech:015493
- check_id: validate-references-network-recheck
  name: Reference validation after documented DNS recovery
  command: just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 2; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - validate-references-network-recheck
- check_id: culturebothtRepository-source-access
  name: 'Exact source content access: culturebothtRepository'
  required: true
  status: unavailable
  summary: 'Original CultureBotHT source authentication remains unavailable: exact
    https://api.github.com/repos/CultureBotAI/CultureBotHT returned HTTP 404 at 2026-10-21T22:53:13.557900Z.
    Preserved response is not usable recipe/method content; no absence from the wider
    literature is claimed.'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - culturebothtRepository-attempt
- check_id: culturebothtExactBHIS-source-access
  name: 'Exact source content access: culturebothtExactBHIS'
  required: true
  status: unavailable
  summary: 'Original CultureBotHT source authentication remains unavailable: exact
    https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml
    returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not
    usable recipe/method content; no absence from the wider literature is claimed.'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - culturebothtExactBHIS-attempt
- check_id: paper8573497DOI-source-access
  name: 'Exact source content access: paper8573497DOI'
  required: true
  status: unavailable
  summary: 'Full 1996 article methods needed for exact formula and oxygen protocol
    remains unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned
    HTTP 403 at 2026-10-21T23:27:14.556019+00:00. Preserved response is not usable
    recipe/method content; no absence from the wider literature is claimed.'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - paper8573497DOI-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHIS__8d771a65.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/bhis.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHIS__8d771a65.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:26.628248Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHIS__8d771a65.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch042/420/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:27.585684Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/420/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHIS__8d771a65.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:28.724829Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:46:30.477307Z'
  support: refutes
  summary: "Validating evidence references (MediaRecipe)...\n  [ERROR] Could not fetch\
    \ reference: PMID:8573497\n    Location: variants[0].evidence[0].snippet\n  [ERROR]\
    \ Could not fetch reference: PMID:8573497\n    Location: target_organisms[0].growth_metrics[0].evidence[0].snippet\n\
    Reference checks: 2; issues: 2\n\nWARNING:linkml_reference_validator.etl.sources.pmid:Failed\
    \ to fetch PMID:8573497 from NCBI: <urlopen error [Errno 8] nodename nor servname\
    \ provided, or not known>\nWARNING:linkml_reference_validator.etl.sources.pmid:Failed\
    \ to fetch PMID:8573497 from NCBI: <urlopen error [Errno 8] nodename nor servname\
    \ provided, or not known>\nerror: recipe `validate-references` failed with exit\
    \ code 1"
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:53:28Z'
  support: supports
  summary: './data/normalized_yaml/specialized/bhis.yaml:1:id: CultureMech:015493

    ./data/merge_yaml/merged/BHIS__8d771a65.yaml:1:id: CultureMech:015493

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: validate-references-network-recheck
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHIS__8d771a65.yaml
  locator: Separate exact-command network-enabled recheck; original failure retained
  accessed_at: '2026-10-21T23:47:04.346041Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 2; issues: 0

    ✓ Reference validation passed


    '
  snapshot_sha256: 3066c82e552bd70949bf041b0e6192aca14f7dc850c24dc435a371a1bb89e895
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/source-preflight-bound/420/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:53:28Z'
  support: supports
  summary: 21 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: dafb93743ffd9fad23d678a28d7194897bb451c3c08d88444a9119c3d55aba6c
- evidence_id: feba-main
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Exact BHIS accession block, media lines 1396–1408
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: Complete current eight-ingredient formula. Printed g/L rates do not establish
    a batch volume, product decomposition, paper recipe or preparation protocol.
  quote: "Media\tBHIS\t\r\nDescription\tBrain heart infusion salt broth\t\r\nMinimal\t\
    FALSE\t\r\nControlled vocabulary\tConcentration\tUnits\r\nCalf brains\t7.7\tg/L\r\
    \nBeef heart\t9.8\tg/L\r\nProteose Peptone\t10\tg/L\r\nSodium Chloride\t5\tg/L\r\
    \nDisodium phosphate\t2.5\tg/L\r\nL-Cysteine\t1\tg/L\r\nSodium bicarbonate\t2\t\
    g/L\r\nHemin\t0.005\tg/L\r\n\t\t\r\n"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-version
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b
  locator: Exact commit hash/date
  accessed_at: '2026-10-21T07:59:41.378955Z'
  support: supports
  summary: Revision 803273865ea9e83fab770ec4f13670db80e1180b dates to 2026-09-10,
    later than the March 2026 CultureBotHT import. Current row agreement is not authenticated
    import-time equivalence.
  snapshot_sha256: 0a4998d61b96db10c549512e2fe06718e04b687e6bbc6b2c1ea121c3c11a53ca
- evidence_id: culturebothtRepository-attempt
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:53:13.557900Z'
  support: context_only
  summary: 'Original CultureBotHT source authentication remains unavailable: exact
    https://api.github.com/repos/CultureBotAI/CultureBotHT returned HTTP 404 at 2026-10-21T22:53:13.557900Z.
    Preserved response is not usable recipe/method content; no absence from the wider
    literature is claimed.'
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: culturebothtExactBHIS-attempt
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T23:23:21.747848Z'
  support: context_only
  summary: 'Original CultureBotHT source authentication remains unavailable: exact
    https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml
    returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not
    usable recipe/method content; no absence from the wider literature is claimed.'
  snapshot_sha256: d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed
- evidence_id: paper8573497DOI-attempt
  kind: database
  reference: https://doi.org/10.1099/00207713-46-1-206
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T23:27:14.556019Z'
  support: context_only
  summary: 'Full 1996 article methods needed for exact formula and oxygen protocol
    remains unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned
    HTTP 403 at 2026-10-21T23:27:14.556019+00:00. Preserved response is not usable
    recipe/method content; no absence from the wider literature is claimed.'
  snapshot_sha256: aad69d8ea92f67da40f946775af92ad6d0ab41a862f4ff3f4f5b90a6951a5354
- evidence_id: excluded-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/bhis.yaml
  locator: Full distinct namesake read; exact ID/source/import-event comparison
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: 'Explicit non-owner boundary only: no scientific or quantity transfer from
    TOGO M2814.'
  snapshot_sha256: 0acacc8bfd30711e2df753d5485e08cbfb7b85a060760b00f315a70f6d73bda3
- evidence_id: compound-0
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 569
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Calf brains\t\t\t\t\t\tUsed in BHIS_K3 media\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-1
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 570
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Beef heart\t\t\t\t\t\tUsed in BHIS_K3 media\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-2
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 568
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-3
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 375
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\
    \r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-4
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 171
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\
    \t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-5
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 519
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-6
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 369
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-7
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 520
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact supplied-material metadata; CAS/FW are not a medium dose or measured
    growth result.
  quote: "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: growth-abstract
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml
  locator: PMID 8573497 Article/Abstract/AbstractText, exact BHIS growth sentence
  accessed_at: '2026-10-21T23:23:22.524228Z'
  support: supports
  summary: Current primary abstract directly supports the strain-specific ranges and
    maximum density. It does not establish a paired exact lower endpoint, the eight-row
    FEBA formulation, or an anaerobic protocol.
  quote: In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to
    a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.
  snapshot_sha256: 71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3
- evidence_id: growth-full-abstract
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml
  locator: Complete PMID 8573497 abstract
  accessed_at: '2026-10-21T23:23:22.524228Z'
  support: supports
  summary: Full accessible primary abstract read. Oxygen consumption, substrate-utilization
    and taxonomic comparisons are not a recipe or an anaerobic incubation instruction.
  snapshot_sha256: 71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/420/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9939769d014eb8805a9b8f8ad7a52e41aeccd81ea527e5f0c5ee4655cb849dec
- evidence_id: forms
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/420/chemical-form-inventory.json
  locator: Eight source-material comparisons and five full OLS scientific projections
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Separate source form assessment; unmapped complex materials are retained
    honestly.
  snapshot_sha256: 60a8c78ad1941dd36922941c79a8b39a6520860f5c7e268f787307f8f601d12e
- evidence_id: chebi17561
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.213329Z'
  support: supports
  summary: CHEBI:17561 resolves to L-cysteine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea82f62413bdf5b5575ec20c8bd9e19bb3f41efb6f1efa500401656e6c186292
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
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi50385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.648821Z'
  support: supports
  summary: CHEBI:50385 resolves to hemin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b989203634707b89526a8664c8fa65cb4976c4cdd791427218cf01b37d17356e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T23:53:28Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: attached-claims
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/420/historical-evidence-inventory.json
  locator: 'All four evidence-object instances: two per local layer'
  accessed_at: '2026-10-21T23:53:28Z'
  support: supports
  summary: Exact current raw-substring matches, original explanations and unsupported
    interpretation limits. No historical raw identity is invented.
  snapshot_sha256: f73e821b9d007d06deadb90ea34680b276b0bf42c1aeeb05829eee8d28c75b9d
- evidence_id: taxon
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1042417&retmode=xml
  locator: TaxaSet/Taxon with TaxId 1042417; full current object and lineage
  accessed_at: '2026-10-21T23:23:23.069748Z'
  support: supports
  summary: Canonical strain label, rank and ATCC 51139 synonym support the asserted
    organism identity. Historical Serpulina naming in the 1996 paper is distinguished
    from the current Brachyspira label.
  snapshot_sha256: 8c82fc002ca0410cd840072d7ab9af049696e1f4b5a40c5a1283b2f77693a18e
- evidence_id: assemblyGCA0003256651
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000325665.1/dataset_report
  locator: $.reports[0], full organism/assembly/BioSample and ANI qualification
  accessed_at: '2026-10-21T23:23:23.347617Z'
  support: supports
  summary: Reciprocal current complete-genome accession identifies the same P43/6/78
    / ATCC 51139 strain. The below_threshold_mismatch field is accompanied by taxonomy_check_status
    OK and a type-strain no-match-expected comment; it is not evidence of a taxon
    conflict.
  snapshot_sha256: 63adf1d4634812636d8ba082643517d0c1a6e45856f1d251c145ec876ce39687
- evidence_id: assemblyGCF0003256651
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000325665.1/dataset_report
  locator: $.reports[0], full organism/assembly/BioSample and ANI qualification
  accessed_at: '2026-10-21T23:23:23.751792Z'
  support: supports
  summary: Reciprocal current complete-genome accession identifies the same P43/6/78
    / ATCC 51139 strain. The below_threshold_mismatch field is accompanied by taxonomy_check_status
    OK and a type-strain no-match-expected comment; it is not evidence of a taxon
    conflict.
  snapshot_sha256: 31608ad7329a64a6421c832917461b19a8fcabb1a268a483c6167c628bad0918
- evidence_id: genome-paper
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23469345&retmode=xml
  locator: Full PubMed23469345 citation/abstract and linked PMC3587939
  accessed_at: '2026-10-21T23:23:22.725299Z'
  support: supports
  summary: Complete genome identity statement for the same P43/6/78T strain, distinct
    from growth formulation evidence.
  snapshot_sha256: 5aaad23cbf9fde4c723124edf0ec8a19cd75a85869f37c1bf053494b2ba0e096
- evidence_id: genome-fulltext
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3587939/
  locator: Complete article element, including GENOME ANNOUNCEMENT and Nucleotide
    sequence accession number
  accessed_at: '2026-10-21T23:27:14.709717Z'
  support: supports
  summary: Full article reports complete genome CP002873 and sequencing/identity context.
    It provides no BHIS formula or cultivation protocol, so it does not close the
    1996 methods gap.
  snapshot_sha256: 53f288980deab641a3148252e1c6d4fe6d1dbc97f4daa64eface71475960fd05
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHIS__8d771a65.yaml; data/normalized_yaml/specialized/bhis.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: '[{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis.yaml",
    "events": 4, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_legacy_fields.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-4
  kind: record_content
  reference: scripts/propose_growth_evidence.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: 2d5a5b388c2e63bf1cc395645af1972800618bbe5ec1caef3d7aa60fd7a2d0db
- evidence_id: writer-5
  kind: record_content
  reference: scripts/curate_organism_culture_type.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: 8686de3d3736eaaf3702e2009a299a53819a5ba321966ab2ea01104538ca6a65
- evidence_id: writer-6
  kind: record_content
  reference: scripts/repair_culturebotht_bhis_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Relevant current import/migration, range-extraction proposal, organism
    classification, provenance repair and formulation-preserving merge code was read.
    Current functions do not authenticate historical execution. The September repair
    only restores structured sources/references/history and does not authenticate
    amounts, oxygen conditions or growth scalars.
  snapshot_sha256: a600d3cf5286268fc003f713557588bab018e95fdac24bbbcdcea558753677e6
- evidence_id: prior-report-0
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis.md
  locator: Complete exact-identity prior report
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Earlier local derivative report read in full. It records source limits,
    range and provenance concerns; current sources and local bytes establish this
    review’s findings independently.
  snapshot_sha256: 166fc42dd691bc17e677c30b21aae60ebb9244102122550dfc1a9bb3962adfee
- evidence_id: prior-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS__8d771a65.md
  locator: Complete exact-identity prior report
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Earlier local derivative report read in full. It records source limits,
    range and provenance concerns; current sources and local bytes establish this
    review’s findings independently.
  snapshot_sha256: dbce0b4695b5bae2378b5b28909c0c64ae5756a7926d7664080bc22705766d29
- evidence_id: prior-report-2
  kind: record_content
  reference: reports/yaml_record_review/20260921T212501Z-BHIS__8d771a65.md
  locator: Complete exact-identity prior report
  accessed_at: '2026-10-21T23:53:28Z'
  support: context_only
  summary: Earlier local derivative report read in full. It records source limits,
    range and provenance concerns; current sources and local bytes establish this
    review’s findings independently.
  snapshot_sha256: b8bc7ce1eb079bf9cb5ee2a91051435432b3694726e79ef301e80e5d7c5a6763
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: concern
  summary: Original schema, strict and term checks passed. Original reference validation
    attempted two PMID:8573497 snippets and failed twice because DNS retrieval failed;
    this original failed required check is retained. One separately recorded exact-command
    network-enabled recheck passed two checks with zero issues. These snippet checks
    do not establish the exact scalar growth value, oxygen condition, formulation
    identity or strain/assembly interpretation; those are separately assessed against
    bound sources.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
  - validate-references-network-recheck
- assessment_id: identity
  area: identity
  topic: Exact maintained owner and excluded BHIS namesake
  outcome: supported
  summary: CultureMech:015493, the explicit CultureBotHT import event, source_data
    and merged_from identify specialized/bhis.yaml. The bacterial/bhis.yaml namesake
    is CultureMech:009362, TOGO M2814 solid agar, and is excluded. Its product amounts,
    secondary identifiers and preparation do not transfer. Target and owner agree
    in ingredients and growth assertions; structured provenance differs.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - record
  - owner-0
  - id-search
  - feba-main
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 44 decisions cover all 16 ingredient concentration fields, all 12 numeric/material-note
    fields, both layers’ growth scalars, preparation/variant scope and source-only
    maximum density. All 16 concentration matches are evidence_only. The attached
    growth sentence is genuine, while its exact endpoint and recipe-scope interpretations
    need correction.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Calf brains\",\n\
    \    \"stage\": \"Named FEBA BHIS direct formulation; generated target\",\n  \
    \  \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"7.7\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"value\": \"7.7\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1400 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Calf brains\\t7.7\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q2\",\n    \"name\": \"Beef heart\",\n    \"stage\": \"\
    Named FEBA BHIS direct formulation; generated target\",\n    \"decision\": \"\
    evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"9.8\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1401 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Beef heart\\t9.8\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q3\",\n    \"name\": \"Proteose Peptone\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; generated target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1402 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Proteose Peptone\\t10\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q4\",\n    \"name\": \"Sodium Chloride\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; generated target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1403 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Sodium Chloride\\t5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q5\",\n    \"name\": \"Disodium phosphate\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; generated target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    2.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1404 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Disodium phosphate\\t2.5\\tg/L\\n\",\n        \"\
    snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q6\",\n    \"name\": \"L-Cysteine\",\n    \"stage\": \"\
    Named FEBA BHIS direct formulation; generated target\",\n    \"decision\": \"\
    evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1405 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"L-Cysteine\\t1\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q7\",\n    \"name\": \"Sodium bicarbonate\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; generated target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1406 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Sodium bicarbonate\\t2\\tg/L\\n\",\n        \"\
    snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q8\",\n    \"name\": \"Hemin\",\n    \"stage\": \"Named\
    \ FEBA BHIS direct formulation; generated target\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1407 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Hemin\\t0.005\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q9\",\n    \"name\": \"Calf brains\",\n    \"stage\":\
    \ \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.7\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    7.7\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1400 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Calf brains\\t7.7\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q10\",\n    \"name\": \"Beef heart\",\n    \"stage\":\
    \ \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"9.8\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    9.8\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1401 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Beef heart\\t9.8\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q11\",\n    \"name\": \"Proteose Peptone\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1402 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Proteose Peptone\\t10\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q12\",\n    \"name\": \"Sodium Chloride\",\n    \"stage\"\
    : \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1403 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Sodium Chloride\\t5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q13\",\n    \"name\": \"Disodium phosphate\",\n    \"\
    stage\": \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    2.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1404 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Disodium phosphate\\t2.5\\tg/L\\n\",\n        \"\
    snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q14\",\n    \"name\": \"L-Cysteine\",\n    \"stage\":\
    \ \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1405 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"L-Cysteine\\t1\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q15\",\n    \"name\": \"Sodium bicarbonate\",\n    \"\
    stage\": \"Named FEBA BHIS direct formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1406 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Sodium bicarbonate\\t2\\tg/L\\n\",\n        \"\
    snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q16\",\n    \"name\": \"Hemin\",\n    \"stage\": \"Named\
    \ FEBA BHIS direct formulation; maintained owner\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1407 in exact BHIS block\",\n    \
    \    \"exact_source_quote\": \"Hemin\\t0.005\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Printed\
    \ amount and g/L basis match, but no matching concentration evidence is attached.\
    \ Add exact current version/row linkage without changing the amount or claiming\
    \ the March import or 1996 paper used these exact ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q17\",\n    \"name\": \"Proteose Peptone material notes\"\
    ,\n    \"stage\": \"Identity metadata, not dose\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"CAS:\
    \ 91079-38-8\"\n      }\n    ],\n    \"desired\": \"CAS: 91079-38-8\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\",\n \
    \       \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 568\",\n        \"exact_source_quote\"\
    : \"Proteose Peptone\\t91079-38-8\\tSigma\\t82450\\t\\t\\t\\t\\t\\t\\t\\t\\t\\\
    n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n  \
    \  \"name\": \"Proteose Peptone material notes\",\n    \"stage\": \"Identity metadata,\
    \ not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n\
    \        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"CAS:\
    \ 91079-38-8\"\n      }\n    ],\n    \"desired\": \"CAS: 91079-38-8\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\",\n \
    \       \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 568\",\n        \"exact_source_quote\"\
    : \"Proteose Peptone\\t91079-38-8\\tSigma\\t82450\\t\\t\\t\\t\\t\\t\\t\\t\\t\\\
    n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n  \
    \  \"name\": \"Sodium Chloride material notes\",\n    \"stage\": \"Identity metadata,\
    \ not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n\
    \        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"CAS:\
    \ 7647-14-5; MW: 58.44\"\n      }\n    ],\n    \"desired\": \"CAS: 7647-14-5;\
    \ MW: 58.44\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 375\",\n        \"exact_source_quote\"\
    : \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\t58.44\\tNaCl\\t\\t\\tyes\\t\\\
    t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n  \
    \  \"name\": \"Sodium Chloride material notes\",\n    \"stage\": \"Identity metadata,\
    \ not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n\
    \        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"CAS:\
    \ 7647-14-5; MW: 58.44\"\n      }\n    ],\n    \"desired\": \"CAS: 7647-14-5;\
    \ MW: 58.44\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 375\",\n        \"exact_source_quote\"\
    : \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\t58.44\\tNaCl\\t\\t\\tyes\\t\\\
    t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n  \
    \  \"name\": \"Disodium phosphate material notes\",\n    \"stage\": \"Identity\
    \ metadata, not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96\"\n  \
    \    }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 7558-79-4; MW: 141.96\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 171\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate\\t7558-79-4\\t\\t\\t141.96\\tNa2HPO4, Sodium phosphate\
    \ dibasic\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n  \
    \  \"name\": \"Disodium phosphate material notes\",\n    \"stage\": \"Identity\
    \ metadata, not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96\"\n  \
    \    }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 7558-79-4; MW: 141.96\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 171\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate\\t7558-79-4\\t\\t\\t141.96\\tNa2HPO4, Sodium phosphate\
    \ dibasic\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n  \
    \  \"name\": \"L-Cysteine material notes\",\n    \"stage\": \"Identity metadata,\
    \ not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n\
    \        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\n    \
    \  }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 52-90-4; MW: 121.16\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 519\",\n        \"exact_source_quote\"\
    : \"L-Cysteine\\t52-90-4\\tsigmaaldrich\\tW326305-100G\\t121.16\\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n  \
    \  \"name\": \"L-Cysteine material notes\",\n    \"stage\": \"Identity metadata,\
    \ not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n\
    \        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\n    \
    \  }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 52-90-4; MW: 121.16\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 519\",\n        \"exact_source_quote\"\
    : \"L-Cysteine\\t52-90-4\\tsigmaaldrich\\tW326305-100G\\t121.16\\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n  \
    \  \"name\": \"Sodium bicarbonate material notes\",\n    \"stage\": \"Identity\
    \ metadata, not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007\"\n   \
    \   }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 144-55-8; MW: 84.007\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 369\",\n        \"exact_source_quote\"\
    : \"Sodium bicarbonate\\t144-55-8\\t\\t\\t84.007\\tNaHCO3\\t\\t\\tyes\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n  \
    \  \"name\": \"Sodium bicarbonate material notes\",\n    \"stage\": \"Identity\
    \ metadata, not dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007\"\n   \
    \   }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 144-55-8; MW: 84.007\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 369\",\n        \"exact_source_quote\"\
    : \"Sodium bicarbonate\\t144-55-8\\t\\t\\t84.007\\tNaHCO3\\t\\t\\tyes\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ supports the printed CAS and any FW at its own precision. Local confidence 0.90\
    \ and mapping-method notes are algorithm provenance, not experimental measurements\
    \ or upstream authentication.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n  \
    \  \"name\": \"Hemin material notes\",\n    \"stage\": \"Identity metadata, not\
    \ dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94\"\n \
    \     }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 16009-13-5; MW: 651.94\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 520\",\n        \"exact_source_quote\"\
    : \"Hemin\\t16009-13-5\\tsigmaaldrich\\tH9039-10G\\t651.94\\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"Exact source text with line endings normalized to LF;\
    \ tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source supports\
    \ the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method\
    \ notes are algorithm provenance, not experimental measurements or upstream authentication.\"\
    \n  },\n  {\n    \"decision_id\": \"q28\",\n    \"name\": \"Hemin material notes\"\
    ,\n    \"stage\": \"Identity metadata, not dose\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94\"\n \
    \     }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 16009-13-5; MW: 651.94\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 520\",\n        \"exact_source_quote\"\
    : \"Hemin\\t16009-13-5\\tsigmaaldrich\\tH9039-10G\\t651.94\\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"Exact source text with line endings normalized to LF;\
    \ tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source supports\
    \ the printed CAS and any FW at its own precision. Local confidence 0.90 and mapping-method\
    \ notes are algorithm provenance, not experimental measurements or upstream authentication.\"\
    \n  },\n  {\n    \"decision_id\": \"q29\",\n    \"name\": \"Water, volume and\
    \ preparation\",\n    \"stage\": \"FEBA formula completeness\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [],\n    \"desired\": null,\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"feba_media\",\n     \
    \   \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Complete media lines 1396–1408\",\n        \"\
    exact_source_quote\": \"Media\\tBHIS\\t\\nDescription\\tBrain heart infusion salt\
    \ broth\\t\\nMinimal\\tFALSE\\t\\nControlled vocabulary\\tConcentration\\tUnits\\\
    nCalf brains\\t7.7\\tg/L\\nBeef heart\\t9.8\\tg/L\\nProteose Peptone\\t10\\tg/L\\\
    nSodium Chloride\\t5\\tg/L\\nDisodium phosphate\\t2.5\\tg/L\\nL-Cysteine\\t1\\\
    tg/L\\nSodium bicarbonate\\t2\\tg/L\\nHemin\\t0.005\\tg/L\\n\\t\\t\\n\",\n   \
    \     \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"No water,\
    \ final batch volume, stock addition, pH, temperature or sterilization cycle is\
    \ supplied by this FEBA block. Do not default to a measured 1 L batch or infer\
    \ anaerobic preparation from ingredient names.\"\n  },\n  {\n    \"decision_id\"\
    : \"q30\",\n    \"name\": \"Doubling time\",\n    \"stage\": \"P43/6/78T in the\
    \ paper’s BHIS broth\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"target_organisms[0].growth_metrics[0].doubling_time_minutes\"\
    ,\n        \"stored\": 60.0\n      }\n    ],\n    \"desired\": {\n      \"range_minutes\"\
    : [\n        60,\n        120\n      ],\n      \"exact_point\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The cited\
    \ 1–2 h range converts arithmetically to 60–120 min. Stored 60.0 is its lower\
    \ endpoint, not an authenticated exact doubling-time observation. Preserve the\
    \ source range in supported text; do not populate invented numeric range slots\
    \ or substitute an average.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"\
    name\": \"Growth temperature\",\n    \"stage\": \"P43/6/78T paper context\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\"\
    : \"target_organisms[0].growth_metrics[0].temperature_celsius\",\n        \"stored\"\
    : 37.0\n      }\n    ],\n    \"desired\": {\n      \"source_range_degrees_C\"\
    : [\n        37,\n        42\n      ],\n      \"exact_point\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ gives 37–42 degrees C, not a specific measurement temperature paired with a\
    \ 60 min doubling time. Remove or qualify the unsupported exact scalar while retaining\
    \ the literal range.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"name\"\
    : \"Measurement range and maximum-density text\",\n    \"stage\": \"Paper-specific\
    \ growth context\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n\
    \        \"field_path\": \"target_organisms[0].growth_metrics[0].measurement_conditions\"\
    ,\n        \"stored\": \"BHIS broth; source reports 1 to 2 h doubling time, maximum\
    \ cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.\"\n\
    \      }\n    ],\n    \"desired\": \"BHIS broth; source reports 1 to 2 h doubling\
    \ time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42\
    \ degrees C.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"pubmed8573497\",\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The range\
    \ and maximum-density numbers are accurately repeated and have attached matching\
    \ text. Their assignment to this particular FEBA formula remains unverified; preserve\
    \ the literal paper observation under explicit unresolved recipe scope.\"\n  },\n\
    \  {\n    \"decision_id\": \"q33\",\n    \"name\": \"Variant temperature range\"\
    ,\n    \"stage\": \"Paper-specific variant text\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\"\
    ,\n        \"field_path\": \"variants[0].modifications[1]\",\n        \"stored\"\
    : \"Source reports growth at 37 to 42 degrees C.\"\n      }\n    ],\n    \"desired\"\
    : \"Source reports growth at 37 to 42 degrees C.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"pubmed8573497\",\n        \"source_url\"\
    : \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The literal\
    \ 37–42 degrees C range matches attached evidence. The exact FEBA-to-paper recipe\
    \ identity remains unresolved, so this is not unqualified verification of growth\
    \ on the parent formulation.\"\n  },\n  {\n    \"decision_id\": \"q34\",\n   \
    \ \"name\": \"Anaerobic method\",\n    \"stage\": \"Asserted incubation instruction\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\"\
    : \"variants[0].modifications[0]\",\n        \"stored\": \"Incubate BHIS broth\
    \ anaerobically for Brachyspira growth.\"\n      }\n    ],\n    \"desired\": null,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Complete accessible AbstractText; full methods\
    \ unavailable\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"No explicit\
    \ anaerobic cultivation protocol appears in the full accessible abstract. Consumption\
    \ of substrate amounts of oxygen is not an anaerobic-method instruction. The failed\
    \ DOI full text leaves this required protocol check unresolved; do not infer aerobic\
    \ conditions either.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"name\"\
    : \"Maximum-attainment classification\",\n    \"stage\": \"Growth-metric interpretation\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\"\
    : \"target_organisms[0].growth_metrics[0].is_max_attainment\",\n        \"stored\"\
    : false\n      }\n    ],\n    \"desired\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pubmed8573497\",\n        \"source_url\":\
    \ \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The optional\
    \ false value asserts a conditional/non-default growth context under the schema,\
    \ but no corresponding perturbation or nutrient override is established by this\
    \ sentence. Its maximum cell density does not imply that a doubling-time metric\
    \ should be marked true. Retain unknown rather than infer either Boolean.\"\n\
    \  },\n  {\n    \"decision_id\": \"q36\",\n    \"name\": \"Paper BHIS versus FEBA\
    \ BHIS\",\n    \"stage\": \"Variant-to-parent formula correspondence\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n        \"field_path\": \"\
    variants[0].description\",\n        \"stored\": \"BHIS broth condition supporting\
    \ growth of the Brachyspira pilosicoli type strain P43/6/78T.\"\n      },\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n \
    \       \"field_path\": \"variants[0].purpose\",\n        \"stored\": \"Capture\
    \ strain-specific BHIS growth evidence under the parent BHIS broth record.\"\n\
    \      }\n    ],\n    \"desired\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"pubmed8573497\",\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      },\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Complete FEBA BHIS lines 1396–1408\",\n     \
    \   \"exact_source_quote\": \"Media\\tBHIS\\t\\nDescription\\tBrain heart infusion\
    \ salt broth\\t\\nMinimal\\tFALSE\\t\\nControlled vocabulary\\tConcentration\\\
    tUnits\\nCalf brains\\t7.7\\tg/L\\nBeef heart\\t9.8\\tg/L\\nProteose Peptone\\\
    t10\\tg/L\\nSodium Chloride\\t5\\tg/L\\nDisodium phosphate\\t2.5\\tg/L\\nL-Cysteine\\\
    t1\\tg/L\\nSodium bicarbonate\\t2\\tg/L\\nHemin\\t0.005\\tg/L\\n\\t\\t\\n\",\n\
    \        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The matching\
    \ medium abbreviation supports a research lead, not compositional equality. The\
    \ abstract does not enumerate the paper’s BHIS formula; keep the growth claim\
    \ and organism identity qualified until a complete methods formulation can be\
    \ matched.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"name\": \"Doubling\
    \ time\",\n    \"stage\": \"P43/6/78T in the paper’s BHIS broth\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"target_organisms[0].growth_metrics[0].doubling_time_minutes\"\
    ,\n        \"stored\": 60.0\n      }\n    ],\n    \"desired\": {\n      \"range_minutes\"\
    : [\n        60,\n        120\n      ],\n      \"exact_point\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The cited\
    \ 1–2 h range converts arithmetically to 60–120 min. Stored 60.0 is its lower\
    \ endpoint, not an authenticated exact doubling-time observation. Preserve the\
    \ source range in supported text; do not populate invented numeric range slots\
    \ or substitute an average.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"\
    name\": \"Growth temperature\",\n    \"stage\": \"P43/6/78T paper context\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\"\
    : \"target_organisms[0].growth_metrics[0].temperature_celsius\",\n        \"stored\"\
    : 37.0\n      }\n    ],\n    \"desired\": {\n      \"source_range_degrees_C\"\
    : [\n        37,\n        42\n      ],\n      \"exact_point\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The source\
    \ gives 37–42 degrees C, not a specific measurement temperature paired with a\
    \ 60 min doubling time. Remove or qualify the unsupported exact scalar while retaining\
    \ the literal range.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"name\"\
    : \"Measurement range and maximum-density text\",\n    \"stage\": \"Paper-specific\
    \ growth context\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n\
    \        \"field_path\": \"target_organisms[0].growth_metrics[0].measurement_conditions\"\
    ,\n        \"stored\": \"BHIS broth; source reports 1 to 2 h doubling time, maximum\
    \ cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.\"\n\
    \      }\n    ],\n    \"desired\": \"BHIS broth; source reports 1 to 2 h doubling\
    \ time, maximum cell density of 2 x 10(9) cells per ml, and growth at 37 to 42\
    \ degrees C.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"pubmed8573497\",\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The range\
    \ and maximum-density numbers are accurately repeated and have attached matching\
    \ text. Their assignment to this particular FEBA formula remains unverified; preserve\
    \ the literal paper observation under explicit unresolved recipe scope.\"\n  },\n\
    \  {\n    \"decision_id\": \"q40\",\n    \"name\": \"Variant temperature range\"\
    ,\n    \"stage\": \"Paper-specific variant text\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"variants[0].modifications[1]\",\n        \"stored\"\
    : \"Source reports growth at 37 to 42 degrees C.\"\n      }\n    ],\n    \"desired\"\
    : \"Source reports growth at 37 to 42 degrees C.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"pubmed8573497\",\n        \"source_url\"\
    : \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The literal\
    \ 37–42 degrees C range matches attached evidence. The exact FEBA-to-paper recipe\
    \ identity remains unresolved, so this is not unqualified verification of growth\
    \ on the parent formulation.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n   \
    \ \"name\": \"Anaerobic method\",\n    \"stage\": \"Asserted incubation instruction\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\"\
    : \"variants[0].modifications[0]\",\n        \"stored\": \"Incubate BHIS broth\
    \ anaerobically for Brachyspira growth.\"\n      }\n    ],\n    \"desired\": null,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Complete accessible AbstractText; full methods\
    \ unavailable\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"No explicit\
    \ anaerobic cultivation protocol appears in the full accessible abstract. Consumption\
    \ of substrate amounts of oxygen is not an anaerobic-method instruction. The failed\
    \ DOI full text leaves this required protocol check unresolved; do not infer aerobic\
    \ conditions either.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"name\"\
    : \"Maximum-attainment classification\",\n    \"stage\": \"Growth-metric interpretation\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\"\
    : \"target_organisms[0].growth_metrics[0].is_max_attainment\",\n        \"stored\"\
    : false\n      }\n    ],\n    \"desired\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"pubmed8573497\",\n        \"source_url\":\
    \ \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The optional\
    \ false value asserts a conditional/non-default growth context under the schema,\
    \ but no corresponding perturbation or nutrient override is established by this\
    \ sentence. Its maximum cell density does not imply that a doubling-time metric\
    \ should be marked true. Retain unknown rather than infer either Boolean.\"\n\
    \  },\n  {\n    \"decision_id\": \"q43\",\n    \"name\": \"Paper BHIS versus FEBA\
    \ BHIS\",\n    \"stage\": \"Variant-to-parent formula correspondence\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/bhis.yaml\",\n        \"field_path\": \"\
    variants[0].description\",\n        \"stored\": \"BHIS broth condition supporting\
    \ growth of the Brachyspira pilosicoli type strain P43/6/78T.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\",\n \
    \       \"field_path\": \"variants[0].purpose\",\n        \"stored\": \"Capture\
    \ strain-specific BHIS growth evidence under the parent BHIS broth record.\"\n\
    \      }\n    ],\n    \"desired\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"pubmed8573497\",\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Article/Abstract/AbstractText, exact BHIS growth\
    \ sentence\",\n        \"exact_source_quote\": \"In BHIS broth, P43/6/78T cells\
    \ had a doubling time of 1 to 2 h and grew to a maximum cell density of 2 x 10(9)\
    \ cells per ml at 37 to 42 degrees C.\",\n        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      },\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Complete FEBA BHIS lines 1396–1408\",\n     \
    \   \"exact_source_quote\": \"Media\\tBHIS\\t\\nDescription\\tBrain heart infusion\
    \ salt broth\\t\\nMinimal\\tFALSE\\t\\nControlled vocabulary\\tConcentration\\\
    tUnits\\nCalf brains\\t7.7\\tg/L\\nBeef heart\\t9.8\\tg/L\\nProteose Peptone\\\
    t10\\tg/L\\nSodium Chloride\\t5\\tg/L\\nDisodium phosphate\\t2.5\\tg/L\\nL-Cysteine\\\
    t1\\tg/L\\nSodium bicarbonate\\t2\\tg/L\\nHemin\\t0.005\\tg/L\\n\\t\\t\\n\",\n\
    \        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"The matching\
    \ medium abbreviation supports a research lead, not compositional equality. The\
    \ abstract does not enumerate the paper’s BHIS formula; keep the growth claim\
    \ and organism identity qualified until a complete methods formulation can be\
    \ matched.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"name\": \"Maximum\
    \ cell density\",\n    \"stage\": \"Paper-only observation already retained in\
    \ free text\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/BHIS__8d771a65.yaml\",\n  \
    \      \"field_path\": \"target_organisms[0].growth_metrics[0].measurement_conditions\"\
    ,\n        \"stored\": \"BHIS broth; source reports 1 to 2 h doubling time, maximum\
    \ cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis.yaml\"\
    ,\n        \"field_path\": \"target_organisms[0].growth_metrics[0].measurement_conditions\"\
    ,\n        \"stored\": \"BHIS broth; source reports 1 to 2 h doubling time, maximum\
    \ cell density of 2 x 10(9) cells per ml, and growth at 37 to 42 degrees C.\"\n\
    \      }\n    ],\n    \"desired\": {\n      \"maximum_cells_per_ml\": 2000000000\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"pubmed8573497\"\
    ,\n        \"source_url\": \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8573497&retmode=xml\"\
    ,\n        \"source_locator\": \"Exact growth sentence\",\n        \"exact_source_quote\"\
    : \"In BHIS broth, P43/6/78T cells had a doubling time of 1 to 2 h and grew to\
    \ a maximum cell density of 2 x 10(9) cells per ml at 37 to 42 degrees C.\",\n\
    \        \"snapshot_sha256\": \"71ffa1807dfc76cbde2ed9f179f182636b401e85b095f40e9c99654a18907cc3\"\
    ,\n        \"quote_representation\": \"Exact source text with line endings normalized\
    \ to LF; tabs retained.\"\n      }\n    ],\n    \"interpretation\": \"Verified\
    \ only as narrow source-text correspondence: the authentic cited maximum-density\
    \ text agrees with the existing measurement_conditions in both layers. The source\
    \ reports maximum 2 x 10(9) cells per ml for its BHIS condition. This does not\
    \ verify FEBA formulation equivalence or an exact paired scalar observation. It\
    \ is cell count density, not OD600; no optical-density conversion is made.\"\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '5 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 5/8 primary
    and 0/8 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 62.50%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: source-forms
  area: grounding
  topic: Exact supplied forms and optional ingredient linkages
  outcome: supported
  summary: 'Five primary chemical IDs agree with their canonical labels and source
    name/CAS: sodium chloride, disodium hydrogenphosphate, L-cysteine, sodium hydrogencarbonate
    and hemin. The three complex materials remain unmapped. Neither actual target
    nor maintained owner asserts a secondary or legacy MediaIngredientMech link; identifiers
    in excluded bacterial/bhis.yaml do not transfer.'
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - forms
  - feba-main
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
- assessment_id: growth
  area: evidence
  topic: Claim-level growth support and method/formula boundaries
  outcome: concern
  summary: All four attached evidence instances exactly match the current primary
    abstract. They support P43/6/78T growth in the paper’s BHIS, range 1–2 h, temperature
    range 37–42 degrees C and maximum density 2 x 10(9) cells/ml. Exact scalar 60
    min/37 C, anaerobic instruction, conditional Boolean and equivalence to FEBA BHIS
    are not thereby established. The primary’s broader substrate and taxonomic observations
    are excluded from the recipe.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - growth-abstract
  - growth-full-abstract
  - attached-claims
  - feba-main
- assessment_id: taxon-genome
  area: identity
  topic: Strain, taxon and paired genome identities
  outcome: supported
  summary: NCBITaxon:1042417 is the strain Brachyspira pilosicoli P43/6/78 with synonym
    ATCC 51139. Reciprocal current GCA_000325665.1 and GCF_000325665.1 identify that
    strain and CP002873. PMID:23469345/PMC3587939 supports its complete genome, not
    this medium formula. These identities remain valid despite unresolved growth-condition
    interpretation.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - taxon
  - assemblyGCA0003256651
  - assemblyGCF0003256651
  - genome-paper
  - genome-fulltext
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 8 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: owner-repair
  area: provenance
  topic: Completed maintained-owner repair and stale generated metadata
  outcome: concern
  summary: The specialized owner already contains structured CultureBotHT sources,
    two references and the 2026-09-13 repair event. The August generated target lacks
    them. Credit this completed owner repair and reconcile the projection after any
    scientific corrections; do not propose repeating it or blame the current guarded
    merger for historical losses. Neither layer has a dedicated event recording addition
    of the two Brachyspira evidence blocks; append a truthful current verification/qualification
    event without inventing its historical date.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-6
- assessment_id: history-scope
  area: provenance
  topic: Prior derivative reports and import chronology
  outcome: supported
  summary: The three exact target/owner reports were read. Their concentration triage
    was not a source check. The broad corpus growth report is retained as a search
    lead only and was not fully reread or treated as primary evidence. Four attached
    quote instances have current raw support without a claimed historical response
    digest. FEBA’s September revision postdates the March import.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - prior-report-0
  - prior-report-1
  - prior-report-2
  - attached-claims
  - feba-version
- assessment_id: completeness
  area: completeness
  topic: Unknown formulation protocol and missing quantitative representation
  outcome: unknown
  summary: The accessible FEBA formula has no water, volume, stocks or protocol. GrowthMetrics
    supplies scalar fields but no numeric doubling-time or temperature range slots;
    retain exact ranges in measurement_conditions and omit unsupported point estimates.
    Do not map cell density to OD600. Missing full methods and original CultureBotHT
    bytes make required scientific source coverage partial.
  target_ids:
  - CultureMech:015493
  evidence_ids:
  - feba-main
  - growth-abstract
  - paper8573497DOI-attempt
findings:
- finding_id: f1
  issue_key: culturemech.015493.growth-range-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source growth ranges are stored as exact lower endpoints
  description: Both layers retain a genuine 1–2 h and 37–42 degrees C excerpt but
    store 60.0 minutes and 37.0 degrees C as exact measurement fields. Arithmetic
    establishes 60–120 minutes, not an observed 60 minute doubling time paired with
    37 degrees C.
  target_ids:
  - CultureMech:015493
  field_paths:
  - target_organisms[0].growth_metrics[0].doubling_time_minutes
  - target_organisms[0].growth_metrics[0].temperature_celsius
  evidence_ids:
  - growth-abstract
  - attached-claims
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2.3 is major because source ranges have become exact empirical
    observations, changing their quantitative meaning despite a literal matching snippet.
- finding_id: f2
  issue_key: culturemech.015493.unverified-paper-formula-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Paper growth is asserted for an unreconciled formula and protocol
  description: The growth variant and target organism are attached to this FEBA BHIS
    formula, but the accessible 1996 source names BHIS without its composition or
    an anaerobic method. The current genome article closes neither gap. The optional
    is_max_attainment false also lacks a demonstrated perturbation/non-default context;
    maximum density is a separate observation and does not justify either Boolean.
  target_ids:
  - CultureMech:015493
  field_paths:
  - variants[0].description
  - variants[0].purpose
  - variants[0].modifications[0]
  - variants[0].evidence[0].explanation
  - target_organisms[0].growth_metrics[0].is_max_attainment
  - target_organisms[0].growth_metrics[0].evidence[0].explanation
  evidence_ids:
  - growth-full-abstract
  - feba-main
  - genome-fulltext
  - paper8573497DOI-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2
  normalization_reason: P2.1 is major because a genuine paper observation is assigned
    to an unverified recipe/protocol and classification, changing the biological applicability
    of otherwise authentic evidence.
- finding_id: f3
  issue_key: culturemech.015493.amount-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Current supported ingredient rates lack attached evidence
  description: All eight direct FEBA rates agree numerically in both layers, but none
    has claim-level concentration evidence. Generic source identifiers and a provenance
    repair do not supply the exact version/row/material basis.
  target_ids:
  - CultureMech:015493
  field_paths:
  - ingredients
  - sources
  - references
  evidence_ids:
  - feba-main
  - feba-version
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is a minor traceability exception because all numerical
    ingredient rates are supported; the defect is missing attached versioned source
    linkage, not a demonstrated wrong amount.
- finding_id: f4
  issue_key: culturemech.015493.stale-generated-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target omits completed owner source repair
  description: The maintained owner already has structured sources, two references
    and the September provenance repair event. The older target lacks this information.
    The repair did not change or validate growth values.
  target_ids:
  - CultureMech:015493
  field_paths:
  - sources
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - writer-6
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: 'P4.4 is a minor reconciliation exception: the target omits
    actual maintained provenance, while the owner repair itself is already complete
    and does not establish scientific correctness.'
- finding_id: f5
  issue_key: culturemech.015493.growth-curation-event-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Growth-evidence addition lacks a dedicated audit event
  description: Both layers contain Brachyspira variant and growth evidence, but their
    complete histories record import, ID assignment, organism culture classification
    and either merge or provenance repair, without an event documenting the evidence
    addition or its interpretation. No historical creation time is inferred.
  target_ids:
  - CultureMech:015493
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - attached-claims
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: P4.4 is a minor audit-traceability exception because the supported
    quote is present but its addition/interpretation is not documented by a corresponding
    event; this does not imply fabricated source text.
actions:
- action_id: a1
  description: In the maintained owner, remove or explicitly qualify unsupported exact
    scalars and preserve the original ranges in supported text. Use numeric ranges
    only after a separately authorized schema change; do not insert an average or
    claim a paired endpoint.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
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
  description: Retain the supported strain and paper observation, but qualify its
    relationship to the FEBA formula until the original full recipe and cultivation
    method are verified. Remove unsupported anaerobic/conditional assertions or attach
    exact method evidence. Do not infer the opposite oxygen condition or a true maximum-attainment
    flag.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
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
  description: Attach exact current FEBA concentration evidence to the maintained
    owner, retaining original units and later source date. Do not claim the current
    revision authenticates the original import or the 1996 BHIS recipe.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
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
  description: Preserve the completed owner repair and regenerate its corrected projection
    after scientific follow-up. Confirm sources, references, histories and scoped
    evidence survive; do not repeat the owner repair or rewrite past dates.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:015493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
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
  description: When qualifying the existing evidence, append an accurately dated verification/curation
    event naming the supported ranges and unresolved recipe/protocol limits. Preserve
    earlier events and do not fabricate an original evidence-insertion date.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:015493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis.yaml
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
- The original reference check failed on two DNS fetch errors; the separate exact-command
  recheck passed two snippet checks. Both attempts and actual timestamps are retained.
  This recovery is not evidence that every scientific interpretation of those snippets
  is correct.
- 'Original CultureBotHT source authentication remains unavailable: exact https://api.github.com/repos/CultureBotAI/CultureBotHT
  returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Preserved response is not usable
  recipe/method content; no absence from the wider literature is claimed.'
- 'Original CultureBotHT source authentication remains unavailable: exact https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS.yaml
  returned HTTP 404 at 2026-10-21T23:23:21.747848+00:00. Preserved response is not
  usable recipe/method content; no absence from the wider literature is claimed.'
- 'Full 1996 article methods needed for exact formula and oxygen protocol remains
  unavailable: exact https://doi.org/10.1099/00207713-46-1-206 returned HTTP 403 at
  2026-10-21T23:27:14.556019+00:00. Preserved response is not usable recipe/method
  content; no absence from the wider literature is claimed.'
tags:
- unreviewed-records
- batch-042
- generated-medium
```
