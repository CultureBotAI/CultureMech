# YAML Record Review: medium_a_for_alkaliphiles
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_a_for_alkaliphiles.yaml`
- Started UTC: 2026-09-24T01:20:21Z
- Finished UTC: 2026-09-24T01:21:13Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:009659` / `medium_a_for_alkaliphiles`.
- Current generated record has source term `TOGO:M321`, TOGO/JCM source notes, `SOLID_AGAR`, and 9 ingredient rows.
- Exact source-ID and owner checks included ignored files. The exact `TOGO:M321` scan found only `data/normalized_yaml/bacterial/TOGO_M321_Medium_A_For_Alkaliphiles.yaml`, this generated record, and normalized index entries.
- A second exact scan found a separate JCM owner, `data/normalized_yaml/bacterial/medium_a_for_alkaliphiles.yaml`, with source term `mediadive.medium:J326`, plus a separate generated output at `data/merge_yaml/merged/medium_a_for_alkaliphiles__4520f84a.yaml`.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- TOGO M321 identifies the original source as JCM M326 and points to the JCM formula page.
- The separate `mediadive.medium:J326` normalized owner is the same named JCM formula, `MEDIUM ''A'' FOR ALKALIPHILES`, with the same non-water ingredient amounts.
- The generated TOGO record did not merge with the parallel JCM owner, apparently because the TOGO import retained `Distilled water` as a concentration row while the JCM import omitted water and captured pH 9.6.
- The TOGO owner has a primary CHEBI term for `MgSO4 x 7 H2O` but no matching `mediaingredientmech_chebi_term`, while the JCM owner already has both.

## Evidence
- Live TOGO M321 and live JCM M326 both give this formula: Glucose 10 g, Bacto peptone 5 g, Yeast extract 5 g, KH2PO4 1 g, MgSO4 x 7 H2O 0.2 g, NaCl 40 g, Na2CO3 10 g, Agar 15 g, and Distilled water 1 L.
- The live JCM page instructs adjustment to pH 9.6 if necessary, and the live TOGO M321 metadata also records pH 9.6.
- The generated TOGO record represents the 1 L distilled-water row as value `1` with unit `G_PER_L`.
- The generated TOGO record has no `ph_value` or preparation step, whereas the parallel JCM owner has `ph_value: 9.6` and an `ADJUST_PH` preparation step.

## Completeness
- The generated record keeps all 9 TOGO owner ingredient rows and preserves the TOGO M321 source term and the original JCM M326 URL.
- The generated record has agar state, broad applications, source notes, CHEBI grounding for the chemically specific rows except the MgSO4 x 7 H2O secondary link, merge provenance, and curation history.
- The generated record is missing the pH 9.6 assertion available in both live sources and in the parallel JCM owner.

## Findings
- The TOGO water row is mis-modeled. `Distilled water` was imported from `1 L` as `1 G_PER_L`, which is neither the correct volume nor a useful final-medium concentration.
- The generated TOGO record lost the source pH 9.6 and the pH-adjustment instruction.
- The same JCM formula exists in two unmerged normalized and generated records: the TOGO M321 path and the `mediadive.medium:J326` path.
- The TOGO MgSO4 x 7 H2O row is only partially regrounded. Its primary term is `CHEBI:31795`, but it is missing the matching CHEBI-keyed MediaIngredientMech secondary link present on the other chemically grounded rows.

## Recommended Edits
- Remove the `Distilled water` concentration row from `data/normalized_yaml/bacterial/TOGO_M321_Medium_A_For_Alkaliphiles.yaml` or represent it with a volume-preserving water field if the schema supports one.
- Backfill pH 9.6 and the adjustment step from TOGO/JCM evidence into the TOGO owner.
- Refresh the `MgSO4 x 7 H2O` secondary CHEBI link after the heptahydrate primary-term repair.
- De-duplicate TOGO `M321` and JCM `J326` so the same source formula does not produce separate generated records.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on any regenerated merged record.
- Repeat exact TOGO M321 and JCM J326 source-ID scans with ignored files included after de-duplication.
- Compare the regenerated output against live JCM M326 to verify pH, water handling, and all non-water ingredient amounts.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
