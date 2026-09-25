# YAML Record Review: PYGV Marine Medium (B)

- Repository: CultureMech
- Record: data/merge_yaml/merged/pygv_marine_medium_b.yaml
- Started UTC: 2026-09-24T23:12:07Z
- Finished UTC: 2026-09-24T23:13:31Z
- Verdict: needs curation

## Target

- Generated file: data/merge_yaml/merged/pygv_marine_medium_b.yaml
- Stable ID: CultureMech:007648
- Maintained owner: data/normalized_yaml/bacterial/TOGO_M1127_PYGV_Marine_Medium_B.yaml
- Merge sources: TOGO_M1127_PYGV_Marine_Medium_B
- Merge fingerprint: 551ee5a6094e50e093f5b2ad11fb998ba1d15c9e40ca332a5db623a574c9498d
- Source grounding: TOGO M1127 / JCM Medium 1059 PYGV Marine Medium (B), solid formulation

## Validation

| Check | Result |
| --- | --- |
| LinkML open schema | Passed; exited 0 with no diagnostics. |
| Strict schema | Passed with 0 errors. `/private/tmp/pygv_marine_medium_b.strict.tsv` contains only the header line. |
| Reference validation | Passed 1 file with 0 reference checks. |
| Term validation | Passed after the known `eutils` / `pkg_resources` warning. |
| Embedded history validation | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated record is the TOGO M1127 solid-agar branch for JCM Medium 1059, not the parallel TOGO M1126 liquid branch. Its maintained owner, `data/normalized_yaml/bacterial/TOGO_M1127_PYGV_Marine_Medium_B.yaml`, has already been repaired with a 2026-09-11 `RESOLVED_TOGO_M1127_SCORE15` curation entry.

Exact TOGO M1127 lists 0.25 g/L Bacto peptone, 0.25 g/L Yeast extract, 20 ml/L Mineral salt solution from M299/JCM 304, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution from M299/JCM 304, 250 ml/L Artificial seawater from M299/JCM 304, 710 ml/L Distilled water, and 15 g/L Agar for solid medium. The repaired owner carries those main components, pH 7.2-7.4, nested Mineral salt solution, 2.5% Glucose solution, Vitamin solution, and Artificial seawater, and source preparation steps.

An exact ignored-file search for `TOGO:M1126`, `gm_id=M1126`, `GRMD=1059`, `J1059`, `mediadive.medium:J1059`, and `pygv_marine_medium_b` under `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` found the repaired M1126 and M1127 owners plus three generated PYGV Marine Medium B branches.

## Evidence

- `data/merge_yaml/merged/pygv_marine_medium_b.yaml` has no `repair_togo_m1127_score15.py` curation history entry.
- The generated file still has `composition_type: UNDEFINED`, no pH range, and no source preparation steps.
- The generated file stores 710 ml Distilled water as `710 G_PER_L`.
- The generated file keeps 2.5% Glucose solution, Mineral salt solution, Vitamin solution, and Artificial seawater as empty `solutions` rows with concentrations of 10, 20, 10, and 250 `G_PER_L`.
- The repaired owner stores the four solution aliquots in `ML_PER_L`, expands their source compositions where needed, stores Distilled water as 710 `ML_PER_L`, keeps Agar at 15 g/L, and restores six preparation steps.

## Completeness

The maintained owner is already substantially complete for the solid TOGO M1127 / JCM 1059 formulation. The generated record is incomplete because it has not been regenerated after that repair, so downstream consumers still see the older empty-solution representation.

## Findings

- Major: the generated YAML is stale; it still contains pre-repair empty solution placeholders, wrong `G_PER_L` units for volume aliquots, missing pH 7.2-7.4, and no nested JCM 304-derived solution content.
- Major: the generated artifact omits the September 2026 repaired preparation sequence for boiling, autoclaving, cooling, aseptic glucose/vitamin addition, and pH adjustment.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/pygv_marine_medium_b.yaml` from `data/normalized_yaml/bacterial/TOGO_M1127_PYGV_Marine_Medium_B.yaml`.
2. Verify that the regenerated M1127 output keeps physical state `SOLID_AGAR`, Agar 15 g/L, pH 7.2-7.4, 710 ml/L water, and `ML_PER_L` units for the four source solution aliquots.
3. Re-run merge generation and confirm the repaired M1127 branch is distinct from the liquid M1126 branch only by the expected solid-agar addition.

## Follow-up Checks

- Re-run open, strict, reference, and term validators on regenerated `pygv_marine_medium_b` output.
- Compare the regenerated M1127 branch against TOGO M1127, JCM Medium 1059, TOGO M299, JCM Medium 304, and JCM Medium 149.
- Repeat the exact ignored-file search for `TOGO:M1127`, `gm_id=M1127`, `GRMD=1059`, and `pygv_marine_medium_b` to confirm stale generated output is gone.

## Additional Notes

None.
