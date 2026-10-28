# Scientific review: Clostridial medium

- Review: 20261028T145322Z-culturemech-009330-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T14:34:08.181616Z
- Finished UTC: 2026-10-28T14:53:22.857150Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Partial source review identifies an incorrect water unit and unsupported final-volume bases while preserving all nine exact source batch amounts. Current ontology identities and complex-liquid classification are supported; source experiment provenance remains unresolved.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch070 index 07
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009330 | data/merge_yaml/merged/Clostridial_medium.yaml | generated | clostridial_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009330 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009330 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009330 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009330 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source identity

identity: supported. Targets: CultureMech:009330.

The selected generated CM009330 is a singleton of the declared normalized clostridial_medium owner. Current TOGO M2781 has the same identity and nine ingredient names. No sibling medium or organism-specific formulation is substituted.

### Classification and organism scope

consistency: supported. Targets: CultureMech:009330.

COMPLEX/UNDEFINED/LIQUID is consistent with the inspected extract/peptone recipe and absence of an agar component. P. acnes appears only in an untraced source experiment comment; no strain-growth assertion is added.

### Native structural checks

schema: supported. Targets: CultureMech:009330.

All four original canonical commands passed. No references were attached, so the zero-reference result does not authenticate source support. The complete scalar census and current inputs are retained.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009330.

18 current concentration fields are covered by 10 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridial_medium.yaml","quantity_field_count":18,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source states an input of 1 L water, not 1 g/L. Preserve that volume without asserting final volume.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast Extract","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Yeast Extract\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Sodium Chloride","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Sodium Chloride\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Dextrose","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"Dextrose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001010\",\n          \"gmo_id\": \"GMO_001010\",\n          \"label\": \"D-Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Sodium Acetate","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Sodium Acetate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Soluble Starch","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Soluble Starch\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001837\",\n          \"gmo_id\": \"GMO_001837\",\n          \"label\": \"Soluble starch\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Cysteine HCl","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Cysteine HCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001032\",\n          \"gmo_id\": \"GMO_001032\",\n          \"label\": \"Cysteine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Beef Extract","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"Beef Extract\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001072\",\n          \"gmo_id\": \"GMO_001072\",\n          \"label\": \"Beef extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass agrees numerically, but its grams and 1 L input water do not establish final volume. The existing G_PER_L assertion remains unsupported as a final-medium rate; retain the source batch amount separately.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"Peptone\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_000012\",\n          \"gmo_id\": \"GMO_000012\",\n          \"label\": \"Peptone\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Source experimental context","local_fields":[],"decision":"evidence_only","rationale":"This is an attributed TOGO comment about a P. acnes DNA-extraction experiment. It is not an independently verified paper, a strain-level growth assertion, or a universal preparation condition for this medium.","source_stage":"Source-only experiment context, not a curated growth condition","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"Genomic DNA extraction of P. acnes isolates - Isolates were grown in 5 mL of Clostridial medium under anaerobic conditions at 37°C for 5 - 7 days.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Clostridial_medium.yaml":null,"data/normalized_yaml/bacterial/clostridial_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:009330.

All five distinct asserted CHEBI objects are current and active; dextrose is an exact D-glucose synonym, sodium chloride and acetate are salts, and starch denotes the polysaccharide class. Soluble grade and unspecified acetate hydrate remain source limits, not verified grades. Both documents have 4 secondary links among 9 ingredient instances, with exact current-slot label agreement. Unmapped mixtures and unspecified cysteine HCl stereochemistry are not assigned guessed identifiers.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:009330.

Both complete historical concentration reports explicitly performed zero source checks. They are derivative context, not authentication. All current history events are retained; there are no existing attached formulation snippets to authenticate. The current merge preserves scientific assertions conservatively and the present importer already maps L water correctly; the old generated/maintained water encoding is not proof of unchanged writer behavior.

## Findings

### f1: Input water is represented as a mass concentration

major / open / confirmed; issue key: culturemech-009330-input-water-unit.

Both target and maintained owner encode distilled water as 1 G_PER_L although the exact TOGO object gives 1 L. Correct the maintained volume representation with exact evidence, preserving its status as input water rather than a final-volume declaration.

### f2: Batch masses lack an established final-volume denominator

major / open / confirmed; issue key: culturemech-009330-unverified-final-basis.

The remaining eight source amounts are grams in a batch containing 1 L input water. Their numeric values survive, but local G_PER_L rates and absent attached evidence do not establish the final-medium denominator. Resolve the actual primary formulation basis before certifying or converting these rates. Do not invent final volume.

### f3: TOGO experimental comment lacks a traceable primary citation

minor / open / confirmed; issue key: culturemech-009330-source-provenance.

The exact M2781 metadata has an empty src_url and contains a comment concerning P. acnes isolates and genomic-DNA extraction. Preserve this as scoped source context and seek its exact bibliography; neither the name nor that comment establishes a target strain, universal growth claim or complete preparation protocol. The local source URL in notes remains valid identity provenance.

## Recommended Actions And Acceptance Checks

### a1

Both target and maintained owner encode distilled water as 1 G_PER_L although the exact TOGO object gives 1 L. Correct the maintained volume representation with exact evidence, preserving its status as input water rather than a final-volume declaration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The remaining eight source amounts are grams in a batch containing 1 L input water. Their numeric values survive, but local G_PER_L rates and absent attached evidence do not establish the final-medium denominator. Resolve the actual primary formulation basis before certifying or converting these rates. Do not invent final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The exact M2781 metadata has an empty src_url and contains a comment concerning P. acnes isolates and genomic-DNA extraction. Preserve this as scoped source context and seek its exact bibliography; neither the name nor that comment establishes a target strain, universal growth claim or complete preparation protocol. The local source URL in notes remains valid identity provenance.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| currentTogo2781 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781; REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.json; exact original raw/text/hash/time metadata | context_only | Official structured TOGO route observed in prior reviewed application; exact source object and original timestamp retained. |
| togo2781 | https://togomedium.org/rest/medium/M2781; REVIEW_WORK/batch070/source07-08-10/togo2781.json; exact original raw/text/hash/time metadata | context_only | Exact source identity first; generic medium names alone do not establish strain growth or hazardous organism association. No scientific assessment before native inspection. |
| target | data/merge_yaml/merged/Clostridial_medium.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/clostridial_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridial_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridial_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _extract_ingredients, _parse_unit, _extract_preparation_steps | context_only | Current _parse_unit maps l to L, correcting the historical water-unit representation, but maps bare g to G_PER_L without proving final volume. Current comment extraction would retain prose; no historical execution is inferred. |
| historical-reading | REVIEW_WORK/batch070/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch070/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch070/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch070/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch070/source07-08-10-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch070/source07-08-10-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634; REVIEW_WORK/batch070/source07-08-10-supplement/chebi17634.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch070/source07-08-10-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28017; REVIEW_WORK/batch070/source07-08-10-supplement/chebi28017.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| quantities | REVIEW_WORK/batch070/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch070/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch070/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch070/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch070/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch070/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch070/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch070/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch070/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch070/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch070/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Partial: TOGO M2781 is readable, but it does not identify an original publication or a source-final-volume declaration. The experimental comment is not independently attributed.
- The initial /rest/medium/M2781 request returned an HTTP200 application shell. Its bytes/time remain preserved separately from the successful official SPARQList JSON capture.
- iModulonDB structured adapters are not applicable to this medium record: no gene, locus, expression module or transcriptomic assertion is present.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T145322Z-culturemech-009330-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Clostridial medium'
started_at: '2026-10-28T14:34:08.181616Z'
finished_at: '2026-10-28T14:53:22.857150Z'
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
summary: Partial source review identifies an incorrect water unit and unsupported
  final-volume bases while preserving all nine exact source batch amounts. Current
  ontology identities and complex-liquid classification are supported; source experiment
  provenance remains unresolved.
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
  - path: data/merge_yaml/merged/Clostridial_medium.yaml
    sha256: 6472e11001a9b07cff92217ab0969ce8e7af46396c2543cec152251529cfd0d1
    role: target
  - path: data/normalized_yaml/bacterial/clostridial_medium.yaml
    sha256: 9d1d3a70bb6ff2c40fdc4a71ab6b34a806ed99ac70e7574a818cf7d83ca01a06
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridial_medium.md
    sha256: b904d5279bfd12d31baaecce1a3a3e1ef6d77b656dc2e5a61e0545db10e20426
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridial_medium.md
    sha256: 69fb0d599fb3dedfbdd3b5a8290a6282bbc67e2da79d1a815f9a159e4a7774e0
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
  selection: Authoritative batch070 index 07
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009330
targets:
- target_id: CultureMech:009330
  path: data/merge_yaml/merged/Clostridial_medium.yaml
  label: clostridial_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
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
  - CultureMech:009330
  command: just validate-schema data/merge_yaml/merged/Clostridial_medium.yaml
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
  - CultureMech:009330
  command: just validate-strict data/merge_yaml/merged/Clostridial_medium.yaml --out
    REVIEW_WORK/batch070/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:009330
  command: just validate-terms data/merge_yaml/merged/Clostridial_medium.yaml
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
  - CultureMech:009330
  command: just validate-references data/merge_yaml/merged/Clostridial_medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: currentTogo2781
  kind: primary_source
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781
  accessed_at: '2026-10-28T14:35:16.158985Z'
  locator: REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.json;
    exact original raw/text/hash/time metadata
  support: context_only
  summary: Official structured TOGO route observed in prior reviewed application;
    exact source object and original timestamp retained.
  snapshot_sha256: 0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4
- evidence_id: togo2781
  kind: database
  reference: https://togomedium.org/rest/medium/M2781
  accessed_at: '2026-10-28T14:34:10.266999Z'
  locator: REVIEW_WORK/batch070/source07-08-10/togo2781.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity first; generic medium names alone do not establish
    strain growth or hazardous organism association. No scientific assessment before
    native inspection.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Clostridial_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:38:02.382893Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 6472e11001a9b07cff92217ab0969ce8e7af46396c2543cec152251529cfd0d1
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridial_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:38:02.383053Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 9d1d3a70bb6ff2c40fdc4a71ab6b34a806ed99ac70e7574a818cf7d83ca01a06
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T14:38:02.383074Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T14:38:02.383352Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T14:38:02.383373Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T14:38:02.383392Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridial_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:38:02.383415Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b904d5279bfd12d31baaecce1a3a3e1ef6d77b656dc2e5a61e0545db10e20426
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridial_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:38:02.383442Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 69fb0d599fb3dedfbdd3b5a8290a6282bbc67e2da79d1a815f9a159e4a7774e0
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _extract_ingredients, _parse_unit, _extract_preparation_steps
  accessed_at: '2026-10-28T14:38:02.384145Z'
  support: context_only
  summary: Current _parse_unit maps l to L, correcting the historical water-unit representation,
    but maps bare g to G_PER_L without proving final volume. Current comment extraction
    would retain prose; no historical execution is inferred.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/historical-reading.json
  accessed_at: '2026-10-28T14:38:02.384861Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 7f48af203f4ef63354b5ba140c0b4a15c820dbd014b85d6bcb88ea75bbbd1770
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T14:38:02.384892Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/complete-document-reader.json
  accessed_at: '2026-10-28T14:38:02.385014Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 6a2f10c0bb4953d81ed0d67c33478b1257c185813d3c485f9d37e309ad987bbd
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T14:38:02.385044Z'
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
  accessed_at: '2026-10-28T14:38:02.385076Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch070/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T14:38:02.385101Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: ad361243e6b07718da5c7c1fdb45df1d8f585118ce901c93f44d338b45c64e70
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T14:35:01.173152Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T14:35:02.822174Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634
  accessed_at: '2026-10-28T14:35:02.671194Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi17634.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 04060738e01fe33b9fc8e5bf54807590127ce391eb8a962d1d013002502169b2
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T14:35:04.871672Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi32954.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28017
  accessed_at: '2026-10-28T14:35:03.371099Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi28017.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 8d5cfcf42eb1f0d584069e65aa21275d1863248742e38cef6b0bbe3853db7084
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416757Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 1cfd767d4a72a877174e555e75db5081cff265cffdd274a8d1bb9f55b4b45fac
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416793Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: a49a2f4ad354b8b402c6df81127c5d3a1ef27764623d9c12993d2e5e93728d08
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416833Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 3af7e3c5f968a7a7687f908f9a43d415a7cfae8b8375dc45a5b34e677e70606a
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416863Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 0b093ba9f8029c553d00fccfcae4f7b16334c7a6c42744444cdb9cf48a740137
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416889Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 42e1d1e9349ab18d28b642934e5e3c89acb50133ffecb0cdb208d03a2df68601
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416909Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: e87f0ee9ee8482dbd02ff2a8ea053f3adf2a89b8c924c94a62b48a272e3713f0
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch070/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:38:02.416926Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch070/record07/schema-result.json
  accessed_at: '2026-10-28T14:34:09.197471Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 436676eb93db9e2b1dd8a583b0340baf3eda55f1d6ec34c173fc2debaed593bc
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch070/record07/strict-result.json
  accessed_at: '2026-10-28T14:34:10.113930Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 503d3cbf37ececb8c65ff3f9a090d89613c7287747d63f5fb6c83fcedc4d7bf8
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch070/record07/terms-result.json
  accessed_at: '2026-10-28T14:34:11.111346Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 31b260a6ce1d3e750dde8f7ca6e333c09ded30f301301f5ba2eb492f6e9c8e2c
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch070/record07/references-result.json
  accessed_at: '2026-10-28T14:34:11.755937Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 18465b1e2821d27c0c9d5081714e5013bcea32b320be0d018e1f154206515aaf
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source identity
  outcome: supported
  summary: The selected generated CM009330 is a singleton of the declared normalized
    clostridial_medium owner. Current TOGO M2781 has the same identity and nine ingredient
    names. No sibling medium or organism-specific formulation is substituted.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - target
  - owner
  - currentTogo2781
- assessment_id: classification
  area: consistency
  topic: Classification and organism scope
  outcome: supported
  summary: COMPLEX/UNDEFINED/LIQUID is consistent with the inspected extract/peptone
    recipe and absence of an agar component. P. acnes appears only in an untraced
    source experiment comment; no strain-growth assertion is added.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - target
  - owner
  - currentTogo2781
- assessment_id: structure
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four original canonical commands passed. No references were attached,
    so the zero-reference result does not authenticate source support. The complete
    scalar census and current inputs are retained.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 18 current concentration fields are covered by 10 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridial_medium.yaml","quantity_field_count":18,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source states an input of 1 L water, not 1 g/L. Preserve that volume without asserting
    final volume.","source_stage":"Main recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    Extract","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Yeast Extract\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Sodium Chloride","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Sodium Chloride\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Dextrose","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"Dextrose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001010\",\n          \"gmo_id\": \"GMO_001010\",\n          \"label\":
    \"D-Glucose\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Sodium
    Acetate","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Sodium Acetate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\":
    \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"Soluble Starch","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"Soluble Starch\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001837\",\n          \"gmo_id\": \"GMO_001837\",\n          \"label\":
    \"Soluble starch\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Cysteine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Cysteine HCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001032\",\n          \"gmo_id\": \"GMO_001032\",\n          \"label\":
    \"Cysteine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Beef
    Extract","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"Beef Extract\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001072\",\n          \"gmo_id\": \"GMO_001072\",\n          \"label\":
    \"Beef extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/Clostridial_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridial_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass agrees numerically, but its grams and 1 L input water
    do not establish final volume. The existing G_PER_L assertion remains unsupported
    as a final-medium rate; retain the source batch amount separately.","source_stage":"Main
    recipe batch; no explicit final make-up","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"Peptone\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_000012\",\n          \"gmo_id\": \"GMO_000012\",\n          \"label\":
    \"Peptone\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Source experimental context","local_fields":[],"decision":"evidence_only","rationale":"This
    is an attributed TOGO comment about a P. acnes DNA-extraction experiment. It is
    not an independently verified paper, a strain-level growth assertion, or a universal
    preparation condition for this medium.","source_stage":"Source-only experiment
    context, not a curated growth condition","sources":[{"evidence_id":"currentTogo2781","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2781","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo2781.raw","raw_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","text_sha256":"0f4da1e7c7504b2d243e9193c7807db2a699197f5375fb7546cc776c111ec6a4","accessed_at":"2026-10-28T14:35:16.158985Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Genomic DNA extraction of P. acnes isolates - Isolates
    were grown in 5 mL of Clostridial medium under anaerobic conditions at 37°C for
    5 - 7 days.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/Clostridial_medium.yaml":null,"data/normalized_yaml/bacterial/clostridial_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: All five distinct asserted CHEBI objects are current and active; dextrose
    is an exact D-glucose synonym, sodium chloride and acetate are salts, and starch
    denotes the polysaccharide class. Soluble grade and unspecified acetate hydrate
    remain source limits, not verified grades. Both documents have 4 secondary links
    among 9 ingredient instances, with exact current-slot label agreement. Unmapped
    mixtures and unspecified cysteine HCl stereochemistry are not assigned guessed
    identifiers.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: Both complete historical concentration reports explicitly performed zero
    source checks. They are derivative context, not authentication. All current history
    events are retained; there are no existing attached formulation snippets to authenticate.
    The current merge preserves scientific assertions conservatively and the present
    importer already maps L water correctly; the old generated/maintained water encoding
    is not proof of unchanged writer behavior.
  target_ids:
  - CultureMech:009330
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009330-input-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Input water is represented as a mass concentration
  description: Both target and maintained owner encode distilled water as 1 G_PER_L
    although the exact TOGO object gives 1 L. Correct the maintained volume representation
    with exact evidence, preserving its status as input water rather than a final-volume
    declaration.
  target_ids:
  - CultureMech:009330
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - currentTogo2781
  - target
  - owner
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009330-unverified-final-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch masses lack an established final-volume denominator
  description: The remaining eight source amounts are grams in a batch containing
    1 L input water. Their numeric values survive, but local G_PER_L rates and absent
    attached evidence do not establish the final-medium denominator. Resolve the actual
    primary formulation basis before certifying or converting these rates. Do not
    invent final volume.
  target_ids:
  - CultureMech:009330
  field_paths:
  - ingredients
  evidence_ids:
  - currentTogo2781
  - quantities
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009330-source-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: TOGO experimental comment lacks a traceable primary citation
  description: The exact M2781 metadata has an empty src_url and contains a comment
    concerning P. acnes isolates and genomic-DNA extraction. Preserve this as scoped
    source context and seek its exact bibliography; neither the name nor that comment
    establishes a target strain, universal growth claim or complete preparation protocol.
    The local source URL in notes remains valid identity provenance.
  target_ids:
  - CultureMech:009330
  field_paths:
  - references
  - notes
  - media_term
  evidence_ids:
  - currentTogo2781
  - target
  - owner
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Both target and maintained owner encode distilled water as 1 G_PER_L
    although the exact TOGO object gives 1 L. Correct the maintained volume representation
    with exact evidence, preserving its status as input water rather than a final-volume
    declaration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
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
  description: The remaining eight source amounts are grams in a batch containing
    1 L input water. Their numeric values survive, but local G_PER_L rates and absent
    attached evidence do not establish the final-medium denominator. Resolve the actual
    primary formulation basis before certifying or converting these rates. Do not
    invent final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
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
  description: The exact M2781 metadata has an empty src_url and contains a comment
    concerning P. acnes isolates and genomic-DNA extraction. Preserve this as scoped
    source context and seek its exact bibliography; neither the name nor that comment
    establishes a target strain, universal growth claim or complete preparation protocol.
    The local source URL in notes remains valid identity provenance.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridial_medium.yaml
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
- 'Partial: TOGO M2781 is readable, but it does not identify an original publication
  or a source-final-volume declaration. The experimental comment is not independently
  attributed.'
- The initial /rest/medium/M2781 request returned an HTTP200 application shell. Its
  bytes/time remain preserved separately from the successful official SPARQList JSON
  capture.
- 'iModulonDB structured adapters are not applicable to this medium record: no gene,
  locus, expression module or transcriptomic assertion is present.'
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
