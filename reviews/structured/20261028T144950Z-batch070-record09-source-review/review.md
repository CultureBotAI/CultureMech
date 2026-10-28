# Clostridium Cellulolytic medium source and formulation review

- Review: 20261028T144950Z-batch070-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T14:33:56.536593Z
- Finished UTC: 2026-10-28T14:49:50.045205Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

ATCC 1368 and the exact TOGO M2711/M2701 transcriptions establish the source identity but contradict the stored iron, resazurin and water units. Other masses lack an explicit final-volume basis. Both owners omit source preparation and the optional solid branch; M2701 alone retains an unquantified alkali stub. The trihydrate phosphate name must remain distinct from the ontology formula. All 37 local concentration fields were assessed.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch070 native selection index 09.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009263 | data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml | generated | clostridium_cellulolytic_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009263 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:009263 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:009263 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:009263 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Two maintained contributors and one primary medium

identity: supported. Targets: CultureMech:009263.

The declared stems each resolve uniquely. M2711/CultureMech:009263 and M2701/CultureMech:009254 have distinct provenance but both name ATCC 1368. The target follows M2711 and lacks the M2701 alkali stub. This is a source-stage representation difference; identity alone does not make current formulations losslessly mergeable.

### Classification and source branch boundaries

representation: supported. Targets: CultureMech:009263.

Yeast extract supports complex/undefined composition. The nongelled basal branch is consistent with LIQUID, while agar belongs to an explicitly optional branch. Provider role/property notes are transcription context; no strain-specific nutritional requirement or experimental growth follows from them. Current generic application and bacterial category do not establish a target-organism claim.

### Historical diagnostics and current evidence gap

evidence: concern. Targets: CultureMech:009263.

The complete three historical reports checked zero of 12, 12 and 13 quantity claims. Their record hashes match current files; neither those hashes nor the automatic flags authenticate source amounts. Both owner rows in the content manifest flag variable concentrations. No attached ingredient evidence currently records the primary excerpts used here.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:009263.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Yeast Extract", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 9–9", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 9, "line_end": 9, "quote": "       Yeast Extract………………………………..2.0                       g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q2", "topic": "CaCl2 x 2H2O", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 7–7", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 7, "line_end": 7, "quote": "       CaCl2 x 2H2O………………………………0.15                         g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q3", "topic": "KH2PO4", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 4–4", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 4, "line_end": 4, "quote": "       KH2PO4…………………………………….1.5                             g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q4", "topic": "Resazurin", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 11–11", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 11, "line_end": 11, "quote": "       Resazurin……………………………………2.0                           ml"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL, not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume addition and leave final mass contribution unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL, not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume addition and leave final mass contribution unresolved."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL, not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume addition and leave final mass contribution unresolved."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL, not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume addition and leave final mass contribution unresolved."}]}, {"quantity_id": "q5", "topic": "MgCl2 x 6H2O", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 6–6", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 6, "line_end": 6, "quote": "       MgCl2 x 6H2O……………………………...1.0                        g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q6", "topic": "(NH4)2SO4", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 5–5", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 5, "line_end": 5, "quote": "       (NH4)2SO4…………………………………1.3                            g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "1.3", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "1.3", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "1.3", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q7", "topic": "K2HPO4 x 3H2O", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 3–3", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 3, "line_end": 3, "quote": "       K2HPO4 x 3H2O…………………………...2.9                        g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The named material is the trihydrate; the current CHEBI formula does not encode its three waters, so do not calculate molarity from the anhydrous formula weight.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The named material is the trihydrate; the current CHEBI formula does not encode its three waters, so do not calculate molarity from the anhydrous formula weight."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The named material is the trihydrate; the current CHEBI formula does not encode its three waters, so do not calculate molarity from the anhydrous formula weight."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The named material is the trihydrate; the current CHEBI formula does not encode its three waters, so do not calculate molarity from the anhydrous formula weight."}]}, {"quantity_id": "q8", "topic": "Cellulose", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 10–10", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 10, "line_end": 10, "quote": "       Cellulose…………………………………….7.5                          g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis."}]}, {"quantity_id": "q9", "topic": "FeSO4", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 8–8", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 8, "line_end": 8, "quote": "       FeSO4……………………………………….1.25                            mg or ( 1.25ml of mg/ml solution)"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25 mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL of mg/mL solution without a numeric strength; visual inspection confirms the omission. Do not supply 1 mg/mL or infer a final-volume-normalized rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25 mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL of mg/mL solution without a numeric strength; visual inspection confirms the omission. Do not supply 1 mg/mL or infer a final-volume-normalized rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25 mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL of mg/mL solution without a numeric strength; visual inspection confirms the omission. Do not supply 1 mg/mL or infer a final-volume-normalized rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25 mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL of mg/mL solution without a numeric strength; visual inspection confirms the omission. Do not supply 1 mg/mL or infer a final-volume-normalized rate."}]}, {"quantity_id": "q10", "topic": "DI Water", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 13–13", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 13, "line_end": 13, "quote": "       DI Water…………………………………….1.0                          L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent addition, not 1 g/L. This ingredient volume is not an instruction to make the completed medium up to 1 L.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent addition, not 1 g/L. This ingredient volume is not an instruction to make the completed medium up to 1 L."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent addition, not 1 g/L. This ingredient volume is not an instruction to make the completed medium up to 1 L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent addition, not 1 g/L. This ingredient volume is not an instruction to make the completed medium up to 1 L."}]}, {"quantity_id": "q11", "topic": "Cysteine HCl", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 12–12", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 12, "line_end": 12, "quote": "       Cysteine HCl (add after boiling)……………1.0             g"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The primary specifies addition after boiling; it does not identify L/D stereochemistry or hydrochloride hydration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The primary specifies addition after boiling; it does not identify L/D stereochemistry or hydrochloride hydration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The primary specifies addition after boiling; it does not identify L/D stereochemistry or hydrochloride hydration."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this mass per stated batch, with 1 L of water as a separate ingredient. It does not instruct making up to a measured final volume. Preserve the batch mass and explicit form; the stored g/L denominator remains unresolved pending a documented basis. The primary specifies addition after boiling; it does not identify L/D stereochemistry or hydrochloride hydration."}]}, {"quantity_id": "q12", "topic": "N2", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 14–15", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 14, "line_end": 15, "quote": "                Adjust final pH to 7.2. Prepare medium, dispense under a constant flow of nitrogen,\n       stopper and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust pH to"}, "decision": "unresolved", "rationale": "The source describes a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default placeholder, not a source-quantified dose. Preserve gas identity and put the supported stage in preparation; do not invent a gas concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default placeholder, not a source-quantified dose. Preserve gas identity and put the supported stage in preparation; do not invent a gas concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default placeholder, not a source-quantified dose. Preserve gas identity and put the supported stage in preparation; do not invent a gas concentration."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default placeholder, not a source-quantified dose. Preserve gas identity and put the supported stage in preparation; do not invent a gas concentration."}]}, {"quantity_id": "q13", "topic": "NaOH adjustment stub", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 15–16", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 15, "line_end": 16, "quote": "       stopper and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust pH to\n       7.5 with NaOH."}, "decision": "unresolved", "rationale": "M2701 alone contains an unquantified NaOH solution stub. The primary locates NaOH in the optional solid branch with pH 7.5; no dose or strength is supplied. Do not automatically insert this stub into the basal liquid medium or fill its composition from a namesake stock.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "M2701 alone contains an unquantified NaOH solution stub. The primary locates NaOH in the optional solid branch with pH 7.5; no dose or strength is supplied. Do not automatically insert this stub into the basal liquid medium or fill its composition from a namesake stock."}]}, {"quantity_id": "q14", "topic": "Basal pH and preparation stages", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 12–16", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 12, "line_end": 16, "quote": "       Cysteine HCl (add after boiling)……………1.0             g\n       DI Water…………………………………….1.0                          L\n                Adjust final pH to 7.2. Prepare medium, dispense under a constant flow of nitrogen,\n       stopper and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust pH to\n       7.5 with NaOH."}, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}, {"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "All three local records omit preparation_steps and pH. Preserve the primary basal pH and sequence, including cysteine after boiling, nitrogen during dispensing, stoppering and the stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen flow rate, incubation temperature or growth duration; none may be invented.", "missing": true}]}, {"quantity_id": "q15", "topic": "Optional solid-medium branch", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0", "locator": "PDF page 1; derived text physical LF lines 15–16", "accessed_at": "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start": 15, "line_end": 16, "quote": "       stopper and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust pH to\n       7.5 with NaOH."}, "decision": "evidence_only", "rationale": "The primary solid branch specifies an agar batch addition and a different pH adjustment. Keep it explicitly optional and separate from basal liquid identity; its final volume and NaOH amount remain unspecified. Do not silently add agar or the solid pH to the basal record.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:009263.

All 51 current ingredient CHEBI slots (nine unique IDs) use active OLS objects and matching canonical labels. Calcium dihydrate, magnesium hexahydrate, KH2PO4, ammonium sulfate, cellulose and nitrogen identities agree with the named sources. FeSO4 is printed without a hydrate, so its present anhydrous-form term is compatible with the printed formula; no heptahydrate is inferred. Resazurin is not replaced by sodium resazurin from generic MIM aliases. CHEBI:131527 has formula HO4P.2K and mass 174.174, while the source explicitly names three waters; its related trihydrate synonym does not make that formula hydrated. Retain source-form detail and avoid anhydrous molarity. The 180 MIM rows include MAPPED and REJECTED aliases, plus linked-only hydrate records; these do not override chemical identity. Yeast extract, DI water and cysteine HCl lack primary IDs: yeast has a catalog candidate, but no unverified identifier is asserted; cysteine stereochemistry/hydration are unspecified.

### History and evidence scope

provenance: concern. Targets: CultureMech:009263.

Complete histories of all three records were read. They separately record imports, enrichment, gas/alkali defaults, identifier assignment, name normalization, legacy-field/link migration and canonical labels; M2701 also records solution migration/default naming. The generated target adds two merge events and omits the M2701-specific history. Current writers and packaged MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9 are current observations, not recovered historical execution. Preserve all original histories and distinct source IDs during curation.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:009263.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:009263.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Source amount units and concentration basis need repair

major / open / confirmed; issue key: culturemech-009263-source-amount-units-and-concentration-basis-need-repair.

All layers store resazurin 2 g/L, FeSO4 1.25 g/L and DI water 1 g/L. The exact primary instead supplies a volume addition, a milligram batch mass and a litre solvent addition. Other gram numerals match batch masses but an explicit final-volume denominator is absent. Attach exact source evidence and separate batch quantities from concentrations; unknown resazurin strength and the incomplete alternative iron-stock expression prevent mass-contribution reconstruction.

### f2: Preparation and optional solid branch are omitted

major / open / confirmed; issue key: culturemech-009263-preparation-and-optional-solid-branch-are-omitted.

All three local records lack basal pH and preparation_steps despite explicit primary text. The second owner has an unquantified alkali stub associated by the source with an optional solid branch; copying it into the liquid record would lose that context. Preserve branch-specific pH, agar and adjustment roles while keeping unspecified dose, strength and temperatures unresolved.

### f3: Phosphate trihydrate needs explicit form preservation

minor / open / confirmed; issue key: culturemech-009263-phosphate-trihydrate-needs-explicit-form-preservation.

The source and local ingredient name specify K2HPO4 x 3H2O, but CHEBI:131527 has the anhydrous elemental formula and mass. Its current related synonym mentions trihydrate, so this is a form-granularity limitation rather than a canonical-label error. Preserve the specified hydrate in evidence and representation, and do not use the bare ontology mass for molar conversion. No unverified replacement term is proposed.

## Recommended Actions And Acceptance Checks

### action1

Curate both maintained owners using the exact primary batch amounts and source units. Preserve unspecified stock strengths and final volume as unresolved; do not infer densities or stock recipes. Attach claim-level source excerpts and any justified arithmetic, then regenerate compatible outputs.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Represent the supported basal preparation and optional solid branch separately through maintained records or explicit variant context. Reconcile the M2701 stub without inventing composition or promoting solid conditions into the liquid definition. Retain contributor identities and history before regeneration.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

The source and local ingredient name specify K2HPO4 x 3H2O, but CHEBI:131527 has the anhydrous elemental formula and mass. Its current related synonym mentions trihydrate, so this is a form-granularity limitation rather than a canonical-label error. Preserve the specified hydrate in evidence and representation, and do not use the bare ontology mass for molar conversion. No unverified replacement term is proposed.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch070/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| atcc1368 | https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx; PDF page 1, complete table and final paragraph; physical LF text lines 1–16 | supports | Exact declared primary sheet read in full as text and page image. It gives batch amounts, basal preparation and an optional solid branch. The iron stock alternative visibly omits a numeric strength; resazurin strength and final batch volume are not specified. |
| togo2711 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2711; meta, components[].items[], comments[] | supports | Exact M2711 metadata, all items and comments read. Both transcriptions name the same ATCC sheet and basal pH; M2701 separately lists an unquantified NaOH solution. Provider roles are provenance, not experimental growth evidence. |
| togo2701 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2701; meta, components[].items[], comments[] | supports | Exact M2701 metadata, all items and comments read. Both transcriptions name the same ATCC sheet and basal pH; M2701 separately lists an unquantified NaOH solution. Provider roles are provenance, not experimental growth evidence. |
| atcc35319 | https://www.atcc.org/products/35319; title and Product category/Strain designation/Type strain/Isolation source; extracted physical LF lines 1 and262–271 | context_only | Collection identity context only: Clostridium cellulolyticum H10 [JCM 6584], type strain, from decayed grass in compost. This is not transferred as a growth claim or as culture-condition evidence. |
| primary-text | REVIEW_WORK/batch070/source09/atcc1368.txt | context_only | Complete primary PDF text; physical LF lines, with form feed preserved. |
| primary-image | REVIEW_WORK/batch070/source09/atcc1368-page1.png | context_only | Complete primary page visually inspected, including the incomplete iron-stock expression. |
| derivation | REVIEW_WORK/batch070/source09/derivation.json | context_only | Exact successful text and image derivation commands, times and file hashes. |
| collection-text | REVIEW_WORK/batch070/source09/atcc35319.txt | context_only | Derived collection text; only identity fields and title used. |
| historical-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_Cellulolytic_medium.md; Complete document | context_only | Complete October5 report read, with matching current local record hash. Its quantity checks were not performed; plausibility flags are derivative diagnostics. |
| historical-report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.md; Complete document | context_only | Complete October5 report read, with matching current local record hash. Its quantity checks were not performed; plausibility flags are derivative diagnostics. |
| historical-report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulolytic_medium.md; Complete document | context_only | Complete October5 report read, with matching current local record hash. Its quantity checks were not performed; plausibility flags are derivative diagnostics. |
| writer-import | src/culturemech/import/togo_importer.py; _ingredient_from_item; _extract_primary_components; _extract_preparation_steps; _parse_unit; _convert_to_culturemech | context_only | Current importer distinguishes primary sections and preparations, but still maps bare g/mg/mL to per-litre units. Current code does not authenticate the historical import or establish final volume. |
| writer-solutions | scripts/migrate_solutions_from_ingredients.py; _resolve_solution; _migrate_media_file | context_only | Current migration preserves an unresolved solution stub and copies its existing amount; this does not verify NaOH strength or historical execution. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merger delegates to compatible formulation comparison. The historical ingredient-similarity merge is a separate artifact. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current equality includes formulation content and rejects incompatible formulations before unioning permitted evidence. Differing solutions cannot simply be discarded. |
| mim-pool | REVIEW_WORK/batch070/record09/mim-row-pool.json | context_only | All 180 packaged rows matching an asserted CHEBI identifier or ontology_id; exact preferred, rejected and linked-only rows are distinguished. |
| historical-joins | REVIEW_WORK/batch070/record09/historical-joins.json | context_only | Exact selected historical manifest rows and current hashes; these are diagnostics, not source evidence. |
| ols86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols18246 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch070/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch070/record09/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch070/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch070/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch070/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch070/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch070/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch070/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch070/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Partial completion: exact primary and TOGO sources were fully read, but the primary leaves resazurin stock strength, numeric iron-stock strength and final-volume basis unresolved. Review coverage includes every stored concentration; no unsupported replacement rates are supplied.
- The primary optional solid branch is kept separate from basal liquid identity. No autoclave temperature, gas flow rate, incubation condition, strain growth assertion, cysteine stereochemistry or unprinted salt hydrate is inferred.
- Collection identity was used only to establish ordinary environmental organism context. It does not attach a target-organism growth claim or replace the exact medium sheet.
- Current OLS and packaged MIM rows are current identity observations. Misleading/rejected aliases and ontology-linked hydrate variants are not endorsements or evidence of historical catalog membership. No ontology-linked literature was adopted.
- Three historical reports and current writer code were inspected as diagnostics and process context. They do not authenticate historical external source bytes or execution; all existing records and history remain unchanged.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T144950Z-batch070-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Clostridium Cellulolytic medium source and formulation review
started_at: '2026-10-28T14:33:56.536593Z'
finished_at: '2026-10-28T14:49:50.045205Z'
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
summary: ATCC 1368 and the exact TOGO M2711/M2701 transcriptions establish the source
  identity but contradict the stored iron, resazurin and water units. Other masses
  lack an explicit final-volume basis. Both owners omit source preparation and the
  optional solid branch; M2701 alone retains an unquantified alkali stub. The trihydrate
  phosphate name must remain distinct from the ontology formula. All 37 local concentration
  fields were assessed.
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
  - path: data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
    sha256: 71f25dddb39a492311a82fa68e65792db7eee2c117447e618cdb6cc500a8ba28
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    sha256: 5efa8cb069cbd5743090f63b8c410d0bb241e47542541d6091ade4a7c9d73b25
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    sha256: fafc4b5adc8e4c47670ce8d7ec5c88f6f3b555e0c6b38b6b68bbc4e2e7ec681b
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_Cellulolytic_medium.md
    sha256: d9991014835ab37f4bea4bf0364ec729c93b9d277cabb06342c654708ccccb65
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.md
    sha256: f1acfaadc23f6460647ecab79876a4bd4d4e59f1d86eac0419aee7472f29d9b7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulolytic_medium.md
    sha256: 0d4d651d15eb5edb9837bfb3d3db3770892d395716aed25dd3e642349d2cfff8
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
  selection: Actual batch070 native selection index 09.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009263
targets:
- target_id: CultureMech:009263
  path: data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
  label: clostridium_cellulolytic_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009263
  command: just validate-schema data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
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
  - CultureMech:009263
  command: just validate-strict data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
    --out REVIEW_WORK/batch070/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:009263
  command: just validate-terms data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
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
  - CultureMech:009263
  command: just validate-references data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 71f25dddb39a492311a82fa68e65792db7eee2c117447e618cdb6cc500a8ba28
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 5efa8cb069cbd5743090f63b8c410d0bb241e47542541d6091ade4a7c9d73b25
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: fafc4b5adc8e4c47670ce8d7ec5c88f6f3b555e0c6b38b6b68bbc4e2e7ec681b
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch070/record09/identity-search.json
  accessed_at: '2026-10-28T14:46:27.929577Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 4230a851c04017f6dce7c49710f922fb77ad87693830786cdc0f202c7bdbc881
- evidence_id: atcc1368
  kind: primary_source
  reference: https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx
  locator: PDF page 1, complete table and final paragraph; physical LF text lines
    1–16
  accessed_at: '2026-10-28T14:35:31.702307Z'
  support: supports
  summary: Exact declared primary sheet read in full as text and page image. It gives
    batch amounts, basal preparation and an optional solid branch. The iron stock
    alternative visibly omits a numeric strength; resazurin strength and final batch
    volume are not specified.
  snapshot_sha256: ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0
- evidence_id: togo2711
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2711
  locator: meta, components[].items[], comments[]
  accessed_at: '2026-10-28T14:35:31.951086Z'
  support: supports
  summary: Exact M2711 metadata, all items and comments read. Both transcriptions
    name the same ATCC sheet and basal pH; M2701 separately lists an unquantified
    NaOH solution. Provider roles are provenance, not experimental growth evidence.
  snapshot_sha256: 6a94fbfa7b56242182e3208e93bd2b8426653b340c8756294e18cb69175728ed
- evidence_id: togo2701
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2701
  locator: meta, components[].items[], comments[]
  accessed_at: '2026-10-28T14:35:31.945533Z'
  support: supports
  summary: Exact M2701 metadata, all items and comments read. Both transcriptions
    name the same ATCC sheet and basal pH; M2701 separately lists an unquantified
    NaOH solution. Provider roles are provenance, not experimental growth evidence.
  snapshot_sha256: 391c0b3cb8dccfeb0bc4e5bdfd5aa441254349bc52da5416620338e3074a96bf
- evidence_id: atcc35319
  kind: primary_source
  reference: https://www.atcc.org/products/35319
  locator: title and Product category/Strain designation/Type strain/Isolation source;
    extracted physical LF lines 1 and262–271
  accessed_at: '2026-10-28T14:35:36.022509Z'
  support: context_only
  summary: 'Collection identity context only: Clostridium cellulolyticum H10 [JCM
    6584], type strain, from decayed grass in compost. This is not transferred as
    a growth claim or as culture-condition evidence.'
  snapshot_sha256: cbc5dc0101d288c2f0cd8deea51048b4bd1ea020d5509e5a2696ce7113631640
- evidence_id: primary-text
  kind: record_content
  reference: REVIEW_WORK/batch070/source09/atcc1368.txt
  accessed_at: '2026-10-28T14:46:27.930883Z'
  support: context_only
  summary: Complete primary PDF text; physical LF lines, with form feed preserved.
  snapshot_sha256: ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c
- evidence_id: primary-image
  kind: record_content
  reference: REVIEW_WORK/batch070/source09/atcc1368-page1.png
  accessed_at: '2026-10-28T14:46:27.930922Z'
  support: context_only
  summary: Complete primary page visually inspected, including the incomplete iron-stock
    expression.
  snapshot_sha256: 3e0c59c986d47aff7f875aa5c0858fc744bc40f72624b61a87c22a36beddc350
- evidence_id: derivation
  kind: record_content
  reference: REVIEW_WORK/batch070/source09/derivation.json
  accessed_at: '2026-10-28T14:46:27.931206Z'
  support: context_only
  summary: Exact successful text and image derivation commands, times and file hashes.
  snapshot_sha256: 07e2257b50020742dce63f961de01ae1466027411aae8111d57cdaca350cc7c5
- evidence_id: collection-text
  kind: record_content
  reference: REVIEW_WORK/batch070/source09/atcc35319.txt
  accessed_at: '2026-10-28T14:46:27.931360Z'
  support: context_only
  summary: Derived collection text; only identity fields and title used.
  snapshot_sha256: d34d624121ee10776c914c06cc2d9b1c3e7e28d28c08145b1af65db3b72a238c
- evidence_id: historical-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_Cellulolytic_medium.md
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete October5 report read, with matching current local record hash.
    Its quantity checks were not performed; plausibility flags are derivative diagnostics.
  snapshot_sha256: d9991014835ab37f4bea4bf0364ec729c93b9d277cabb06342c654708ccccb65
- evidence_id: historical-report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.md
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete October5 report read, with matching current local record hash.
    Its quantity checks were not performed; plausibility flags are derivative diagnostics.
  snapshot_sha256: f1acfaadc23f6460647ecab79876a4bd4d4e59f1d86eac0419aee7472f29d9b7
- evidence_id: historical-report-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulolytic_medium.md
  locator: Complete document
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Complete October5 report read, with matching current local record hash.
    Its quantity checks were not performed; plausibility flags are derivative diagnostics.
  snapshot_sha256: 0d4d651d15eb5edb9837bfb3d3db3770892d395716aed25dd3e642349d2cfff8
- evidence_id: writer-import
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _extract_primary_components; _extract_preparation_steps;
    _parse_unit; _convert_to_culturemech
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Current importer distinguishes primary sections and preparations, but still
    maps bare g/mg/mL to per-litre units. Current code does not authenticate the historical
    import or establish final volume.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-solutions
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Current migration preserves an unresolved solution stub and copies its
    existing amount; this does not verify NaOH strength or historical execution.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Current merger delegates to compatible formulation comparison. The historical
    ingredient-similarity merge is a separate artifact.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T14:46:27.881394Z'
  support: context_only
  summary: Current equality includes formulation content and rejects incompatible
    formulations before unioning permitted evidence. Differing solutions cannot simply
    be discarded.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mim-pool
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/mim-row-pool.json
  accessed_at: '2026-10-28T14:46:27.951000Z'
  support: context_only
  summary: All 180 packaged rows matching an asserted CHEBI identifier or ontology_id;
    exact preferred, rejected and linked-only rows are distinguished.
  snapshot_sha256: ad90b928452dce1983f1112755351c576df31b9b9298a852010d26ad14f30a1b
- evidence_id: historical-joins
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/historical-joins.json
  accessed_at: '2026-10-28T14:46:27.951046Z'
  support: context_only
  summary: Exact selected historical manifest rows and current hashes; these are diagnostics,
    not source evidence.
  snapshot_sha256: 0f0308a800956eed02a3a3961a8337f8c2e9277b8e3246b08f0e1f861a64d700
- evidence_id: ols86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:32.906564Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ols63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:33.018470Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: ols8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:33.211141Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: ols86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:33.107471Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: ols62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:32.510056Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: ols131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:32.617193Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: ols18246
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:32.310087Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f7abaf5dd620c7de0e80d8e5718cbab4fa7a6455577d0a176847d4e8829be90c
- evidence_id: ols75832
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:33.020658Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b9119cb3893b1a8171f719ef3e8fe6e5775a4fd59575baec8cd6da953801d089
- evidence_id: ols17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T14:35:31.906784Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/quantity-inventory.json
  accessed_at: '2026-10-28T14:49:50.016240Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 993fa6e149a977e9ae09992753b6d95bef0b954e4f0ad2460f87a6e46e761ba1
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/grounding-inventory.json
  accessed_at: '2026-10-28T14:46:27.963804Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: ff9e081f1e2402167d1341cffa91568c9dd0290d834abf169170fbd961a134b5
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T14:46:27.963870Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: b09e692822d43b8ecbc64b6060f250fbfeb25454b6708f17d45b0f8a69f20b27
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch070/record09/scalar-census.json
  accessed_at: '2026-10-28T14:46:27.963893Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: e7ee51c589e1d7aa646d181d94d359c77c73ce3a97ef6637580238030a325bc6
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch070/record09/validate-schema.json
  accessed_at: '2026-10-28T14:33:57.588551Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 447f34c12fb35ff54ed86fe0d09deaea00f0ac20060737945bbc274539109daf
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch070/record09/validate-strict.json
  accessed_at: '2026-10-28T14:33:58.506801Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch070/record09/strict.tsv\n"
  snapshot_sha256: d42068a48db053a06a700526285f2cbecbd0e0ce3bed3e107c9add1e4a9bc50b
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch070/record09/validate-terms.json
  accessed_at: '2026-10-28T14:33:59.505618Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: e55a255522899127c00f6760c6299671d919d92c17b4fe99f22b227d3931d4a7
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch070/record09/validate-references.json
  accessed_at: '2026-10-28T14:34:00.162736Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: f630af5b9b56819f41f1b299b388b1a41055da81d06e4a67aa4b1a99070664f3
assessments:
- assessment_id: a1
  area: identity
  topic: Two maintained contributors and one primary medium
  outcome: supported
  summary: The declared stems each resolve uniquely. M2711/CultureMech:009263 and
    M2701/CultureMech:009254 have distinct provenance but both name ATCC 1368. The
    target follows M2711 and lacks the M2701 alkali stub. This is a source-stage representation
    difference; identity alone does not make current formulations losslessly mergeable.
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - identity-search
  - local-target
  - owner-1
  - owner-2
  - atcc1368
  - togo2711
  - togo2701
- assessment_id: a2
  area: representation
  topic: Classification and source branch boundaries
  outcome: supported
  summary: Yeast extract supports complex/undefined composition. The nongelled basal
    branch is consistent with LIQUID, while agar belongs to an explicitly optional
    branch. Provider role/property notes are transcription context; no strain-specific
    nutritional requirement or experimental growth follows from them. Current generic
    application and bacterial category do not establish a target-organism claim.
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - atcc1368
  - togo2711
  - togo2701
  - local-target
- assessment_id: a3
  area: evidence
  topic: Historical diagnostics and current evidence gap
  outcome: concern
  summary: The complete three historical reports checked zero of 12, 12 and 13 quantity
    claims. Their record hashes match current files; neither those hashes nor the
    automatic flags authenticate source amounts. Both owner rows in the content manifest
    flag variable concentrations. No attached ingredient evidence currently records
    the primary excerpts used here.
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - historical-report-1
  - historical-report-2
  - historical-report-3
  - historical-joins
  - atcc1368
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Yeast Extract", "source": {"evidence_id":
    "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 9–9", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    9, "line_end": 9, "quote": "       Yeast Extract………………………………..2.0                       g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this
    mass per stated batch, with 1 L of water as a separate ingredient. It does not
    instruct making up to a measured final volume. Preserve the batch mass and explicit
    form; the stored g/L denominator remains unresolved pending a documented basis."},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this
    mass per stated batch, with 1 L of water as a separate ingredient. It does not
    instruct making up to a measured final volume. Preserve the batch mass and explicit
    form; the stored g/L denominator remains unresolved pending a documented basis."}]},
    {"quantity_id": "q2", "topic": "CaCl2 x 2H2O", "source": {"evidence_id": "atcc1368",
    "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 7–7", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    7, "line_end": 7, "quote": "       CaCl2 x 2H2O………………………………0.15                         g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}]}, {"quantity_id": "q3", "topic": "KH2PO4", "source": {"evidence_id":
    "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 4–4", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    4, "line_end": 4, "quote": "       KH2PO4…………………………………….1.5                             g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}]}, {"quantity_id": "q4", "topic": "Resazurin", "source":
    {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 11–11", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 11, "line_end": 11, "quote": "       Resazurin……………………………………2.0                           ml"},
    "decision": "correct", "rationale": "Primary resazurin is 2.0 mL, not 2 g/L. Its
    stock strength and salt form are unspecified; preserve the volume addition and
    leave final mass contribution unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL,
    not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume
    addition and leave final mass contribution unresolved."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL,
    not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume
    addition and leave final mass contribution unresolved."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary resazurin is 2.0 mL,
    not 2 g/L. Its stock strength and salt form are unspecified; preserve the volume
    addition and leave final mass contribution unresolved."}]}, {"quantity_id": "q5",
    "topic": "MgCl2 x 6H2O", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 6–6", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    6, "line_end": 6, "quote": "       MgCl2 x 6H2O……………………………...1.0                        g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this
    mass per stated batch, with 1 L of water as a separate ingredient. It does not
    instruct making up to a measured final volume. Preserve the batch mass and explicit
    form; the stored g/L denominator remains unresolved pending a documented basis."},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet gives this
    mass per stated batch, with 1 L of water as a separate ingredient. It does not
    instruct making up to a measured final volume. Preserve the batch mass and explicit
    form; the stored g/L denominator remains unresolved pending a documented basis."}]},
    {"quantity_id": "q6", "topic": "(NH4)2SO4", "source": {"evidence_id": "atcc1368",
    "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 5–5", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    5, "line_end": 5, "quote": "       (NH4)2SO4…………………………………1.3                            g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "1.3", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "1.3",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "1.3",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}]}, {"quantity_id": "q7", "topic": "K2HPO4 x 3H2O", "source":
    {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 3–3", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    3, "line_end": 3, "quote": "       K2HPO4 x 3H2O…………………………...2.9                        g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis. The
    named material is the trihydrate; the current CHEBI formula does not encode its
    three waters, so do not calculate molarity from the anhydrous formula weight.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The named material is the trihydrate; the current CHEBI formula
    does not encode its three waters, so do not calculate molarity from the anhydrous
    formula weight."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The named material is the trihydrate; the current CHEBI formula
    does not encode its three waters, so do not calculate molarity from the anhydrous
    formula weight."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "2.9",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The named material is the trihydrate; the current CHEBI formula
    does not encode its three waters, so do not calculate molarity from the anhydrous
    formula weight."}]}, {"quantity_id": "q8", "topic": "Cellulose", "source": {"evidence_id":
    "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 10–10", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 10, "line_end": 10, "quote": "       Cellulose…………………………………….7.5                          g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "7.5",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "7.5",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis."}]}, {"quantity_id": "q9", "topic": "FeSO4", "source": {"evidence_id":
    "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 8–8", "accessed_at": "2026-10-28T14:35:31.702307Z",
    "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt", "derived_sha256":
    "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c", "line_start":
    8, "line_end": 8, "quote": "       FeSO4……………………………………….1.25                            mg
    or ( 1.25ml of mg/ml solution)"}, "decision": "correct", "rationale": "Primary
    FeSO4 is 1.25 mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative
    says 1.25 mL of mg/mL solution without a numeric strength; visual inspection confirms
    the omission. Do not supply 1 mg/mL or infer a final-volume-normalized rate.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25
    mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL
    of mg/mL solution without a numeric strength; visual inspection confirms the omission.
    Do not supply 1 mg/mL or infer a final-volume-normalized rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25
    mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL
    of mg/mL solution without a numeric strength; visual inspection confirms the omission.
    Do not supply 1 mg/mL or infer a final-volume-normalized rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary FeSO4 is 1.25
    mg (0.00125 g batch mass), not 1.25 g/L. The printed alternative says 1.25 mL
    of mg/mL solution without a numeric strength; visual inspection confirms the omission.
    Do not supply 1 mg/mL or infer a final-volume-normalized rate."}]}, {"quantity_id":
    "q10", "topic": "DI Water", "source": {"evidence_id": "atcc1368", "reference":
    "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx", "raw_path":
    "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 13–13", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 13, "line_end": 13, "quote": "       DI Water…………………………………….1.0                          L"},
    "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent addition,
    not 1 g/L. This ingredient volume is not an instruction to make the completed
    medium up to 1 L.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent
    addition, not 1 g/L. This ingredient volume is not an instruction to make the
    completed medium up to 1 L."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent
    addition, not 1 g/L. This ingredient volume is not an instruction to make the
    completed medium up to 1 L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Primary DI water is a 1.0 L solvent
    addition, not 1 g/L. This ingredient volume is not an instruction to make the
    completed medium up to 1 L."}]}, {"quantity_id": "q11", "topic": "Cysteine HCl",
    "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 12–12", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 12, "line_end": 12, "quote": "       Cysteine HCl (add after boiling)……………1.0             g"},
    "decision": "unresolved", "rationale": "The primary sheet gives this mass per
    stated batch, with 1 L of water as a separate ingredient. It does not instruct
    making up to a measured final volume. Preserve the batch mass and explicit form;
    the stored g/L denominator remains unresolved pending a documented basis. The
    primary specifies addition after boiling; it does not identify L/D stereochemistry
    or hydrochloride hydration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The primary specifies addition after boiling; it does not
    identify L/D stereochemistry or hydrochloride hydration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The primary specifies addition after boiling; it does not
    identify L/D stereochemistry or hydrochloride hydration."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unresolved", "rationale": "The primary sheet
    gives this mass per stated batch, with 1 L of water as a separate ingredient.
    It does not instruct making up to a measured final volume. Preserve the batch
    mass and explicit form; the stored g/L denominator remains unresolved pending
    a documented basis. The primary specifies addition after boiling; it does not
    identify L/D stereochemistry or hydrochloride hydration."}]}, {"quantity_id":
    "q12", "topic": "N2", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 14–15", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 14, "line_end": 15, "quote": "                Adjust final pH to
    7.2. Prepare medium, dispense under a constant flow of nitrogen,\n       stopper
    and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust
    pH to"}, "decision": "unresolved", "rationale": "The source describes a constant
    nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default
    placeholder, not a source-quantified dose. Preserve gas identity and put the supported
    stage in preparation; do not invent a gas concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml", "field_path":
    "ingredients[11].concentration", "stored_value": {"value": "variable", "unit":
    "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes a constant
    nitrogen flow during dispensing, with no flow rate or amount. VARIABLE is a schema-default
    placeholder, not a source-quantified dose. Preserve gas identity and put the supported
    stage in preparation; do not invent a gas concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes
    a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE
    is a schema-default placeholder, not a source-quantified dose. Preserve gas identity
    and put the supported stage in preparation; do not invent a gas concentration."},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "The source describes
    a constant nitrogen flow during dispensing, with no flow rate or amount. VARIABLE
    is a schema-default placeholder, not a source-quantified dose. Preserve gas identity
    and put the supported stage in preparation; do not invent a gas concentration."}]},
    {"quantity_id": "q13", "topic": "NaOH adjustment stub", "source": {"evidence_id":
    "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 15–16", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 15, "line_end": 16, "quote": "       stopper and autoclave 15 minutes.
    For preparation of solid media add 20g of agar, adjust pH to\n       7.5 with
    NaOH."}, "decision": "unresolved", "rationale": "M2701 alone contains an unquantified
    NaOH solution stub. The primary locates NaOH in the optional solid branch with
    pH 7.5; no dose or strength is supplied. Do not automatically insert this stub
    into the basal liquid medium or fill its composition from a namesake stock.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "unresolved", "rationale": "M2701 alone contains
    an unquantified NaOH solution stub. The primary locates NaOH in the optional solid
    branch with pH 7.5; no dose or strength is supplied. Do not automatically insert
    this stub into the basal liquid medium or fill its composition from a namesake
    stock."}]}, {"quantity_id": "q14", "topic": "Basal pH and preparation stages",
    "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 12–16", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 12, "line_end": 16, "quote": "       Cysteine HCl (add after boiling)……………1.0             g\n       DI
    Water…………………………………….1.0                          L\n                Adjust final
    pH to 7.2. Prepare medium, dispense under a constant flow of nitrogen,\n       stopper
    and autoclave 15 minutes. For preparation of solid media add 20g of agar, adjust
    pH to\n       7.5 with NaOH."}, "decision": "add", "rationale": "All three local
    records omit preparation_steps and pH. Preserve the primary basal pH and sequence,
    including cysteine after boiling, nitrogen during dispensing, stoppering and the
    stated autoclave duration. The sheet supplies no autoclave temperature, nitrogen
    flow rate, incubation temperature or growth duration; none may be invented.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}, {"path": "data/merge_yaml/merged/Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "All three local records omit preparation_steps and pH. Preserve the primary basal
    pH and sequence, including cysteine after boiling, nitrogen during dispensing,
    stoppering and the stated autoclave duration. The sheet supplies no autoclave
    temperature, nitrogen flow rate, incubation temperature or growth duration; none
    may be invented.", "missing": true}]}, {"quantity_id": "q15", "topic": "Optional
    solid-medium branch", "source": {"evidence_id": "atcc1368", "reference": "https://www.atcc.org/~/media/E4C9EF983C184615BD6DB87D147DE3AA.ashx",
    "raw_path": "REVIEW_WORK/batch070/source09/atcc1368.raw", "raw_sha256": "ff331fc6fc4949415d4e310f196f2e00b63d01b4143995f04d7681a5db9a18c0",
    "locator": "PDF page 1; derived text physical LF lines 15–16", "accessed_at":
    "2026-10-28T14:35:31.702307Z", "derived_path": "REVIEW_WORK/batch070/source09/atcc1368.txt",
    "derived_sha256": "ab0fc560333152c9daa14f9f17aa7fc6f2ac9a58f8a64e199df02407d2a5e62c",
    "line_start": 15, "line_end": 16, "quote": "       stopper and autoclave 15 minutes.
    For preparation of solid media add 20g of agar, adjust pH to\n       7.5 with
    NaOH."}, "decision": "evidence_only", "rationale": "The primary solid branch specifies
    an agar batch addition and a different pH adjustment. Keep it explicitly optional
    and separate from basal liquid identity; its final volume and NaOH amount remain
    unspecified. Do not silently add agar or the solid pH to the basal record.", "layer_assessments":
    []}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: 'All 51 current ingredient CHEBI slots (nine unique IDs) use active OLS
    objects and matching canonical labels. Calcium dihydrate, magnesium hexahydrate,
    KH2PO4, ammonium sulfate, cellulose and nitrogen identities agree with the named
    sources. FeSO4 is printed without a hydrate, so its present anhydrous-form term
    is compatible with the printed formula; no heptahydrate is inferred. Resazurin
    is not replaced by sodium resazurin from generic MIM aliases. CHEBI:131527 has
    formula HO4P.2K and mass 174.174, while the source explicitly names three waters;
    its related trihydrate synonym does not make that formula hydrated. Retain source-form
    detail and avoid anhydrous molarity. The 180 MIM rows include MAPPED and REJECTED
    aliases, plus linked-only hydrate records; these do not override chemical identity.
    Yeast extract, DI water and cysteine HCl lack primary IDs: yeast has a catalog
    candidate, but no unverified identifier is asserted; cysteine stereochemistry/hydration
    are unspecified.'
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete histories of all three records were read. They separately record
    imports, enrichment, gas/alkali defaults, identifier assignment, name normalization,
    legacy-field/link migration and canonical labels; M2701 also records solution
    migration/default naming. The generated target adds two merge events and omits
    the M2701-specific history. Current writers and packaged MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9
    are current observations, not recovered historical execution. Preserve all original
    histories and distinct source IDs during curation.
  target_ids:
  - CultureMech:009263
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
  - CultureMech:009263
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:009263
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009263-source-amount-units-and-concentration-basis-need-repair
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source amount units and concentration basis need repair
  description: All layers store resazurin 2 g/L, FeSO4 1.25 g/L and DI water 1 g/L.
    The exact primary instead supplies a volume addition, a milligram batch mass and
    a litre solvent addition. Other gram numerals match batch masses but an explicit
    final-volume denominator is absent. Attach exact source evidence and separate
    batch quantities from concentrations; unknown resazurin strength and the incomplete
    alternative iron-stock expression prevent mass-contribution reconstruction.
  target_ids:
  - CultureMech:009263
  field_paths:
  - ingredients[*].concentration
  - ingredients[*].evidence
  evidence_ids:
  - atcc1368
  - primary-image
  - togo2711
  - togo2701
  - quantities
  - writer-import
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-009263-preparation-and-optional-solid-branch-are-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and optional solid branch are omitted
  description: All three local records lack basal pH and preparation_steps despite
    explicit primary text. The second owner has an unquantified alkali stub associated
    by the source with an optional solid branch; copying it into the liquid record
    would lose that context. Preserve branch-specific pH, agar and adjustment roles
    while keeping unspecified dose, strength and temperatures unresolved.
  target_ids:
  - CultureMech:009263
  field_paths:
  - ph_value
  - preparation_steps
  - solutions
  - physical_state
  evidence_ids:
  - atcc1368
  - togo2711
  - togo2701
  - quantities
  - writer-solutions
  - writer-merge
  - writer-formulation
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-009263-phosphate-trihydrate-needs-explicit-form-preservation
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Phosphate trihydrate needs explicit form preservation
  description: The source and local ingredient name specify K2HPO4 x 3H2O, but CHEBI:131527
    has the anhydrous elemental formula and mass. Its current related synonym mentions
    trihydrate, so this is a form-granularity limitation rather than a canonical-label
    error. Preserve the specified hydrate in evidence and representation, and do not
    use the bare ontology mass for molar conversion. No unverified replacement term
    is proposed.
  target_ids:
  - CultureMech:009263
  field_paths:
  - ingredients[6].term
  - ingredients[6].mediaingredientmech_chebi_term
  - ingredients[6].preferred_term
  evidence_ids:
  - atcc1368
  - ols131527
  - grounding
  - mim-pool
  rule_id: source-hydrate-granularity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate both maintained owners using the exact primary batch amounts
    and source units. Preserve unspecified stock strengths and final volume as unresolved;
    do not infer densities or stock recipes. Attach claim-level source excerpts and
    any justified arithmetic, then regenerate compatible outputs.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Represent the supported basal preparation and optional solid branch
    separately through maintained records or explicit variant context. Reconcile the
    M2701 stub without inventing composition or promoting solid conditions into the
    liquid definition. Retain contributor identities and history before regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: The source and local ingredient name specify K2HPO4 x 3H2O, but CHEBI:131527
    has the anhydrous elemental formula and mass. Its current related synonym mentions
    trihydrate, so this is a form-granularity limitation rather than a canonical-label
    error. Preserve the specified hydrate in evidence and representation, and do not
    use the bare ontology mass for molar conversion. No unverified replacement term
    is proposed.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2711_Clostridium_Cellulolytic_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulolytic_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- 'Partial completion: exact primary and TOGO sources were fully read, but the primary
  leaves resazurin stock strength, numeric iron-stock strength and final-volume basis
  unresolved. Review coverage includes every stored concentration; no unsupported
  replacement rates are supplied.'
- The primary optional solid branch is kept separate from basal liquid identity. No
  autoclave temperature, gas flow rate, incubation condition, strain growth assertion,
  cysteine stereochemistry or unprinted salt hydrate is inferred.
- Collection identity was used only to establish ordinary environmental organism context.
  It does not attach a target-organism growth claim or replace the exact medium sheet.
- Current OLS and packaged MIM rows are current identity observations. Misleading/rejected
  aliases and ontology-linked hydrate variants are not endorsements or evidence of
  historical catalog membership. No ontology-linked literature was adopted.
- Three historical reports and current writer code were inspected as diagnostics and
  process context. They do not authenticate historical external source bytes or execution;
  all existing records and history remain unchanged.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
