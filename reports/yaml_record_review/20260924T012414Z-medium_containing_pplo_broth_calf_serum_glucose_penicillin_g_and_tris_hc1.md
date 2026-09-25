# YAML Record Review: medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1.yaml`
- Started UTC: 2026-09-24T01:23:39Z
- Finished UTC: 2026-09-24T01:24:14Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:008829` / `medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1`.
- Current generated record has source term `TOGO:M2240`, a stale `kg_microbe_match: mediadive.medium:21`, `LIQUID`, and 5 ingredient rows.
- Exact source-ID and owner checks included ignored files. `find data/normalized_yaml -name 'medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1*.yaml' -print` found only `data/normalized_yaml/bacterial/medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1.yaml`; the exact `TOGO:M2240` scan found only that owner, the generated record, and normalized index entries.
- The generated record is stale relative to the normalized owner, which has a 2026-09-12 `RESOLVED_TOGO_M2240_SCORE15` repair that fixed percent units, added pH 7.6, grounded Penicillin G, and removed the wrong MediaDive 21 match.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The normalized owner is the only exact owner for `TOGO:M2240` under `data/normalized_yaml`.
- The generated `media_term` preserves TOGO identifier `TOGO:M2240` and the long source label for the Mycoplasma capricolum ATCC 27343 medium.
- The generated record's `mediadive.medium:21` KG-Microbe match is wrong. Live MediaDive 21 is DSMZ `SARCINA MEDIUM`, pH 6.0, with glucose, peptone, yeast extract, and water, not PPLO broth, calf serum, penicillin G, and 50 mM Tris-HC1.

## Evidence
- Live TOGO M2240 lists 2.2% w/v PPLO broth from Difco, 1% v/v calf serum from Gibco, 0.2% w/v glucose, 400 units(U)/ml Penicillin G, and 50 mM Tris-HC1 at pH 7.6.
- Live TOGO M2240 metadata also records pH 7.6.
- The current normalized owner now preserves 0.2% w/v Glucose, 1.0% v/v Calf serum, 2.2% w/v PPLO broth, variable Penicillin G with a note for 400 units(U)/ml, and 50.0 mM Tris-HC1.
- The generated artifact still emits Glucose 0.2 g/L, Calf serum 1 g/L, PPLO broth 2.2 g/L, ungrounded variable Penicillin G, no pH value, and the stale MediaDive 21 match.

## Completeness
- The generated record keeps all 5 normalized owner ingredient names, but its unit handling is stale for three of them and its pH and reference data are stale.
- The generated record has liquid state, broad applications, source notes, the TOGO source term, merge provenance, and curation history.
- The generated record is missing the live TOGO pH 7.6 assertion and the normalized owner's explicit `references` entry.

## Findings
- Generated output was not regenerated after the September 2026 normalized-owner repair, so it still has wrong units for all percent-based ingredients.
- Glucose 0.2% w/v was converted to 0.2 g/L instead of being preserved as percent w/v or converted to 2 g/L.
- PPLO broth 2.2% w/v was converted to 2.2 g/L instead of being preserved as percent w/v or converted to 22 g/L.
- Calf serum 1% v/v was converted to 1 g/L even though the source amount is volume/volume.
- The generated record lost pH 7.6 and still carries the wrong `kg_microbe_match: mediadive.medium:21`.

## Recommended Edits
- Regenerate `data/merge_yaml/merged/medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1.yaml` from the repaired normalized owner.
- Preserve the percent w/v, percent v/v, activity-unit, and millimolar distinctions in the generated output.
- Keep the Penicillin G CHEBI grounding added in the normalized owner and keep the MediaDive 21 match removed.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on the regenerated merged record.
- Repeat exact owner and source-ID scans with ignored files included after regeneration.
- Compare the final generated record against live TOGO M2240 and verify that no MediaDive 21 relationship remains.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
