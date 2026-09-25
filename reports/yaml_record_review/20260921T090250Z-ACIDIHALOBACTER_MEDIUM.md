# YAML Record Review: acidihalobacter_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIHALOBACTER_MEDIUM.yaml`
- Started UTC: 2026-09-21T09:00:42Z
- Finished UTC: 2026-09-21T09:02:50Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIHALOBACTER_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M1281_Acidihalobacter_Medium.yaml`. It represents TOGO M1281, whose original source is JCM Medium 1196 / ACIDIHALOBACTER MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The TOGO and direct JCM imports are source duplicates. TOGO M1281 reports `original_media_id: JCM_M1196` and the same `GRMD=1196` URL used by the direct `mediadive.medium:J1196` source, but they currently generate separately as `ACIDIHALOBACTER_MEDIUM.yaml` and `acidihalobacter_medium__2a7ca782.yaml`.

KOMODO Medium 1321 has the same ACIDIHALOBACTER name and related chemistry, but it is a separate KOMODO/DSMZ-derived import that is already linked to the strain-specific `for_dsm_14174` variant. It should be reviewed and corrected through that source family rather than forced into the JCM 1196 TOGO singleton by name alone.

## Evidence

- Primary JCM source `GRMD=1196`: source page fetched from JCM during review. It defines Solution A with salts in 900 ml water and pH 1.7 H2SO4 adjustment; Solution B with 13.9 g FeSO4.7H2O in 100 ml water at pH 1.25; Solution C with 0.3 g K2S4O6 in 10 ml water; Solution D with 0.1 g yeast extract in 10 ml water; and a final instruction to aseptically combine A and B after cooling, then add C and D.
- TOGO source M1281: API record fetched during review. It preserves the four JCM solution blocks and the pH/sterilization comments before CultureMech normalization collapses those subcomponents.
- Local ignored-inclusive exact source-ID search: exact `TOGO:M1281` occurs in the TOGO normalized source and this generated target; exact `mediadive.medium:J1196` occurs in the direct JCM normalized source and the separate `acidihalobacter_medium__2a7ca782.yaml` generated merge.

## Completeness

The generated target preserves most solution formula rows as recognizable top-level ingredients, but it has no `preparation_steps`, no `ph_value`, and no usable Solution A/B/C/D composition. The four source water volumes are summed into one `1020.0 G_PER_L` water row, and the four solution additions are kept only as empty mediadive solution references with source milliliter volumes stored as `G_PER_L`.

Without the JCM solution boundaries, a consumer cannot determine that Solution A and Solution B require separate pH adjustment and heat sterilization, Solution C is filter-sterilized, Solution D is autoclaved, and the solutions are combined only after cooling.

## Findings

- CRITICAL: JCM Solution A/B/C/D boundaries were flattened. The target has NaCl, ammonium sulfate, MgSO4.7H2O, K2HPO4, FeSO4.7H2O, K2S4O6, and yeast extract as final top-level ingredients, while the four `solutions` are empty shells.
- MAJOR: The four source solution volumes are represented as mass concentrations. Solution A, B, C, and D should be 900 ml, 100 ml, 10 ml, and 10 ml portions, not `900`, `100`, `10`, and `10` `G_PER_L`.
- MAJOR: TOGO M1281 and the direct JCM J1196 import point at the same `GRMD=1196` recipe but are split into two generated records because their solution modeling differs.
- MAJOR: All preparation instructions are missing from the generated target: pH 1.7 for Solution A, pH 1.25 and 115C/10 min autoclaving or filter sterilization for Solution B, filtration for Solution C, autoclaving for Solution D, and the cooled aseptic combination order.
- MAJOR: Four separate water rows were summed into `Distilled water 1020.0 G_PER_L`. The 900/100/10/10 ml rows belong to different solution compositions and should not be represented as one final mass concentration.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M1281_Acidihalobacter_Medium.yaml` so Solutions A, B, C, and D remain structured solution components with 900, 100, 10, and 10 ml final volumes.
- Move the corresponding salts, FeSO4.7H2O, K2S4O6, yeast extract, and water rows into their source solution compositions instead of keeping them as one flattened ingredient list.
- Restore all JCM/TOGO preparation comments as ordered `preparation_steps`, preserving the per-solution pH and sterilization instructions plus the final cooled combination order.
- Normalize the direct `data/normalized_yaml/bacterial/acidihalobacter_medium.yaml` JCM source to the same four-solution representation and regenerate so exact `TOGO:M1281` and exact `mediadive.medium:J1196` merge into one generated JCM 1196 record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the corrected TOGO M1281 and JCM J1196 normalized records and on the regenerated target.
- Re-run an ignored-inclusive exact search for `TOGO:M1281`, `mediadive.medium:J1196`, and `GRMD=1196` to verify no JCM 1196 split remains.
- Confirm the KOMODO 1321 / `for_dsm_14174` source family is still separate and keeps its `STRAIN_SPECIFIC_VARIANT` relationship.

## Additional Notes

The direct JCM and KOMODO records already show the hazard of losing solution boundaries: they carry the FeSO4 and tetrathionate stock concentrations as final rows. The TOGO generated target does not inflate those two rows as far, but it still lacks enough structure to reconstruct JCM 1196 faithfully.
