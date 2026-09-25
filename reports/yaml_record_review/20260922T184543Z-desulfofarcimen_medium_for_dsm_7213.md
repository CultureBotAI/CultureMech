# YAML Record Review: Desulfofarcimen Medium (For DSM 7213)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml
- Started UTC: 2026-09-22T18:41:21Z
- Finished UTC: 2026-09-22T18:45:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009103 |
| Name | desulfofarcimen_medium_for_dsm_7213 |
| Original name | Desulfofarcimen Medium (For DSM 7213) |
| Media term | TOGO:M2533, TOGO Medium M2533 |
| Source | TOGO M2533, derived from DSMZ Medium 124 |
| Category | bacterial |
| Generated status | Generated single-source merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained parent | `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml` |
| Merge fingerprint | 18367784c1e1721b1a9209b80e5711699416fa3da6000feb1e00960e2a88f6a1 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml --out /private/tmp/desulfofarcimen_medium_for_dsm_7213.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning first. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is correct. TOGO M2533 identifies `Desulfofarcimen Medium (For DSM 7213)`, cites DSMZ Medium 124 as its original source, and includes the DSM 7213-specific benzoate substitution from that DSMZ recipe. DSMZ Medium 124 describes this variant by replacing acetate and butyrate with 0.60 g/l Na-benzoate added after autoclaving from a filter-sterilized anoxic stock solution.

The source's final pH 7.0-7.2 did not survive onto the generated YAML even though TOGO M2533 exposes it in metadata and the linked DSMZ PDF states the same final pH. The bacterial category, liquid physical state, and complex/undefined composition are otherwise consistent with the source recipe.

## Evidence

The core final-medium salts, yeast extract, sulfate, bicarbonate, sulfide, sodium resazurin, water, and DSM 7213 benzoate replacement are supported by TOGO M2533 and the DSMZ Medium 124 PDF. The generated record correctly omits the acetate and butyrate that appear in the base medium but should be replaced for DSM 7213.

The stock and solution evidence is not faithfully represented:

- `Distilled water` is a top-level 3990.0 G_PER_L ingredient created by summing water from the final medium and three stocks: 1000 ml, 990 ml, 1000 ml, and 1000 ml.
- Trace element SL-10 stock components are top-level final ingredients, and the milligram stock values from TOGO were coerced into G_PER_L values such as 36 G_PER_L `Na2MoO4 x 2 H2O`, 70 G_PER_L `ZnCl2`, and 100 G_PER_L `MnCl2 x 4 H2O`.
- Selenite-tungstate stock components have the same stock-to-final error for `NaOH`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O`.
- Vitamin stock components have the same milligram-to-G_PER_L error for `Biotin`, `Folic acid`, `Thiamine-HCl`, `Pyridoxine-HCl`, `Riboflavin`, `Nicotinic acid`, `Vitamin B12`, `Lipoic acid`, and `D-Ca-pantothenate`.
- The 0.5 ml sodium resazurin stock and the 0.6 g/l sodium benzoate replacement are present only as empty `Unknown solution` stubs with `G_PER_L` units.

TOGO M2533 also appears to have parsed DSMZ's `Wolin's vitamin solution (10x)` label into a generic `Vitamin solution` at 10 ml, while the current linked DSMZ Medium 124 PDF lists `Wolin's vitamin solution (10x)` at 1.00 ml. The CultureMech record should either follow the DSMZ primary source or preserve that disagreement explicitly; accepting a 10 G_PER_L `Vitamin solution` stub hides the source conflict.

## Completeness

No source preparation comments survived as structured `preparation_steps`. TOGO M2533 has the anaerobic final-medium preparation comment, the DSM 7213 benzoate post-autoclave comment, and the SL-10 dissolution comment; the generated YAML has none of them.

The top-level `N2` and `Carbon dioxide gas` rows are gas-atmosphere preparation conditions, not ingredients. They also lose the 80% N2/20% CO2 final-medium sparging and dispensing atmosphere and the 100% N2 stock-preparation context.

The record correctly leaves explicit growth evidence empty because the inspected TOGO/DSMZ recipe sources do not establish a strain growth experiment.

Gitignore-independent `rg --no-ignore --hidden` over `data`, `.claude`, `src`, and `scripts` found exactly the normalized owner, generated merge, TOGO source indexes, and import-tracking diagnostics for `CultureMech:009103` / `TOGO:M2533`. A `find` under the ignored report directory found no pre-existing `desulfofarcimen_medium_for_dsm_7213` review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Water and stock components from four TOGO recipe sections are collapsed into one flat final ingredient list. | The generated record has 3990.0 G_PER_L water and stock-strength trace, selenite-tungstate, and vitamin chemicals as top-level ingredients; TOGO and DSMZ keep those quantities inside distinct final, SL-10, selenite-tungstate, and vitamin sections. | `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml`, or the TOGO importer if this pattern is repaired globally. |
| Major | The DSM 7213 benzoate replacement is modeled as an unresolved empty solution rather than as sodium benzoate added after autoclaving. | TOGO M2533 imports `Na-benzoate*` with the comment that it replaces acetate and butyrate at 0.60 g/l for DSM 7213; the generated YAML has `Na-benzoate*` under `solutions` with an empty composition and no chemical grounding. | `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml`. |
| Major | The vitamin addition conflicts with the linked primary source and uses the wrong unit. | DSMZ Medium 124 lists 1.00 ml `Wolin's vitamin solution (10x)`, but the generated YAML inherits TOGO's generic `Vitamin solution` stub at `10` G_PER_L. | `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml`; compare the TOGO import against DSMZ before deciding whether to override or preserve a conflict note. |
| Major | Source preparation and gas-atmosphere claims are missing or mis-scoped. | TOGO M2533 and DSMZ describe 80% N2/20% CO2 sparging, 100% N2 stock preparation, filter-sterilized benzoate stock, filter-sterilized vitamin stock, autoclaving, final pH checking, and SL-10 preparation; the generated YAML has no `preparation_steps` and treats N2/CO2 as variable ingredients. | `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml`. |

## Recommended Edits

1. Rebuild the normalized DSM 7213 variant from the TOGO M2533 sections while preserving final-medium components, named stock additions, and stock recipes separately.
2. Remove the collapsed 3990.0 G_PER_L water row and move each water volume to its actual final or stock solution context.
3. Ground `Na-benzoate*` to sodium benzoate after removing the source footnote marker, model it as the DSM 7213 replacement for acetate and butyrate, and capture that it is added after autoclaving from a filter-sterilized anoxic stock.
4. Reconcile TOGO's `Vitamin solution` 10 ml row with the linked DSMZ `Wolin's vitamin solution (10x)` 1 ml row and record whichever decision the inspected source text supports.
5. Restore source preparation steps, including the anaerobic N2/CO2 atmosphere and the SL-10 stock-specific dissolution instruction, without leaving N2 and CO2 as top-level variable ingredients.
6. Regenerate `data/merge_yaml/merged/desulfofarcimen_medium_for_dsm_7213.yaml`.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on the repaired normalized record and regenerated merged record.
2. Re-run concentration-plausibility reporting for `CultureMech:009103`; the WATER_AS_VOLUME, TRACE_SALT_AS_STOCK, and INDICATOR_UNIT_SLIP rows should disappear.
3. Re-run ungrounded-ingredient reporting; the `Na-benzoate*` unresolved-solution row should disappear.
4. Manually compare the regenerated record against TOGO M2533 and the current DSMZ Medium 124 PDF for the DSM 7213 benzoate substitution, stock addition amounts, final pH 7.0-7.2, and anaerobic preparation.

## Additional Notes

The generated record has `high_metal: true`; that flag is an artifact of the imported stock-strength trace-element salts being misrepresented as final G_PER_L concentrations.
