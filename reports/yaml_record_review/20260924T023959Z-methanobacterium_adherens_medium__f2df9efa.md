# YAML Record Review: METHANOBACTERIUM ADHERENS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_adherens_medium__f2df9efa.yaml
- Started UTC: 2026-09-24T02:39:25Z
- Finished UTC: 2026-09-24T02:39:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002797 |
| Name | methanobacterium_adherens_medium |
| Original name | METHANOBACTERIUM ADHERENS MEDIUM |
| Category | archaea |
| Medium term | mediadive.medium:J447, JCM Medium J447 |
| Source | JCM via MediaDive |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=447 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml |
| Merge fingerprint | f2df9efabe1e8643fd3bdac92a5f2d861045e5edea5d7658bc3fe048f6127fe4 |

This generated record is a single-source merge from `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml`.
Future fixes belong in that maintained MediaDive/JCM owner, the MediaDive import path that flattened nested stocks, or source-alias rules that merge its TOGO M448 duplicate, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_adherens_medium__f2df9efa.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_adherens_medium__f2df9efa.yaml --out /private/tmp/methanobacterium_adherens_medium__f2df9efa.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_adherens_medium__f2df9efa.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_adherens_medium__f2df9efa.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The MediaDive identity is correct: MediaDive `J447` names `METHANOBACTERIUM ADHERENS MEDIUM`, carries source `JCM`, uses the JCM `GRMD=447` URL, and records pH 7.7 for this archaeal liquid medium.

The live JCM 447 URL now returns a small "Nothing found" page, so this review treated the MediaDive J447 and TOGO M448 local imports as preserved snapshots of the JCM recipe rather than as independently inspected live JCM content.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found two maintained MediaRecipe owners for the same JCM 447 source: this MediaDive owner at `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml` and the TOGO owner at `data/normalized_yaml/archaea/TOGO_M448_Methanobacterium_Adherens_Medium.yaml`. No third exact MediaRecipe owner or generated medium was found in that bounded, ignored-file-inclusive search; the remaining J447 hits were indexes and the MediaDive `Main sol. J447` SolutionRecipe.

## Evidence

MediaDive J447 supports the top-level final-medium masses for calcium chloride, magnesium chloride, ammonium chloride, potassium phosphate, potassium chloride, sodium chloride, sodium acetate, yeast extract, direct vitamin B12, sodium bicarbonate, resazurin, and sodium sulfide after normalization over a 1012 ml final volume.

Three source stocks are not represented correctly:

- `Trace element solution` is a 1 ml addition, but its nitrilotriacetic acid, ferrous sulfate, boric acid, manganese chloride, cobalt chloride, copper chloride, zinc sulfate, and molybdate rows are top-level ingredients at stock concentration.
- `Selenite-tungstate solution` is a 1 ml addition, but NaOH, sodium selenite, and sodium tungstate from that 1 L stock are top-level ingredients at stock concentration.
- `Trace vitamins` is a 10 ml addition, but the vitamin stock rows are top-level ingredients at stock concentration.

The `Vitamin B12` ingredient was merged across two separate source claims: the final medium has a direct 0.05 mg row, while Trace vitamins contains 0.1 mg vitamin B12 in 1 L stock. The generated `0.0001494071 G_PER_L` sum mixes final-medium and stock concentrations.

The main preparation procedure is supported by the MediaDive payload, including boiling, H2-CO2 gassing, autoclaving, filter-sterilized bicarbonate, separately autoclaved sulfide, anaerobic addition of those two solutions, pH 7.6 - 7.8, and H2-CO2 pressurization. The second `preparation_steps` entry for nitrilotriacetic acid pH adjustment belongs to Trace element solution, not the final medium.

## Completeness

The record has no target-organism, strain, literature growth, or variant claims, so there were no growth-evidence assertions to check.

The record also loses the 8% bicarbonate and 5% sulfide stock strengths from the main MediaDive payload. Their final masses are present, but the source preparation cannot be reproduced from mass-only rows.

The `BD-Difco` attribute on yeast extract is dropped in this MediaDive projection; the TOGO sibling preserves it in the preferred term.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three source stocks were flattened into final-medium ingredients at stock strength. | MediaDive J447 doses Trace element solution at 1 ml, Selenite-tungstate solution at 1 ml, and Trace vitamins at 10 ml. The generated YAML stores every stock component as a direct `ingredient` at the stock concentration. | `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml` and MediaDive importer stock handling. |
| Major | Vitamin B12 rows from different contexts were merged. | The generated `Vitamin B12` row sums `4.94071e-05` from the final-medium 0.05 mg row with `0.0001` from the 1 L Trace vitamins stock row. | Same maintained owner; prevent stock flattening before duplicate cleanup. |
| Major | Trace-element preparation text is scoped to the final medium. | The nitrilotriacetic acid / pH 6.5 / NaOH step belongs to Trace element solution, but the YAML appends it as a top-level `preparation_steps` entry. | `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml`. |
| Major | JCM 447 is duplicated through MediaDive and TOGO import paths. | This owner and `data/normalized_yaml/archaea/TOGO_M448_Methanobacterium_Adherens_Medium.yaml` both cite JCM `GRMD=447` and merge to separate generated files. | Source aliasing for MediaDive J447 and TOGO M448, plus a regenerated merge. |
| Minor | Liquid-stock strengths and yeast supplier detail are weakened. | MediaDive records bicarbonate as an 8% solution and sulfide as a 5% solution; the YAML keeps only final masses. MediaDive records yeast extract with `BD-Difco`; the YAML stores only `Yeast extract`. | `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml`. |

## Recommended Edits

1. Preserve Trace element solution, Selenite-tungstate solution, and Trace vitamins as stock additions dosed at 1 ml, 1 ml, and 10 ml.
2. Remove all components of those stocks from top-level final-medium `ingredients` and undo the cross-context `Vitamin B12` sum.
3. Attach the nitrilotriacetic acid / NaOH pH-adjustment preparation step to Trace element solution.
4. Preserve 8% NaHCO3, 5% Na2S x 9 H2O, and the `BD-Difco` yeast-extract attribute from the source payload.
5. Add a source alias between MediaDive J447 and TOGO M448 so one generated Methanobacterium adherens Medium record is emitted for JCM 447.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/archaea/methanobacterium_adherens_medium.yaml` and the regenerated merge output.
- Compare the regenerated formula against MediaDive J447 for the 1 ml Trace element solution, 1 ml Selenite-tungstate solution, 10 ml Trace vitamins, and the standalone 0.05 mg vitamin B12 row.
- Search the regenerated YAML for exact unsupported stock-strength concentrations `12.8 G_PER_L`, `0.4 G_PER_L` on `NaOH`, and `0.0001494071 G_PER_L` on `Vitamin B12`; none should remain as final direct ingredient rows.
- Search `data/merge_yaml/merged` with ignored files included for exact `GRMD=447`, `mediadive.medium:J447`, and `TOGO:M448` after merge regeneration; the same JCM source should not publish as both a MediaDive and TOGO record.

## Additional Notes

The TOGO M448 sibling keeps the three external stock additions as empty solution stubs instead of flattening them, but it also turns gases into variable ingredients and lacks the MediaDive preparation text needed to reproduce the anaerobic bottle handling.
