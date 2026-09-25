# YAML Record Review: medium_a_for_alkaliphiles__4520f84a
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_a_for_alkaliphiles__4520f84a.yaml`
- Started UTC: 2026-09-24T01:21:44Z
- Finished UTC: 2026-09-24T01:22:01Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:002684` / `medium_a_for_alkaliphiles`.
- Current generated record has source term `mediadive.medium:J326`, JCM source notes, pH 9.6, `SOLID_AGAR`, and 8 ingredient rows.
- Exact source-ID and owner checks included ignored files. The exact `mediadive.medium:J326` scan found only `data/normalized_yaml/bacterial/medium_a_for_alkaliphiles.yaml`, this generated record, and normalized index entries.
- A second exact scan found the duplicate TOGO `M321` owner at `data/normalized_yaml/bacterial/TOGO_M321_Medium_A_For_Alkaliphiles.yaml` plus a separate generated output at `data/merge_yaml/merged/medium_a_for_alkaliphiles.yaml`.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The normalized owner is the only exact owner for `mediadive.medium:J326` under `data/normalized_yaml`.
- JCM M326 is the original source behind TOGO M321, and both sources identify the same `MEDIUM ''A'' FOR ALKALIPHILES` recipe.
- Unlike the TOGO owner, this JCM owner already omits the 1 L water row and preserves pH 9.6 with an `ADJUST_PH` preparation step.
- All six chemically specific ingredient rows have primary CHEBI terms and matching CHEBI-keyed MediaIngredientMech secondary links.

## Evidence
- The live JCM M326 page gives this formula: Glucose 10 g, Bacto peptone 5 g, Yeast extract 5 g, KH2PO4 1 g, MgSO4 x 7 H2O 0.2 g, NaCl 40 g, Na2CO3 10 g, Agar 15 g, and Distilled water 1 L.
- The live JCM page instructs adjustment to pH 9.6 if necessary.
- Live TOGO M321 mirrors the same non-water formula and names JCM M326 as the original source.
- The generated JCM record matches the source non-water ingredient amounts and pH.

## Completeness
- The generated record keeps all 8 normalized owner ingredient rows.
- The generated record has pH, agar state, a pH-adjustment preparation step, broad applications, source notes, the JCM source term, CHEBI grounding for all chemically specific rows, merge provenance, and curation history.
- The generated record omits the source water row, which is appropriate because the formula is prepared to a final 1 L volume.

## Findings
- This JCM-generated record is a duplicate of the TOGO M321 generated record for the same original JCM M326 formula, but the two records were not merged because the TOGO owner retained a mis-modeled `Distilled water` concentration row and lost pH 9.6.

## Recommended Edits
- De-duplicate the JCM `J326` and TOGO `M321` owners after repairing the TOGO water and pH fields.
- Prefer this JCM owner's non-water ingredient list, pH value, and pH-adjustment preparation step when normalizing the duplicate TOGO source.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on the canonical generated record after de-duplication.
- Repeat exact TOGO M321 and JCM J326 source-ID scans with ignored files included after de-duplication.
- Compare the final canonical record against live JCM M326 to verify pH, water handling, and all non-water ingredient amounts.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
