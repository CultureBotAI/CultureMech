# YAML Record Review: pyrococcus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml
- Started UTC: 2026-09-24T23:41:12Z
- Finished UTC: 2026-09-24T23:42:39Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml` as a generated `MediaRecipe` for `CultureMech:008197`, label `pyrococcus_medium`, with `media_term` `TOGO:M1641`.

The single maintained owner is `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml`. This generated artifact was built on 2026-08-06 and predates a 2026-09-02 normalized repair that collapsed one duplicate water row.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml` | Passed; printed `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml --out /private/tmp/pyrococcus_medium__3fe52a8c.strict.tsv --workers 1 --quiet` | Passed; 1 TSV line, header only, 0 error rows. |
| Internal references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were configured for this record. |
| Term grounding | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyrococcus_medium__3fe52a8c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the available validator covers standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

TOGO M1641 and NBRC Medium 844 both identify `Pyrococcus Medium`, and the TOGO payload's `original_media_id` and `src_url` agree with the normalized record's NBRC source fields.

An ignored-file-inclusive exact search across `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports/yaml_record_review` for `TOGO_M1641_Pyrococcus_Medium`, `TOGO:M1641`, `togomedium.org/medium/M1641`, `NBRC_M844`, `NBRCMediumDetailServlet?NO=844`, `CultureMech:008197`, `mediadive.solution:6108`, `mediadive.solution:6109`, and the full `3fe52a8c1a10f55e3ed0186b1abbc3de410623f5574a56c3d324eb47bd47424c` fingerprint found the expected maintained TOGO owner, this generated artifact, the normalized solution index rows for 6108 and 6109, and separate global solution files for the two MediaDive solution IDs. The search found no direct NBRC Medium 844 owner.

## Evidence

The live TOGO M1641 API and live NBRC 844 page agree on the top-level formulation: 1 L distilled water, 1 g yeast extract, 13.5 g NaCl, 1.5 g `CaCl2*2H2O`, 1 mg resazurin, 10.8 g `MgCl2*6H2O`, 0.25 g `Na2S*9H2O`, 4 g `Na2SO4`, 30 g sulfur powder, 5 g tryptone, 10 ml `Solution 1`, and 10 ml `Solution 2`.

The same sources define `Solution 1` as a 1 L stock with 7 g KCl, 2 g NaHCO3, 1 g NaBr, and distilled water, and define `Solution 2` as a 1 L stock with 0.3 g H3BO3, 0.25 g `SrCl2*6H2O`, and distilled water. The reviewed YAML flattens all five stock salts into top-level final-medium ingredient rows at their stock concentrations and keeps both 10 ml stock additions only as empty solution shells with `10 G_PER_L`.

The source preparation requires mixing the main ingredients except solutions 1 and 2, sulfur, and sodium sulfide; autoclaving under an N2 atmosphere; sterilizing sulfur separately for 60 min at 105 C on each of 3 successive days; neutralizing sodium sulfide as a 5% solution and autoclaving under N2; filter-sterilizing solutions 1 and 2; and aseptically adding the sterile sulfur, stock solutions, and sodium sulfide before inoculation. No `preparation_steps` preserve that workflow.

## Completeness

Empty optional fields are not defects.

Consequential omissions:

- `Solution 1` and `Solution 2` have no inline composition, and their `mediadive.solution:6108` and `mediadive.solution:6109` links point at unrelated global solution records rather than the NBRC inline stocks.
- The 10 ml stock additions are modeled as `G_PER_L`, not as volume additions.
- The generated record still has the stale `Distilled water: 3.0 G_PER_L` row from summing main, Solution 1, and Solution 2 water.
- The NBRC anaerobic preparation and staged sterilization instructions are absent.

The normalized owner has already collapsed the water row from `3.0` back to `1.0` but still leaves both referenced solutions empty; the generated record needs a fresh regeneration after the remaining owner repairs.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The two NBRC inline stocks were flattened into final-medium ingredients and left as empty solution shells. | NBRC 844/TOGO M1641 add 10 ml each of Solution 1 and Solution 2 to the main 1 L medium. The YAML instead lists KCl, NaHCO3, NaBr, H3BO3, and SrCl2*6H2O at stock strength as main ingredients while `solutions` has two `composition: []` placeholders at `10 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml` |
| Major | The `mediadive.solution:6108` and `mediadive.solution:6109` links are wrong for this NBRC recipe. | The local 6108 file is an FeNa-EDTA/Na2-EDTA solution, and the local 6109 file is an H3BO3/MnCl2/ammonium molybdate solution; neither matches NBRC Solution 1 or Solution 2 for Medium 844. | `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml`; solution-linking import logic |
| Major | Resazurin is inflated 1000-fold. | TOGO M1641 and NBRC 844 specify 1 mg; the YAML records `1 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml` |
| Major | The NBRC preparation workflow is missing. | The source distinguishes main-medium autoclaving under N2, repeated sulfur sterilization, sodium sulfide neutralization and anoxic autoclaving, filter-sterile stock additions, and aseptic anaerobic additions. The YAML has no `preparation_steps`, only a variable N2 ingredient. | `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml` |
| Major | The generated artifact is stale relative to the normalized water repair. | The generated row is `Distilled water: 3.0 G_PER_L`; the maintained owner was repaired on 2026-09-02 to `1.0` after detecting the triple duplicate merge. | Regenerate `data/merge_yaml/merged` from `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml` |
| Minor | Sulfur still carries a legacy MediaIngredientMech identifier. | `Sulfur (powder)` has primary `CHEBI:33403` grounding but still uses `mediaingredientmech_term: MediaIngredientMech:001072`. | `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M1641_Pyrococcus_Medium.yaml`, rehydrate `Solution 1` and `Solution 2` as inline 10 ml stock additions with the exact NBRC/TOGO stock components and their 1 L water rows.

2. Remove the erroneous `mediadive.solution:6108` and `mediadive.solution:6109` groundings from those NBRC inline stocks or replace them with source-local identifiers that cannot collide with unrelated MediaDive solution records.

3. Convert the 1 mg resazurin row to `0.001 G_PER_L`.

4. Add preparation steps for N2 autoclaving, three repeated sulfur sterilizations at 105 C, separate sodium sulfide stock preparation, filter-sterilized stock additions, and aseptic anaerobic addition before inoculation.

5. Regenerate `data/merge_yaml/merged` after the normalized owner is repaired so the generated water row stays at 1 L and the stock salts are no longer emitted as top-level stock-strength ingredients.

6. Refresh sulfur's MediaIngredientMech link to the CHEBI-keyed slot after the primary `CHEBI:33403` grounding.

## Follow-up Checks

- Re-run the focused schema, strict, reference, and term validators on the repaired TOGO owner and regenerated merged YAML.
- Re-run an ignored-file-inclusive exact search for `TOGO:M1641`, `NBRC_M844`, `mediadive.solution:6108`, and `mediadive.solution:6109` to confirm no generated Pyrococcus record still points to the unrelated global solution files.
- Manually compare the regenerated YAML against the live TOGO M1641 payload and NBRC 844 page to confirm the 10 ml stock boundaries, 1 mg resazurin amount, and anaerobic preparation survived.

## Additional Notes

The two global solution records for `mediadive.solution:6108` and `mediadive.solution:6109` are also flagged `incomplete_composition`, but they should not be fixed as part of this Pyrococcus repair. The immediate issue is that NBRC's inline Solution 1/Solution 2 labels were over-grounded to unrelated non-Pyrococcus solution identifiers.
