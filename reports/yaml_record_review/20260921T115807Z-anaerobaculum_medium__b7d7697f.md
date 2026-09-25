# YAML Record Review: anaerobaculum_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml`
- Started UTC: 2026-09-21T11:57:38Z
- Finished UTC: 2026-09-21T11:59:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007872` |
| Name | `anaerobaculum_medium` |
| Original name | Anaerobaculum Medium |
| Source identity | `TOGO:M1336`, imported from `JCM_M1242` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Generated or maintained | Generated merge from `TOGO_M1336_Anaerobaculum_Medium`; authoritative owner is `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml` |
| Merge fingerprint | `b7d7697f883320aaf6f36c60cfc333cbd8c89f367be5feaa0b588f172ea7088b` |

The generated merge was last produced by `merge_recipes.py` on 2026-08-06. Its only source is the TOGO M1336 normalized owner, which was subsequently repaired in place on 2026-09-11 by `scripts/repair_togo_m1336_score15.py`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml` | Passed, `No issues found` |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml --out /private/tmp/anaerobaculum_medium__b7d7697f.strict.tsv --workers 1 --quiet` | Passed, 0 files with errors and 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks for this file |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` / `pkg_resources` deprecation warning |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, and no focused validator is documented for one generated record's embedded `MediaRecipe.curation_history` block |

## Identity and Grounding

The source identity is coherent. The generated record's `media_term` is `TOGO:M1336` with label `Anaerobaculum Medium`; the TOGO API record for M1336 and the original JCM GRMD page for 1242 both identify the same medium as Anaerobaculum Medium.

An ignored-inclusive exact search for `CultureMech:007872`, `TOGO:M1336`, `JCM_M1242`, `M1336`, and the merge fingerprint across `data/`, `scripts/`, `reports/`, `history/`, `.claude/`, `CLAUDE.md`, and `justfile` found the normalized owner, the generated merge, registry/index rows, archived validation reports, a current media-content review row, `scripts/repair_togo_m1336_score15.py`, and one unrelated NBRC M1336 mention in Leptospirillum HH Medium records. `find reports/yaml_record_review -maxdepth 1 -type f -name '*anaerobaculum_medium__b7d7697f.md' -print` found no existing report for this target before this review.

Grounded terms that are present in the generated file are plausible for the supplied materials:

- `CHEBI:15377` / water for Distilled water.
- `CHEBI:26710` / sodium chloride for NaCl.
- `CHEBI:8806` / Resazurin for Resazurin.
- `CHEBI:17997` / dinitrogen for N2.

The generated merge is stale relative to the maintained owner. It still reports `composition_type: UNDEFINED`, has no `ph_value`, retains empty `Unknown solution` stubs, lacks the structured stock compositions and preparation steps added on 2026-09-11, and still flattens JCM milliliter or milligram quantities into `G_PER_L`.

## Evidence

JCM Medium 1242 supports the generated record's source identity and several base ingredients:

| Claim | Evidence judgment |
|---|---|
| `Trypticase peptone`, 5 g | Supported by JCM 1242 |
| `Peptone`, 5 g | Supported by JCM 1242 |
| `Yeast extract`, 10 g | Supported by JCM 1242 |
| `NaCl`, 8 g | Supported by JCM 1242 |
| `TOGO:M1336` / JCM Medium 1242 source identity | Supported by TOGO M1336 and JCM 1242 |

The same JCM record does not support these generated quantities and representations:

| Generated claim | Inspected source | Judgment |
|---|---|---|
| `Distilled water`, `960 G_PER_L` | JCM lists 960 ml distilled water | Wrong unit; final-volume water was imported as mass |
| `Resazurin`, `0.5 G_PER_L` | JCM lists 0.5 mg resazurin | Wrong unit and 1000-fold high if read as grams per liter |
| `Salt solution (see Medium [M695])`, `40 G_PER_L`, no composition | JCM lists 40 ml Salt solution and links it to JCM Medium 676 | Wrong unit; referenced stock recipe is missing |
| `5% L-Cysteine HCl H2O solution`, `10 G_PER_L`, no composition | JCM lists 10 ml of the 5% L-Cysteine HCl H2O solution | Wrong unit; the stock concentration has been left only in the label |
| `1 M Glucose solution`, `6 G_PER_L`, no composition | JCM lists 6 ml of a 1 M glucose stock after cooling | Wrong unit; the stock concentration has been left only in the label |
| `1 M Na2S2O3 solution`, `10 G_PER_L`, no composition | JCM lists 10 ml of a 1 M thiosulfate stock after cooling | Wrong unit; the stock concentration has been left only in the label |

The source comments also support protocol details that are absent from the generated merge: mix and boil the base, cool under N2, add cysteine solution while gassing, adjust to pH 7.0, distribute under N2 into butyl-stoppered culture vessels, autoclave at 121 C for 15 min, cool, and then add separately autoclaved glucose and thiosulfate stocks stored under N2.

## Completeness

The generated record is incomplete for the source protocol. Compared with the maintained TOGO M1336 owner, it lacks:

- Structured Salt solution, L-Cysteine HCl H2O, glucose, and sodium thiosulfate stock compositions.
- Correct `ML_PER_L`, `MG_PER_L`, `MOLAR`, and `PERCENT_W_V` unit boundaries.
- `ph_value: 7.0`.
- `preparation_steps` for N2 cooling/gassing, pH adjustment, aliquoting into sealed vessels, autoclaving, cooling, and post-autoclave stock additions.
- A `sterilization` block.
- A `references` block with the inspected TOGO, JCM, and MediaDive source URLs.

Empty `target_organisms` and `growth_metrics` are not defects for this record. The inspected TOGO and JCM source records give a recipe, not primary growth outcomes for specific strains.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and no longer reflects the repaired authoritative source record. | The generated merge ends at the 2026-08-06 `MERGED_RECIPES` event and contains the pre-repair TOGO import, while `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml` has a 2026-09-11 `RESOLVED_TOGO_M1336_SCORE15` event that corrects pH, units, stock solutions, preparation steps, sterilization, and references. | Regenerate `data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml` from `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml`; if the regenerated merge still differs, fix `merge_recipes.py` or the merge freshness path that owns generated output. |
| Major | The generated quantities for distilled water, resazurin, and stock additions have the wrong units. | JCM 1242 lists distilled water as 960 ml, resazurin as 0.5 mg, Salt solution as 40 ml, 5% cysteine stock as 10 ml, 1 M glucose stock as 6 ml, and 1 M Na2S2O3 stock as 10 ml; the generated merge represents every one of those rows as `G_PER_L`. | Already corrected in `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml`; regenerate the merge and verify the normalized `ML_PER_L`, `MG_PER_L`, `MOLAR`, and `PERCENT_W_V` units survive. |
| Major | The generated solution objects are empty `Unknown solution` stubs, so the record loses source stock boundaries. | JCM 1242 names four solution additions and links the Salt solution to JCM Medium 676. The generated merge has four `solutions` entries with empty `composition: []`, all named `Unknown solution`. | Already corrected in `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml`; regenerate and verify the structured stock compositions are preserved in the merge. |
| Major | The generated merge omits anaerobic preparation details required to reproduce the source formulation. | JCM 1242 gives pH 7.0 adjustment, N2 gassing, sealed culture vessels, 121 C for 15 min autoclaving, and post-autoclave aseptic stock additions. The generated merge has no `ph_value`, `preparation_steps`, or `sterilization`. | Already corrected in `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml`; regenerate and verify those slots are copied into the merge. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml` from the current normalized owner so the generated view includes the 2026-09-11 TOGO M1336 repair.
2. After regeneration, compare the generated merge against `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml` for `ph_value`, `references`, `preparation_steps`, `sterilization`, all four `solutions` objects, and the repaired `ML_PER_L`, `MG_PER_L`, `MOLAR`, and `PERCENT_W_V` units.
3. If the regenerated merge still drops stock compositions or converts stock addition volumes to `G_PER_L`, fix the merge generator rather than editing `data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml` directly.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the regenerated merge.
- Run the merge freshness check that proves `data/merge_yaml/merged/anaerobaculum_medium__b7d7697f.yaml` was regenerated from `data/normalized_yaml/bacterial/TOGO_M1336_Anaerobaculum_Medium.yaml`.
- Manually inspect the regenerated `solutions` array to ensure JCM 676 stock components remain nested under Salt solution rather than being flattened into the final medium.
- Manually inspect the regenerated `preparation_steps` to ensure N2 remains scoped to cooling, gassing, vessel filling, and glucose/thiosulfate stock storage.

## Additional Notes

- The link reference validator passed with 0 checks, so it did not exercise the external TOGO or JCM URLs.
- The generated record's `notes` still point to `https://togomedium.org/medium/M1336`; the browsable public page currently returns only a small SPA shell, so the TOGO formulation was checked through the `gmdb_medium_by_gmid` API and the original JCM GRMD 1242 HTML page.
- The normalized owner uses `references` for TOGO M1336, JCM Medium 1242, JCM Medium 676, and MediaDive J1242. The generated stale merge lacks that block and only carries the source URLs as free text in `notes`.
