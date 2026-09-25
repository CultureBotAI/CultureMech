# YAML Record Review: DESULFOVIBRIO MEDIUM (SEAWATER)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_medium_seawater.yaml`
- Started UTC: 2026-09-22T20:45:48Z
- Finished UTC: 2026-09-22T20:46:46Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:001775` for `desulfovibrio_medium_seawater`, a MediaDive import of DSMZ Medium 63b.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, exit 0 with a header-only TSV and 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

An exact gitignore-independent lookup found only `data/normalized_yaml/bacterial/desulfovibrio_medium_seawater.yaml` and this generated record for the DSMZ 63b seawater variant.

The reviewed record is grounded to `mediadive.medium:63b`, `DESULFOVIBRIO MEDIUM (SEAWATER)`, with the DSMZ Medium 63b PDF URL preserved in `notes`.

## Evidence

MediaDive 63b models the final 1 liter medium as 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C.

Solution A contains phosphate, ammonium, sulfate, calcium, magnesium, Na-DL-lactate, yeast extract, 0.5 ml 0.1% w/v sodium resazurin, and 980 ml filtered aged seawater. Solution B contains 0.5 g ferrous sulfate heptahydrate in 10 ml water. Solution C contains 0.1 g sodium thioglycolate and 0.1 g ascorbic acid in 10 ml water.

## Completeness

The record preserves the imported pH range and the DSMZ text about boiling Solution A, cooling under nitrogen, adding Solutions B and C, dispensing under nitrogen, autoclaving, and optionally using Biomaris bottled seawater.

The composition is incomplete because the 980/10/10 ml solution structure is flattened: Solution A rows are scaled to 980 ml stock concentrations, Solution B and C rows are stock-strength top-level ingredients, and water/seawater volumes are not modeled with the correct units.

## Findings

- High: Solution B was flattened at stock strength. The generated record lists `FeSO4 x 7 H2O` as 50 G/L even though DSMZ 63b uses the 10 ml Solution B stock to add 0.5 g per final liter.
- High: Solution C was flattened at stock strength. Sodium thioglycolate and ascorbic acid are listed as 10 G/L, but each should be 0.1 G/L in the final 1 liter medium.
- Medium: Solution A ingredients were scaled to the 980 ml Solution A volume, yielding values such as K2HPO4 0.510204 G/L, Na-DL-lactate 2.04082 G/L, and yeast extract 1.02041 G/L instead of their final 1 liter amounts.
- Medium: The filtered aged seawater row is represented as `Sea water` 980 `G_PER_L`; it should stay a 980 ml Solution A solvent volume.
- Medium: The 10 ml water row for Solution B and the 10 ml water row for Solution C are absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_medium_seawater.yaml` so the 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C source structure is either preserved as solutions or converted to correct final 1 liter concentrations.
- Convert the ferrous sulfate, sodium thioglycolate, and ascorbic acid rows from 50/10/10 G/L stock strengths to 0.5/0.1/0.1 G/L final-medium amounts if the recipe remains flattened.
- Represent the 980 ml filtered aged seawater row as a volume contribution rather than 980 G/L.
- Split the long DSMZ procedure into ordered steps and keep the Biomaris alternative seawater note attached to the seawater/Solution A context.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate the merged YAML and compare the final amounts against MediaDive 63b.
- Confirm the regenerated record has the same final 1 liter arithmetic as DSMZ 63b: 980 ml Solution A plus 10 ml Solution B plus 10 ml Solution C.

## Additional Notes

None found.
