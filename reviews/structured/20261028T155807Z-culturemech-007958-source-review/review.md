# Scientific review: Cornmeal Agar

- Review: 20261028T155807Z-culturemech-007958-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T15:21:37.344891Z
- Finished UTC: 2026-10-28T15:58:07.333938Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact primary NBRC identity is supported, but water units and concentration basis require maintained-owner curation. The source pH is missing. All original schema, strict, term and reference commands passed; those checks did not verify scientific sources.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch071 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007958 | data/merge_yaml/merged/Cornmeal_Agar.yaml | generated | cornmeal_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:007958 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:007958 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:007958 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:007958 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and generated ownership

identity: supported. Targets: CultureMech:007958.

Both complete current records identify TOGO M1420; fresh TOGO meta independently links the exact NBRC page and matching name. The current recipe is a single-owner generated copy. No organism-specific growth claim follows from its category or medium name.

### Complexity and physical state

consistency: supported. Targets: CultureMech:007958.

Agar supports the selected solid formulation. Corn-derived material is compositionally undefined, so COMPLEX/UNDEFINED is supported. Category bacterial is retained as local organization, not a verified strain-growth restriction.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:007958.

6 current concentration fields are covered by 4 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/Cornmeal_Agar.yaml","quantity_field_count":6,"decisions":[{"quantity_id":"q1","label":"Water input","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Both exact sources give 1 L water, not 1 g/L. Preserve an input-volume quantity using schema unit L; do not apply a density conversion or silently equate solvent volume with finished-medium volume.","source_stage":"Recipe input water","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt lines 29-31","quote":"Distilled water\n1\nL","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact 20 g input is supported, but the listed 1 L is water input and neither source states final make-up. The local G_PER_L concentration therefore remains unsupported as a final-medium rate; preserve the batch amount and unresolved denominator.","source_stage":"Recipe batch input","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt lines 32-34","quote":"Agar\n20\ng","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Agar\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\": \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Cornmeal extract","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact 2 g input is supported, but the listed 1 L is water input and neither source states final make-up. The local G_PER_L concentration therefore remains unsupported as a final-medium rate; preserve the batch amount and unresolved denominator.","source_stage":"Recipe batch input","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt lines 26-28","quote":"Cornmeal extract\n2\ng","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Cornmeal extract\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001157\",\n          \"gmo_id\": \"GMO_001157\",\n          \"label\": \"Cornmeal extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Source pH","local_fields":[],"decision":"evidence_only","rationale":"The exact pH is source-supported and absent from both current records. Restore the source value with attached evidence; no temperature, incubation or growth range is inferred.","source_stage":"Source pH","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt lines 35-35","quote":"pH 6.0","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"pH 6.0\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Cornmeal_Agar.yaml":null,"data/normalized_yaml/bacterial/cornmeal_agar.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:007958.

All existing water and agar primary and secondary IDs match current active exact OLS labels and their supplied chemical class. Each document has secondary links on 2 of 3 ingredient instances; exact label validity among those asserted slots is separate from link-presence coverage. The corn-derived mixture or extract is intentionally not forced to a single molecular identifier; current preferred-name MIM lookups and no-match results are explicit in the sidecar.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:007958.

Complete target and owner histories and both October 5 reports were read. Both reports recorded 0/3 source-checked claims and exact current record hashes; they do not authenticate old source retrieval. No attached amount claims exist to credit. Current unit handling and comment retention are improved relative to stored records; current exact formulation matching does not justify rewriting historical execution or replaying imports. Preserve all old events and append new curation.

## Findings

### f1: Input water is misencoded and final-volume basis is unsupported

major / open / confirmed; issue key: culturemech-007958-water-and-amount-basis.

Correct maintained water from 1 G_PER_L to the exact 1 L input. Retain agar 20 g and cornmeal extract 2 g as the source batch inputs until their final-volume basis can be represented honestly. No final make-up is printed, so do not infer an exact final litre from solvent input.

### f2: The exact primary pH is absent

minor / open / confirmed; issue key: culturemech-007958-missing-source-ph.

Add the source pH 6.0 with its exact primary claim to the maintained owner and regenerate the target. Current TOGO _extract_ph reads root ph, whereas this payload stores meta.ph; address that parser boundary without implying that current comment retention is absent.

### f3: Source identity is retained but amount and preparation claims lack evidence

minor / open / confirmed; issue key: culturemech-007958-claim-evidence-gap.

Keep the exact NBRC/TOGO identity and existing history. Attach source-specific literal claims to the maintained ingredient quantities and root preparation context, including unchanged supported input numbers and unresolved concentration bases. The old October report is a derivative review, not a substitute for the fresh source bytes.

## Recommended Actions And Acceptance Checks

### a1

Correct maintained water from 1 G_PER_L to the exact 1 L input. Retain agar 20 g and cornmeal extract 2 g as the source batch inputs until their final-volume basis can be represented honestly. No final make-up is printed, so do not infer an exact final litre from solvent input.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Add the source pH 6.0 with its exact primary claim to the maintained owner and regenerate the target. Current TOGO _extract_ph reads root ph, whereas this payload stores meta.ph; address that parser boundary without implying that current comment retention is absent.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Keep the exact NBRC/TOGO identity and existing history. Attach source-specific literal claims to the maintained ingredient quantities and root preparation context, including unchanged supported input numbers and unresolved concentration bases. The old October report is a derivative review, not a substitute for the fresh source bytes.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| nbrc17 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17; REVIEW_WORK/batch071/source07-08-10/nbrc17.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. |
| currentTogo1420 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420; REVIEW_WORK/batch071/source07-08-10/currentTogo1420.json; exact original raw/text/hash/time metadata | context_only | Exact current provider recipe. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch071/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; REVIEW_WORK/batch071/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/Cornmeal_Agar.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cornmeal_agar.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cornmeal_Agar.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cornmeal_agar.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-togo | src/culturemech/import/togo_importer.py; _parse_unit, _ingredient_from_item, _extract_preparation_steps, _extract_ph, _convert_to_culturemech | context_only | Current _parse_unit maps l to L, unlike the stored water defect. _ingredient_from_item maps bare grams to G_PER_L without establishing final volume. _extract_preparation_steps retains comments, while _extract_ph reads root ph and this actual payload places ph under meta. Current code behavior is distinct from historical execution. |
| historical-reading | REVIEW_WORK/batch071/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch071/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch071/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch071/record08/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| quantities | REVIEW_WORK/batch071/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch071/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch071/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch071/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch071/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch071/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch071/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch071/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch071/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch071/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch071/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The source pages give no organism-specific growth evidence. No strain, temperature, incubation duration, sterilization temperature or product equivalence is inferred.
- COMPLEX/UNDEFINED and existing ingredient labels are retained; an unresolved mixture mapping is not a wrong-ID finding.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T155807Z-culturemech-007958-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Cornmeal Agar'
started_at: '2026-10-28T15:21:37.344891Z'
finished_at: '2026-10-28T15:58:07.333938Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact primary NBRC identity is supported, but water units and concentration
  basis require maintained-owner curation. The source pH is missing. All original
  schema, strict, term and reference commands passed; those checks did not verify
  scientific sources.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/Cornmeal_Agar.yaml
    sha256: 7ab58c442c6080ef2c4ae8d45f92d64a9d1849017f31859458b19459f647812d
    role: target
  - path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    sha256: af6ecec836ce0e7b606161a0ff7f56d85adf16a29e1a01a4c63950b26318c207
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cornmeal_Agar.md
    sha256: f125e0e3e3d649513893dcd89b1a1f52efa85463ce898bef205438f3f18493d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cornmeal_agar.md
    sha256: b1da188a7e17c467cc985facc472c70fa52540d55f906a9f1690d7be5672dcaa
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_j261_variant.py
    sha256: 040fbe3cb823c3f4d15f344869a4a88cdb0605147ee1a0d30a9e161dcd132506
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch071 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007958
targets:
- target_id: CultureMech:007958
  path: data/merge_yaml/merged/Cornmeal_Agar.yaml
  label: cornmeal_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:007958
  command: just validate-schema data/merge_yaml/merged/Cornmeal_Agar.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:007958
  command: just validate-strict data/merge_yaml/merged/Cornmeal_Agar.yaml --out REVIEW_WORK/batch071/record08/strict.tsv
    --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:007958
  command: just validate-terms data/merge_yaml/merged/Cornmeal_Agar.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:007958
  command: just validate-references data/merge_yaml/merged/Cornmeal_Agar.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: nbrc17
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17
  accessed_at: '2026-10-28T15:22:16.090591Z'
  locator: REVIEW_WORK/batch071/source07-08-10/nbrc17.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth.
  snapshot_sha256: 61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06
- evidence_id: currentTogo1420
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420
  accessed_at: '2026-10-28T15:22:15.458579Z'
  locator: REVIEW_WORK/batch071/source07-08-10/currentTogo1420.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current provider recipe.
  snapshot_sha256: 0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T15:22:16.114980Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  accessed_at: '2026-10-28T15:22:16.982634Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Cornmeal_Agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:27:41.288294Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 7ab58c442c6080ef2c4ae8d45f92d64a9d1849017f31859458b19459f647812d
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cornmeal_agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:27:41.288451Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: af6ecec836ce0e7b606161a0ff7f56d85adf16a29e1a01a4c63950b26318c207
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T15:27:41.288478Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T15:27:41.288755Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T15:27:41.288778Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T15:27:41.288797Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cornmeal_Agar.md
  locator: Complete report
  accessed_at: '2026-10-28T15:27:41.288820Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f125e0e3e3d649513893dcd89b1a1f52efa85463ce898bef205438f3f18493d0
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cornmeal_agar.md
  locator: Complete report
  accessed_at: '2026-10-28T15:27:41.288840Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b1da188a7e17c467cc985facc472c70fa52540d55f906a9f1690d7be5672dcaa
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _parse_unit, _ingredient_from_item, _extract_preparation_steps, _extract_ph,
    _convert_to_culturemech
  accessed_at: '2026-10-28T15:27:41.288875Z'
  support: context_only
  summary: Current _parse_unit maps l to L, unlike the stored water defect. _ingredient_from_item
    maps bare grams to G_PER_L without establishing final volume. _extract_preparation_steps
    retains comments, while _extract_ph reads root ph and this actual payload places
    ph under meta. Current code behavior is distinct from historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/historical-reading.json
  accessed_at: '2026-10-28T15:27:41.289529Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 653de878f9981615aed59d65fd13c7907337644bfeeea3b6eb97df93dbdd89a1
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:27:41.289555Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/complete-document-reader.json
  accessed_at: '2026-10-28T15:27:41.289582Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 81dc278c2087c83b2e4c1cbb38d1c7dd109fd6d44441f86ef5b589f2af0387b5
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T15:27:41.289602Z'
  support: context_only
  summary: Current parser excludes percent-stock additions from primary ingredients,
    preserves referenced stock amounts/attributes separately and prioritizes explicit
    provider g_l. It skips source water; bare units alone do not establish a final-volume
    basis. Current code is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T15:27:41.289630Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch071/record08/historical-current-object-joins.json
  accessed_at: '2026-10-28T15:27:41.289651Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: c34c2fecda5a82b3c96b5cbcafeca57d0f61adc06c1e0c7d54c8ad369f4855af
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306847Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 70d513339987cffc0aedf3e4a2ac36003292b8a79b1e04999426d581dc84385f
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306879Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 236df4c034e62541dc52a117214940fcd83f36bd7d2f1649e086f59c0d4f6fee
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306905Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 79a822b1b3291cfe1034c75e401493e0a0fcdd67587207b2fac70ed2b4b63d78
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306931Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: d89006248b9fb007de95f371eee7007328d556bf6de399f69d55271093ea04b7
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306953Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: d0dc521310c4b6e09f6920df13cfca72282e1205bfc3c69e57a9f27477d00cd4
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306972Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 61623fe606a831a51e035e1b456a9cc972887f7d7d251b0867d7212440467ddc
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch071/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:27:41.306989Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch071/record08/schema-result.json
  accessed_at: '2026-10-28T15:21:38.373967Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c70367cd6ca9144dc563499d397c5d67805fa830ad4378359215a0dcd2bc4b49
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch071/record08/strict-result.json
  accessed_at: '2026-10-28T15:21:39.313803Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: cfd745008c859f6e271efb90b5851aa7b22484cb8dc74337e9bf1e49be8e60c1
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch071/record08/terms-result.json
  accessed_at: '2026-10-28T15:21:40.351328Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 5ecc1eebf78c93b5ad21c392cf7e6ad58605ad1cc728e825286a0ad525f7c905
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch071/record08/references-result.json
  accessed_at: '2026-10-28T15:21:40.999997Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 5e05e23708dcd929ec619174bb3c14cbee2680fc7e5295365ffd418274e07316
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and generated ownership
  outcome: supported
  summary: Both complete current records identify TOGO M1420; fresh TOGO meta independently
    links the exact NBRC page and matching name. The current recipe is a single-owner
    generated copy. No organism-specific growth claim follows from its category or
    medium name.
  target_ids:
  - CultureMech:007958
  evidence_ids:
  - target
  - owner
  - currentTogo1420
  - nbrc17
- assessment_id: classification
  area: consistency
  topic: Complexity and physical state
  outcome: supported
  summary: Agar supports the selected solid formulation. Corn-derived material is
    compositionally undefined, so COMPLEX/UNDEFINED is supported. Category bacterial
    is retained as local organization, not a verified strain-growth restriction.
  target_ids:
  - CultureMech:007958
  evidence_ids:
  - target
  - nbrc17
  - chebi2509
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 6 current concentration fields are covered by 4 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:007958
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/Cornmeal_Agar.yaml","quantity_field_count":6,"decisions":[{"quantity_id":"q1","label":"Water
    input","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Both
    exact sources give 1 L water, not 1 g/L. Preserve an input-volume quantity using
    schema unit L; do not apply a density conversion or silently equate solvent volume
    with finished-medium volume.","source_stage":"Recipe input water","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt
    lines 29-31","quote":"Distilled water\n1\nL","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact 20 g input is supported, but the listed 1 L is water input and neither source
    states final make-up. The local G_PER_L concentration therefore remains unsupported
    as a final-medium rate; preserve the batch amount and unresolved denominator.","source_stage":"Recipe
    batch input","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt
    lines 32-34","quote":"Agar\n20\ng","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Agar\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\":
    \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Cornmeal extract","local_fields":[{"path":"data/merge_yaml/merged/Cornmeal_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cornmeal_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact 2 g input is supported, but the listed 1 L is water input and neither source
    states final make-up. The local G_PER_L concentration therefore remains unsupported
    as a final-medium rate; preserve the batch amount and unresolved denominator.","source_stage":"Recipe
    batch input","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt
    lines 26-28","quote":"Cornmeal extract\n2\ng","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Cornmeal extract\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001157\",\n          \"gmo_id\": \"GMO_001157\",\n          \"label\":
    \"Cornmeal extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Source pH","local_fields":[],"decision":"evidence_only","rationale":"The
    exact pH is source-supported and absent from both current records. Restore the
    source value with attached evidence; no temperature, incubation or growth range
    is inferred.","source_stage":"Source pH","sources":[{"evidence_id":"nbrc17","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=17","raw_path":"REVIEW_WORK/batch071/source07-08-10/nbrc17.raw","raw_sha256":"61a096b5b8137f489a3185197978ae793693636a96269c8576c46c7a69496a06","text_sha256":"689edbba0dc24b2366b05d0b3d151fbd141ce231cc8bcb44863594e03f02e89a","accessed_at":"2026-10-28T15:22:16.090591Z","locator":"nbrc17.txt
    lines 35-35","quote":"pH 6.0","quote_basis":"derivative text"},{"evidence_id":"currentTogo1420","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1420","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo1420.raw","raw_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","text_sha256":"0ed8ca35b2ba98a45484811556c0a92fa151a4f231c1a66bbd88eb0b50821da9","accessed_at":"2026-10-28T15:22:15.458579Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"pH 6.0\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Cornmeal_Agar.yaml":null,"data/normalized_yaml/bacterial/cornmeal_agar.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: All existing water and agar primary and secondary IDs match current active
    exact OLS labels and their supplied chemical class. Each document has secondary
    links on 2 of 3 ingredient instances; exact label validity among those asserted
    slots is separate from link-presence coverage. The corn-derived mixture or extract
    is intentionally not forced to a single molecular identifier; current preferred-name
    MIM lookups and no-match results are explicit in the sidecar.
  target_ids:
  - CultureMech:007958
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: Complete target and owner histories and both October 5 reports were read.
    Both reports recorded 0/3 source-checked claims and exact current record hashes;
    they do not authenticate old source retrieval. No attached amount claims exist
    to credit. Current unit handling and comment retention are improved relative to
    stored records; current exact formulation matching does not justify rewriting
    historical execution or replaying imports. Preserve all old events and append
    new curation.
  target_ids:
  - CultureMech:007958
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-007958-water-and-amount-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Input water is misencoded and final-volume basis is unsupported
  description: Correct maintained water from 1 G_PER_L to the exact 1 L input. Retain
    agar 20 g and cornmeal extract 2 g as the source batch inputs until their final-volume
    basis can be represented honestly. No final make-up is printed, so do not infer
    an exact final litre from solvent input.
  target_ids:
  - CultureMech:007958
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  evidence_ids:
  - nbrc17
  - currentTogo1420
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-007958-missing-source-ph
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The exact primary pH is absent
  description: Add the source pH 6.0 with its exact primary claim to the maintained
    owner and regenerate the target. Current TOGO _extract_ph reads root ph, whereas
    this payload stores meta.ph; address that parser boundary without implying that
    current comment retention is absent.
  target_ids:
  - CultureMech:007958
  field_paths:
  - ph_value
  evidence_ids:
  - nbrc17
  - currentTogo1420
  - writer-togo
  rule_id: review-yaml-record/completeness
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained importer
- finding_id: f3
  issue_key: culturemech-007958-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source identity is retained but amount and preparation claims lack evidence
  description: Keep the exact NBRC/TOGO identity and existing history. Attach source-specific
    literal claims to the maintained ingredient quantities and root preparation context,
    including unchanged supported input numbers and unresolved concentration bases.
    The old October report is a derivative review, not a substitute for the fresh
    source bytes.
  target_ids:
  - CultureMech:007958
  field_paths:
  - ingredients
  - evidence
  - curation_history
  evidence_ids:
  - nbrc17
  - currentTogo1420
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
actions:
- action_id: a1
  description: Correct maintained water from 1 G_PER_L to the exact 1 L input. Retain
    agar 20 g and cornmeal extract 2 g as the source batch inputs until their final-volume
    basis can be represented honestly. No final make-up is printed, so do not infer
    an exact final litre from solvent input.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007958
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Add the source pH 6.0 with its exact primary claim to the maintained
    owner and regenerate the target. Current TOGO _extract_ph reads root ph, whereas
    this payload stores meta.ph; address that parser boundary without implying that
    current comment retention is absent.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007958
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained importer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Keep the exact NBRC/TOGO identity and existing history. Attach source-specific
    literal claims to the maintained ingredient quantities and root preparation context,
    including unchanged supported input numbers and unresolved concentration bases.
    The old October report is a derivative review, not a substitute for the fresh
    source bytes.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007958
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cornmeal_agar.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- The source pages give no organism-specific growth evidence. No strain, temperature,
  incubation duration, sterilization temperature or product equivalence is inferred.
- COMPLEX/UNDEFINED and existing ingredient labels are retained; an unresolved mixture
  mapping is not a wrong-ID finding.
- No strain-growth claim, optimization or experimental recommendation is inferred
  from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent
  rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed
  only on their declared normalization basis; unspecified percent bases and hydrate
  numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was
  performed by this author.
```
