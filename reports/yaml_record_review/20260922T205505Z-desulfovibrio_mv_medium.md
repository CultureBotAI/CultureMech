# YAML Record Review: DESULFOVIBRIO (MV) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_mv_medium.yaml`
- Started UTC: 2026-09-22T20:55:05Z
- Finished UTC: 2026-09-22T20:55:05Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:001779` for `desulfovibrio_mv_medium`, a MediaDive import of DSMZ Medium 641.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:641`, `DESULFOVIBRIO (MV) MEDIUM`, with DSMZ provenance in `notes`.

A gitignore-independent exact filename lookup found the DSMZ 641 normalized source plus a distinct `desulfovibrio_mv_medium_for_dsm_13257` record family. The generated merge for the current target correctly groups DSMZ Medium 641 with seven KOMODO 641 exact or strain-specific companion records.

## Evidence

MediaDive 641 represents the main recipe as a 1003 ml solution at pH 7.0-7.2 with six basal salts, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, yeast extract, 0.5 ml 0.1% sodium resazurin, sodium carbonate, Na-DL-lactate, 1 ml Wolin's vitamin solution, sodium sulfide, and 1000 ml distilled water.

Trace element solution SL-10 is a 1000 ml stock containing 10 ml 25% HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, molybdate, and 990 ml distilled water. Selenite-tungstate solution is a 1000 ml stock containing NaOH, selenite, tungstate, and water. Wolin's vitamin solution is a 1000 ml stock containing ten vitamins plus water.

## Completeness

The target preserves the DSMZ pH range and the high-level preparation text for sparging the basal medium, adding carbonate, vitamins, lactate, and sulfide after autoclaving, and optional sodium dithionite before inoculation.

The composition is incomplete because the three 1 ml stock additions are absent as `solutions`. Their constituents were flattened into top-level ingredient rows at stock G/L values, and the water rows for the main solution and all three stocks are missing.

## Findings

- High: Trace element solution SL-10 was flattened. HCl, FeCl2 x 4 H2O, zinc, manganese, borate, cobalt, copper, nickel, and molybdate are listed at stock strengths instead of inside a 1 ml/L solution addition.
- High: Selenite-tungstate solution was flattened. NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O are listed at stock strengths instead of inside a 1 ml/L solution addition.
- High: Wolin's vitamin solution was flattened. Its biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid concentrations are stock concentrations rather than 1 ml/L final-medium contributions.
- Medium: The 1000 ml main distilled-water row, 990 ml Trace element stock water row, 1000 ml Selenite-tungstate stock water row, and 1000 ml Wolin's vitamin stock water row are absent.
- Low: The Trace element solution preparation instruction was appended as a top-level preparation step instead of being scoped to the Trace element stock recipe.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_mv_medium.yaml` so DSMZ 641 uses structured 1 ml additions for Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution.
- Move each stock recipe into a subordinate `solutions` entry with its own water row.
- Keep the KOMODO Medium 641 source-duplicate and strain-specific variant links rooted under the repaired DSMZ Medium 641 parent.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the seven KOMODO 641 companion records still merge with, or remain variant children of, the repaired DSMZ 641 record as intended.
- Verify the regenerated main recipe keeps 1 ml/L Trace element, Selenite-tungstate, and Wolin's vitamin additions rather than stock-strength top-level trace-metal and vitamin rows.

## Additional Notes

None found.
