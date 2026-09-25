# YAML Record Review: Halarchaeum Neutrophilum Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/halarchaeum_neutrophilum_medium__daff5c52.yaml
- Started UTC: 2026-09-23T08:51:55Z
- Finished UTC: 2026-09-23T08:52:29Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for solid `Halarchaeum Neutrophilum Medium`.
- Stable ID: `CultureMech:010282`.
- Primary source in generated record: Togo `TOGO:M865`, original source `JCM_M829-2`.
- Merge fingerprint: `daff5c521f33d6afaf93e3937d4027175973f94173b47e56f27bf665d9af842a`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass, 0 error rows in `/private/tmp/halarchaeum_neutrophilum_medium_daff5c52.strict.tsv`.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the Togo solid-agar child for JCM medium 829, with Togo term `TOGO:M865` and original identifier `JCM_M829-2`.
- An exact `rg --no-ignore --hidden` search for `JCM_M829`, `GRMD=829`, and `mediadive.medium:J829` found the direct JCM/MediaDive `J829` record, Togo `M864` / `JCM_M829`, and this Togo `M865` / `JCM_M829-2` solid child in `data/merge_yaml` and `data/normalized_yaml`.
- The live JCM `GRMD=829` endpoint currently returns `Nothing found`; the surviving Togo API records and MediaDive `J829` were used for cross-checking.

## Evidence

- The Togo `M865` API record carries the same salts, glucose, 2 g BD-Difco complex nutrients, KOH pH adjustment, and 20 g/L agar as its solidification-specific row.
- Togo `M865` does not carry a `ph` value in its metadata, but Togo `M864` and MediaDive `J829` both report pH 5.5 for the same JCM 829 recipe.
- The direct MediaDive `J829` record keeps the pH-adjustment instruction and the solid-medium note, while this Togo-derived generated record promotes water and KOH to top-level ingredients and omits preparation steps entirely.

## Completeness

- The solidifying 20 g/L agar row is present and grounded.
- pH 5.5 is missing.
- The pH-adjustment and solid-medium preparation notes are missing.
- `Distilled water` is present as `1 G_PER_L` instead of as the solvent basis for a 1 L recipe.
- KOH is a variable top-level ingredient rather than a pH-adjustment reagent.

## Findings

- Major: pH 5.5 and the JCM/Togo preparation steps are absent.
- Major: 1 L distilled water is imported as a `1 G_PER_L` ingredient.
- Major: KOH from the pH adjustment is imported as a variable medium ingredient.
- Minor: This solid-agar child is split from the direct JCM/MediaDive record's existing 20 g/L agar note.
- Minor: The BD-Difco complex ingredients are ungrounded.

## Recommended Edits

- Restore pH 5.5 and the two preparation steps from the source-equivalent JCM/Togo liquid record.
- Remove top-level `Distilled water` and KOH from the formula, preserving KOH only in the pH-adjustment preparation step.
- Decide whether `TOGO:M865` should remain a separate solid-agar variant, become a `SOLIDIFICATION_VARIANT` child, or collapse into the direct JCM/MediaDive record's existing agar note.

## Follow-up Checks

- After repair, verify that the solid variant has agar at 20 g/L, pH 5.5, no top-level water or KOH ingredient, and either a variant edge or merged-source relationship to JCM/MediaDive `J829`.

## Additional Notes

- None found.
