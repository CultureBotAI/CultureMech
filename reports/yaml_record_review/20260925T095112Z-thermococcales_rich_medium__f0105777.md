# YAML Record Review: THERMOCOCCALES RICH MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcales_rich_medium__f0105777.yaml`
- Started UTC: `2026-09-25T09:51:12Z`
- Finished UTC: `2026-09-25T09:52:17Z`
- Verdict: pass with minor issues

## Target
Generated MediaDive archaeal recipe `CultureMech:003156`, `thermococcales_rich_medium`, with medium term `mediadive.medium:J811` and label `THERMOCOCCALES RICH MEDIUM`.

It is a single-source generated record from normalized source `thermococcales_rich_medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The target is correctly grounded to JCM Medium 811, `THERMOCOCCALES RICH MEDIUM`, through `mediadive.medium:J811`.

The reviewed target groundings match the source ingredient strings, including tungstate dihydrate, ferric chloride hexahydrate, sodium bromide, and strontium chloride hexahydrate.

The same JCM 811 URL is also represented by TOGO M845 in `data/merge_yaml/merged/THERMOCOCCALES_RICH_MEDIUM.yaml`.

## Evidence
JCM 811 and MediaDive J811 specify a flat 1 L recipe with PIPES, NaCl, MgCl2 x 6 H2O, KCl, ammonium sulfate, K2HPO4, KH2PO4, CaCl2 x 2 H2O, NaBr, SrCl2 x 6 H2O, 3.3 mg Na2WO4 x 2 H2O, 6.8 mg FeCl3 x 6 H2O, yeast extract, tryptone, sulfur powder, Na2S x 9 H2O, resazurin, and water.

The generated MediaDive record matches the source quantities and correctly represents the milligram tungstate, ferric chloride, and resazurin rows as `0.0033`, `0.0068`, and `0.001 G_PER_L`.

The source preparation step, including 3-day sulfur steaming, sterile sulfide reduction under N2, pH readjustment, and the JCM 16557 high-pressure cultivation comment, is preserved.

Exact source search found the separate TOGO M845 branch for JCM 811. That branch must not be merged as-is because it converts the source 1 L water row to `1 G_PER_L`, source 1 mg resazurin to `1 G_PER_L`, and source milligram tungsten and iron rows to whole gram-per-liter rows.

## Completeness
The target MediaDive branch contains the complete JCM 811 formula and preparation text visible in both JCM and MediaDive.

The duplicate TOGO branch lacks the structured preparation steps and has multiple unit-conversion defects.

## Findings
1. Minor issue: TOGO M845 remains split from this MediaDive JCM 811 identity.
2. Minor issue: the unmerged TOGO M845 branch has liter-to-gram and milligram-to-gram conversion defects.

## Recommended Edits
1. Normalize `TOGO_M845_Thermococcales_Rich_Medium` in `data/normalized_yaml`, not the generated TOGO branch, to preserve liter and milligram units.
2. Preserve the sterile sulfide-reduction and JCM 16557 high-pressure preparation text on the TOGO source.
3. Merge `TOGO:M845` with `mediadive.medium:J811` by exact JCM 811 source identity after the TOGO chemistry is corrected.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M845`, `mediadive.medium:J811`, and `jcm_grmd?GRMD=811` and confirm that JCM 811 regenerates as one canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files.
