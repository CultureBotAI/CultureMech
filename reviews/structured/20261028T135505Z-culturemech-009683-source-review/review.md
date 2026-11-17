# Scientific review: Cgya medium

- Review: 20261028T135505Z-culturemech-009683-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:46:07.720543Z
- Finished UTC: 2026-10-28T13:55:05.014820Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Partial source review: one major water-unit defect and two minor evidence/linkage gaps. The three explicit solute rates, glycerol repair and complex liquid classification are supported. The source primary bibliography remains unresolved; no strain-growth relationship or replacement formulation is inferred.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch069 index 08
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009683 | data/merge_yaml/merged/Cgya_medium.yaml | generated | cgya_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009683 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009683 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009683 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009683 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and maintained contributor

identity: supported. Targets: CultureMech:009683.

CM009683, cgya_medium.yaml and TOGO M3250 agree on identity. DSM6575 is Sphaerotilus natans subsp. natans; that corroborates only the source comment identity, not a new growth assertion. No agar is specified in the inspected M3250 formulation, and none is inferred from the acronym.

### Mixture and physical-state classification

representation: supported. Targets: CultureMech:009683.

LIQUID is compatible with the four listed components; the source contains no agar. COMPLEX/UNDEFINED is appropriate to yeast extract and Casitone. No pH, sterilization cycle, or additional stock is invented where the inspected source does not specify it.

### Native checks and source limits

schema: supported. Targets: CultureMech:009683.

The original four canonical commands passed. Strict reports zero errors and references checked zero entries; these diagnostics do not authenticate concentration sources or establish complete bibliographic provenance.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009683.

8 current concentration fields are covered by 5 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b069-quantity-inventory-v1","target":"data/merge_yaml/merged/Cgya_medium.yaml","quantity_field_count":8,"decisions":[{"quantity_id":"q1","label":"Water input","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact TOGO row is 1 L of input water, not 1 g/L. Preserve L and do not infer measured final volume from water alone.","source_stage":"Listed input water","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current numerical g/L rate agrees with the explicit L−1 formulation in the source comment and the matching component row. No attached concentration claim exists locally, so this is evidence_only rather than verified. No inferred water denominator or glycerol density conversion is used.","source_stage":"Source explicitly stated solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig, Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g yeast extract L−1) (Nierman &amp; Maglott, 1989) under aerobic conditions at 30 °C for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Glycerol","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current numerical g/L rate agrees with the explicit L−1 formulation in the source comment and the matching component row. No attached concentration claim exists locally, so this is evidence_only rather than verified. No inferred water denominator or glycerol density conversion is used.","source_stage":"Source explicitly stated solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Glycerol\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001083\",\n          \"gmo_id\": \"GMO_001083\",\n          \"label\": \"Glycerol\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig, Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g yeast extract L−1) (Nierman &amp; Maglott, 1989) under aerobic conditions at 30 °C for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Casitone","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current numerical g/L rate agrees with the explicit L−1 formulation in the source comment and the matching component row. No attached concentration claim exists locally, so this is evidence_only rather than verified. No inferred water denominator or glycerol density conversion is used.","source_stage":"Source explicitly stated solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"Casitone\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001104\",\n          \"gmo_id\": \"GMO_001104\",\n          \"label\": \"Bacto &amp;trade; Casitone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig, Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g yeast extract L−1) (Nierman &amp; Maglott, 1989) under aerobic conditions at 30 °C for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Source-only scoped pre-growth context","local_fields":[],"decision":"evidence_only","rationale":"The source describes one pre-growth experiment for S. natans DSM6575T, not universal growth support for the medium. Preserve the source citation/context without asserting a new target-organism growth relationship or substituting collection conditions.","source_stage":"TOGO comment; experiment-specific, not a general recipe condition","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig, Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g yeast extract L−1) (Nierman &amp; Maglott, 1989) under aerobic conditions at 30 °C for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Cgya_medium.yaml":null,"data/normalized_yaml/bacterial/cgya_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009683.

All four existing target/owner CHEBI slots per layer (water and glycerol primary/secondary) resolve to active exact canonical labels and appropriate supplied identity. Glycerol regrounding is retained. Secondary linkage is 2/4 ingredient instances per layer; agreement among the two existing secondary slots is exact. MIM contains both mapped and rejected name variants, so name membership is not automatic approval. The two unlinked complex ingredients require bounded source/product review, not guessed molecule mappings.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:009683.

Both complete October5 reports marked all four concentrations unreviewed; those are derivative historical diagnostics, not fresh source evidence. Full target/owner histories are preserved, including the current glycerol repair. The owner and generated formulation agree; current conservative merging copies singleton sources and does not establish scientific validity. No original TOGO import payload or Nierman/Maglott publication has been authenticated.

## Findings

### f1: Input water is represented as a mass concentration

major / open / confirmed; issue key: culturemech-009683-water-unit.

The target and maintained owner encode the listed 1 L water input as 1 G_PER_L. Correct the maintained water unit to the source input-volume representation and attach the exact row; retain the separately explicit solute rates without deriving a measured final volume. Current _parse_unit already maps l to L, so this is retained-record staleness rather than evidence that the current parser still makes this exact unit error.

### f2: Source bibliography and claim-level support are incomplete

minor / open / confirmed; issue key: culturemech-009683-source-context.

TOGO M3250 matches the four ingredient names and explicit solute rates. Its comment includes a scoped S. natans DSM6575T pre-growth statement and an incomplete Nierman &amp; Maglott (1989) citation; meta.src_url is empty. Neither layer retains that context or narrow concentration evidence. Attach the exact component/comment claims and resolve the primary bibliographic identity before certifying the experimental association. The DSM6575 collection page confirms the named organism/strain identity only; its other media are not substitutes for CGYA.

### f3: Two complex ingredient names have no secondary linkage

minor / open / confirmed; issue key: culturemech-009683-secondary-link-coverage.

Water and glycerol have current exact CHEBI labels and secondary keys. Yeast extract and Casitone remain unlinked: the current MIM snapshot has exact preferred-name rows, but those rows alone do not authenticate a particular product or chemical mixture. Review those bounded linkage candidates against exact source identity rather than assigning a single-molecule CHEBI term.

## Recommended Actions And Acceptance Checks

### a1

The target and maintained owner encode the listed 1 L water input as 1 G_PER_L. Correct the maintained water unit to the source input-volume representation and attach the exact row; retain the separately explicit solute rates without deriving a measured final volume. Current _parse_unit already maps l to L, so this is retained-record staleness rather than evidence that the current parser still makes this exact unit error.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

TOGO M3250 matches the four ingredient names and explicit solute rates. Its comment includes a scoped S. natans DSM6575T pre-growth statement and an incomplete Nierman &amp; Maglott (1989) citation; meta.src_url is empty. Neither layer retains that context or narrow concentration evidence. Attach the exact component/comment claims and resolve the primary bibliographic identity before certifying the experimental association. The DSM6575 collection page confirms the named organism/strain identity only; its other media are not substitutes for CGYA.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Water and glycerol have current exact CHEBI labels and secondary keys. Yeast extract and Casitone remain unlinked: the current MIM snapshot has exact preferred-name rows, but those rows alone do not authenticate a particular product or chemical mixture. Review those bounded linkage candidates against exact source identity rather than assigning a single-molecule CHEBI term.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo3250full | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250; REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.json; exact original raw/text/hash/time metadata | context_only | Exact TOGO3250 structured endpoint; organism/source identity screened before assessment. Earlier guessed /rest/medium route is not recipe evidence. |
| togo3250 | https://togomedium.org/rest/medium/M3250; REVIEW_WORK/batch069/source07-08-10/togo3250.json; exact original raw/text/hash/time metadata | context_only | Exact ordinary08 source; inspect source identity before further acquisition. |
| dsm6575identity | https://www.dsmz.de/collection/catalogue/details/culture/DSM-6575; REVIEW_WORK/batch069/source07-08-10-supplement/dsm6575identity.json; exact original raw/text/hash/time metadata | context_only | Exact DSM6575 collection identity only; cultivation recommendations on this page are not transferred to CGYA. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch069/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17754; REVIEW_WORK/batch069/source07-08-10/chebi17754.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| target | data/merge_yaml/merged/Cgya_medium.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cgya_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cgya_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgya_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _extract_primary_components, _parse_unit, _extract_preparation_steps, _convert_to_culturemech | context_only | Current primary-section extraction keeps source stages, _parse_unit maps l to L, and _extract_preparation_steps retains nonempty comments. The current code is not the historical import implementation; a comment can contain scoped experiment prose rather than a universal preparation instruction. |
| writer-grounding | scripts/migrate_chebi_regrounding.py; Complete glycerol conditional correction | context_only | The current glycerol correction and exact retained CHEBI17754 are credited; current code does not prove an older execution. |
| historical-reading | REVIEW_WORK/batch069/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch069/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch069/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch069/record08/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| quantities | REVIEW_WORK/batch069/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch069/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch069/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch069/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch069/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch069/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch069/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch069/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch069/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch069/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch069/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Completion is partial because the full primary citation underlying the TOGO comment is unresolved. TOGO supports the explicitly quoted claims, but does not authenticate the original experimental paper or its complete variant scope.
- The earlier guessed TOGO /rest/medium/M3250 route returned an application shell with HTTP200; it is retained as an unsuccessful source lead. The separately captured structured endpoint is the inspected source.
- The DSM6575 page is used only for collection identity. Its cultivation media/conditions are not transferred to this record. The source comment supports a bounded description of a past pre-growth context, not an automatic culture recommendation.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T135505Z-culturemech-009683-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Cgya medium'
started_at: '2026-10-28T13:46:07.720543Z'
finished_at: '2026-10-28T13:55:05.014820Z'
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
summary: 'Partial source review: one major water-unit defect and two minor evidence/linkage
  gaps. The three explicit solute rates, glycerol repair and complex liquid classification
  are supported. The source primary bibliography remains unresolved; no strain-growth
  relationship or replacement formulation is inferred.'
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
  - path: data/merge_yaml/merged/Cgya_medium.yaml
    sha256: c2f6de6ac22c7568999f91b6b5f52f548e04b5046b6108835cae0799f65660f0
    role: target
  - path: data/normalized_yaml/bacterial/cgya_medium.yaml
    sha256: 99c9290444bcfc9753c10c0727e96bc52b47c038e068a36fbdcfece3c7c66467
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cgya_medium.md
    sha256: 3d5972e691818b27805710f23ec2d52dfd6110f3f67abe132d8862efe164eebc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgya_medium.md
    sha256: ac4c7696a518b6a12b1d7bcbf060846baeb7e4d5b3f174a1adc19b53c4bb2c76
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
  selection: Authoritative batch069 index 08
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009683
targets:
- target_id: CultureMech:009683
  path: data/merge_yaml/merged/Cgya_medium.yaml
  label: cgya_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
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
  - CultureMech:009683
  command: just validate-schema data/merge_yaml/merged/Cgya_medium.yaml
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
  - CultureMech:009683
  command: just validate-strict data/merge_yaml/merged/Cgya_medium.yaml --out REVIEW_WORK/batch069/record08/strict.tsv
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
  - CultureMech:009683
  command: just validate-terms data/merge_yaml/merged/Cgya_medium.yaml
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
  - CultureMech:009683
  command: just validate-references data/merge_yaml/merged/Cgya_medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo3250full
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250
  accessed_at: '2026-10-28T13:47:34.803439Z'
  locator: REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Exact TOGO3250 structured endpoint; organism/source identity screened before
    assessment. Earlier guessed /rest/medium route is not recipe evidence.
  snapshot_sha256: e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23
- evidence_id: togo3250
  kind: database
  reference: https://togomedium.org/rest/medium/M3250
  accessed_at: '2026-10-28T13:46:49.530049Z'
  locator: REVIEW_WORK/batch069/source07-08-10/togo3250.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ordinary08 source; inspect source identity before further acquisition.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: dsm6575identity
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-6575
  accessed_at: '2026-10-28T13:53:20.101736Z'
  locator: REVIEW_WORK/batch069/source07-08-10-supplement/dsm6575identity.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Exact DSM6575 collection identity only; cultivation recommendations on
    this page are not transferred to CGYA.
  snapshot_sha256: 69823969b7c960e902e27c2c77e891c6c86196a55889ea18acbc31333c40646c
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T13:46:59.030541Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi17754
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17754
  accessed_at: '2026-10-28T13:47:05.321405Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi17754.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: ca362e6979f6695f1591245af450722b47bc8be8bc23d7d64a39b63034414eaa
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Cgya_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:55:04.990975Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: c2f6de6ac22c7568999f91b6b5f52f548e04b5046b6108835cae0799f65660f0
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cgya_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:55:04.991139Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 99c9290444bcfc9753c10c0727e96bc52b47c038e068a36fbdcfece3c7c66467
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:55:04.991163Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:55:04.991494Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:55:04.991518Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:55:04.991539Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cgya_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:55:04.991565Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 3d5972e691818b27805710f23ec2d52dfd6110f3f67abe132d8862efe164eebc
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgya_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:55:04.991589Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: ac4c7696a518b6a12b1d7bcbf060846baeb7e4d5b3f174a1adc19b53c4bb2c76
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _extract_primary_components, _parse_unit, _extract_preparation_steps,
    _convert_to_culturemech
  accessed_at: '2026-10-28T13:55:04.991615Z'
  support: context_only
  summary: Current primary-section extraction keeps source stages, _parse_unit maps
    l to L, and _extract_preparation_steps retains nonempty comments. The current
    code is not the historical import implementation; a comment can contain scoped
    experiment prose rather than a universal preparation instruction.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-grounding
  kind: record_content
  reference: scripts/migrate_chebi_regrounding.py
  locator: Complete glycerol conditional correction
  accessed_at: '2026-10-28T13:55:04.991651Z'
  support: context_only
  summary: The current glycerol correction and exact retained CHEBI17754 are credited;
    current code does not prove an older execution.
  snapshot_sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/historical-reading.json
  accessed_at: '2026-10-28T13:55:04.992180Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 54d376a31bb320d6585b26bcc0c1d31927beb3c98cc8b3fc3267c7d73ba875c6
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:55:04.992206Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/complete-document-reader.json
  accessed_at: '2026-10-28T13:55:04.992233Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 4e183caa7a0c21086ce16675b4f52b5497b522fd48ebb6005d8140f02638f405
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:55:04.992255Z'
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
  accessed_at: '2026-10-28T13:55:04.992288Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch069/record08/historical-current-object-joins.json
  accessed_at: '2026-10-28T13:55:04.992311Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: e8ceecdb8edc7ef574863f0c4dca6475b54ce09bf25235962e8fc17643fda0aa
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014269Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 0d3ff2d61b67f042817308eae2f736719f0edd831e19118b7a90be7b3dcdd52c
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014299Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: beeede32ab02fcb22213e7347fa3e6454bdad47f1e33617fc951b18ae35d87e0
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014330Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 81a95d5fe89c842d043c1bf3515e8634c9ff336b4ec3191610a094ec170478ff
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014357Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: a73366863cdee333491c43a1c984ba1da7cbe57ba5a1adce642781f0604363c0
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014380Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: b058a482725994060775919f8cabcd9fe4748e0833105d2458bdd01a4f0a106b
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014404Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 7c195ef5d8c9c6173d8d561c645ad8ab82dd754999e673e8843285142b542b18
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch069/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:55:05.014421Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch069/record08/schema-result.json
  accessed_at: '2026-10-28T13:46:08.821851Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4b69709e1a4921f9932d4a81ada6b7f3d8605eced4cd7f1255ce3f2ec22250a8
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch069/record08/strict-result.json
  accessed_at: '2026-10-28T13:46:09.725811Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 30aef9d220a24bbafe7c2db1e4d6c6504fb8799f6e1bbcb4f8eb8098752141ae
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch069/record08/terms-result.json
  accessed_at: '2026-10-28T13:46:10.713254Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 185caf0f594371a5aecc908edcb21713a67cf73165c9d77dbebd2b5eef6ce834
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch069/record08/references-result.json
  accessed_at: '2026-10-28T13:46:11.343686Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 9d72f77fac561bc7c844ab221e0bc794753184c04075a721eeadd7061fc3b589
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and maintained contributor
  outcome: supported
  summary: CM009683, cgya_medium.yaml and TOGO M3250 agree on identity. DSM6575 is
    Sphaerotilus natans subsp. natans; that corroborates only the source comment identity,
    not a new growth assertion. No agar is specified in the inspected M3250 formulation,
    and none is inferred from the acronym.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - target
  - owner
  - togo3250full
  - dsm6575identity
- assessment_id: representation
  area: representation
  topic: Mixture and physical-state classification
  outcome: supported
  summary: LIQUID is compatible with the four listed components; the source contains
    no agar. COMPLEX/UNDEFINED is appropriate to yeast extract and Casitone. No pH,
    sterilization cycle, or additional stock is invented where the inspected source
    does not specify it.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - target
  - owner
  - togo3250full
- assessment_id: schema
  area: schema
  topic: Native checks and source limits
  outcome: supported
  summary: The original four canonical commands passed. Strict reports zero errors
    and references checked zero entries; these diagnostics do not authenticate concentration
    sources or establish complete bibliographic provenance.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 8 current concentration fields are covered by 5 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b069-quantity-inventory-v1","target":"data/merge_yaml/merged/Cgya_medium.yaml","quantity_field_count":8,"decisions":[{"quantity_id":"q1","label":"Water
    input","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact TOGO row is 1 L of input water, not 1 g/L. Preserve L and do not infer measured
    final volume from water alone.","source_stage":"Listed input water","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current numerical g/L rate agrees with the explicit L−1 formulation in the source
    comment and the matching component row. No attached concentration claim exists
    locally, so this is evidence_only rather than verified. No inferred water denominator
    or glycerol density conversion is used.","source_stage":"Source explicitly stated
    solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was
    purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig,
    Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g
    yeast extract L−1) (Nierman & Maglott, 1989) under aerobic conditions at 30 °C
    for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Glycerol","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current numerical g/L rate agrees with the explicit L−1 formulation in the source
    comment and the matching component row. No attached concentration claim exists
    locally, so this is evidence_only rather than verified. No inferred water denominator
    or glycerol density conversion is used.","source_stage":"Source explicitly stated
    solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Glycerol\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001083\",\n          \"gmo_id\": \"GMO_001083\",\n          \"label\":
    \"Glycerol\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was
    purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig,
    Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g
    yeast extract L−1) (Nierman & Maglott, 1989) under aerobic conditions at 30 °C
    for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Casitone","local_fields":[{"path":"data/merge_yaml/merged/Cgya_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cgya_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current numerical g/L rate agrees with the explicit L−1 formulation in the source
    comment and the matching component row. No attached concentration claim exists
    locally, so this is evidence_only rather than verified. No inferred water denominator
    or glycerol density conversion is used.","source_stage":"Source explicitly stated
    solute rate","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"Casitone\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001104\",\n          \"gmo_id\": \"GMO_001104\",\n          \"label\":
    \"Bacto &trade; Casitone\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was
    purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig,
    Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g
    yeast extract L−1) (Nierman & Maglott, 1989) under aerobic conditions at 30 °C
    for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Source-only
    scoped pre-growth context","local_fields":[],"decision":"evidence_only","rationale":"The
    source describes one pre-growth experiment for S. natans DSM6575T, not universal
    growth support for the medium. Preserve the source citation/context without asserting
    a new target-organism growth relationship or substituting collection conditions.","source_stage":"TOGO
    comment; experiment-specific, not a general recipe condition","sources":[{"evidence_id":"togo3250full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3250","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo3250full.raw","raw_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","text_sha256":"e5bddad1fe97706d999bf8525b647de38b04c61acea78fd3164d732ccf08be23","accessed_at":"2026-10-28T13:47:34.803439Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Iron-oxidizing bacterium S. natans strain DSM 6575T was
    purchased from the Deutsche Sammlung von Mikroorganismen (DSMZ, Braunschweig,
    Germany) and was pregrown in CGYA medium (5 g casitone, 10 g glycerol, and 1 g
    yeast extract L−1) (Nierman & Maglott, 1989) under aerobic conditions at 30 °C
    for 1 day.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Cgya_medium.yaml":null,"data/normalized_yaml/bacterial/cgya_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All four existing target/owner CHEBI slots per layer (water and glycerol
    primary/secondary) resolve to active exact canonical labels and appropriate supplied
    identity. Glycerol regrounding is retained. Secondary linkage is 2/4 ingredient
    instances per layer; agreement among the two existing secondary slots is exact.
    MIM contains both mapped and rejected name variants, so name membership is not
    automatic approval. The two unlinked complex ingredients require bounded source/product
    review, not guessed molecule mappings.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: Both complete October5 reports marked all four concentrations unreviewed;
    those are derivative historical diagnostics, not fresh source evidence. Full target/owner
    histories are preserved, including the current glycerol repair. The owner and
    generated formulation agree; current conservative merging copies singleton sources
    and does not establish scientific validity. No original TOGO import payload or
    Nierman/Maglott publication has been authenticated.
  target_ids:
  - CultureMech:009683
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009683-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Input water is represented as a mass concentration
  description: The target and maintained owner encode the listed 1 L water input as
    1 G_PER_L. Correct the maintained water unit to the source input-volume representation
    and attach the exact row; retain the separately explicit solute rates without
    deriving a measured final volume. Current _parse_unit already maps l to L, so
    this is retained-record staleness rather than evidence that the current parser
    still makes this exact unit error.
  target_ids:
  - CultureMech:009683
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - target
  - owner
  - togo3250full
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009683-source-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source bibliography and claim-level support are incomplete
  description: TOGO M3250 matches the four ingredient names and explicit solute rates.
    Its comment includes a scoped S. natans DSM6575T pre-growth statement and an incomplete
    Nierman & Maglott (1989) citation; meta.src_url is empty. Neither layer retains
    that context or narrow concentration evidence. Attach the exact component/comment
    claims and resolve the primary bibliographic identity before certifying the experimental
    association. The DSM6575 collection page confirms the named organism/strain identity
    only; its other media are not substitutes for CGYA.
  target_ids:
  - CultureMech:009683
  field_paths:
  - notes
  - ingredients
  - references
  - evidence
  evidence_ids:
  - target
  - owner
  - togo3250full
  - dsm6575identity
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009683-secondary-link-coverage
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two complex ingredient names have no secondary linkage
  description: 'Water and glycerol have current exact CHEBI labels and secondary keys.
    Yeast extract and Casitone remain unlinked: the current MIM snapshot has exact
    preferred-name rows, but those rows alone do not authenticate a particular product
    or chemical mixture. Review those bounded linkage candidates against exact source
    identity rather than assigning a single-molecule CHEBI term.'
  target_ids:
  - CultureMech:009683
  field_paths:
  - ingredients[1]
  - ingredients[3]
  evidence_ids:
  - target
  - owner
  - mim
  - mim-meta
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: The target and maintained owner encode the listed 1 L water input as
    1 G_PER_L. Correct the maintained water unit to the source input-volume representation
    and attach the exact row; retain the separately explicit solute rates without
    deriving a measured final volume. Current _parse_unit already maps l to L, so
    this is retained-record staleness rather than evidence that the current parser
    still makes this exact unit error.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009683
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
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
  description: TOGO M3250 matches the four ingredient names and explicit solute rates.
    Its comment includes a scoped S. natans DSM6575T pre-growth statement and an incomplete
    Nierman & Maglott (1989) citation; meta.src_url is empty. Neither layer retains
    that context or narrow concentration evidence. Attach the exact component/comment
    claims and resolve the primary bibliographic identity before certifying the experimental
    association. The DSM6575 collection page confirms the named organism/strain identity
    only; its other media are not substitutes for CGYA.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009683
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: 'Water and glycerol have current exact CHEBI labels and secondary keys.
    Yeast extract and Casitone remain unlinked: the current MIM snapshot has exact
    preferred-name rows, but those rows alone do not authenticate a particular product
    or chemical mixture. Review those bounded linkage candidates against exact source
    identity rather than assigning a single-molecule CHEBI term.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009683
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cgya_medium.yaml
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
- Completion is partial because the full primary citation underlying the TOGO comment
  is unresolved. TOGO supports the explicitly quoted claims, but does not authenticate
  the original experimental paper or its complete variant scope.
- The earlier guessed TOGO /rest/medium/M3250 route returned an application shell
  with HTTP200; it is retained as an unsuccessful source lead. The separately captured
  structured endpoint is the inspected source.
- The DSM6575 page is used only for collection identity. Its cultivation media/conditions
  are not transferred to this record. The source comment supports a bounded description
  of a past pre-growth context, not an automatic culture recommendation.
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
