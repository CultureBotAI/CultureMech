# YAML Record Review: PYGV MARINE MEDIUM (B)

- Repository: CultureMech
- Record: data/merge_yaml/merged/pygv_marine_medium_b__496c513c.yaml
- Started UTC: 2026-09-24T23:14:11Z
- Finished UTC: 2026-09-24T23:14:45Z
- Verdict: needs curation

## Target

- Generated file: data/merge_yaml/merged/pygv_marine_medium_b__496c513c.yaml
- Stable ID: CultureMech:015378
- Maintained owner: data/normalized_yaml/specialized/pygv_marine_medium_b.yaml
- Merge sources: pygv_marine_medium_b
- Merge fingerprint: 496c513c756f782f6171dc99b7bd87c5786f76a4fba03a5fe070e4549265e9b9
- Source grounding: JCM Medium 1059 / MediaDive J1059 PYGV MARINE MEDIUM (B), liquid formulation

## Validation

| Check | Result |
| --- | --- |
| LinkML open schema | Passed with `No issues found`. |
| Strict schema | Passed with 0 errors. `/private/tmp/pygv_marine_medium_b__496c513c.strict.tsv` contains only the header line. |
| Reference validation | Passed 1 file with 0 reference checks. |
| Term validation | Passed after the known `eutils` / `pkg_resources` warning. |
| Embedded history validation | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is correctly identified as the direct JCM/MediaDive J1059 import for PYGV Marine Medium (B). JCM Medium 1059 lists the liquid recipe as 0.25 g/L Bacto peptone, 0.25 g/L Yeast extract, 20 ml/L Mineral salt solution from JCM 304, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution from JCM 304, 250 ml/L Artificial seawater from JCM 304, 710 ml/L Distilled water, and optional KOH to pH 7.2-7.4.

MediaDive J1059 expands the JCM 304 stocks, including Metals 44, into the REST payload. The direct importer then flattened the Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 contents into top-level ingredients and dropped all solution aliquots.

An exact ignored-file search for `mediadive.medium:J1059`, `GRMD=1059`, `TOGO:M1126`, `TOGO:M1127`, and `pygv_marine_medium_b` under `data/normalized_yaml` and `data/merge_yaml/merged` found the direct JCM J1059 branch, the repaired TOGO M1126 liquid owner, and the repaired TOGO M1127 solid owner.

## Evidence

- JCM Medium 1059 lists 20 ml Mineral salt solution, 10 ml 2.5% Glucose solution, 10 ml Vitamin solution, 250 ml Artificial seawater, and 710 ml Distilled water per liter.
- JCM Medium 1059 references JCM Medium 304 for Mineral salt solution, Vitamin solution, and Artificial seawater.
- MediaDive J1059 expands Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 as nested REST solutions.
- The generated YAML has no `solutions` section and no 710 ml/L water ingredient.
- The generated top-level list includes Mineral salt solution internals, Vitamin solution internals, Artificial seawater internals, and Metals 44 internals.
- The generated top-level values `CaCl2 x 2 H2O: 4.442 G_PER_L` and `FeSO4 x 7 H2O: 0.599 G_PER_L` are sums across unrelated source stocks.
- The owner stores pH 7.3 as a scalar even though JCM gives an adjustment range of 7.2-7.4.

## Completeness

The direct JCM J1059 branch preserves the intended liquid identity and the main source preparation string, but it is incomplete as a usable CultureMech recipe because it has lost all cross-referenced JCM 304 stock boundaries, all source solution aliquot volumes, all stock-local water rows, the 2.5% glucose concentration, and the pH range. The repaired TOGO M1126 owner is already a model for the same liquid formulation with those stock structures restored.

## Findings

- Major: Mineral salt solution, 2.5% Glucose solution, Vitamin solution, Artificial seawater, and Metals 44 are absent as solution aliquots.
- Major: stock-local ingredients from four source stocks are flattened as final top-level ingredients.
- Major: duplicate ingredient merging summed chemicals that appear in different stocks, generating CaCl2 x 2 H2O 4.442 g/L and FeSO4 x 7 H2O 0.599 g/L values that are not source ingredients.
- Major: the 10 ml 2.5% Glucose solution aliquot was stored as top-level Glucose 10 g/L.
- Minor: the source pH range 7.2-7.4 was collapsed to `ph_value: 7.3`.

## Recommended Edits

1. Re-resolve `data/normalized_yaml/specialized/pygv_marine_medium_b.yaml` from MediaDive J1059 and the exact JCM Medium 1059 page.
2. Restore top-level ingredients to Bacto peptone, Yeast extract, 20 ml/L Mineral salt solution, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution, 250 ml/L Artificial seawater, 710 ml/L Distilled water, and variable KOH for final pH adjustment.
3. Move JCM 304 Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 internals into nested stock solutions.
4. Store pH 7.2-7.4 as `ph_range` instead of scalar pH 7.3.
5. Regenerate and check whether the repaired direct JCM J1059 branch de-duplicates with TOGO M1126 while remaining distinct from the M1127 solid agar variant.

## Follow-up Checks

- Re-run open, strict, reference, and term validators on regenerated `pygv_marine_medium_b__496c513c`.
- Compare the regenerated direct branch against MediaDive J1059, JCM Medium 1059, JCM Medium 304, and JCM Medium 149.
- Repeat the exact ignored-file search for `mediadive.medium:J1059`, `GRMD=1059`, `TOGO:M1126`, `TOGO:M1127`, and `pygv_marine_medium_b` to confirm the J1059 liquid and solid branches merge only where appropriate.

## Additional Notes

None.
