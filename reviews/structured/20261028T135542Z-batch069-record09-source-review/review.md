# Chakraborty Basal source and provenance review

- Review: 20261028T135542Z-batch069-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:47:26.680970Z
- Finished UTC: 2026-10-28T13:55:42.803444Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact versioned FEBA definition supports all 29 stored ingredient rates, including the 24 contributions from its two 100X mixes used at 1X. Both local layers lack ingredient evidence and structured mix provenance. Current CHEBI identities are supported; the three phosphate entries are explicitly separate source rows. The historical CultureBotHT import version remains unavailable, and the unmapped-ingredient flag needs reconciliation.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch069 native selection index 09.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015502 | data/merge_yaml/merged/Chakraborty_Basal.yaml | generated | Chakraborty Basal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015502 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:015502 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:015502 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:015502 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact target, owner and source name

identity: supported. Targets: CultureMech:015502.

The sole declared contributor resolves uniquely and retains the same CultureMech identity. The exact FEBA Chakraborty_Basal header and description agree with both local layers. No organism or laboratory identity is inferred from the surname.

### Basal definition, source components and absence limits

representation: supported. Targets: CultureMech:015502.

Defined/minimal description is supported by Minimal TRUE and the named chemical components. Source phosphate monohydrate, anhydrous NaH2PO4 and disodium phosphate are three explicit rows; do not deduplicate or treat them as alternatives. Liquid is consistent with the nongelled definition but not an independently documented physical-state measurement. The scoped source gives no pH, final-volume instruction, carbon amendment, growth conditions or preparation method. Their absence does not justify invented values.

### Historical checks and current claims

evidence: concern. Targets: CultureMech:015502.

The two full October5 reports have matching current record hashes and recorded zero source-checked claims. The selected October9 pending object still reports 29 missing attached ingredient claims. Current direct source and mix verification supports all 29 rates, but neither YAML layer yet carries these claim-level excerpts. The older July manganese report names a wrong identifier; current 86364 is correct, without inferring when or how the change occurred.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:015502.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Ammonium chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1062", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Ammonium chloride\t0.25\tg/L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.25 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.25 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.25 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "calculation": {"source_value": "0.25", "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.25", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q2", "topic": "Potassium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1063", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Potassium Chloride\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.1 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.1 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.1 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "calculation": {"source_value": "0.1", "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.1", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q3", "topic": "Sodium phosphate monobasic monohydrate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1064", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Sodium phosphate monobasic monohydrate\t0.6\tg/L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.6 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.6 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.6 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "calculation": {"source_value": "0.6", "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.6", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q4", "topic": "NaH2PO4", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1065", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "NaH2PO4\t0.3792\tg/L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.3792 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3792", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.3792 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3792", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.3792 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "calculation": {"source_value": "0.3792", "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.3792", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q5", "topic": "Disodium phosphate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1066", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Disodium phosphate\t0.9713\tg/L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.9713 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.9713", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.9713 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.9713", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal source row states 0.9713 g/L; the stored value and chemical form agree. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "calculation": {"source_value": "0.9713", "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.9713", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q6", "topic": "Magnesium Sulfate Heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 5", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Magnesium Sulfate Heptahydrate\t3\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "3", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.03", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q7", "topic": "Nitrilotriacetic acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 6", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nitrilotriacetic acid\t1.5\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.015", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.015", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "1.5", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.015", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q8", "topic": "Sodium Chloride", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 7", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium Chloride\t1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "1", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.01", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q9", "topic": "Manganese (II) sulfate monohydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 8", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Manganese (II) sulfate monohydrate\t0.5\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.5 g/L at 100X; selected medium requires 1X, so 0.5×(1/100)=0.005 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.5 g/L at 100X; selected medium requires 1X, so 0.5×(1/100)=0.005 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.5 g/L at 100X; selected medium requires 1X, so 0.5×(1/100)=0.005 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.5", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.005", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q10", "topic": "Cobalt chloride hexahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 9", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Cobalt chloride hexahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q11", "topic": "Zinc sulfate heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 10", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Zinc sulfate heptahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q12", "topic": "Calcium Chloride Dihydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 11", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Calcium Chloride Dihydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q13", "topic": "Iron (II) sulfate heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 12", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Iron (II) sulfate heptahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q14", "topic": "Nickel (II) chloride hexahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 13", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nickel (II) chloride hexahydrate\t0.025\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.025 g/L at 100X; selected medium requires 1X, so 0.025×(1/100)=0.00025 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.00025", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.025 g/L at 100X; selected medium requires 1X, so 0.025×(1/100)=0.00025 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.00025", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.025 g/L at 100X; selected medium requires 1X, so 0.025×(1/100)=0.00025 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.025", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.00025", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q15", "topic": "Aluminum potassium sulfate dodecahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 14", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Aluminum potassium sulfate dodecahydrate\t0.02\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.02 g/L at 100X; selected medium requires 1X, so 0.02×(1/100)=0.0002 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.0002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.02 g/L at 100X; selected medium requires 1X, so 0.02×(1/100)=0.0002 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.0002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.02 g/L at 100X; selected medium requires 1X, so 0.02×(1/100)=0.0002 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.02", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0002", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q16", "topic": "Copper (II) sulfate pentahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 15", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Copper (II) sulfate pentahydrate\t0.01\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q17", "topic": "Boric Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 16", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Boric Acid\t0.01\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q18", "topic": "Sodium Molybdate Dihydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 17", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium Molybdate Dihydrate\t0.01\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit": "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q19", "topic": "Sodium selenite pentahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 18", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium selenite pentahydrate\t0.3\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.3 mg/L at 100X; selected medium requires 1X, so 0.3×(1/100)=0.003 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.003", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.3 mg/L at 100X; selected medium requires 1X, so 0.3×(1/100)=0.003 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.003", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.3 mg/L at 100X; selected medium requires 1X, so 0.3×(1/100)=0.003 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}], "calculation": {"source_value": "0.3", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.003", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q20", "topic": "pyridoxine HCl", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 42", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "pyridoxine HCl\t10\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "10", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.1", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q21", "topic": "4-Aminobenzoic acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 43", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "4-Aminobenzoic acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q22", "topic": "Lipoic acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 44", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Lipoic acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q23", "topic": "Nicotinic Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 45", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nicotinic Acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q24", "topic": "Riboflavin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 46", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Riboflavin\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q25", "topic": "thiamine HCl", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 47", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "thiamine HCl\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q26", "topic": "calcium pantothenate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 48", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "calcium pantothenate\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q27", "topic": "biotin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 49", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "biotin\t2\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "2", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.02", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q28", "topic": "Folic Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 50", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Folic Acid\t2\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "2", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.02", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q29", "topic": "Cyanocobalamin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 51", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Cyanocobalamin\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 mg/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.001", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 mg/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.001", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 mg/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 mg/L. The stored mass rate agrees; this is a concentration-factor derivation, not an assumed batch volume or measured final volume. Neither local layer has attached ingredient evidence, so retain the amount and add exact source evidence through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit": "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id": "q30", "topic": "mineral mix strength and receiving factor", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, "decision": "add", "rationale": "The exact mineral mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The exact mineral mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "missing": true}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The exact mineral mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "missing": true}], "basis_controls": [{"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q31", "topic": "vitamin mix strength and receiving factor", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"}, "decision": "add", "rationale": "The exact vitamin mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The exact vitamin mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "missing": true}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The exact vitamin mix is explicitly 100X and the receiving medium explicitly 1X. Local origin notes credit the mix name but omit its structured identity, strength and evidence. Preserve correct flattened rates; represent the exact source mix and its factor without inventing preparation instructions or aliquot volumes.", "missing": true}], "basis_controls": [{"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote": "Wolfe's vitamin mix\t1\tX"}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:015502.

All 58 asserted CHEBI slots use29 active current OLS identities with matching canonical labels and source-specific salt/hydrate forms. Exact MIM preferred rows include MAPPED and REJECTED aliases plus ontology-linked records of different granularity; these are not interchangeable endorsements. The source monohydrate CAS/mass and exact compound name agree despite its erroneous dihydrate synonym. Lipoic acid remains non-stereospecific at the asserted ontology level; no enantiomer is inferred. Calcium pantothenate source FW 238.27 is a hemicalcium-unit convention, whereas OLS 31345 represents 2C9H16NO5.Ca at 476.536; this does not alter the supported mass-per-volume amount.

### History and evidence scope

provenance: concern. Targets: CultureMech:015502.

Complete target and owner histories and their references were read. The single-owner generated record has unchanged ingredient content and no attached claims; the import provenance names a file and generic repository but no immutable upstream revision. Current FEBA bytes support the present source correspondence, not the original import event. Current importer/grounding/merger behavior is distinguished from historical execution; no history is overwritten.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:015502.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:015502.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Supported rates need exact claim evidence and mix provenance

major / open / confirmed; issue key: culturemech-015502-supported-rates-need-exact-claim-evidence-and-mix-provenance.

All 29 stored rates are supported by the exact versioned FEBA definition and its named 100X mixes used at 1X. Both layers retain flattened components with free-text origin notes but no attached quantity evidence or structured mix strength/source linkage. Preserve those correct rates and origin notes while representing the exact named source dependencies and calculations through the maintained owner; unrelated ATCC or minus-component mixes are not substitutes.

### f2: Historical upstream version remains unresolved

minor / open / confirmed; issue key: culturemech-015502-historical-upstream-version-remains-unresolved.

The recorded CultureBotHT source is a generic repository URL and imported filename. Its current public API request returned 404, while the recoverable FEBA revision is a later source observation. Add accurately timed versioned source citations and preserve the distinction from the original import; an access failure does not establish deletion or nonexistence.

### f3: Unmapped-ingredient flag is stale for current term occupancy

minor / open / confirmed; issue key: culturemech-015502-unmapped-ingredient-flag-is-stale-for-current-term-occupancy.

Both local layers retain has_unmapped_ingredients although each of their 29 ingredients now has an explicit supported CHEBI term. The current importer appends this flag when IDs are absent and does not remove an inherited flag. Re-evaluate the flag after curation while preserving historical entries; do not equate mere ID presence with scientific validity or add arbitrary secondary identifiers.

## Recommended Actions And Acceptance Checks

### action1

Attach exact versioned base and mix excerpts to maintained ingredient evidence, including the 100X-to-1X factor. Preserve all 29 supported mass rates and explicit chemical forms; represent the two source mix identities without inventing physical preparation volumes. Regenerate the compatible target only after owner curation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

The recorded CultureBotHT source is a generic repository URL and imported filename. Its current public API request returned 404, while the recoverable FEBA revision is a later source observation. Add accurately timed versioned source citations and preserve the distinction from the original import; an access failure does not establish deletion or nonexistence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Both local layers retain has_unmapped_ingredients although each of their 29 ingredients now has an explicit supported CHEBI term. The current importer appends this flag when IDs are absent and does not remove an inherited flag. Re-evaluate the flag after curation while preserving historical entries; do not equate mere ID presence with scientific validity or add arbitrary secondary identifiers.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Chakraborty_Basal.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/specialized/chakraborty_basal.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch069/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| febaCommit | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1; values[0].hash | context_only | Current public FEBA revision is 803273865ea9e83fab770ec4f13670db80e1180b. This does not recover the historical CultureBotHT import revision. |
| febaMedia | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; lines 1058–1069 | supports | Exact Chakraborty_Basal block: five basal components plus separately named Wolfe mineral and vitamin mixes, each at 1X. No organism, pH, batch volume or preparation conditions are supplied in this block. |
| febaMixes | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes; lines 1–19 and38–52 | supports | Exact non-ATCC Wolfe mineral and vitamin definitions each state X=100. The 1X receiving factor supports division of component mass rates by 100. Distinct ATCC and minus-component mixtures are not substituted. |
| febaCompounds | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact Compound names and NaH2PO4 synonym rows | context_only | Exact matching compound rows supply chemical names, CAS and formula-weight metadata. Source aliases are not uniformly reliable: monohydrate row has an inconsistent dihydrate synonym; calcium pantothenate FW uses hemicalcium convention; lipoic acid is labelled D,L. |
| culturebotRepo | https://api.github.com/repos/CultureBotAI/CultureBotHT; HTTP status and retained response body | context_only | The exact public repository metadata request returned 404. This records an access outcome, not proof of deletion, nonexistence or the imported historical bytes. |
| historical-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chakraborty_Basal.md; Complete document | context_only | Entire historical record report read; all 29 source checks were not performed at that time. Its exact current record digest is separately checked. |
| historical-report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/chakraborty_basal.md; Complete document | context_only | Entire historical record report read; all 29 source checks were not performed at that time. Its exact current record digest is separately checked. |
| writer-import | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium and import_file | context_only | Current transform_medium shallow-copies provided source data, adds generic repository and file attribution, and appends an unmapped flag only when a term ID is absent. This code is not proof of the historical input or execution. |
| writer-grounding | scripts/fix_primary_term_grounding.py; classify and main | context_only | Current controlled re-grounding/canonicalization preserves flags for unresolved cases and appends curation events; it does not authenticate an old run. |
| writer-merge | src/culturemech/merge/merger.py; Complete document | context_only | Current compatible-formulation merger read separately from this historical generated artifact; no source mutation or regeneration performed. |
| mim-pool | REVIEW_WORK/batch069/record09/mim-row-pool.json | context_only | Complete exact current MIM identifier-or-ontology-ID row pool; preferred statuses and linked-only rows are kept distinct. |
| historical-joins | REVIEW_WORK/batch069/record09/historical-joins.json | context_only | Exact selected historical table rows and pending coverage object, with original file hashes and current record hash joins. |
| ols31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols114249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114249; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols37585 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_37585; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch069/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch069/record09/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch069/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch069/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch069/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch069/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch069/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch069/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch069/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Partial completion: the original CultureBotHT import snapshot/revision is unavailable through the current public repository API; present FEBA correspondence does not authenticate past execution.
- All 29 stored ingredient rates on both layers were assessed, including 24 mix-derived contributions. The source supports concentration-factor scaling only; no measured final volume, aliquot, culture condition or preparation instruction is inferred.
- The current OLS and MIM snapshots support current identifier review only. Rejected aliases and linked records are not used to replace valid primary chemical identities. No literature linked from ontology objects was treated as independently verified.
- No organism-specific growth evidence is present in the scoped source. No taxon, strain, carbon amendment, pH or cultivation method is proposed from a medium or laboratory name.
- The historical concentration reports and exact coverage row are diagnostics; matching digests authenticate the local record snapshot, not an unavailable external source event. All existing history remains preserved.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T135542Z-batch069-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Chakraborty Basal source and provenance review
started_at: '2026-10-28T13:47:26.680970Z'
finished_at: '2026-10-28T13:55:42.803444Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact versioned FEBA definition supports all 29 stored ingredient rates,
  including the 24 contributions from its two 100X mixes used at 1X. Both local layers
  lack ingredient evidence and structured mix provenance. Current CHEBI identities
  are supported; the three phosphate entries are explicitly separate source rows.
  The historical CultureBotHT import version remains unavailable, and the unmapped-ingredient
  flag needs reconciliation.
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
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/Chakraborty_Basal.yaml
    sha256: 42e063ccbb4bd978bfd7d367f17f206e38e73cfe20d39b8f5d5b33ae7ab56bf5
    role: target
  - path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    sha256: 833c10f9885eae526360b0dc3a223b93e5efbad994e94483965bd8daa9730772
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
  - path: reports/ingredient_concentration_curation/20261009-desulfurobacterium-family/followup-coverage.json
    sha256: 871e276901c623bab98b153c0f2dc0854a19964af11d6d3c38e051e1261a3ca1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chakraborty_Basal.md
    sha256: 81cd031b6d58a6071498ab66068aa8ea4fa9a5ba271768199b5d7592014a5c98
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/chakraborty_basal.md
    sha256: 7315bbc0e17af9e1692b4746c8f806e7658e77c48ceedc91afe1bfff76e9093b
    role: context
  - path: reports/label_plausibility_2026-07-19.tsv
    sha256: eda647ffbb87d5ea90db812858b2d1d9388393c4d1abc8dec78672324c1509d9
    role: context
  - path: reports/media_content_review_manifest.tsv
    sha256: e5ff2f1241ba046ae7a5dc0d543d340bdba10d31fa1fdc3e36203600cf1ec0ce
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
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
  selection: Actual batch069 native selection index 09.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015502
targets:
- target_id: CultureMech:015502
  path: data/merge_yaml/merged/Chakraborty_Basal.yaml
  label: Chakraborty Basal
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:015502
  command: just validate-schema data/merge_yaml/merged/Chakraborty_Basal.yaml
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
  - CultureMech:015502
  command: just validate-strict data/merge_yaml/merged/Chakraborty_Basal.yaml --out
    REVIEW_WORK/batch069/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:015502
  command: just validate-terms data/merge_yaml/merged/Chakraborty_Basal.yaml
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
  - CultureMech:015502
  command: just validate-references data/merge_yaml/merged/Chakraborty_Basal.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Chakraborty_Basal.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 42e063ccbb4bd978bfd7d367f17f206e38e73cfe20d39b8f5d5b33ae7ab56bf5
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/specialized/chakraborty_basal.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 833c10f9885eae526360b0dc3a223b93e5efbad994e94483965bd8daa9730772
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch069/record09/identity-search.json
  accessed_at: '2026-10-28T13:55:42.733640Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 24339015f50d43c1c2b7ef75f9951ad67162bd7b79457c555e477d53e8e26d33
- evidence_id: febaCommit
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1
  locator: values[0].hash
  accessed_at: '2026-10-28T13:47:55.369203Z'
  support: context_only
  summary: Current public FEBA revision is 803273865ea9e83fab770ec4f13670db80e1180b.
    This does not recover the historical CultureBotHT import revision.
  snapshot_sha256: e802ea5aee4c66aa42d5425b9aac40af420f9072365b3963288985afa771a498
- evidence_id: febaMedia
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: lines 1058–1069
  accessed_at: '2026-10-28T13:47:55.683994Z'
  support: supports
  summary: 'Exact Chakraborty_Basal block: five basal components plus separately named
    Wolfe mineral and vitamin mixes, each at 1X. No organism, pH, batch volume or
    preparation conditions are supplied in this block.'
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: febaMixes
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes
  locator: lines 1–19 and38–52
  accessed_at: '2026-10-28T13:50:00.698954Z'
  support: supports
  summary: Exact non-ATCC Wolfe mineral and vitamin definitions each state X=100.
    The 1X receiving factor supports division of component mass rates by 100. Distinct
    ATCC and minus-component mixtures are not substituted.
  snapshot_sha256: b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4
- evidence_id: febaCompounds
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact Compound names and NaH2PO4 synonym rows
  accessed_at: '2026-10-28T13:50:00.678009Z'
  support: context_only
  summary: 'Exact matching compound rows supply chemical names, CAS and formula-weight
    metadata. Source aliases are not uniformly reliable: monohydrate row has an inconsistent
    dihydrate synonym; calcium pantothenate FW uses hemicalcium convention; lipoic
    acid is labelled D,L.'
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: culturebotRepo
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: HTTP status and retained response body
  accessed_at: '2026-10-28T13:47:55.642792Z'
  support: context_only
  summary: The exact public repository metadata request returned 404. This records
    an access outcome, not proof of deletion, nonexistence or the imported historical
    bytes.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: historical-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chakraborty_Basal.md
  locator: Complete document
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Entire historical record report read; all 29 source checks were not performed
    at that time. Its exact current record digest is separately checked.
  snapshot_sha256: 81cd031b6d58a6071498ab66068aa8ea4fa9a5ba271768199b5d7592014a5c98
- evidence_id: historical-report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/chakraborty_basal.md
  locator: Complete document
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Entire historical record report read; all 29 source checks were not performed
    at that time. Its exact current record digest is separately checked.
  snapshot_sha256: 7315bbc0e17af9e1692b4746c8f806e7658e77c48ceedc91afe1bfff76e9093b
- evidence_id: writer-import
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium and import_file
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Current transform_medium shallow-copies provided source data, adds generic
    repository and file attribution, and appends an unmapped flag only when a term
    ID is absent. This code is not proof of the historical input or execution.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-grounding
  kind: record_content
  reference: scripts/fix_primary_term_grounding.py
  locator: classify and main
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Current controlled re-grounding/canonicalization preserves flags for unresolved
    cases and appends curation events; it does not authenticate an old run.
  snapshot_sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Complete document
  accessed_at: '2026-10-28T13:55:42.684324Z'
  support: context_only
  summary: Current compatible-formulation merger read separately from this historical
    generated artifact; no source mutation or regeneration performed.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: mim-pool
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/mim-row-pool.json
  accessed_at: '2026-10-28T13:55:42.787594Z'
  support: context_only
  summary: Complete exact current MIM identifier-or-ontology-ID row pool; preferred
    statuses and linked-only rows are kept distinct.
  snapshot_sha256: 25c598fe2d00e086c8645fbcc6f9cf5db7742cd83177188d89dd469c171fda7c
- evidence_id: historical-joins
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/historical-joins.json
  accessed_at: '2026-10-28T13:55:42.787681Z'
  support: context_only
  summary: Exact selected historical table rows and pending coverage object, with
    original file hashes and current record hash joins.
  snapshot_sha256: 893aff873835c2e1cd3fa588a8f5be1d7ae3f7f442aab5d5ced17e062bd29939
- evidence_id: ols31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:16.805867Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: ols32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:02.966877Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: ols114249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:59.272854Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 95f1a21c34a9515cd8ea47ffd1cfc2f5788bd31203f6888efb22b05eb6eb4efa
- evidence_id: ols37585
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_37585
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:08.269360Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 41dce71ee822e488298c467569974159cbd109700160a5863720dd3ae3213b13
- evidence_id: ols34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:19.423166Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: ols31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:01.756328Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: ols44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:20.370096Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: ols26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:56.749131Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: ols86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:16.110086Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: ols53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:12.548570Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: ols32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:02.356367Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: ols86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:24.665794Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ols75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:15.481464Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: ols53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:13.151912Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: ols86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:16.719997Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: ols31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:01.117424Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: ols33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:03.574106Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: ols75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:15.134057Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: ols131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:56.003184Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: ols30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:59.884741Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: ols30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:14.517358Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: ols16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:07.442659Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: ols15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:56.139368Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: ols17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:07.682735Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: ols49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:20.602232Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: ols31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:00.507771Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: ols15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:59.319509Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: ols27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:47:57.716973Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: ols17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:48:11.913114Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/quantity-inventory.json
  accessed_at: '2026-10-28T13:55:42.802326Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 27bf0b6cb8be57603c2e091a304c93d1ff8fa6e8209c7d57d0d72aadd0a660dd
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/grounding-inventory.json
  accessed_at: '2026-10-28T13:55:42.802397Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 734adab08b893d2749c3d3bc4cd637a9763bd6b12ff2fd7b0ac56c380338951d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T13:55:42.802492Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 1d7a0d56400f182078d287397b87a238158beaa2140d63b169147be7a1240345
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch069/record09/scalar-census.json
  accessed_at: '2026-10-28T13:55:42.802511Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 1ec43130a08d0ac9370f63422233db5d3a60802970509c5931747420ee443363
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch069/record09/validate-schema.json
  accessed_at: '2026-10-28T13:47:27.702342Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: b76bee7c6036b0a2df253333f5b108f2b7d0e01c8da2aaaf378abef35dd35f69
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch069/record09/validate-strict.json
  accessed_at: '2026-10-28T13:47:28.614956Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch069/record09/strict.tsv\n"
  snapshot_sha256: b534a39e583fb2e00b1d9232a9733b1ce6f96ca734ced1ccc7d2ee45edacc763
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch069/record09/validate-terms.json
  accessed_at: '2026-10-28T13:47:29.615574Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: e384d0c75de947564aa27dd2f13269bb536cd3ea0a9766c49d4ecc55abed10a2
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch069/record09/validate-references.json
  accessed_at: '2026-10-28T13:47:30.303994Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 14e8d23218cd51ef352424edcb800330b42e69c1a8577d21c16a5fec48e4b0f8
assessments:
- assessment_id: a1
  area: identity
  topic: Exact target, owner and source name
  outcome: supported
  summary: The sole declared contributor resolves uniquely and retains the same CultureMech
    identity. The exact FEBA Chakraborty_Basal header and description agree with both
    local layers. No organism or laboratory identity is inferred from the surname.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - identity-search
  - local-target
  - owner-1
  - febaMedia
- assessment_id: a2
  area: representation
  topic: Basal definition, source components and absence limits
  outcome: supported
  summary: Defined/minimal description is supported by Minimal TRUE and the named
    chemical components. Source phosphate monohydrate, anhydrous NaH2PO4 and disodium
    phosphate are three explicit rows; do not deduplicate or treat them as alternatives.
    Liquid is consistent with the nongelled definition but not an independently documented
    physical-state measurement. The scoped source gives no pH, final-volume instruction,
    carbon amendment, growth conditions or preparation method. Their absence does
    not justify invented values.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - febaMedia
  - febaMixes
  - local-target
- assessment_id: a3
  area: evidence
  topic: Historical checks and current claims
  outcome: concern
  summary: The two full October5 reports have matching current record hashes and recorded
    zero source-checked claims. The selected October9 pending object still reports
    29 missing attached ingredient claims. Current direct source and mix verification
    supports all 29 rates, but neither YAML layer yet carries these claim-level excerpts.
    The older July manganese report names a wrong identifier; current 86364 is correct,
    without inferring when or how the change occurred.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - historical-report-1
  - historical-report-2
  - historical-joins
  - local-target
  - owner-1
  - febaMedia
  - febaMixes
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Ammonium chloride", "source": {"evidence_id":
    "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1062", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Ammonium chloride\t0.25\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named basal source row states 0.25 g/L; the stored value and chemical form agree.
    Neither local layer has attached ingredient evidence, so retain the amount and
    add exact source evidence through the maintained owner.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Exact named basal source row states 0.25 g/L; the stored value and
    chemical form agree. Neither local layer has attached ingredient evidence, so
    retain the amount and add exact source evidence through the maintained owner."},
    {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Exact named basal source row states
    0.25 g/L; the stored value and chemical form agree. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "calculation": {"source_value": "0.25", "source_unit":
    "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.25",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q2", "topic": "Potassium Chloride", "source": {"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1063", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Potassium Chloride\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named basal source row states 0.1 g/L; the stored value and chemical form agree.
    Neither local layer has attached ingredient evidence, so retain the amount and
    add exact source evidence through the maintained owner.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Exact named basal source row states 0.1 g/L; the stored value and
    chemical form agree. Neither local layer has attached ingredient evidence, so
    retain the amount and add exact source evidence through the maintained owner."},
    {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Exact named basal source row states
    0.1 g/L; the stored value and chemical form agree. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "calculation": {"source_value": "0.1", "source_unit":
    "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.1",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q3", "topic": "Sodium phosphate monobasic monohydrate", "source": {"evidence_id":
    "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1064", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Sodium phosphate monobasic monohydrate\t0.6\tg/L"}, "decision": "evidence_only",
    "rationale": "Exact named basal source row states 0.6 g/L; the stored value and
    chemical form agree. Neither local layer has attached ingredient evidence, so
    retain the amount and add exact source evidence through the maintained owner.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.6",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal
    source row states 0.6 g/L; the stored value and chemical form agree. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.6",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named basal
    source row states 0.6 g/L; the stored value and chemical form agree. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner."}], "calculation": {"source_value": "0.6",
    "source_unit": "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value":
    "0.6", "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q4", "topic": "NaH2PO4", "source": {"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1065", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "NaH2PO4\t0.3792\tg/L"}, "decision": "evidence_only", "rationale": "Exact named
    basal source row states 0.3792 g/L; the stored value and chemical form agree.
    Neither local layer has attached ingredient evidence, so retain the amount and
    add exact source evidence through the maintained owner.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "0.3792", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Exact named basal source row states 0.3792 g/L; the stored value
    and chemical form agree. Neither local layer has attached ingredient evidence,
    so retain the amount and add exact source evidence through the maintained owner."},
    {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "0.3792", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Exact named basal source row states
    0.3792 g/L; the stored value and chemical form agree. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}], "calculation": {"source_value": "0.3792", "source_unit":
    "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.3792",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q5", "topic": "Disodium phosphate", "source": {"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1066", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Disodium phosphate\t0.9713\tg/L"}, "decision": "evidence_only", "rationale":
    "Exact named basal source row states 0.9713 g/L; the stored value and chemical
    form agree. Neither local layer has attached ingredient evidence, so retain the
    amount and add exact source evidence through the maintained owner.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "0.9713", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Exact named basal source row states 0.9713 g/L; the stored value
    and chemical form agree. Neither local layer has attached ingredient evidence,
    so retain the amount and add exact source evidence through the maintained owner."},
    {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.9713", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Exact named basal source row states
    0.9713 g/L; the stored value and chemical form agree. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}], "calculation": {"source_value": "0.9713", "source_unit":
    "g/L", "source_strength_x": 1, "receiving_strength_x": 1, "derived_value": "0.9713",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q6", "topic": "Magnesium Sulfate Heptahydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 5", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Magnesium
    Sulfate Heptahydrate\t3\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named source mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03 g/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 3 g/L at 100X; selected medium requires 1X, so 3×(1/100)=0.03 g/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "3", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.03",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q7", "topic": "Nitrilotriacetic acid", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 6", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nitrilotriacetic
    acid\t1.5\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.015",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.015",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1.5 g/L at 100X; selected medium requires 1X, so 1.5×(1/100)=0.015
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "1.5", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.015",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q8", "topic": "Sodium Chloride", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 7", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium
    Chloride\t1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 1 g/L at 100X; selected medium requires 1X, so 1×(1/100)=0.01 g/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "1", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.01",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q9", "topic": "Manganese (II) sulfate monohydrate", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 8", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Manganese
    (II) sulfate monohydrate\t0.5\tg/L"}, "decision": "evidence_only", "rationale":
    "Exact named source mix states 0.5 g/L at 100X; selected medium requires 1X, so
    0.5×(1/100)=0.005 g/L. The stored mass rate agrees; this is a concentration-factor
    derivation, not an assumed batch volume or measured final volume. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.5 g/L at 100X; selected medium requires 1X, so 0.5×(1/100)=0.005
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.5 g/L at 100X; selected medium requires 1X, so 0.5×(1/100)=0.005
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.5", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.005",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q10", "topic": "Cobalt chloride hexahydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 9", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Cobalt
    chloride hexahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q11", "topic": "Zinc sulfate heptahydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 10", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Zinc sulfate
    heptahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact named
    source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q12", "topic": "Calcium Chloride Dihydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 11", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Calcium
    Chloride Dihydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q13", "topic": "Iron (II) sulfate heptahydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 12", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Iron (II)
    sulfate heptahydrate\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named source mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 g/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q14", "topic": "Nickel (II) chloride hexahydrate", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 13", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nickel
    (II) chloride hexahydrate\t0.025\tg/L"}, "decision": "evidence_only", "rationale":
    "Exact named source mix states 0.025 g/L at 100X; selected medium requires 1X,
    so 0.025×(1/100)=0.00025 g/L. The stored mass rate agrees; this is a concentration-factor
    derivation, not an assumed batch volume or measured final volume. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.00025",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.025 g/L at 100X; selected medium requires 1X, so 0.025×(1/100)=0.00025
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.00025",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.025 g/L at 100X; selected medium requires 1X, so 0.025×(1/100)=0.00025
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.025", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.00025",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q15", "topic": "Aluminum potassium sulfate dodecahydrate", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 14", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Aluminum
    potassium sulfate dodecahydrate\t0.02\tg/L"}, "decision": "evidence_only", "rationale":
    "Exact named source mix states 0.02 g/L at 100X; selected medium requires 1X,
    so 0.02×(1/100)=0.0002 g/L. The stored mass rate agrees; this is a concentration-factor
    derivation, not an assumed batch volume or measured final volume. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.0002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.02 g/L at 100X; selected medium requires 1X, so 0.02×(1/100)=0.0002
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.0002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.02 g/L at 100X; selected medium requires 1X, so 0.02×(1/100)=0.0002
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.02", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0002",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q16", "topic": "Copper (II) sulfate pentahydrate", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 15", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Copper
    (II) sulfate pentahydrate\t0.01\tg/L"}, "decision": "evidence_only", "rationale":
    "Exact named source mix states 0.01 g/L at 100X; selected medium requires 1X,
    so 0.01×(1/100)=0.0001 g/L. The stored mass rate agrees; this is a concentration-factor
    derivation, not an assumed batch volume or measured final volume. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q17", "topic": "Boric Acid", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 16", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Boric
    Acid\t0.01\tg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q18", "topic": "Sodium Molybdate Dihydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 17", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium
    Molybdate Dihydrate\t0.01\tg/L"}, "decision": "evidence_only", "rationale": "Exact
    named source mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.01 g/L at 100X; selected medium requires 1X, so 0.01×(1/100)=0.0001
    g/L. The stored mass rate agrees; this is a concentration-factor derivation, not
    an assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.01", "source_unit":
    "g/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value": "0.0001",
    "unit": "G_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q19", "topic": "Sodium selenite pentahydrate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 18", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Sodium
    selenite pentahydrate\t0.3\tmg/L"}, "decision": "evidence_only", "rationale":
    "Exact named source mix states 0.3 mg/L at 100X; selected medium requires 1X,
    so 0.3×(1/100)=0.003 mg/L. The stored mass rate agrees; this is a concentration-factor
    derivation, not an assumed batch volume or measured final volume. Neither local
    layer has attached ingredient evidence, so retain the amount and add exact source
    evidence through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.003",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.3 mg/L at 100X; selected medium requires 1X, so 0.3×(1/100)=0.003
    mg/L. The stored mass rate agrees; this is a concentration-factor derivation,
    not an assumed batch volume or measured final volume. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.003",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.3 mg/L at 100X; selected medium requires 1X, so 0.3×(1/100)=0.003
    mg/L. The stored mass rate agrees; this is a concentration-factor derivation,
    not an assumed batch volume or measured final volume. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}], "calculation": {"source_value": "0.3", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.003", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q20", "topic": "pyridoxine HCl", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 42", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "pyridoxine
    HCl\t10\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 10 mg/L at 100X; selected medium requires 1X, so 10×(1/100)=0.1 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "10", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.1", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q21", "topic": "4-Aminobenzoic acid", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 43", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "4-Aminobenzoic
    acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q22", "topic": "Lipoic acid", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 44", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Lipoic
    acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q23", "topic": "Nicotinic Acid", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 45", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Nicotinic
    Acid\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q24", "topic": "Riboflavin", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 46", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Riboflavin\t5\tmg/L"},
    "decision": "evidence_only", "rationale": "Exact named source mix states 5 mg/L
    at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L. The stored mass
    rate agrees; this is a concentration-factor derivation, not an assumed batch volume
    or measured final volume. Neither local layer has attached ingredient evidence,
    so retain the amount and add exact source evidence through the maintained owner.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q25", "topic": "thiamine HCl", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 47", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "thiamine
    HCl\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q26", "topic": "calcium pantothenate", "source": {"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 48", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "calcium
    pantothenate\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named
    source mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05
    mg/L. The stored mass rate agrees; this is a concentration-factor derivation,
    not an assumed batch volume or measured final volume. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 5 mg/L at 100X; selected medium requires 1X, so 5×(1/100)=0.05 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "5", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.05", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q27", "topic": "biotin", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 49", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "biotin\t2\tmg/L"},
    "decision": "evidence_only", "rationale": "Exact named source mix states 2 mg/L
    at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L. The stored mass
    rate agrees; this is a concentration-factor derivation, not an assumed batch volume
    or measured final volume. Neither local layer has attached ingredient evidence,
    so retain the amount and add exact source evidence through the maintained owner.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "2", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.02", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q28", "topic": "Folic Acid", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 50", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Folic
    Acid\t2\tmg/L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 2 mg/L at 100X; selected medium requires 1X, so 2×(1/100)=0.02 mg/L.
    The stored mass rate agrees; this is a concentration-factor derivation, not an
    assumed batch volume or measured final volume. Neither local layer has attached
    ingredient evidence, so retain the amount and add exact source evidence through
    the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "2", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.02", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q29", "topic": "Cyanocobalamin", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 51", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "Cyanocobalamin\t0.1\tmg/L"},
    "decision": "evidence_only", "rationale": "Exact named source mix states 0.1 mg/L
    at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001 mg/L. The stored mass
    rate agrees; this is a concentration-factor derivation, not an assumed batch volume
    or measured final volume. Neither local layer has attached ingredient evidence,
    so retain the amount and add exact source evidence through the maintained owner.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.001",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 mg/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    mg/L. The stored mass rate agrees; this is a concentration-factor derivation,
    not an assumed batch volume or measured final volume. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.001",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Exact named source
    mix states 0.1 mg/L at 100X; selected medium requires 1X, so 0.1×(1/100)=0.001
    mg/L. The stored mass rate agrees; this is a concentration-factor derivation,
    not an assumed batch volume or measured final volume. Neither local layer has
    attached ingredient evidence, so retain the amount and add exact source evidence
    through the maintained owner."}], "basis_controls": [{"evidence_id": "febaMixes",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}], "calculation": {"source_value": "0.1", "source_unit":
    "mg/L", "source_strength_x": 100, "receiving_strength_x": 1, "derived_value":
    "0.001", "unit": "MG_PER_L", "measured_final_volume_asserted": false}}, {"quantity_id":
    "q30", "topic": "mineral mix strength and receiving factor", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 3", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    "decision": "add", "rationale": "The exact mineral mix is explicitly 100X and
    the receiving medium explicitly 1X. Local origin notes credit the mix name but
    omit its structured identity, strength and evidence. Preserve correct flattened
    rates; represent the exact source mix and its factor without inventing preparation
    instructions or aliquot volumes.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The exact mineral mix is explicitly 100X and the receiving medium explicitly
    1X. Local origin notes credit the mix name but omit its structured identity, strength
    and evidence. Preserve correct flattened rates; represent the exact source mix
    and its factor without inventing preparation instructions or aliquot volumes.",
    "missing": true}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The exact mineral mix is explicitly 100X and the receiving medium explicitly
    1X. Local origin notes credit the mix name but omit its structured identity, strength
    and evidence. Preserve correct flattened rates; represent the exact source mix
    and its factor without inventing preparation instructions or aliquot volumes.",
    "missing": true}], "basis_controls": [{"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1067", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s mineral mix\t1\tX"}]}, {"quantity_id": "q31", "topic": "vitamin mix
    strength and receiving factor", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch069/source09-supplement/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "text line 40", "accessed_at": "2026-10-28T13:50:00.698954Z", "quote": "X\t100\t"},
    "decision": "add", "rationale": "The exact vitamin mix is explicitly 100X and
    the receiving medium explicitly 1X. Local origin notes credit the mix name but
    omit its structured identity, strength and evidence. Preserve correct flattened
    rates; represent the exact source mix and its factor without inventing preparation
    instructions or aliquot volumes.", "layer_assessments": [{"path": "data/merge_yaml/merged/Chakraborty_Basal.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The exact vitamin mix is explicitly 100X and the receiving medium explicitly
    1X. Local origin notes credit the mix name but omit its structured identity, strength
    and evidence. Preserve correct flattened rates; represent the exact source mix
    and its factor without inventing preparation instructions or aliquot volumes.",
    "missing": true}, {"path": "data/normalized_yaml/specialized/chakraborty_basal.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The exact vitamin mix is explicitly 100X and the receiving medium explicitly
    1X. Local origin notes credit the mix name but omit its structured identity, strength
    and evidence. Preserve correct flattened rates; represent the exact source mix
    and its factor without inventing preparation instructions or aliquot volumes.",
    "missing": true}], "basis_controls": [{"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch069/source09/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
    "locator": "text line 1068", "accessed_at": "2026-10-28T13:47:55.683994Z", "quote":
    "Wolfe''s vitamin mix\t1\tX"}]}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: All 58 asserted CHEBI slots use29 active current OLS identities with matching
    canonical labels and source-specific salt/hydrate forms. Exact MIM preferred rows
    include MAPPED and REJECTED aliases plus ontology-linked records of different
    granularity; these are not interchangeable endorsements. The source monohydrate
    CAS/mass and exact compound name agree despite its erroneous dihydrate synonym.
    Lipoic acid remains non-stereospecific at the asserted ontology level; no enantiomer
    is inferred. Calcium pantothenate source FW 238.27 is a hemicalcium-unit convention,
    whereas OLS 31345 represents 2C9H16NO5.Ca at 476.536; this does not alter the
    supported mass-per-volume amount.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete target and owner histories and their references were read. The
    single-owner generated record has unchanged ingredient content and no attached
    claims; the import provenance names a file and generic repository but no immutable
    upstream revision. Current FEBA bytes support the present source correspondence,
    not the original import event. Current importer/grounding/merger behavior is distinguished
    from historical execution; no history is overwritten.
  target_ids:
  - CultureMech:015502
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
  - CultureMech:015502
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:015502
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-015502-supported-rates-need-exact-claim-evidence-and-mix-provenance
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Supported rates need exact claim evidence and mix provenance
  description: All 29 stored rates are supported by the exact versioned FEBA definition
    and its named 100X mixes used at 1X. Both layers retain flattened components with
    free-text origin notes but no attached quantity evidence or structured mix strength/source
    linkage. Preserve those correct rates and origin notes while representing the
    exact named source dependencies and calculations through the maintained owner;
    unrelated ATCC or minus-component mixes are not substitutes.
  target_ids:
  - CultureMech:015502
  field_paths:
  - ingredients
  - solutions
  - sources
  evidence_ids:
  - local-target
  - owner-1
  - febaMedia
  - febaMixes
  - quantities
  - writer-import
  rule_id: source-quantity-and-mix-provenance
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-015502-historical-upstream-version-remains-unresolved
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical upstream version remains unresolved
  description: The recorded CultureBotHT source is a generic repository URL and imported
    filename. Its current public API request returned 404, while the recoverable FEBA
    revision is a later source observation. Add accurately timed versioned source
    citations and preserve the distinction from the original import; an access failure
    does not establish deletion or nonexistence.
  target_ids:
  - CultureMech:015502
  field_paths:
  - sources
  - curation_history
  evidence_ids:
  - local-target
  - owner-1
  - culturebotRepo
  - febaCommit
  - writer-import
  rule_id: source-version-provenance
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-015502-unmapped-ingredient-flag-is-stale-for-current-term-occupancy
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Unmapped-ingredient flag is stale for current term occupancy
  description: Both local layers retain has_unmapped_ingredients although each of
    their 29 ingredients now has an explicit supported CHEBI term. The current importer
    appends this flag when IDs are absent and does not remove an inherited flag. Re-evaluate
    the flag after curation while preserving historical entries; do not equate mere
    ID presence with scientific validity or add arbitrary secondary identifiers.
  target_ids:
  - CultureMech:015502
  field_paths:
  - data_quality_flags
  evidence_ids:
  - local-target
  - owner-1
  - grounding
  - writer-import
  rule_id: current-quality-flag-consistency
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Attach exact versioned base and mix excerpts to maintained ingredient
    evidence, including the 100X-to-1X factor. Preserve all 29 supported mass rates
    and explicit chemical forms; represent the two source mix identities without inventing
    physical preparation volumes. Regenerate the compatible target only after owner
    curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: The recorded CultureBotHT source is a generic repository URL and imported
    filename. Its current public API request returned 404, while the recoverable FEBA
    revision is a later source observation. Add accurately timed versioned source
    citations and preserve the distinction from the original import; an access failure
    does not establish deletion or nonexistence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Both local layers retain has_unmapped_ingredients although each of
    their 29 ingredients now has an explicit supported CHEBI term. The current importer
    appends this flag when IDs are absent and does not remove an inherited flag. Re-evaluate
    the flag after curation while preserving historical entries; do not equate mere
    ID presence with scientific validity or add arbitrary secondary identifiers.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/chakraborty_basal.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- 'Partial completion: the original CultureBotHT import snapshot/revision is unavailable
  through the current public repository API; present FEBA correspondence does not
  authenticate past execution.'
- All 29 stored ingredient rates on both layers were assessed, including 24 mix-derived
  contributions. The source supports concentration-factor scaling only; no measured
  final volume, aliquot, culture condition or preparation instruction is inferred.
- The current OLS and MIM snapshots support current identifier review only. Rejected
  aliases and linked records are not used to replace valid primary chemical identities.
  No literature linked from ontology objects was treated as independently verified.
- No organism-specific growth evidence is present in the scoped source. No taxon,
  strain, carbon amendment, pH or cultivation method is proposed from a medium or
  laboratory name.
- The historical concentration reports and exact coverage row are diagnostics; matching
  digests authenticate the local record snapshot, not an unavailable external source
  event. All existing history remains preserved.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
