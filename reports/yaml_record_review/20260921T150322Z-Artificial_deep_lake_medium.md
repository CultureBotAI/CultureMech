# YAML Record Review: artificial_deep_lake_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Artificial_deep_lake_medium.yaml
- Started UTC: 2026-09-21T15:01:41Z
- Finished UTC: 2026-09-21T15:03:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/Artificial_deep_lake_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml` |
| Stable ID | `CultureMech:008960` |
| Name | `artificial_deep_lake_medium` |
| Original name | `Artificial deep lake medium` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_deep_lake_medium` with fingerprint `70f819f1f49edac4b291e122b26817909cc804233990027ead7a2047ffc07d77` |

The reviewed file is a generated merge product. Future corrections belong in the normalized owner above, the TOGO import path if the same parse error recurs on reimport, or the solution-migration/duplicate-cleanup scripts that created the incorrect stock boundary; the merged YAML should be regenerated, not hand-edited.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Artificial_deep_lake_medium.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Artificial_deep_lake_medium.yaml --out /private/tmp/Artificial_deep_lake_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Artificial_deep_lake_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Artificial_deep_lake_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** The record is grounded to `TOGO:M2376` as `Artificial deep lake medium`; the TOGO API response for `M2376` and the cited ATCC PDF both identify the formulation as `ATCC medium: 1682 Artificial deep lake medium`.
- **The direct basal salts and solids are the right chemical forms.** ATCC Medium 1682 lists NaCl, `MgCl2 . 6H2O`, `MgSO4 . 7H2O`, KCl, `CaCl2 . 2H2O`, sodium succinate, yeast extract, Noble agar, a 10 mL Vitamin Solution addition, and 990 mL distilled water. The generated record preserves the salt, succinate, yeast-extract, and agar amounts as one-liter recipe amounts.
- **The `SOLID_AGAR` physical state is source-supported.** ATCC includes 15.0 g Noble agar in the formulation.
- **The direct vitamin and water ingredients do not preserve source identity.** ATCC places biotin, cyanocobalamin, thiamine HCl, and 1.0 L distilled water under the separately prepared Vitamin Solution; the generated medium flattens those stock ingredients into the final recipe and merges stock water into the basal water amount.

## Evidence

- The TOGO API returned `gm` `http://togomedium.org/medium/M2376`, `name` `Artificial deep lake medium`, `src_url` pointing to the ATCC PDF, and `ph` `7.4`; this agrees with `media_term.id: TOGO:M2376` and the imported source note.
- The ATCC PDF reached by the TOGO `src_url` returned as `ATCC Medium 1682.pdf` and its extracted text matches the TOGO component list, including a 10.0 mL Vitamin Solution added to the basal medium and a separate Vitamin Solution made from 0.1 g each of biotin, cyanocobalamin, and thiamine HCl in 1.0 L distilled water.
- The ATCC preparation paragraph supports four currently missing procedural claims: adjust the final medium to pH 7.4, autoclave the basal medium at 121 C for 15 minutes, cool to 50 C before aseptic vitamin addition, and filter-sterilize the vitamin stock before adding it aseptically.
- `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml` is not the ATCC Medium 1682 Vitamin Solution. It is a generic MediaDive solution record with a 100 mL preparation note and a different parsed composition, including `Biotin` at `2000.0 G_PER_L`; linking this record to the ATCC-specific 10 mL stock addition over-scopes `mediadive.solution:6241`.

## Completeness

- The medium source is recoverable from the `notes` URL and `TOGO:M2376`; no structured `references` or `source_data` block is present, but the existing source note is enough to recover the imported formulation.
- No `target_organisms`, `growth_metrics`, `incubation`, or strain-specific evidence is present. That is acceptable for this source-only import: the inspected TOGO/ATCC formulation page does not assert a growth outcome for a named organism or strain.
- The pH and preparation omission is consequential because it changes the recipe a user would follow: the present record has no final pH, autoclave, cooling, aseptic-addition, or filter-sterilization instructions.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*Artificial_deep_lake_medium.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Vitamin Solution stock boundary was flattened into the final medium. The final record carries direct `Biotin`, `Thiamine . HCl`, and `Cyanocobalamin` ingredients at `0.1 G_PER_L`, and a `Distilled water` amount of `991.0 G_PER_L` with a duplicate-merge note. | ATCC and TOGO separate the stock from the final medium: the final medium has 990 mL distilled water plus 10 mL Vitamin Solution, while the 0.1 g vitamins and 1.0 L water belong inside `Vitamin Solution`. Adding 990 mL to 1.0 L and rewriting the sum as 991 g/L is dimensionally wrong. | `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml`; likely also the TOGO import or `scripts/cleanup_media_quality.py` duplicate-water path. |
| Major | The final-medium stock addition has the wrong unit. | ATCC and TOGO specify `Vitamin Solution` as `10.0 ml`; the record has `solutions[0].concentration` as `10 G_PER_L`. | `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml`; likely also `scripts/migrate_solutions_from_ingredients.py`. |
| Major | The solution term points to the wrong stock record. | The linked `mediadive.solution:6241` stock record prepares an unrelated generic solution to 100 mL and has a materially different composition from ATCC Medium 1682's Vitamin Solution. | `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml`; likely also `scripts/migrate_solutions_from_ingredients.py`. |
| Major | Required pH and sterilization/preparation details from ATCC are missing. | The ATCC source gives final pH 7.4, basal-medium autoclaving at 121 C for 15 minutes, cooling to 50 C before aseptic vitamin addition, and filter sterilization of the vitamin stock. None of those instructions is represented in the generated or normalized YAML. | `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml`. |

No blockers found: the YAML is valid, the generated record has the intended `CultureMech:008960` identity, and the TOGO grounding points to the right source medium.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml`, preserve the ATCC stock boundary:
   - keep the final-medium salts, sodium succinate, yeast extract, Noble agar, and 990 mL distilled water as direct ingredients;
   - remove the direct final-medium `Biotin`, `Thiamine . HCl`, and `Cyanocobalamin` ingredients;
   - represent the final Vitamin Solution addition as 10 mL, not 10 g/L.
2. Replace the `mediadive.solution:6241` descriptor with a stock solution that actually denotes the ATCC Medium 1682 Vitamin Solution, or represent this TOGO subcomponent without asserting an unrelated MediaDive solution identifier.
3. Represent the Vitamin Solution composition as a stock made from 0.1 g biotin, 0.1 g cyanocobalamin, 0.1 g thiamine HCl, and 1.0 L distilled water.
4. Add source-scoped preparation detail for final pH 7.4, basal-medium autoclaving at 121 C for 15 minutes, cooling to 50 C, aseptic vitamin addition, and filter sterilization of the vitamin stock.
5. Add or refine an importer or normalization regression check that keeps TOGO subcomponent ingredients from being merged into direct final-medium ingredients, then regenerate `data/merge_yaml/merged/Artificial_deep_lake_medium.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml` after the normalized edit.
- Re-run `just validate-references data/normalized_yaml/bacterial/artificial_deep_lake_medium.yaml` after any new or changed stock-solution reference.
- Regenerate or verify the merge layer and confirm that `data/merge_yaml/merged/Artificial_deep_lake_medium.yaml` no longer contains direct final-medium entries for the three vitamin compounds or a `991.0 G_PER_L` distilled-water amount.
- Manually compare the regenerated generated YAML against TOGO `M2376` or the ATCC PDF and confirm that the basal medium, stock, and preparation instructions remain separated.

## Additional Notes

- `find data/normalized_yaml -name mediadive_6241_Vitamin_solution.yaml -print` located the linked solution record at `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml`.
- An exact gitignore-independent search for `TOGO:M2376`, `M2376`, and `CultureMech:008960` across `data/normalized_yaml` and `data/merge_yaml` found only the normalized owner and generated merge record for this stable ID/source pair.
- Exact searches in `scripts` and `src` found `solution-migrator-v1.0` in `scripts/migrate_solutions_from_ingredients.py` and `data-quality-cleanup-v1.0` in `scripts/cleanup_media_quality.py`; those are plausible script owners for the incorrect stock migration and duplicate water merge history events.
