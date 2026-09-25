# YAML Record Review: acidiferrobacter_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIFERROBACTER_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:56:47Z
- Finished UTC: 2026-09-21T08:58:12Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIFERROBACTER_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml`. It represents TOGO M898, whose original source is JCM Medium 861 / ACIDIFERROBACTER MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The TOGO identity maps back to the correct JCM source: TOGO M898 reports `original_media_id: JCM_M861` and the same JCM `GRMD=861` URL used by the direct `mediadive.medium:J861` import. The ignored-inclusive exact source-ID search found one normalized TOGO M898 record and one normalized JCM J861 record, but they currently generate as separate `acidiferrobacter_medium` records instead of one source-duplicate merge.

The JCM 861 source also cross-references other JCM media: 50 ml Modified UBS solution from JCM Medium 860 and 10 ml trace element solution from JCM Medium 748. TOGO preserves those as medium references using the corresponding TOGO IDs, but CultureMech keeps them only as ungrounded text in empty solution records.

## Evidence

- Primary JCM source `GRMD=861`: source page fetched from JCM during review. It lists 50 ml Modified UBS solution, 26.64 g MgSO4.7H2O, 1.0 g sulfur powder, and 885 ml distilled water; instructs the curator to mix without sulfur, adjust pH to 1.9 with H2SO4, autoclave, steam sulfur for three successive days, and then add sulfur plus 10 ml 1.0 M FeSO4, 5 ml 100 mM potassium tetrathionate, and 10 ml filter-sterilized trace element solution after cooling.
- TOGO source M898: API record fetched during review. It preserves the same `GRMD=861` provenance, basal component block, and post-cooling solution-addition block before CultureMech normalization moves every solution into empty `solutions`.
- Local ignored-inclusive exact source-ID search: exact `TOGO:M898` occurs in the TOGO normalized source and `ACIDIFERROBACTER_MEDIUM.yaml`; exact `mediadive.medium:J861` occurs in the direct JCM normalized source and `acidiferrobacter_medium__9d43544a.yaml`.

## Completeness

The generated target is missing the operational constraints that make JCM 861 interpretable. It has H2SO4 as a variable ingredient but no pH-1.9 adjustment text, no instruction that sulfur is excluded before autoclaving and steamed separately, and no instruction that sulfur plus FeSO4, potassium tetrathionate, and trace-element solution are added after cooling.

The target also retains four empty `solutions` with invalid concentration units. All four source rows are milliliter additions, but `Modified UBS solution`, `1.0 M FeSO4 solution`, `100 mM Potassium tetrathionate solution`, and `Trace element solution` are represented as `50`, `10`, `5`, and `10` `G_PER_L`, respectively.

## Findings

- CRITICAL: The source solution additions are represented with gram-per-liter units and empty compositions. JCM 861 calls for 50 ml, 10 ml, 5 ml, and 10 ml liquid additions; the generated record turns those volumes into 50, 10, 5, and 10 `G_PER_L`, which changes both unit semantics and dose.
- MAJOR: JCM 861 is split into two generated records. TOGO M898 and the direct JCM J861 source point at the same `GRMD=861` recipe, but they fingerprint separately because the TOGO path keeps cross-references as empty solution shells plus malformed water/H2SO4 rows while the direct JCM path flattened the referenced and molar solutions into top-level ingredients.
- MAJOR: The generated target drops the JCM pH and post-sterilization instructions. That loses pH 1.9, the separate sulfur steaming step, and the filter-sterilized post-cooling additions.
- MAJOR: `Distilled water 885 ml` is stored as `885 G_PER_L`. This is a partial-volume water row that exists to leave room for 75 ml of stock additions, not a mass concentration.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M898_Acidiferrobacter_Medium.yaml` to preserve the source hierarchy: basal MgSO4.7H2O, sulfur, 885 ml water, and 50 ml Modified UBS solution, followed by the three post-cooling solution additions of 10 ml FeSO4, 5 ml potassium tetrathionate, and 10 ml trace element solution.
- Convert all four solution additions from `G_PER_L` to an explicit volume unit and keep the JCM/TOGO medium references for Modified UBS and trace elements as structured `culturemech_term` or `media_term` links rather than bare text.
- Restore the preparation instructions from JCM/TOGO, including pH adjustment to 1.9 with H2SO4, separate sulfur sterilization, and filter-sterilized post-cooling additions.
- Normalize the direct `data/normalized_yaml/bacterial/acidiferrobacter_medium.yaml` representation to the same stock-preserving model and regenerate merged YAML so exact `TOGO:M898` and exact `mediadive.medium:J861` land in one generated record.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the corrected normalized sources and regenerated target.
- Re-run an ignored-inclusive exact search for `TOGO:M898`, `mediadive.medium:J861`, and `GRMD=861` to verify the TOGO and direct JCM sources now merge.
- Verify the regenerated target no longer has empty `solutions` or milliliter source rows expressed as `G_PER_L`.

## Additional Notes

The fetched JCM page labels the referenced Modified UBS source as JCM Medium 860 and the trace-element source as JCM Medium 748; the TOGO parse uses TOGO medium references M896 and M773 for those same cross-references.
