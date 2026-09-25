# YAML Record Review: ARTIFICIAL SEAWATER YEAST EXTRACT-TRYPTONE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml`
- Started UTC: 2026-09-21T15:29:13Z
- Finished UTC: 2026-09-21T15:29:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:010499` |
| Name | `artificial_seawater_yeast_extract_tryptone_medium` |
| Original name | ARTIFICIAL SEAWATER YEAST EXTRACT-TRYPTONE MEDIUM |
| Category | `fungal` |
| Source identity | MediaDive/JCM `mediadive.medium:J1269` |
| Generated status | Generated single-source merge of `data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml` |

This review covers the fungal MediaDive/JCM record. It is distinct from the
adjacent bacterial TOGO `M1365` record with the same normalized recipe name.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml --out /private/tmp/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

I used no-project validator invocations because the documented `just`
entrypoints try to build `llvmlite==0.46.0` under Python 3.13 and fail before
the requested target-specific validation begins.

## Identity and Grounding

MediaDive's `J1269` JSON resolves to the same title,
`ARTIFICIAL SEAWATER YEAST EXTRACT-TRYPTONE MEDIUM`, source `JCM`, and JCM
`GRMD=1269` link recorded in the YAML. The live JCM `GRMD=1269` URL currently
returns a "Nothing found" page, so formulation verification used the MediaDive
JSON export.

All simple ingredients in the flattened list are grounded to plausible exact
ChEBI terms, including the hydrated Mg, Ca, and Sr salts and ferric ammonium
citrate. The identity defect is structural rather than a wrong ChEBI CURIE:
the artificial seawater 4x stock is gone.

## Evidence

MediaDive exports two solution sections for `J1269`:

- `Main sol. J1269`, volume 1000 ml, with 2 g yeast extract, 2 g tryptone, 800
  ml distilled water, and a 200 ml addition of solution 5411, `Artificial
  seawater (4x)`.
- `Artificial seawater (4x)`, volume 1000 ml, containing NaCl, MgCl2 x 6 H2O,
  MgSO4 x 7 H2O, ammonium sulfate, NaHCO3, CaCl2 x 2 H2O, KCl, K2HPO4, NaBr,
  SrCl2 x 6 H2O, ammonium ferric citrate, and water.

The CultureMech record has no `solutions` block and no 200 ml artificial
seawater stock addition. Instead, the 4x stock salts are direct final-medium
ingredients at their undiluted stock grams per liter.

The pH and preparation sentence are supported: MediaDive records pH 7.0 and the
instruction to adjust pH, distribute under N2, seal with butyl rubber stoppers,
and autoclave.

## Completeness

The record preserves the pH/prep text but is incomplete in the core
composition:

- missing `Artificial seawater (4x)` as a volume-based stock addition;
- missing the stock's own solution boundary and 1000 ml stock volume;
- missing the 800 ml main-solution water row if the record is meant to preserve
  recipe rows exactly; and
- stock salts are present at 5x their final 1 L concentration if interpreted as
  final-medium `G_PER_L` values.

Optional target-organism and growth-evidence slots are empty. I did not flag
that as a defect because the inspected MediaDive source supports a recipe, not
a growth experiment.

Before reporting raw-source absence, I searched for `CultureMech:010499`,
`mediadive.medium:J1269`, `JCM Medium J1269`, and
`ARTIFICIAL SEAWATER YEAST EXTRACT-TRYPTONE MEDIUM` with
`rg --no-ignore --hidden` across `data`, `scripts`, `history`, `src`,
`reports`, and `references_cache`. That gitignore-independent search found the
normalized owner, generated merge, indexes, collision reports, and archived
reports, but no maintained raw YAML or source-specific importer file for J1269.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 4x artificial-seawater stock was flattened and its 200 ml final-medium addition was lost. | MediaDive J1269 has a main solution with a 200 ml `Artificial seawater (4x)` addition and a separate solution 5411; the generated CultureMech record has only direct salt ingredients. | `data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml` |
| major | The final ingredient concentrations for stock salts use undiluted stock values. | MediaDive lists 80 g/L NaCl, 12 g/L MgCl2 x 6 H2O, 24 g/L MgSO4 x 7 H2O, and other salt values inside the 4x stock, which is added at 200 ml to a 1 L final main solution; the CultureMech record stores those stock values directly as final-medium `G_PER_L`. | `data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml` |

## Recommended Edits

1. Restore `Artificial seawater (4x)` as a nested stock or solution addition at 200 ml in the final 1000 ml main solution.
2. Move the stock salts under that 4x stock, preserving its 1000 ml stock volume.
3. Keep yeast extract, tryptone, 800 ml water, pH 7.0, and the anaerobic autoclave preparation on the final medium.
4. Regenerate `data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium__1da012b1.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-references data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated record with MediaDive `J1269` to confirm that solution 5411 remains nested and is added to the main solution at 200 ml.

## Additional Notes

- The cited JCM URL for `GRMD=1269` returned a "Nothing found" page during
  review; MediaDive's machine-readable export was available.
