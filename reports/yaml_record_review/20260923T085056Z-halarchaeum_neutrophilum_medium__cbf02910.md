# YAML Record Review: HALARCHAEUM NEUTROPHILUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/halarchaeum_neutrophilum_medium__cbf02910.yaml
- Started UTC: 2026-09-23T08:49:38Z
- Finished UTC: 2026-09-23T08:50:56Z
- Verdict: pass with minor issues

## Target

- Reviewed generated YAML for liquid `HALARCHAEUM NEUTROPHILUM MEDIUM`.
- Stable ID: `CultureMech:003173`.
- Primary source in generated record: direct JCM/MediaDive `mediadive.medium:J829`.
- Merge fingerprint: `cbf02910cca26f2047cd101c0d4f31cf9bc7a3438f36d0aec7c96d41b3ad63e9`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass, 0 error rows in `/private/tmp/halarchaeum_neutrophilum_medium_cbf02910.strict.tsv`.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the direct JCM/MediaDive import for JCM medium 829.
- An exact `rg --no-ignore --hidden` search for `JCM_M829`, `GRMD=829`, and `mediadive.medium:J829` found the direct JCM/MediaDive source, source-equivalent Togo `M864` / `JCM_M829`, and a Togo `M865` / `JCM_M829-2` solid-agar child in `data/merge_yaml` and `data/normalized_yaml`.
- The live JCM `GRMD=829` endpoint currently returns `Nothing found`, so MediaDive `J829` and the Togo API records were the available cross-checks for this JCM recipe.

## Evidence

- MediaDive `J829` lists Casamino acids, Tryptone, and Yeast extract at 2 g/L each; NaCl 180 g/L, MgCl2 x 6 H2O 20 g/L, KCl 5 g/L, glucose 10 g/L; pH 5.5; and an optional solid-medium instruction to add 20.0 g/L agar.
- The Togo `M864` API record reports the same JCM `M829` source, ingredient masses, pH 5.5, KOH pH-adjustment note, and 20 g/L agar solid-medium note.
- The generated direct JCM/MediaDive record preserves the liquid formula, pH 5.5, pH-adjustment preparation step, and solid-medium agar note without importing KOH or water as top-level formula ingredients.

## Completeness

- Required source fields, medium identity, non-water concentrations, units, pH, preparation notes, application, and generated merge metadata are present.
- `Casamino acids`, `Tryptone`, and `Yeast extract` are intentionally ungrounded complex ingredients; MediaDive marks all three as `BD-Difco` products, but those source attributes are not retained in the generated direct record.
- No target-organism assertions are present; none were evident in the generated source record.

## Findings

- Minor: The source-equivalent Togo `M864` / `JCM_M829` liquid import is split from the direct JCM/MediaDive `J829` import.
- Minor: The Togo `M865` / `JCM_M829-2` solid-agar child is split as `halarchaeum_neutrophilum_medium__daff5c52.yaml`; it is represented in the direct generated record only as a 20 g/L agar preparation note.
- Minor: Source `BD-Difco` qualifiers on Casamino acids, Tryptone, and Yeast extract are not retained.

## Recommended Edits

- Add source-equivalence handling so direct `mediadive.medium:J829` merges with Togo `M864` / `JCM_M829`.
- Decide whether Togo `M865` / `JCM_M829-2` should remain a separate solid-agar variant, become a `SOLIDIFICATION_VARIANT` child, or collapse into the direct JCM/MediaDive record's existing agar note.
- Preserve the `BD-Difco` qualifiers for Casamino acids, Tryptone, and Yeast extract if product-level specificity is in scope for this recipe.

## Follow-up Checks

- After regeneration, verify that the liquid record still has no top-level water or KOH ingredient and that any solid-agar variant has agar at exactly 20 g/L.

## Additional Notes

- None found.
