# YAML Record Review: EUGON AGAR WITH 5% SHEEP BLOOD AND ARTIFICIAL SEAWATER

- Repository: CultureMech
- Record: data/merge_yaml/merged/eugon_agar_with_5_sheep_blood_and_artificial_seawater.yaml
- Started UTC: 2026-09-23T00:45:10Z
- Finished UTC: 2026-09-23T00:47:22Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/eugon_agar_with_5_sheep_blood_and_artificial_seawater.yaml` is the generated direct JCM GRMD 1380 record. Its maintained owner is `data/normalized_yaml/bacterial/JCM_J1380_EUGON_AGAR_WITH_5_SHEEP_BLOOD_AND_ARTIFICIAL_SEAWATER.yaml`.

This generated file predates the 2026-09-07 owner repair that resolved the JCM Medium 736 artificial-seawater cross-reference.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/eugon_j1380.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `jcm.grmd:1380` media term, title, `SOLID_AGAR` physical state, and direct JCM URL all match JCM Medium 1380.

The generated record has no small-molecule salt rows because the artificial seawater is still an opaque cross-reference ingredient. `Eugon agar (BD-Difco)` and sheep blood are complex products and do not require CHEBI groundings.

The lower-case normalized owner was absent in an ignored-file-inclusive `find`; the only exact owner is the original direct-JCM import filename.

## Evidence

JCM 1380 lists:

- 45.4 g Eugon agar (BD-Difco).
- 50.0 ml sheep blood.
- 950.0 ml Artificial seawater from Medium 736.

The preparation mixes everything except sheep blood, autoclaves, cools to about 45 C, aseptically adds sterile defibrinated sheep blood to 5% final volume, then mixes and quickly dispenses into sterile petri dishes.

JCM 736 supplies the artificial-seawater subrecipe with NaCl, MgCl2 x 6 H2O, Na2SO4, CaCl2 x 2 H2O, KCl, NaHCO3, KBr, H3BO3, SrCl2 x 6 H2O, NaF, and 1 L distilled water.

## Completeness

The generated file has the right top-level Eugon agar, sheep blood, and artificial-seawater quantities. It is still incomplete as a standalone recipe because `Artificial seawater (see Medium No. 736 )` has no nested composition or structured source link to JCM 736.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to the cross-reference repair in the owner. | The owner gained a 2026-09-07 `repair_cross_reference_score25.py` event with an `Artificial seawater` solution populated from JCM 736; the generated 2026-08-06 merge still has only an opaque 950 ml top-level ingredient. | Regenerate `data/merge_yaml/merged/eugon_agar_with_5_sheep_blood_and_artificial_seawater.yaml` from the repaired owner. |
| Major | Artificial seawater is not reconstructible in the generated record. | JCM 1380 points to Medium 736 for the seawater recipe, and JCM 736 prints ten salts plus distilled water; the generated file only says `Artificial seawater (see Medium No. 736 )` at `950.0 ML_PER_L`. | Preserve an `Artificial seawater` nested solution with the JCM 736 salt composition. |
| Minor | The generated record lacks structured source references. | The repaired owner now lists both GRMD 1380 and GRMD 736 under `references`; the generated file has only a free-text JCM link in `notes` and no Medium 736 reference. | Regenerate after the owner repair so both source URLs are retained. |

## Recommended Edits

1. Regenerate the generated merge from `data/normalized_yaml/bacterial/JCM_J1380_EUGON_AGAR_WITH_5_SHEEP_BLOOD_AND_ARTIFICIAL_SEAWATER.yaml`.
2. Confirm `Eugon agar (BD-Difco)` and `Sheep blood` remain top-level ingredients at 45.4 g/l and 50 ml/l.
3. Confirm the 950 ml/l `Artificial seawater` solution contains the full JCM 736 salt composition plus distilled water.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merge.
- Confirm the regenerated record has structured references for both JCM 1380 and JCM 736.
- Confirm no top-level ingredient still contains the literal text `see Medium No. 736`.

## Additional Notes

The MediaDive REST endpoint for `J1380` returned `DataNotFound`; this review used the live JCM 1380 and JCM 736 pages.
