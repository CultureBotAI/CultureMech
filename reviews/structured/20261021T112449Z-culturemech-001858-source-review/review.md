# Source and formulation review: acidithiobacillus_thiooxidans_medium (CultureMech:001858)

- Review: 20261021T112449Z-culturemech-001858-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:17:55Z
- Finished UTC: 2026-10-21T11:24:49Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSMZ 71 base amounts and preparation are supported, but the generated record collapses the DSM 14366 variant into a source duplicate. Its maintained variant lacks the primary-specified iron supplement, and current topology/evidence are newer than the generated copy. Exact KOMODO 71.1 detail remains inaccessible, so the review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 177; batch 018 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seventeen task batches contain 170 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 172 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001858 | data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml | generated | acidithiobacillus_thiooxidans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001858 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001858 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/177/strict.tsv |
| validate-terms | passed | True | CultureMech:001858 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001858 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001858 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo71_1detail | unavailable | True | CultureMech:001858 | The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved original access time. No recipe content was obtained. The accessible MediaList establishes its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently specifies the strain supplement; complete KOMODO-specific formulation verification remains unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001858.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:001858.

5 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 5/5 primary and 5/5 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 5: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:001858.

36 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Base medium, exact source duplicate and DSM 14366 child

identity: concern. Targets: CultureMech:001858.

All three normalized IDs and paths resolve exactly and have the same five base-solute rows. The current normalized topology makes DSMZ 71 the parent, KOMODO 71 a SOURCE_DUPLICATE and KOMODO 71.1 a STRAIN_SPECIFIC_VARIANT. The older generated record instead points to the DSM 14366 child as its SOURCE_DUPLICATE parent and lists that variant as a synonym. The primary explicitly requires an additional 10 mg/L FeSO4 heptahydrate for DSM 14366, absent from the variant owner; this omission explains why its copied base signature alone cannot establish formulation equivalence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001858.

19 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "verified",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "verified"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "KH2PO4 3.00 g",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The base value/unit/basis agrees. Verified is limited to owner layers with exact attached evidence; the target and strain child need evidence. The child also requires the separately assessed supplement.",
    "source_name": "KH2PO4",
    "source_original_amount": 3,
    "source_original_unit": "g",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "3 g / (1000 ml / 1000 ml per L) = 3 g/L; explicit primary final-volume header and provider g_l agree."
  },
  {
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "verified",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "verified"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The base value/unit/basis agrees. Verified is limited to owner layers with exact attached evidence; the target and strain child need evidence. The child also requires the separately assessed supplement.",
    "source_name": "MgSO4 x 7 H2O",
    "source_original_amount": 0.5,
    "source_original_unit": "g",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "0.5 g / (1000 ml / 1000 ml per L) = 0.5 g/L; explicit primary final-volume header and provider g_l agree."
  },
  {
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "verified",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "verified"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.7032,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "(NH4)2SO4 3.00 g",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The base value/unit/basis agrees. Verified is limited to owner layers with exact attached evidence; the target and strain child need evidence. The child also requires the separately assessed supplement.",
    "source_name": "(NH4)2SO4",
    "source_original_amount": 3,
    "source_original_unit": "g",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "3 g / (1000 ml / 1000 ml per L) = 3 g/L; explicit primary final-volume header and provider g_l agree."
  },
  {
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "verified",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "verified"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.70051,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.25 g",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The base value/unit/basis agrees. Verified is limited to owner layers with exact attached evidence; the target and strain child need evidence. The child also requires the separately assessed supplement.",
    "source_name": "CaCl2 x 2 H2O",
    "source_original_amount": 0.25,
    "source_original_unit": "g",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "0.25 g / (1000 ml / 1000 ml per L) = 0.25 g/L; explicit primary final-volume header and provider g_l agree."
  },
  {
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "verified",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "verified"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 20.1462,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "Na2S2O3 x 5 H2O 5.00 g",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The base value/unit/basis agrees. Verified is limited to owner layers with exact attached evidence; the target and strain child need evidence. The child also requires the separately assessed supplement.",
    "source_name": "Na2S2O3 x 5 H2O",
    "source_original_amount": 5,
    "source_original_unit": "g",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "5 g / (1000 ml / 1000 ml per L) = 5 g/L; explicit primary final-volume header and provider g_l agree."
  },
  {
    "field_path": "preparation.water_batch",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "add",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "add",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "add"
    },
    "source_stage": "DSMZ 71 base medium; explicit final volume 1000 ml",
    "source_snippets": [
      {
        "source_key": "mediadive71api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/71",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"
      },
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 page 1, base ingredient table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Retain the source 1000 ml distilled-water row in preparation/batch context, not as a mass concentration.",
    "source_name": "Distilled water",
    "source_original_amount": 1000,
    "source_original_unit": "ml",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "preparation.final_volume",
    "decision": "add",
    "layer_decisions": {
      "target": "add",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "add",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "add",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "add"
    },
    "source_stage": "Base batch",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "Final volume: 1000 ml",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Retain the explicit final-volume basis without deriving it solely from water.",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "ph_range",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "evidence_only"
    },
    "source_stage": "Base medium",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "Final pH: 4.4 - 4.7",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Retain the range in target/base and KOMODO 71 owners; DSM 14366 has its own pH 4.4 decision below.",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "preparation_steps[0].temperature",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "add",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "add"
    },
    "source_stage": "Base medium without thiosulfate",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "autoclave at 121°C",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Target and DSMZ owner preserve 121°C; KOMODO owners omit the operation. Add qualified source preparation there, preserving separate thiosulfate filtration.",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "preparation_steps[0].duration",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "evidence_only",
      "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml": "evidence_only",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "add",
      "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml": "add"
    },
    "source_stage": "Base medium without thiosulfate",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "for 15 min.",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Target and DSMZ owner preserve 15 minutes; KOMODO owners need this source preparation attached and scoped.",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "source_variant.DSM585.tetrathionate",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 585 only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "5.00 g/l tetrathionate (K2S4O6)",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Replace thiosulfate only for this named source variant. The source says add from a filter-sterilized stock, without a stock concentration/dose; do not calculate either or alter the base.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM9463.pH",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 9463 only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "For DSM 9463: Adjust the final pH of the medium to 3.5.",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Qualified source-only pH; not the base pH or evidence for DSM 14366.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM14366.iron_supplement",
    "decision": "add",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "add"
    },
    "source_stage": "DSM 14366 only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "Supplement medium with 10.00 mg/l FeSO4 x 7 H2O.",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Restore this primary-specified supplement in the maintained strain variant and distinguish that variant in generated output. Do not add iron unconditionally to base DSMZ/KOMODO 71.",
    "primary_source_evidence_id": "dsmz71",
    "arithmetic": "10.00 mg/L = 0.01000 g/L; retain the printed heptahydrate mass. This source variant is separate from the five-solute base."
  },
  {
    "field_path": "source_variant.DSM14366.pH",
    "decision": "evidence_only",
    "layer_decisions": {
      "target": "correct",
      "data/normalized_yaml/bacterial/for_dsm_14366.yaml": "evidence_only"
    },
    "source_stage": "DSM 14366 only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "medium should be 4.4.",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The strain owner pH 4.4 agrees but lacks attached support. Preserve separately from the base 4.4–4.7 range.",
    "primary_source_evidence_id": "dsmz71"
  },
  {
    "field_path": "source_variant.DSM14887.CO2",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 14887 gas atmosphere only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "5% CO2 in the gas",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The 5% is a source gas-atmosphere instruction, not a dissolved ingredient concentration or a universal incubation condition.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM103717.sulfur",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 103717 only",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "add 10.00 g/l elemental sulfur",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "The source explicitly omits thiosulfate and substitutes sulfur for this variant; do not combine both substrates or apply it to the reviewed base.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM103717.wetting_water",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 103717 separate sulfur sterilization",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "add 1-2 drops of",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Preserve the stated drop-count range; do not invent a milliliter conversion.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM103717.successive_days",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 103717 separate sulfur sterilization",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "3 successive days",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Preserve source treatment frequency, separate from growth incubation.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  },
  {
    "field_path": "source_variant.DSM103717.duration",
    "decision": "add",
    "layer_decisions": {
      "target": "add"
    },
    "source_stage": "DSM 103717 separate sulfur sterilization",
    "source_snippets": [
      {
        "source_key": "dsmz71",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf",
        "source_locator": "DSMZ 71 PDF page 1, exact header, step 1 or explicitly named strain note",
        "exact_source_quote": "for 3 h at 90-100°C",
        "snapshot_sha256": "36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f",
        "parsed_text_sha256": "a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d"
      }
    ],
    "explanation": "Preserve the 3-hour duration and 90–100°C range together; neither belongs to the base thiosulfate filtration process.",
    "primary_source_evidence_id": "dsmz71",
    "scope_limit": "Source-only conditional context, not an asserted existing variant or automatic base-medium change."
  }
]

### Base protocol, strain scope and owner completeness

completeness: concern. Targets: CultureMech:001858.

Target and DSMZ owner correctly retain the base pH range, 121°C/15-minute autoclaving without thiosulfate, separate thiosulfate filtration/addition and static incubation. Both KOMODO owners omit preparation. Their Aerobic: No notes match the MediaList Is Aerobic=false metadata; this table flag is not independently established anaerobic cultivation guidance and is not converted into a gas instruction. Water/final volume should be retained as source batch context. All five primary strain clauses were read and kept conditional.

### Supplied forms and secondary identity correspondence

grounding: supported. Targets: CultureMech:001858.

The five base primary/secondary terms match phosphate, ammonium sulfate, magnesium sulfate heptahydrate, calcium chloride dihydrate and sodium thiosulfate pentahydrate. All five exact secondary keys exist in the pinned index. The source-only missing DSM 14366 supplement is explicitly FeSO4 heptahydrate; no ontology ID is invented for that proposed addition or other conditional supplements.

### Base medium classification and source metadata

scope: supported. Targets: CultureMech:001858.

The base formulation supports DEFINED/DEFINED and liquid state; bacterial placement is consistent with the collection identity. KOMODO table Is Complex=false agrees at that metadata level. Medium names are retained as source labels, not evidence that every named organism or strain grows in the unmodified base.

### Source evidence, current topology and generated staleness

provenance: concern. Targets: CultureMech:001858.

All ten attached concentration excerpts in the DSMZ and exact KOMODO 71 owners match the current provider bytes and recorded response hash; the KOMODO root identity excerpt also matches exactly. The generated August merge omits those October entries and the September repair topology. The current repair writer preserves the five-solute signature rather than implementing the primary DSM 14366 iron addition. Current merge requires exact formulation compatibility and preserves evidence; the observed legacy merge does not prove a present merger defect.

### Biological identifiers, cultivation claims and literature scope

scope: supported. Targets: CultureMech:001858.

The medium title, generic cultivation application and source-specific strain instructions do not establish an experimental growth result or a taxon/strain equivalence. No target-organism CURIE, genome assembly, DOI or PMID is asserted in the reviewed target or maintained owners. No organism identifier, incubation optimum or unreported growth claim is added. The source-specific DSM numbers are collection recipe qualifiers. Their taxonomic identities, equivalences and experimental growth outcomes were not independently inferred from the title or MediaList.

## Findings

### f1: DSM 14366 is collapsed into the unmodified base despite its iron supplement

blocker / open / confirmed; issue key: cm001858-strain-variant-formulation-collapse.

The generated target calls the DSM 14366 child a SOURCE_DUPLICATE and synonym and points to it as parent. Current owners instead designate a STRAIN_SPECIFIC_VARIANT, while its copied five-row formula still omits the explicit DSMZ 71 requirement for 10 mg/L FeSO4 heptahydrate at pH 4.4. Ingredient-set coincidence from this omission cannot establish equivalence.

### f2: The contributing KOMODO owners omit source-specific preparation

major / open / confirmed; issue key: cm001858-komodo-preparation-scope.

The target and DSMZ owner retain the protocol, but both maintained KOMODO contributors lack the 121°C/15-minute basal operation, separate thiosulfate filtration and static-incubation instructions. Their source boolean note cannot replace a preparation protocol.

### f3: Later verified source evidence is absent from the generated copy

minor / open / confirmed; issue key: cm001858-generated-evidence-staleness.

The target lacks ten existing concentration excerpts across the two evidenced owners, their bibliography and the current identity-only table evidence. The amounts themselves agree with the base source; this gap concerns scoped evidence propagation.

### f4: Historical KOMODO timestamps have malformed or missing zones

minor / open / confirmed; issue key: cm001858-historical-timestamp-format.

36 timestamp instances across target and three maintained contributors were inspected. Two KOMODO import timestamps contain literal .fZ and two resolver timestamps lack a timezone. Current web-import time formatting explains the literal template limitation but does not authenticate a replacement instant.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the maintained DSM 14366 variant with the exact primary supplement and pH, retain the base recipe separately, and regenerate with formulation-aware identity and current topology. Preserve the unavailable KOMODO detail limitation; do not claim exact variant-table composition was retrieved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add exact source-scoped preparation to the maintained contributors only after preserving base versus strain-variant distinctions; retain literal pH, time, temperature, filtration and water/final-volume context with evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the verified owner evidence and its identity-only versus amount scope during authorized regeneration, after correcting variant boundaries.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve existing append-only events. Append a narrowly supported clarification or repair the responsible writer prospectively without fabricating historical UTC times.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/for_dsm_14366.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch018/177/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/177/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml:1:id: CultureMech:001858<br>./data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml:1:id: CultureMech:001858<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch018/source-preflight-bound/177/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 9 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz71 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf; Complete DSMZ 71 PDF page 1, table, final volume/pH, preparation and all five strain notes | supports | Primary text and page image were read. The base formulation is explicit, and the DSM 14366 clause requires 10 mg/L FeSO4 heptahydrate at pH 4.4. |
| mediadive71api | https://mediadive.dsmz.de/rest/medium/71; $.data.medium and complete $.data.solutions[0], main solution 116 | supports | Provider medium 71 supports the base five-solute formulation and preparation. It does not contain the primary PDF strain-specific clauses. |
| komodo-71 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaList row ID=71 and column headers; introductory variant-number explanation | supports | The row supports accession, title, DSMZ 71 original-source mapping, pH and table boolean metadata only. It supplies no ingredient quantities or direct growth experiment. |
| komodo-71-1 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaList row ID=71.1 and column headers; introductory variant-number explanation | supports | The row supports accession, title, DSMZ 71 original-source mapping, pH and table boolean metadata only. It supplies no ingredient quantities or direct growth experiment. |
| komodo71_1detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=71.1; Preserved exact public retrieval result | context_only | The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved original access time. No recipe content was obtained. The accessible MediaList establishes its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently specifies the strain supplement; complete KOMODO-specific formulation verification remains unavailable. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml; data/normalized_yaml/bacterial/for_dsm_14366.yaml; data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_14366.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:08.610055"}]}, {"input": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.698385"}]}] |
| existing-amount-evidence | data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml; data/normalized_yaml/bacterial/for_dsm_14366.yaml; data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml; Every existing attached ingredient excerpt, exact provider object and response hash | supports | [{"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "field_path": "ingredients[0].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "field_path": "ingredients[1].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "field_path": "ingredients[2].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "field_path": "ingredients[3].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml", "field_path": "ingredients[4].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "field_path": "ingredients[0].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "field_path": "ingredients[1].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "field_path": "ingredients[2].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "field_path": "ingredients[3].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}, {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml", "field_path": "ingredients[4].evidence", "literal_and_parsed_object_match": true, "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}] |
| existing-komodo-identity-evidence | data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml; Root evidence[0], exact accession-71 table excerpt and stated identity-only explanation | supports | The attached table excerpt is an exact literal match to the bound MediaList bytes and its response hash. Its explanation correctly limits support to source mapping, not quantities or variants. |
| writer-0 | scripts/repair_komodo_71_acidithiobacillus_score10.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The complete KOMODO 71 repair writer checks an identical five-solute signature, re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain child; it does not add the missing iron. Current KOMODO web import copies is_aerobic to a source note and uses a time.strftime %f template, relevant to literal .fZ history. Current MediaDive extraction omits water and uses provider g_l. Current merge requires scientific formulation compatibility and preserves scoped evidence; the older generated grouping is not proof of current merger behavior. No writer is executed. |
| writer-1 | src/culturemech/import/komodo_web_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The complete KOMODO 71 repair writer checks an identical five-solute signature, re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain child; it does not add the missing iron. Current KOMODO web import copies is_aerobic to a source note and uses a time.strftime %f template, relevant to literal .fZ history. Current MediaDive extraction omits water and uses provider g_l. Current merge requires scientific formulation compatibility and preserves scoped evidence; the older generated grouping is not proof of current merger behavior. No writer is executed. |
| writer-2 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The complete KOMODO 71 repair writer checks an identical five-solute signature, re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain child; it does not add the missing iron. Current KOMODO web import copies is_aerobic to a source note and uses a time.strftime %f template, relevant to literal .fZ history. Current MediaDive extraction omits water and uses provider g_l. Current merge requires scientific formulation compatibility and preserves scoped evidence; the older generated grouping is not proof of current merger behavior. No writer is executed. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The complete KOMODO 71 repair writer checks an identical five-solute signature, re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain child; it does not add the missing iron. Current KOMODO web import copies is_aerobic to a source note and uses a time.strftime %f template, relevant to literal .fZ history. Current MediaDive extraction omits water and uses provider g_l. Current merge requires scientific formulation compatibility and preserves scoped evidence; the older generated grouping is not proof of current merger behavior. No writer is executed. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The complete KOMODO 71 repair writer checks an identical five-solute signature, re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain child; it does not add the missing iron. Current KOMODO web import copies is_aerobic to a source note and uses a time.strftime %f template, relevant to literal .fZ history. Current MediaDive extraction omits water and uses provider g_l. Current merge requires scientific formulation compatibility and preserves scoped evidence; the older generated grouping is not proof of current merger behavior. No writer is executed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch018/177/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved original access time. No recipe content was obtained. The accessible MediaList establishes its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently specifies the strain supplement; complete KOMODO-specific formulation verification remains unavailable.
- Exact KOMODO 71.1 detail is unavailable (HTTP 403), so completion and coverage remain partial despite successful local diagnostics and accessible primary variant instructions.
- The five strain-specific DSMZ clauses are bounded source context, not unconditional ingredients, new growth assertions or inferred taxonomic identities. No concentration is derived for unspecified tetrathionate stock strength/dose.
- The source-specific gas 5% CO2 instruction applies only to DSM 14887. MediaList Aerobic=false does not independently establish an anaerobic protocol for the base or DSM 14366.
- Current writer inspection is static. No historical import replay, merge regeneration, graph export or experimental validation was performed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112449Z-culturemech-001858-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidithiobacillus_thiooxidans_medium (CultureMech:001858)'
started_at: '2026-10-21T11:17:55Z'
finished_at: '2026-10-21T11:24:49Z'
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
summary: The DSMZ 71 base amounts and preparation are supported, but the generated
  record collapses the DSM 14366 variant into a source duplicate. Its maintained variant
  lacks the primary-specified iron supplement, and current topology/evidence are newer
  than the generated copy. Exact KOMODO 71.1 detail remains inaccessible, so the review
  is partial.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
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
  - path: data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
    sha256: 68404f44ca9983ef60a71dcbbfe50caf8b6e667756210949c46320f476e8e18a
    role: target
  - path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    sha256: 4c4d62631c3c43256a4d8f16c1166858e584ec3e5c2d67e1b6d80b87b9a9e10b
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    sha256: fd2b42f0faddaa9f952686f9f64d7cf03f410bb8a18210d5646e1645738d065f
    role: context
  - path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
    sha256: fd5c6bbfb5d8f0c49f39e1d54a7d2d91e206a75291856dedd1317dd240ef9c78
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_komodo_71_acidithiobacillus_score10.py
    sha256: c82b417a6e071952bf842d1a8c1483b30f954e492fe64152f3e9bccd3e5d03fe
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_fetcher.py
    sha256: 0d31cd0ee30e06bb950a4227d76c317b123e3ad69fe455b913fc1dad93265a86
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 177; batch 018 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seventeen task batches
    contain 170 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 172 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001858
targets:
- target_id: CultureMech:001858
  path: data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  label: acidithiobacillus_thiooxidans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/177/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/177/strict.tsv"
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001858
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
  - CultureMech:001858
- check_id: komodo71_1detail-source-access
  name: 'Exact source content access: komodo71_1detail'
  required: true
  status: unavailable
  summary: The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved
    original access time. No recipe content was obtained. The accessible MediaList
    establishes its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently
    specifies the strain supplement; complete KOMODO-specific formulation verification
    remains unavailable.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - komodo71_1detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_14366.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:21.629823Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/177/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:26.888554Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/177/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:30.718563Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:19:32.227111Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:24:48Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml:1:id:
    CultureMech:001858

    ./data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml:1:id:
    CultureMech:001858

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/source-preflight-bound/177/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:24:48Z'
  support: supports
  summary: 9 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: fb9fc3f42daec8398884aead801ab0eb6a9ca4a706b12f1025bc0807a9fb8b97
- evidence_id: dsmz71
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf
  locator: Complete DSMZ 71 PDF page 1, table, final volume/pH, preparation and all
    five strain notes
  accessed_at: '2026-10-21T11:01:46.924075Z'
  support: supports
  summary: Primary text and page image were read. The base formulation is explicit,
    and the DSM 14366 clause requires 10 mg/L FeSO4 heptahydrate at pH 4.4.
  snapshot_sha256: 36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f
- evidence_id: mediadive71api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/71
  locator: $.data.medium and complete $.data.solutions[0], main solution 116
  accessed_at: '2026-10-21T11:01:44.785188Z'
  support: supports
  summary: Provider medium 71 supports the base five-solute formulation and preparation.
    It does not contain the primary PDF strain-specific clauses.
  snapshot_sha256: a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895
- evidence_id: komodo-71
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaList row ID=71 and column headers; introductory variant-number
    explanation
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The row supports accession, title, DSMZ 71 original-source mapping, pH
    and table boolean metadata only. It supplies no ingredient quantities or direct
    growth experiment.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=71'\
    \ >71</a></TD>\n\t\t\t\t\t<TD>THIOBACILLUS FERROOXIDANS MEDIUM WITH THIOSULFATE</TD>\n\
    \t\t\t\t\t<TD> 4.4 - 4.7</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    \t\t\t\t\t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo-71-1
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaList row ID=71.1 and column headers; introductory variant-number
    explanation
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The row supports accession, title, DSMZ 71 original-source mapping, pH
    and table boolean metadata only. It supplies no ingredient quantities or direct
    growth experiment.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=71.1'\
    \ >71.1</a></TD>\n\t\t\t\t\t<TD> For DSM 14366</TD>\n\t\t\t\t\t<TD> 4.4</TD>\n\
    \t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo71_1detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=71.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:01:44.784535Z'
  support: context_only
  summary: The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved
    original access time. No recipe content was obtained. The accessible MediaList
    establishes its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently
    specifies the strain supplement; complete KOMODO-specific formulation verification
    remains unavailable.
  snapshot_sha256: 5779c4c892aeeb3bcb74f55af53dde142e4bca7db44de5fd53203aacf7a31885
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
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T11:24:48Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label":
    "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_THIOOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml;
    data/normalized_yaml/bacterial/for_dsm_14366.yaml; data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_14366.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:08.610055"}]}, {"input": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.698385"}]}]'
- evidence_id: existing-amount-evidence
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml;
    data/normalized_yaml/bacterial/for_dsm_14366.yaml; data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
  locator: Every existing attached ingredient excerpt, exact provider object and response
    hash
  accessed_at: '2026-10-21T11:24:48Z'
  support: supports
  summary: '[{"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "field_path": "ingredients[0].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "field_path": "ingredients[1].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "field_path": "ingredients[2].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "field_path": "ingredients[3].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml",
    "field_path": "ingredients[4].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "field_path": "ingredients[0].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "field_path": "ingredients[1].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "field_path": "ingredients[2].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "field_path": "ingredients[3].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"},
    {"owner": "data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml",
    "field_path": "ingredients[4].evidence", "literal_and_parsed_object_match": true,
    "response_sha256": "a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895"}]'
- evidence_id: existing-komodo-identity-evidence
  kind: record_content
  reference: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
  locator: Root evidence[0], exact accession-71 table excerpt and stated identity-only
    explanation
  accessed_at: '2026-10-21T11:24:48Z'
  support: supports
  summary: The attached table excerpt is an exact literal match to the bound MediaList
    bytes and its response hash. Its explanation correctly limits support to source
    mapping, not quantities or variants.
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_komodo_71_acidithiobacillus_score10.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: The complete KOMODO 71 repair writer checks an identical five-solute signature,
    re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain
    child; it does not add the missing iron. Current KOMODO web import copies is_aerobic
    to a source note and uses a time.strftime %f template, relevant to literal .fZ
    history. Current MediaDive extraction omits water and uses provider g_l. Current
    merge requires scientific formulation compatibility and preserves scoped evidence;
    the older generated grouping is not proof of current merger behavior. No writer
    is executed.
  snapshot_sha256: c82b417a6e071952bf842d1a8c1483b30f954e492fe64152f3e9bccd3e5d03fe
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: The complete KOMODO 71 repair writer checks an identical five-solute signature,
    re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain
    child; it does not add the missing iron. Current KOMODO web import copies is_aerobic
    to a source note and uses a time.strftime %f template, relevant to literal .fZ
    history. Current MediaDive extraction omits water and uses provider g_l. Current
    merge requires scientific formulation compatibility and preserves scoped evidence;
    the older generated grouping is not proof of current merger behavior. No writer
    is executed.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: The complete KOMODO 71 repair writer checks an identical five-solute signature,
    re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain
    child; it does not add the missing iron. Current KOMODO web import copies is_aerobic
    to a source note and uses a time.strftime %f template, relevant to literal .fZ
    history. Current MediaDive extraction omits water and uses provider g_l. Current
    merge requires scientific formulation compatibility and preserves scoped evidence;
    the older generated grouping is not proof of current merger behavior. No writer
    is executed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: The complete KOMODO 71 repair writer checks an identical five-solute signature,
    re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain
    child; it does not add the missing iron. Current KOMODO web import copies is_aerobic
    to a source note and uses a time.strftime %f template, relevant to literal .fZ
    history. Current MediaDive extraction omits water and uses provider g_l. Current
    merge requires scientific formulation compatibility and preserves scoped evidence;
    the older generated grouping is not proof of current merger behavior. No writer
    is executed.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: The complete KOMODO 71 repair writer checks an identical five-solute signature,
    re-roots DSMZ 71, and distinguishes the KOMODO 71 duplicate from the 71.1 strain
    child; it does not add the missing iron. Current KOMODO web import copies is_aerobic
    to a source note and uses a time.strftime %f template, relevant to literal .fZ
    history. Current MediaDive extraction omits water and uses provider g_l. Current
    merge requires scientific formulation compatibility and preserves scoped evidence;
    the older generated grouping is not proof of current merger behavior. No writer
    is executed.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/177/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:24:48Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7f6a356b139d6ac97fea18278a0bb7d90892296cc1ad3e6923b6564bb246174c
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '5 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 5/5 primary and 5/5 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi31795
  - chebi32150
  - chebi62946
  - chebi63036
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 5: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 36 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: identity
  area: identity
  topic: Base medium, exact source duplicate and DSM 14366 child
  outcome: concern
  summary: All three normalized IDs and paths resolve exactly and have the same five
    base-solute rows. The current normalized topology makes DSMZ 71 the parent, KOMODO
    71 a SOURCE_DUPLICATE and KOMODO 71.1 a STRAIN_SPECIFIC_VARIANT. The older generated
    record instead points to the DSM 14366 child as its SOURCE_DUPLICATE parent and
    lists that variant as a synonym. The primary explicitly requires an additional
    10 mg/L FeSO4 heptahydrate for DSM 14366, absent from the variant owner; this
    omission explains why its copied base signature alone cannot establish formulation
    equivalence.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsmz71
  - komodo-71
  - komodo-71-1
  - writer-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 19 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"field_path\": \"ingredients[0].concentration\",\n    \"\
    decision\": \"evidence_only\",\n    \"layer_decisions\": {\n      \"target\":\
    \ \"evidence_only\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"verified\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\":\
    \ \"evidence_only\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"verified\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit\
    \ final volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n                \
    \        \\\"compound_id\\\": 11,\\n                        \\\"amount\\\": 3,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 3,\\n                        \\\"mmol_l\\\": 22.045,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 3.00 g\",\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The base value/unit/basis agrees. Verified\
    \ is limited to owner layers with exact attached evidence; the target and strain\
    \ child need evidence. The child also requires the separately assessed supplement.\"\
    ,\n    \"source_name\": \"KH2PO4\",\n    \"source_original_amount\": 3,\n    \"\
    source_original_unit\": \"g\",\n    \"primary_source_evidence_id\": \"dsmz71\"\
    ,\n    \"arithmetic\": \"3 g / (1000 ml / 1000 ml per L) = 3 g/L; explicit primary\
    \ final-volume header and provider g_l agree.\"\n  },\n  {\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"evidence_only\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"verified\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\":\
    \ \"evidence_only\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"verified\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit\
    \ final volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 8,\\n                        \\\"amount\\\
    \": 0.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.02859,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\
    \n      },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n     \
    \   \"source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"\
    exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\":\
    \ \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\",\n    \
    \    \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The base value/unit/basis agrees. Verified\
    \ is limited to owner layers with exact attached evidence; the target and strain\
    \ child need evidence. The child also requires the separately assessed supplement.\"\
    ,\n    \"source_name\": \"MgSO4 x 7 H2O\",\n    \"source_original_amount\": 0.5,\n\
    \    \"source_original_unit\": \"g\",\n    \"primary_source_evidence_id\": \"\
    dsmz71\",\n    \"arithmetic\": \"0.5 g / (1000 ml / 1000 ml per L) = 0.5 g/L;\
    \ explicit primary final-volume header and provider g_l agree.\"\n  },\n  {\n\
    \    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"evidence_only\",\n      \"\
    data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\": \"\
    verified\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\": \"evidence_only\"\
    ,\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"verified\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit\
    \ final volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n             \
    \           \\\"compound_id\\\": 27,\\n                        \\\"amount\\\"\
    : 3,\\n                        \\\"unit\\\": \\\"g\\\",\\n                   \
    \     \\\"g_l\\\": 3,\\n                        \\\"mmol_l\\\": 22.7032,\\n  \
    \                      \\\"optional\\\": 0\\n                    }\",\n      \
    \  \"snapshot_sha256\": \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\
    \n      },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n     \
    \   \"source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"\
    exact_source_quote\": \"(NH4)2SO4 3.00 g\",\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The base value/unit/basis agrees. Verified\
    \ is limited to owner layers with exact attached evidence; the target and strain\
    \ child need evidence. The child also requires the separately assessed supplement.\"\
    ,\n    \"source_name\": \"(NH4)2SO4\",\n    \"source_original_amount\": 3,\n \
    \   \"source_original_unit\": \"g\",\n    \"primary_source_evidence_id\": \"dsmz71\"\
    ,\n    \"arithmetic\": \"3 g / (1000 ml / 1000 ml per L) = 3 g/L; explicit primary\
    \ final-volume header and provider g_l agree.\"\n  },\n  {\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"layer_decisions\": {\n      \"target\": \"evidence_only\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"verified\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\":\
    \ \"evidence_only\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"verified\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit\
    \ final volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 0.25,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.25,\\n                        \\\"mmol_l\\\": 1.70051,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\
    \n      },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n     \
    \   \"source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"\
    exact_source_quote\": \"CaCl2 x 2 H2O 0.25 g\",\n        \"snapshot_sha256\":\
    \ \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\",\n    \
    \    \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The base value/unit/basis agrees. Verified\
    \ is limited to owner layers with exact attached evidence; the target and strain\
    \ child need evidence. The child also requires the separately assessed supplement.\"\
    ,\n    \"source_name\": \"CaCl2 x 2 H2O\",\n    \"source_original_amount\": 0.25,\n\
    \    \"source_original_unit\": \"g\",\n    \"primary_source_evidence_id\": \"\
    dsmz71\",\n    \"arithmetic\": \"0.25 g / (1000 ml / 1000 ml per L) = 0.25 g/L;\
    \ explicit primary final-volume header and provider g_l agree.\"\n  },\n  {\n\
    \    \"field_path\": \"ingredients[4].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"layer_decisions\": {\n      \"target\": \"evidence_only\",\n      \"\
    data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\": \"\
    verified\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\": \"evidence_only\"\
    ,\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"verified\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit\
    \ final volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 65,\\n                        \\\"amount\\\
    \": 5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 5,\\n                        \\\"mmol_l\\\": 20.1462,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\
    \n      },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n     \
    \   \"source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"\
    exact_source_quote\": \"Na2S2O3 x 5 H2O 5.00 g\",\n        \"snapshot_sha256\"\
    : \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\",\n    \
    \    \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The base value/unit/basis agrees. Verified\
    \ is limited to owner layers with exact attached evidence; the target and strain\
    \ child need evidence. The child also requires the separately assessed supplement.\"\
    ,\n    \"source_name\": \"Na2S2O3 x 5 H2O\",\n    \"source_original_amount\":\
    \ 5,\n    \"source_original_unit\": \"g\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\",\n    \"arithmetic\": \"5 g / (1000 ml / 1000 ml per L) = 5 g/L;\
    \ explicit primary final-volume header and provider g_l agree.\"\n  },\n  {\n\
    \    \"field_path\": \"preparation.water_batch\",\n    \"decision\": \"add\",\n\
    \    \"layer_decisions\": {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"add\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\": \"add\"\
    ,\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"DSMZ 71 base medium; explicit final\
    \ volume 1000 ml\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive71api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/71\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"a8cc5d040527ea27750d2a6ffcfc518c03b0ea1da2b7da7acf62783f67748895\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 page 1, base ingredient table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the source 1000 ml distilled-water\
    \ row in preparation/batch context, not as a mass concentration.\",\n    \"source_name\"\
    : \"Distilled water\",\n    \"source_original_amount\": 1000,\n    \"source_original_unit\"\
    : \"ml\",\n    \"primary_source_evidence_id\": \"dsmz71\"\n  },\n  {\n    \"field_path\"\
    : \"preparation.final_volume\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"add\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\": \"add\"\
    ,\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Base batch\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"Final volume: 1000 ml\",\n\
    \        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the explicit final-volume basis\
    \ without deriving it solely from water.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\"\n  },\n  {\n    \"field_path\": \"ph_range\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"layer_decisions\": {\n      \"target\": \"evidence_only\"\
    ,\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"evidence_only\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"evidence_only\"\n    },\n    \"source_stage\": \"Base medium\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"Final pH: 4.4 - 4.7\",\n \
    \       \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the range in target/base and\
    \ KOMODO 71 owners; DSM 14366 has its own pH 4.4 decision below.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\"\n  },\n  {\n    \"field_path\": \"preparation_steps[0].temperature\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"layer_decisions\": {\n      \"\
    target\": \"evidence_only\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"evidence_only\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\"\
    : \"add\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Base medium without thiosulfate\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz71\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"autoclave at 121°C\"\
    ,\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Target and DSMZ owner preserve 121°C;\
    \ KOMODO owners omit the operation. Add qualified source preparation there, preserving\
    \ separate thiosulfate filtration.\",\n    \"primary_source_evidence_id\": \"\
    dsmz71\"\n  },\n  {\n    \"field_path\": \"preparation_steps[0].duration\",\n\
    \    \"decision\": \"evidence_only\",\n    \"layer_decisions\": {\n      \"target\"\
    : \"evidence_only\",\n      \"data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml\"\
    : \"evidence_only\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\"\
    : \"add\",\n      \"data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"Base medium without thiosulfate\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz71\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"for 15 min.\",\n   \
    \     \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Target and DSMZ owner preserve 15 minutes;\
    \ KOMODO owners need this source preparation attached and scoped.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\"\n  },\n  {\n    \"field_path\": \"source_variant.DSM585.tetrathionate\"\
    ,\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"\
    add\"\n    },\n    \"source_stage\": \"DSM 585 only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"5.00 g/l tetrathionate (K2S4O6)\"\
    ,\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Replace thiosulfate only for this named\
    \ source variant. The source says add from a filter-sterilized stock, without\
    \ a stock concentration/dose; do not calculate either or alter the base.\",\n\
    \    \"primary_source_evidence_id\": \"dsmz71\",\n    \"scope_limit\": \"Source-only\
    \ conditional context, not an asserted existing variant or automatic base-medium\
    \ change.\"\n  },\n  {\n    \"field_path\": \"source_variant.DSM9463.pH\",\n \
    \   \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"add\"\
    \n    },\n    \"source_stage\": \"DSM 9463 only\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"For DSM 9463: Adjust\
    \ the final pH of the medium to 3.5.\",\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Qualified source-only pH; not the base\
    \ pH or evidence for DSM 14366.\",\n    \"primary_source_evidence_id\": \"dsmz71\"\
    ,\n    \"scope_limit\": \"Source-only conditional context, not an asserted existing\
    \ variant or automatic base-medium change.\"\n  },\n  {\n    \"field_path\": \"\
    source_variant.DSM14366.iron_supplement\",\n    \"decision\": \"add\",\n    \"\
    layer_decisions\": {\n      \"target\": \"correct\",\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\"\
    : \"add\"\n    },\n    \"source_stage\": \"DSM 14366 only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"Supplement medium with 10.00\
    \ mg/l FeSO4 x 7 H2O.\",\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this primary-specified supplement\
    \ in the maintained strain variant and distinguish that variant in generated output.\
    \ Do not add iron unconditionally to base DSMZ/KOMODO 71.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\",\n    \"arithmetic\": \"10.00 mg/L = 0.01000 g/L; retain the printed\
    \ heptahydrate mass. This source variant is separate from the five-solute base.\"\
    \n  },\n  {\n    \"field_path\": \"source_variant.DSM14366.pH\",\n    \"decision\"\
    : \"evidence_only\",\n    \"layer_decisions\": {\n      \"target\": \"correct\"\
    ,\n      \"data/normalized_yaml/bacterial/for_dsm_14366.yaml\": \"evidence_only\"\
    \n    },\n    \"source_stage\": \"DSM 14366 only\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"medium should be 4.4.\",\n\
    \        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The strain owner pH 4.4 agrees but lacks\
    \ attached support. Preserve separately from the base 4.4–4.7 range.\",\n    \"\
    primary_source_evidence_id\": \"dsmz71\"\n  },\n  {\n    \"field_path\": \"source_variant.DSM14887.CO2\"\
    ,\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"\
    add\"\n    },\n    \"source_stage\": \"DSM 14887 gas atmosphere only\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz71\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"5% CO2 in the gas\"\
    ,\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The 5% is a source gas-atmosphere instruction,\
    \ not a dissolved ingredient concentration or a universal incubation condition.\"\
    ,\n    \"primary_source_evidence_id\": \"dsmz71\",\n    \"scope_limit\": \"Source-only\
    \ conditional context, not an asserted existing variant or automatic base-medium\
    \ change.\"\n  },\n  {\n    \"field_path\": \"source_variant.DSM103717.sulfur\"\
    ,\n    \"decision\": \"add\",\n    \"layer_decisions\": {\n      \"target\": \"\
    add\"\n    },\n    \"source_stage\": \"DSM 103717 only\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"add 10.00 g/l elemental sulfur\"\
    ,\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"The source explicitly omits thiosulfate\
    \ and substitutes sulfur for this variant; do not combine both substrates or apply\
    \ it to the reviewed base.\",\n    \"primary_source_evidence_id\": \"dsmz71\"\
    ,\n    \"scope_limit\": \"Source-only conditional context, not an asserted existing\
    \ variant or automatic base-medium change.\"\n  },\n  {\n    \"field_path\": \"\
    source_variant.DSM103717.wetting_water\",\n    \"decision\": \"add\",\n    \"\
    layer_decisions\": {\n      \"target\": \"add\"\n    },\n    \"source_stage\"\
    : \"DSM 103717 separate sulfur sterilization\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"add 1-2 drops of\",\n\
    \        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the stated drop-count range;\
    \ do not invent a milliliter conversion.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz71\",\n    \"scope_limit\": \"Source-only conditional context, not an\
    \ asserted existing variant or automatic base-medium change.\"\n  },\n  {\n  \
    \  \"field_path\": \"source_variant.DSM103717.successive_days\",\n    \"decision\"\
    : \"add\",\n    \"layer_decisions\": {\n      \"target\": \"add\"\n    },\n  \
    \  \"source_stage\": \"DSM 103717 separate sulfur sterilization\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz71\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\",\n        \"\
    source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly named\
    \ strain note\",\n        \"exact_source_quote\": \"3 successive days\",\n   \
    \     \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve source treatment frequency,\
    \ separate from growth incubation.\",\n    \"primary_source_evidence_id\": \"\
    dsmz71\",\n    \"scope_limit\": \"Source-only conditional context, not an asserted\
    \ existing variant or automatic base-medium change.\"\n  },\n  {\n    \"field_path\"\
    : \"source_variant.DSM103717.duration\",\n    \"decision\": \"add\",\n    \"layer_decisions\"\
    : {\n      \"target\": \"add\"\n    },\n    \"source_stage\": \"DSM 103717 separate\
    \ sulfur sterilization\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz71\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium71.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 71 PDF page 1, exact header, step 1 or explicitly\
    \ named strain note\",\n        \"exact_source_quote\": \"for 3 h at 90-100°C\"\
    ,\n        \"snapshot_sha256\": \"36a029be28669c3bdf6f75e34e94e29d40e433d26723ebbf5f7c5cc34392c77f\"\
    ,\n        \"parsed_text_sha256\": \"a0421de6eff93ee49193bf009c5df2b209bf70fbb671df632d01cfc5111e1e6d\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the 3-hour duration and 90–100°C\
    \ range together; neither belongs to the base thiosulfate filtration process.\"\
    ,\n    \"primary_source_evidence_id\": \"dsmz71\",\n    \"scope_limit\": \"Source-only\
    \ conditional context, not an asserted existing variant or automatic base-medium\
    \ change.\"\n  }\n]"
- assessment_id: preparation
  area: completeness
  topic: Base protocol, strain scope and owner completeness
  outcome: concern
  summary: 'Target and DSMZ owner correctly retain the base pH range, 121°C/15-minute
    autoclaving without thiosulfate, separate thiosulfate filtration/addition and
    static incubation. Both KOMODO owners omit preparation. Their Aerobic: No notes
    match the MediaList Is Aerobic=false metadata; this table flag is not independently
    established anaerobic cultivation guidance and is not converted into a gas instruction.
    Water/final volume should be retained as source batch context. All five primary
    strain clauses were read and kept conditional.'
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsmz71
  - komodo-71
  - komodo-71-1
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Supplied forms and secondary identity correspondence
  outcome: supported
  summary: The five base primary/secondary terms match phosphate, ammonium sulfate,
    magnesium sulfate heptahydrate, calcium chloride dihydrate and sodium thiosulfate
    pentahydrate. All five exact secondary keys exist in the pinned index. The source-only
    missing DSM 14366 supplement is explicitly FeSO4 heptahydrate; no ontology ID
    is invented for that proposed addition or other conditional supplements.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsmz71
  - mim
  - chebi63036
  - chebi31795
  - chebi62946
  - chebi86158
  - chebi32150
- assessment_id: classification
  area: scope
  topic: Base medium classification and source metadata
  outcome: supported
  summary: The base formulation supports DEFINED/DEFINED and liquid state; bacterial
    placement is consistent with the collection identity. KOMODO table Is Complex=false
    agrees at that metadata level. Medium names are retained as source labels, not
    evidence that every named organism or strain grows in the unmodified base.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsmz71
  - mediadive71api
  - komodo-71
  - komodo-71-1
- assessment_id: provenance
  area: provenance
  topic: Source evidence, current topology and generated staleness
  outcome: concern
  summary: All ten attached concentration excerpts in the DSMZ and exact KOMODO 71
    owners match the current provider bytes and recorded response hash; the KOMODO
    root identity excerpt also matches exactly. The generated August merge omits those
    October entries and the September repair topology. The current repair writer preserves
    the five-solute signature rather than implementing the primary DSM 14366 iron
    addition. Current merge requires exact formulation compatibility and preserves
    evidence; the observed legacy merge does not prove a present merger defect.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - existing-amount-evidence
  - existing-komodo-identity-evidence
  - history-metadata
  - writer-0
  - writer-3
  - writer-4
- assessment_id: biology
  area: scope
  topic: Biological identifiers, cultivation claims and literature scope
  outcome: supported
  summary: The medium title, generic cultivation application and source-specific strain
    instructions do not establish an experimental growth result or a taxon/strain
    equivalence. No target-organism CURIE, genome assembly, DOI or PMID is asserted
    in the reviewed target or maintained owners. No organism identifier, incubation
    optimum or unreported growth claim is added. The source-specific DSM numbers are
    collection recipe qualifiers. Their taxonomic identities, equivalences and experimental
    growth outcomes were not independently inferred from the title or MediaList.
  target_ids:
  - CultureMech:001858
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
findings:
- finding_id: f1
  issue_key: cm001858-strain-variant-formulation-collapse
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: DSM 14366 is collapsed into the unmodified base despite its iron supplement
  description: The generated target calls the DSM 14366 child a SOURCE_DUPLICATE and
    synonym and points to it as parent. Current owners instead designate a STRAIN_SPECIFIC_VARIANT,
    while its copied five-row formula still omits the explicit DSMZ 71 requirement
    for 10 mg/L FeSO4 heptahydrate at pH 4.4. Ingredient-set coincidence from this
    omission cannot establish equivalence.
  target_ids:
  - CultureMech:001858
  field_paths:
  - parent_media
  - variant_relationship
  - variant_modifications
  - synonyms
  - merged_from
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - dsmz71
  - komodo-71-1
  - quantity-inventory
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
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
  issue_key: cm001858-komodo-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The contributing KOMODO owners omit source-specific preparation
  description: The target and DSMZ owner retain the protocol, but both maintained
    KOMODO contributors lack the 121°C/15-minute basal operation, separate thiosulfate
    filtration and static-incubation instructions. Their source boolean note cannot
    replace a preparation protocol.
  target_ids:
  - CultureMech:001858
  field_paths:
  - preparation_steps
  evidence_ids:
  - owner-1
  - owner-2
  - dsmz71
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because omitting the required
    separate thiosulfate sterilization and exact basal cycle materially limits reproducibility
    in maintained contributors, even though the generated canonical copy retains the
    base protocol.
- finding_id: f3
  issue_key: cm001858-generated-evidence-staleness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Later verified source evidence is absent from the generated copy
  description: The target lacks ten existing concentration excerpts across the two
    evidenced owners, their bibliography and the current identity-only table evidence.
    The amounts themselves agree with the base source; this gap concerns scoped evidence
    propagation.
  target_ids:
  - CultureMech:001858
  field_paths:
  - ingredients[*].evidence
  - references
  - evidence
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-2
  - existing-amount-evidence
  - existing-komodo-identity-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is normalized to minor because independently supported
    values already have maintained evidence that is missing from the generated view;
    the scientific variant defect is separately classified as a blocker.
- finding_id: f4
  issue_key: cm001858-historical-timestamp-format
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical KOMODO timestamps have malformed or missing zones
  description: 36 timestamp instances across target and three maintained contributors
    were inspected. Two KOMODO import timestamps contain literal .fZ and two resolver
    timestamps lack a timezone. Current web-import time formatting explains the literal
    template limitation but does not authenticate a replacement instant.
  target_ids:
  - CultureMech:001858
  field_paths:
  - curation_history
  evidence_ids:
  - owner-1
  - owner-2
  - history-metadata
  - writer-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4
  native_severity: P4
  normalization_reason: P4 provenance metadata is normalized to minor because malformed
    or zone-naive historical times reduce audit precision without changing the supported
    base recipe amounts.
actions:
- action_id: a1
  description: Reconcile the maintained DSM 14366 variant with the exact primary supplement
    and pH, retain the base recipe separately, and regenerate with formulation-aware
    identity and current topology. Preserve the unavailable KOMODO detail limitation;
    do not claim exact variant-table composition was retrieved.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001858
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
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
  description: Add exact source-scoped preparation to the maintained contributors
    only after preserving base versus strain-variant distinctions; retain literal
    pH, time, temperature, filtration and water/final-volume context with evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001858
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
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
  description: Preserve the verified owner evidence and its identity-only versus amount
    scope during authorized regeneration, after correcting variant boundaries.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001858
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
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
  description: Preserve existing append-only events. Append a narrowly supported clarification
    or repair the responsible writer prospectively without fabricating historical
    UTC times.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001858
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_thiooxidans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14366.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_thiosulfate.yaml
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
- The exact public KOMODO 71.1 detail attempt returned HTTP 403 at its preserved original
  access time. No recipe content was obtained. The accessible MediaList establishes
  its DSMZ 71/DSM 14366 identity context, while the DSMZ primary independently specifies
  the strain supplement; complete KOMODO-specific formulation verification remains
  unavailable.
- Exact KOMODO 71.1 detail is unavailable (HTTP 403), so completion and coverage remain
  partial despite successful local diagnostics and accessible primary variant instructions.
- The five strain-specific DSMZ clauses are bounded source context, not unconditional
  ingredients, new growth assertions or inferred taxonomic identities. No concentration
  is derived for unspecified tetrathionate stock strength/dose.
- The source-specific gas 5% CO2 instruction applies only to DSM 14887. MediaList
  Aerobic=false does not independently establish an anaerobic protocol for the base
  or DSM 14366.
- Current writer inspection is static. No historical import replay, merge regeneration,
  graph export or experimental validation was performed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-018
- generated-medium
```
