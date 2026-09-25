# YAML Record Review: MRS medium (containing erythromycin)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml
- Started UTC: 2026-09-24T14:53:06Z
- Finished UTC: 2026-09-24T14:54:29Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:009064` / `mrs_medium_containing_erythromycin` at `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_containing_erythromycin.yaml`
- Merge source: `mrs_medium_containing_erythromycin`
- Merge fingerprint: `51f00c669824875eb32f8ee23d8dca1a24f02ff6f10848dc562ff7106a268a3d`
- Category: `bacterial`
- Medium term: `TOGO:M2490`, label `MRS medium (containing erythromycin)`

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml --out /private/tmp/mrs_medium_containing_erythromycin.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies TOGO M2490, `MRS medium (containing erythromycin)`. The generated medium term agrees with the inspected TOGO API response, which reports `gm` `http://togomedium.org/medium/M2490`, the same name, and no secondary `src_url`.

The ingredients are the right two source rows but both generated units are stale:

| TOGO row | Generated row | Current maintained row |
|---|---|---|
| erythromycin, 5 ug/ml | 5 `G_PER_L` | 5 `MG_PER_L` |
| MRS medium (Difco), 1 L | 1 `G_PER_L` | 1000 `ML_PER_L` |

The exact `CultureMech:009064` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only.

## Evidence

TOGO M2490 lists erythromycin at 5 ug/ml and 1 L of MRS medium (Difco). Its free-text comment states that the source cultures used MRS medium from Difco containing erythromycin and were incubated 24 h at 37 C.

The maintained normalized file was repaired on 2026-09-10 and now stores erythromycin as the equivalent 5 mg/L, stores the MRS medium base as 1000 ml/L, adds `temperature_value: 37.0`, records two preparation steps, and carries `data_quality_flags` plus a TOGO M2490 reference. The generated file was last merged on 2026-08-06, so none of those corrections are present in `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml`.

## Completeness

The generated record is incomplete because it has the pre-repair ingredient units and lacks the current normalized temperature, preparation, source, curation-history, quality-flag, role, and reference fields.

No target-organism or growth-metric block is present. The TOGO comment mentions an experiment using Lb. casei BL23, but this TOGO recipe record does not itself provide the strain identifiers or full publication context needed to add a narrow growth-evidence block from the inspected TOGO JSON alone.

## Findings

### Major

1. The generated record is stale relative to its repaired maintained source.
   - Evidence: `data/normalized_yaml/bacterial/mrs_medium_containing_erythromycin.yaml` has a 2026-09-10 repair event that corrected TOGO M2490; the generated merge still ends at the 2026-08-06 merge event.
   - Impact: generated consumers still see the old 5 g/L erythromycin row, old 1 g/L MRS medium product row, and no 37 C condition or preparation steps.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml` from `data/normalized_yaml/bacterial/mrs_medium_containing_erythromycin.yaml`.

2. The erythromycin concentration in the generated record is 1000-fold too high.
   - Evidence: TOGO M2490 reports erythromycin at 5 ug/ml, equivalent to 5 mg/L; the generated record has 5 `G_PER_L`.
   - Impact: until the merge is regenerated, the emitted antimicrobial concentration is incorrect.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml` from the already repaired normalized source.

3. The MRS medium base volume is represented as a mass concentration.
   - Evidence: TOGO M2490 reports 1 L MRS medium (Difco), and the normalized source now stores that as 1000 `ML_PER_L`; the generated record still has 1 `G_PER_L`.
   - Impact: the generated recipe makes the opaque MRS base dimensionally wrong.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml` from the already repaired normalized source.

### Minor

None found.

### Blocker

None found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml` so it picks up the 2026-09-10 normalized TOGO M2490 repair.
2. Confirm the regenerated record has 5 `MG_PER_L` erythromycin, 1000 `ML_PER_L` MRS medium (Difco), `temperature_value: 37.0`, the two TOGO-derived preparation steps, the `INHIBITOR` erythromycin role, and the TOGO M2490 reference.

## Follow-up Checks

After regeneration, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_containing_erythromycin.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun the merge freshness check that owns `data/merge_yaml/merged/` to prove the generated record no longer predates its normalized source.

## Additional Notes

None found.
