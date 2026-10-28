# Scientific review of blood_agar_medium

- Review: 20261028T045044Z-blood-agar-medium-batch055
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:31:47.030271Z
- Finished UTC: 2026-10-28T04:50:44.855036Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The source is an opaque 1 L Blood agar plate entry, not a recoverable lower-level recipe. The owner has useful volume and provenance repairs, while the generated target retains a mass artifact. The absolute amount is supported; the per-litre normalization and complete formulation remain unresolved.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch055 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008862 | data/merge_yaml/merged/Blood_agar_medium.yaml | generated | blood_agar_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008862 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:008862 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:008862 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:008862 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Distinct opaque TOGO 2276 identity

identity: supported. Targets: CultureMech:008862.

The generated record and sole owner identify TOGO M2276. Its current component is labelled Blood agar plate, with undefined/complex properties; this supports the opaque solid-medium identity only. No original-source URL is present. TOGO M1474/NBRC 254 is a different record and cannot supply the missing formulation.

### Owner repair and unavailable historical writer

provenance: concern. Targets: CultureMech:008862.

The owner already corrects the mass artifact to volume presentation, retains an explicit opaque-source note, a one-liter use instruction and reference. The target is stale. An ignored-inclusive repository filename search and scripts/src/tests content search did not locate repair_togo_eggs_blood_yem_score40.py, named by the September history; historical execution is therefore not reconstructed. Current TOGO importer and conservative merger are inspected future-fix context.

### Empty atomic grounding denominator is intentional

grounding: supported. Targets: CultureMech:008862.

Each selected document has one complex prepared-medium component and zero primary or secondary atomic identifiers. There are no asserted CHEBI labels to verify and no numeric legacy MIM identifiers. Zero links is not a zero-percent accuracy score or evidence that this opaque whole product should be assigned an invented molecule. The upstream GMO descriptor is retained only as a source-reported product category, not a separately asserted local ontology slot.

### Unresolved composition and optional claims

scope: unknown. Targets: CultureMech:008862.

The lower composition and preparation are unavailable in the current exact source. No organism-specific growth, performance, pH or incubation claim is asserted locally. This review remains partial for the unrecovered formulation; it does not invent a recipe or reinterpret empty source fields as proof of universal absence.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:008862.

All 2 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008862", "selected_concentration_field_count": 2, "selected_concentration_fields_covered": 2, "decisions": [{"decision_id": "q1", "subject": "Generated opaque medium quantity", "local_fields": [{"record_path": "data/merge_yaml/merged/Blood_agar_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "opaque prepared product amount", "interpretation": "The source lists 1 L of Blood agar medium, not 1 g/L of a chemical ingredient. Restore the source volume while keeping the formulation opaque; no density, blood proportion or borrowed base formulation is justified.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\": \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\": \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "Maintained volume repair and normalization", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1000", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "opaque prepared product amount", "interpretation": "Credit the repair’s 1 L → 1000 ml conversion and removal of the mass unit. The source supplies an absolute 1 L amount, however, and no receiving final-volume denominator. Retain or explicitly annotate the source batch amount rather than asserting an independently verified 1000 ML_PER_L ingredient concentration.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\": \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\": \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Maintained use-volume instruction", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Use one liter of Blood agar medium."}, {"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml", "field_path": "ingredients[0].notes", "original": "TOGO M2276 lists one liter of Blood agar medium as an opaque blood agar plate."}, {"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml", "field_path": "notes", "original": "TOGO M2276 records one liter of Blood agar medium as an opaque ready-to-use blood agar plate."}], "decision": "evidence_only", "stage": "opaque product use", "interpretation": "The owner’s Use one liter wording faithfully retains the source quantity. This is an amount/use instruction, not a source-supported recipe-preparation protocol.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\": \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\": \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Lower formulation and preparation quantities", "local_fields": [], "decision": "not_quantified", "stage": "unresolved source scope", "interpretation": "The exact TOGO object has no external original-source URL, no lower-level constituents and an empty comments list. It does not specify blood source/dose, agar/base amounts, pH, sterilization or incubation. Do not substitute NBRC 254 or any other similarly named blood agar.", "sources": [{"locator": "$.meta", "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n    \"gm\": \"http://togomedium.org/medium/M2276\",\n    \"name\": \"Blood agar medium\",\n    \"src_url\": \"\"\n  }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[0]", "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\": \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\": \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch055/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:008862.

data/merge_yaml/merged/Blood_agar_medium.yaml: primary 0/1, secondary 0/1; data/normalized_yaml/bacterial/blood_agar_medium.yaml: primary 0/1, secondary 0/1. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI/UBERON term is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is a historical placeholder, not an ID. No percentage is calculated for the empty identifier set of record06. Complex commercial/product components are not forced to pure-compound IDs.

### Native structural checks

schema: supported. Targets: CultureMech:008862.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Generated opaque blood agar retains a mass-unit artifact

major / open / confirmed; issue key: culturemech-008862-stale-generated.

The target’s 1 G_PER_L does not represent the source 1 L prepared-product amount. It also omits the owner’s corrected volume interpretation, opaque-source note, use-volume step and reference. Preserve those meaningful repairs while qualifying the remaining normalization basis.

### f2: Owner normalization exceeds the explicit source amount

minor / open / confirmed; issue key: culturemech-008862-opaque-batch-basis.

The owner records 1000 ML_PER_L for a source row whose only quantity is 1 L. The 1000 ml conversion is correct; a receiving per-litre concentration is not specified. The historical narrative’s endorsement of source faithfulness does not resolve this denominator. The owner’s absolute one-liter preparation sentence is more precise.

### f3: Source opacity and evidence limits need claim-level preservation

minor / open / confirmed; issue key: culturemech-008862-source-evidence.

The owner source URL is useful but the product-volume claim has no attached excerpt. The ingredients_curated flag does not establish a complete lower formulation or independently assessed proprietary recipe.

## Recommended Actions And Acceptance Checks

### action1

Retain the exact opaque source boundary and corrected volume in the maintained owner, then regenerate the target. Do not expand the product using another blood-agar formulation.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Represent or explicitly annotate the absolute 1 L opaque-product amount and avoid presenting the per-litre normalization as direct source evidence. Keep source quantities unchanged until an exact fuller source is inspected.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Attach the exact source object and current access metadata to the volume/opaque-identity claim; explicitly retain missing lower-formulation and preparation information without creating speculative ingredients.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/Blood_agar_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/blood_agar_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch055/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch055/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch055/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch055/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| togoM2276 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276; $.meta; $.components[0].items[0]; $.comments | supports | The complete current object supports only the exact opaque Blood agar medium/product identity and an absolute 1 L amount. Its original-source URL and comments are empty, and no lower formulation or preparation protocol is supplied. It does not establish strain-specific growth. |
| grounding | REVIEW_WORK/batch055/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260921T223358Z-Blood_agar_medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blood_agar_medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Blood_agar_medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| writer11 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer12 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer13 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer14 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch055/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- TOGO M2276 provides no external primary-source URL or constituent recipe. No neighboring blood-agar formulation, blood fraction or sterilization/incubation value was borrowed.
- The source absolute 1 L amount supports 1000 ml conversion but does not itself establish a receiving-medium denominator. Prior reports’ broader normalization endorsement is reassessed rather than inherited.
- The named September repair script was not located by ignored-inclusive search of this owned checkout; no historic code execution is inferred. No asserted atomic or numeric legacy MIM slots exist, so chemical-linkage percentage over such a set is not calculated.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T045044Z-blood-agar-medium-batch055
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of blood_agar_medium
started_at: '2026-10-28T04:31:47.030271Z'
finished_at: '2026-10-28T04:50:44.855036Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The source is an opaque 1 L Blood agar plate entry, not a recoverable lower-level
  recipe. The owner has useful volume and provenance repairs, while the generated
  target retains a mass artifact. The absolute amount is supported; the per-litre
  normalization and complete formulation remain unresolved.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/Blood_agar_medium.yaml
    sha256: 86ec7d4b3e2a6f5f99dac8075c31f36824d1ad0b6d73087a361896b019a93b92
    role: target
  - path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    sha256: 51c32a8a6569f29c775ad959a169ad706957d5a2af2ab42412dea7529a239549
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Blood_agar_medium.md
    sha256: b09781d887b2d6fc08122d7ff8d65af3fba18c9da9be6d6c3b155a48498d7563
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blood_agar_medium.md
    sha256: a4a4b6a9f1915af2c2957191eebb520568e637b844090a24d4c227cbc2319318
    role: context
  - path: reports/yaml_record_review/20260921T223358Z-Blood_agar_medium.md
    sha256: c4e938997f013ddf21564755cb089c91db02df4d73ccd380768c4c8fb83c0206
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch055 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008862
targets:
- target_id: CultureMech:008862
  path: data/merge_yaml/merged/Blood_agar_medium.yaml
  label: blood_agar_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008862
  command: just validate-schema data/merge_yaml/merged/Blood_agar_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008862
  command: just validate-strict data/merge_yaml/merged/Blood_agar_medium.yaml --workers
    1 --out REVIEW_WORK/batch055/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008862
  command: just validate-terms data/merge_yaml/merged/Blood_agar_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:008862
  command: just validate-references data/merge_yaml/merged/Blood_agar_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/Blood_agar_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T04:41:02.153625Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 86ec7d4b3e2a6f5f99dac8075c31f36824d1ad0b6d73087a361896b019a93b92
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/blood_agar_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T04:41:02.153859Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 51c32a8a6569f29c775ad959a169ad706957d5a2af2ab42412dea7529a239549
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch055/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:31:48.417486Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2aa4e1749ba385fec80216d48cacaeb7a081a8a38baf4361c449b504781c4101
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch055/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:31:49.789623Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: a6b77a9b5e5c1380dd33a6aef99f52820fc6ce4dfc83ecd93a9bc321eefe1a1f
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch055/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:31:51.455335Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2e2d946b53cb0f42812423aa52abcf6179b5aebb9bcc16e3b178fe18bd32350a
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch055/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:31:52.347932Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: aa4ce5300aa5921ec385ccadbb1691b2f466785a170b472d620c2d75f2aa0d4b
- evidence_id: togoM2276
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276
  locator: $.meta; $.components[0].items[0]; $.comments
  accessed_at: '2026-10-28T04:32:10.724310Z'
  support: supports
  summary: The complete current object supports only the exact opaque Blood agar medium/product
    identity and an absolute 1 L amount. Its original-source URL and comments are
    empty, and no lower formulation or preparation protocol is supplied. It does not
    establish strain-specific growth.
  snapshot_sha256: 61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch055/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T04:41:02.154907Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 52cdeac873637e16157957b252eb3c29ebd50c9f17fcfe4912962f12161cfb1e
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260921T223358Z-Blood_agar_medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:41:02.154945Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: c4e938997f013ddf21564755cb089c91db02df4d73ccd380768c4c8fb83c0206
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/blood_agar_medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:41:02.154974Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: a4a4b6a9f1915af2c2957191eebb520568e637b844090a24d4c227cbc2319318
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Blood_agar_medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:41:02.154997Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: b09781d887b2d6fc08122d7ff8d65af3fba18c9da9be6d6c3b155a48498d7563
- evidence_id: writer11
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:41:02.155036Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer12
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:41:02.155058Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer13
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:41:02.155081Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer14
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:41:02.155104Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch055/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T04:41:02.155559Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: e827bb0823470d2968d40cae6a651a77f4ea913c06a7e6eef36d2dddf0afcfac
assessments:
- assessment_id: a1
  area: identity
  topic: Distinct opaque TOGO 2276 identity
  outcome: supported
  summary: The generated record and sole owner identify TOGO M2276. Its current component
    is labelled Blood agar plate, with undefined/complex properties; this supports
    the opaque solid-medium identity only. No original-source URL is present. TOGO
    M1474/NBRC 254 is a different record and cannot supply the missing formulation.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - local0
  - local1
  - togoM2276
- assessment_id: a2
  area: provenance
  topic: Owner repair and unavailable historical writer
  outcome: concern
  summary: The owner already corrects the mass artifact to volume presentation, retains
    an explicit opaque-source note, a one-liter use instruction and reference. The
    target is stale. An ignored-inclusive repository filename search and scripts/src/tests
    content search did not locate repair_togo_eggs_blood_yem_score40.py, named by
    the September history; historical execution is therefore not reconstructed. Current
    TOGO importer and conservative merger are inspected future-fix context.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - local0
  - local1
  - history0
  - togoM2276
- assessment_id: a3
  area: grounding
  topic: Empty atomic grounding denominator is intentional
  outcome: supported
  summary: Each selected document has one complex prepared-medium component and zero
    primary or secondary atomic identifiers. There are no asserted CHEBI labels to
    verify and no numeric legacy MIM identifiers. Zero links is not a zero-percent
    accuracy score or evidence that this opaque whole product should be assigned an
    invented molecule. The upstream GMO descriptor is retained only as a source-reported
    product category, not a separately asserted local ontology slot.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - grounding
  - togoM2276
- assessment_id: a4
  area: scope
  topic: Unresolved composition and optional claims
  outcome: unknown
  summary: The lower composition and preparation are unavailable in the current exact
    source. No organism-specific growth, performance, pH or incubation claim is asserted
    locally. This review remains partial for the unrecovered formulation; it does
    not invent a recipe or reinterpret empty source fields as proof of universal absence.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - togoM2276
  - local0
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 2 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008862",
    "selected_concentration_field_count": 2, "selected_concentration_fields_covered":
    2, "decisions": [{"decision_id": "q1", "subject": "Generated opaque medium quantity",
    "local_fields": [{"record_path": "data/merge_yaml/merged/Blood_agar_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "opaque prepared product amount",
    "interpretation": "The source lists 1 L of Blood agar medium, not 1 g/L of a chemical
    ingredient. Restore the source volume while keeping the formulation opaque; no
    density, blood proportion or borrowed base formulation is justified.", "sources":
    [{"locator": "$.components[0].items[0]", "source_key": "togoM2276", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276", "source_raw_sha256":
    "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "source_text_sha256":
    "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98", "accessed_at":
    "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\":
    \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\":
    \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            },\n            {\n              \"id\":
    \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\":
    \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject":
    "Maintained volume repair and normalization", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/blood_agar_medium.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "1000", "unit": "ML_PER_L"}}], "decision": "unsupported",
    "stage": "opaque prepared product amount", "interpretation": "Credit the repair’s
    1 L → 1000 ml conversion and removal of the mass unit. The source supplies an
    absolute 1 L amount, however, and no receiving final-volume denominator. Retain
    or explicitly annotate the source batch amount rather than asserting an independently
    verified 1000 ML_PER_L ingredient concentration.", "sources": [{"locator": "$.components[0].items[0]",
    "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276",
    "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\":
    \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\":
    \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            },\n            {\n              \"id\":
    \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\":
    \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject":
    "Maintained use-volume instruction", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Use one liter of
    Blood agar medium."}, {"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml",
    "field_path": "ingredients[0].notes", "original": "TOGO M2276 lists one liter
    of Blood agar medium as an opaque blood agar plate."}, {"record_path": "data/normalized_yaml/bacterial/blood_agar_medium.yaml",
    "field_path": "notes", "original": "TOGO M2276 records one liter of Blood agar
    medium as an opaque ready-to-use blood agar plate."}], "decision": "evidence_only",
    "stage": "opaque product use", "interpretation": "The owner’s Use one liter wording
    faithfully retains the source quantity. This is an amount/use instruction, not
    a source-supported recipe-preparation protocol.", "sources": [{"locator": "$.components[0].items[0]",
    "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276",
    "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\":
    \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\":
    \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            },\n            {\n              \"id\":
    \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\":
    \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject":
    "Lower formulation and preparation quantities", "local_fields": [], "decision":
    "not_quantified", "stage": "unresolved source scope", "interpretation": "The exact
    TOGO object has no external original-source URL, no lower-level constituents and
    an empty comments list. It does not specify blood source/dose, agar/base amounts,
    pH, sterilization or incubation. Do not substitute NBRC 254 or any other similarly
    named blood agar.", "sources": [{"locator": "$.meta", "source_key": "togoM2276",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276",
    "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n    \"gm\":
    \"http://togomedium.org/medium/M2276\",\n    \"name\": \"Blood agar medium\",\n    \"src_url\":
    \"\"\n  }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[0]",
    "source_key": "togoM2276", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2276",
    "source_raw_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "source_text_sha256": "61e4356b5c0aa195de91dd653189d4667191049de959b23287ac06ae69979d98",
    "accessed_at": "2026-10-28T04:32:10.724310Z", "exact_source_quote": "{\n          \"component_name\":
    \"Blood agar medium\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002397\",\n          \"gmo_id\": \"GMO_002397\",\n          \"label\":
    \"Blood agar plate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            },\n            {\n              \"id\":
    \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\":
    \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch055/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/Blood_agar_medium.yaml: primary 0/1, secondary
    0/1; data/normalized_yaml/bacterial/blood_agar_medium.yaml: primary 0/1, secondary
    0/1. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI/UBERON term is joined
    to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy
    MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is
    a historical placeholder, not an ID. No percentage is calculated for the empty
    identifier set of record06. Complex commercial/product components are not forced
    to pure-compound IDs.'
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - grounding
- assessment_id: a7
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:008862
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-008862-stale-generated
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Generated opaque blood agar retains a mass-unit artifact
  description: The target’s 1 G_PER_L does not represent the source 1 L prepared-product
    amount. It also omits the owner’s corrected volume interpretation, opaque-source
    note, use-volume step and reference. Preserve those meaningful repairs while qualifying
    the remaining normalization basis.
  target_ids:
  - CultureMech:008862
  field_paths:
  - ingredients[0].concentration
  - preparation_steps
  - references
  - notes
  evidence_ids:
  - local0
  - local1
  - togoM2276
  rule_id: generated-record-freshness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008862-opaque-batch-basis
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  title: Owner normalization exceeds the explicit source amount
  description: The owner records 1000 ML_PER_L for a source row whose only quantity
    is 1 L. The 1000 ml conversion is correct; a receiving per-litre concentration
    is not specified. The historical narrative’s endorsement of source faithfulness
    does not resolve this denominator. The owner’s absolute one-liter preparation
    sentence is more precise.
  target_ids:
  - CultureMech:008862
  field_paths:
  - data/normalized_yaml/bacterial/blood_agar_medium.yaml::ingredients[0].concentration
  - data/normalized_yaml/bacterial/blood_agar_medium.yaml::ingredients[0].notes
  evidence_ids:
  - local1
  - togoM2276
  - history0
  rule_id: source-quantity-basis
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008862-source-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source opacity and evidence limits need claim-level preservation
  description: The owner source URL is useful but the product-volume claim has no
    attached excerpt. The ingredients_curated flag does not establish a complete lower
    formulation or independently assessed proprietary recipe.
  target_ids:
  - CultureMech:008862
  field_paths:
  - ingredients[*].evidence
  - data/normalized_yaml/bacterial/blood_agar_medium.yaml::data_quality_flags
  - references
  evidence_ids:
  - grounding
  - local1
  - togoM2276
  rule_id: source-specific-formulation-fidelity
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Retain the exact opaque source boundary and corrected volume in the
    maintained owner, then regenerate the target. Do not expand the product using
    another blood-agar formulation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Represent or explicitly annotate the absolute 1 L opaque-product amount
    and avoid presenting the per-litre normalization as direct source evidence. Keep
    source quantities unchanged until an exact fuller source is inspected.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Attach the exact source object and current access metadata to the volume/opaque-identity
    claim; explicitly retain missing lower-formulation and preparation information
    without creating speculative ingredients.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/blood_agar_medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- TOGO M2276 provides no external primary-source URL or constituent recipe. No neighboring
  blood-agar formulation, blood fraction or sterilization/incubation value was borrowed.
- The source absolute 1 L amount supports 1000 ml conversion but does not itself establish
  a receiving-medium denominator. Prior reports’ broader normalization endorsement
  is reassessed rather than inherited.
- The named September repair script was not located by ignored-inclusive search of
  this owned checkout; no historic code execution is inferred. No asserted atomic
  or numeric legacy MIM slots exist, so chemical-linkage percentage over such a set
  is not calculated.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
