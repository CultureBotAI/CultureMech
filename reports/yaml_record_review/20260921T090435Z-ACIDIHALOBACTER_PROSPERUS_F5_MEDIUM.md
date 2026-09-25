# YAML Record Review: acidihalobacter_prosperus_f5_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIHALOBACTER_PROSPERUS_F5_MEDIUM.yaml`
- Started UTC: 2026-09-21T09:02:50Z
- Finished UTC: 2026-09-21T09:04:35Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIHALOBACTER_PROSPERUS_F5_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M1282_Acidihalobacter_Prosperus_F5_Medium.yaml`. It represents TOGO M1282, whose original source is JCM Medium 1197 / ACIDIHALOBACTER PROSPERUS F5 MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The TOGO and direct JCM imports are source duplicates. TOGO M1282 reports `original_media_id: JCM_M1197` and the same `GRMD=1197` URL used by the direct `mediadive.medium:J1197` source, but they currently generate separately as `ACIDIHALOBACTER_PROSPERUS_F5_MEDIUM.yaml` and `acidihalobacter_prosperus_f5_medium__0fa15dd8.yaml`.

The 1 ml trace element row is source-grounded as a cross-reference to JCM Medium 1182 / TOGO Medium M1267. It should remain a stock-solution reference, not be flattened into the JCM 1197 final ingredient list.

## Evidence

- Primary JCM source `GRMD=1197`: source page fetched from JCM during review. It defines Solution A with NaCl, ammonium sulfate, MgSO4.7H2O, and K2HPO4 in 900 ml water at pH 2.5; Solution B with FeSO4.7H2O and K2S4O6 in 100 ml water at pH 2.5; and a final 1 ml autoclaved trace element solution addition from JCM Medium 1182.
- TOGO source M1282: API record fetched during review. It preserves the two internal solution blocks, the 1 ml trace-solution cross-reference, and the pH/filter/autoclave comments before CultureMech normalization collapses those blocks.
- Local ignored-inclusive exact source-ID search: exact `TOGO:M1282` occurs in the TOGO normalized source and this generated target; exact `mediadive.medium:J1197` occurs in the direct JCM normalized source and the separate direct-JCM generated merge.

## Completeness

The generated target preserves the visible A/B formula components as top-level ingredients and keeps a trace-solution placeholder, but it is incomplete as a preparation recipe. It has no `ph_value`, no `preparation_steps`, no structured Solution A/B compositions, and no structured link from the trace element addition to the corresponding Medium 1182 recipe.

Solution B's source constraint is especially important: JCM says it is adjusted to pH 2.5, filter-sterilized, and prepared just prior to use. That instruction is entirely absent from the generated record.

## Findings

- CRITICAL: JCM Solution A and Solution B boundaries were flattened. The target moves the salts, FeSO4.7H2O, K2S4O6, and both water rows into one top-level ingredient list, while `Solution A` and `Solution B` survive only as empty solution references.
- MAJOR: TOGO M1282 and the direct JCM J1197 import point at the same `GRMD=1197` recipe but are split into two generated records because their solution modeling differs.
- MAJOR: The source solution volumes are represented with mass-concentration units. Solution A, Solution B, and trace element solution should be 900 ml, 100 ml, and 1 ml additions, not 900, 100, and 1 `G_PER_L`.
- MAJOR: The preparation and condition text is missing. The generated record loses pH 2.5 for both Solution A and Solution B, the Solution B filter-sterilization and freshness requirement, and the final aseptic combination of freshly prepared B into A followed by trace elements.
- MAJOR: The Solution A and B water rows were summed into `Distilled water 1000.0 G_PER_L`; the source rows belong to different solution compositions and are volumes, not a final water concentration.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M1282_Acidihalobacter_Prosperus_F5_Medium.yaml` so Solution A, Solution B, and the 1 ml trace element solution remain structured `solutions` with volume additions.
- Move the Solution A salts plus 900 ml water into Solution A composition and the FeSO4.7H2O / K2S4O6 / 100 ml water rows into Solution B composition.
- Restore the JCM/TOGO preparation comments as ordered `preparation_steps`, including pH 2.5 for both internal solutions, freshly prepared filter-sterilized Solution B, and the final aseptic combination step.
- Normalize the direct `data/normalized_yaml/bacterial/acidihalobacter_prosperus_f5_medium.yaml` JCM source to the same solution-preserving representation and regenerate so exact `TOGO:M1282` and exact `mediadive.medium:J1197` merge into one generated JCM 1197 record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the corrected TOGO M1282 and JCM J1197 normalized records and on the regenerated target.
- Re-run an ignored-inclusive exact search for `TOGO:M1282`, `mediadive.medium:J1197`, and `GRMD=1197` to verify no JCM 1197 split remains.
- Verify the regenerated target has no empty `Solution A`, `Solution B`, or trace element solution entries.

## Additional Notes

The direct JCM generated record is not safer than the TOGO singleton: it flattened Solution B and the Medium 1182 trace elements into full-strength final ingredients.
