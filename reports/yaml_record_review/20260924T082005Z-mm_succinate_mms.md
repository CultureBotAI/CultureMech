# YAML Record Review: mm_succinate_mms

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mm_succinate_mms.yaml
- Started UTC: 2026-09-24T08:20:05Z
- Finished UTC: 2026-09-24T08:20:05Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mm_succinate_mms.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:009660`
- Label: `mm_succinate_mms`
- Original label: `MM succinate (MMS)`
- Source grounding: `TOGO:M3220`, labelled `MM succinate (MMS)`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: 5ec5d14bdf40e59090c234552429dba35117a9cd813231c139519cee6e8b1192`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/mm_succinate_mms.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mm_succinate_mms.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mm_succinate_mms.yaml --out /private/tmp/mm_succinate_mms.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mm_succinate_mms.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mm_succinate_mms.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mm_succinate_mms.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches the inspected TOGO API response for medium M3220: both identify `MM succinate (MMS)`.
- The TOGO response has a parent medium paragraph with `Distilled water` 1 L, `MgSO4.7H2O` 0.1 g, `KH2PO4` 2.5 g, `NH4Cl` 1 g, `Na2HPO4` 2.5 g, saturated `CaCl2` 10 ul, saturated `FeSO4` 10 ul, `Succinate` 20 mM, `Ampicillin` 300 ug/ml, `Kanamycin` 10 ug/ml, and `Bauchop & Elsden solution` 1 ml.
- The TOGO response has a separate `Bauchop & Elsden solution` subcomponent that contains 1 L water, eight salt rows, and 51.3 ml concentrated hydrochloric acid.
- The maintained MediaRecipe source was found with an exact `rg --files --no-ignore --hidden` search under `data/normalized_yaml`; ignored files were included.

## Evidence

- The parent source adds `Saturated CaCl2 solution` and `Saturated FeSO4 solution` at 10 ul each. The YAML moved both into `solutions` with empty `composition` arrays and `G_PER_L` units, so the source volumes and semantics were lost.
- The parent source adds 1 ml `Bauchop & Elsden solution`, whose own stock formula belongs in a nested composition. The YAML instead has an empty `Bauchop & Elsden solution` solution row and has flattened the Bauchop and Elsden stock ingredients into top-level ingredients at stock strength.
- `Ampicillin` is 300 ug/ml and `Kanamycin` is 10 ug/ml in the TOGO payload. The YAML has the same numeric values but rewrites the units to `G_PER_L`, producing 1000x too much antibiotic if interpreted literally.
- The generated merged record is stale relative to the maintained normalized source: `data/normalized_yaml/bacterial/mm_succinate_mms.yaml` has an August 20, 2026 `apply_mim_groundings.py` event for the missing Kanamycin CHEBI grounding and a September 2, 2026 `repair_merged_duplicates.py` event that changed duplicated distilled water from the generated `2.0` to `1.0`.

## Completeness

- The record preserves the source identity and several parent ingredient amounts, including the phosphate salts, ammonium chloride, magnesium sulfate heptahydrate, and succinate.
- The nested solution structure is incomplete: all three generated `solutions` entries have empty compositions, and the only defined stock, `Bauchop & Elsden solution`, is flattened into parent ingredients.
- The generated output is incomplete relative to its maintained owner because it lacks the Kanamycin grounding and the September duplicate-water correction.

## Findings

1. **major - TOGO stock-solution additions lost their source volume units and compositions**
   - Evidence: M3220 adds 10 ul saturated `CaCl2`, 10 ul saturated `FeSO4`, and 1 ml `Bauchop & Elsden solution`. The YAML represents those as empty solutions with concentrations of 10, 10, and 1 `G_PER_L`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_succinate_mms.yaml`, via the TOGO importer and `solution-migrator-v1.0`.
2. **major - Bauchop and Elsden stock ingredients were flattened into the final medium**
   - Evidence: TOGO separates the final MM-succinate medium from the `Bauchop & Elsden solution` subcomponent. The YAML places H3BO3, FeSO4.7H2O, ZnSO4.7H2O, CuSO4.5H2O, CoSO4.7H2O, CaCO3, MgSO4, MnSO4.7H2O, and concentrated hydrochloric acid directly in `ingredients`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_succinate_mms.yaml`, via the TOGO importer or solution migration logic.
3. **major - antibiotic units were imported as grams per liter instead of micrograms per milliliter**
   - Evidence: the TOGO response lists `Ampicillin` at 300 ug/ml and `Kanamycin` at 10 ug/ml; the YAML lists 300 `G_PER_L` and 10 `G_PER_L`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_succinate_mms.yaml`, via the TOGO unit mapper.
4. **minor - generated output is stale versus duplicate-merge and Kanamycin grounding repairs**
   - Evidence: the maintained normalized source collapses duplicated distilled water to 1.0 and maps `Kanamycin` to `CHEBI:6104`; the generated record still has 2.0 distilled water and no Kanamycin term.
   - Maintained owner: regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/mm_succinate_mms.yaml`.

## Recommended Edits

1. Rework the TOGO solution importer or migration logic so parent additions of saturated `CaCl2`, saturated `FeSO4`, and `Bauchop & Elsden solution` retain source volume units instead of becoming empty `G_PER_L` stocks.
2. Move the nine `Bauchop & Elsden solution` stock rows out of top-level `ingredients` and into a nested solution composition for the stock that is added at 1 ml per liter.
3. Correct `ug/ml` handling so the two antibiotic rows are preserved or converted to equivalent `G_PER_L` values, 0.3 g/L for Ampicillin and 0.01 g/L for Kanamycin.
4. Regenerate `data/merge_yaml/merged/mm_succinate_mms.yaml` after fixing the normalized source so the duplicate-water repair and Kanamycin grounding are also carried into generated output.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mm_succinate_mms.yaml`.
- Compare the regenerated parent ingredient rows against the TOGO M3220 parent component and keep the Bauchop and Elsden stock rows nested under that solution rather than flattened.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `Saturated CaCl2 solution`, `Saturated FeSO4 solution`, `Bauchop & Elsden solution`, `Ampicillin`, `Kanamycin`, and `Collapsed 2 identical duplicates` against the maintained normalized owner and regenerated merge output.

## Additional Notes

- The generated record predates the August 20, 2026 Kanamycin grounding and the September 2, 2026 duplicate-water repair, but the stock-solution and `ug/ml` conversion problems are still present in the maintained normalized record and need source-level curation.
