# Brucella Blood Agar: preserve stock repairs and qualify unresolved main-volume basis

- Review: 20261028T052236Z-batch056-record02-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:11:04.555553Z
- Finished UTC: 2026-10-28T05:22:36.456493Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated M696 record is stale relative to its repaired normalized owner. The exact JCM677 table supports batch quantities, while JCM469 explicitly supports the two stock makeups. Owner stock strengths are credited, but main per-liter denominators and the imposed processing sequence are not fully supported. Only the linked stock portions of M470 are assessed.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch056 native selection index 02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010102 | data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml | generated | brucella_blood_agar_with_hemin_menadione |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010102 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:010102 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:010102 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:010102 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact JCM677 identity and linked stock scope

identity: supported. Targets: CultureMech:010102.

TOGO M696 and current JCM677 identify the selected recipe. JCM469/M470 is a scoped stock dependency, not a contributing owner or alternative source of the whole receiving formula. No strain-specific claim follows from the recipe title.

### Current terms and undefined materials

grounding: supported. Targets: CultureMech:010102.

All asserted selected/owner chemical labels match exact current OLS objects. The alkaline stock identifies sodium hydroxide as a chemical in a normal solution; it is not evidence of pure hydroxide mass. Commercial Brucella agar and horse blood remain complex materials. The dependency medium/provider identifiers are structural references, outside the MIM chemical validity test.

### Unchanged classification and source boundaries

scope: supported. Targets: CultureMech:010102.

COMPLEX, UNDEFINED, SOLID_AGAR and generic cultivation application are consistent with the table. The owner already carries structured references, corrected liquid dimensions and supported stock strengths; these are credited. Neither primary specifies a target organism or a pH for JCM677; no such claim is added.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:010102.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696", "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T05:11:33.357211Z", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}}, "decision": "mixed", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1000", "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis."}]}, {"quantity_id": "q2", "topic": "Horse blood", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696", "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T05:11:33.357211Z", "exact_decoded_object": {"component_name": "Horse blood", "volume": 50, "unit": "ml", "gmo": "http://purl.jp/bio/10/gmo/GMO_001562", "gmo_id": "GMO_001562", "label": "Horse blood", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles": [{"id": "GMO_000042", "uri": "http://purl.jp/bio/10/gmo/GMO_000042", "label": "Nutrient source"}]}}, "decision": "mixed", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "50.0", "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup. The generated target additionally represents a liquid volume as a mass rate; correct that dimensional error on the source batch basis."}]}, {"quantity_id": "q3", "topic": "Brucella agar", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696", "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T05:11:33.357211Z", "exact_decoded_object": {"component_name": "Brucella agar (BD-BBL)", "volume": 43, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001522", "gmo_id": "GMO_001522", "label": "BBL &amp;trade; Brucella agar", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}, {"id": "GMO_000050", "uri": "http://purl.jp/bio/10/gmo/GMO_000050", "label": "Complex component"}], "roles": []}}, "decision": "unsupported", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "43", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "43.0", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The exact source supplies a batch amount, alongside a listed water input, without declaring final-medium volume. The owner preserves the correct source magnitude and physical dimension, but its per-liter denominator remains unsupported. Do not sum liquid additions or silently reinterpret input water as final makeup."}]}, {"quantity_id": "q4", "topic": "Hemin solution receiving addition", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696", "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f", "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T05:11:33.357211Z", "exact_decoded_object": {"component_name": "Hemin solution (see Medium [M470])", "volume": 10, "unit": "ml", "reference_media_id": "M470", "properties": [], "roles": []}}, "decision": "mixed", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10.0", "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred."}]}, {"quantity_id": "q5", "topic": "Menadione solution receiving addition", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696", "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f", "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T05:11:33.357211Z", "exact_decoded_object": {"component_name": "Menadione solution (see Medium [M470])", "volume": 10, "unit": "ml", "reference_media_id": "M470", "properties": [], "roles": []}}, "decision": "mixed", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "10.0", "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "JCM677 explicitly lists this stock addition as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension and magnitude are credited but its per-liter qualifier is unresolved because JCM677 has no explicit final-volume statement. The final-dose statement in parent JCM469 belongs to its TSA medium and is not transferred."}]}, {"quantity_id": "q6", "topic": "Hemin stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "mixed", "rationale": "The source explicitly adjusts the stock to 100 mL final volume: 50 mg / 100 mL = 0.5 g/L. The existing owner stock solute concentration is supported; add claim-level linkage.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].composition[0].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source explicitly adjusts the stock to 100 mL final volume: 50 mg / 100 mL = 0.5 g/L. The existing owner stock solute concentration is supported; add claim-level linkage."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Restore the supported composition from the maintained owner while preserving its stock stage; an empty list currently lacks these ingredients."}]}, {"quantity_id": "q7", "topic": "Hemin stock initial solvent", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "mixed", "rationale": "The source uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No molarity, density or receiving dilution is invented.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].composition[1].concentration", "stored_value": {"value": "10.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No molarity, density or receiving dilution is invented."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Restore the supported composition from the maintained owner while preserving its stock stage; an empty list currently lacks these ingredients."}]}, {"quantity_id": "q8", "topic": "Hemin stock preparation and final makeup", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].preparation_notes", "stored_value": null, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].preparation_notes", "stored_value": null, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "missing": true}]}, {"quantity_id": "q9", "topic": "Hemin placeholder shell and retained name", "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b", "locator": "Exact named stock cross-reference", "accessed_at": "2026-10-28T05:11:33.651507Z", "quote": "Hemin solution"}, "decision": "mixed", "rationale": "The generated placeholder is stale; the exact owner preferred term is already supported.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder with the already supported specific stock name."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[0].preferred_term", "stored_value": "Hemin solution", "decision": "evidence_only", "rationale": "Retain the correct named stock; this field needs evidence linkage, not a replacement."}]}, {"quantity_id": "q10", "topic": "Menadione stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume to 100 ml."}, "decision": "mixed", "rationale": "The source explicitly adjusts the stock to 100 mL final volume: 5 mg / 100 mL = 0.05 g/L. The existing owner stock solute concentration is supported; add claim-level linkage.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source explicitly adjusts the stock to 100 mL final volume: 5 mg / 100 mL = 0.05 g/L. The existing owner stock solute concentration is supported; add claim-level linkage."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Restore the supported composition from the maintained owner while preserving its stock stage; an empty list currently lacks these ingredients."}]}, {"quantity_id": "q11", "topic": "Menadione stock initial solvent", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume to 100 ml."}, "decision": "mixed", "rationale": "The source uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No molarity, density or receiving dilution is invented.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].composition[1].concentration", "stored_value": {"value": "10.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No molarity, density or receiving dilution is invented."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Restore the supported composition from the maintained owner while preserving its stock stage; an empty list currently lacks these ingredients."}]}, {"quantity_id": "q12", "topic": "Menadione stock preparation and final makeup", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume to 100 ml."}, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].preparation_notes", "stored_value": null, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].preparation_notes", "stored_value": null, "decision": "add", "rationale": "The exact stock subsection supplies dissolve-first order and an explicit final-makeup volume. These details are not represented by composition alone; retain them as stock preparation, without importing the parent TSA medium or assuming the makeup liquid identity beyond what is printed.", "missing": true}]}, {"quantity_id": "q13", "topic": "Menadione placeholder shell and retained name", "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b", "locator": "Exact named stock cross-reference", "accessed_at": "2026-10-28T05:11:33.651507Z", "quote": "Menadione solution"}, "decision": "mixed", "rationale": "The generated placeholder is stale; the exact owner preferred term is already supported.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder with the already supported specific stock name."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "solutions[1].preferred_term", "stored_value": "Menadione solution", "decision": "evidence_only", "rationale": "Retain the correct named stock; this field needs evidence linkage, not a replacement."}]}, {"quantity_id": "q14", "topic": "Existing owner preparation step 1", "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b", "locator": "Complete table; no ordered preparation text", "accessed_at": "2026-10-28T05:11:33.651507Z"}, "decision": "unsupported", "rationale": "The numerical batch inputs can be traced to the primary table, but that table does not prescribe this step ordering. The addition step also introduces unsupported per-liter qualifiers. Preserve source quantities separately and qualify or remove the invented ordered instruction; no replacement order is inferred.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Suspend 43.0 g Brucella agar (BD-BBL) in 1.0 L distilled water.", "decision": "unsupported", "rationale": "The numerical batch inputs can be traced to the primary table, but that table does not prescribe this step ordering. The addition step also introduces unsupported per-liter qualifiers. Preserve source quantities separately and qualify or remove the invented ordered instruction; no replacement order is inferred."}]}, {"quantity_id": "q15", "topic": "Existing owner preparation step 2", "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b", "locator": "Complete table; no ordered preparation text", "accessed_at": "2026-10-28T05:11:33.651507Z"}, "decision": "unsupported", "rationale": "The numerical batch inputs can be traced to the primary table, but that table does not prescribe this step ordering. The addition step also introduces unsupported per-liter qualifiers. Preserve source quantities separately and qualify or remove the invented ordered instruction; no replacement order is inferred.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Add 50.0 ml/L horse blood, 10.0 ml/L hemin solution, and 10.0 ml/L menadione solution.", "decision": "unsupported", "rationale": "The numerical batch inputs can be traced to the primary table, but that table does not prescribe this step ordering. The addition step also introduces unsupported per-liter qualifiers. Preserve source quantities separately and qualify or remove the invented ordered instruction; no replacement order is inferred."}]}, {"quantity_id": "q16", "topic": "General sterilization header", "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b", "locator": "General page header", "accessed_at": "2026-10-28T05:11:33.651507Z", "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}, "decision": "mixed", "rationale": "The source explicitly states the general sterilization instruction. Its numbers are supported; a complete ordered process after blood/stock addition is not thereby authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "preparation_steps[2].description", "stored_value": "Autoclave at 121 C for 15 min unless otherwise stated.", "decision": "evidence_only", "rationale": "The temperature and duration match the primary general header; credit this content without treating its position after all additions as independently supported."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "sterilization.method", "stored_value": "AUTOCLAVE", "decision": "evidence_only", "rationale": "The general primary header supports the method, with its unless-otherwise-stated qualification."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path": "sterilization", "stored_value": null, "decision": "add", "rationale": "Restore only source-qualified method metadata, preserving the general-header scope.", "missing": true}]}, {"quantity_id": "q17", "topic": "Scoped M470 dependency: Initial alkaline solvent volume and normality", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]}, {"quantity_id": "q18", "topic": "Scoped M470 dependency: Collapsed water / final-makeup context", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported. The single collapsed water field cannot stand for both independently made stocks. The primary specifies final makeup to 100 mL for each; it does not print 100 g/L water.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "100.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported. The single collapsed water field cannot stand for both independently made stocks. The primary specifies final makeup to 100 mL for each; it does not print 100 g/L water."}]}, {"quantity_id": "q19", "topic": "Scoped M470 dependency: Hemin stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]}, {"quantity_id": "q20", "topic": "Scoped M470 dependency: Initial ethanol volume", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]}, {"quantity_id": "q21", "topic": "Scoped M470 dependency: Menadione stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z", "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock content flattened into direct ingredient mass rates. The exact JCM469 stock subsection supports a distinct stock amount/final-makeup representation, not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]}, {"quantity_id": "q22", "topic": "Excluded parent-medium quantities", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4", "locator": "Parent TSA paragraph, excluded from M696 receiving-dose support", "accessed_at": "2026-10-28T05:11:34.009484Z"}, "decision": "not_assessed", "rationale": "M470 solutions[0:3] receiving concentrations and JCM469 TSA156 parent composition are excluded from quantitative assessment here. They are not used to fill JCM677 final-volume or addition-dose evidence.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:010102.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:010102.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:010102.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:010102.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Generated content omits supported owner stock repairs

major / open / confirmed; issue key: culturemech-010102-generated-content-omits-supported-owner-stock-repairs.

The generated file retains liquid additions as mass rates, empty stock compositions and Unknown solution names. Its maintained owner already has liquid dimensions, both supported stock compositions and structured source references. Preserve those repairs, but do not regenerate unresolved main denominator or ordering claims as if verified.

### f2: Main per-liter denominators exceed the printed batch basis

major / open / confirmed; issue key: culturemech-010102-main-per-liter-denominators-exceed-the-printed-batch-basis.

The primary table supplies amounts and a water input without explicitly declaring final-medium volume. The owner has corrected liquid dimensions but expresses all main rows and additions per liter, and its second preparation step repeats those qualifiers. JCM469 final receiving doses apply to a different parent medium.

### f3: Owner preparation imposes an unsupported process order

major / open / confirmed; issue key: culturemech-010102-owner-preparation-imposes-an-unsupported-process-order.

The owner orders suspension, all liquid additions, then autoclaving. JCM677 supplies a table and a general sterilization header, not that exact ordered process. The supported header values must remain scoped without asserting the point at which blood or stock additions are treated.

### f4: Linked stock dependency still flattens stock contents

major / open / confirmed; issue key: culturemech-010102-linked-stock-dependency-still-flattens-stock-contents.

Within the explicitly linked M470 dependency, five direct ingredients encode stock solute/solvent/makeup information as mass rates. This is separate from the selected owner, whose stock strengths were repaired. Restore only the two linked stock scopes; do not transfer or assess its unrelated TSA parent formula.

## Recommended Actions And Acceptance Checks

### action1

Reconcile remaining owner basis/process limits, then regenerate the target with the supported stock composition and specific names. Keep the exact source batch amounts and named stocks; no cross-source whole-medium substitution.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Preserve batch amounts with explicit basis and qualify unsupported main per-liter interpretations until an exact final-volume statement is verified. Keep valid stock-level concentrations intact; do not infer final volume by summing additions.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Separate the source-supported general header and batch quantities from inferred processing order. Document the unresolved order rather than supply a replacement protocol without exact evidence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Repair the two exact linked stock representations with their primary stock-stage amounts, solvent normality/volume and explicit final makeup. Preserve the parent-medium boundary and do not add a JCM677 receiving dose from JCM469.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| stock-dependency | data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml; ingredients[0:5]; source pointers/history; solutions are structural context only | context_only | Complete dependency read for identity/history; scientific scope is only its hemin/menadione stock ingredients and representation. Parent TSA base and receiving-stock doses are excluded. |
| jcm677 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677; JCM677 title/table and general page header | supports | Exact current primary table identifies M696/JCM677 and all five batch additions. Its general sterilization header is separately scoped; no explicit final-medium makeup or ordered preparation is printed. |
| togo696 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696; $.meta; $.components and $.comments | supports | Exact current TOGO M696 JSON matches the five source rows and explicitly references M470. Its provider role labels and source pointers are distinct from experimental growth evidence. |
| jcm469 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469; Hemin solution and Menadione solution subsections | supports | Only the explicitly linked Hemin solution and Menadione solution subsections support stock composition and preparation. The parent TSA156 instruction and its receiving-medium final doses are not transferred to JCM677. |
| togo470 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M470; $.meta; named stock sections and scoped comments | supports | The exact M470 source confirms the JCM469 accession and stock sections. Its separate water input rows are not equivalent to the primary final-makeup instruction; primary wording governs the stock denominator. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components/_solution_from_item/_extract_preparation_steps | context_only | Current primary-component extraction separates direct ingredients and stock additions; local stock content is normalized only where source basis is explicit. It retains source comments as preparation. These safeguards are current behavior, not historical execution proof. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current single-contributor merge copies owner content and adds generated metadata. The selected older merge does not contain the September owner repair; a future regeneration must follow reconciliation of remaining owner limitations. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-4 | reports/yaml_record_review/20260922T003757Z-Brucella_Blood_Agar_With_Hemin_Menadione.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-reader | REVIEW_WORK/batch056/record02/historical-reader.json | context_only | Complete selected target/owner historical reports and exact report hashes, preserving derivative-only limits. |
| identity-search | REVIEW_WORK/batch056/record02/identity-search.json | supports | Exact stable ID resolves the selected generated record and its declared maintained contributor. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi28869 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16236 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16236; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch056/record02/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch056/record02/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch056/record02/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch056/record02/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch056/record02/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch056/record02/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch056/record02/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch056/record02/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch056/record02/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- JCM677 has no explicit final-medium makeup declaration; its water input is not treated as final volume. The linked stocks do have explicit final makeup, so their owner strengths are credited.
- The general JCM sterilization header is not a complete source-specific ordered process. No unprinted order, pH, incubation condition or strain claim is proposed.
- Only M470 stock content is assessed. Its TSA/M147 base and receiving-dose fields, plus standalone provider identities mentioned in its notes, remain excluded from scientific transfer.
- Historical reports are derivative; their older confident per-liter interpretations are not adopted where the currently inspected primary does not state a final denominator. Current code cannot authenticate past writer execution.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T052236Z-batch056-record02-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Brucella Blood Agar: preserve stock repairs and qualify unresolved main-volume
  basis'
started_at: '2026-10-28T05:11:04.555553Z'
finished_at: '2026-10-28T05:22:36.456493Z'
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
summary: The generated M696 record is stale relative to its repaired normalized owner.
  The exact JCM677 table supports batch quantities, while JCM469 explicitly supports
  the two stock makeups. Owner stock strengths are credited, but main per-liter denominators
  and the imposed processing sequence are not fully supported. Only the linked stock
  portions of M470 are assessed.
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
  - path: data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    sha256: 637ebd2a0bf5e07ebd3cfc44be33f69f673fa8a57cd5551e76f6172e60191750
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml
    sha256: 3cd4a7ffd458969b5ad8ef4a0a8b6e066eeb1d2574ee61e2febcd6fe2625b21a
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    sha256: 713e970067fcf06ff7140d5f8642ca311ad3de4b14c525ee085d83af407258ee
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.md
    sha256: e33c47e35d2a980f637fb4440bd9df126f392821f156704d67afadd90cab9cd2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.md
    sha256: 81698cf8ef4f08b1ce8704fc3e63388b26fb95942a0c0bcca358cd9b4bd2ce26
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.md
    sha256: 65ef2ec703d0cd50682cefd6924ae2c2588c8241c43f94b9c6e1fa80dd758436
    role: context
  - path: reports/yaml_record_review/20260922T003757Z-Brucella_Blood_Agar_With_Hemin_Menadione.md
    sha256: c10d5db6ec61e9d0b3c7abb8337c097d48138ae05e188491c636d554bf073a07
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch056 native selection index 02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010102
targets:
- target_id: CultureMech:010102
  path: data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
  label: brucella_blood_agar_with_hemin_menadione
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:010102
  command: just validate-schema data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
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
  - CultureMech:010102
  command: just validate-strict data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    --out REVIEW_WORK/batch056/record02/strict.tsv --workers 1
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
  - CultureMech:010102
  command: just validate-terms data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
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
  - CultureMech:010102
  command: just validate-references data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 637ebd2a0bf5e07ebd3cfc44be33f69f673fa8a57cd5551e76f6172e60191750
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 713e970067fcf06ff7140d5f8642ca311ad3de4b14c525ee085d83af407258ee
- evidence_id: stock-dependency
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml
  locator: ingredients[0:5]; source pointers/history; solutions are structural context
    only
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Complete dependency read for identity/history; scientific scope is only
    its hemin/menadione stock ingredients and representation. Parent TSA base and
    receiving-stock doses are excluded.
  snapshot_sha256: 3cd4a7ffd458969b5ad8ef4a0a8b6e066eeb1d2574ee61e2febcd6fe2625b21a
- evidence_id: jcm677
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677
  locator: JCM677 title/table and general page header
  accessed_at: '2026-10-28T05:11:33.651507Z'
  support: supports
  summary: Exact current primary table identifies M696/JCM677 and all five batch additions.
    Its general sterilization header is separately scoped; no explicit final-medium
    makeup or ordered preparation is printed.
  snapshot_sha256: 1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b
- evidence_id: togo696
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696
  locator: $.meta; $.components and $.comments
  accessed_at: '2026-10-28T05:11:33.357211Z'
  support: supports
  summary: Exact current TOGO M696 JSON matches the five source rows and explicitly
    references M470. Its provider role labels and source pointers are distinct from
    experimental growth evidence.
  snapshot_sha256: 3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f
- evidence_id: jcm469
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469
  locator: Hemin solution and Menadione solution subsections
  accessed_at: '2026-10-28T05:11:34.009484Z'
  support: supports
  summary: Only the explicitly linked Hemin solution and Menadione solution subsections
    support stock composition and preparation. The parent TSA156 instruction and its
    receiving-medium final doses are not transferred to JCM677.
  snapshot_sha256: ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4
- evidence_id: togo470
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M470
  locator: $.meta; named stock sections and scoped comments
  accessed_at: '2026-10-28T05:11:33.987094Z'
  support: supports
  summary: The exact M470 source confirms the JCM469 accession and stock sections.
    Its separate water input rows are not equivalent to the primary final-makeup instruction;
    primary wording governs the stock denominator.
  snapshot_sha256: 0fa05cacbfb91cc54e92a840cf9f49d8bffb751ea48eaed183f7012fa8bc84bd
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components/_solution_from_item/_extract_preparation_steps
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Current primary-component extraction separates direct ingredients and stock
    additions; local stock content is normalized only where source basis is explicit.
    It retains source comments as preparation. These safeguards are current behavior,
    not historical execution proof.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Current single-contributor merge copies owner content and adds generated
    metadata. The selected older merge does not contain the September owner repair;
    a future regeneration must follow reconciliation of remaining owner limitations.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: e33c47e35d2a980f637fb4440bd9df126f392821f156704d67afadd90cab9cd2
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 81698cf8ef4f08b1ce8704fc3e63388b26fb95942a0c0bcca358cd9b4bd2ce26
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 65ef2ec703d0cd50682cefd6924ae2c2588c8241c43f94b9c6e1fa80dd758436
- evidence_id: historical-4
  kind: record_content
  reference: reports/yaml_record_review/20260922T003757Z-Brucella_Blood_Agar_With_Hemin_Menadione.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:22:36.126231Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: c10d5db6ec61e9d0b3c7abb8337c097d48138ae05e188491c636d554bf073a07
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch056/record02/historical-reader.json
  accessed_at: '2026-10-28T05:22:36.137719Z'
  support: context_only
  summary: Complete selected target/owner historical reports and exact report hashes,
    preserving derivative-only limits.
  snapshot_sha256: 474867bc13c80089f4459514f7eeab449f48ea4214de50d82112d5eef9e07487
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch056/record02/identity-search.json
  accessed_at: '2026-10-28T05:22:36.447458Z'
  support: supports
  summary: Exact stable ID resolves the selected generated record and its declared
    maintained contributor.
  snapshot_sha256: 73e9d2a9b589414c5f4ae5143407536a2ae8265931a10be699f8367ed71717ad
  search_scope: Exact stable record ID across complete normalized and merged YAML
    trees, including hidden and ignored files. Other accession/name records are not
    automatically contributing owners.
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:34.290739Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: chebi50385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.867181Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9531274295a20e5b89ae5c0a87c0772ec355c40948c99661eacec8d887712a8a
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.613998Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1f39a220b091088af20782dd27577fb7ca89e037d2b0ea83e76075fb8d77b797
- evidence_id: chebi28869
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.629824Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4715ccbed9d157f51f1faec46f5f0a552319f187925f9119582a93b84e8c829b
- evidence_id: chebi16236
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16236
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:34.389542Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 13f540b5f7d1da3048cb39c5d42fc708b9165abff06f1209414ef248c5975547
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch056/record02/quantity-inventory.json
  accessed_at: '2026-10-28T05:22:36.455517Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 59c15fc0571d227fab436ad9d7421d4b37a86e981b3ee28386a3b08ab132bdde
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch056/record02/grounding-inventory.json
  accessed_at: '2026-10-28T05:22:36.455562Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 99fe54774664e6c87524995ca7f20d3411e30a70c6ee11e3f8ac48350d45a327
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch056/record02/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T05:22:36.455614Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 9d583189c2f230c730210f69ffba1f5af88d6499715be5617c22795788b7d9f8
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch056/record02/scalar-census.json
  accessed_at: '2026-10-28T05:22:36.455638Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 4da33336dc8c67b8b49911d4397ba96ef7bce29e765a474c930e304951a7ef91
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch056/record02/validate-schema.json
  accessed_at: '2026-10-28T05:11:05.711742Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 943b41ac54f2455b976a55e3646386e13b6f1dc7edbadf7ad0a1e5004281f40c
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch056/record02/validate-strict.json
  accessed_at: '2026-10-28T05:11:06.768458Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch056/record02/strict.tsv\n"
  snapshot_sha256: bb38f5bea10a0ee518f2c98bc6c1153705f8ee7a26de4f2e64495cbcc69ccf01
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch056/record02/validate-terms.json
  accessed_at: '2026-10-28T05:11:07.877648Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 0c1ea7698255c492bec60282c6fdd1c92f879a679250d5f084b0d6f346c881a6
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch056/record02/validate-references.json
  accessed_at: '2026-10-28T05:11:08.605319Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: f88fdce28783e50cdf10993075a8f7a7ac53e24e9112c078d09ef53814c8b871
assessments:
- assessment_id: a1
  area: identity
  topic: Exact JCM677 identity and linked stock scope
  outcome: supported
  summary: TOGO M696 and current JCM677 identify the selected recipe. JCM469/M470
    is a scoped stock dependency, not a contributing owner or alternative source of
    the whole receiving formula. No strain-specific claim follows from the recipe
    title.
  target_ids:
  - CultureMech:010102
  evidence_ids:
  - jcm677
  - togo696
  - jcm469
  - identity-search
- assessment_id: a2
  area: grounding
  topic: Current terms and undefined materials
  outcome: supported
  summary: All asserted selected/owner chemical labels match exact current OLS objects.
    The alkaline stock identifies sodium hydroxide as a chemical in a normal solution;
    it is not evidence of pure hydroxide mass. Commercial Brucella agar and horse
    blood remain complex materials. The dependency medium/provider identifiers are
    structural references, outside the MIM chemical validity test.
  target_ids:
  - CultureMech:010102
  evidence_ids:
  - grounding
  - jcm469
  - owner-1
- assessment_id: a3
  area: scope
  topic: Unchanged classification and source boundaries
  outcome: supported
  summary: COMPLEX, UNDEFINED, SOLID_AGAR and generic cultivation application are
    consistent with the table. The owner already carries structured references, corrected
    liquid dimensions and supported stock strengths; these are credited. Neither primary
    specifies a target organism or a pH for JCM677; no such claim is added.
  target_ids:
  - CultureMech:010102
  evidence_ids:
  - jcm677
  - jcm469
  - owner-1
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:010102
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id":
    "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696",
    "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T05:11:33.357211Z",
    "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit":
    "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label":
    "Distilled water", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044",
    "label": "Solvating media"}]}}, "decision": "mixed", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup. The generated target additionally
    represents a liquid volume as a mass rate; correct that dimensional error on the
    source batch basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The exact source supplies a batch
    amount, alongside a listed water input, without declaring final-medium volume.
    The owner preserves the correct source magnitude and physical dimension, but its
    per-liter denominator remains unsupported. Do not sum liquid additions or silently
    reinterpret input water as final makeup. The generated target additionally represents
    a liquid volume as a mass rate; correct that dimensional error on the source batch
    basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1000",
    "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup. The generated target additionally
    represents a liquid volume as a mass rate; correct that dimensional error on the
    source batch basis."}]}, {"quantity_id": "q2", "topic": "Horse blood", "source":
    {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696",
    "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T05:11:33.357211Z",
    "exact_decoded_object": {"component_name": "Horse blood", "volume": 50, "unit":
    "ml", "gmo": "http://purl.jp/bio/10/gmo/GMO_001562", "gmo_id": "GMO_001562", "label":
    "Horse blood", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047",
    "label": "Undefined component"}], "roles": [{"id": "GMO_000042", "uri": "http://purl.jp/bio/10/gmo/GMO_000042",
    "label": "Nutrient source"}]}}, "decision": "mixed", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup. The generated target additionally
    represents a liquid volume as a mass rate; correct that dimensional error on the
    source batch basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The exact source supplies
    a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup. The generated target additionally
    represents a liquid volume as a mass rate; correct that dimensional error on the
    source batch basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "50.0",
    "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup. The generated target additionally
    represents a liquid volume as a mass rate; correct that dimensional error on the
    source batch basis."}]}, {"quantity_id": "q3", "topic": "Brucella agar", "source":
    {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696",
    "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T05:11:33.357211Z",
    "exact_decoded_object": {"component_name": "Brucella agar (BD-BBL)", "volume":
    43, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001522", "gmo_id": "GMO_001522",
    "label": "BBL &trade; Brucella agar", "properties": [{"id": "GMO_000047", "uri":
    "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}, {"id":
    "GMO_000050", "uri": "http://purl.jp/bio/10/gmo/GMO_000050", "label": "Complex
    component"}], "roles": []}}, "decision": "unsupported", "rationale": "The exact
    source supplies a batch amount, alongside a listed water input, without declaring
    final-medium volume. The owner preserves the correct source magnitude and physical
    dimension, but its per-liter denominator remains unsupported. Do not sum liquid
    additions or silently reinterpret input water as final makeup.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "43",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "43.0",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The exact source
    supplies a batch amount, alongside a listed water input, without declaring final-medium
    volume. The owner preserves the correct source magnitude and physical dimension,
    but its per-liter denominator remains unsupported. Do not sum liquid additions
    or silently reinterpret input water as final makeup."}]}, {"quantity_id": "q4",
    "topic": "Hemin solution receiving addition", "source": {"evidence_id": "togo696",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696",
    "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f",
    "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T05:11:33.357211Z",
    "exact_decoded_object": {"component_name": "Hemin solution (see Medium [M470])",
    "volume": 10, "unit": "ml", "reference_media_id": "M470", "properties": [], "roles":
    []}}, "decision": "mixed", "rationale": "JCM677 explicitly lists this stock addition
    as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension
    and magnitude are credited but its per-liter qualifier is unresolved because JCM677
    has no explicit final-volume statement. The final-dose statement in parent JCM469
    belongs to its TSA medium and is not transferred.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path":
    "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "JCM677 explicitly lists this stock addition
    as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension
    and magnitude are credited but its per-liter qualifier is unresolved because JCM677
    has no explicit final-volume statement. The final-dose statement in parent JCM469
    belongs to its TSA medium and is not transferred."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10.0",
    "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "JCM677 explicitly
    lists this stock addition as a batch liquid volume. The generated mass unit is
    wrong; the owner liquid dimension and magnitude are credited but its per-liter
    qualifier is unresolved because JCM677 has no explicit final-volume statement.
    The final-dose statement in parent JCM469 belongs to its TSA medium and is not
    transferred."}]}, {"quantity_id": "q5", "topic": "Menadione solution receiving
    addition", "source": {"evidence_id": "togo696", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M696",
    "raw_path": "REVIEW_WORK/batch056/source01-03/togo696.bin", "raw_sha256": "3a8ab7a0354513dfd2dc2a4dbeb69cdeaf21f6c19f36c0d735fec5466f11404f",
    "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T05:11:33.357211Z",
    "exact_decoded_object": {"component_name": "Menadione solution (see Medium [M470])",
    "volume": 10, "unit": "ml", "reference_media_id": "M470", "properties": [], "roles":
    []}}, "decision": "mixed", "rationale": "JCM677 explicitly lists this stock addition
    as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension
    and magnitude are credited but its per-liter qualifier is unresolved because JCM677
    has no explicit final-volume statement. The final-dose statement in parent JCM469
    belongs to its TSA medium and is not transferred.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml", "field_path":
    "solutions[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "JCM677 explicitly lists this stock addition
    as a batch liquid volume. The generated mass unit is wrong; the owner liquid dimension
    and magnitude are credited but its per-liter qualifier is unresolved because JCM677
    has no explicit final-volume statement. The final-dose statement in parent JCM469
    belongs to its TSA medium and is not transferred."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "10.0",
    "unit": "ML_PER_L"}, "decision": "unsupported", "rationale": "JCM677 explicitly
    lists this stock addition as a batch liquid volume. The generated mass unit is
    wrong; the owner liquid dimension and magnitude are credited but its per-liter
    qualifier is unresolved because JCM677 has no explicit final-volume statement.
    The final-dose statement in parent JCM469 belongs to its TSA medium and is not
    transferred."}]}, {"quantity_id": "q6", "topic": "Hemin stock solute", "source":
    {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "mixed", "rationale": "The source explicitly adjusts the
    stock to 100 mL final volume: 50 mg / 100 mL = 0.5 g/L. The existing owner stock
    solute concentration is supported; add claim-level linkage.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].composition[0].concentration", "stored_value": {"value":
    "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source
    explicitly adjusts the stock to 100 mL final volume: 50 mg / 100 mL = 0.5 g/L.
    The existing owner stock solute concentration is supported; add claim-level linkage."},
    {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Restore the supported composition from the maintained owner while
    preserving its stock stage; an empty list currently lacks these ingredients."}]},
    {"quantity_id": "q7", "topic": "Hemin stock initial solvent", "source": {"evidence_id":
    "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "mixed", "rationale": "The source uses 1 mL initial solvent
    in 100 mL final stock, supporting 10 mL/L at this stock stage. This is a volume
    of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No molarity,
    density or receiving dilution is invented.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].composition[1].concentration", "stored_value": {"value":
    "10.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source
    uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock
    stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical
    dose. No molarity, density or receiving dilution is invented."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Restore the supported composition from the maintained owner while
    preserving its stock stage; an empty list currently lacks these ingredients."}]},
    {"quantity_id": "q8", "topic": "Hemin stock preparation and final makeup", "source":
    {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "add", "rationale": "The exact stock subsection supplies
    dissolve-first order and an explicit final-makeup volume. These details are not
    represented by composition alone; retain them as stock preparation, without importing
    the parent TSA medium or assuming the makeup liquid identity beyond what is printed.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].preparation_notes", "stored_value": null, "decision":
    "add", "rationale": "The exact stock subsection supplies dissolve-first order
    and an explicit final-makeup volume. These details are not represented by composition
    alone; retain them as stock preparation, without importing the parent TSA medium
    or assuming the makeup liquid identity beyond what is printed.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].preparation_notes", "stored_value": null, "decision":
    "add", "rationale": "The exact stock subsection supplies dissolve-first order
    and an explicit final-makeup volume. These details are not represented by composition
    alone; retain them as stock preparation, without importing the parent TSA medium
    or assuming the makeup liquid identity beyond what is printed.", "missing": true}]},
    {"quantity_id": "q9", "topic": "Hemin placeholder shell and retained name", "source":
    {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b",
    "locator": "Exact named stock cross-reference", "accessed_at": "2026-10-28T05:11:33.651507Z",
    "quote": "Hemin solution"}, "decision": "mixed", "rationale": "The generated placeholder
    is stale; the exact owner preferred term is already supported.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Replace the placeholder with the already supported specific
    stock name."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[0].preferred_term", "stored_value": "Hemin solution",
    "decision": "evidence_only", "rationale": "Retain the correct named stock; this
    field needs evidence linkage, not a replacement."}]}, {"quantity_id": "q10", "topic":
    "Menadione stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume
    to 100 ml."}, "decision": "mixed", "rationale": "The source explicitly adjusts
    the stock to 100 mL final volume: 5 mg / 100 mL = 0.05 g/L. The existing owner
    stock solute concentration is supported; add claim-level linkage.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value":
    "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source
    explicitly adjusts the stock to 100 mL final volume: 5 mg / 100 mL = 0.05 g/L.
    The existing owner stock solute concentration is supported; add claim-level linkage."},
    {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].composition", "stored_value": [], "decision": "add",
    "rationale": "Restore the supported composition from the maintained owner while
    preserving its stock stage; an empty list currently lacks these ingredients."}]},
    {"quantity_id": "q11", "topic": "Menadione stock initial solvent", "source": {"evidence_id":
    "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume
    to 100 ml."}, "decision": "mixed", "rationale": "The source uses 1 mL initial
    solvent in 100 mL final stock, supporting 10 mL/L at this stock stage. This is
    a volume of 1 N NaOH solution or ethanol, not a final-medium chemical dose. No
    molarity, density or receiving dilution is invented.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].composition[1].concentration", "stored_value": {"value":
    "10.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source
    uses 1 mL initial solvent in 100 mL final stock, supporting 10 mL/L at this stock
    stage. This is a volume of 1 N NaOH solution or ethanol, not a final-medium chemical
    dose. No molarity, density or receiving dilution is invented."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].composition", "stored_value": [], "decision": "add",
    "rationale": "Restore the supported composition from the maintained owner while
    preserving its stock stage; an empty list currently lacks these ingredients."}]},
    {"quantity_id": "q12", "topic": "Menadione stock preparation and final makeup",
    "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume
    to 100 ml."}, "decision": "add", "rationale": "The exact stock subsection supplies
    dissolve-first order and an explicit final-makeup volume. These details are not
    represented by composition alone; retain them as stock preparation, without importing
    the parent TSA medium or assuming the makeup liquid identity beyond what is printed.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].preparation_notes", "stored_value": null, "decision":
    "add", "rationale": "The exact stock subsection supplies dissolve-first order
    and an explicit final-makeup volume. These details are not represented by composition
    alone; retain them as stock preparation, without importing the parent TSA medium
    or assuming the makeup liquid identity beyond what is printed.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].preparation_notes", "stored_value": null, "decision":
    "add", "rationale": "The exact stock subsection supplies dissolve-first order
    and an explicit final-makeup volume. These details are not represented by composition
    alone; retain them as stock preparation, without importing the parent TSA medium
    or assuming the makeup liquid identity beyond what is printed.", "missing": true}]},
    {"quantity_id": "q13", "topic": "Menadione placeholder shell and retained name",
    "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b",
    "locator": "Exact named stock cross-reference", "accessed_at": "2026-10-28T05:11:33.651507Z",
    "quote": "Menadione solution"}, "decision": "mixed", "rationale": "The generated
    placeholder is stale; the exact owner preferred term is already supported.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Replace the placeholder with the already supported specific
    stock name."}, {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "solutions[1].preferred_term", "stored_value": "Menadione solution",
    "decision": "evidence_only", "rationale": "Retain the correct named stock; this
    field needs evidence linkage, not a replacement."}]}, {"quantity_id": "q14", "topic":
    "Existing owner preparation step 1", "source": {"evidence_id": "jcm677", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677", "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin",
    "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b",
    "locator": "Complete table; no ordered preparation text", "accessed_at": "2026-10-28T05:11:33.651507Z"},
    "decision": "unsupported", "rationale": "The numerical batch inputs can be traced
    to the primary table, but that table does not prescribe this step ordering. The
    addition step also introduces unsupported per-liter qualifiers. Preserve source
    quantities separately and qualify or remove the invented ordered instruction;
    no replacement order is inferred.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Suspend 43.0
    g Brucella agar (BD-BBL) in 1.0 L distilled water.", "decision": "unsupported",
    "rationale": "The numerical batch inputs can be traced to the primary table, but
    that table does not prescribe this step ordering. The addition step also introduces
    unsupported per-liter qualifiers. Preserve source quantities separately and qualify
    or remove the invented ordered instruction; no replacement order is inferred."}]},
    {"quantity_id": "q15", "topic": "Existing owner preparation step 2", "source":
    {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b",
    "locator": "Complete table; no ordered preparation text", "accessed_at": "2026-10-28T05:11:33.651507Z"},
    "decision": "unsupported", "rationale": "The numerical batch inputs can be traced
    to the primary table, but that table does not prescribe this step ordering. The
    addition step also introduces unsupported per-liter qualifiers. Preserve source
    quantities separately and qualify or remove the invented ordered instruction;
    no replacement order is inferred.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "Add 50.0 ml/L
    horse blood, 10.0 ml/L hemin solution, and 10.0 ml/L menadione solution.", "decision":
    "unsupported", "rationale": "The numerical batch inputs can be traced to the primary
    table, but that table does not prescribe this step ordering. The addition step
    also introduces unsupported per-liter qualifiers. Preserve source quantities separately
    and qualify or remove the invented ordered instruction; no replacement order is
    inferred."}]}, {"quantity_id": "q16", "topic": "General sterilization header",
    "source": {"evidence_id": "jcm677", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm677.bin", "raw_sha256": "1fdeadcd67dafa51db698781735827d4d43c86cff1a89ecc436920e883cd2c6b",
    "locator": "General page header", "accessed_at": "2026-10-28T05:11:33.651507Z",
    "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for
    15 min."}, "decision": "mixed", "rationale": "The source explicitly states the
    general sterilization instruction. Its numbers are supported; a complete ordered
    process after blood/stock addition is not thereby authenticated.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "Autoclave at
    121 C for 15 min unless otherwise stated.", "decision": "evidence_only", "rationale":
    "The temperature and duration match the primary general header; credit this content
    without treating its position after all additions as independently supported."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "sterilization.method", "stored_value": "AUTOCLAVE", "decision":
    "evidence_only", "rationale": "The general primary header supports the method,
    with its unless-otherwise-stated qualification."}, {"path": "data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml",
    "field_path": "sterilization", "stored_value": null, "decision": "add", "rationale":
    "Restore only source-qualified method metadata, preserving the general-header
    scope.", "missing": true}]}, {"quantity_id": "q17", "topic": "Scoped M470 dependency:
    Initial alkaline solvent volume and normality", "source": {"evidence_id": "jcm469",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469", "raw_path":
    "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]},
    {"quantity_id": "q18", "topic": "Scoped M470 dependency: Collapsed water / final-makeup
    context", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported.
    The single collapsed water field cannot stand for both independently made stocks.
    The primary specifies final makeup to 100 mL for each; it does not print 100 g/L
    water.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "100.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency
    has stock content flattened into direct ingredient mass rates. The exact JCM469
    stock subsection supports a distinct stock amount/final-makeup representation,
    not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality
    and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation
    is imported. The single collapsed water field cannot stand for both independently
    made stocks. The primary specifies final makeup to 100 mL for each; it does not
    print 100 g/L water."}]}, {"quantity_id": "q19", "topic": "Scoped M470 dependency:
    Hemin stock solute", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Hemin solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to
    100 ml."}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency
    has stock content flattened into direct ingredient mass rates. The exact JCM469
    stock subsection supports a distinct stock amount/final-makeup representation,
    not the stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality
    and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation
    is imported."}]}, {"quantity_id": "q20", "topic": "Scoped M470 dependency: Initial
    ethanol volume", "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume
    to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has
    stock content flattened into direct ingredient mass rates. The exact JCM469 stock
    subsection supports a distinct stock amount/final-makeup representation, not the
    stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality
    and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation
    is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]},
    {"quantity_id": "q21", "topic": "Scoped M470 dependency: Menadione stock solute",
    "source": {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Menadione solution subsection", "accessed_at": "2026-10-28T05:11:34.009484Z",
    "quote": "Dissolve 5 mg menadione first in 1 ml of ethanol. Then adjust volume
    to 100 ml."}, "decision": "correct", "rationale": "This linked dependency has
    stock content flattened into direct ingredient mass rates. The exact JCM469 stock
    subsection supports a distinct stock amount/final-makeup representation, not the
    stored direct G_PER_L value. Keep stock solute, initial solvent volume/normality
    and final makeup separate. No parent-medium receiving dose or unrelated TSA formulation
    is imported.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "This linked dependency has stock
    content flattened into direct ingredient mass rates. The exact JCM469 stock subsection
    supports a distinct stock amount/final-makeup representation, not the stored direct
    G_PER_L value. Keep stock solute, initial solvent volume/normality and final makeup
    separate. No parent-medium receiving dose or unrelated TSA formulation is imported."}]},
    {"quantity_id": "q22", "topic": "Excluded parent-medium quantities", "source":
    {"evidence_id": "jcm469", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469",
    "raw_path": "REVIEW_WORK/batch056/source01-03/jcm469.bin", "raw_sha256": "ba068131e3a9bc84e768b439d002a611071950faa0fe2b2608866791b94c74c4",
    "locator": "Parent TSA paragraph, excluded from M696 receiving-dose support",
    "accessed_at": "2026-10-28T05:11:34.009484Z"}, "decision": "not_assessed", "rationale":
    "M470 solutions[0:3] receiving concentrations and JCM469 TSA156 parent composition
    are excluded from quantitative assessment here. They are not used to fill JCM677
    final-volume or addition-dose evidence.", "layer_assessments": []}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:010102
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
  - CultureMech:010102
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
  - CultureMech:010102
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:010102
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-010102-generated-content-omits-supported-owner-stock-repairs
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated content omits supported owner stock repairs
  description: The generated file retains liquid additions as mass rates, empty stock
    compositions and Unknown solution names. Its maintained owner already has liquid
    dimensions, both supported stock compositions and structured source references.
    Preserve those repairs, but do not regenerate unresolved main denominator or ordering
    claims as if verified.
  target_ids:
  - CultureMech:010102
  field_paths:
  - ingredients
  - solutions
  - references
  evidence_ids:
  - local-target
  - owner-1
  - jcm677
  - jcm469
  - writer-merge
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-010102-main-per-liter-denominators-exceed-the-printed-batch-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main per-liter denominators exceed the printed batch basis
  description: The primary table supplies amounts and a water input without explicitly
    declaring final-medium volume. The owner has corrected liquid dimensions but expresses
    all main rows and additions per liter, and its second preparation step repeats
    those qualifiers. JCM469 final receiving doses apply to a different parent medium.
  target_ids:
  - CultureMech:010102
  field_paths:
  - ingredients[2].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::ingredients[0].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::ingredients[1].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::ingredients[2].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::solutions[0].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::solutions[1].concentration
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::preparation_steps[1].description
  evidence_ids:
  - jcm677
  - jcm469
  - togo696
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-010102-owner-preparation-imposes-an-unsupported-process-order
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Owner preparation imposes an unsupported process order
  description: The owner orders suspension, all liquid additions, then autoclaving.
    JCM677 supplies a table and a general sterilization header, not that exact ordered
    process. The supported header values must remain scoped without asserting the
    point at which blood or stock additions are treated.
  target_ids:
  - CultureMech:010102
  field_paths:
  - preparation_steps
  - data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml::preparation_steps
  evidence_ids:
  - jcm677
  - owner-1
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-010102-linked-stock-dependency-still-flattens-stock-contents
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Linked stock dependency still flattens stock contents
  description: Within the explicitly linked M470 dependency, five direct ingredients
    encode stock solute/solvent/makeup information as mass rates. This is separate
    from the selected owner, whose stock strengths were repaired. Restore only the
    two linked stock scopes; do not transfer or assess its unrelated TSA parent formula.
  target_ids:
  - CultureMech:010102
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml::ingredients[0].concentration
  - data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml::ingredients[1].concentration
  - data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml::ingredients[2].concentration
  - data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml::ingredients[3].concentration
  - data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml::ingredients[4].concentration
  evidence_ids:
  - stock-dependency
  - jcm469
  - togo470
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Reconcile remaining owner basis/process limits, then regenerate the
    target with the supported stock composition and specific names. Keep the exact
    source batch amounts and named stocks; no cross-source whole-medium substitution.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010102
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Preserve batch amounts with explicit basis and qualify unsupported
    main per-liter interpretations until an exact final-volume statement is verified.
    Keep valid stock-level concentrations intact; do not infer final volume by summing
    additions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010102
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Separate the source-supported general header and batch quantities from
    inferred processing order. Document the unresolved order rather than supply a
    replacement protocol without exact evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010102
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Repair the two exact linked stock representations with their primary
    stock-stage amounts, solvent normality/volume and explicit final makeup. Preserve
    the parent-medium boundary and do not add a JCM677 receiving dose from JCM469.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010102
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M470_TSA_Hemin_Menadione_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- JCM677 has no explicit final-medium makeup declaration; its water input is not treated
  as final volume. The linked stocks do have explicit final makeup, so their owner
  strengths are credited.
- The general JCM sterilization header is not a complete source-specific ordered process.
  No unprinted order, pH, incubation condition or strain claim is proposed.
- Only M470 stock content is assessed. Its TSA/M147 base and receiving-dose fields,
  plus standalone provider identities mentioned in its notes, remain excluded from
  scientific transfer.
- Historical reports are derivative; their older confident per-liter interpretations
  are not adopted where the currently inspected primary does not state a final denominator.
  Current code cannot authenticate past writer execution.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
