# Scientific review: DESULFONATRONOVIBRIO medium

- Review: 20261028T195150Z-culturemech-006393-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T19:40:39.422579Z
- Finished UTC: 2026-10-28T19:51:50.518538Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSM742 formulation exposes a cross-stage NaCl sum, flattened mineral/vitamin stocks, lost generated preparation and an atmosphere contradiction. Existing DSM preparation, final pH and provider rates are credited; two supplied-form IDs need correction. Exact KOMODO source access remains unresolved, so the review is partial.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch076 index 10
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006393 | data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml | generated | desulfonatronovibrio_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:006393 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:006393 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:006393 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:006393 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### DSM identity and unresolved KOMODO branch

identity: concern. Targets: CultureMech:006393.

The exact current DSM742 PDF and API define the DSM formulation. The local KOMODO lineage records copied composition, but its exact historical route is currently inaccessible. This is a partial source review; no blanket parent transfer or strain-growth claim is asserted.

### Classification and existing physical state

consistency: supported. Targets: CultureMech:006393.

Yeast extract supports COMPLEX/UNDEFINED, and the liquid source supports LIQUID. The source-specific atmosphere contradiction is assessed separately; physical LIQUID does not certify aerobic conditions.

### Original native diagnostics

schema: supported. Targets: CultureMech:006393.

All four original canonical checks passed, with complete actual streams retained. Reference validation performed zero reference checks and does not authenticate the external sources.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:006393.

105 current concentration fields are covered by 45 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","quantity_field_count":105,"decisions":[{"quantity_id":"q1","label":"NaCl combined across main and mineral stock","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock NaCl 1 g/L. These rates have different solution bases, so their sum is invalid as a final-medium concentration. Preserve the primary 10 g main batch amount and separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate repair cannot resolve unequal source-stage contributions. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main and mineral stock distinct","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 3-3","quote":"NaCl                                                   10.00        g","quote_basis":"derivative text"},{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 33-33","quote":"NaCl                                                    1.00       g","quote_basis":"derivative text"},{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 8-8","quote":"Modified Wolin's mineral solution                      10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\": 169.254,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock NaCl 1 g/L. These rates have different solution bases, so their sum is invalid as a final-medium concentration. Preserve the primary 10 g main batch amount and separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate repair cannot resolve unequal source-stage contributions."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock NaCl 1 g/L. These rates have different solution bases, so their sum is invalid as a final-medium concentration. Preserve the primary 10 g main batch amount and separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate repair cannot resolve unequal source-stage contributions."}]},{"quantity_id":"q2","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 4-4","quote":"Na2SO4                                                  3.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.96736,\n                        \"mmol_l\": 20.891,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q3","label":"Na2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 5-5","quote":"Na2HPO4                                                 0.20        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.197824,\n                        \"mmol_l\": 1.39353,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 6-6","quote":"KCl                                                     0.20        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.197824,\n                        \"mmol_l\": 2.65357,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 7-7","quote":"NH4Cl                                                   1.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 18.4917,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q6","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 9-9","quote":"Sodium resazurin (0.1% w/v)                             0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate."}]},{"quantity_id":"q7","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 10-10","quote":"NaHCO3                                                 15.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.8368,\n                        \"mmol_l\": 176.614,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q8","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 11-11","quote":"Na2CO3                                                 10.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\": 93.3237,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 12-12","quote":"Yeast extract                                           1.50        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.48368,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q10","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 13-13","quote":"Na-formate                                              5.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9456,\n                        \"mmol_l\": 72.7217,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q11","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main provider normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 15-15","quote":"Na2S x 9 H2O                                            1.00        g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 4.11821,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The DSM-linked number matches the explicit API main g_l declaration on its stated 1011 mL provider normalization. Credit that uncited provider rate separately from the printed batch mass. The primary lists 1000 mL water followed by additions, not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q12","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 30-30","quote":"Nitrilotriacetic acid                                   1.50       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q13","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 31-31","quote":"MgSO4 x 7 H2O                                           3.00       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q14","label":"MnSO4 x H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 32-32","quote":"MnSO4 x H2O                                             0.50       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q15","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 34-34","quote":"FeSO4 x 7 H2O                                           0.10       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q16","label":"CoSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 35-35","quote":"CoSO4 x 7 H2O                                           0.18       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q17","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 36-36","quote":"CaCl2 x 2 H2O                                           0.10       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q18","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 37-37","quote":"ZnSO4 x 7 H2O                                           0.18       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q19","label":"CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 38-38","quote":"CuSO4 x 5 H2O                                           0.01       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q20","label":"AlK(SO4)2 x 12 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 39-39","quote":"AlK(SO4)2 x 12 H2O                                      0.02       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q21","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 40-40","quote":"H3BO3                                                   0.01       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q22","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 41-41","quote":"Na2MoO4 x 2 H2O                                         0.01       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 42-42","quote":"NiCl2 x 6 H2O                                           0.03       g","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q24","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 43-43","quote":"Na2SeO3 x 5 H2O                                         0.30      mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q25","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 44-44","quote":"Na2WO4 x 2 H2O                                          0.40      mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient position incorrectly presents it as a main-medium concentration for the DSM formulation. Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed 1000 mL water is not an explicit measured-final-volume instruction; the provider stock basis is still credited."}]},{"quantity_id":"q26","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 61-61","quote":"Biotin                                                   20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q27","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 62-62","quote":"Folic acid                                               20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q28","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 63-63","quote":"Pyridoxine hydrochloride                                100.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q29","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 64-64","quote":"Thiamine HCl                                             50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q30","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 65-65","quote":"Riboflavin                                               50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q31","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 66-66","quote":"Nicotinic acid                                           50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[30].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q32","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 67-67","quote":"Calcium D-(+)-pantothenate                               50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[31].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q33","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 68-68","quote":"Vitamin B12                                               1.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[32].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q34","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 69-69","quote":"p-Aminobenzoic acid                                      50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[33].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[33].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q35","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 70-70","quote":"(DL)-alpha-Lipoic acid                                   50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[34].concentration","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[34].concentration","decision":"correct","rationale":"The local rate is explicitly declared for the 10x vitamin stock by the API, not for the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining the literal primary mg amount and source 10x name. The listed water is an input, not an independent final-volume instruction."}]},{"quantity_id":"q36","label":"Mineral receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This exact source batch dose and named stock is absent as a solution descriptor. Preserve its stage and source strength without treating the listed water as measured final medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 8-8","quote":"Modified Wolin's mineral solution                      10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Vitamin 10x receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This exact source batch dose and named stock is absent as a solution descriptor. Preserve its stage and source strength without treating the listed water as measured final medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 14-14","quote":"Wolin's vitamin solution (10x)                          1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Resazurin stock and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This exact source batch dose and named stock is absent as a solution descriptor. Preserve its stage and source strength without treating the listed water as measured final medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 9-9","quote":"Sodium resazurin (0.1% w/v)                             0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Water in source solution 0","local_fields":[],"decision":"evidence_only","rationale":"The source lists this separate water input; it does not explicitly instruct make-up to a final volume. Preserve the stage rather than collapsing waters or deriving final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 16-16","quote":"Distilled water                                      1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Water in source solution 1","local_fields":[],"decision":"evidence_only","rationale":"The source lists this separate water input; it does not explicitly instruct make-up to a final volume. Preserve the stage rather than collapsing waters or deriving final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 45-45","quote":"Distilled water                                      1000.00      ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Water in source solution 2","local_fields":[],"decision":"evidence_only","rationale":"The source lists this separate water input; it does not explicitly instruct make-up to a final volume. Preserve the stage rather than collapsing waters or deriving final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 71-71","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Retained final main pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}}],"decision":"mixed","rationale":"The existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction. Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Main final pH","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium\nshould be at 9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction. Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ph_range","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction. Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0."}]},{"quantity_id":"q43","label":"Retained DSM main method","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium should be at 9.5 - 9.7."}}],"decision":"evidence_only","rationale":"The owner already preserves the full main method:100% N2,30–45 min, initial pH9.5, autoclaving and separate sterile stock additions with vitamin filtration and final pH9.5–9.7. Credit that text while recovering it in the generated target; this is source method context, not a strain-growth assertion.","source_stage":"Main preparation","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium\nshould be at 9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained mineral-stock pH method needs scope","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}}],"decision":"correct","rationale":"The retained text correctly states mineral-stock pH6.5 with KOH before remaining minerals and final stock pH7.0. Its ADJUST_PH action is appropriate, but placement as an unqualified main preparation step loses the mineral-stock boundary. Nest it under that stock without changing values or inventing a KOH amount.","source_stage":"Mineral stock preparation","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 55-56","quote":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\nfinal to pH 7.0 with KOH.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Aerobic note versus DSM anoxic method","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"notes","stored":"Source: KOMODO ModelSEED &#124; ID: 742 &#124; DSMZ Medium: 742 (mediadive.medium:742) &#124; Aerobic: Yes"},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"notes","stored":"Source: KOMODO ModelSEED &#124; ID: 742 &#124; DSMZ Medium: 742 (mediadive.medium:742) &#124; Aerobic: Yes"}],"decision":"mixed","rationale":"The generated target retains Aerobic: Yes from KOMODO metadata, which contradicts the exact DSM anoxic method represented by its copied composition. Keep provenance explicit, flag that contradiction, and resolve the exact KOMODO source before asserting its own atmosphere. The exact KOMODO branch remains unsupported pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Atmosphere metadata and method","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium\nshould be at 9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"notes","decision":"correct","rationale":"The generated target retains Aerobic: Yes from KOMODO metadata, which contradicts the exact DSM anoxic method represented by its copied composition. Keep provenance explicit, flag that contradiction, and resolve the exact KOMODO source before asserting its own atmosphere."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"notes","decision":"unsupported","rationale":"Exact KOMODO source unresolved; no automatic parent transfer."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml":null,"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:006393.

All asserted ontology and secondary slots were checked against fresh scientific objects and exact current MIM rows, including their mapping_status. Sodium resazurin has primary CHEBI:8806 only and no invented secondary slot; nickel hexahydrate conflicts with anhydrous primary/secondary IDs. CoSO4·7H2O CHEBI:91244 and source-explicit calcium D-(+)-pantothenate CHEBI:31345 are supported supplied forms. Generic CHEBI:16494 is compatible with the lipoic-acid class but does not by itself certify a DL mixture, so preserve the source DL name. Canonical-label agreement is separate from chemical specificity and accepted mapping status.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:006393.

The five per-record historical reports were read in full, together with complete archive methodology/general prose and the exact selected pair row. Both selected historical plan rows were joined claim by claim. Current API742 raw bytes equal the historical source digest, and every non-null source snippet joins literally and as its exact decoded object; null snippets remain false. This authenticates content only. The old mapping page remains derivative because its raw capture was not recovered and current exact routes are 403. Current MediaDive code preserves stock references but omits water and flattens preparation across solution stages; current conservative merger compares full scientific fields. Preserve existing preparation/history credit and append actual curation events; the current timestamp writer defect and stored .fZ are distinct observations.

## Findings

### f1: Main and mineral-stock NaCl rates were summed

major / open / confirmed; issue key: culturemech-006393-cross-stage-nacl.

Reconcile NaCl 10.8912 G_PER_L in the DSM-linked target and owner: it combines API main9.8912 with stock1.0 across incompatible solution bases. Restore separate main and stock rows and the mineral receiving dose; preserve printed batch amounts and explicit provider normalizations without inventing measured final volume. The current duplicate repair intentionally leaves unequal contributions unresolved, and current cleanup does not sum them. Exact KOMODO quantities remain unsupported until that branch is resolved.

### f2: Mineral and vitamin stock rates are direct ingredients

major / open / confirmed; issue key: culturemech-006393-stock-topology.

Restore the modified Wolin mineral stock and 10x vitamin stock with their10 mL and1 mL receiving doses and separate waters. Twenty-four stock-only rows are direct ingredients, while the mineral NaCl was merged with main NaCl. Credit explicit provider stock rates without transferring them as main-medium values. Preserve the resazurin0.1% w/v stock and0.5 mL dose. Resolve the inaccessible KOMODO branch independently.

### f3: Generated preparation is lost and atmosphere metadata conflicts

major / open / confirmed; issue key: culturemech-006393-prep-atmosphere.

Credit both existing DSM preparation descriptions and final pH range. Restore the main anoxic method to the generated DSM representation, and explicitly scope the retained6.5→7.0 KOH adjustment to the mineral stock rather than the main medium. Aerobic: Yes in target/KOMODO notes conflicts with the DSM method; preserve its lineage and resolve exact source identity before recoding the KOMODO branch. Current _parse_preparation_steps flattens all solution steps, so correct its stage association.

### f4: Sodium resazurin and nickel hydrate are misidentified

major / open / confirmed; issue key: culturemech-006393-supplied-forms.

The source supplies sodium resazurin, but its primary CHEBI:8806 object has no sodium. Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in primary and secondary slots; fresh CHEBI:53542 is the exact hydrate candidate. Reconcile only those supplied-form contradictions with source evidence. Credit the current cobalt sulfate heptahydrate and the source-specific D-calcium-pantothenate match to CHEBI:31345.

### f5: Copied ingredient equality does not establish source equivalence

major / open / confirmed; issue key: culturemech-006393-source-equivalence.

Retain the explicit DSM and KOMODO provenance boundaries. The historical SOURCE_DUPLICATE links are based on identical ingredient/concentration signatures and copied-source notes, while preparation and history differ. Resolve the inaccessible exact KOMODO branch before endorsing parent transfer or an exact merge. The current full scientific-field comparator already rejects differing scientific metadata; preserve that gate.

### f6: Stored malformed timestamp and current writer need distinct treatment

minor / open / confirmed; issue key: culturemech-006393-timestamp-provenance.

The existing KOMODO import timestamp ends in .fZ. The current writer uses a %f directive with time.strftime, which does not provide datetime microsecond formatting. Correct future writer serialization with a supported UTC implementation; retain the old literal event and append any explanatory provenance. Do not invent a repaired historical instant or assert that current code was independently observed executing then.

## Recommended Actions And Acceptance Checks

### a1

Reconcile NaCl 10.8912 G_PER_L in the DSM-linked target and owner: it combines API main9.8912 with stock1.0 across incompatible solution bases. Restore separate main and stock rows and the mineral receiving dose; preserve printed batch amounts and explicit provider normalizations without inventing measured final volume. The current duplicate repair intentionally leaves unequal contributions unresolved, and current cleanup does not sum them. Exact KOMODO quantities remain unsupported until that branch is resolved.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Restore the modified Wolin mineral stock and 10x vitamin stock with their10 mL and1 mL receiving doses and separate waters. Twenty-four stock-only rows are direct ingredients, while the mineral NaCl was merged with main NaCl. Credit explicit provider stock rates without transferring them as main-medium values. Preserve the resazurin0.1% w/v stock and0.5 mL dose. Resolve the inaccessible KOMODO branch independently.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Credit both existing DSM preparation descriptions and final pH range. Restore the main anoxic method to the generated DSM representation, and explicitly scope the retained6.5→7.0 KOH adjustment to the mineral stock rather than the main medium. Aerobic: Yes in target/KOMODO notes conflicts with the DSM method; preserve its lineage and resolve exact source identity before recoding the KOMODO branch. Current _parse_preparation_steps flattens all solution steps, so correct its stage association.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The source supplies sodium resazurin, but its primary CHEBI:8806 object has no sodium. Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in primary and secondary slots; fresh CHEBI:53542 is the exact hydrate candidate. Reconcile only those supplied-form contradictions with source evidence. Credit the current cobalt sulfate heptahydrate and the source-specific D-calcium-pantothenate match to CHEBI:31345.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Retain the explicit DSM and KOMODO provenance boundaries. The historical SOURCE_DUPLICATE links are based on identical ingredient/concentration signatures and copied-source notes, while preparation and history differ. Resolve the inaccessible exact KOMODO branch before endorsing parent transfer or an exact merge. The current full scientific-field comparator already rejects differing scientific metadata; preserve that gate.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

The existing KOMODO import timestamp ends in .fZ. The current writer uses a %f directive with time.strftime, which does not provide datetime microsecond formatting. Correct future writer serialization with a supported UTC implementation; retain the old literal event and append any explanatory provenance. Do not invent a repaired historical instant or assert that current code was independently observed executing then.

- Future timestamps use a supported UTC serializer and literal Z; preserved historical event bytes remain unchanged.
- Any provenance clarification is a new actual event, never an invented historical microsecond value.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm742 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf; REVIEW_WORK/batch076/source07-08-10/dsm742.json; exact original raw/text/hash/time metadata | context_only | Exact selected DSM742 primary; embedded stock sections and conditional notes retain their own scopes. |
| api742 | https://mediadive.dsmz.de/rest/medium/742; REVIEW_WORK/batch076/source07-08-10/api742.json; exact original raw/text/hash/time metadata | context_only | Exact current provider 742 full source; stage-specific g_l rates distinct from final-medium concentration. |
| komodo742 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=742; REVIEW_WORK/batch076/source07-08-10/komodo742.json; exact original raw/text/hash/time metadata | context_only | Exact historical KOMODO contributor MediaInfo identity route; failure is an access limitation, not absence of a formulation. |
| komodoExactList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch076/source07-08-10-extra/komodoExactList.json; exact original raw/text/hash/time metadata | context_only | Exact absolute MediaList URL printed in the selected October7 source-mapping reports; bounded access check only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch076/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; General methodology and exact 742 selected row; archive-selected-reading.json | context_only | Complete archive methodology/general prose and exact 742 pair row read; the other pair-table rows are outside this record scope. Its ingredient/concentration signature is not a complete scientific-equivalence test. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json; Parent context only; exact selected rows are joined from plan.json | context_only | Inspected parent candidate context; no exact selected record row is claimed from this file. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-21 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronovibrio_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronovibrio_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch076/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch076/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch076/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch076/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | The current importer passes a %f directive to time.strftime; the stored event ends .fZ. Current code is not proof of the historical execution event. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group does not add unequal concentrations; this code cannot be cited as proof of the historical sum. |
| writer-repair | scripts/repair_merged_duplicates.py; repair_ingredient, repair_record | context_only | Current repair_ingredient/repair_record collapse identical merged parts only; distinct main and stock amounts require source-specific review. |
| archive-reading | REVIEW_WORK/batch076/record10/archive-selected-reading.json; Complete scoped sidecar | supports | Whole archive methodology/general prose plus exact selected row; unrelated pair-table entries excluded. |
| parent-auth | REVIEW_WORK/batch076/record10/historical-parent-authentication.json; Complete scoped sidecar | supports | Each exact historical parent claim joined to current raw content; null snippets remain unauthenticated even where the response digest matches. |
| provider-census | REVIEW_WORK/batch076/record10/provider-stage-census.json; Complete scoped sidecar | supports | Complete provider data, every solution recipe row and preparation step retained with original raw source digest. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch076/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch076/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; REVIEW_WORK/batch076/source07-08-10/chebi34683.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch076/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch076/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch076/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; REVIEW_WORK/batch076/source07-08-10/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; REVIEW_WORK/batch076/source07-08-10/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965; REVIEW_WORK/batch076/source07-08-10/chebi62965.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch076/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; REVIEW_WORK/batch076/source07-08-10/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; REVIEW_WORK/batch076/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; REVIEW_WORK/batch076/source07-08-10/chebi86364.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch076/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; REVIEW_WORK/batch076/source07-08-10/chebi91244.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch076/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; REVIEW_WORK/batch076/source07-08-10/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; REVIEW_WORK/batch076/source07-08-10/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; REVIEW_WORK/batch076/source07-08-10/chebi86465.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch076/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch076/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch076/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; REVIEW_WORK/batch076/source07-08-10/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch076/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch076/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch076/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch076/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch076/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch076/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch076/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch076/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch076/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch076/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch076/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch076/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch076/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch076/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch076/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch076/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch076/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch076/record10/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims in this scoped sidecar; historical object joins are separate evidence. |
| check-schema | REVIEW_WORK/batch076/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch076/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch076/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch076/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The exact historical KOMODO MediaInfo route and absolute MediaList endpoint returned HTTP 403. The copied local DSM composition and derivative mapping snippet do not authenticate the unresolved current KOMODO formulation.
- The May archive was read for its full methodology/general prose and exact selected pair row only; unrelated pair-table rows are not additional review targets.
- Current equal API bytes authenticate historical quoted content, not the original retrieval event. Null historical snippets remain null and do not become attached ingredient evidence.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T195150Z-culturemech-006393-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFONATRONOVIBRIO medium'
started_at: '2026-10-28T19:40:39.422579Z'
finished_at: '2026-10-28T19:51:50.518538Z'
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
summary: The DSM742 formulation exposes a cross-stage NaCl sum, flattened mineral/vitamin
  stocks, lost generated preparation and an atmosphere contradiction. Existing DSM
  preparation, final pH and provider rates are credited; two supplied-form IDs need
  correction. Exact KOMODO source access remains unresolved, so the review is partial.
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
  - path: data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
    sha256: 059617043fd0cdf9fc7400d9e4b2d7d39d07d7fc99b3413cd7b73c494c77f92e
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    sha256: 966736295b5b2fd198a43b4c640c4505b827b8372ed718170df90989e32abc09
    role: context
  - path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    sha256: 8d9feb6e8d3082f85f3eb59f450d6c27271254165b5d6d319fe562e2f857a038
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml.md
    sha256: c24b68f4e91f7520de6b47fcc07ca92c48a68eb24d3e53a675344186ef179aa4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronovibrio_medium.yaml.md
    sha256: 513c9c941f10a0c02bb24acce6305eeccf1ce2c65ac3aa65571c2e5a06171268
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.md
    sha256: 613f5c8289ac0c2a009afc2c01a8c09dc3fed6b815dc148db45a97dbb642cc89
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.md
    sha256: 0480541dca67800a3cc32795c4223c34a390c649575df603143b699502d8362d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronovibrio_medium.md
    sha256: 874c0003305baad31099f2de1c6adafd2dbecd60097f9cf0c305f452d94f45f3
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
  selection: Authoritative batch076 index 10
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006393
targets:
- target_id: CultureMech:006393
  path: data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
  label: desulfonatronovibrio_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
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
  - CultureMech:006393
  command: just validate-schema data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
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
  - CultureMech:006393
  command: just validate-strict data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
    --out REVIEW_WORK/batch076/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:006393
  command: just validate-terms data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
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
  - CultureMech:006393
  command: just validate-references data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm742
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf
  accessed_at: '2026-10-28T19:40:27.118500Z'
  locator: REVIEW_WORK/batch076/source07-08-10/dsm742.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected DSM742 primary; embedded stock sections and conditional
    notes retain their own scopes.
  snapshot_sha256: a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0
- evidence_id: api742
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/742
  accessed_at: '2026-10-28T19:40:26.976354Z'
  locator: REVIEW_WORK/batch076/source07-08-10/api742.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider 742 full source; stage-specific g_l rates distinct
    from final-medium concentration.
  snapshot_sha256: 7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d
- evidence_id: komodo742
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=742
  accessed_at: '2026-10-28T19:40:26.511045Z'
  locator: REVIEW_WORK/batch076/source07-08-10/komodo742.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical KOMODO contributor MediaInfo identity route; failure is
    an access limitation, not absence of a formulation.
  snapshot_sha256: f9a68fe4e7bff3e539be9f8393f1b6c9e8c32cc8b03f2f0c5108fdee709dd706
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=742;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoExactList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T19:43:47.207335Z'
  locator: REVIEW_WORK/batch076/source07-08-10-extra/komodoExactList.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact absolute MediaList URL printed in the selected October7 source-mapping
    reports; bounded access check only.
  snapshot_sha256: 3a638e3d7aafe2c5e992ff014d9a22958c2f4f47f565ee11bac57fa60332ea12
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T19:40:32.046901Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:51:50.333331Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 059617043fd0cdf9fc7400d9e4b2d7d39d07d7fc99b3413cd7b73c494c77f92e
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:51:50.333512Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 966736295b5b2fd198a43b4c640c4505b827b8372ed718170df90989e32abc09
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:51:50.333542Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:51:50.333835Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:51:50.333857Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:51:50.333878Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:51:50.333900Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 8d9feb6e8d3082f85f3eb59f450d6c27271254165b5d6d319fe562e2f857a038
- evidence_id: report-18
  kind: prior_review
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: General methodology and exact 742 selected row; archive-selected-reading.json
  accessed_at: '2026-10-28T19:51:50.333925Z'
  support: context_only
  summary: Complete archive methodology/general prose and exact 742 pair row read;
    the other pair-table rows are outside this record scope. Its ingredient/concentration
    signature is not a complete scientific-equivalence test.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
  locator: Parent context only; exact selected rows are joined from plan.json
  accessed_at: '2026-10-28T19:51:50.333981Z'
  support: context_only
  summary: Inspected parent candidate context; no exact selected record row is claimed
    from this file.
  snapshot_sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:51:50.334713Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:51:50.340176Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: c24b68f4e91f7520de6b47fcc07ca92c48a68eb24d3e53a675344186ef179aa4
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:51:50.340248Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronovibrio_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:51:50.346541Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 513c9c941f10a0c02bb24acce6305eeccf1ce2c65ac3aa65571c2e5a06171268
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:51:50.346635Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 613f5c8289ac0c2a009afc2c01a8c09dc3fed6b815dc148db45a97dbb642cc89
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:51:50.346673Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 0480541dca67800a3cc32795c4223c34a390c649575df603143b699502d8362d
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronovibrio_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:51:50.346701Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 874c0003305baad31099f2de1c6adafd2dbecd60097f9cf0c305f452d94f45f3
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/historical-reading.json
  accessed_at: '2026-10-28T19:51:50.350239Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 322bee7b660402f7c75d74ab027c83fa4e1c4f3c450ecb4367c6a58e53b53e1a
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:51:50.350353Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: de564a040c25dc3c5d72ff5de446fbfeebb327494f8762530756da57de00d191
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/complete-document-reader.json
  accessed_at: '2026-10-28T19:51:50.350596Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 8b523def3688ea4fc03e42c70650f716ecc006a350bfaa2f5522b491f50fcf8a
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T19:51:50.350642Z'
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
  accessed_at: '2026-10-28T19:51:50.350688Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch076/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T19:51:50.350716Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 41f20b3e85a151149d8e7f9bbb3b6b1878d7514ffba3cf2d12fe38e71b55b989
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T19:51:50.350796Z'
  support: context_only
  summary: The current importer passes a %f directive to time.strftime; the stored
    event ends .fZ. Current code is not proof of the historical execution event.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T19:51:50.350820Z'
  support: context_only
  summary: Current _merge_ingredient_group does not add unequal concentrations; this
    code cannot be cited as proof of the historical sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient, repair_record
  accessed_at: '2026-10-28T19:51:50.350844Z'
  support: context_only
  summary: Current repair_ingredient/repair_record collapse identical merged parts
    only; distinct main and stock amounts require source-specific review.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: archive-reading
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/archive-selected-reading.json
  accessed_at: '2026-10-28T19:51:50.350872Z'
  locator: Complete scoped sidecar
  support: supports
  summary: Whole archive methodology/general prose plus exact selected row; unrelated
    pair-table entries excluded.
  snapshot_sha256: d811c89987f90d1147357b2e193305a7cebc27f07c9f92f68c37a9bac49ba210
- evidence_id: parent-auth
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/historical-parent-authentication.json
  accessed_at: '2026-10-28T19:51:50.351096Z'
  locator: Complete scoped sidecar
  support: supports
  summary: Each exact historical parent claim joined to current raw content; null
    snippets remain unauthenticated even where the response digest matches.
  snapshot_sha256: af9bed202a035752454ac7326ad4031b222b01525e366a06333bbd570564797f
- evidence_id: provider-census
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/provider-stage-census.json
  accessed_at: '2026-10-28T19:51:50.351195Z'
  locator: Complete scoped sidecar
  support: supports
  summary: Complete provider data, every solution recipe row and preparation step
    retained with original raw source digest.
  snapshot_sha256: 4cfab5a8d6dab73fb1a2a054776d5a3af42e362eb040c40b685f36e86e2021cd
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T19:40:28.803367Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T19:40:30.237352Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  accessed_at: '2026-10-28T19:40:30.968301Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi34683.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T19:40:30.726069Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T19:40:29.643732Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T19:40:33.870543Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  accessed_at: '2026-10-28T19:40:30.131111Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  accessed_at: '2026-10-28T19:40:28.998997Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi29377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965
  accessed_at: '2026-10-28T19:40:32.216557Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi62965.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f36b7c1107922c948bf6387ce77e0468c3fcdf76ce80969b5411b600e051910d
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T19:40:33.151048Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  accessed_at: '2026-10-28T19:40:31.459032Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  accessed_at: '2026-10-28T19:40:30.088231Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  accessed_at: '2026-10-28T19:40:33.710365Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi86364.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T19:40:33.115496Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  accessed_at: '2026-10-28T19:40:34.305774Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi91244.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T19:40:33.256487Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  accessed_at: '2026-10-28T19:40:30.674383Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  accessed_at: '2026-10-28T19:40:29.770250Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  accessed_at: '2026-10-28T19:40:33.857877Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi86465.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T19:40:30.840133Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T19:40:32.669688Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T19:40:31.295602Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  accessed_at: '2026-10-28T19:40:27.062903Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T19:40:32.556885Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T19:40:27.631883Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  accessed_at: '2026-10-28T19:40:28.999053Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T19:40:29.503180Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T19:40:31.450132Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  accessed_at: '2026-10-28T19:40:27.888014Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T19:40:27.477267Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T19:40:29.645981Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T19:40:28.239467Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T19:40:29.484850Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  accessed_at: '2026-10-28T19:40:27.714759Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516480Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 013658ef00f77b1f4d73fd1de019e20dd0b34629302f4a66bc63db9a922159ff
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516573Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 69fa6ce17fcd2f893930d2415d1a323daba843d8e4e2442d9914f616e719fb04
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516742Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 1a07a364a17f0737972f1479a34b3c8b2f85b2c80df3913712b2ce03033b11e5
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516818Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 888ab0a3628ee370d41b2a7aa53991446edb01c3c83b098c4171c9f7c26c4174
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516889Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 6297e90db84835ef5e0b91a981df7411870e3496020fd1ca77f64dc7b64ea2bf
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516911Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 88b119d16cdb42473c6b96d644caa9c2cfd62e223b59ed1b4b0246b300274ff9
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch076/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:51:50.516930Z'
  support: context_only
  summary: No attached claims in this scoped sidecar; historical object joins are
    separate evidence.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch076/record10/schema-result.json
  accessed_at: '2026-10-28T19:40:40.520882Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: cd2a8c22af9abaf1e807503c05e74ff13f80036720bae8521f975109ffdc36a9
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch076/record10/strict-result.json
  accessed_at: '2026-10-28T19:40:41.498346Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: f1aeb2b1ec03efc6695a4e1baf58209545cf9f89bf3c82b40b7d77698be909d4
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch076/record10/terms-result.json
  accessed_at: '2026-10-28T19:40:42.567560Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 083866e323a363f4b40e513ac76b39fdefccef52ec8d83d82d65223f8963de21
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch076/record10/references-result.json
  accessed_at: '2026-10-28T19:40:43.342872Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: bfd9a2e75276dc0cc0800598e0a7b45c25dfa9c9ae046fff787e09d0537b49a0
assessments:
- assessment_id: identity
  area: identity
  topic: DSM identity and unresolved KOMODO branch
  outcome: concern
  summary: The exact current DSM742 PDF and API define the DSM formulation. The local
    KOMODO lineage records copied composition, but its exact historical route is currently
    inaccessible. This is a partial source review; no blanket parent transfer or strain-growth
    claim is asserted.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - target
  - owner
  - owner-2
  - dsm742
  - api742
  - komodo742
  - komodoExactList
  - archive-reading
- assessment_id: classification
  area: consistency
  topic: Classification and existing physical state
  outcome: supported
  summary: Yeast extract supports COMPLEX/UNDEFINED, and the liquid source supports
    LIQUID. The source-specific atmosphere contradiction is assessed separately; physical
    LIQUID does not certify aerobic conditions.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - target
  - owner-2
  - dsm742
  - api742
- assessment_id: structure
  area: schema
  topic: Original native diagnostics
  outcome: supported
  summary: All four original canonical checks passed, with complete actual streams
    retained. Reference validation performed zero reference checks and does not authenticate
    the external sources.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - census
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 105 current concentration fields are covered by 45 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","quantity_field_count":105,"decisions":[{"quantity_id":"q1","label":"NaCl
    combined across main and mineral stock","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10.8912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock
    NaCl 1 g/L. These rates have different solution bases, so their sum is invalid
    as a final-medium concentration. Preserve the primary 10 g main batch amount and
    separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate
    repair cannot resolve unequal source-stage contributions. The exact KOMODO branch
    remains unsupported pending its own source resolution; DSM evidence is comparison-only
    for that owner.","source_stage":"Main and mineral stock distinct","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 3-3","quote":"NaCl                                                   10.00        g","quote_basis":"derivative
    text"},{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 33-33","quote":"NaCl                                                    1.00       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 8-8","quote":"Modified Wolin''s mineral solution                      10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\":
    169.254,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock
    NaCl 1 g/L. These rates have different solution bases, so their sum is invalid
    as a final-medium concentration. Preserve the primary 10 g main batch amount and
    separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate
    repair cannot resolve unequal source-stage contributions."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    local 10.8912 G_PER_L equals a sum of API main NaCl 9.8912 g/L and mineral-stock
    NaCl 1 g/L. These rates have different solution bases, so their sum is invalid
    as a final-medium concentration. Preserve the primary 10 g main batch amount and
    separate 1 g mineral-stock amount, plus the 10 mL stock dose. Current identical-duplicate
    repair cannot resolve unequal source-stage contributions."}]},{"quantity_id":"q2","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.96736","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 4-4","quote":"Na2SO4                                                  3.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.96736,\n                        \"mmol_l\":
    20.891,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q3","label":"Na2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 5-5","quote":"Na2HPO4                                                 0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\":
    233,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.197824,\n                        \"mmol_l\":
    1.39353,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.197824","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 6-6","quote":"KCl                                                     0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.197824,\n                        \"mmol_l\":
    2.65357,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 7-7","quote":"NH4Cl                                                   1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\":
    18.4917,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q6","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00049456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 9-9","quote":"Sodium resazurin (0.1% w/v)                             0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    Preserve the primary 0.5 mL of 0.1% w/v stock, not just the flattened solute rate."}]},{"quantity_id":"q7","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"14.8368","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 10-10","quote":"NaHCO3                                                 15.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 14.8368,\n                        \"mmol_l\":
    176.614,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q8","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"9.8912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 11-11","quote":"Na2CO3                                                 10.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\":
    93.3237,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q9","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.48368","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 12-12","quote":"Yeast extract                                           1.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.48368,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q10","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"4.9456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 13-13","quote":"Na-formate                                              5.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.9456,\n                        \"mmol_l\":
    72.7217,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q11","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.98912","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main provider
    normalization","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 15-15","quote":"Na2S x 9 H2O                                            1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\":
    4.11821,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    DSM-linked number matches the explicit API main g_l declaration on its stated
    1011 mL provider normalization. Credit that uncited provider rate separately from
    the printed batch mass. The primary lists 1000 mL water followed by additions,
    not a measured final-volume instruction; do not invent a different final denominator."}]},{"quantity_id":"q12","label":"Nitrilotriacetic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 30-30","quote":"Nitrilotriacetic acid                                   1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q13","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 31-31","quote":"MgSO4 x 7 H2O                                           3.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q14","label":"MnSO4 x H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 32-32","quote":"MnSO4 x H2O                                             0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q15","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 34-34","quote":"FeSO4 x 7 H2O                                           0.10       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q16","label":"CoSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 35-35","quote":"CoSO4 x 7 H2O                                           0.18       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q17","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 36-36","quote":"CaCl2 x 2 H2O                                           0.10       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q18","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 37-37","quote":"ZnSO4 x 7 H2O                                           0.18       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q19","label":"CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 38-38","quote":"CuSO4 x 5 H2O                                           0.01       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q20","label":"AlK(SO4)2 x 12
    H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 39-39","quote":"AlK(SO4)2 x 12 H2O                                      0.02       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q21","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 40-40","quote":"H3BO3                                                   0.01       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q22","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 41-41","quote":"Na2MoO4 x 2 H2O                                         0.01       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 42-42","quote":"NiCl2 x 6 H2O                                           0.03       g","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q24","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 43-43","quote":"Na2SeO3 x 5 H2O                                         0.30      mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q25","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited. The exact KOMODO branch remains unsupported pending
    its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Modified
    Wolin mineral stock","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 44-44","quote":"Na2WO4 x 2 H2O                                          0.40      mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The
    API explicitly declares this mineral-stock g_l rate, but the local top-level ingredient
    position incorrectly presents it as a main-medium concentration for the DSM formulation.
    Restore the separate modified Wolin mineral stock and 10 mL receiving dose. Listed
    1000 mL water is not an explicit measured-final-volume instruction; the provider
    stock basis is still credited."}]},{"quantity_id":"q26","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 61-61","quote":"Biotin                                                   20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q27","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 62-62","quote":"Folic acid                                               20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q28","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 63-63","quote":"Pyridoxine hydrochloride                                100.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q29","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 64-64","quote":"Thiamine HCl                                             50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q30","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 65-65","quote":"Riboflavin                                               50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q31","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 66-66","quote":"Nicotinic acid                                           50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[30].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q32","label":"Calcium
    D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 67-67","quote":"Calcium D-(+)-pantothenate                               50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[31].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q33","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 68-68","quote":"Vitamin B12                                               1.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[32].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q34","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 69-69","quote":"p-Aminobenzoic acid                                      50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[33].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[33].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q35","label":"(DL)-alpha-Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction. The exact KOMODO branch remains unsupported
    pending its own source resolution; DSM evidence is comparison-only for that owner.","source_stage":"Wolin
    vitamin stock 10x","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 70-70","quote":"(DL)-alpha-Lipoic acid                                   50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ingredients[34].concentration","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ingredients[34].concentration","decision":"correct","rationale":"The
    local rate is explicitly declared for the 10x vitamin stock by the API, not for
    the main medium. Restore that stock boundary and its 1 mL receiving dose, retaining
    the literal primary mg amount and source 10x name. The listed water is an input,
    not an independent final-volume instruction."}]},{"quantity_id":"q36","label":"Mineral
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This
    exact source batch dose and named stock is absent as a solution descriptor. Preserve
    its stage and source strength without treating the listed water as measured final
    medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 8-8","quote":"Modified Wolin''s mineral solution                      10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q37","label":"Vitamin 10x receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This
    exact source batch dose and named stock is absent as a solution descriptor. Preserve
    its stage and source strength without treating the listed water as measured final
    medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 14-14","quote":"Wolin''s vitamin solution (10x)                          1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q38","label":"Resazurin stock and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"This
    exact source batch dose and named stock is absent as a solution descriptor. Preserve
    its stage and source strength without treating the listed water as measured final
    medium.","source_stage":"Main receiving dose","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 9-9","quote":"Sodium resazurin (0.1% w/v)                             0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Water
    in source solution 0","local_fields":[],"decision":"evidence_only","rationale":"The
    source lists this separate water input; it does not explicitly instruct make-up
    to a final volume. Preserve the stage rather than collapsing waters or deriving
    final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 16-16","quote":"Distilled water                                      1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q40","label":"Water in source solution 1","local_fields":[],"decision":"evidence_only","rationale":"The
    source lists this separate water input; it does not explicitly instruct make-up
    to a final volume. Preserve the stage rather than collapsing waters or deriving
    final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 45-45","quote":"Distilled water                                      1000.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"Water in source solution 2","local_fields":[],"decision":"evidence_only","rationale":"The
    source lists this separate water input; it does not explicitly instruct make-up
    to a final volume. Preserve the stage rather than collapsing waters or deriving
    final concentrations.","source_stage":"Exact source water stage","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 71-71","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q42","label":"Retained final main pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ph_range","stored":{"min":9.5,"max":9.7}}],"decision":"mixed","rationale":"The
    existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction.
    Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0.
    The exact KOMODO branch remains unsupported pending its own source resolution;
    DSM evidence is comparison-only for that owner.","source_stage":"Main final pH","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast
    extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30
    - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH
    to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and
    sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins
    should be sterilized by filtration. The pH of the complete medium\nshould be at
    9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins,
    formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it
    anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium
    under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration.
    The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction.
    Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"ph_range","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."},{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    existing DSM-linked pH range 9.5–9.7 matches the final main-medium instruction.
    Preserve it distinctly from main pre-autoclave pH9.5 and mineral-stock pH6.5 then7.0."}]},{"quantity_id":"q43","label":"Retained
    DSM main method","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients except bicarbonate, carbonate, yeast extract, vitamins, formate, and
    sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then
    add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium under 100%
    N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add yeast extract, vitamins, formate and sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas. Vitamins should be sterilized by filtration. The pH
    of the complete medium should be at 9.5 - 9.7."}}],"decision":"evidence_only","rationale":"The
    owner already preserves the full main method:100% N2,30–45 min, initial pH9.5,
    autoclaving and separate sterile stock additions with vitamin filtration and final
    pH9.5–9.7. Credit that text while recovering it in the generated target; this
    is source method context, not a strain-growth assertion.","source_stage":"Main
    preparation","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast
    extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30
    - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH
    to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and
    sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins
    should be sterilized by filtration. The pH of the complete medium\nshould be at
    9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins,
    formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it
    anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium
    under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration.
    The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q44","label":"Retained mineral-stock pH method needs
    scope","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First
    dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.
    Adjust final to pH 7.0 with KOH."}}],"decision":"correct","rationale":"The retained
    text correctly states mineral-stock pH6.5 with KOH before remaining minerals and
    final stock pH7.0. Its ADJUST_PH action is appropriate, but placement as an unqualified
    main preparation step loses the mineral-stock boundary. Nest it under that stock
    without changing values or inventing a KOH amount.","source_stage":"Mineral stock
    preparation","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 55-56","quote":"First dissolve nitrilotriacetic acid and adjust pH to 6.5
    with KOH, then add minerals. Adjust\nfinal to pH 7.0 with KOH.","quote_basis":"derivative
    text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add
    minerals. Adjust final to pH 7.0 with KOH.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q45","label":"Aerobic note versus DSM anoxic method","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"notes","stored":"Source:
    KOMODO ModelSEED | ID: 742 | DSMZ Medium: 742 (mediadive.medium:742) | Aerobic:
    Yes"},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"notes","stored":"Source:
    KOMODO ModelSEED | ID: 742 | DSMZ Medium: 742 (mediadive.medium:742) | Aerobic:
    Yes"}],"decision":"mixed","rationale":"The generated target retains Aerobic: Yes
    from KOMODO metadata, which contradicts the exact DSM anoxic method represented
    by its copied composition. Keep provenance explicit, flag that contradiction,
    and resolve the exact KOMODO source before asserting its own atmosphere. The exact
    KOMODO branch remains unsupported pending its own source resolution; DSM evidence
    is comparison-only for that owner.","source_stage":"Atmosphere metadata and method","sources":[{"evidence_id":"dsm742","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium742.pdf","raw_path":"REVIEW_WORK/batch076/source07-08-10/dsm742.raw","raw_sha256":"a9d5aa2b56205ba487f1407f422fbe54dbde411b8f093dc3699cde64284195a0","text_sha256":"485368d707caae42bf02633c4fec14c3ca53fbfd012add2e469c268b1decd22c","accessed_at":"2026-10-28T19:40:27.118500Z","locator":"dsm742.txt
    lines 18-24","quote":"Dissolve ingredients except bicarbonate, carbonate, yeast
    extract, vitamins, formate, and\nsulfide. Sparge medium with 100% N2 gas for 30
    - 45 min to make it anoxic, then add\nbicarbonate and carbonate and adjust pH
    to 9.5. Dispense medium under 100% N2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add yeast\nextract, vitamins, formate and
    sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas. Vitamins
    should be sterilized by filtration. The pH of the complete medium\nshould be at
    9.5 - 9.7.","quote_basis":"derivative text"},{"evidence_id":"api742","reference":"https://mediadive.dsmz.de/rest/medium/742","raw_path":"REVIEW_WORK/batch076/source07-08-10/api742.raw","raw_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","text_sha256":"7941de923b76bbf8c93b7914e33591ac1051f7e89dc4fa52a2611ba1dafa9d3d","accessed_at":"2026-10-28T19:40:26.976354Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except bicarbonate, carbonate, yeast extract, vitamins,
    formate, and sulfide. Sparge medium with 100% N2 gas for 30 - 45 min to make it
    anoxic, then add bicarbonate and carbonate and adjust pH to 9.5. Dispense medium
    under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Add yeast extract, vitamins, formate and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration.
    The pH of the complete medium should be at 9.5 - 9.7.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_decisions":[{"path":"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml","field_path":"notes","decision":"correct","rationale":"The
    generated target retains Aerobic: Yes from KOMODO metadata, which contradicts
    the exact DSM anoxic method represented by its copied composition. Keep provenance
    explicit, flag that contradiction, and resolve the exact KOMODO source before
    asserting its own atmosphere."},{"path":"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml","field_path":"notes","decision":"unsupported","rationale":"Exact
    KOMODO source unresolved; no automatic parent transfer."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONOVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml":null,"data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted ontology and secondary slots were checked against fresh scientific
    objects and exact current MIM rows, including their mapping_status. Sodium resazurin
    has primary CHEBI:8806 only and no invented secondary slot; nickel hexahydrate
    conflicts with anhydrous primary/secondary IDs. CoSO4·7H2O CHEBI:91244 and source-explicit
    calcium D-(+)-pantothenate CHEBI:31345 are supported supplied forms. Generic CHEBI:16494
    is compatible with the lipoic-acid class but does not by itself certify a DL mixture,
    so preserve the source DL name. Canonical-label agreement is separate from chemical
    specificity and accepted mapping status.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: The five per-record historical reports were read in full, together with
    complete archive methodology/general prose and the exact selected pair row. Both
    selected historical plan rows were joined claim by claim. Current API742 raw bytes
    equal the historical source digest, and every non-null source snippet joins literally
    and as its exact decoded object; null snippets remain false. This authenticates
    content only. The old mapping page remains derivative because its raw capture
    was not recovered and current exact routes are 403. Current MediaDive code preserves
    stock references but omits water and flattens preparation across solution stages;
    current conservative merger compares full scientific fields. Preserve existing
    preparation/history credit and append actual curation events; the current timestamp
    writer defect and stored .fZ are distinct observations.
  target_ids:
  - CultureMech:006393
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-mediadive
  - writer-formulation
  - writer-merger
  - writer-komodo
  - writer-cleanup
  - writer-repair
  - archive-reading
  - parent-auth
findings:
- finding_id: f1
  issue_key: culturemech-006393-cross-stage-nacl
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main and mineral-stock NaCl rates were summed
  description: 'Reconcile NaCl 10.8912 G_PER_L in the DSM-linked target and owner:
    it combines API main9.8912 with stock1.0 across incompatible solution bases. Restore
    separate main and stock rows and the mineral receiving dose; preserve printed
    batch amounts and explicit provider normalizations without inventing measured
    final volume. The current duplicate repair intentionally leaves unequal contributions
    unresolved, and current cleanup does not sum them. Exact KOMODO quantities remain
    unsupported until that branch is resolved.'
  target_ids:
  - CultureMech:006393
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - dsm742
  - api742
  - quantities
  - writer-repair
  - writer-cleanup
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-006393-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Mineral and vitamin stock rates are direct ingredients
  description: Restore the modified Wolin mineral stock and 10x vitamin stock with
    their10 mL and1 mL receiving doses and separate waters. Twenty-four stock-only
    rows are direct ingredients, while the mineral NaCl was merged with main NaCl.
    Credit explicit provider stock rates without transferring them as main-medium
    values. Preserve the resazurin0.1% w/v stock and0.5 mL dose. Resolve the inaccessible
    KOMODO branch independently.
  target_ids:
  - CultureMech:006393
  field_paths:
  - ingredients[11]
  - ingredients[34]
  - solutions
  evidence_ids:
  - dsm742
  - api742
  - provider-census
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-006393-prep-atmosphere
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation is lost and atmosphere metadata conflicts
  description: 'Credit both existing DSM preparation descriptions and final pH range.
    Restore the main anoxic method to the generated DSM representation, and explicitly
    scope the retained6.5→7.0 KOH adjustment to the mineral stock rather than the
    main medium. Aerobic: Yes in target/KOMODO notes conflicts with the DSM method;
    preserve its lineage and resolve exact source identity before recoding the KOMODO
    branch. Current _parse_preparation_steps flattens all solution steps, so correct
    its stage association.'
  target_ids:
  - CultureMech:006393
  field_paths:
  - notes
  - preparation_steps
  - ph_range
  - data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml::preparation_steps[1]
  evidence_ids:
  - owner-2
  - dsm742
  - api742
  - writer-mediadive
  - quantities
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained preparation parser
- finding_id: f4
  issue_key: culturemech-006393-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin and nickel hydrate are misidentified
  description: The source supplies sodium resazurin, but its primary CHEBI:8806 object
    has no sodium. Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in primary
    and secondary slots; fresh CHEBI:53542 is the exact hydrate candidate. Reconcile
    only those supplied-form contradictions with source evidence. Credit the current
    cobalt sulfate heptahydrate and the source-specific D-calcium-pantothenate match
    to CHEBI:31345.
  target_ids:
  - CultureMech:006393
  field_paths:
  - ingredients[5].term
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm742
  - groundings
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-006393-source-equivalence
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Copied ingredient equality does not establish source equivalence
  description: Retain the explicit DSM and KOMODO provenance boundaries. The historical
    SOURCE_DUPLICATE links are based on identical ingredient/concentration signatures
    and copied-source notes, while preparation and history differ. Resolve the inaccessible
    exact KOMODO branch before endorsing parent transfer or an exact merge. The current
    full scientific-field comparator already rejects differing scientific metadata;
    preserve that gate.
  target_ids:
  - CultureMech:006393
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml::parent_media
  - data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml::variant_children
  - merged_from
  evidence_ids:
  - owner
  - owner-2
  - archive-reading
  - parent-auth
  - komodo742
  - komodoExactList
  - writer-formulation
  - writer-merger
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
- finding_id: f6
  issue_key: culturemech-006393-timestamp-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Stored malformed timestamp and current writer need distinct treatment
  description: The existing KOMODO import timestamp ends in .fZ. The current writer
    uses a %f directive with time.strftime, which does not provide datetime microsecond
    formatting. Correct future writer serialization with a supported UTC implementation;
    retain the old literal event and append any explanatory provenance. Do not invent
    a repaired historical instant or assert that current code was independently observed
    executing then.
  target_ids:
  - CultureMech:006393
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml::curation_history[0].timestamp
  evidence_ids:
  - owner
  - writer-komodo
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
actions:
- action_id: a1
  description: 'Reconcile NaCl 10.8912 G_PER_L in the DSM-linked target and owner:
    it combines API main9.8912 with stock1.0 across incompatible solution bases. Restore
    separate main and stock rows and the mineral receiving dose; preserve printed
    batch amounts and explicit provider normalizations without inventing measured
    final volume. The current duplicate repair intentionally leaves unequal contributions
    unresolved, and current cleanup does not sum them. Exact KOMODO quantities remain
    unsupported until that branch is resolved.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
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
  description: Restore the modified Wolin mineral stock and 10x vitamin stock with
    their10 mL and1 mL receiving doses and separate waters. Twenty-four stock-only
    rows are direct ingredients, while the mineral NaCl was merged with main NaCl.
    Credit explicit provider stock rates without transferring them as main-medium
    values. Preserve the resazurin0.1% w/v stock and0.5 mL dose. Resolve the inaccessible
    KOMODO branch independently.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
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
  description: 'Credit both existing DSM preparation descriptions and final pH range.
    Restore the main anoxic method to the generated DSM representation, and explicitly
    scope the retained6.5→7.0 KOH adjustment to the mineral stock rather than the
    main medium. Aerobic: Yes in target/KOMODO notes conflicts with the DSM method;
    preserve its lineage and resolve exact source identity before recoding the KOMODO
    branch. Current _parse_preparation_steps flattens all solution steps, so correct
    its stage association.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained preparation parser
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained DSM curation; mediadive_importer.py preparation-stage preservation
    and conservative regeneration
- action_id: a4
  description: The source supplies sodium resazurin, but its primary CHEBI:8806 object
    has no sodium. Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in primary
    and secondary slots; fresh CHEBI:53542 is the exact hydrate candidate. Reconcile
    only those supplied-form contradictions with source evidence. Credit the current
    cobalt sulfate heptahydrate and the source-specific D-calcium-pantothenate match
    to CHEBI:31345.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: Retain the explicit DSM and KOMODO provenance boundaries. The historical
    SOURCE_DUPLICATE links are based on identical ingredient/concentration signatures
    and copied-source notes, while preparation and history differ. Resolve the inaccessible
    exact KOMODO branch before endorsing parent transfer or an exact merge. The current
    full scientific-field comparator already rejects differing scientific metadata;
    preserve that gate.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: The existing KOMODO import timestamp ends in .fZ. The current writer
    uses a %f directive with time.strftime, which does not provide datetime microsecond
    formatting. Correct future writer serialization with a supported UTC implementation;
    retain the old literal event and append any explanatory provenance. Do not invent
    a repaired historical instant or assert that current code was independently observed
    executing then.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:006393
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
  acceptance_checks:
  - Future timestamps use a supported UTC serializer and literal Z; preserved historical
    event bytes remain unchanged.
  - Any provenance clarification is a new actual event, never an invented historical
    microsecond value.
  generator: src/culturemech/import/komodo_web_importer.py timestamp serialization;
    append-only provenance clarification
limitations:
- The exact historical KOMODO MediaInfo route and absolute MediaList endpoint returned
  HTTP 403. The copied local DSM composition and derivative mapping snippet do not
  authenticate the unresolved current KOMODO formulation.
- The May archive was read for its full methodology/general prose and exact selected
  pair row only; unrelated pair-table rows are not additional review targets.
- Current equal API bytes authenticate historical quoted content, not the original
  retrieval event. Null historical snippets remain null and do not become attached
  ingredient evidence.
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
