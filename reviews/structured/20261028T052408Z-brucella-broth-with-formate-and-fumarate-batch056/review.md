# Scientific review of brucella_broth_with_formate_and_fumarate

- Review: 20261028T052408Z-brucella-broth-with-formate-and-fumarate-batch056
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:12:05.506865Z
- Finished UTC: 2026-10-28T05:24:08.170514Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source identifies a liquid base plus one combined formate/fumarate supplement. All three local mass rates misrepresent source volumes, and the stock/base preparation structure is missing. The valid chemical identities should be retained at the proper stock stage; agar and scratch alternatives do not replace the selected branch.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch056 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008875 | data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml | generated | brucella_broth_with_formate_and_fumarate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008875 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:008875 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:008875 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:008875 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact broad identity with distinct source branches

identity: supported. Targets: CultureMech:008875.

TOGO M2289 points to ATCC 1540, combining the ATCC 1115 base with ATCC 9733. The selected liquid broth is distinct from the PDF agar and optional scratch alternatives. The current three flat ingredient rows do not preserve those layers.

### Organism and performance boundaries

scope: supported. Targets: CultureMech:008875.

The complete selected target and owner and the exact recipe sources name no strain or organism-specific growth experiment. Generic Microbial cultivation is a use category, not empirical growth support. No organism, incubation atmosphere, growth rate or performance claim is inferred from a medium name.

### Historical reports and current writers

provenance: concern. Targets: CultureMech:008875.

The September narrative is independently reassessed; the October target/owner concentration reports explicitly deferred source lookup rather than authenticating the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml distinctly and retains comments. It still maps bare mass units to per-litre enums; _extract_ph reads a root ph key whereas these captured payloads put pH in meta. These inspected behaviors require explicit source-basis and pH review, but do not prove how the old imports ran. The current merger preserves scientific content and rejects incompatible formulations; stale generated data are not evidence that its present logic still discards these fields.

### Supplied chemical identities are valid but assigned to the wrong stage

grounding: supported. Targets: CultureMech:008875.

Current CHEBI:18012 fumaric acid and CHEBI:62965 sodium formate match exact source names, labels, definitions and formulas. Their primary/secondary links should be preserved within the combined stock; chemical correctness does not validate the current final-medium mass rates. The complex base is not a pure compound.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:008875.

All 6 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008875", "selected_concentration_field_count": 6, "selected_concentration_fields_covered": 6, "decisions": [{"decision_id": "q1", "subject": "fumaric acid", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "correct", "stage": "one combined formate/fumarate stock dose", "interpretation": "The source uses one 0.25 ml addition of a combined stock containing both chemicals. The two local 0.25 G_PER_L dry-solute rows lose volume and stock identity. Restore one shared addition, not two separate 0.25 ml doses. Its local final concentration cannot be recovered by treating approximately 5 ml broth as an exact final denominator.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289", "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\": \"fumaric acid\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"conc_value\": 6,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001959\",\n          \"gmo_id\": \"GMO_001959\",\n          \"label\": \"Fumaric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000003\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000003\",\n              \"label\": \"決定培地\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium 1115.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "sodium formate", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "correct", "stage": "one combined formate/fumarate stock dose", "interpretation": "The source uses one 0.25 ml addition of a combined stock containing both chemicals. The two local 0.25 G_PER_L dry-solute rows lose volume and stock identity. Restore one shared addition, not two separate 0.25 ml doses. Its local final concentration cannot be recovered by treating approximately 5 ml broth as an exact final denominator.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289", "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\": \"sodium formate\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"conc_value\": 6,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001491\",\n          \"gmo_id\": \"GMO_001491\",\n          \"label\": \"Sodium formate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium 1115.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "Prepared broth receiving amount", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "prepared ATCC 1115 broth, not powder", "interpretation": "TOGO 5 ml and ATCC approximately 5 ml describe prepared broth in the receiving tube, not 5 g/L powder. Preserve the qualified volume and identify the base independently.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289", "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\": \"Brucella Broth (BD 211088)\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002023\",\n          \"gmo_id\": \"GMO_002023\",\n          \"label\": \"BBL &amp;trade; Brucella broth (BD)\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium 1115.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "Stock batch: Sodium Formate", "local_fields": [], "decision": "evidence_only", "stage": "ATCC 9733 combined stock", "interpretation": "The primary prints 6.0 g of this supplied chemical in the stock recipe. Preserve both rows in the same stock. The explicit 6% heading is a source concentration description; do not infer a final receiving-medium concentration from an approximate tube volume.", "sources": [{"locator": "extracted-text lines 39-39", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Sodium Formate………………………… 6.0 g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 37-37", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "6% Formate and 6% Fumarate Solution (ATCC Medium 9733)", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "Stock batch: Fumaric Acid", "local_fields": [], "decision": "evidence_only", "stage": "ATCC 9733 combined stock", "interpretation": "The primary prints 6.0 g of this supplied chemical in the stock recipe. Preserve both rows in the same stock. The explicit 6% heading is a source concentration description; do not infer a final receiving-medium concentration from an approximate tube volume.", "sources": [{"locator": "extracted-text lines 40-40", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Fumaric Acid……………………………. 6.0 g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 37-37", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "6% Formate and 6% Fumarate Solution (ATCC Medium 9733)", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "Stock water", "local_fields": [], "decision": "evidence_only", "stage": "ATCC 9733 combined stock", "interpretation": "The stock recipe lists 100 ml water. Preserve this preparation amount and the source 6% description without asserting an independently measured 100 ml final stock volume.", "sources": [{"locator": "extracted-text lines 41-41", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "DI Water………………………………… 100.0 mL", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Stock pH and filtration", "local_fields": [], "decision": "evidence_only", "stage": "ATCC 9733 before addition", "interpretation": "The primary explicitly adjusts stock pH 7.0 and filter-sterilizes it. This stock pH is not a measured final pH after mixing with broth.", "sources": [{"locator": "extracted-text lines 43-43", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Adjust pH to 7.0 and filter-sterilize.", "quote_representation": "captured extracted text"}, {"locator": "$.comments[0]", "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289", "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef", "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n      \"paragraph_index\": 1,\n      \"comment\": \"Prepare a solution containing sodium formate and fumaric acid at a concentration of 6% each, adjust the pH to 7.0 and filter-sterilize. Prior to inoculation add 0.25 ml to a tube containing approximately 5 ml Brucella Broth (BD 211088).\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Separate delivery and one use dose", "local_fields": [], "decision": "evidence_only", "stage": "assembly immediately before inoculation", "interpretation": "Retain separate delivery of ATCC 9733 and ATCC 1115 and the single 0.25 ml into approximately 5 ml use instruction. No exact 5.25 ml final volume, additive volume, or exact g/L normalization is inferred.", "sources": [{"locator": "extracted-text lines 46-46", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Note: deliver ATCC Medium 9733 separately from ATCC Medium 1115.", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium 1115.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Broth base: Brucella Broth", "local_fields": [], "decision": "evidence_only", "stage": "commercial ATCC 1115 batch", "interpretation": "The selected liquid branch uses 28 g commercial broth with 1000 ml water. Keep powder preparation separate from the approximately 5 ml prepared-broth dose; listed water does not certify measured final volume.", "sources": [{"locator": "extracted-text lines 5-5", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Brucella Broth……………………………………………………… 28.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Broth base: DI water", "local_fields": [], "decision": "evidence_only", "stage": "commercial ATCC 1115 batch", "interpretation": "The selected liquid branch uses 28 g commercial broth with 1000 ml water. Keep powder preparation separate from the approximately 5 ml prepared-broth dose; listed water does not certify measured final volume.", "sources": [{"locator": "extracted-text lines 6-6", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "DI Water……………………………………………………………. 1000.0 mL", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Broth base sterilization", "local_fields": [], "decision": "evidence_only", "stage": "commercial broth before stock assembly", "interpretation": "Preserve dissolve, dispense and autoclave 121 °C. Do not autoclave the already filter-sterilized combined supplement by collapsing the stages. No holding time or incubation condition is provided.", "sources": [{"locator": "extracted-text lines 8-8", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Mix well until dissolved. Dispense as required and autoclave at 121oC.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Optional scratch branch: Tryptone", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 21-21", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Tryptone(Trypticase)……………………………………. 10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Optional scratch branch: Peptamin", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 22-22", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Peptamin*(Peptone)……………………………………... 10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "Optional scratch branch: Dextrose", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 23-23", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Dextrose…………………………………………………. 1.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "Optional scratch branch: Yeast Extract", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 24-24", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Yeast Extract…………………………………………….. 2.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "Optional scratch branch: NaCl", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 25-25", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "NaCl……………………………………………………… 5.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "Optional scratch branch: Na2S2O5", "local_fields": [], "decision": "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain this printed batch quantity only as an alternative source branch. Do not add it to the commercial powder or infer proprietary composition. The sodium metabisulfite note concerns solid versus aqueous form and does not authorize silently changing a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 26-26", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Na2S2O5**………………………………………………. 0.1 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "Optional scratch water and pH", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch branch", "interpretation": "The scratch table lists 1000 ml water and pH 7.0±0.2. These do not establish exact final volume or final post-supplement pH. Keep the alternative branch separate.", "sources": [{"locator": "extracted-text lines 21-34", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Tryptone(Trypticase)……………………………………. 10.0 g\nPeptamin*(Peptone)……………………………………... 10.0 g\nDextrose…………………………………………………. 1.0 g\nYeast Extract…………………………………………….. 2.0 g\nNaCl……………………………………………………… 5.0 g\nNa2S2O5**………………………………………………. 0.1 g\nDI Water………………………………………………….. 1000.0 mL\n       pH 7.0 +/- 0.2\n\n\n*Peptic Digest of Animal Tissue\n\n**When solid, this product is Sodium metabisulfite. When in water, it yields Sodium\nbisulfite.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "Excluded agar branch", "local_fields": [], "decision": "evidence_only", "stage": "different physical-state variant", "interpretation": "The same PDF separately gives 43 g Brucella Agar/1000 ml water and a cooling/dispensing instruction. This is a source comparison variant, not an omission from the selected liquid broth. Do not add agar or its preparation to this record.", "sources": [{"locator": "extracted-text lines 12-15", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Brucella Agar………………………………………………………. 43.0 g\nDI Water……………………………………………………………. 1000.0 mL\n\nHeat and mix well until dissolved. Autoclave at 121oC. Cool and dispense as required.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch056/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:008875.

data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml: primary 2/3, secondary 2/3; data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml: primary 2/3, secondary 2/3. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI/UBERON term is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Native structural checks

schema: supported. Targets: CultureMech:008875.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: All three source volumes became unrelated mass rates

major / open / confirmed; issue key: culturemech-008875-dose-to-mass.

The two 0.25 G_PER_L values derive from one shared 0.25 ml stock addition, and 5 G_PER_L derives from approximately 5 ml prepared broth. These are different objects and stages, not dry ingredients at those rates.

### f2: The combined stock and prepared broth are not represented

major / open / confirmed; issue key: culturemech-008875-missing-stock-base.

The record lacks the shared ATCC 9733 stock composition, stock water/pH/filtration and separate delivery, and does not distinguish ATCC 1115 powder preparation from the prepared-broth dose. The source agar and scratch alternatives must remain separate.

### f3: Formulation and preparation lack attached source support

minor / open / confirmed; issue key: culturemech-008875-claim-evidence.

Both selected layers expose source URLs only in notes and contain no attached claim excerpts. The empty native reference check does not verify the source recipe. Stock-dose and preparation claims belong in root evidence explicitly scoped to the proposed solutions[*].concentration and preparation_steps[*] stages; SolutionDescriptor and PreparationStep have no evidence slot.

## Recommended Actions And Acceptance Checks

### action1

Restore the source volume objects and approximate receiving quantity; avoid double-counting the shared supplement or guessing a final denominator.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Represent the exact base and combined supplement with scoped preparation and source batch amounts. Preserve the two chemical identities in stock composition and the liquid-branch boundary.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Attach exact primary excerpts and references separately for base, supplement and use stage; retain source uncertainty and do not assert growth support.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch056/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch056/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch056/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch056/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| togoM2289 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| atccOld | https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| chebi18012 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18012; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18012 = fumaric acid; definition ['A butenedioic acid in which the C=C double bond has &lt;i&gt;E&lt;/i&gt; geometry. It is an intermediate metabolite in the citric acid cycle.']; formula ['C4H4O4']; mass ['116.072']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62965 = sodium formate; definition ['An organic sodium salt which is the monosodium salt of formic acid.']; formula ['CHO2.Na']; mass ['68.007']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch056/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T004446Z-Brucella_broth_with_formate_and_fumarate.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| writer14 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer15 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer16 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer17 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch056/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The receiving broth is approximately 5 ml; no exact post-addition final volume or normalized final chemical concentration is justified.
- Source 6% stock wording and 6 g/100 ml water quantities are retained, without inventing measured stock volume or mixing additivity.
- ATCC explicitly separates agar and scratch alternatives. No proprietary product equivalence, organism-specific growth or incubation condition is inferred.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T052408Z-brucella-broth-with-formate-and-fumarate-batch056
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of brucella_broth_with_formate_and_fumarate
started_at: '2026-10-28T05:12:05.506865Z'
finished_at: '2026-10-28T05:24:08.170514Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The source identifies a liquid base plus one combined formate/fumarate supplement.
  All three local mass rates misrepresent source volumes, and the stock/base preparation
  structure is missing. The valid chemical identities should be retained at the proper
  stock stage; agar and scratch alternatives do not replace the selected branch.
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
  - path: data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
    sha256: 45a9ee465a809f8424cd540738e14cb7af9ad632c4bc5d74403a02f522458d3b
    role: target
  - path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
    sha256: 9a99ab90b113e6fe0c8aa6742da73804db0742a6dbfde63451ddfc4cb35d7e7e
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.md
    sha256: 68481a0e51cedaaf797858aa68991514ed8f2534942ab7b7360b64a97b56aded
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.md
    sha256: 247ff2f16ce598e2097cf17ab40b5aebe49d8e50631a11b589fef00241d7a5f1
    role: context
  - path: reports/yaml_record_review/20260922T004446Z-Brucella_broth_with_formate_and_fumarate.md
    sha256: 8b56845e805c5f2e0ec5443f343081b03a6f91dd5f6edd58d1170bf0fed7d927
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
  selection: Authoritative batch056 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008875
targets:
- target_id: CultureMech:008875
  path: data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
  label: brucella_broth_with_formate_and_fumarate
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008875
  command: just validate-schema data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008875
  command: just validate-strict data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
    --workers 1 --out REVIEW_WORK/batch056/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008875
  command: just validate-terms data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:008875
  command: just validate-references data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:10.948099Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 45a9ee465a809f8424cd540738e14cb7af9ad632c4bc5d74403a02f522458d3b
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:10.948291Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 9a99ab90b113e6fe0c8aa6742da73804db0742a6dbfde63451ddfc4cb35d7e7e
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch056/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:06.654193Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 0a4e21bf835380bea32535a432081fd519f590112b2d3d60d1b397e60d63b544
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch056/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:07.715614Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 352b006d5903dfc0a0b628ee0fa87a20f0e6e2a048014f1405f1b4dc509a928e
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch056/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:08.902282Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2d088df1f2146cda3ad1d9abeaa5e365dc5aabe475b3fa73b6ffc23679fa9fe4
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch056/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:09.619466Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 7a04f7fd49b713d8be59fae7f66e21dc258811b20e4f197e8f708baca4de17e6
- evidence_id: togoM2289
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:24.953851Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: 2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef
- evidence_id: atccOld
  kind: primary_source
  reference: https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:24.953913Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: 0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab
- evidence_id: chebi18012
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18012
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:24.953973Z'
  support: supports
  summary: OLS current exact CHEBI:18012 = fumaric acid; definition ['A butenedioic
    acid in which the C=C double bond has <i>E</i> geometry. It is an intermediate
    metabolite in the citric acid cycle.']; formula ['C4H4O4']; mass ['116.072'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: b98b7dc71ebd871e4fa296cca103eb821dcca0cc557727b75d32ddaa8906f79e
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:25.725797Z'
  support: supports
  summary: OLS current exact CHEBI:62965 = sodium formate; definition ['An organic
    sodium salt which is the monosodium salt of formic acid.']; formula ['CHO2.Na'];
    mass ['68.007']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f36b7c1107922c948bf6387ce77e0468c3fcdf76ce80969b5411b600e051910d
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch056/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T05:18:10.950277Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 555aa5ac88862ae60818b7d7088a0e30c68124031728fe9e56aab1ae5033b5ea
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T004446Z-Brucella_broth_with_formate_and_fumarate.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.950313Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 8b56845e805c5f2e0ec5443f343081b03a6f91dd5f6edd58d1170bf0fed7d927
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.950346Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 247ff2f16ce598e2097cf17ab40b5aebe49d8e50631a11b589fef00241d7a5f1
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.950369Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 68481a0e51cedaaf797858aa68991514ed8f2534942ab7b7360b64a97b56aded
- evidence_id: writer14
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.950407Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer15
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.950429Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer16
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.950451Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer17
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.950479Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch056/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T05:18:10.975234Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 04eec160e02ab2abe423e55b065cd960b607d9945c202ecf91317d0e8f8f388d
assessments:
- assessment_id: a1
  area: identity
  topic: Exact broad identity with distinct source branches
  outcome: supported
  summary: TOGO M2289 points to ATCC 1540, combining the ATCC 1115 base with ATCC
    9733. The selected liquid broth is distinct from the PDF agar and optional scratch
    alternatives. The current three flat ingredient rows do not preserve those layers.
  target_ids:
  - CultureMech:008875
  evidence_ids:
  - atccOld
  - togoM2289
  - local0
  - local1
- assessment_id: a2
  area: scope
  topic: Organism and performance boundaries
  outcome: supported
  summary: The complete selected target and owner and the exact recipe sources name
    no strain or organism-specific growth experiment. Generic Microbial cultivation
    is a use category, not empirical growth support. No organism, incubation atmosphere,
    growth rate or performance claim is inferred from a medium name.
  target_ids:
  - CultureMech:008875
  evidence_ids:
  - atccOld
  - togoM2289
  - local0
  - local1
- assessment_id: a3
  area: provenance
  topic: Historical reports and current writers
  outcome: concern
  summary: The September narrative is independently reassessed; the October target/owner
    concentration reports explicitly deferred source lookup rather than authenticating
    the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml
    distinctly and retains comments. It still maps bare mass units to per-litre enums;
    _extract_ph reads a root ph key whereas these captured payloads put pH in meta.
    These inspected behaviors require explicit source-basis and pH review, but do
    not prove how the old imports ran. The current merger preserves scientific content
    and rejects incompatible formulations; stale generated data are not evidence that
    its present logic still discards these fields.
  target_ids:
  - CultureMech:008875
  evidence_ids:
  - local0
  - local1
  - history0
  - history1
  - history2
  - writer14
  - writer15
  - writer16
  - writer17
- assessment_id: a4
  area: grounding
  topic: Supplied chemical identities are valid but assigned to the wrong stage
  outcome: supported
  summary: Current CHEBI:18012 fumaric acid and CHEBI:62965 sodium formate match exact
    source names, labels, definitions and formulas. Their primary/secondary links
    should be preserved within the combined stock; chemical correctness does not validate
    the current final-medium mass rates. The complex base is not a pure compound.
  target_ids:
  - CultureMech:008875
  evidence_ids:
  - chebi18012
  - chebi62965
  - grounding
  - atccOld
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 6 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:008875
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008875",
    "selected_concentration_field_count": 6, "selected_concentration_fields_covered":
    6, "decisions": [{"decision_id": "q1", "subject": "fumaric acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "one combined formate/fumarate stock
    dose", "interpretation": "The source uses one 0.25 ml addition of a combined stock
    containing both chemicals. The two local 0.25 G_PER_L dry-solute rows lose volume
    and stock identity. Restore one shared addition, not two separate 0.25 ml doses.
    Its local final concentration cannot be recovered by treating approximately 5
    ml broth as an exact final denominator.", "sources": [{"locator": "$.components[0].items[0]",
    "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289",
    "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\":
    \"fumaric acid\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"conc_value\":
    6,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001959\",\n          \"gmo_id\":
    \"GMO_001959\",\n          \"label\": \"Fumaric acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000003\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000003\",\n              \"label\": \"決定培地\"\n            },\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to
    inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium
    1115.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q2", "subject": "sodium formate", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "one combined formate/fumarate stock
    dose", "interpretation": "The source uses one 0.25 ml addition of a combined stock
    containing both chemicals. The two local 0.25 G_PER_L dry-solute rows lose volume
    and stock identity. Restore one shared addition, not two separate 0.25 ml doses.
    Its local final concentration cannot be recovered by treating approximately 5
    ml broth as an exact final denominator.", "sources": [{"locator": "$.components[0].items[1]",
    "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289",
    "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\":
    \"sodium formate\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"conc_value\":
    6,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001491\",\n          \"gmo_id\":
    \"GMO_001491\",\n          \"label\": \"Sodium formate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text
    lines 47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to
    inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium
    1115.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q3", "subject": "Prepared broth receiving amount", "local_fields": [{"record_path":
    "data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "prepared ATCC 1115 broth, not powder",
    "interpretation": "TOGO 5 ml and ATCC approximately 5 ml describe prepared broth
    in the receiving tube, not 5 g/L powder. Preserve the qualified volume and identify
    the base independently.", "sources": [{"locator": "$.components[0].items[2]",
    "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289",
    "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n          \"component_name\":
    \"Brucella Broth (BD 211088)\",\n          \"volume\": 5,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002023\",\n          \"gmo_id\":
    \"GMO_002023\",\n          \"label\": \"BBL &trade; Brucella broth (BD)\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    47-48", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to
    inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium
    1115.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q4", "subject": "Stock batch: Sodium Formate", "local_fields": [], "decision":
    "evidence_only", "stage": "ATCC 9733 combined stock", "interpretation": "The primary
    prints 6.0 g of this supplied chemical in the stock recipe. Preserve both rows
    in the same stock. The explicit 6% heading is a source concentration description;
    do not infer a final receiving-medium concentration from an approximate tube volume.",
    "sources": [{"locator": "extracted-text lines 39-39", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Sodium Formate…………………………
    6.0 g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 37-37", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "6% Formate
    and 6% Fumarate Solution (ATCC Medium 9733)", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q5", "subject": "Stock batch: Fumaric Acid",
    "local_fields": [], "decision": "evidence_only", "stage": "ATCC 9733 combined
    stock", "interpretation": "The primary prints 6.0 g of this supplied chemical
    in the stock recipe. Preserve both rows in the same stock. The explicit 6% heading
    is a source concentration description; do not infer a final receiving-medium concentration
    from an approximate tube volume.", "sources": [{"locator": "extracted-text lines
    40-40", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Fumaric Acid…………………………….
    6.0 g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 37-37", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "6% Formate
    and 6% Fumarate Solution (ATCC Medium 9733)", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q6", "subject": "Stock water", "local_fields":
    [], "decision": "evidence_only", "stage": "ATCC 9733 combined stock", "interpretation":
    "The stock recipe lists 100 ml water. Preserve this preparation amount and the
    source 6% description without asserting an independently measured 100 ml final
    stock volume.", "sources": [{"locator": "extracted-text lines 41-41", "source_key":
    "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "DI Water…………………………………
    100.0 mL", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q7", "subject": "Stock pH and filtration", "local_fields": [], "decision": "evidence_only",
    "stage": "ATCC 9733 before addition", "interpretation": "The primary explicitly
    adjusts stock pH 7.0 and filter-sterilizes it. This stock pH is not a measured
    final pH after mixing with broth.", "sources": [{"locator": "extracted-text lines
    43-43", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Adjust pH
    to 7.0 and filter-sterilize.", "quote_representation": "captured extracted text"},
    {"locator": "$.comments[0]", "source_key": "togoM2289", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2289",
    "source_raw_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "source_text_sha256": "2ccbe6d63a2cafe7e0e106e62d771188463334f05a26f19cd0ce9ad20fc6ffef",
    "accessed_at": "2026-10-28T05:12:24.953851Z", "exact_source_quote": "{\n      \"paragraph_index\":
    1,\n      \"comment\": \"Prepare a solution containing sodium formate and fumaric
    acid at a concentration of 6% each, adjust the pH to 7.0 and filter-sterilize.
    Prior to inoculation add 0.25 ml to a tube containing approximately 5 ml Brucella
    Broth (BD 211088).\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q8", "subject": "Separate delivery and one use dose", "local_fields": [], "decision":
    "evidence_only", "stage": "assembly immediately before inoculation", "interpretation":
    "Retain separate delivery of ATCC 9733 and ATCC 1115 and the single 0.25 ml into
    approximately 5 ml use instruction. No exact 5.25 ml final volume, additive volume,
    or exact g/L normalization is inferred.", "sources": [{"locator": "extracted-text
    lines 46-46", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Note: deliver
    ATCC Medium 9733 separately from ATCC Medium 1115.", "quote_representation": "captured
    extracted text"}, {"locator": "extracted-text lines 47-48", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Prior to
    inoculation, 0.25 ml is added to a tube containing approximately 5 ml of ATCC\nMedium
    1115.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q9", "subject": "Broth base: Brucella Broth", "local_fields": [], "decision":
    "evidence_only", "stage": "commercial ATCC 1115 batch", "interpretation": "The
    selected liquid branch uses 28 g commercial broth with 1000 ml water. Keep powder
    preparation separate from the approximately 5 ml prepared-broth dose; listed water
    does not certify measured final volume.", "sources": [{"locator": "extracted-text
    lines 5-5", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Brucella
    Broth……………………………………………………… 28.0 g", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q10", "subject": "Broth base: DI water", "local_fields":
    [], "decision": "evidence_only", "stage": "commercial ATCC 1115 batch", "interpretation":
    "The selected liquid branch uses 28 g commercial broth with 1000 ml water. Keep
    powder preparation separate from the approximately 5 ml prepared-broth dose; listed
    water does not certify measured final volume.", "sources": [{"locator": "extracted-text
    lines 6-6", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "DI Water…………………………………………………………….
    1000.0 mL", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "Broth base sterilization", "local_fields": [], "decision":
    "evidence_only", "stage": "commercial broth before stock assembly", "interpretation":
    "Preserve dissolve, dispense and autoclave 121 °C. Do not autoclave the already
    filter-sterilized combined supplement by collapsing the stages. No holding time
    or incubation condition is provided.", "sources": [{"locator": "extracted-text
    lines 8-8", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Mix well
    until dissolved. Dispense as required and autoclave at 121oC.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q12", "subject": "Optional scratch
    branch: Tryptone", "local_fields": [], "decision": "evidence_only", "stage": "alternative
    base formulation", "interpretation": "Retain this printed batch quantity only
    as an alternative source branch. Do not add it to the commercial powder or infer
    proprietary composition. The sodium metabisulfite note concerns solid versus aqueous
    form and does not authorize silently changing a supplied reagent identity.", "sources":
    [{"locator": "extracted-text lines 21-21", "source_key": "atccOld", "reference":
    "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx", "source_raw_sha256":
    "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab", "source_text_sha256":
    "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac", "accessed_at":
    "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Tryptone(Trypticase)…………………………………….
    10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "Optional scratch branch: Peptamin", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain
    this printed batch quantity only as an alternative source branch. Do not add it
    to the commercial powder or infer proprietary composition. The sodium metabisulfite
    note concerns solid versus aqueous form and does not authorize silently changing
    a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 22-22",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Peptamin*(Peptone)……………………………………...
    10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q14", "subject": "Optional scratch branch: Dextrose", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain
    this printed batch quantity only as an alternative source branch. Do not add it
    to the commercial powder or infer proprietary composition. The sodium metabisulfite
    note concerns solid versus aqueous form and does not authorize silently changing
    a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 23-23",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Dextrose………………………………………………….
    1.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q15", "subject": "Optional scratch branch: Yeast Extract", "local_fields": [],
    "decision": "evidence_only", "stage": "alternative base formulation", "interpretation":
    "Retain this printed batch quantity only as an alternative source branch. Do not
    add it to the commercial powder or infer proprietary composition. The sodium metabisulfite
    note concerns solid versus aqueous form and does not authorize silently changing
    a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 24-24",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Yeast Extract……………………………………………..
    2.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q16", "subject": "Optional scratch branch: NaCl", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain
    this printed batch quantity only as an alternative source branch. Do not add it
    to the commercial powder or infer proprietary composition. The sodium metabisulfite
    note concerns solid versus aqueous form and does not authorize silently changing
    a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 25-25",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "NaCl………………………………………………………
    5.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q17", "subject": "Optional scratch branch: Na2S2O5", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative base formulation", "interpretation": "Retain
    this printed batch quantity only as an alternative source branch. Do not add it
    to the commercial powder or infer proprietary composition. The sodium metabisulfite
    note concerns solid versus aqueous form and does not authorize silently changing
    a supplied reagent identity.", "sources": [{"locator": "extracted-text lines 26-26",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Na2S2O5**……………………………………………….
    0.1 g", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q18", "subject": "Optional scratch water and pH", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative scratch branch", "interpretation": "The
    scratch table lists 1000 ml water and pH 7.0±0.2. These do not establish exact
    final volume or final post-supplement pH. Keep the alternative branch separate.",
    "sources": [{"locator": "extracted-text lines 21-34", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Tryptone(Trypticase)…………………………………….
    10.0 g\nPeptamin*(Peptone)……………………………………... 10.0 g\nDextrose………………………………………………….
    1.0 g\nYeast Extract…………………………………………….. 2.0 g\nNaCl……………………………………………………… 5.0 g\nNa2S2O5**……………………………………………….
    0.1 g\nDI Water………………………………………………….. 1000.0 mL\n       pH 7.0 +/- 0.2\n\n\n*Peptic
    Digest of Animal Tissue\n\n**When solid, this product is Sodium metabisulfite.
    When in water, it yields Sodium\nbisulfite.", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q19", "subject": "Excluded agar branch",
    "local_fields": [], "decision": "evidence_only", "stage": "different physical-state
    variant", "interpretation": "The same PDF separately gives 43 g Brucella Agar/1000
    ml water and a cooling/dispensing instruction. This is a source comparison variant,
    not an omission from the selected liquid broth. Do not add agar or its preparation
    to this record.", "sources": [{"locator": "extracted-text lines 12-15", "source_key":
    "atccOld", "reference": "https://www.atcc.org/~/media/2DA0E266AE7E419288C2291420B9E93E.ashx",
    "source_raw_sha256": "0431020453f41086b17986ae2509575753df903e31d3e74efc33aea07de666ab",
    "source_text_sha256": "b7135c2e40261d46ab084b2e61a89a1fa8af3652b3336ef443e056d5fb3d79ac",
    "accessed_at": "2026-10-28T05:12:24.953913Z", "exact_source_quote": "Brucella
    Agar………………………………………………………. 43.0 g\nDI Water……………………………………………………………. 1000.0 mL\n\nHeat
    and mix well until dissolved. Autoclave at 121oC. Cool and dispense as required.",
    "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch056/record05/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml:
    primary 2/3, secondary 2/3; data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml:
    primary 2/3, secondary 2/3. These are ingredient-instance linkage fractions, not
    accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI/UBERON term is joined to its exact current OLS object and packaged MIM CSV
    rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected
    documents; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:008875
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
  - CultureMech:008875
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-008875-dose-to-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: All three source volumes became unrelated mass rates
  description: The two 0.25 G_PER_L values derive from one shared 0.25 ml stock addition,
    and 5 G_PER_L derives from approximately 5 ml prepared broth. These are different
    objects and stages, not dry ingredients at those rates.
  target_ids:
  - CultureMech:008875
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  evidence_ids:
  - atccOld
  - togoM2289
  rule_id: source-quantity-unit-stage
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008875-missing-stock-base
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The combined stock and prepared broth are not represented
  description: The record lacks the shared ATCC 9733 stock composition, stock water/pH/filtration
    and separate delivery, and does not distinguish ATCC 1115 powder preparation from
    the prepared-broth dose. The source agar and scratch alternatives must remain
    separate.
  target_ids:
  - CultureMech:008875
  field_paths:
  - solutions
  - preparation_steps
  - ph_value
  - ingredients
  evidence_ids:
  - atccOld
  - togoM2289
  rule_id: source-stock-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008875-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Formulation and preparation lack attached source support
  description: Both selected layers expose source URLs only in notes and contain no
    attached claim excerpts. The empty native reference check does not verify the
    source recipe. Stock-dose and preparation claims belong in root evidence explicitly
    scoped to the proposed solutions[*].concentration and preparation_steps[*] stages;
    SolutionDescriptor and PreparationStep have no evidence slot.
  target_ids:
  - CultureMech:008875
  field_paths:
  - references
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - grounding
  - atccOld
  - togoM2289
  rule_id: source-specific-formulation-fidelity
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore the source volume objects and approximate receiving quantity;
    avoid double-counting the shared supplement or guessing a final denominator.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008875
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
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
  description: Represent the exact base and combined supplement with scoped preparation
    and source batch amounts. Preserve the two chemical identities in stock composition
    and the liquid-branch boundary.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008875
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
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
  description: Attach exact primary excerpts and references separately for base, supplement
    and use stage; retain source uncertainty and do not assert growth support.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008875
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml
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
- The receiving broth is approximately 5 ml; no exact post-addition final volume or
  normalized final chemical concentration is justified.
- Source 6% stock wording and 6 g/100 ml water quantities are retained, without inventing
  measured stock volume or mixing additivity.
- ATCC explicitly separates agar and scratch alternatives. No proprietary product
  equivalence, organism-specific growth or incubation condition is inferred.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
