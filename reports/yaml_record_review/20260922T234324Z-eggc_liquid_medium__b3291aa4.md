# YAML Record Review: EGGC LIQUID MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml
- Started UTC: 2026-09-22T23:38:00Z
- Finished UTC: 2026-09-22T23:43:24Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:002220`
- Name: `eggc_liquid_medium`
- Original label: `EGGC LIQUID MEDIUM`
- Category: `bacterial`
- Medium term: `mediadive.medium:J1036` / `JCM Medium J1036`
- Generated status: generated merge record with fingerprint `b3291aa434832905cbb6d1b010a09c77f15a6e8d89ef3d061b0fba35dea3ac42`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml`

The merge record adds only the `merge_recipes.py` history entry, `merge_fingerprint`, and `merged_from` metadata on top of the maintained normalized record.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml --out /private/tmp/eggc_liquid_medium__b3291aa4.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes JCM Medium 1036, `EGGC LIQUID MEDIUM`. The JCM page labels `1036 EGGC LIQUID MEDIUM`, MediaDive resolves `J1036` with the same name and JCM source URL, and TOGO M1100 independently identifies the source as `JCM_M1036`.

The high-level type fields are consistent with the source: this is a complex, undefined, liquid bacterial recipe with pH 7.0-7.2. The record's `ph_value: 7.1` is the midpoint of the JCM range.

The CHEBI groundings for glucose, sodium acetate, calcium carbonate, ammonium sulfate, magnesium sulfate heptahydrate, potassium chloride, calcium chloride dihydrate, iron trichloride hexahydrate, the named vitamins, and biotin are chemically aligned. The `Casamino acids` mixture and `Na2HPO4-NaH2PO4 buffer` correctly remain ungrounded to a single CHEBI entity.

## Evidence

The main low-mass ingredients match MediaDive's final-volume conversion for the main JCM recipe: 0.6 g glucose, 0.3 g sodium acetate, 0.3 g Casamino acids, and 0.02 g calcium carbonate are stored as 0.5923, 0.29615, 0.29615, and 0.0197433 g/L after MediaDive's 1013 ml final-volume calculation.

The source formulation is not a flat list, however:

- The main recipe adds 5.0 ml Solution A and 8.0 ml Solution B to 1.0 L distilled water.
- Solution A is a 1 L stock containing 20.0 g ammonium sulfate, 10.0 g magnesium sulfate heptahydrate, 10.0 g potassium chloride, and 4.0 g calcium chloride dihydrate.
- Solution B is mixed and filter-sterilized just before addition from 2.0 ml of 0.5 M phosphate buffer at pH 7.3, 5.0 ml of Vitamins mix solution from JCM Medium 296, and 1.0 ml of FeCl3 solution.
- The FeCl3 solution is a 300 ml stock with 0.15 g ferric chloride hexahydrate and is prepared just before use.
- JCM Medium 296 defines the Vitamins mix solution as a 1 L stock with 20 mg/L each riboflavin, thiamine HCl, nicotinic acid, calcium pantothenate, myo-inositol, p-aminobenzoic acid, and pyridoxine HCl, plus 1 mg/L each folic acid, vitamin B12, and biotin.

The reviewed record promotes every Solution A component, every Vitamins mix component, the phosphate buffer, and the FeCl3 solution to top-level final ingredients at stock strength. Its preparation text mentions Solution B filtering and the FeCl3 preparation boundary, but the ingredient table has no `solutions` array and no rows for the 5 ml Solution A or 8 ml Solution B additions.

## Completeness

The record is incomplete because its nested stock relationships are not represented. Following the flat ingredient table would add ammonium sulfate, magnesium sulfate heptahydrate, potassium chloride, calcium chloride dihydrate, vitamins, phosphate buffer, and ferric chloride at orders of magnitude above the source final concentrations.

No organism-growth claims, strain claims, DOI, PMID, or source snippets are present. Their absence is not a defect for this imported JCM recipe. A `find data/normalized_yaml -name '*eggc_liquid_medium*' -o -name '*EGGC*' -o -name '*Eggc*'` search, which includes ignored files, found adjacent TOGO/JCM and KOMODO EGGC records, but none changes the JCM J1036 identity of this direct MediaDive record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Solution A is flattened at stock strength instead of modeled as a 5 ml/L stock addition. | JCM J1036 and MediaDive J1036 add `5.0 ml` of Solution A to the main recipe; the reviewed record lists 20 g/L ammonium sulfate, 10 g/L magnesium sulfate heptahydrate, 10 g/L potassium chloride, and 4 g/L calcium chloride dihydrate as final ingredients. | `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml` |
| major | Solution B and its nested Vitamins mix and FeCl3 stocks are flattened at stock strength. | JCM J1036 adds 8 ml Solution B made from 2 ml phosphate buffer, 5 ml Vitamins mix, and 1 ml FeCl3 solution; the reviewed record lists the buffer, vitamins, and FeCl3 as final g/L ingredients. | `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml` |
| major | The structured record has no `solutions` array despite source-mandated stock boundaries. | MediaDive exposes separate records for `Solution A`, `Solution B`, `Vitamins mix solution`, and `FeCl3 solution 0.5 g/L`; the reviewed YAML has only a flat `ingredients` list. | `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml` |
| minor | The Casamino acids vendor attribute is dropped. | JCM names `Casamino acids (BD-Difco)`; the reviewed record stores only `Casamino acids`. | `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/eggc_liquid_medium.yaml`, restore explicit Solution A, Solution B, Vitamins mix solution, and FeCl3 solution records with their source volumes and stock compositions.
2. Replace stock-strength top-level ingredient rows with only the four main base ingredients plus 5 ml Solution A, 8 ml Solution B, and 1 L distilled water, or with final calculated contributions that keep their stock provenance unambiguous.
3. Attach JCM J1036 and JCM J296 source notes narrowly to Solution B and Vitamins mix rows so readers can see why the J1036 record depends on the Medium 296 vitamin stock.
4. Preserve the `BD-Difco` attribute for Casamino acids in a source note or structured attribute field.
5. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/eggc_liquid_medium__b3291aa4.yaml`.
2. Reopen JCM `GRMD=1036`, MediaDive `J1036`, and JCM `GRMD=296`; verify Solution A is a 5 ml/L addition, Solution B is an 8 ml/L filter-sterilized addition, Vitamins mix comes from Medium 296, and the FeCl3 stock remains 0.15 g in 300 ml water.
3. Manually inspect the rendered medium page to confirm stock compositions are displayed separately from final-medium ingredients.

## Additional Notes

- TOGO M1100 is the TOGO snapshot of the same JCM J1036 source but has its own flattened artifacts and was not used as the reviewed record's owner.
- `data/merge_yaml/merged/eggc_medium__a1774e77.yaml` is the related solid EGGC Medium from JCM J296 and is a separate generated record.
