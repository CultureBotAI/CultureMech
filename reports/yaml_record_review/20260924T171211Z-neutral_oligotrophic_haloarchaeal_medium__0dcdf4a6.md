# YAML Record Review: neutral_oligotrophic_haloarchaeal_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml
- Started UTC: 2026-09-24T17:11:29Z
- Finished UTC: 2026-09-24T17:12:11Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml` as a generated `MediaRecipe` for TOGO M1219, `CultureMech:007747`, label `neutral_oligotrophic_haloarchaeal_medium`, category `archaea`, and physical state `SOLID_AGAR`.

The generated record was merged from `data/normalized_yaml/archaea/TOGO_M1219_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml`. It is derived; the maintained owner is the normalized TOGO M1219 YAML plus the shared source-family relationship to JCM 1138/M1218.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml --out /private/tmp/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__0dcdf4a6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The target denotes TOGO M1219, Neutral Oligotrophic Haloarchaeal Medium, original source `JCM_M1138-2`.
- The inspected TOGO M1219 API record supports a 20 g/L agar variant of Neutral Oligotrophic Haloarchaeal Medium built from 233 ml distilled water, 767 ml `MDS salt water`, NH4Cl, K2HPO4, sodium pyruvate, yeast extract, peptone, and agar.
- The live JCM GRMD 1138 page now returns `Nothing found`, so current JCM text was unavailable; MediaDive REST `J1138` and TOGO M1218 were inspected as corroborating provider records for the same liquid source family.
- A gitignore-independent hidden-file search for `TOGO:M1219`, `JCM_M1138-2`, `togomedium.org/medium/M1219`, and `M1219` across `data/normalized_yaml` and `data/merge_yaml` found this normalized M1219 owner and its generated merge, plus unrelated provider-local M1219 records from JCM and NBRC.
- A broader gitignore-independent hidden-file search for `J1138`, `GRMD=1138`, and `neutral_oligotrophic_haloarchaeal_medium` across `data/normalized_yaml` and `data/merge_yaml` found separate direct-JCM, TOGO M1218 liquid, and TOGO M1219 agar records for this source family.

## Evidence

The TOGO M1219 payload represents a single main solution with these rows: 233 ml distilled water, 0.25 g NH4Cl, 0.3 g K2HPO4, 1 g sodium pyruvate, 20 g/L agar, 0.05 g yeast extract, 0.25 g peptone, and 767 ml MDS salt water. Its comment instructs mixing thoroughly and adjusting the pH to 7.0; the agar row is the solid-medium addition described for the JCM 1138 recipe family.

The generated YAML preserves the small component masses and the agar row, but it moves `MDS salt water` to an empty `solutions` row with `767 G_PER_L` instead of a 767 ml addition and drops the pH 7.0 preparation instruction entirely.

## Completeness

- Consequential gap: MDS salt water is an empty `Unknown solution` at `767 G_PER_L`; the record does not resolve Medium M578 or preserve the 767 ml unit.
- Consequential gap: the pH 7.0 preparation instruction from TOGO M1219 is absent.
- Consequential gap: M1219 is not linked to the M1218 liquid parent or direct JCM `J1138` import in the generated record.
- Empty optional fields are not defects. The inspected TOGO payload does not provide a target organism or incubation temperature.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The MDS salt water addition has the wrong structure and unit. | TOGO M1219 lists 767 ml `MDS salt water (see Medium [M578])`; the generated record has an empty `Unknown solution` with `concentration.value: 767` and `unit: G_PER_L`. | Recurate `data/normalized_yaml/archaea/TOGO_M1219_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml` so Medium M578 is a 767 ml solution reference or is expanded with correct scaling. |
| major | Preparation is incomplete. | TOGO M1219 instructs mixing thoroughly and adjusting pH to 7.0; the generated record has no `preparation_steps` and no `ph_value`. | Add the pH 7.0 preparation to the normalized TOGO M1219 owner. |
| major | The agar variant is not explicitly linked to its liquid parent or direct JCM duplicate. | Exact hidden-file searches found separate M1219, M1218, and direct `J1138` normalized owners for the same JCM 1138 source family; the M1219 generated record has no parent/variant relationship. | Link `TOGO_M1219_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml` to TOGO M1218 as the 20 g/L agar variant while resolving the direct JCM duplicate. |

## Recommended Edits

1. Represent `MDS salt water` as a 767 ml addition from Medium M578, or expand it with the 0.767 dilution explicitly documented.
2. Add the source pH 7.0 preparation instruction to the M1219 normalized record.
3. Link M1219 as the agar variant of M1218 and reconcile both with the direct JCM `J1138` owner.
4. Regenerate the merged YAML after normalized curation and relationship fixes.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired normalized M1219 owner and regenerated merged YAML.
- Re-run a gitignore-independent hidden-file search for `TOGO:M1219`, `JCM_M1138-2`, `GRMD=1138`, and `MDS salt water` under `data/normalized_yaml` and `data/merge_yaml`.
- Manually compare the regenerated record against the TOGO M1219 API payload and retry live JCM GRMD 1138.

## Additional Notes

The live JCM GRMD 1138 URL returned `Nothing found` at review time, but the TOGO M1219 API payload remained available and was sufficient to verify the agar variant's base formulation and pH instruction.
