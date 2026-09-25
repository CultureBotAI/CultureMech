# YAML Record Review: Low-Salt Luria-Broth (LSLB)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_salt_luria_broth_lslb.yaml`
- Started UTC: `2026-09-23T20:19:18Z`
- Finished UTC: `2026-09-23T20:20:11Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:009438`
- `name`: `low_salt_luria_broth_lslb`
- `original_name`: `Low-Salt Luria-Broth (LSLB)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2900`
- `merge_fingerprint`: `db4e9e8387a58879a5939b46c3f5347640f855d78cf02af3b18c829774f02e2d`
- `merged_from`: `low_salt_luria_broth_lslb`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_salt_luria_broth_lslb.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:009438`, `TOGO:M2900`, `Source: TOGO, ID: M2900`, `low_salt_luria_broth_lslb`, and the merge fingerprint found one maintained owner, `data/normalized_yaml/bacterial/low_salt_luria_broth_lslb.yaml`, plus this generated record. No duplicate generated recipe or archived conflicting owner was found in the checked paths.
- The generated record merges exactly one owner on the recorded fingerprint and preserves the TOGO medium ID.
- The generated record is stale relative to its maintained owner: the owner has a 2026-09-12 `repair_togo_m2900_lslb_score15.py` event that corrected the water row, NaCl identity, yeast-extract grounding, composition type, incubation condition, and a source-backed dissolve step.
- TOGO M2900 confirms the maintained owner values: `Low-Salt Luria-Broth (LSLB)`, 1 L distilled water, 5 g `NaCl (VWR, X190-1KG)`, 5 g `Yeast Extract (BD, 212750)`, and 10 g `Tryptone (VWR, J859-500G)`.

## Evidence

- TOGO M2900's component block lists four rows: `Distilled water` with 1 L, `NaCl (VWR, X190-1KG)` with 5 g, `Yeast Extract (BD, 212750)` with 5 g, and `Tryptone (VWR, J859-500G)` with 10 g.
- TOGO M2900's comments state that LSLB broth was prepared from 10 g tryptone, 5 g yeast extract, and 5 g NaCl per liter of water.
- TOGO M2900 also states that liquid LSLB cultures were incubated at 28 C with rotational shaking at 225 rpm.
- The generated record predates the owner repair and still stores `Distilled water` as `1 G_PER_L`, leaves `NaCl (VWR, X190-1KG)` without a CHEBI `term`, keeps yeast extract ungrounded, keeps `composition_type: UNDEFINED`, and lacks `temperature_value`, `aeration`, references, and the dissolve preparation step present in the maintained owner.

## Completeness

- The generated record preserves all four TOGO ingredient rows and the imported mass values for NaCl, yeast extract, and tryptone.
- The generated `Distilled water` amount and unit are wrong for TOGO M2900 because the source says 1 L and the generated row says 1 g/L.
- The generated record omits source-supported incubation context: 28 C and rotational shaking at 225 rpm.
- The generated record omits the maintained owner's source-backed preparation step and explicit TOGO references.

## Findings

1. The generated record is stale and still carries the pre-repair water unit artifact.
   - Evidence: TOGO M2900 lists `Distilled water` with 1 L, and the maintained owner corrected it to 1000 `ML_PER_L` on 2026-09-12; the generated record still says 1 `G_PER_L`.
   - Impact: consumers see water as a mass concentration rather than the final per-liter solvent volume.

2. Source-supported NaCl and yeast-extract groundings have not propagated.
   - Evidence: the maintained owner normalizes `NaCl` to `CHEBI:26710` and grounds yeast extract to `FOODON:03315426`; the generated record still leaves `NaCl (VWR, X190-1KG)` and `Yeast Extract (BD, 212750)` ungrounded.
   - Impact: generated artifacts miss the curated ontology links needed for ingredient search and grouping.

3. TOGO incubation and preparation context has not propagated.
   - Evidence: TOGO says liquid LSLB cultures were incubated at 28 C with rotational shaking at 225 rpm and prepared from the three dry ingredients per liter of water; the generated record lacks `temperature_value`, `aeration`, and `preparation_steps` even though the maintained owner now carries them.
   - Impact: the generated record under-represents source preparation and condition facts that are already curated.

## Recommended Edits

1. Rebuild `data/merge_yaml/merged/low_salt_luria_broth_lslb.yaml` from `data/normalized_yaml/bacterial/low_salt_luria_broth_lslb.yaml` so the 2026-09-12 M2900 repair propagates.
2. Confirm the rebuilt record has 1000 `ML_PER_L` water, normalized `NaCl`, grounded yeast extract, `composition_type: SEMI_DEFINED`, `temperature_value: 28.0`, `aeration: rotational shaking at 225 rpm`, the TOGO references, and the dissolve preparation step.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Re-fetch `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2900` and verify that the rebuilt generated YAML still matches the current TOGO component and comment rows.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
