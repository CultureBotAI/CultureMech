# Beer Medium: preserve the beer solvent and manganese mass unit

- Review: 20261028T045505Z-batch055-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:31:50.117257Z
- Finished UTC: 2026-10-28T04:55:05.255208Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 426 explicitly applies the MRS base to normally hopped beer and sets pH 5.2. The selected record and sole TOGO owner misrepresent the beer volume as a mass and the manganese hydrate milligrams as grams, and omit the source preparation. Other batch masses and source-specific form limits are preserved.

## Scope And Provenance

Full selected record and exact maintained contributors; external source limits explicitly retained.

Selection: Actual batch055 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009811 | data/merge_yaml/merged/Beer_Medium.yaml | generated | beer_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009811 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:009811 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:009811 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:009811 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact426 and explicit base reference

identity: supported. Targets: CultureMech:009811.

The selected merge has one TOGO_M426 maintained contributor. Current JCM 426 and TOGO agree on exact Beer identity; JCM 1 is an explicitly linked formulation dependency, not a second owner. The provider J426 confirms identity/preparation only and supplies no amount basis.

### Supplied forms and mixture limits

grounding: supported. Targets: CultureMech:009811.

All asserted CHEBI labels match current OLS. Magnesium heptahydrate is explicitly supported. CHEBI:86360 identifies manganese(II) sulfate but does not resolve the source x-hydrate, so no molecular-weight conversion follows. Tween 80 is a polymeric mixture; its ontology mass does not support a mass/volume conversion. Undefined extracts and hopped beer remain mixtures, not missing stoichiometric chemical identities. Current MIM rows and ontology-linked hydrate aliases are kept separate.

### Classification and unchanged provider annotations

scope: supported. Targets: CultureMech:009811.

COMPLEX, UNDEFINED and LIQUID are consistent with the source ingredient mixture. Provider mineral/buffer/surfactant/carbon and undefined-component notes are preserved as TOGO annotations. Generic microbial-cultivation application and bacterial filing do not establish growth, an organism list or incubation conditions.

### Complete quantity and numeric preparation audit

quantity: concern. Targets: CultureMech:009811.

Every local concentration field has an explicit disposition; source-only doses, batch volumes and conditional preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "MgSO4・7H2O", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. The heptahydrate identity is explicitly supported and the prior local correction is credited.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. The heptahydrate identity is explicitly supported and the prior local correction is credited."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. The heptahydrate identity is explicitly supported and the prior local correction is credited."}]}, {"quantity_id": "q2", "topic": "K2HPO4", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q3", "topic": "Sodium acetate", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Sodium acetate\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q4", "topic": "Tween 80", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Tween 80\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001060\",\n          \"gmo_id\": \"GMO_001060\",\n          \"label\": \"Polysorbate 80\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000075\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000075\",\n              \"label\": \"Surfactant\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar formulation or density.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar formulation or density."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented. Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar formulation or density."}]}, {"quantity_id": "q5", "topic": "MnSO4・xH2O", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "Both TOGO and the linked primary MRS table specify 50 mg manganese sulfate x-hydrate, not 50 g. 50 mg equals 0.05 g as batch mass. Preserve the unspecified hydrate number and nominal 1 L solvent recipe basis; do not invent an exact hydrate, molar conversion or independently measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Both TOGO and the linked primary MRS table specify 50 mg manganese sulfate x-hydrate, not 50 g. 50 mg equals 0.05 g as batch mass. Preserve the unspecified hydrate number and nominal 1 L solvent recipe basis; do not invent an exact hydrate, molar conversion or independently measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Both TOGO and the linked primary MRS table specify 50 mg manganese sulfate x-hydrate, not 50 g. 50 mg equals 0.05 g as batch mass. Preserve the unspecified hydrate number and nominal 1 L solvent recipe basis; do not invent an exact hydrate, molar conversion or independently measured final volume."}]}, {"quantity_id": "q6", "topic": "Diammonium citrate", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Diammonium citrate\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001084\",\n          \"gmo_id\": \"GMO_001084\",\n          \"label\": \"Diammonium hydrogen citrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q7", "topic": "Glucose", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\": \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q8", "topic": "hopped beer", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"hopped beer\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002246\",\n          \"gmo_id\": \"GMO_002246\",\n          \"label\": \"Beer\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The source specifies 1 L normally hopped beer as the solvent replacing water, not 1 g/L beer. Restore a liquid-volume representation and replacement relationship. No beer density, alcohol percentage or chemical composition is supplied, and no mass conversion is justified.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source specifies 1 L normally hopped beer as the solvent replacing water, not 1 g/L beer. Restore a liquid-volume representation and replacement relationship. No beer density, alcohol percentage or chemical composition is supplied, and no mass conversion is justified."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source specifies 1 L normally hopped beer as the solvent replacing water, not 1 g/L beer. Restore a liquid-volume representation and replacement relationship. No beer density, alcohol percentage or chemical composition is supplied, and no mass conversion is justified."}]}, {"quantity_id": "q9", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q10", "topic": "Beef extract (BD-Difco)", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Beef extract (BD-Difco)\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001442\",\n          \"gmo_id\": \"GMO_001442\",\n          \"label\": \"Bacto &amp;trade; Beef extract, dessicated (BD)\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q11", "topic": "Casein peptone, tryptic digest", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T04:32:46.735923+00:00", "quote": "{\n          \"component_name\": \"Casein peptone, tryptic digest\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001615\",\n          \"gmo_id\": \"GMO_001615\",\n          \"label\": \"Pancreatic digest of casein\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting that the 1 L quantity is the solvent input rather than an explicit measured-final-volume statement. No stock dilution is invented."}]}, {"quantity_id": "q12", "topic": "Beer-specific pH and preparation", "source": {"evidence_id": "jcm426", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426", "raw_path": "REVIEW_WORK/batch055/source01-03/jcm426.bin", "raw_sha256": "fb8c82340997fc2848d8e4e1ca1223e19456e5b3fdc1976fe9100b35d5af48a9", "locator": "Exact426 instruction", "accessed_at": "2026-10-28T04:32:45.979171+00:00", "quote": "in normally hopped beer instead of distilled water. Adjust pH to 5.2."}, "decision": "add", "rationale": "The accessible primary and both provider records agree on the Beer-specific pH and solvent replacement.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "Add exact Beer pH 5.2; do not inherit base-MRS pH 6.0–6.5.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "Add exact Beer pH 5.2; do not inherit base-MRS pH 6.0–6.5.", "missing": true}, {"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Add the explicit MRS in beer solvent-replacement and pH adjustment instruction.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Add the explicit MRS in beer solvent-replacement and pH adjustment instruction.", "missing": true}]}, {"quantity_id": "q13", "topic": "General JCM sterilization instruction", "source": {"evidence_id": "jcm426", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426", "raw_path": "REVIEW_WORK/batch055/source01-03/jcm426.bin", "raw_sha256": "fb8c82340997fc2848d8e4e1ca1223e19456e5b3fdc1976fe9100b35d5af48a9", "locator": "Page header general instruction", "accessed_at": "2026-10-28T04:32:45.979171+00:00", "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}, "decision": "add", "rationale": "The explicit general instruction appears on the exact426 page; no organism temperature, exposure optimization or additional treatment is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Preserve the primary page general instruction with its unless-otherwise-stated scope: 121 °C for 15 min. This is preparation, not an incubation condition.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Preserve the primary page general instruction with its unless-otherwise-stated scope: 121 °C for 15 min. This is preparation, not an incubation condition.", "missing": true}]}, {"quantity_id": "q14", "topic": "Excluded base-medium pH and replaced water", "source": {"evidence_id": "jcm1", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1", "raw_path": "REVIEW_WORK/batch055/source01-03/jcm1.bin", "raw_sha256": "41b844456434a1a492b81092c8dafdf7ce9836165130b0f3efabce53d5af993c", "locator": "MRS1 base footer and water row", "accessed_at": "2026-10-28T04:32:46.133660+00:00", "quote": "Adjust pH to 6.0-6.5."}, "decision": "evidence_only", "rationale": "The base pH 6.0–6.5 is explicitly superseded by Beer 5.2, and its 1 L water is replaced by beer rather than added alongside it. Base amounts enter only through the 426 cross-reference; no other parent condition transfers.", "layer_assessments": []}, {"quantity_id": "q15", "topic": "Unknown beer composition and manganese hydrate number", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31", "locator": "$.components[0].items[4,7]", "accessed_at": "2026-10-28T04:32:46.735923+00:00"}, "decision": "unsupported", "rationale": "The source names normally hopped beer and MnSO4 xH2O but does not specify beer density/composition or x. These are explicit limits; no new compound, stock strength, alcohol concentration or exact hydrate is guessed.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:009811.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:009811.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:009811.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:009811.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Manganese hydrate milligrams were represented as grams

major / open / confirmed; issue key: culturemech-009811-manganese-hydrate-milligrams-were-represented-as-grams.

ingredients[4] stores 50 G_PER_L. Both current TOGO and the linked primary MRS table specify 50 mg manganese sulfate x-hydrate. The mass-unit factor is 1000, but correcting it does not establish an exact hydrate or measured final-medium volume.

### f2: Beer solvent volume was represented as mass

major / open / confirmed; issue key: culturemech-009811-beer-solvent-volume-was-represented-as-mass.

ingredients[7] stores 1 G_PER_L hopped beer. The source requires 1 L normally hopped beer in place of the base water. This changes a solvent-volume instruction into an unsupported mass concentration.

### f3: Beer-specific pH and preparation are absent

major / open / confirmed; issue key: culturemech-009811-beer-specific-ph-and-preparation-are-absent.

Both target and owner omit pH 5.2 and the exact instruction to prepare MRS in normally hopped beer. The exact JCM 426 page also gives its general 121 °C/15 min sterilization instruction. Base MRS pH 6.0–6.5 must not be copied into Beer Medium.

## Recommended Actions And Acceptance Checks

### action1

Curate the maintained owner to preserve 50 mg batch mass on the stated recipe basis, retaining unknown hydrate number. Attach exact source evidence and regenerate; do not add an unsupported molar conversion.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Represent the sourced 1 L beer volume and explicit water-replacement relationship in the maintained owner. Do not invent density, beer composition or an additional 1 L water input; regenerate afterward.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Add source-scoped pH and preparation to the maintained owner, preserving the explicit general sterilization qualifier and separating preparation from growth conditions. Regenerate and verify that these instructions survive.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Beer_Medium.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| jcm426 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426; Exact source identity and scoped formulation/preparation | supports | Exact primary426 instructs MRS medium in normally hopped beer instead of water and pH 5.2. Its explicit general sterilization instruction is 121 °C for 15 min unless otherwise stated. |
| jcm1 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1; Exact source identity and scoped formulation/preparation | supports | Exact explicitly linked MRS 1 base supplies ten solute batch amounts and 1 L water. Only its base formulation is inherited by426; base pH 6.0–6.5 is overridden by Beer 5.2. |
| togo426 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426; Exact source identity and scoped formulation/preparation | supports | Exact M426 expands the same ten base solutes and 1 L hopped beer, with pH 5.2 and source instruction. Role/property labels are provider annotations, not strain growth evidence. |
| apiJ426 | https://mediadive.dsmz.de/rest/medium/J426; Exact source identity and scoped formulation/preparation | supports | Exact J426 provider confirms identity, pH 5.2 and preparation; it provides no recipe quantities or declared final volume. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components/_solution_from_item/_extract_preparation_steps | context_only | Current primary-component extraction distinguishes stock sections and preserves source comments via _extract_preparation_steps. This code establishes present safeguards only, not which historical conversion caused the two unit errors. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | The current sole-contributor merge copies owner content and adds provenance; regeneration cannot correct an owner unit error without prior owner curation. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Beer_Medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-3 | reports/yaml_record_review/20260921T193633Z-Beer_Medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-reader | REVIEW_WORK/batch055/record03/historical-reader.json | context_only | Complete selected target/owner historical reports and exact report hashes, preserving derivative-only limits. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53426 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53426; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63076 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63076; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch055/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch055/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch055/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch055/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch055/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch055/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch055/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch055/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch055/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The primary formulation lists a 1 L solvent input, not explicit measured final-volume makeup; nominal recipe-basis rates are not presented as independently measured final concentrations.
- Normally hopped beer composition/density and manganese sulfate hydrate number are unspecified. No culture strain, growth result, incubation condition, beer alcohol percentage or exact hydrate is inferred.
- Historical reports are derivative evidence; no claim is made that old external responses were recovered. Current primary/provider captures directly support the bounded findings.
- The JCM 1 base pH is excluded because JCM 426 specifies 5.2. Current J426 API lacks recipe quantities and does not supply a missing final-volume denominator.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T045505Z-batch055-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Beer Medium: preserve the beer solvent and manganese mass unit'
started_at: '2026-10-28T04:31:50.117257Z'
finished_at: '2026-10-28T04:55:05.255208Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: JCM 426 explicitly applies the MRS base to normally hopped beer and sets
  pH 5.2. The selected record and sole TOGO owner misrepresent the beer volume as
  a mass and the manganese hydrate milligrams as grams, and omit the source preparation.
  Other batch masses and source-specific form limits are preserved.
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
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/Beer_Medium.yaml
    sha256: 1c7897a654a9a6e6cd5219a294c2882b756129888c4e75d7ff439a5d43d043f5
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    sha256: 26776127a3b06407e5bb6114652a1393bb4282eaecc115c382cea4748eeacc62
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Beer_Medium.md
    sha256: d0cbc320f6a2dbf943c2c989555af7468d57b14678760904945f2550834fb0c3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.md
    sha256: bdb58159030060e8a6db0dbc2325c587cfd3cda6cf92380e1f1aa64c06fa282f
    role: context
  - path: reports/yaml_record_review/20260921T193633Z-Beer_Medium.md
    sha256: bdfd5725a273869da3d2f8b8885b82c081eb7b029e7261befe7332b61d3e17f9
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
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
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Full selected record and exact maintained contributors; external source
    limits explicitly retained.
  selection: Actual batch055 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009811
targets:
- target_id: CultureMech:009811
  path: data/merge_yaml/merged/Beer_Medium.yaml
  label: beer_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009811
  command: just validate-schema data/merge_yaml/merged/Beer_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009811
  command: just validate-strict data/merge_yaml/merged/Beer_Medium.yaml --out REVIEW_WORK/batch055/record03/strict.tsv
    --workers 1
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009811
  command: just validate-terms data/merge_yaml/merged/Beer_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:009811
  command: just validate-references data/merge_yaml/merged/Beer_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Beer_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 1c7897a654a9a6e6cd5219a294c2882b756129888c4e75d7ff439a5d43d043f5
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 26776127a3b06407e5bb6114652a1393bb4282eaecc115c382cea4748eeacc62
- evidence_id: jcm426
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:32:45.979171Z'
  support: supports
  summary: Exact primary426 instructs MRS medium in normally hopped beer instead of
    water and pH 5.2. Its explicit general sterilization instruction is 121 °C for
    15 min unless otherwise stated.
  snapshot_sha256: fb8c82340997fc2848d8e4e1ca1223e19456e5b3fdc1976fe9100b35d5af48a9
- evidence_id: jcm1
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:32:46.133660Z'
  support: supports
  summary: Exact explicitly linked MRS 1 base supplies ten solute batch amounts and
    1 L water. Only its base formulation is inherited by426; base pH 6.0–6.5 is overridden
    by Beer 5.2.
  snapshot_sha256: 41b844456434a1a492b81092c8dafdf7ce9836165130b0f3efabce53d5af993c
- evidence_id: togo426
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:32:46.735923Z'
  support: supports
  summary: Exact M426 expands the same ten base solutes and 1 L hopped beer, with
    pH 5.2 and source instruction. Role/property labels are provider annotations,
    not strain growth evidence.
  snapshot_sha256: 7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31
- evidence_id: apiJ426
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J426
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:32:46.551533Z'
  support: supports
  summary: Exact J426 provider confirms identity, pH 5.2 and preparation; it provides
    no recipe quantities or declared final volume.
  snapshot_sha256: 28078004dc6039128f396c2d31fbf2165d509184f9d41d50f956b3faac79741d
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components/_solution_from_item/_extract_preparation_steps
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Current primary-component extraction distinguishes stock sections and preserves
    source comments via _extract_preparation_steps. This code establishes present
    safeguards only, not which historical conversion caused the two unit errors.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: The current sole-contributor merge copies owner content and adds provenance;
    regeneration cannot correct an owner unit error without prior owner curation.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Beer_Medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: d0cbc320f6a2dbf943c2c989555af7468d57b14678760904945f2550834fb0c3
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: bdb58159030060e8a6db0dbc2325c587cfd3cda6cf92380e1f1aa64c06fa282f
- evidence_id: historical-3
  kind: record_content
  reference: reports/yaml_record_review/20260921T193633Z-Beer_Medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:43:50.215049Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: bdfd5725a273869da3d2f8b8885b82c081eb7b029e7261befe7332b61d3e17f9
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch055/record03/historical-reader.json
  accessed_at: '2026-10-28T04:43:50.229039Z'
  support: context_only
  summary: Complete selected target/owner historical reports and exact report hashes,
    preserving derivative-only limits.
  snapshot_sha256: 0deb38ba3366b4d854ac94ccf2b1278990e9cc499eed9cd036927b8395132f91
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:49.479874Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:47.022231Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.028297Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 34c7d0dea7bc001a0a3b3b388138837cb1aba3b252017bc1ff8625b7a3ff655d
- evidence_id: chebi53426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53426
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.980481Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1f7138a13b34b7476b99f7452a3af718a8d2f06ee9270446095c99b4ad1f805d
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:52.905639Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d7fa588a0312e9c257c235a7219db2e63b9d8a1ae7c8af0af9d549739f00aa6d
- evidence_id: chebi63076
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63076
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:51.720460Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f6ecc5ad3aa8d31ffb9db3602f1a719ba341b5a7b93a50bfa70782098415b57e
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:48.004108Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch055/record03/quantity-inventory.json
  accessed_at: '2026-10-28T04:55:05.255208Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 4483705eb5650817295aac48deee371257fee2f457c0395c74970dbb49f9ada6
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch055/record03/grounding-inventory.json
  accessed_at: '2026-10-28T04:43:50.237719Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: a880c687ebcd5209d00c16df3a2d3ab7e9dcebd24ee513f7eb93ad4d958d5d3b
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch055/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T04:43:50.237767Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 579c4b61b3fae9f3154d4d8f18b5f1d0120ef72fbfbfb51fd97986b281a66c21
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch055/record03/scalar-census.json
  accessed_at: '2026-10-28T04:43:50.237795Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: cb7d86b207c47c6016a1aeb9adb31f9be47454aa965339b6c4e0440fae4d872a
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch055/record03/validate-schema.json
  accessed_at: '2026-10-28T04:31:51.695292Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: bd5f07a1a4c41b06c110eb11a9de7a15042a7af4882367df9145cd93eed3648a
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch055/record03/validate-strict.json
  accessed_at: '2026-10-28T04:31:52.987613Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch055/record03/strict.tsv\n"
  snapshot_sha256: 7e9b144360bc5ba622b7d984a89bc02340d9d247ac83fe2395f11bdd5cb40fe0
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch055/record03/validate-terms.json
  accessed_at: '2026-10-28T04:31:54.526601Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: dfe6c5762a531996466d415b7396b893cfda2f9044b023ef724bded3bf0c141d
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch055/record03/validate-references.json
  accessed_at: '2026-10-28T04:31:56.688543Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 8a6085560076b58fb7b777036eba6d8f3ff1025f89b4a37ff71fc7f4e53b7fa9
assessments:
- assessment_id: a1
  area: identity
  topic: Exact426 and explicit base reference
  outcome: supported
  summary: The selected merge has one TOGO_M426 maintained contributor. Current JCM
    426 and TOGO agree on exact Beer identity; JCM 1 is an explicitly linked formulation
    dependency, not a second owner. The provider J426 confirms identity/preparation
    only and supplies no amount basis.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - local-target
  - owner-1
  - jcm426
  - jcm1
  - togo426
  - apiJ426
- assessment_id: a2
  area: grounding
  topic: Supplied forms and mixture limits
  outcome: supported
  summary: All asserted CHEBI labels match current OLS. Magnesium heptahydrate is
    explicitly supported. CHEBI:86360 identifies manganese(II) sulfate but does not
    resolve the source x-hydrate, so no molecular-weight conversion follows. Tween
    80 is a polymeric mixture; its ontology mass does not support a mass/volume conversion.
    Undefined extracts and hopped beer remain mixtures, not missing stoichiometric
    chemical identities. Current MIM rows and ontology-linked hydrate aliases are
    kept separate.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - grounding
  - chebi31795
  - chebi86360
  - chebi53426
  - jcm1
- assessment_id: a3
  area: scope
  topic: Classification and unchanged provider annotations
  outcome: supported
  summary: COMPLEX, UNDEFINED and LIQUID are consistent with the source ingredient
    mixture. Provider mineral/buffer/surfactant/carbon and undefined-component notes
    are preserved as TOGO annotations. Generic microbial-cultivation application and
    bacterial filing do not establish growth, an organism list or incubation conditions.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - local-target
  - togo426
- assessment_id: a4
  area: quantity
  topic: Complete quantity and numeric preparation audit
  outcome: concern
  summary: Every local concentration field has an explicit disposition; source-only
    doses, batch volumes and conditional preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "MgSO4・7H2O", "source": {"evidence_id":
    "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\":
    \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_basis": "Literal raw
    JSON substring, independently decoded to the located object"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented. The heptahydrate identity is explicitly
    supported and the prior local correction is credited.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented. The heptahydrate identity is explicitly
    supported and the prior local correction is credited."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO
    batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated
    mass on the source recipe basis, noting that the 1 L quantity is the solvent input
    rather than an explicit measured-final-volume statement. No stock dilution is
    invented. The heptahydrate identity is explicitly supported and the prior local
    correction is credited."}]}, {"quantity_id": "q2", "topic": "K2HPO4", "source":
    {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\":
    2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\":
    \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_basis": "Literal raw
    JSON substring, independently decoded to the located object"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}]},
    {"quantity_id": "q3", "topic": "Sodium acetate", "source": {"evidence_id": "togo426",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Sodium acetate\",\n          \"volume\":
    5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\":
    \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented."}]}, {"quantity_id": "q4", "topic":
    "Tween 80", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Tween 80\",\n          \"volume\":
    1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001060\",\n          \"gmo_id\":
    \"GMO_001060\",\n          \"label\": \"Polysorbate 80\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000075\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000075\",\n              \"label\": \"Surfactant\"\n            }\n          ]\n        }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.
    Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar
    formulation or density.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.
    Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar
    formulation or density."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.
    Tween 80 is literally 1 g in this source, not 1 mL; do not substitute a familiar
    formulation or density."}]}, {"quantity_id": "q5", "topic": "MnSO4・xH2O", "source":
    {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\":
    50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\":
    \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_basis": "Literal
    raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "Both TOGO and the linked primary MRS table specify 50
    mg manganese sulfate x-hydrate, not 50 g. 50 mg equals 0.05 g as batch mass. Preserve
    the unspecified hydrate number and nominal 1 L solvent recipe basis; do not invent
    an exact hydrate, molar conversion or independently measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Both TOGO and the linked primary MRS table specify 50 mg manganese sulfate x-hydrate,
    not 50 g. 50 mg equals 0.05 g as batch mass. Preserve the unspecified hydrate
    number and nominal 1 L solvent recipe basis; do not invent an exact hydrate, molar
    conversion or independently measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Both TOGO and the linked
    primary MRS table specify 50 mg manganese sulfate x-hydrate, not 50 g. 50 mg equals
    0.05 g as batch mass. Preserve the unspecified hydrate number and nominal 1 L
    solvent recipe basis; do not invent an exact hydrate, molar conversion or independently
    measured final volume."}]}, {"quantity_id": "q6", "topic": "Diammonium citrate",
    "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Diammonium citrate\",\n          \"volume\":
    2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001084\",\n          \"gmo_id\":
    \"GMO_001084\",\n          \"label\": \"Diammonium hydrogen citrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_basis": "Literal
    raw JSON substring, independently decoded to the located object"}, "decision":
    "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly
    linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting
    that the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}]},
    {"quantity_id": "q7", "topic": "Glucose", "source": {"evidence_id": "togo426",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\":
    20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\":
    \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_basis": "Literal
    raw JSON substring, independently decoded to the located object"}, "decision":
    "unsupported", "rationale": "The current TOGO batch amount agrees with the explicitly
    linked JCM 1 base table. Retain the stated mass on the source recipe basis, noting
    that the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO
    batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated
    mass on the source recipe basis, noting that the 1 L quantity is the solvent input
    rather than an explicit measured-final-volume statement. No stock dilution is
    invented."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The current TOGO
    batch amount agrees with the explicitly linked JCM 1 base table. Retain the stated
    mass on the source recipe basis, noting that the 1 L quantity is the solvent input
    rather than an explicit measured-final-volume statement. No stock dilution is
    invented."}]}, {"quantity_id": "q8", "topic": "hopped beer", "source": {"evidence_id":
    "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"hopped beer\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002246\",\n          \"gmo_id\":
    \"GMO_002246\",\n          \"label\": \"Beer\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_basis": "Literal
    raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "The source specifies 1 L normally hopped beer as the
    solvent replacing water, not 1 g/L beer. Restore a liquid-volume representation
    and replacement relationship. No beer density, alcohol percentage or chemical
    composition is supplied, and no mass conversion is justified.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ingredients[7].concentration",
    "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The source specifies 1 L normally hopped beer as the solvent replacing water,
    not 1 g/L beer. Restore a liquid-volume representation and replacement relationship.
    No beer density, alcohol percentage or chemical composition is supplied, and no
    mass conversion is justified."}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source specifies 1 L normally
    hopped beer as the solvent replacing water, not 1 g/L beer. Restore a liquid-volume
    representation and replacement relationship. No beer density, alcohol percentage
    or chemical composition is supplied, and no mass conversion is justified."}]},
    {"quantity_id": "q9", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id":
    "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\":
    5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path":
    "ingredients[8].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented."}]}, {"quantity_id": "q10", "topic":
    "Beef extract (BD-Difco)", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Beef extract (BD-Difco)\",\n          \"volume\":
    10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001442\",\n          \"gmo_id\":
    \"GMO_001442\",\n          \"label\": \"Bacto &trade; Beef extract, dessicated
    (BD)\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented."}]}, {"quantity_id": "q11", "topic":
    "Casein peptone, tryptic digest", "source": {"evidence_id": "togo426", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426", "raw_path":
    "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T04:32:46.735923+00:00",
    "quote": "{\n          \"component_name\": \"Casein peptone, tryptic digest\",\n          \"volume\":
    10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001615\",\n          \"gmo_id\":
    \"GMO_001615\",\n          \"label\": \"Pancreatic digest of casein\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "unsupported", "rationale": "The current TOGO batch amount
    agrees with the explicitly linked JCM 1 base table. Retain the stated mass on
    the source recipe basis, noting that the 1 L quantity is the solvent input rather
    than an explicit measured-final-volume statement. No stock dilution is invented.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path":
    "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The current TOGO batch amount agrees
    with the explicitly linked JCM 1 base table. Retain the stated mass on the source
    recipe basis, noting that the 1 L quantity is the solvent input rather than an
    explicit measured-final-volume statement. No stock dilution is invented."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "The current TOGO batch amount agrees with the explicitly linked
    JCM 1 base table. Retain the stated mass on the source recipe basis, noting that
    the 1 L quantity is the solvent input rather than an explicit measured-final-volume
    statement. No stock dilution is invented."}]}, {"quantity_id": "q12", "topic":
    "Beer-specific pH and preparation", "source": {"evidence_id": "jcm426", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426", "raw_path": "REVIEW_WORK/batch055/source01-03/jcm426.bin",
    "raw_sha256": "fb8c82340997fc2848d8e4e1ca1223e19456e5b3fdc1976fe9100b35d5af48a9",
    "locator": "Exact426 instruction", "accessed_at": "2026-10-28T04:32:45.979171+00:00",
    "quote": "in normally hopped beer instead of distilled water. Adjust pH to 5.2."},
    "decision": "add", "rationale": "The accessible primary and both provider records
    agree on the Beer-specific pH and solvent replacement.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "ph_value",
    "stored_value": null, "decision": "add", "rationale": "Add exact Beer pH 5.2;
    do not inherit base-MRS pH 6.0–6.5.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "Add exact Beer pH 5.2; do not inherit base-MRS pH 6.0–6.5.", "missing": true},
    {"path": "data/merge_yaml/merged/Beer_Medium.yaml", "field_path": "preparation_steps",
    "stored_value": null, "decision": "add", "rationale": "Add the explicit MRS in
    beer solvent-replacement and pH adjustment instruction.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml", "field_path": "preparation_steps",
    "stored_value": null, "decision": "add", "rationale": "Add the explicit MRS in
    beer solvent-replacement and pH adjustment instruction.", "missing": true}]},
    {"quantity_id": "q13", "topic": "General JCM sterilization instruction", "source":
    {"evidence_id": "jcm426", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/jcm426.bin", "raw_sha256": "fb8c82340997fc2848d8e4e1ca1223e19456e5b3fdc1976fe9100b35d5af48a9",
    "locator": "Page header general instruction", "accessed_at": "2026-10-28T04:32:45.979171+00:00",
    "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for
    15 min."}, "decision": "add", "rationale": "The explicit general instruction appears
    on the exact426 page; no organism temperature, exposure optimization or additional
    treatment is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Beer_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Preserve the primary page general instruction with its unless-otherwise-stated
    scope: 121 °C for 15 min. This is preparation, not an incubation condition.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Preserve the primary page general instruction with its unless-otherwise-stated
    scope: 121 °C for 15 min. This is preparation, not an incubation condition.",
    "missing": true}]}, {"quantity_id": "q14", "topic": "Excluded base-medium pH and
    replaced water", "source": {"evidence_id": "jcm1", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1",
    "raw_path": "REVIEW_WORK/batch055/source01-03/jcm1.bin", "raw_sha256": "41b844456434a1a492b81092c8dafdf7ce9836165130b0f3efabce53d5af993c",
    "locator": "MRS1 base footer and water row", "accessed_at": "2026-10-28T04:32:46.133660+00:00",
    "quote": "Adjust pH to 6.0-6.5."}, "decision": "evidence_only", "rationale": "The
    base pH 6.0–6.5 is explicitly superseded by Beer 5.2, and its 1 L water is replaced
    by beer rather than added alongside it. Base amounts enter only through the 426
    cross-reference; no other parent condition transfers.", "layer_assessments": []},
    {"quantity_id": "q15", "topic": "Unknown beer composition and manganese hydrate
    number", "source": {"evidence_id": "togo426", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M426",
    "raw_path": "REVIEW_WORK/batch055/source01-03/togo426.bin", "raw_sha256": "7ad9c37d468afe126d517d0dc0033d1879eb3fcb1600e2f8850d9e9029f00e31",
    "locator": "$.components[0].items[4,7]", "accessed_at": "2026-10-28T04:32:46.735923+00:00"},
    "decision": "unsupported", "rationale": "The source names normally hopped beer
    and MnSO4 xH2O but does not specify beer density/composition or x. These are explicit
    limits; no new compound, stock strength, alcohol concentration or exact hydrate
    is guessed.", "layer_assessments": []}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - history
  - scalars
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:009811
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009811-manganese-hydrate-milligrams-were-represented-as-grams
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Manganese hydrate milligrams were represented as grams
  description: ingredients[4] stores 50 G_PER_L. Both current TOGO and the linked
    primary MRS table specify 50 mg manganese sulfate x-hydrate. The mass-unit factor
    is 1000, but correcting it does not establish an exact hydrate or measured final-medium
    volume.
  target_ids:
  - CultureMech:009811
  field_paths:
  - ingredients[4].concentration
  evidence_ids:
  - togo426
  - jcm1
  - chebi86360
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-009811-beer-solvent-volume-was-represented-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Beer solvent volume was represented as mass
  description: ingredients[7] stores 1 G_PER_L hopped beer. The source requires 1
    L normally hopped beer in place of the base water. This changes a solvent-volume
    instruction into an unsupported mass concentration.
  target_ids:
  - CultureMech:009811
  field_paths:
  - ingredients[7].concentration
  evidence_ids:
  - togo426
  - jcm426
  - jcm1
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-009811-beer-specific-ph-and-preparation-are-absent
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Beer-specific pH and preparation are absent
  description: Both target and owner omit pH 5.2 and the exact instruction to prepare
    MRS in normally hopped beer. The exact JCM 426 page also gives its general 121
    °C/15 min sterilization instruction. Base MRS pH 6.0–6.5 must not be copied into
    Beer Medium.
  target_ids:
  - CultureMech:009811
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - jcm426
  - jcm1
  - togo426
  - apiJ426
  - writer-togo
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Major despite native P3 completeness: the omitted pH and
    solvent-replacement process distinguish this exact recipe from its linked MRS
    base; the loss changes which medium is represented.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate the maintained owner to preserve 50 mg batch mass on the stated
    recipe basis, retaining unknown hydrate number. Attach exact source evidence and
    regenerate; do not add an unsupported molar conversion.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009811
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Represent the sourced 1 L beer volume and explicit water-replacement
    relationship in the maintained owner. Do not invent density, beer composition
    or an additional 1 L water input; regenerate afterward.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009811
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Add source-scoped pH and preparation to the maintained owner, preserving
    the explicit general sterilization qualifier and separating preparation from growth
    conditions. Regenerate and verify that these instructions survive.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009811
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M426_Beer_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The primary formulation lists a 1 L solvent input, not explicit measured final-volume
  makeup; nominal recipe-basis rates are not presented as independently measured final
  concentrations.
- Normally hopped beer composition/density and manganese sulfate hydrate number are
  unspecified. No culture strain, growth result, incubation condition, beer alcohol
  percentage or exact hydrate is inferred.
- Historical reports are derivative evidence; no claim is made that old external responses
  were recovered. Current primary/provider captures directly support the bounded findings.
- The JCM 1 base pH is excluded because JCM 426 specifies 5.2. Current J426 API lacks
  recipe quantities and does not supply a missing final-volume denominator.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
