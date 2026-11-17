# Scientific review: CC

- Review: 20261028T081519Z-culturemech-001250-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:45:08.081968Z
- Finished UTC: 2026-10-28T08:15:19.476128Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Partial source review of CC: exact1817 identity and four batch-mass rows are recovered, while KG102 is a different medium. Final-volume normalization and premix/alternative details remain unresolved. Current source bytes, exact ontology/MIM lookups, all8 local concentration fields and all four canonical diagnostics are retained; no record edits were made.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch060 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001250 | data/merge_yaml/merged/CC.yaml | generated | cc |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001250 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001250 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001250 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001250 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and cross-reference

identity: concern. Targets: CultureMech:001250.

DSMZ/MediaDive1817 and CC identify the selected record; asserted KG102 identifies another medium. Czapek-Dox product identity and the explicit alternative substrate remain bounded source descriptions.

### Native shape and owner routing

schema: supported. Targets: CultureMech:001250.

Generated CC resolves to one maintained cc owner; schema and strict checks passed. The present singleton merger copies its source and does not infer source identity.

### Source controls and classification

completeness: unknown. Targets: CultureMech:001250.

Complex/undefined and solid agar classification is consistent with the listed premix and agar. API1817 supplies no pH, atmosphere, temperature, solvent row, sterilization steps or strain-specific growth evidence; the attempted DSM PDF route is unavailable. These omissions do not justify invented protocol defaults or a target organism.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001250.

8 current concentration fields are covered by 5 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b060-quantity-inventory-v1","target":"data/merge_yaml/merged/CC.yaml","quantity_field_count":8,"decisions":[{"quantity_id":"q1","label":"Czapek-Dox liquid medium","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[0].concentration","stored":{"value":"35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[0].concentration","stored":{"value":"35","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact API1817 batch mass and ingredient wording agree with the stored numeric value. The provider declares solution volume1000, but gives no explicit final-volume statement, solvent row or g_l rate. This supports the nominal provider batch mass, not independently verified final-medium G_PER_L. No alternative amount or conversion is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Czapek-Dox liquid medium\",\n                        \"compound_id\": 1610,\n                        \"amount\": 35,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Cellobiose or Cellulose MN 300","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact API1817 batch mass and ingredient wording agree with the stored numeric value. The provider declares solution volume1000, but gives no explicit final-volume statement, solvent row or g_l rate. This supports the nominal provider batch mass, not independently verified final-medium G_PER_L. No alternative amount or conversion is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Cellobiose or Cellulose MN 300\",\n                        \"compound_id\": 1627,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact API1817 batch mass and ingredient wording agree with the stored numeric value. The provider declares solution volume1000, but gives no explicit final-volume statement, solvent row or g_l rate. This supports the nominal provider batch mass, not independently verified final-medium G_PER_L. No alternative amount or conversion is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact API1817 batch mass and ingredient wording agree with the stored numeric value. The provider declares solution volume1000, but gives no explicit final-volume statement, solvent row or g_l rate. This supports the nominal provider batch mass, not independently verified final-medium G_PER_L. No alternative amount or conversion is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Provider main-solution volume","local_fields":[],"decision":"evidence_only","rationale":"The declared1000 provider volume is retained as source context. It is not a locally stated water dose, measured final volume, or permission to invent a makeup step.","source_stage":"Provider solution metadata only","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CC.yaml":null,"data/normalized_yaml/bacterial/cc.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001250.

Fresh OLS confirms CHEBI131527 as dipotassium hydrogen phosphate (HO4P.2K) and CHEBI2509 as agar, with exact asserted labels on all8 primary/secondary slots across two documents. No hydrate is claimed by the source K2HPO4 row, so synonym variants do not change it. Two of four ingredient instances in each document have current secondary links (50%); agreement among those links is separate from supplied-form/source support. The premix and explicit alternative are not forced to narrow chemical IDs.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:001250.

All four exact historical reports were read. October5 reports performed no source checks; October7 retained unresolved claims and unchanged bytes. September22 already identified the KG102 conflict and treated provider volume as sufficient normalization; this review independently confirms identity but keeps final-volume uncertainty explicit. The exact historical parent is retained as decoded ancestry; no historical command is replayed and no original retrieval timestamp is assigned to the fresh capture. Current importer already separates stock references and reads only the primary formulation, yet its bare g→G_PER_L fallback remains insufficient proof of a final-volume basis. Current conservative merger behavior is credited.

## Findings

### f1: KG cross-reference denotes a different medium

major / open / confirmed; issue key: culturemech-001250-wrong-kg-crossreference.

Both target and exact maintained owner assert mediadive.medium:102. Fresh API102 identifies FLAVOBACTERIUM AQUATILE MEDIUM, whereas the exact source accession1817 identifies CC. This is a confirmed external identity conflict; it is not resolved by a partial ingredient overlap. Reconcile only the maintained kg_microbe_match assertion against exact CC identity, without automatically assigning1817 as a KG node or importing102 preparation. Append any actual curation event and regenerate the singleton target.

### f2: Source evidence and denominator limits are absent from maintained quantities

major / open / confirmed; issue key: culturemech-001250-source-basis-evidence.

The four maintained ingredient concentrations have no attached source evidence. Fresh API1817 supports their batch masses and literal component wording, but provides no explicit final-volume instruction or g_l rate. Retain the unresolved G_PER_L interpretation, source version and exact rows; do not silently endorse the September report normalization or substitute a guessed solvent quantity. The Czapek-Dox premix has no inspected brand/component formulation, and the source explicitly permits cellobiose OR Cellulose MN300; preserve this disjunction rather than ground it as one compound or use both simultaneously.

## Recommended Actions And Acceptance Checks

### a1

Both target and exact maintained owner assert mediadive.medium:102. Fresh API102 identifies FLAVOBACTERIUM AQUATILE MEDIUM, whereas the exact source accession1817 identifies CC. This is a confirmed external identity conflict; it is not resolved by a partial ingredient overlap. Reconcile only the maintained kg_microbe_match assertion against exact CC identity, without automatically assigning1817 as a KG node or importing102 preparation. Append any actual curation event and regenerate the singleton target.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The four maintained ingredient concentrations have no attached source evidence. Fresh API1817 supports their batch masses and literal component wording, but provides no explicit final-volume instruction or g_l rate. Retain the unresolved G_PER_L interpretation, source version and exact rows; do not silently endorse the September report normalization or substitute a guessed solvent quantity. The Czapek-Dox premix has no inspected brand/component formulation, and the source explicitly permits cellobiose OR Cellulose MN300; preserve this disjunction rather than ground it as one compound or use both simultaneously.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| api1817 | https://mediadive.dsmz.de/rest/medium/1817; REVIEW_WORK/batch060/source07-09/api1817.json; exact original raw/text/hash/time metadata | context_only | Exact CC provider identity and declared recipe basis; source g_l is a provider normalization. |
| api102 | https://mediadive.dsmz.de/rest/medium/102; REVIEW_WORK/batch060/source07-09/api102.json; exact original raw/text/hash/time metadata | context_only | Identity-only comparison for asserted kg_microbe_match102; do not transfer its formulation or growth scope. |
| dsm1817 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1817.pdf; REVIEW_WORK/batch060/source07-09/dsm1817.json; exact original raw/text/hash/time metadata | context_only | Exact CC medium1817 primary formulation and printed preparation; no strain-growth inference. |
| target | data/merge_yaml/merged/CC.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cc.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cc.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CC.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cc.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/yaml_record_review/20260922T062655Z-CC.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit | context_only | Current parser reads only the primary recipe, separates referenced solutions and percentage/ml additions, and preserves their source attributes. It prefers explicit g_l but otherwise maps bare mass/volume units to per-litre schema units. This credits existing stage handling without certifying a source final volume or historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current duplicate cleanup collapses identical values but flags conflicting values without summing. Earlier sums require source-stage curation; do not rerun cleanup as a substitute for scientific reconciliation. |
| writer-kg | scripts/enrich_with_kg_microbe_matches.py; enrich_recipe_with_kg_match; complete function and main read | context_only | Current enrichment delegates ingredient matching and writes only a returned match, appending history. The inspected owner has no matching enrichment event; this code does not prove how the existing wrong102 assertion was introduced. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch060/source07-09/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/formula and scientific annotations for ordinary record07 only. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch060/source07-09/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/formula and scientific annotations for ordinary record07 only. |
| quantities | REVIEW_WORK/batch060/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch060/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch060/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch060/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch060/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch060/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch060/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch060/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch060/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch060/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch060/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Current canonical checks validate encoded structure/labels; zero reference checks do not verify external source claims.
- The requested primary PDF route returned HTTP404; the complete current API1817 payload was read. No visual PDF reading is claimed. Current source status, retrieval times and raw/text bytes remain in the capture catalog.
- Partial scientific review: exact current API content is available, but the DSM1817 PDF request returned404 and no authenticated manufacturer formulation for the named Czapek-Dox product was captured.
- Provider1000 solution volume supports a nominal batch context only. No preparation procedure, final makeup, measured final volume or growth association was inferred.
- Historical reports are derivative observations. Their numeric decisions are independently reassessed here; no terminal disposition of prior structured findings or historical validation success is asserted.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T081519Z-culturemech-001250-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CC'
started_at: '2026-10-28T07:45:08.081968Z'
finished_at: '2026-10-28T08:15:19.476128Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Partial source review of CC: exact1817 identity and four batch-mass rows
  are recovered, while KG102 is a different medium. Final-volume normalization and
  premix/alternative details remain unresolved. Current source bytes, exact ontology/MIM
  lookups, all8 local concentration fields and all four canonical diagnostics are
  retained; no record edits were made.'
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
  - path: data/merge_yaml/merged/CC.yaml
    sha256: af9b5bb47b924dc132fb0425837ad1d039e267723f4f55b44c575e730d0e7723
    role: target
  - path: data/normalized_yaml/bacterial/cc.yaml
    sha256: 30ccf0a48bbe19b43545c2761602e4348299fbd08dd077f2a01bb07e2ddd3406
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cc.yaml.md
    sha256: afcca9f9afa769c20da0efd835e5dc2ece0de79ef19eec63c3456778a9e49c11
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CC.md
    sha256: 1395639d872f2cd0a571e906e8ae3f979d81d1836d8d5a9d30b3fd32b7825482
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cc.md
    sha256: 7b2b3a98986c800825e5635f9c48fa95bca242bb5330117e51fb9f9b0f709d5e
    role: context
  - path: reports/yaml_record_review/20260922T062655Z-CC.md
    sha256: a8252a297b1cad57abd9b21d8376b5efb5574f13a7ce0952ca1477a43032d03f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
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
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/fix_mediadb_leading_compounds.py
    sha256: 2b3b6adfdb298b51b6d87a30151b4f530ac5cd1726fb3763ce7c9fe07cfec729
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_mediadb_names.py
    sha256: 56ad322b70927ac6dff2de12c63d7bfc640d72a6c2521b55293a788ac3cca4c5
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
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
  selection: Authoritative batch060 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001250
targets:
- target_id: CultureMech:001250
  path: data/merge_yaml/merged/CC.yaml
  label: cc
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cc.yaml
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
  - CultureMech:001250
  command: just validate-schema data/merge_yaml/merged/CC.yaml
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
  - CultureMech:001250
  command: just validate-strict data/merge_yaml/merged/CC.yaml --out REVIEW_WORK/batch060/record07/strict.tsv
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
  - CultureMech:001250
  command: just validate-terms data/merge_yaml/merged/CC.yaml
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
  - CultureMech:001250
  command: just validate-references data/merge_yaml/merged/CC.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: api1817
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1817
  accessed_at: '2026-10-28T07:45:40.645097Z'
  locator: REVIEW_WORK/batch060/source07-09/api1817.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact CC provider identity and declared recipe basis; source g_l is a provider
    normalization.
  snapshot_sha256: a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4
- evidence_id: api102
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/102
  accessed_at: '2026-10-28T07:45:40.629132Z'
  locator: REVIEW_WORK/batch060/source07-09/api102.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Identity-only comparison for asserted kg_microbe_match102; do not transfer
    its formulation or growth scope.
  snapshot_sha256: e5a4a1e76a49e0b3977733e352e0cb342eafee8538e243931b3a9722003bb4c5
- evidence_id: dsm1817
  kind: search
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1817.pdf
  accessed_at: '2026-10-28T07:45:40.651112Z'
  locator: REVIEW_WORK/batch060/source07-09/dsm1817.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact CC medium1817 primary formulation and printed preparation; no strain-growth
    inference.
  snapshot_sha256: bf2c2f5fca024514f0fdd5df876d3ea991fcc84119f559ab5d8855db9582f93c
  search_scope: One exact public GET of https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1817.pdf;
    retained status 404. No exhaustive repository or literature absence claim.
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CC.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:48:37.546938Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: af9b5bb47b924dc132fb0425837ad1d039e267723f4f55b44c575e730d0e7723
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cc.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:48:37.547126Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 30ccf0a48bbe19b43545c2761602e4348299fbd08dd077f2a01bb07e2ddd3406
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T07:48:37.547158Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T07:48:37.547479Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T07:48:37.547505Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T07:48:37.547527Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:48:37.547554Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cc.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:48:37.553609Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: afcca9f9afa769c20da0efd835e5dc2ece0de79ef19eec63c3456778a9e49c11
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CC.md
  locator: Complete report
  accessed_at: '2026-10-28T07:48:37.553669Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 1395639d872f2cd0a571e906e8ae3f979d81d1836d8d5a9d30b3fd32b7825482
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cc.md
  locator: Complete report
  accessed_at: '2026-10-28T07:48:37.553697Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 7b2b3a98986c800825e5635f9c48fa95bca242bb5330117e51fb9f9b0f709d5e
- evidence_id: report-20
  kind: prior_review
  reference: reports/yaml_record_review/20260922T062655Z-CC.md
  locator: Complete report
  accessed_at: '2026-10-28T07:48:37.553720Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a8252a297b1cad57abd9b21d8376b5efb5574f13a7ce0952ca1477a43032d03f
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit
  accessed_at: '2026-10-28T07:48:37.553746Z'
  support: context_only
  summary: Current parser reads only the primary recipe, separates referenced solutions
    and percentage/ml additions, and preserves their source attributes. It prefers
    explicit g_l but otherwise maps bare mass/volume units to per-litre schema units.
    This credits existing stage handling without certifying a source final volume
    or historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T07:48:37.553786Z'
  support: context_only
  summary: Current duplicate cleanup collapses identical values but flags conflicting
    values without summing. Earlier sums require source-stage curation; do not rerun
    cleanup as a substitute for scientific reconciliation.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-kg
  kind: record_content
  reference: scripts/enrich_with_kg_microbe_matches.py
  locator: enrich_recipe_with_kg_match; complete function and main read
  accessed_at: '2026-10-28T07:48:37.607600Z'
  support: context_only
  summary: Current enrichment delegates ingredient matching and writes only a returned
    match, appending history. The inspected owner has no matching enrichment event;
    this code does not prove how the existing wrong102 assertion was introduced.
  snapshot_sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T07:45:40.767709Z'
  locator: REVIEW_WORK/batch060/source07-09/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/formula and scientific annotations for ordinary
    record07 only.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T07:45:40.779363Z'
  locator: REVIEW_WORK/batch060/source07-09/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/formula and scientific annotations for ordinary
    record07 only.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631518Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: e4af3dd2a54a733210a45bedfcb37730aa04456e7fac9a8933fc56979d79e216
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631550Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 09fd20b7ca9f1bad03c83e0ee2c49225eb974b1b317c15fbf7a171bda0b1fad0
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631579Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 8b5392f1f1fa3f904053276e648ff978fcbc7541216337ef05d4918f64ededdc
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631604Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 6d42a6dbd375a2742931cca30e99cbd8c6af98bdc0ae421b8d78b0f37a3a6a53
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631627Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: f96a5b870b993b93de2fa726e315ea762e0a26330a0502f0775bfe4ea629921f
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631646Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 9381be18da3c99aac611b964171b8737262694c1b548652bd53f59603c43064e
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch060/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:48:37.631666Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record07/schema-result.json
  accessed_at: '2026-10-28T07:45:09.387821Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0390d58253ad7fbae799f4cdf372d5bd52fc90131ad41ca31778574bd52abf68
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record07/strict-result.json
  accessed_at: '2026-10-28T07:45:10.324671Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: d571d0a8425d26b4ea2f66c3fd88370324e3d02293115060de44c2738f3938f8
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record07/terms-result.json
  accessed_at: '2026-10-28T07:45:11.726483Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: bced6f3d06e6dc59552ba7d2fdc1f1b95b6c6016ce5b54fc4da29ebf3e8b240b
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch060/record07/references-result.json
  accessed_at: '2026-10-28T07:45:12.451152Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 6a7601cfa87e8e83804b1fc9ddd389f10ef168ce3cad2ced4a9a45d35b72a18d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and cross-reference
  outcome: concern
  summary: DSMZ/MediaDive1817 and CC identify the selected record; asserted KG102
    identifies another medium. Czapek-Dox product identity and the explicit alternative
    substrate remain bounded source descriptions.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - api1817
  - api102
  - target
  - owner
- assessment_id: structure
  area: schema
  topic: Native shape and owner routing
  outcome: supported
  summary: Generated CC resolves to one maintained cc owner; schema and strict checks
    passed. The present singleton merger copies its source and does not infer source
    identity.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - target
  - owner
  - writer-merger
- assessment_id: preparation
  area: completeness
  topic: Source controls and classification
  outcome: unknown
  summary: Complex/undefined and solid agar classification is consistent with the
    listed premix and agar. API1817 supplies no pH, atmosphere, temperature, solvent
    row, sterilization steps or strain-specific growth evidence; the attempted DSM
    PDF route is unavailable. These omissions do not justify invented protocol defaults
    or a target organism.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - api1817
  - dsm1817
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 8 current concentration fields are covered by 5 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b060-quantity-inventory-v1","target":"data/merge_yaml/merged/CC.yaml","quantity_field_count":8,"decisions":[{"quantity_id":"q1","label":"Czapek-Dox
    liquid medium","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[0].concentration","stored":{"value":"35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[0].concentration","stored":{"value":"35","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact API1817 batch mass and ingredient wording agree with the stored numeric
    value. The provider declares solution volume1000, but gives no explicit final-volume
    statement, solvent row or g_l rate. This supports the nominal provider batch mass,
    not independently verified final-medium G_PER_L. No alternative amount or conversion
    is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator
    unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Czapek-Dox liquid medium\",\n                        \"compound_id\":
    1610,\n                        \"amount\": 35,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Cellobiose or
    Cellulose MN 300","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact API1817 batch mass and ingredient wording agree with the stored numeric
    value. The provider declares solution volume1000, but gives no explicit final-volume
    statement, solvent row or g_l rate. This supports the nominal provider batch mass,
    not independently verified final-medium G_PER_L. No alternative amount or conversion
    is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator
    unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Cellobiose or Cellulose MN 300\",\n                        \"compound_id\":
    1627,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact API1817 batch mass and ingredient wording agree with the stored numeric
    value. The provider declares solution volume1000, but gives no explicit final-volume
    statement, solvent row or g_l rate. This supports the nominal provider batch mass,
    not independently verified final-medium G_PER_L. No alternative amount or conversion
    is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator
    unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CC.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cc.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact API1817 batch mass and ingredient wording agree with the stored numeric
    value. The provider declares solution volume1000, but gives no explicit final-volume
    statement, solvent row or g_l rate. This supports the nominal provider batch mass,
    not independently verified final-medium G_PER_L. No alternative amount or conversion
    is proposed.","source_stage":"Main sol.1817 provider batch; final-medium denominator
    unresolved","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Provider main-solution
    volume","local_fields":[],"decision":"evidence_only","rationale":"The declared1000
    provider volume is retained as source context. It is not a locally stated water
    dose, measured final volume, or permission to invent a makeup step.","source_stage":"Provider
    solution metadata only","sources":[{"evidence_id":"api1817","reference":"https://mediadive.dsmz.de/rest/medium/1817","raw_path":"REVIEW_WORK/batch060/source07-09/api1817.raw","raw_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","text_sha256":"a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4","accessed_at":"2026-10-28T07:45:40.645097Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CC.yaml":null,"data/normalized_yaml/bacterial/cc.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Fresh OLS confirms CHEBI131527 as dipotassium hydrogen phosphate (HO4P.2K)
    and CHEBI2509 as agar, with exact asserted labels on all8 primary/secondary slots
    across two documents. No hydrate is claimed by the source K2HPO4 row, so synonym
    variants do not change it. Two of four ingredient instances in each document have
    current secondary links (50%); agreement among those links is separate from supplied-form/source
    support. The premix and explicit alternative are not forced to narrow chemical
    IDs.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All four exact historical reports were read. October5 reports performed
    no source checks; October7 retained unresolved claims and unchanged bytes. September22
    already identified the KG102 conflict and treated provider volume as sufficient
    normalization; this review independently confirms identity but keeps final-volume
    uncertainty explicit. The exact historical parent is retained as decoded ancestry;
    no historical command is replayed and no original retrieval timestamp is assigned
    to the fresh capture. Current importer already separates stock references and
    reads only the primary formulation, yet its bare g→G_PER_L fallback remains insufficient
    proof of a final-volume basis. Current conservative merger behavior is credited.
  target_ids:
  - CultureMech:001250
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-001250-wrong-kg-crossreference
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: KG cross-reference denotes a different medium
  description: Both target and exact maintained owner assert mediadive.medium:102.
    Fresh API102 identifies FLAVOBACTERIUM AQUATILE MEDIUM, whereas the exact source
    accession1817 identifies CC. This is a confirmed external identity conflict; it
    is not resolved by a partial ingredient overlap. Reconcile only the maintained
    kg_microbe_match assertion against exact CC identity, without automatically assigning1817
    as a KG node or importing102 preparation. Append any actual curation event and
    regenerate the singleton target.
  target_ids:
  - CultureMech:001250
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - api1817
  - api102
  - target
  - owner
  - writer-kg
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cc.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001250-source-basis-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Source evidence and denominator limits are absent from maintained quantities
  description: The four maintained ingredient concentrations have no attached source
    evidence. Fresh API1817 supports their batch masses and literal component wording,
    but provides no explicit final-volume instruction or g_l rate. Retain the unresolved
    G_PER_L interpretation, source version and exact rows; do not silently endorse
    the September report normalization or substitute a guessed solvent quantity. The
    Czapek-Dox premix has no inspected brand/component formulation, and the source
    explicitly permits cellobiose OR Cellulose MN300; preserve this disjunction rather
    than ground it as one compound or use both simultaneously.
  target_ids:
  - CultureMech:001250
  field_paths:
  - ingredients
  - references
  evidence_ids:
  - api1817
  - dsm1817
  - quantities
  - owner
  rule_id: review-yaml-record/evidence
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cc.yaml
    role: maintained source
actions:
- action_id: a1
  description: Both target and exact maintained owner assert mediadive.medium:102.
    Fresh API102 identifies FLAVOBACTERIUM AQUATILE MEDIUM, whereas the exact source
    accession1817 identifies CC. This is a confirmed external identity conflict; it
    is not resolved by a partial ingredient overlap. Reconcile only the maintained
    kg_microbe_match assertion against exact CC identity, without automatically assigning1817
    as a KG node or importing102 preparation. Append any actual curation event and
    regenerate the singleton target.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001250
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cc.yaml
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
  description: The four maintained ingredient concentrations have no attached source
    evidence. Fresh API1817 supports their batch masses and literal component wording,
    but provides no explicit final-volume instruction or g_l rate. Retain the unresolved
    G_PER_L interpretation, source version and exact rows; do not silently endorse
    the September report normalization or substitute a guessed solvent quantity. The
    Czapek-Dox premix has no inspected brand/component formulation, and the source
    explicitly permits cellobiose OR Cellulose MN300; preserve this disjunction rather
    than ground it as one compound or use both simultaneously.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001250
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cc.yaml
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
- Current canonical checks validate encoded structure/labels; zero reference checks
  do not verify external source claims.
- The requested primary PDF route returned HTTP404; the complete current API1817 payload
  was read. No visual PDF reading is claimed. Current source status, retrieval times
  and raw/text bytes remain in the capture catalog.
- 'Partial scientific review: exact current API content is available, but the DSM1817
  PDF request returned404 and no authenticated manufacturer formulation for the named
  Czapek-Dox product was captured.'
- Provider1000 solution volume supports a nominal batch context only. No preparation
  procedure, final makeup, measured final volume or growth association was inferred.
- Historical reports are derivative observations. Their numeric decisions are independently
  reassessed here; no terminal disposition of prior structured findings or historical
  validation success is asserted.
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
