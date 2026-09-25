# YAML Record Review: HALOSIMPLEX MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml`
- Started UTC: 2026-09-23T11:30:45Z
- Finished UTC: 2026-09-23T11:31:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002655` |
| Name | `halosimplex_medium` |
| Original name | `HALOSIMPLEX MEDIUM` |
| Category | `archaea` |
| Physical state | `LIQUID` |
| pH | `3.5` |
| Generated from | `data/normalized_yaml/archaea/halosimplex_medium.yaml` |
| Source accession | `mediadive.medium:J298` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=298` |
| Merge fingerprint | `bc49b9b53422a1f2945f25ebb45a083b4a3faa3e91b4ccfe802231623707d1e1` |

I reviewed the generated merged record, its direct MediaDive/JCM normalized
owner, the live JCM 298 page, and the MediaDive `J298` REST payload.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halosimplex_medium`, `HALOSIMPLEX MEDIUM`,
`Halosimplex Medium`, and `halosimplex`. Ignored files were included. The
search found this direct JCM 298 branch, Togo `M292` and `M293` Halosimplex
branches, a modified Halosimplex branch family, and their generated outputs;
only `halosimplex_medium.yaml` feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml --out /private/tmp/halosimplex_medium_bc49b9b5.strict.tsv --workers 1 --quiet` exited 0 and wrote a header-only TSV. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record correctly identifies JCM medium 298, `HALOSIMPLEX MEDIUM`, but its
pH and ingredient concentrations do not represent the final medium. JCM 298
adjusts the final medium to pH 7.15; the pH 3.0-4.0 instruction belongs to the
trace metal stock.

Most main-medium ingredient identities are correct, but the generated
concentrations are 500-fold too high because MediaDive `J298` reports the
`Main sol. J298` volume as `2`, matching the 2 ml trace-stock addition rather
than the stated 1 L final volume.

## Evidence

JCM 298 lists 2.5 g glycerol, 2.5 g sodium pyruvate, 0.5 g K2HPO4, 1 g
ammonium sulfate, 4 g KCl, 200 g NaCl, 20 g `MgSO4 x 7 H2O`, and 2 ml trace
metal solution in a recipe brought to 1.0 L and adjusted to pH 7.15.

The generated record uses MediaDive's incorrect 2 ml main-solution volume to
turn those source amounts into impossible concentrations:

| Ingredient | JCM source amount | Generated amount |
|---|---:|---:|
| `Glycerol` | 2.5 g/L | 1250 g/L |
| `Sodium pyruvate` | 2.5 g/L | 1250 g/L |
| `K2HPO4` | 0.5 g/L | 250 g/L |
| `(NH4)2SO4` | 1 g/L | 500 g/L |
| `KCl` | 4 g/L | 2000 g/L |
| `NaCl` | 200 g/L | 100000 g/L |
| `MgSO4 x 7 H2O` | 20 g/L | 10000 g/L |

MediaDive also preserves the trace metal stock as a separate 100 ml recipe
referenced from the final medium at 2 ml/L. The generated record flattens Zn,
Mn, B, Co, Cu, Ni, and Mo rows from that stock into top-level ingredients at
stock concentration, drops the stock's 100 ml water row, and stores the stock's
pH 3.0-4.0 instruction as a main-medium preparation step.

## Completeness

The record is missing the main 1 L distilled-water final-volume context, the
separate 100 ml trace-metal stock boundary, and the 2 ml/L trace-stock addition.

JCM 298 also says that solid agar slopes or plates may be made by adding 20 g
Bacto agar `(BD-Difco)`. The liquid base record preserves this only as
unstructured text; the solid option has no structured variant.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Every main-medium concentration is 500-fold too high. | JCM says to bring the main medium to 1.0 L; MediaDive imported `Main sol. J298` with `volume: 2`, so 200 g NaCl became 100000 g/L and 20 g magnesium sulfate became 10000 g/L. | `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the MediaDive importer |
| Major | The trace metal solution was flattened into top-level ingredients at stock strength. | JCM lists `Trace metal solution` as a 2 ml addition and defines a separate 100 ml stock; the generated record has Zn, Mn, B, Co, Cu, Ni, and Mo as final-medium ingredients. | `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the MediaDive importer |
| Major | The record uses trace-stock pH as final-medium pH. | JCM says the final medium is adjusted to pH 7.15 and the trace stock to pH 3.0-4.0; the generated top-level `ph_value` is 3.5. | `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the MediaDive preparation importer |
| Major | Water and stock boundaries are missing. | JCM gives a 1 L final volume and a 100 ml trace-stock water row; neither water component nor the 2 ml/L stock reference is structured. | `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the MediaDive importer |
| Minor | `NiCl2 x 6 H2O` is grounded to generic `nickel dichloride`. | The source ingredient is a hexahydrate, but the generated CHEBI label is only `nickel dichloride`. | `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the ingredient resolver |

## Recommended Edits

1. In `data/normalized_yaml/archaea/halosimplex_medium.yaml` or the MediaDive
   importer, treat JCM 298's main solution as a 1 L recipe and recalculate the
   weighed main ingredients at the source g/L values.
2. Preserve the trace metal solution as a 100 ml stock and reference it from
   the main medium at 2 ml/L.
3. Move pH 3.0-4.0 onto the trace metal stock and set the final medium pH to
   7.15.
4. Restore water/final-volume representation for both the main solution and
   the trace stock.
5. Represent the optional 20 g Bacto agar `(BD-Difco)` solid branch explicitly.
6. Resolve `NiCl2 x 6 H2O` to an exact hexahydrate term or leave it
   ungrounded.
7. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halosimplex_medium__bc49b9b5.yaml` directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halosimplex_medium.yaml`
   after the normalized JCM 298 record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/halosimplex_medium.yaml`
   to confirm exact trace-metal hydrate grounding.
3. Run `just verify-merges` to prove the generated JCM 298 branch regenerates
   from the corrected normalized source.
4. Manually compare the regenerated record with JCM 298 and MediaDive `J298`
   to confirm the final-medium pH, trace-stock pH, and 2 ml/L trace-stock
   addition are no longer conflated.

## Additional Notes

The modified Halosimplex medium branches are separate JCM media and should not
be used to patch this record except through explicit parent/variant curation.
