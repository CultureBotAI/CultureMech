# YAML Record Review: medium_for_nautilia_profundicola_baa_1463

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml
- Started UTC: 2026-09-24T01:44:34Z
- Finished UTC: 2026-09-24T01:45:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009122` |
| Label | `medium_for_nautilia_profundicola_baa_1463` |
| Original name | `Medium for Nautilia profundicola BAA-1463` |
| Category | `bacterial` |
| Source accession | `TOGO:M2553` |
| Maintained owner | `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml` |
| Generated status | Generated merge from one TOGO import, with `merge_fingerprint` `83d3c9421ea9bc9241916a5d09ffc9fa1db8db4ce6520737be54d593734c4316` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml --out /private/tmp/medium_for_nautilia_profundicola_baa_1463.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The generated record has the correct source identity for TOGO `M2553`: the TOGO API names `Medium for Nautilia profundicola BAA-1463`, links the ATCC PDF URL preserved in `notes`, and reports the final pH range as 7.0 to 7.5.
- ATCC Medium 2686 carries the same `Medium for Nautilia profundicola BAA-1463` title, so the TOGO layer and the original ATCC PDF agree on the medium identity.
- An exact, gitignore-independent search that included ignored and hidden files for `TOGO:M2553`, `M2553`, the normalized slug, the original label, and the ATCC PDF URL found only the generated record and its direct normalized owner.
- The generated record is stale relative to `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml`: the normalized owner has a 2026-09-02 duplicate-water repair and keeps `Distilled water` at 1.0, while the generated merge still ends at the 2026-08-06 merge event and still lists `Distilled water` as 3.0 `G_PER_L`.

## Evidence

Supported claims:

- The direct ATCC/TOGO main-medium quantities for NaCl 20 g/l, MgCl2 . 6H2O 3 g/l, CaCl2 . 2H2O 0.15 g/l, KCl 0.5 g/l, NH4Cl 0.25 g/l, KH2PO4 0.2 g/l, Resazurin 0.015 g/l, So(Sulfur Powder) 5 g/l, and DI WATER 1 l are present in the TOGO M2553 API payload and the ATCC PDF.
- TOGO and ATCC both list NaHCO3 as 30 ml of a 1 M solution, Na2S as 0.2 M, and three 1 ml additions of `Trace Elements (ATCC)`, `Selenite-tungstate`, and `Vitamins (ATCC)`.
- The source explicitly gives the 80:20 H2/CO2 headspace, final pH adjustment to 7.0 - 7.5 with 2m HCl, and a formate option at final 10 to 20 mM for increased growth rate.

Unsupported or over-scoped claims:

- The YAML flattens the `Trace Elements (ATCC)`, `Selenite-tungstate`, and `Vitamins (ATCC)` stock formulae into direct final-medium ingredients, and assigns the stock masses as final `G_PER_L` values. The source says the final medium receives each stock at 1 ml/l.
- The existing `solutions` entries have the wrong shape: `NaHCO3 (1M solution)` and `Trace Elements (ATCC)` use `G_PER_L` even though the source gives 30 ml/l and 1 ml/l additions, and the two entries have empty `composition` arrays and placeholder `Unknown solution` names.
- `Selenite-tungstate` and `Vitamins (ATCC)` remain as direct 1 `G_PER_L` ingredients even though the source makes them 1 ml/l stock additions with their own 1 l formulae.
- `2m HCl`, `Carbon dioxide gas`, and `Hydrogen gas` are modeled as variable ingredients. The source uses them as pH-adjustment and headspace instructions, not as directly measured formulation components.
- Hydrated stock salts are grounded too broadly in several rows: `Na2MoO4 . H2O` is linked to anhydrous sodium molybdate, `CoCl2 . 6H2O` to cobalt dichloride, `NiCl2 . 6H2O` to nickel dichloride, and `Na2SeO3 . 5H2O` to disodium selenite.

## Completeness

- The source pH range 7.0 to 7.5 is missing from the generated record.
- The headspace, pH adjustment, and formate note are missing as preparation, atmosphere, or variant facts.
- The medium is classified as `COMPLEX` and `UNDEFINED`, but the inspected ATCC and TOGO source describes salts plus fully specified trace, selenite-tungstate, and vitamin stock formulae.
- `target_organisms` and organism-specific growth evidence are empty. That is acceptable for this pass because the ATCC medium name mentions BAA-1463 but the inspected formulation PDF does not provide a measured growth assertion beyond the recipe title.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three local stock recipes were flattened into final-medium ingredient rows at stock concentrations. | TOGO/ATCC add `Trace Elements (ATCC)`, `Selenite-tungstate`, and `Vitamins (ATCC)` at 1 ml/l each; their Zn, Mn, B, Co, Cu, Ni, Mo, Se, W, NaOH, and vitamin rows are separate 1 l stock formulae. | `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml`; if the defect still exists in new imports, repair `src/culturemech/import/togo_importer.py`. |
| Major | Solution additions have wrong units and incomplete stock representation. | The source gives 30 ml/l of 1 M NaHCO3 and 1 ml/l of Trace Elements, Selenite-tungstate, and Vitamins; the YAML stores NaHCO3 and Trace Elements as `G_PER_L` solution entries with empty `composition`, and leaves Selenite-tungstate and Vitamins as direct 1 `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml`; TOGO importer stock extraction if source-owned. |
| Major | Preparation and condition claims are missing or are stored as pseudo-ingredients. | ATCC/TOGO state the 80:20 H2/CO2 headspace, final pH 7.0 - 7.5 adjustment with 2m HCl, and optional formate at 10 to 20 mM. The YAML has no pH field or preparation step and represents HCl and both gases as variable ingredients. | `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml`. |
| Major | Several hydrated compounds are not grounded to exact hydrated CHEBI terms. | The YAML grounds `Na2MoO4 . H2O`, `CoCl2 . 6H2O`, `NiCl2 . 6H2O`, and `Na2SeO3 . 5H2O` to anhydrous or hydration-unspecified CHEBI classes. | `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml`, followed by MediaIngredientMech enrichment. |
| Major | The generated merge is stale relative to its normalized owner. | The owner has a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` event and 1.0 `G_PER_L` for the remaining `Distilled water` row; the generated merge lacks that event and still has 3.0 `G_PER_L`. | Regenerate `data/merge_yaml/merged/medium_for_nautilia_profundicola_baa_1463.yaml` from `data/normalized_yaml/bacterial/medium_for_nautilia_profundicola_baa_1463.yaml` after normalized curation. |

## Recommended Edits

1. Rebuild the normalized TOGO M2553 record so direct ingredients contain only true main-recipe ingredients and all local ATCC stock additions are represented as `solutions` with `ML_PER_L` doses.
2. Preserve `Trace Elements (ATCC)`, `Selenite-tungstate`, and `Vitamins (ATCC)` as complete local stock formulae, including their one-liter water bases and their stock-specific pH or preparation notes.
3. Move 80:20 H2/CO2 into an atmosphere or preparation field, add the 7.0 - 7.5 pH range with its 2m HCl adjustment, and retain the 10 to 20 mM formate option as an optional variant or discussion item rather than a direct ingredient.
4. Reground hydrated Mo, Co, Ni, and Se salts to exact hydrated terms where OBO has exact terms; otherwise leave them explicit and ungrounded rather than linking them to anhydrous classes.
5. Reclassify the medium as defined after the stock boundaries are represented accurately.
6. Regenerate the merged YAML and derived pages from the normalized record so the 2026-09-02 duplicate-water repair is no longer dropped.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the normalized owner and the regenerated merge.
- Inspect TOGO M2553 again and verify the final recipe has exactly four solution additions: 30 ml/l NaHCO3 (1M solution) and 1 ml/l each of Trace Elements, Selenite-tungstate, and Vitamins.
- Verify that stock constituent rows for Zn, Mn, B, Co, Cu, Ni, Mo, Se, W, NaOH, and vitamins no longer appear as direct final-medium ingredient rows.
- Diff the regenerated merge against the normalized owner and confirm the only generated-only fields are the merge event, `merge_fingerprint`, and `merged_from`.

## Additional Notes

- A similar `nautilia_profundicola_medium` record exists, but the exact M2553 identity search did not find another `TOGO:M2553` record. The similarly named file is a different TOGO import and was not treated as a duplicate of this BAA-1463 ATCC medium.
- The broad TOGO importer search produced too much output to inspect and was not used for absence or duplicate claims; the identity claim above relies on the exact, ignored-inclusive record search.
